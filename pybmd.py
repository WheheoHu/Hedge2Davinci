import importlib.machinery


def load_dynamic(module, path):
    loader = importlib.machinery.ExtensionFileLoader(module, path)
    module = loader.load_module()
    return module


class Bmd():
    """docstring for Bmd."""
    PYLIB = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    APP_NAME='Resolve'
    LOCATION='127.0.0.1'
    
    def __init__(self):
        pass

    def init_davinci(self):
        bmd_module= load_dynamic(module='fusionscript', path=self.PYLIB)
        return bmd_module.scriptapp(self.APP_NAME, self.LOCATION)
