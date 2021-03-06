import pytest

from pywps import Service

from emu.tests.common import client_for, assert_response_success
from emu.processes.wps_inout import InOut


@pytest.mark.skip(reason="fix default values in pywps")
def test_wps_inout():
    client = client_for(Service(processes=[InOut()]))
    datainputs = "string=onetwothree;int=7;float=2.0;boolean=0"
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0', identifier='inout',
        datainputs=datainputs)
    print resp.data
    assert_response_success(resp)
