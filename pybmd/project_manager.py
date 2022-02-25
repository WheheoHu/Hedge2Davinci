from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pybmd.bmd import Bmd


class ProjectManager:

    project_manager = None

    def __init__(self, _local_davinci:'Bmd.local_davinci'):
        self.project_manager = _local_davinci.GetProjectManager()

    #TODO Finish this