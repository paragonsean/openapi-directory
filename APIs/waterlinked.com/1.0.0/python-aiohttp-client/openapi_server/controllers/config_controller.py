from typing import List, Dict
from aiohttp import web

from openapi_server.models.modify_antenna_config_config_payload import ModifyAntennaConfigConfigPayload
from openapi_server.models.modify_config_payload import ModifyConfigPayload
from openapi_server.models.modify_ip_config_payload import ModifyIPConfigPayload
from openapi_server.models.modify_receiver_config_payload import ModifyReceiverConfigPayload
from openapi_server.models.modify_wifi_config_payload import ModifyWIFIConfigPayload
from openapi_server.models.waterlinked_antenna_config import WaterlinkedAntennaConfig
from openapi_server.models.waterlinked_configuration import WaterlinkedConfiguration
from openapi_server.models.waterlinked_ip_config import WaterlinkedIpConfig
from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.waterlinked_receiver import WaterlinkedReceiver
from openapi_server.models.waterlinked_wifi_config import WaterlinkedWifiConfig
from openapi_server import util


async def config_get(request: web.Request, ) -> web.Response:
    """Get config

    Get generic configuration


    """
    return web.Response(status=200)


async def config_get_antenna_config(request: web.Request, ) -> web.Response:
    """GetAntennaConfig config

    Get Antenna configuration


    """
    return web.Response(status=200)


async def config_get_ip(request: web.Request, ) -> web.Response:
    """GetIP config

    Get IP configuration


    """
    return web.Response(status=200)


async def config_get_wifi(request: web.Request, ) -> web.Response:
    """GetWIFI config

    Get WIFI configuration


    """
    return web.Response(status=200)


async def config_list_receiver(request: web.Request, ) -> web.Response:
    """ListReceiver config

    (Re)Load current receiver settings and return them


    """
    return web.Response(status=200)


async def config_modify(request: web.Request, payload) -> web.Response:
    """Modify config

    Modify generic configuration

    :param payload: Configuration parameters
    :type payload: dict | bytes

    """
    payload = ModifyConfigPayload.from_dict(payload)
    return web.Response(status=200)


async def config_modify_antenna_config(request: web.Request, payload) -> web.Response:
    """ModifyAntennaConfig config

    Modify Antenna configuration

    :param payload: Configuration parameters for antenna set up
    :type payload: dict | bytes

    """
    payload = ModifyAntennaConfigConfigPayload.from_dict(payload)
    return web.Response(status=200)


async def config_modify_ip(request: web.Request, payload) -> web.Response:
    """ModifyIP config

    Modify IP configuration

    :param payload: Configuration parameters
    :type payload: dict | bytes

    """
    payload = ModifyIPConfigPayload.from_dict(payload)
    return web.Response(status=200)


async def config_modify_receiver(request: web.Request, id, payload) -> web.Response:
    """ModifyReceiver config

    Modify receiver configuration, does not apply the change until generic modify is called. Calling list will discard changes

    :param id: Identifier
    :type id: int
    :param payload: A receiver configuration
    :type payload: dict | bytes

    """
    payload = ModifyReceiverConfigPayload.from_dict(payload)
    return web.Response(status=200)


async def config_modify_wifi(request: web.Request, payload) -> web.Response:
    """ModifyWIFI config

    Modify WIFI configuration

    :param payload: Configuration parameters
    :type payload: dict | bytes

    """
    payload = ModifyWIFIConfigPayload.from_dict(payload)
    return web.Response(status=200)


async def config_show_receiver(request: web.Request, id) -> web.Response:
    """ShowReceiver config

    Get receiver configuration by id

    :param id: Identifier
    :type id: int

    """
    return web.Response(status=200)
