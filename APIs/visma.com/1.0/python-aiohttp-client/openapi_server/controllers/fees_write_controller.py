from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flat_rate_input_model import FlatRateInputModel
from openapi_server.models.flat_rate_output_model import FlatRateOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.project_fee_input_model import ProjectFeeInputModel
from openapi_server.models.project_fee_output_model import ProjectFeeOutputModel
from openapi_server.models.project_recurring_fee_rule_input_model import ProjectRecurringFeeRuleInputModel
from openapi_server.models.project_recurring_fee_rule_output_model import ProjectRecurringFeeRuleOutputModel
from openapi_server import util


async def flat_rates_patch_flat_rate(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a flat rate or a part of it.

    

    :param guid: ID of the flat rate.
    :type guid: str
    :param body: JSON Patch document of FlatRateModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def flat_rates_post_flat_rate(request: web.Request, body=None) -> web.Response:
    """Insert a flat rate.

    

    :param body: FlatRateModel.
    :type body: dict | bytes

    """
    body = FlatRateInputModel.from_dict(body)
    return web.Response(status=200)


async def project_fees_patch_project_fee(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a projectFee or a part of it.

    

    :param guid: ID of the project fee Can also be comma separate list of IDs to patch multiple project fees with one call. When multiple IDs are given, returns model which has list of succeeded project fees and list of errors.
    :type guid: str
    :param body: JSON Patch document of ProjectFeeInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_fees_post_project_fee(request: web.Request, body=None) -> web.Response:
    """Insert a project fee.

    

    :param body: ProjectFeeInputModel.
    :type body: dict | bytes

    """
    body = ProjectFeeInputModel.from_dict(body)
    return web.Response(status=200)


async def project_recurring_fee_rules_patch_project_recurring_fee_rule(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a projectRecurringFeeRule or a part of it.

    

    :param guid: ID of the projectRecurringFeeRule.
    :type guid: str
    :param body: JSON Patch document of ProjectRecurringFeeRuleModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_recurring_fee_rules_post_project_recurring_fee_rule(request: web.Request, body=None) -> web.Response:
    """Insert a projectRecurringFeeRule.

    

    :param body: ProjectRecurringFeeRuleModel.
    :type body: dict | bytes

    """
    body = ProjectRecurringFeeRuleInputModel.from_dict(body)
    return web.Response(status=200)
