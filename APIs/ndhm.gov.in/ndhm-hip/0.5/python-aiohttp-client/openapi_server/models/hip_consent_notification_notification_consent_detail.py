# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.consent_manager_patient_id import ConsentManagerPatientID
from openapi_server.models.hip_consent_notification_notification_consent_detail_care_contexts_inner import HIPConsentNotificationNotificationConsentDetailCareContextsInner
from openapi_server.models.hip_consent_notification_notification_consent_detail_consent_manager import HIPConsentNotificationNotificationConsentDetailConsentManager
from openapi_server.models.hip_consent_notification_notification_consent_detail_hip import HIPConsentNotificationNotificationConsentDetailHip
from openapi_server.models.hi_type_enum import HITypeEnum
from openapi_server.models.permission import Permission
from openapi_server.models.use_purpose import UsePurpose
from openapi_server import util


class HIPConsentNotificationNotificationConsentDetail(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, care_contexts: List[HIPConsentNotificationNotificationConsentDetailCareContextsInner]=None, consent_id: str=None, consent_manager: HIPConsentNotificationNotificationConsentDetailConsentManager=None, created_at: datetime=None, hi_types: List[HITypeEnum]=None, hip: HIPConsentNotificationNotificationConsentDetailHip=None, patient: ConsentManagerPatientID=None, permission: Permission=None, purpose: UsePurpose=None, schema_version: str=None):
        """HIPConsentNotificationNotificationConsentDetail - a model defined in OpenAPI

        :param care_contexts: The care_contexts of this HIPConsentNotificationNotificationConsentDetail.
        :param consent_id: The consent_id of this HIPConsentNotificationNotificationConsentDetail.
        :param consent_manager: The consent_manager of this HIPConsentNotificationNotificationConsentDetail.
        :param created_at: The created_at of this HIPConsentNotificationNotificationConsentDetail.
        :param hi_types: The hi_types of this HIPConsentNotificationNotificationConsentDetail.
        :param hip: The hip of this HIPConsentNotificationNotificationConsentDetail.
        :param patient: The patient of this HIPConsentNotificationNotificationConsentDetail.
        :param permission: The permission of this HIPConsentNotificationNotificationConsentDetail.
        :param purpose: The purpose of this HIPConsentNotificationNotificationConsentDetail.
        :param schema_version: The schema_version of this HIPConsentNotificationNotificationConsentDetail.
        """
        self.openapi_types = {
            'care_contexts': List[HIPConsentNotificationNotificationConsentDetailCareContextsInner],
            'consent_id': str,
            'consent_manager': HIPConsentNotificationNotificationConsentDetailConsentManager,
            'created_at': datetime,
            'hi_types': List[HITypeEnum],
            'hip': HIPConsentNotificationNotificationConsentDetailHip,
            'patient': ConsentManagerPatientID,
            'permission': Permission,
            'purpose': UsePurpose,
            'schema_version': str
        }

        self.attribute_map = {
            'care_contexts': 'careContexts',
            'consent_id': 'consentId',
            'consent_manager': 'consentManager',
            'created_at': 'createdAt',
            'hi_types': 'hiTypes',
            'hip': 'hip',
            'patient': 'patient',
            'permission': 'permission',
            'purpose': 'purpose',
            'schema_version': 'schemaVersion'
        }

        self._care_contexts = care_contexts
        self._consent_id = consent_id
        self._consent_manager = consent_manager
        self._created_at = created_at
        self._hi_types = hi_types
        self._hip = hip
        self._patient = patient
        self._permission = permission
        self._purpose = purpose
        self._schema_version = schema_version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HIPConsentNotificationNotificationConsentDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HIPConsentNotification_notification_consentDetail of this HIPConsentNotificationNotificationConsentDetail.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def care_contexts(self):
        """Gets the care_contexts of this HIPConsentNotificationNotificationConsentDetail.


        :return: The care_contexts of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: List[HIPConsentNotificationNotificationConsentDetailCareContextsInner]
        """
        return self._care_contexts

    @care_contexts.setter
    def care_contexts(self, care_contexts):
        """Sets the care_contexts of this HIPConsentNotificationNotificationConsentDetail.


        :param care_contexts: The care_contexts of this HIPConsentNotificationNotificationConsentDetail.
        :type care_contexts: List[HIPConsentNotificationNotificationConsentDetailCareContextsInner]
        """
        if care_contexts is None:
            raise ValueError("Invalid value for `care_contexts`, must not be `None`")

        self._care_contexts = care_contexts

    @property
    def consent_id(self):
        """Gets the consent_id of this HIPConsentNotificationNotificationConsentDetail.


        :return: The consent_id of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this HIPConsentNotificationNotificationConsentDetail.


        :param consent_id: The consent_id of this HIPConsentNotificationNotificationConsentDetail.
        :type consent_id: str
        """
        if consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")

        self._consent_id = consent_id

    @property
    def consent_manager(self):
        """Gets the consent_manager of this HIPConsentNotificationNotificationConsentDetail.


        :return: The consent_manager of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: HIPConsentNotificationNotificationConsentDetailConsentManager
        """
        return self._consent_manager

    @consent_manager.setter
    def consent_manager(self, consent_manager):
        """Sets the consent_manager of this HIPConsentNotificationNotificationConsentDetail.


        :param consent_manager: The consent_manager of this HIPConsentNotificationNotificationConsentDetail.
        :type consent_manager: HIPConsentNotificationNotificationConsentDetailConsentManager
        """
        if consent_manager is None:
            raise ValueError("Invalid value for `consent_manager`, must not be `None`")

        self._consent_manager = consent_manager

    @property
    def created_at(self):
        """Gets the created_at of this HIPConsentNotificationNotificationConsentDetail.


        :return: The created_at of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this HIPConsentNotificationNotificationConsentDetail.


        :param created_at: The created_at of this HIPConsentNotificationNotificationConsentDetail.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def hi_types(self):
        """Gets the hi_types of this HIPConsentNotificationNotificationConsentDetail.


        :return: The hi_types of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: List[HITypeEnum]
        """
        return self._hi_types

    @hi_types.setter
    def hi_types(self, hi_types):
        """Sets the hi_types of this HIPConsentNotificationNotificationConsentDetail.


        :param hi_types: The hi_types of this HIPConsentNotificationNotificationConsentDetail.
        :type hi_types: List[HITypeEnum]
        """
        if hi_types is None:
            raise ValueError("Invalid value for `hi_types`, must not be `None`")

        self._hi_types = hi_types

    @property
    def hip(self):
        """Gets the hip of this HIPConsentNotificationNotificationConsentDetail.


        :return: The hip of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: HIPConsentNotificationNotificationConsentDetailHip
        """
        return self._hip

    @hip.setter
    def hip(self, hip):
        """Sets the hip of this HIPConsentNotificationNotificationConsentDetail.


        :param hip: The hip of this HIPConsentNotificationNotificationConsentDetail.
        :type hip: HIPConsentNotificationNotificationConsentDetailHip
        """
        if hip is None:
            raise ValueError("Invalid value for `hip`, must not be `None`")

        self._hip = hip

    @property
    def patient(self):
        """Gets the patient of this HIPConsentNotificationNotificationConsentDetail.


        :return: The patient of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: ConsentManagerPatientID
        """
        return self._patient

    @patient.setter
    def patient(self, patient):
        """Sets the patient of this HIPConsentNotificationNotificationConsentDetail.


        :param patient: The patient of this HIPConsentNotificationNotificationConsentDetail.
        :type patient: ConsentManagerPatientID
        """
        if patient is None:
            raise ValueError("Invalid value for `patient`, must not be `None`")

        self._patient = patient

    @property
    def permission(self):
        """Gets the permission of this HIPConsentNotificationNotificationConsentDetail.


        :return: The permission of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: Permission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this HIPConsentNotificationNotificationConsentDetail.


        :param permission: The permission of this HIPConsentNotificationNotificationConsentDetail.
        :type permission: Permission
        """
        if permission is None:
            raise ValueError("Invalid value for `permission`, must not be `None`")

        self._permission = permission

    @property
    def purpose(self):
        """Gets the purpose of this HIPConsentNotificationNotificationConsentDetail.


        :return: The purpose of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: UsePurpose
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this HIPConsentNotificationNotificationConsentDetail.


        :param purpose: The purpose of this HIPConsentNotificationNotificationConsentDetail.
        :type purpose: UsePurpose
        """
        if purpose is None:
            raise ValueError("Invalid value for `purpose`, must not be `None`")

        self._purpose = purpose

    @property
    def schema_version(self):
        """Gets the schema_version of this HIPConsentNotificationNotificationConsentDetail.


        :return: The schema_version of this HIPConsentNotificationNotificationConsentDetail.
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this HIPConsentNotificationNotificationConsentDetail.


        :param schema_version: The schema_version of this HIPConsentNotificationNotificationConsentDetail.
        :type schema_version: str
        """

        self._schema_version = schema_version
