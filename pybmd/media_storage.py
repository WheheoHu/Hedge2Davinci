
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pybmd.bmd import Bmd

class MediaStorage:
    """docstring for MediaStorage."""
    
    media_storage=None
    
    def __init__(self, _local_davinci:'Bmd.local_davinci'):
        """davinci media storage

        Args:
            _local_davinci (Bmd.local_davinci): davinci object
        """        
        self.media_storage=_local_davinci.GetMediaStorage()  

    #TODO Finish this
    