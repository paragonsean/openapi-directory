from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit_log_item_model import AuditLogItemModel
from openapi_server.models.audit_log_type import AuditLogType
from openapi_server.models.setting_model import SettingModel
from openapi_server.models.setting_model_haljson import SettingModelHaljson
from openapi_server import util


async def get_auditlogs(request: web.Request, product_id, config_id=None, environment_id=None, audit_log_type=None, from_utc_date_time=None, to_utc_date_time=None) -> web.Response:
    """List Audit log items for Product

    This endpoint returns the list of Audit log items for a given Product  and the result can be optionally filtered by Config and/or Environment.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param audit_log_type: Filter Audit logs by Audit log type.
    :type audit_log_type: dict | bytes
    :param from_utc_date_time: Filter Audit logs by starting UTC date.
    :type from_utc_date_time: str
    :param to_utc_date_time: Filter Audit logs by ending UTC date.
    :type to_utc_date_time: str

    """
    audit_log_type = .from_dict(audit_log_type)
    from_utc_date_time = util.deserialize_datetime(from_utc_date_time)
    to_utc_date_time = util.deserialize_datetime(to_utc_date_time)
    return web.Response(status=200)


async def get_deleted_settings(request: web.Request, config_id) -> web.Response:
    """List Deleted Settings

    This endpoint returns the list of Feature Flags and Settings that were deleted from the given Config.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str

    """
    return web.Response(status=200)


async def get_organization_auditlogs(request: web.Request, organization_id, product_id=None, config_id=None, environment_id=None, audit_log_type=None, from_utc_date_time=None, to_utc_date_time=None) -> web.Response:
    """List Audit log items for Organization

    This endpoint returns the list of Audit log items for a given Organization  and the result can be optionally filtered by Product and/or Config and/or Environment.

    :param organization_id: The identifier of the Organization.
    :type organization_id: str
    :type organization_id: str
    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param audit_log_type: Filter Audit logs by Audit log type.
    :type audit_log_type: dict | bytes
    :param from_utc_date_time: Filter Audit logs by starting UTC date.
    :type from_utc_date_time: str
    :param to_utc_date_time: Filter Audit logs by ending UTC date.
    :type to_utc_date_time: str

    """
    audit_log_type = .from_dict(audit_log_type)
    from_utc_date_time = util.deserialize_datetime(from_utc_date_time)
    to_utc_date_time = util.deserialize_datetime(to_utc_date_time)
    return web.Response(status=200)
