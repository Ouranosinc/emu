from pywps import Process, LiteralInput, LiteralOutput, OGCUNIT, UOM, ComplexInput
from pywps import Format, FORMATS
import json
import logging
LOGGER = logging.getLogger("PYWPS")


class DockerApp(Process):
    def __init__(self):
        inputs = [
            LiteralInput('dockerim_name', 'Docker image name', data_type='string'),
            LiteralInput('registry_url', 'Docker image registry url', data_type='string'),
            LiteralInput('dockerim_version', 'Docker image version', data_type = 'string'),
            ComplexInput('input_data', 'all parameters need for the app in json format', supported_formats=[Format('application/json')])
        ]
        outputs = [
            LiteralOutput('output', 'Path to output', data_type='string')]

        super(DockerApp, self).__init__(
            self._handler,
            identifier='dockerapp',
            title='Docker App',
            version='0.1',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        LOGGER.info("run docker app")

        dockerim_version = request.inputs['dockerim_version'][0].data
        dockerim_name = request.inputs['dockerim_name'][0].data
        input_data = request.inputs['input_data'][0].data
        input_data = json.loads(input_data)
        registry_url = request.inputs['registry_url'][0].data

        from pywps.processing.celery_joblauncher import Req
        req = Req(_b=None, _url=registry_url, _imname=dockerim_name, _ver=dockerim_version, _indata=input_data)
        req_json = req.__dict__

        return req_json
