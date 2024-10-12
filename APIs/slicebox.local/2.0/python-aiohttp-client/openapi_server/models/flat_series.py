# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.patient import Patient
from openapi_server.models.series import Series
from openapi_server.models.study import Study
from openapi_server import util


class FlatSeries(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, patient: Patient=None, series: Series=None, study: Study=None):
        """FlatSeries - a model defined in OpenAPI

        :param id: The id of this FlatSeries.
        :param patient: The patient of this FlatSeries.
        :param series: The series of this FlatSeries.
        :param study: The study of this FlatSeries.
        """
        self.openapi_types = {
            'id': int,
            'patient': Patient,
            'series': Series,
            'study': Study
        }

        self.attribute_map = {
            'id': 'id',
            'patient': 'patient',
            'series': 'series',
            'study': 'study'
        }

        self._id = id
        self._patient = patient
        self._series = series
        self._study = study

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FlatSeries':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The flatSeries of this FlatSeries.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this FlatSeries.


        :return: The id of this FlatSeries.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlatSeries.


        :param id: The id of this FlatSeries.
        :type id: int
        """

        self._id = id

    @property
    def patient(self):
        """Gets the patient of this FlatSeries.


        :return: The patient of this FlatSeries.
        :rtype: Patient
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this FlatSeries.


        :param patient: The patient of this FlatSeries.
        :type patient: Patient
        """

        self._patient = patient

    @property
    def series(self):
        """Gets the series of this FlatSeries.


        :return: The series of this FlatSeries.
        :rtype: Series
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this FlatSeries.


        :param series: The series of this FlatSeries.
        :type series: Series
        """

        self._series = series

    @property
    def study(self):
        """Gets the study of this FlatSeries.


        :return: The study of this FlatSeries.
        :rtype: Study
        """
        return self._study

    @study.setter
    def study(self, study):
        """Sets the study of this FlatSeries.


        :param study: The study of this FlatSeries.
        :type study: Study
        """

        self._study = study
