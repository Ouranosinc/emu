from pywps import Process, LiteralInput, LiteralOutput, OGCUNIT, UOM
import json

import logging
LOGGER = logging.getLogger("PYWPS")


class HelloDocker(Process):
    def __init__(self):
        inputs = [
            LiteralInput('dockerim_name', 'Docker image name', data_type='string'),
            LiteralInput('registry_url', 'Docker image registry url', data_type='string'),
            LiteralInput('dockerim_version', 'Docker image version', data_type='string'),
            LiteralInput('queue_name', 'Name of celery queue to send the request', data_type='string'),
            LiteralInput('first_name', 'first parameter (app specific)', data_type='string'),
            LiteralInput('second_name', 'second parameter (app specific)', data_type='string')
        ]
        outputs = [
            LiteralOutput('output', 'Path to output', data_type='string')]

        super(HelloDocker, self).__init__(
            self._handler,
            identifier='hellodocker',
            title='Hello Docker',
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
        queue_name = request.inputs['queue_name'][0].data

        first_name = request.inputs['first_name'][0].data
        second_name = request.inputs['second_name'][0].data
        input_data = {'first_name': first_name,
                      'second_name': second_name}

        registry_url = request.inputs['registry_url'][0].data

        from pywps.processing.celery_joblauncher import Req
        req = Req(_b=None,
                  _url=registry_url,
                  _imname=dockerim_name,
                  _ver=dockerim_version,
                  queue_name=queue_name,
                  _indata=input_data)

        uuid = self.uuid
        req.volume_mapping = {'/tasks/{uuid}/status'.format(uuid=uuid): '/status',
                              '/tasks/{uuid}/outputs'.format(uuid=uuid): '/outputs',
                              '/tasks/{uuid}/inputs'.format(uuid=uuid): '/inputs'}

        req_json = req.__dict__
        return req_json

