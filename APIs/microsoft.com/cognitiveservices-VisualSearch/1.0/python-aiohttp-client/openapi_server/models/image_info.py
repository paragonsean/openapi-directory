# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.crop_area import CropArea
from openapi_server import util


class ImageInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, crop_area: CropArea=None, image_insights_token: str=None, url: str=None):
        """ImageInfo - a model defined in OpenAPI

        :param crop_area: The crop_area of this ImageInfo.
        :param image_insights_token: The image_insights_token of this ImageInfo.
        :param url: The url of this ImageInfo.
        """
        self.openapi_types = {
            'crop_area': CropArea,
            'image_insights_token': str,
            'url': str
        }

        self.attribute_map = {
            'crop_area': 'cropArea',
            'image_insights_token': 'imageInsightsToken',
            'url': 'url'
        }

        self._crop_area = crop_area
        self._image_insights_token = image_insights_token
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImageInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImageInfo of this ImageInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def crop_area(self):
        """Gets the crop_area of this ImageInfo.


        :return: The crop_area of this ImageInfo.
        :rtype: CropArea
        """
        return self._crop_area

    @crop_area.setter
    def crop_area(self, crop_area):
        """Sets the crop_area of this ImageInfo.


        :param crop_area: The crop_area of this ImageInfo.
        :type crop_area: CropArea
        """

        self._crop_area = crop_area

    @property
    def image_insights_token(self):
        """Gets the image_insights_token of this ImageInfo.

        An image insights token. To get the insights token, call one of the Image Search APIs (for example, /images/search). In the search results, the [Image](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#image) object's [imageInsightsToken](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#image-imageinsightstoken) field contains the token. The imageInsightsToken and url fields mutually exclusive; do not specify both. Do not specify an insights token if the request includes the image form data.

        :return: The image_insights_token of this ImageInfo.
        :rtype: str
        """
        return self._image_insights_token

    @image_insights_token.setter
    def image_insights_token(self, image_insights_token):
        """Sets the image_insights_token of this ImageInfo.

        An image insights token. To get the insights token, call one of the Image Search APIs (for example, /images/search). In the search results, the [Image](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#image) object's [imageInsightsToken](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-images-api-v7-reference#image-imageinsightstoken) field contains the token. The imageInsightsToken and url fields mutually exclusive; do not specify both. Do not specify an insights token if the request includes the image form data.

        :param image_insights_token: The image_insights_token of this ImageInfo.
        :type image_insights_token: str
        """

        self._image_insights_token = image_insights_token

    @property
    def url(self):
        """Gets the url of this ImageInfo.

        The URL of the input image. The imageInsightsToken and url fields are mutually exclusive; do not specify both. Do not specify the URL if the request includes the image form data.

        :return: The url of this ImageInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageInfo.

        The URL of the input image. The imageInsightsToken and url fields are mutually exclusive; do not specify both. Do not specify the URL if the request includes the image form data.

        :param url: The url of this ImageInfo.
        :type url: str
        """

        self._url = url
