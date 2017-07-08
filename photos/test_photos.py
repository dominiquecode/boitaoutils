from easygui import diropenbox
import pytest
from .outils import get_folder


# Create your tests here.
class TestPhotos(object):

    def test_get_folder(self):

        # folders = {'source': '/volumes/photo/iphone', 'destination': '/volumes/photo'}
        # folder = diropenbox(folders.get('source'))
        folder = get_folder()
        print(folder)

        assert folder is not None
