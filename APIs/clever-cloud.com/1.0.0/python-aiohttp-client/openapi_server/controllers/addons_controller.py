from typing import List, Dict
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.addon_migration import AddonMigration
from openapi_server.models.application import Application
from openapi_server.models.body import Body
from openapi_server.models.env import Env
from openapi_server.models.list_env import ListEnv
from openapi_server.models.organisations_id_addons_addon_id_migrations_post_request import OrganisationsIdAddonsAddonIdMigrationsPostRequest
from openapi_server.models.sso import Sso
from openapi_server.models.supernova_instance_view import SupernovaInstanceView
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server import util


async def delete_organisations_id_addons_addon_id_0(request: web.Request, id, addon_id) -> web.Response:
    """delete_organisations_id_addons_addon_id_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addons_addon_id_tags_tag_0(request: web.Request, id, tag, addon_id) -> web.Response:
    """delete_organisations_id_addons_addon_id_tags_tag_0

    

    :param id: 
    :type id: str
    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_addons_addon_id_0(request: web.Request, id, app_id, addon_id) -> web.Response:
    """delete_organisations_id_applications_app_id_addons_addon_id_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_addons_addon_id_0(request: web.Request, addon_id) -> web.Response:
    """delete_self_addons_addon_id_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_addons_addon_id_tags_tag_0(request: web.Request, tag, addon_id) -> web.Response:
    """delete_self_addons_addon_id_tags_tag_0

    

    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_addons_addon_id_0(request: web.Request, app_id, addon_id) -> web.Response:
    """delete_self_applications_app_id_addons_addon_id_0

    

    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_config_provider_0(request: web.Request, configuration_provider_id, body=None) -> web.Response:
    """Get Addon provider configuration

    

    :param configuration_provider_id: Automatically added
    :type configuration_provider_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_config_provider_env_0(request: web.Request, configuration_provider_id, body=None) -> web.Response:
    """Get provider&#39;s addon environment

    

    :param configuration_provider_id: Automatically added
    :type configuration_provider_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_matomo_0(request: web.Request, matomo_id, body=None) -> web.Response:
    """Get Matomo addon

    

    :param matomo_id: Automatically added
    :type matomo_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_addons_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_0(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_applications_0(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_applications_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_env_0(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_env_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_tags_0(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_tags_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_env_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_env_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_addons_0(request: web.Request, ) -> web.Response:
    """Addon

    Get all the addons


    """
    return web.Response(status=200)


async def get_self_addons_addon_id_0(request: web.Request, addon_id) -> web.Response:
    """Specific addon

    Get a specific addon

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_applications_0(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_applications_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_env_0(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_env_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_sso_0(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_sso_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_tags_0(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_tags_0

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_env_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_env_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_instances_get_0(request: web.Request, id, addon_id, deployment_id=None, with_deleted=None) -> web.Response:
    """List instances for this add-on.

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str
    :param deployment_id: 
    :type deployment_id: str
    :param with_deleted: 
    :type with_deleted: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_instances_instance_id_get_0(request: web.Request, instance_id, id, addon_id) -> web.Response:
    """Get a specific instance for {addonId}

    

    :param instance_id: 
    :type instance_id: str
    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_get_0(request: web.Request, id, addon_id) -> web.Response:
    """Get past migrations from add-on.

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_migration_id_get_0(request: web.Request, migration_id, id, addon_id) -> web.Response:
    """Get a given migration

    

    :param migration_id: 
    :type migration_id: str
    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_post_0(request: web.Request, id, addon_id, body) -> web.Response:
    """Start a new add-on migration

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = OrganisationsIdAddonsAddonIdMigrationsPostRequest.from_dict(body)
    return web.Response(status=200)


async def organisations_id_addons_addon_id_sso_get_0(request: web.Request, id, addon_id) -> web.Response:
    """organisations_id_addons_addon_id_sso_get_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_preorders_post_0(request: web.Request, id, body) -> web.Response:
    """organisations_id_addons_preorders_post_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addons_0(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_addons_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_addons_0(request: web.Request, id, app_id, body) -> web.Response:
    """post_organisations_id_applications_app_id_addons_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_self_addons_0(request: web.Request, body) -> web.Response:
    """post_self_addons_0

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_addons_0(request: web.Request, app_id, body) -> web.Response:
    """post_self_applications_app_id_addons_0

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addons_addon_id_0(request: web.Request, id, addon_id, body) -> web.Response:
    """put_organisations_id_addons_addon_id_0

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addons_addon_id_tags_tag_0(request: web.Request, id, tag, addon_id, body) -> web.Response:
    """put_organisations_id_addons_addon_id_tags_tag_0

    

    :param id: 
    :type id: str
    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_0(request: web.Request, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_0

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_plan_0(request: web.Request, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_plan_0

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlan.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_tags_tag_0(request: web.Request, tag, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_tags_tag_0

    

    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def self_addons_preorders_post_0(request: web.Request, body) -> web.Response:
    """self_addons_preorders_post_0

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def update_config_provider_env_0(request: web.Request, configuration_provider_id, body) -> web.Response:
    """Update provider&#39;s addon environment

    

    :param configuration_provider_id: Automatically added
    :type configuration_provider_id: str
    :param body: 
    :type body: List[]

    """
    return web.Response(status=200)


async def vendor_addons_post_0(request: web.Request, ) -> web.Response:
    """vendor_addons_post_0

    


    """
    return web.Response(status=200)
