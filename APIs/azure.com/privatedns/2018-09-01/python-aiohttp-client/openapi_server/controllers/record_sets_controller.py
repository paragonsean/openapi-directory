from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.record_set import RecordSet
from openapi_server.models.record_set_list_result import RecordSetListResult
from openapi_server import util


async def record_sets_create_or_update(request: web.Request, resource_group_name, private_zone_name, record_type, relative_record_set_name, api_version, subscription_id, parameters, if_match=None, if_none_match=None) -> web.Response:
    """record_sets_create_or_update

    Creates or updates a record set within a Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param record_type: The type of DNS record in this record set. Record sets of type SOA can be updated but not created (they are created when the Private DNS zone is created).
    :type record_type: str
    :param relative_record_set_name: The name of the record set, relative to the name of the zone.
    :type relative_record_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes
    :param if_match: The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    :type if_match: str
    :param if_none_match: Set to &#39;*&#39; to allow a new record set to be created, but to prevent updating an existing record set. Other values will be ignored.
    :type if_none_match: str

    """
    parameters = RecordSet.from_dict(parameters)
    return web.Response(status=200)


async def record_sets_delete(request: web.Request, resource_group_name, private_zone_name, record_type, relative_record_set_name, api_version, subscription_id, if_match=None) -> web.Response:
    """record_sets_delete

    Deletes a record set from a Private DNS zone. This operation cannot be undone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param record_type: The type of DNS record in this record set. Record sets of type SOA cannot be deleted (they are deleted when the Private DNS zone is deleted).
    :type record_type: str
    :param relative_record_set_name: The name of the record set, relative to the name of the zone.
    :type relative_record_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param if_match: The ETag of the record set. Omit this value to always delete the current record set. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    :type if_match: str

    """
    return web.Response(status=200)


async def record_sets_get(request: web.Request, resource_group_name, private_zone_name, record_type, relative_record_set_name, api_version, subscription_id) -> web.Response:
    """record_sets_get

    Gets a record set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param record_type: The type of DNS record in this record set.
    :type record_type: str
    :param relative_record_set_name: The name of the record set, relative to the name of the zone.
    :type relative_record_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def record_sets_list(request: web.Request, resource_group_name, private_zone_name, api_version, subscription_id, top=None, recordsetnamesuffix=None) -> web.Response:
    """record_sets_list

    Lists all record sets in a Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    :type top: int
    :param recordsetnamesuffix: The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \&quot;.&lt;recordsetnamesuffix&gt;\&quot;.
    :type recordsetnamesuffix: str

    """
    return web.Response(status=200)


async def record_sets_list_by_type(request: web.Request, resource_group_name, private_zone_name, record_type, api_version, subscription_id, top=None, recordsetnamesuffix=None) -> web.Response:
    """record_sets_list_by_type

    Lists the record sets of a specified type in a Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param record_type: The type of record sets to enumerate.
    :type record_type: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    :type top: int
    :param recordsetnamesuffix: The suffix label of the record set name to be used to filter the record set enumeration. If this parameter is specified, the returned enumeration will only contain records that end with \&quot;.&lt;recordsetnamesuffix&gt;\&quot;.
    :type recordsetnamesuffix: str

    """
    return web.Response(status=200)


async def record_sets_update(request: web.Request, resource_group_name, private_zone_name, record_type, relative_record_set_name, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """record_sets_update

    Updates a record set within a Private DNS zone.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param private_zone_name: The name of the Private DNS zone (without a terminating dot).
    :type private_zone_name: str
    :param record_type: The type of DNS record in this record set.
    :type record_type: str
    :param relative_record_set_name: The name of the record set, relative to the name of the zone.
    :type relative_record_set_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update operation.
    :type parameters: dict | bytes
    :param if_match: The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    :type if_match: str

    """
    parameters = RecordSet.from_dict(parameters)
    return web.Response(status=200)
