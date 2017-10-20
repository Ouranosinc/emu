from .wps_sleep import Sleep
from .wps_ultimate_question import UltimateQuestion
from .wps_bbox import Box
from .wps_hello import Hello
from .wps_dummy import Dummy
from .wps_wordcounter import WordCounter
from .wps_chomsky import Chomsky
from .wps_inout import InOut
from .wps_docker_app import DockerApp
from .wps_hello_docker import HelloDocker
from .wps_generate_dem_processing import GenerateDemProcessing
from .wps_snap_cp_tc_processing import SnapCpTcProcessing
from .wps_snap_general_processing import SnapGeneralProcessing

processes = [
    UltimateQuestion(),
    Sleep(),
    Box(),
    Hello(),
    Dummy(),
    WordCounter(),
    Chomsky(),
    InOut(),
    DockerApp(),
    HelloDocker(),
    GenerateDemProcessing(),
    SnapCpTcProcessing(),
    SnapGeneralProcessing(),
]
