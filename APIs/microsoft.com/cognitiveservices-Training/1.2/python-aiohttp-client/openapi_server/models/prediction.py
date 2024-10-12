# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.prediction_tag import PredictionTag
from openapi_server import util


class Prediction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, id: str=None, image_uri: str=None, iteration: str=None, predictions: List[PredictionTag]=None, project: str=None, thumbnail_uri: str=None):
        """Prediction - a model defined in OpenAPI

        :param created: The created of this Prediction.
        :param id: The id of this Prediction.
        :param image_uri: The image_uri of this Prediction.
        :param iteration: The iteration of this Prediction.
        :param predictions: The predictions of this Prediction.
        :param project: The project of this Prediction.
        :param thumbnail_uri: The thumbnail_uri of this Prediction.
        """
        self.openapi_types = {
            'created': datetime,
            'id': str,
            'image_uri': str,
            'iteration': str,
            'predictions': List[PredictionTag],
            'project': str,
            'thumbnail_uri': str
        }

        self.attribute_map = {
            'created': 'Created',
            'id': 'Id',
            'image_uri': 'ImageUri',
            'iteration': 'Iteration',
            'predictions': 'Predictions',
            'project': 'Project',
            'thumbnail_uri': 'ThumbnailUri'
        }

        self._created = created
        self._id = id
        self._image_uri = image_uri
        self._iteration = iteration
        self._predictions = predictions
        self._project = project
        self._thumbnail_uri = thumbnail_uri

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Prediction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Prediction of this Prediction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this Prediction.


        :return: The created of this Prediction.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Prediction.


        :param created: The created of this Prediction.
        :type created: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this Prediction.


        :return: The id of this Prediction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Prediction.


        :param id: The id of this Prediction.
        :type id: str
        """

        self._id = id

    @property
    def image_uri(self):
        """Gets the image_uri of this Prediction.


        :return: The image_uri of this Prediction.
        :rtype: str
        """
        return self._image_uri

    @image_uri.setter
    def image_uri(self, image_uri):
        """Sets the image_uri of this Prediction.


        :param image_uri: The image_uri of this Prediction.
        :type image_uri: str
        """

        self._image_uri = image_uri

    @property
    def iteration(self):
        """Gets the iteration of this Prediction.


        :return: The iteration of this Prediction.
        :rtype: str
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this Prediction.


        :param iteration: The iteration of this Prediction.
        :type iteration: str
        """

        self._iteration = iteration

    @property
    def predictions(self):
        """Gets the predictions of this Prediction.


        :return: The predictions of this Prediction.
        :rtype: List[PredictionTag]
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions):
        """Sets the predictions of this Prediction.


        :param predictions: The predictions of this Prediction.
        :type predictions: List[PredictionTag]
        """

        self._predictions = predictions

    @property
    def project(self):
        """Gets the project of this Prediction.


        :return: The project of this Prediction.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Prediction.


        :param project: The project of this Prediction.
        :type project: str
        """

        self._project = project

    @property
    def thumbnail_uri(self):
        """Gets the thumbnail_uri of this Prediction.


        :return: The thumbnail_uri of this Prediction.
        :rtype: str
        """
        return self._thumbnail_uri

    @thumbnail_uri.setter
    def thumbnail_uri(self, thumbnail_uri):
        """Sets the thumbnail_uri of this Prediction.


        :param thumbnail_uri: The thumbnail_uri of this Prediction.
        :type thumbnail_uri: str
        """

        self._thumbnail_uri = thumbnail_uri
