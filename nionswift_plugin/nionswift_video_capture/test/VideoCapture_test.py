import unittest

from nion.utils import Registry

from nionswift_plugin.nionswift_video_capture import VideoCapture


class TestVideoCapture(unittest.TestCase):

    def test_video_device_factory_registered(self) -> None:
        self.assertGreater(len(Registry.get_components_by_type("video_device_factory")), 0)


if __name__ == '__main__':
    unittest.main()
