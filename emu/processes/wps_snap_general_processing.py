from pywps import Process, LiteralInput, LiteralOutput, OGCUNIT, UOM

import logging
LOGGER = logging.getLogger("PYWPS")


class SnapGeneralProcessing(Process):

    dockerim_name = 'docker-registry.crim.ca/ogc/debian8-snap5-ogc-processingt'
    registry_url = 'docker-registry.crim.ca'
    dockerim_version = 'v1'

    def __init__(self):
        inputs = [
            LiteralInput('input_snap_graph_path', 'Chemin du fichier xml du graphe', data_type='string'),
            LiteralInput('output_directory', 'Chemin de sortie du graphe edite', data_type='string'),
            LiteralInput('Read.file', 'Chemin de l image d entree pour le noeud Read', data_type='string'),
            LiteralInput('Write.file', 'Chemin de sortie de l image filtree pour le noeud Write', data_type='string'),
            LiteralInput('Write.formatName', 'Format de sortie', data_type='string'),
            LiteralInput('Polarimetric-Speckle-Filter.filter', 'Nom du filtre dans snap', data_type='string', min_occurs=0),
            LiteralInput('Polarimetric-Speckle-Filter.numLooksStr', 'Le nombre de vues pour l estimation de l ecart-type du speckle', data_type='string', min_occurs=0),
            LiteralInput('Polarimetric-Speckle-Filter.windowSize', 'Grandeur du filtre', data_type='string', min_occurs=0),
        ]
        outputs = [
            LiteralOutput('output', 'Path to output', data_type='string')
        ]

        super(SnapGeneralProcessing, self).__init__(
            self._handler,
            identifier='snap_general_processing',
            title='Snap General Processing',
            version='1',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("run snap_general_processing")

        input_data_dict = {'process_id': 'snap_general_processing'}

        for lit_input in self.inputs:
            identifier = lit_input.identifier
            if identifier in request.inputs.keys():
                input_data_dict[identifier] = request.inputs[identifier][0].data

        from pywps.processing.celery_joblauncher import Req
        req = Req(_b=None,
                  _url=self.registry_url,
                  _imname=self.dockerim_name,
                  _ver=self.dockerim_version,
                  _indata=input_data_dict)

        req.param_as_envar = False  # Set false to not set param as environment variables
        req.volume_mapping = {'/tmp/demo/data': '/data',
                              '/tmp/demo/outputs': '/outputs',
                              '/tmp/demo/inputs': '/inputs'}

        req_json = req.__dict__
        return req_json

