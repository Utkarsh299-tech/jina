from typing import Dict

import numpy as np

from .. import BaseCrafter
from .helper import _restore_channel_axis, _load_image


class ImageHorizontalFlipper(BaseCrafter):
    """
    :class:`ImageHorizontalFlipper` flips the image horizontally. Flip image in the left/right direction.
    """

    def __init__(self, channel_axis: int = -1, *args, **kwargs):
        """

        :param channel_axis: the axis id of the color channel, ``-1`` indicates the color channel info at the last axis
        """
        super().__init__(*args, **kwargs)
        self.channel_axis = channel_axis

    def craft(self, blob: 'np.ndarray', *args, **kwargs) -> Dict:
        """
        Horizontally flip the input image array.

        :param blob: the ndarray of the image with the color channel at the last axis
        :return: a chunk dict with the mage
        """
        raw_img = _load_image(blob, self.channel_axis)
        _img = self._flip_image(raw_img)
        img = _restore_channel_axis(_img, self.channel_axis)
        return dict(offset=0, weight=1., blob=img)

    def _flip_image(self, img):
        img = np.array(img).astype('float32')
        return np.fliplr(img)


class ImageVerticalFlipper(BaseCrafter):
    """
    :class:`ImageVerticalFlipper` flips the image vertically. Flip image in the up/down direction.
    """

    def __init__(self, channel_axis: int = -1, *args, **kwargs):
        """

        :param channel_axis: the axis id of the color channel, ``-1`` indicates the color channel info at the last axis
        """
        super().__init__(*args, **kwargs)
        self.channel_axis = channel_axis

    def craft(self, blob: 'np.ndarray', *args, **kwargs) -> Dict:
        """
        Vertically flip the input image array.

        :param blob: the ndarray of the image with the color channel at the last axis
        :return: a chunk dict with the mage
        """
        raw_img = _load_image(blob, self.channel_axis)
        _img = self._flip_image(raw_img)
        img = _restore_channel_axis(_img, self.channel_axis)
        return dict(offset=0, weight=1., blob=img)

    def _flip_image(self, img):
        img = np.array(img).astype('float32')
        return np.flipud(img)
