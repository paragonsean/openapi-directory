from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_subject_right_cancel_delete_request_request import DataSubjectRightCancelDeleteRequestRequest
from openapi_server.models.data_subject_right_delete_request202_response import DataSubjectRightDeleteRequest202Response
from openapi_server.models.data_subject_right_delete_status_request200_response import DataSubjectRightDeleteStatusRequest200Response
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse
from openapi_server import util


async def data_subject_right_cancel_delete_request(request: web.Request, token, body=None) -> web.Response:
    """data_subject_right_cancel_delete_request

    

    :param token: Unique request ID (GUID)
    :type token: str
    :type token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DataSubjectRightCancelDeleteRequestRequest.from_dict(body)
    return web.Response(status=200)


async def data_subject_right_cancel_export_request(request: web.Request, token) -> web.Response:
    """data_subject_right_cancel_export_request

    

    :param token: Unique request ID (GUID)
    :type token: str
    :type token: str

    """
    return web.Response(status=200)


async def data_subject_right_delete_request(request: web.Request, ) -> web.Response:
    """data_subject_right_delete_request

    


    """
    return web.Response(status=200)


async def data_subject_right_delete_status_request(request: web.Request, token, email) -> web.Response:
    """data_subject_right_delete_status_request

    

    :param token: Unique request ID (GUID)
    :type token: str
    :type token: str
    :param email: Email used for delete with x-authz-bypass headers
    :type email: str

    """
    return web.Response(status=200)


async def data_subject_right_export_request(request: web.Request, ) -> web.Response:
    """data_subject_right_export_request

    


    """
    return web.Response(status=200)


async def data_subject_right_export_status_request(request: web.Request, token) -> web.Response:
    """data_subject_right_export_status_request

    

    :param token: Unique request ID (GUID)
    :type token: str
    :type token: str

    """
    return web.Response(status=200)
