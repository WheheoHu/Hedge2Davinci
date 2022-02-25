
import importlib.machinery

from pybmd.media_storage import MediaStorage
from pybmd.project_manager import ProjectManager
from typing import TYPE_CHECKING


def load_dynamic(module, path):
    loader = importlib.machinery.ExtensionFileLoader(module, path)
    module = loader.load_module()
    return module


#TODO finish methods
#TODO add docstring to methods

class Bmd:
    """docstring for Bmd."""

    PYLIB = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    APP_NAME = 'Resolve'
    LOCATION = '127.0.0.1'

    local_davinci = None

    def __init__(self):
        self.local_davinci = self.init_davinci()

    def init_davinci(self, davinci_ip=LOCATION):
        bmd_module = load_dynamic(module='fusionscript', path=self.PYLIB)
        return bmd_module.scriptapp(self.APP_NAME, davinci_ip)

    def get_local_davinci(self):
        return self.local_davinci

    def delete_layout_preset(self, preset_name: str) -> bool:
        """Deletes preset named preset_name.

        Args:
            preset_name (string)

        Returns:
            bool: result
        """
        return self.local_davinci.DeleteLayoutPreset(preset_name)

    def export_layout_preset(self, preset_name, preset_file_path) -> bool:
        return self.local_davinci.ExportLayoutPreset(preset_name, preset_file_path)

    def fusion(self):
        # if I find more info about fusion I will finish this function
        return self.local_davinci.Fusion()

    def get_current_page(self) -> str:
        return self.local_davinci.GetCurrentPage()

    def get_media_stroage(self) -> MediaStorage:
        return MediaStorage(self.local_davinci)

    def get_prodect_name(self) -> str:
        return self.local_davinci.GetProdectName()

    def get_project_manager(self) -> ProjectManager:
        return ProjectManager(self.local_davinci)

    def get_version(self) -> list:
        return self.local_davinci.GetVersion()

    def get_version_string(self) -> str:
        return self.local_davinci.GetVersionString()

    def import_layout_preset(self, preset_file_path: str, preset_name: str):
        return self.local_davinci.ImportLayoutPreset(preset_file_path, preset_name)
