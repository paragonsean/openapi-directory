# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.chamber import Chamber
from openapi_server.models.jurisdiction_classification import JurisdictionClassification
from openapi_server.models.legislative_session import LegislativeSession
from openapi_server.models.run_plan import RunPlan
from openapi_server import util


class Jurisdiction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, classification: JurisdictionClassification=None, division_id: str='', id: str=None, latest_bill_update: datetime=None, latest_people_update: datetime=None, latest_runs: List[RunPlan]=None, legislative_sessions: List[LegislativeSession]=None, name: str=None, organizations: List[Chamber]=None, url: str=None):
        """Jurisdiction - a model defined in OpenAPI

        :param classification: The classification of this Jurisdiction.
        :param division_id: The division_id of this Jurisdiction.
        :param id: The id of this Jurisdiction.
        :param latest_bill_update: The latest_bill_update of this Jurisdiction.
        :param latest_people_update: The latest_people_update of this Jurisdiction.
        :param latest_runs: The latest_runs of this Jurisdiction.
        :param legislative_sessions: The legislative_sessions of this Jurisdiction.
        :param name: The name of this Jurisdiction.
        :param organizations: The organizations of this Jurisdiction.
        :param url: The url of this Jurisdiction.
        """
        self.openapi_types = {
            'classification': JurisdictionClassification,
            'division_id': str,
            'id': str,
            'latest_bill_update': datetime,
            'latest_people_update': datetime,
            'latest_runs': List[RunPlan],
            'legislative_sessions': List[LegislativeSession],
            'name': str,
            'organizations': List[Chamber],
            'url': str
        }

        self.attribute_map = {
            'classification': 'classification',
            'division_id': 'division_id',
            'id': 'id',
            'latest_bill_update': 'latest_bill_update',
            'latest_people_update': 'latest_people_update',
            'latest_runs': 'latest_runs',
            'legislative_sessions': 'legislative_sessions',
            'name': 'name',
            'organizations': 'organizations',
            'url': 'url'
        }

        self._classification = classification
        self._division_id = division_id
        self._id = id
        self._latest_bill_update = latest_bill_update
        self._latest_people_update = latest_people_update
        self._latest_runs = latest_runs
        self._legislative_sessions = legislative_sessions
        self._name = name
        self._organizations = organizations
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Jurisdiction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Jurisdiction of this Jurisdiction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def classification(self):
        """Gets the classification of this Jurisdiction.


        :return: The classification of this Jurisdiction.
        :rtype: JurisdictionClassification
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this Jurisdiction.


        :param classification: The classification of this Jurisdiction.
        :type classification: JurisdictionClassification
        """
        if classification is None:
            raise ValueError("Invalid value for `classification`, must not be `None`")

        self._classification = classification

    @property
    def division_id(self):
        """Gets the division_id of this Jurisdiction.


        :return: The division_id of this Jurisdiction.
        :rtype: str
        """
        return self._division_id

    @division_id.setter
    def division_id(self, division_id):
        """Sets the division_id of this Jurisdiction.


        :param division_id: The division_id of this Jurisdiction.
        :type division_id: str
        """

        self._division_id = division_id

    @property
    def id(self):
        """Gets the id of this Jurisdiction.


        :return: The id of this Jurisdiction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Jurisdiction.


        :param id: The id of this Jurisdiction.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def latest_bill_update(self):
        """Gets the latest_bill_update of this Jurisdiction.


        :return: The latest_bill_update of this Jurisdiction.
        :rtype: datetime
        """
        return self._latest_bill_update

    @latest_bill_update.setter
    def latest_bill_update(self, latest_bill_update):
        """Sets the latest_bill_update of this Jurisdiction.


        :param latest_bill_update: The latest_bill_update of this Jurisdiction.
        :type latest_bill_update: datetime
        """
        if latest_bill_update is None:
            raise ValueError("Invalid value for `latest_bill_update`, must not be `None`")

        self._latest_bill_update = latest_bill_update

    @property
    def latest_people_update(self):
        """Gets the latest_people_update of this Jurisdiction.


        :return: The latest_people_update of this Jurisdiction.
        :rtype: datetime
        """
        return self._latest_people_update

    @latest_people_update.setter
    def latest_people_update(self, latest_people_update):
        """Sets the latest_people_update of this Jurisdiction.


        :param latest_people_update: The latest_people_update of this Jurisdiction.
        :type latest_people_update: datetime
        """
        if latest_people_update is None:
            raise ValueError("Invalid value for `latest_people_update`, must not be `None`")

        self._latest_people_update = latest_people_update

    @property
    def latest_runs(self):
        """Gets the latest_runs of this Jurisdiction.


        :return: The latest_runs of this Jurisdiction.
        :rtype: List[RunPlan]
        """
        return self._latest_runs

    @latest_runs.setter
    def latest_runs(self, latest_runs):
        """Sets the latest_runs of this Jurisdiction.


        :param latest_runs: The latest_runs of this Jurisdiction.
        :type latest_runs: List[RunPlan]
        """

        self._latest_runs = latest_runs

    @property
    def legislative_sessions(self):
        """Gets the legislative_sessions of this Jurisdiction.


        :return: The legislative_sessions of this Jurisdiction.
        :rtype: List[LegislativeSession]
        """
        return self._legislative_sessions

    @legislative_sessions.setter
    def legislative_sessions(self, legislative_sessions):
        """Sets the legislative_sessions of this Jurisdiction.


        :param legislative_sessions: The legislative_sessions of this Jurisdiction.
        :type legislative_sessions: List[LegislativeSession]
        """

        self._legislative_sessions = legislative_sessions

    @property
    def name(self):
        """Gets the name of this Jurisdiction.


        :return: The name of this Jurisdiction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Jurisdiction.


        :param name: The name of this Jurisdiction.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def organizations(self):
        """Gets the organizations of this Jurisdiction.


        :return: The organizations of this Jurisdiction.
        :rtype: List[Chamber]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this Jurisdiction.


        :param organizations: The organizations of this Jurisdiction.
        :type organizations: List[Chamber]
        """

        self._organizations = organizations

    @property
    def url(self):
        """Gets the url of this Jurisdiction.


        :return: The url of this Jurisdiction.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Jurisdiction.


        :param url: The url of this Jurisdiction.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url
