from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.inventory_script_info import InventoryScriptInfo
from openapi_server.models.script_instance_custom_user_data import ScriptInstanceCustomUserData
from openapi_server.models.script_instance_details import ScriptInstanceDetails
from openapi_server import util


async def scripts_instances_get(request: web.Request, team_id=None) -> web.Response:
    """Returns all script instances of the SIGNL4 team

    Returns all script instances in the subscription.

    :param team_id: 
    :type team_id: str

    """
    return web.Response(status=200)


async def scripts_instances_instance_id_data_put(request: web.Request, instance_id, body=None) -> web.Response:
    """Updates custom data of a given script instance which includes its display name.

    Updates the specified script instance.

    :param instance_id: InstanceId of the script to be updated.
    :type instance_id: str
    :param body: Script instance to be updated.
    :type body: dict | bytes

    """
    body = ScriptInstanceCustomUserData.from_dict(body)
    return web.Response(status=200)


async def scripts_instances_instance_id_delete(request: web.Request, instance_id) -> web.Response:
    """Deletes a script instance.

    Gets the script instance specified by the passed instance id.

    :param instance_id: Instance Id of script instance to be returned.
    :type instance_id: str

    """
    return web.Response(status=200)


async def scripts_instances_instance_id_disable_post(request: web.Request, instance_id) -> web.Response:
    """Disables a given script instance.

    

    :param instance_id: Id of the instance to be disabled.
    :type instance_id: str

    """
    return web.Response(status=200)


async def scripts_instances_instance_id_enable_post(request: web.Request, instance_id) -> web.Response:
    """Enables a script instance.

    

    :param instance_id: Id of the instance to be enabled.
    :type instance_id: str

    """
    return web.Response(status=200)


async def scripts_instances_instance_id_get(request: web.Request, instance_id) -> web.Response:
    """Returns all information about a given script instance which includes its runtime status.

    Gets the script instance specified by the passed instance id.

    :param instance_id: Instance Id of script instance to be returned.
    :type instance_id: str

    """
    return web.Response(status=200)


async def scripts_instances_instance_id_put(request: web.Request, instance_id, body=None) -> web.Response:
    """Updates a given script instance, typically used for updating the configuration of a script.

    Updates the specified script instance.

    :param instance_id: InstanceId of the script to be updated.
    :type instance_id: str
    :param body: Script instance to be updated.
    :type body: dict | bytes

    """
    body = ScriptInstanceDetails.from_dict(body)
    return web.Response(status=200)


async def scripts_instances_post(request: web.Request, body=None) -> web.Response:
    """Creates a new script instance in the in the SIGNL4 team.

    Creates a new script instance of the script specified in the request body.

    :param body: Script instance to be created.
    :type body: dict | bytes

    """
    body = ScriptInstanceDetails.from_dict(body)
    return web.Response(status=200)


async def scripts_inventory_get(request: web.Request, ) -> web.Response:
    """Returns all available inventory scripts which can be added to a SIGNL4 subscription.

    Returns all available inventory scripts which can be added to a SIGNL4 subscription.


    """
    return web.Response(status=200)


async def scripts_inventory_parsed_get(request: web.Request, language=None) -> web.Response:
    """Returns all inventory scripts.

    

    :param language: 
    :type language: str

    """
    return web.Response(status=200)


async def scripts_inventory_parsed_script_id_get(request: web.Request, script_id, language=None) -> web.Response:
    """Returns an inventory script by its id.

    Gets the script specified by the passed script id.

    :param script_id: The Id of the script to be returned.
    :type script_id: str
    :param language: 
    :type language: str

    """
    return web.Response(status=200)
