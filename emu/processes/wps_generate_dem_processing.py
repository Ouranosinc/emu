from pywps import Process, LiteralInput, LiteralOutput, OGCUNIT, UOM

import logging
LOGGER = logging.getLogger("PYWPS")


class GenerateDemProcessing(Process):

    dockerim_name = 'docker-registry.crim.ca/ogc/debian8-snap5-ogc-processingt'
    registry_url = 'docker-registry.crim.ca'
    dockerim_version = 'v1'

    def __init__(self):
        inputs = [
            LiteralInput('rsat2_product_xml_path', 'rsat2_product_xml_path', data_type='string'),
            LiteralInput('output_directory', 'output_directory', data_type='string'),
            LiteralInput('output_dem_filename', 'output_dem_filename', data_type='string'),
            LiteralInput('download_directory', 'download_directory', data_type='string'),
        ]
        outputs = [
            LiteralOutput('output', 'Path to output', data_type='string')]

        super(GenerateDemProcessing, self).__init__(
            self._handler,
            identifier='generate_dem_processing',
            title='Generate Dem Processing',
            version='1',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("run generate_dem_processing")

        input_data_dict = {'process_id': 'generate_dem_processing'}

        for lit_input in self.inputs:
            identifier = lit_input.identifier
            input_data_dict[identifier] = request.inputs[identifier][0].data

        from pywps.processing.celery_joblauncher import Req
        req = Req(_b=None,
                  _url=self.registry_url,
                  _imname=self.dockerim_name,
                  _ver=self.dockerim_version,
                  _indata=input_data_dict)

        req.param_as_envar = False  # Do not set param as environment variables
        req.volume_mapping = {'/tmp/demo/data': '/data',
                              '/tmp/demo/outputs': '/outputs',
                              '/tmp/demo/inputs': '/inputs'}

        req_json = req.__dict__
        return req_json

