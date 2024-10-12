from typing import List, Dict
from aiohttp import web

from openapi_server.models.code import Code
from openapi_server.models.lookup_type import LookupType
from openapi_server.models.patient_management import PatientManagement
from openapi_server import util


async def get_patient_management(request: web.Request, user_id, group_id, identifier_id) -> web.Response:
    """getPatientManagement

    getPatientManagement

    :param user_id: userId
    :type user_id: int
    :param group_id: groupId
    :type group_id: int
    :param identifier_id: identifierId
    :type identifier_id: int

    """
    return web.Response(status=200)


async def get_patient_management_diagnoses(request: web.Request, ) -> web.Response:
    """getPatientManagementDiagnoses

    getPatientManagementDiagnoses


    """
    return web.Response(status=200)


async def get_patient_management_lookup_types(request: web.Request, ) -> web.Response:
    """getPatientManagementLookupTypes

    getPatientManagementLookupTypes


    """
    return web.Response(status=200)


async def save_patient_management(request: web.Request, user_id, group_id, identifier_id, body=None) -> web.Response:
    """savePatientManagement

    savePatientManagement

    :param user_id: userId
    :type user_id: int
    :param group_id: groupId
    :type group_id: int
    :param identifier_id: identifierId
    :type identifier_id: int
    :param body: patientManagement
    :type body: dict | bytes

    """
    body = PatientManagement.from_dict(body)
    return web.Response(status=200)


async def save_patient_management_surgeries(request: web.Request, user_id, group_id, identifier_id, body=None) -> web.Response:
    """savePatientManagementSurgeries

    savePatientManagementSurgeries

    :param user_id: userId
    :type user_id: int
    :param group_id: groupId
    :type group_id: int
    :param identifier_id: identifierId
    :type identifier_id: int
    :param body: patientManagement
    :type body: dict | bytes

    """
    body = PatientManagement.from_dict(body)
    return web.Response(status=200)


async def validate_patient_management(request: web.Request, body=None) -> web.Response:
    """validatePatientManagement

    validatePatientManagement

    :param body: patientManagement
    :type body: dict | bytes

    """
    body = PatientManagement.from_dict(body)
    return web.Response(status=200)
