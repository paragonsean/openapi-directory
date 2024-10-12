# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CatalogDataProductRenderImageInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, extension_attributes: object=None, height: float=None, label: str=None, resized_height: float=None, resized_width: float=None, url: str=None, width: float=None):
        """CatalogDataProductRenderImageInterface - a model defined in OpenAPI

        :param code: The code of this CatalogDataProductRenderImageInterface.
        :param extension_attributes: The extension_attributes of this CatalogDataProductRenderImageInterface.
        :param height: The height of this CatalogDataProductRenderImageInterface.
        :param label: The label of this CatalogDataProductRenderImageInterface.
        :param resized_height: The resized_height of this CatalogDataProductRenderImageInterface.
        :param resized_width: The resized_width of this CatalogDataProductRenderImageInterface.
        :param url: The url of this CatalogDataProductRenderImageInterface.
        :param width: The width of this CatalogDataProductRenderImageInterface.
        """
        self.openapi_types = {
            'code': str,
            'extension_attributes': object,
            'height': float,
            'label': str,
            'resized_height': float,
            'resized_width': float,
            'url': str,
            'width': float
        }

        self.attribute_map = {
            'code': 'code',
            'extension_attributes': 'extension_attributes',
            'height': 'height',
            'label': 'label',
            'resized_height': 'resized_height',
            'resized_width': 'resized_width',
            'url': 'url',
            'width': 'width'
        }

        self._code = code
        self._extension_attributes = extension_attributes
        self._height = height
        self._label = label
        self._resized_height = resized_height
        self._resized_width = resized_width
        self._url = url
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CatalogDataProductRenderImageInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The catalog-data-product-render-image-interface of this CatalogDataProductRenderImageInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this CatalogDataProductRenderImageInterface.

        Image code

        :return: The code of this CatalogDataProductRenderImageInterface.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CatalogDataProductRenderImageInterface.

        Image code

        :param code: The code of this CatalogDataProductRenderImageInterface.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this CatalogDataProductRenderImageInterface.

        ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRender\\ImageInterface

        :return: The extension_attributes of this CatalogDataProductRenderImageInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this CatalogDataProductRenderImageInterface.

        ExtensionInterface class for @see \\Magento\\Catalog\\Api\\Data\\ProductRender\\ImageInterface

        :param extension_attributes: The extension_attributes of this CatalogDataProductRenderImageInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes

    @property
    def height(self):
        """Gets the height of this CatalogDataProductRenderImageInterface.

        Image height

        :return: The height of this CatalogDataProductRenderImageInterface.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CatalogDataProductRenderImageInterface.

        Image height

        :param height: The height of this CatalogDataProductRenderImageInterface.
        :type height: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")

        self._height = height

    @property
    def label(self):
        """Gets the label of this CatalogDataProductRenderImageInterface.

        Image label

        :return: The label of this CatalogDataProductRenderImageInterface.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CatalogDataProductRenderImageInterface.

        Image label

        :param label: The label of this CatalogDataProductRenderImageInterface.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def resized_height(self):
        """Gets the resized_height of this CatalogDataProductRenderImageInterface.

        Resize height

        :return: The resized_height of this CatalogDataProductRenderImageInterface.
        :rtype: float
        """
        return self._resized_height

    @resized_height.setter
    def resized_height(self, resized_height):
        """Sets the resized_height of this CatalogDataProductRenderImageInterface.

        Resize height

        :param resized_height: The resized_height of this CatalogDataProductRenderImageInterface.
        :type resized_height: float
        """
        if resized_height is None:
            raise ValueError("Invalid value for `resized_height`, must not be `None`")

        self._resized_height = resized_height

    @property
    def resized_width(self):
        """Gets the resized_width of this CatalogDataProductRenderImageInterface.

        Resize width

        :return: The resized_width of this CatalogDataProductRenderImageInterface.
        :rtype: float
        """
        return self._resized_width

    @resized_width.setter
    def resized_width(self, resized_width):
        """Sets the resized_width of this CatalogDataProductRenderImageInterface.

        Resize width

        :param resized_width: The resized_width of this CatalogDataProductRenderImageInterface.
        :type resized_width: float
        """
        if resized_width is None:
            raise ValueError("Invalid value for `resized_width`, must not be `None`")

        self._resized_width = resized_width

    @property
    def url(self):
        """Gets the url of this CatalogDataProductRenderImageInterface.

        Image url

        :return: The url of this CatalogDataProductRenderImageInterface.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CatalogDataProductRenderImageInterface.

        Image url

        :param url: The url of this CatalogDataProductRenderImageInterface.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def width(self):
        """Gets the width of this CatalogDataProductRenderImageInterface.

        Image width in px

        :return: The width of this CatalogDataProductRenderImageInterface.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CatalogDataProductRenderImageInterface.

        Image width in px

        :param width: The width of this CatalogDataProductRenderImageInterface.
        :type width: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")

        self._width = width
