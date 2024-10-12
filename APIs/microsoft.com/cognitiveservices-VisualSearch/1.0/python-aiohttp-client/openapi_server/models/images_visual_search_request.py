# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ImagesVisualSearchRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, knowledge_request: str=None, image: file=None):
        """ImagesVisualSearchRequest - a model defined in OpenAPI

        :param knowledge_request: The knowledge_request of this ImagesVisualSearchRequest.
        :param image: The image of this ImagesVisualSearchRequest.
        """
        self.openapi_types = {
            'knowledge_request': str,
            'image': file
        }

        self.attribute_map = {
            'knowledge_request': 'knowledgeRequest',
            'image': 'image'
        }

        self._knowledge_request = knowledge_request
        self._image = image

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImagesVisualSearchRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Images_VisualSearch_request of this ImagesVisualSearchRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def knowledge_request(self):
        """Gets the knowledge_request of this ImagesVisualSearchRequest.

        The form data is a JSON object that identifies the image using an insights token or URL to the image. The object may also include an optional crop area that identifies an area of interest in the image. The insights token and URL are mutually exclusive – do not specify both. You may specify knowledgeRequest form data and image form data in the same request only if knowledgeRequest form data specifies the cropArea field only (it must not include an insights token or URL).

        :return: The knowledge_request of this ImagesVisualSearchRequest.
        :rtype: str
        """
        return self._knowledge_request

    @knowledge_request.setter
    def knowledge_request(self, knowledge_request):
        """Sets the knowledge_request of this ImagesVisualSearchRequest.

        The form data is a JSON object that identifies the image using an insights token or URL to the image. The object may also include an optional crop area that identifies an area of interest in the image. The insights token and URL are mutually exclusive – do not specify both. You may specify knowledgeRequest form data and image form data in the same request only if knowledgeRequest form data specifies the cropArea field only (it must not include an insights token or URL).

        :param knowledge_request: The knowledge_request of this ImagesVisualSearchRequest.
        :type knowledge_request: str
        """

        self._knowledge_request = knowledge_request

    @property
    def image(self):
        """Gets the image of this ImagesVisualSearchRequest.

        The form data is an image binary. The Content-Disposition header's name parameter must be set to \"image\". You must specify an image binary if you do not use knowledgeRequest form data to specify the image; you may not use both forms to specify an image. You may specify knowledgeRequest form data and image form data in the same request only if knowledgeRequest form data specifies the cropArea field only  (it must not include an insights token or URL).

        :return: The image of this ImagesVisualSearchRequest.
        :rtype: file
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImagesVisualSearchRequest.

        The form data is an image binary. The Content-Disposition header's name parameter must be set to \"image\". You must specify an image binary if you do not use knowledgeRequest form data to specify the image; you may not use both forms to specify an image. You may specify knowledgeRequest form data and image form data in the same request only if knowledgeRequest form data specifies the cropArea field only  (it must not include an insights token or URL).

        :param image: The image of this ImagesVisualSearchRequest.
        :type image: file
        """

        self._image = image
