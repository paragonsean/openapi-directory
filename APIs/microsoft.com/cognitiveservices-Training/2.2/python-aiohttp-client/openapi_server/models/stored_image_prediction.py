# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.prediction import Prediction
from openapi_server import util


class StoredImagePrediction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, domain: str=None, id: str=None, iteration: str=None, original_image_uri: str=None, predictions: List[Prediction]=None, project: str=None, resized_image_uri: str=None, thumbnail_uri: str=None):
        """StoredImagePrediction - a model defined in OpenAPI

        :param created: The created of this StoredImagePrediction.
        :param domain: The domain of this StoredImagePrediction.
        :param id: The id of this StoredImagePrediction.
        :param iteration: The iteration of this StoredImagePrediction.
        :param original_image_uri: The original_image_uri of this StoredImagePrediction.
        :param predictions: The predictions of this StoredImagePrediction.
        :param project: The project of this StoredImagePrediction.
        :param resized_image_uri: The resized_image_uri of this StoredImagePrediction.
        :param thumbnail_uri: The thumbnail_uri of this StoredImagePrediction.
        """
        self.openapi_types = {
            'created': datetime,
            'domain': str,
            'id': str,
            'iteration': str,
            'original_image_uri': str,
            'predictions': List[Prediction],
            'project': str,
            'resized_image_uri': str,
            'thumbnail_uri': str
        }

        self.attribute_map = {
            'created': 'created',
            'domain': 'domain',
            'id': 'id',
            'iteration': 'iteration',
            'original_image_uri': 'originalImageUri',
            'predictions': 'predictions',
            'project': 'project',
            'resized_image_uri': 'resizedImageUri',
            'thumbnail_uri': 'thumbnailUri'
        }

        self._created = created
        self._domain = domain
        self._id = id
        self._iteration = iteration
        self._original_image_uri = original_image_uri
        self._predictions = predictions
        self._project = project
        self._resized_image_uri = resized_image_uri
        self._thumbnail_uri = thumbnail_uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'StoredImagePrediction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The StoredImagePrediction of this StoredImagePrediction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this StoredImagePrediction.


        :return: The created of this StoredImagePrediction.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this StoredImagePrediction.


        :param created: The created of this StoredImagePrediction.
        :type created: datetime
        """

        self._created = created

    @property
    def domain(self):
        """Gets the domain of this StoredImagePrediction.

        Domain used for the prediction.

        :return: The domain of this StoredImagePrediction.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this StoredImagePrediction.

        Domain used for the prediction.

        :param domain: The domain of this StoredImagePrediction.
        :type domain: str
        """

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this StoredImagePrediction.


        :return: The id of this StoredImagePrediction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoredImagePrediction.


        :param id: The id of this StoredImagePrediction.
        :type id: str
        """

        self._id = id

    @property
    def iteration(self):
        """Gets the iteration of this StoredImagePrediction.


        :return: The iteration of this StoredImagePrediction.
        :rtype: str
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this StoredImagePrediction.


        :param iteration: The iteration of this StoredImagePrediction.
        :type iteration: str
        """

        self._iteration = iteration

    @property
    def original_image_uri(self):
        """Gets the original_image_uri of this StoredImagePrediction.

        The URI to the original prediction image.

        :return: The original_image_uri of this StoredImagePrediction.
        :rtype: str
        """
        return self._original_image_uri

    @original_image_uri.setter
    def original_image_uri(self, original_image_uri):
        """Sets the original_image_uri of this StoredImagePrediction.

        The URI to the original prediction image.

        :param original_image_uri: The original_image_uri of this StoredImagePrediction.
        :type original_image_uri: str
        """

        self._original_image_uri = original_image_uri

    @property
    def predictions(self):
        """Gets the predictions of this StoredImagePrediction.


        :return: The predictions of this StoredImagePrediction.
        :rtype: List[Prediction]
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions):
        """Sets the predictions of this StoredImagePrediction.


        :param predictions: The predictions of this StoredImagePrediction.
        :type predictions: List[Prediction]
        """

        self._predictions = predictions

    @property
    def project(self):
        """Gets the project of this StoredImagePrediction.


        :return: The project of this StoredImagePrediction.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this StoredImagePrediction.


        :param project: The project of this StoredImagePrediction.
        :type project: str
        """

        self._project = project

    @property
    def resized_image_uri(self):
        """Gets the resized_image_uri of this StoredImagePrediction.

        The URI to the (resized) prediction image.

        :return: The resized_image_uri of this StoredImagePrediction.
        :rtype: str
        """
        return self._resized_image_uri

    @resized_image_uri.setter
    def resized_image_uri(self, resized_image_uri):
        """Sets the resized_image_uri of this StoredImagePrediction.

        The URI to the (resized) prediction image.

        :param resized_image_uri: The resized_image_uri of this StoredImagePrediction.
        :type resized_image_uri: str
        """

        self._resized_image_uri = resized_image_uri

    @property
    def thumbnail_uri(self):
        """Gets the thumbnail_uri of this StoredImagePrediction.

        The URI to the thumbnail of the original prediction image.

        :return: The thumbnail_uri of this StoredImagePrediction.
        :rtype: str
        """
        return self._thumbnail_uri

    @thumbnail_uri.setter
    def thumbnail_uri(self, thumbnail_uri):
        """Sets the thumbnail_uri of this StoredImagePrediction.

        The URI to the thumbnail of the original prediction image.

        :param thumbnail_uri: The thumbnail_uri of this StoredImagePrediction.
        :type thumbnail_uri: str
        """

        self._thumbnail_uri = thumbnail_uri
