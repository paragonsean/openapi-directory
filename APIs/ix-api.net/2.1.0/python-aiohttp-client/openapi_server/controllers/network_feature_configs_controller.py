from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.network_feature_config import NetworkFeatureConfig
from openapi_server.models.network_feature_config_request import NetworkFeatureConfigRequest
from openapi_server.models.network_feature_config_update import NetworkFeatureConfigUpdate
from openapi_server.models.network_feature_config_update_partial import NetworkFeatureConfigUpdatePartial
from openapi_server import util


async def network_feature_configs_create(request: web.Request, body=None) -> web.Response:
    """network_feature_configs_create

    Create a configuration for a &#x60;NetworkFeature&#x60; defined in the &#x60;NetworkFeature&#x60;s collection.

    :param body: Polymorphic Network Feature Config Request
    :type body: dict | bytes

    """
    body = NetworkFeatureConfigRequest.from_dict(body)
    return web.Response(status=200)


async def network_feature_configs_destroy(request: web.Request, id) -> web.Response:
    """network_feature_configs_destroy

    Remove a network feature config.  The network feature config will be marked as &#x60;decommission_requested&#x60;. Decommissioning a network feature config will not cascade to related services or service configs.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def network_feature_configs_list(request: web.Request, id=None, state=None, state__is_not=None, managing_account=None, consuming_account=None, external_ref=None, type=None, service_config=None, network_feature=None) -> web.Response:
    """network_feature_configs_list

    Get all network feature configs.

    :param id: Filter by id
    :type id: List[str]
    :param state: Filter by state
    :type state: str
    :param state__is_not: Filter by state__is_not
    :type state__is_not: str
    :param managing_account: Filter by managing_account
    :type managing_account: str
    :param consuming_account: Filter by consuming_account
    :type consuming_account: str
    :param external_ref: Filter by external_ref
    :type external_ref: str
    :param type: Filter by type
    :type type: str
    :param service_config: Filter by service_config
    :type service_config: str
    :param network_feature: Filter by network_feature
    :type network_feature: str

    """
    return web.Response(status=200)


async def network_feature_configs_partial_update(request: web.Request, id, body=None) -> web.Response:
    """network_feature_configs_partial_update

    Update parts of a network feature configuration

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Network Feauture Config Update
    :type body: dict | bytes

    """
    body = NetworkFeatureConfigUpdatePartial.from_dict(body)
    return web.Response(status=200)


async def network_feature_configs_read(request: web.Request, id) -> web.Response:
    """network_feature_configs_read

    Get a single network feature config.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def network_feature_configs_update(request: web.Request, id, body=None) -> web.Response:
    """network_feature_configs_update

    Update a network feature configuration

    :param id: Get by id
    :type id: str
    :param body: Polymorphic Network Feauture Config Update
    :type body: dict | bytes

    """
    body = NetworkFeatureConfigUpdate.from_dict(body)
    return web.Response(status=200)
