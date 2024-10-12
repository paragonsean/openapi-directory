# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.image_tag_prediction import ImageTagPrediction
from openapi_server import util


class ImagePredictionResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, id: str=None, iteration: str=None, predictions: List[ImageTagPrediction]=None, project: str=None):
        """ImagePredictionResult - a model defined in OpenAPI

        :param created: The created of this ImagePredictionResult.
        :param id: The id of this ImagePredictionResult.
        :param iteration: The iteration of this ImagePredictionResult.
        :param predictions: The predictions of this ImagePredictionResult.
        :param project: The project of this ImagePredictionResult.
        """
        self.openapi_types = {
            'created': datetime,
            'id': str,
            'iteration': str,
            'predictions': List[ImageTagPrediction],
            'project': str
        }

        self.attribute_map = {
            'created': 'Created',
            'id': 'Id',
            'iteration': 'Iteration',
            'predictions': 'Predictions',
            'project': 'Project'
        }

        self._created = created
        self._id = id
        self._iteration = iteration
        self._predictions = predictions
        self._project = project

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImagePredictionResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImagePredictionResult of this ImagePredictionResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self):
        """Gets the created of this ImagePredictionResult.


        :return: The created of this ImagePredictionResult.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ImagePredictionResult.


        :param created: The created of this ImagePredictionResult.
        :type created: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this ImagePredictionResult.


        :return: The id of this ImagePredictionResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImagePredictionResult.


        :param id: The id of this ImagePredictionResult.
        :type id: str
        """

        self._id = id

    @property
    def iteration(self):
        """Gets the iteration of this ImagePredictionResult.


        :return: The iteration of this ImagePredictionResult.
        :rtype: str
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        """Sets the iteration of this ImagePredictionResult.


        :param iteration: The iteration of this ImagePredictionResult.
        :type iteration: str
        """

        self._iteration = iteration

    @property
    def predictions(self):
        """Gets the predictions of this ImagePredictionResult.


        :return: The predictions of this ImagePredictionResult.
        :rtype: List[ImageTagPrediction]
        """
        return self._predictions

    @predictions.setter
    def predictions(self, predictions):
        """Sets the predictions of this ImagePredictionResult.


        :param predictions: The predictions of this ImagePredictionResult.
        :type predictions: List[ImageTagPrediction]
        """

        self._predictions = predictions

    @property
    def project(self):
        """Gets the project of this ImagePredictionResult.


        :return: The project of this ImagePredictionResult.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ImagePredictionResult.


        :param project: The project of this ImagePredictionResult.
        :type project: str
        """

        self._project = project
