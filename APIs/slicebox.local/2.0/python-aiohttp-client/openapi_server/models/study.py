# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.dicom_property_value import DicomPropertyValue
from openapi_server import util


class Study(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, accession_number: DicomPropertyValue=None, id: int=None, patient_age: DicomPropertyValue=None, patient_id: int=None, study_date: DicomPropertyValue=None, study_description: DicomPropertyValue=None, study_id: DicomPropertyValue=None, study_instance_uid: DicomPropertyValue=None):
        """Study - a model defined in OpenAPI

        :param accession_number: The accession_number of this Study.
        :param id: The id of this Study.
        :param patient_age: The patient_age of this Study.
        :param patient_id: The patient_id of this Study.
        :param study_date: The study_date of this Study.
        :param study_description: The study_description of this Study.
        :param study_id: The study_id of this Study.
        :param study_instance_uid: The study_instance_uid of this Study.
        """
        self.openapi_types = {
            'accession_number': DicomPropertyValue,
            'id': int,
            'patient_age': DicomPropertyValue,
            'patient_id': int,
            'study_date': DicomPropertyValue,
            'study_description': DicomPropertyValue,
            'study_id': DicomPropertyValue,
            'study_instance_uid': DicomPropertyValue
        }

        self.attribute_map = {
            'accession_number': 'accessionNumber',
            'id': 'id',
            'patient_age': 'patientAge',
            'patient_id': 'patientId',
            'study_date': 'studyDate',
            'study_description': 'studyDescription',
            'study_id': 'studyID',
            'study_instance_uid': 'studyInstanceUID'
        }

        self._accession_number = accession_number
        self._id = id
        self._patient_age = patient_age
        self._patient_id = patient_id
        self._study_date = study_date
        self._study_description = study_description
        self._study_id = study_id
        self._study_instance_uid = study_instance_uid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Study':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The study of this Study.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def accession_number(self):
        """Gets the accession_number of this Study.


        :return: The accession_number of this Study.
        :rtype: DicomPropertyValue
        """
        return self._accession_number

    @accession_number.setter
    def accession_number(self, accession_number):
        """Sets the accession_number of this Study.


        :param accession_number: The accession_number of this Study.
        :type accession_number: DicomPropertyValue
        """

        self._accession_number = accession_number

    @property
    def id(self):
        """Gets the id of this Study.


        :return: The id of this Study.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Study.


        :param id: The id of this Study.
        :type id: int
        """

        self._id = id

    @property
    def patient_age(self):
        """Gets the patient_age of this Study.


        :return: The patient_age of this Study.
        :rtype: DicomPropertyValue
        """
        return self._patient_age

    @patient_age.setter
    def patient_age(self, patient_age):
        """Sets the patient_age of this Study.


        :param patient_age: The patient_age of this Study.
        :type patient_age: DicomPropertyValue
        """

        self._patient_age = patient_age

    @property
    def patient_id(self):
        """Gets the patient_id of this Study.


        :return: The patient_id of this Study.
        :rtype: int
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """Sets the patient_id of this Study.


        :param patient_id: The patient_id of this Study.
        :type patient_id: int
        """

        self._patient_id = patient_id

    @property
    def study_date(self):
        """Gets the study_date of this Study.


        :return: The study_date of this Study.
        :rtype: DicomPropertyValue
        """
        return self._study_date

    @study_date.setter
    def study_date(self, study_date):
        """Sets the study_date of this Study.


        :param study_date: The study_date of this Study.
        :type study_date: DicomPropertyValue
        """

        self._study_date = study_date

    @property
    def study_description(self):
        """Gets the study_description of this Study.


        :return: The study_description of this Study.
        :rtype: DicomPropertyValue
        """
        return self._study_description

    @study_description.setter
    def study_description(self, study_description):
        """Sets the study_description of this Study.


        :param study_description: The study_description of this Study.
        :type study_description: DicomPropertyValue
        """

        self._study_description = study_description

    @property
    def study_id(self):
        """Gets the study_id of this Study.


        :return: The study_id of this Study.
        :rtype: DicomPropertyValue
        """
        return self._study_id

    @study_id.setter
    def study_id(self, study_id):
        """Sets the study_id of this Study.


        :param study_id: The study_id of this Study.
        :type study_id: DicomPropertyValue
        """

        self._study_id = study_id

    @property
    def study_instance_uid(self):
        """Gets the study_instance_uid of this Study.


        :return: The study_instance_uid of this Study.
        :rtype: DicomPropertyValue
        """
        return self._study_instance_uid

    @study_instance_uid.setter
    def study_instance_uid(self, study_instance_uid):
        """Sets the study_instance_uid of this Study.


        :param study_instance_uid: The study_instance_uid of this Study.
        :type study_instance_uid: DicomPropertyValue
        """

        self._study_instance_uid = study_instance_uid
