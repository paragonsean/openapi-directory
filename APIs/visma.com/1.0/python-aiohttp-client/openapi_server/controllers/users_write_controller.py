from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flextime_adjustment_input_model import FlextimeAdjustmentInputModel
from openapi_server.models.flextime_adjustment_output_model import FlextimeAdjustmentOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.user_custom_value_input_model import UserCustomValueInputModel
from openapi_server.models.user_custom_value_output_model import UserCustomValueOutputModel
from openapi_server.models.user_input_model import UserInputModel
from openapi_server.models.user_keyword_model import UserKeywordModel
from openapi_server.models.user_output_model import UserOutputModel
from openapi_server.models.work_contract_input_model import WorkContractInputModel
from openapi_server.models.work_contract_output_model import WorkContractOutputModel
from openapi_server.models.workday_model import WorkdayModel
from openapi_server import util


async def flextime_adjustments_delete_flextime_adjustment(request: web.Request, guid) -> web.Response:
    """Delete an flextime adjustment.

    Returns: No Content (204) if succeeded. Not found (404) if flextime adjustment can&#39;t be found.

    :param guid: ID for the flextime adjustment to delete.
    :type guid: str

    """
    return web.Response(status=200)


async def flextime_adjustments_patch_flextime_adjustment(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an Flextime Adjustment or a part of it.

    

    :param guid: ID of the Flextime Adjustment.
    :type guid: str
    :param body: JSON patch document of FlextimeAdjustmentInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def flextime_adjustments_post_flextime_adjustment(request: web.Request, body=None) -> web.Response:
    """Insert a flextime adjustment.

    

    :param body: FlextimeAdjustmentInputModel.
    :type body: dict | bytes

    """
    body = FlextimeAdjustmentInputModel.from_dict(body)
    return web.Response(status=200)


async def keywords_link_keyword_to_user(request: web.Request, user_guid, guid) -> web.Response:
    """Link existing keyword to user

    

    :param user_guid: 
    :type user_guid: str
    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def user_custom_values_patch_user_custom_value(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a user custom value or a part of it.

    

    :param guid: ID of the user custom value Can also be comma separate list of IDs to patch multiple user custom values with one call. When multiple IDs are given, returns model which has list of succeeded user custom values and list of errors.
    :type guid: str
    :param body: JSON Patch document of UserCustomValueModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def user_custom_values_post_user_custom_value(request: web.Request, body=None) -> web.Response:
    """Insert a user custom value.

    

    :param body: UserCustomValueModel.
    :type body: dict | bytes

    """
    body = UserCustomValueInputModel.from_dict(body)
    return web.Response(status=200)


async def users_patch_user(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) an user or a part of it.

    

    :param guid: ID of the user.
    :type guid: str
    :param body: JSON Patch document of UserModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def users_post_user(request: web.Request, body=None) -> web.Response:
    """Insert an user.

    

    :param body: UserModel.
    :type body: dict | bytes

    """
    body = UserInputModel.from_dict(body)
    return web.Response(status=200)


async def work_contracts_patch_work_contract_0(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a work contract or a part of it.

    

    :param guid: ID of the work contract.
    :type guid: str
    :param body: JSON patch document of WorkContractOutputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def work_contracts_post_work_contract_0(request: web.Request, reset_flextime=None, body=None) -> web.Response:
    """Insert a work contract.

    

    :param reset_flextime: Optional. Reset flextime to zero when new work contract starts or keep the flextime value. Default true &#x3D; reset flextime.
    :type reset_flextime: bool
    :param body: WorkContractOutputModel.
    :type body: dict | bytes

    """
    body = WorkContractInputModel.from_dict(body)
    return web.Response(status=200)


async def workdays_patch_work_day(request: web.Request, user_guid, _date, body=None) -> web.Response:
    """Update (Patch) a workday or a part of it

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param _date: Date of the workday..
    :type _date: str
    :param body: JSON patch document of WorkdayModel
    :type body: list | bytes

    """
    _date = util.deserialize_datetime(_date)
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)
