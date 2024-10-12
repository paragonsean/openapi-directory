from typing import List, Dict
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.app_instance import AppInstance
from openapi_server.models.application import Application
from openapi_server.models.body import Body
from openapi_server.models.deployment import Deployment
from openapi_server.models.env import Env
from openapi_server.models.instance import Instance
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server import util


async def delete_organisations_id_applications_app_id_0(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_addons_addon_id_1(request: web.Request, id, app_id, addon_id) -> web.Response:
    """delete_organisations_id_applications_app_id_addons_addon_id_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_dependencies_dependency_id_0(request: web.Request, dependency_id, app_id, id) -> web.Response:
    """delete_organisations_id_applications_app_id_dependencies_dependency_id_0

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_deployments_deployment_id_instances_0(request: web.Request, id, app_id, deployment_id) -> web.Response:
    """delete_organisations_id_applications_app_id_deployments_deployment_id_instances_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_env_env_name_0(request: web.Request, id, app_id, env_name) -> web.Response:
    """delete_organisations_id_applications_app_id_env_env_name_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_instances_0(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_instances_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_tags_tag_0(request: web.Request, id, app_id, tag) -> web.Response:
    """delete_organisations_id_applications_app_id_tags_tag_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_vhosts_domain_0(request: web.Request, id, app_id, domain) -> web.Response:
    """delete_organisations_id_applications_app_id_vhosts_domain_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_vhosts_favourite_0(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_vhosts_favourite_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_0(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_addons_addon_id_1(request: web.Request, app_id, addon_id) -> web.Response:
    """delete_self_applications_app_id_addons_addon_id_1

    

    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_dependencies_dependency_id_0(request: web.Request, dependency_id, app_id) -> web.Response:
    """delete_self_applications_app_id_dependencies_dependency_id_0

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_deployments_deployment_id_instances_0(request: web.Request, app_id, deployment_id) -> web.Response:
    """delete_self_applications_app_id_deployments_deployment_id_instances_0

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_env_env_name_0(request: web.Request, app_id, env_name) -> web.Response:
    """delete_self_applications_app_id_env_env_name_0

    

    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_instances_0(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_instances_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_tags_tag_0(request: web.Request, app_id, tag) -> web.Response:
    """delete_self_applications_app_id_tags_tag_0

    

    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_vhosts_domain_0(request: web.Request, app_id, domain) -> web.Response:
    """delete_self_applications_app_id_vhosts_domain_0

    

    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_vhosts_favourite_0(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_vhosts_favourite_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_github_applications_0(request: web.Request, ) -> web.Response:
    """get_github_applications_0

    


    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_applications_1(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_applications_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_applications_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_env_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_env_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_dependencies_0(request: web.Request, app_id, id) -> web.Response:
    """get_organisations_id_applications_app_id_dependencies_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_dependents_0(request: web.Request, app_id, id) -> web.Response:
    """get_organisations_id_applications_app_id_dependents_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_deployments_0(request: web.Request, id, app_id, limit=None, offset=None, action=None) -> web.Response:
    """get_organisations_id_applications_app_id_deployments_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param limit: 
    :type limit: str
    :param offset: 
    :type offset: str
    :param action: 
    :type action: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_env_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_env_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_instances_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_instances_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_tags_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_tags_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_vhosts_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_vhosts_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_vhosts_favourite_0(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_vhosts_favourite_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_applications_1(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_applications_1

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_applications_0(request: web.Request, ) -> web.Response:
    """get_self_applications_0

    


    """
    return web.Response(status=200)


async def get_self_applications_app_id_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_env_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_env_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_dependencies_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_dependencies_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_dependencies_dependency_id_0(request: web.Request, dependency_id, app_id, body) -> web.Response:
    """get_self_applications_app_id_dependencies_dependency_id_0

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def get_self_applications_app_id_dependents_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_dependents_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_deployments_0(request: web.Request, app_id, limit=None, offset=None, action=None) -> web.Response:
    """get_self_applications_app_id_deployments_0

    

    :param app_id: 
    :type app_id: str
    :param limit: 
    :type limit: str
    :param offset: 
    :type offset: str
    :param action: 
    :type action: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_env_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_env_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_instances_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_instances_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_tags_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_tags_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_vhosts_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_vhosts_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_vhosts_favourite_0(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_vhosts_favourite_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_users_id_applications_0(request: web.Request, id) -> web.Response:
    """get_users_id_applications_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_branch_put_0(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_branch_put_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_branches_get_0(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_branches_get_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_buildflavor_put_0(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_buildflavor_put_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_dependencies_env_get_0(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_dependencies_env_get_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_deployments_deployment_id_get_0(request: web.Request, app_id, deployment_id, id) -> web.Response:
    """organisations_id_applications_app_id_deployments_deployment_id_get_0

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_exposed_env_get_0(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_exposed_env_get_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_exposed_env_put_0(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_exposed_env_put_0

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_instances_instance_id_get_0(request: web.Request, instance_id, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_instances_instance_id_get_0

    

    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_organisations_id_applications_0(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_applications_0

    Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_addons_1(request: web.Request, id, app_id, body) -> web.Response:
    """post_organisations_id_applications_app_id_addons_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_instances_0(request: web.Request, id, app_id, commit=None) -> web.Response:
    """post_organisations_id_applications_app_id_instances_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param commit: 
    :type commit: str

    """
    return web.Response(status=200)


async def post_self_applications_0(request: web.Request, body) -> web.Response:
    """post_self_applications_0

    Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_addons_1(request: web.Request, app_id, body) -> web.Response:
    """post_self_applications_app_id_addons_1

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_instances_0(request: web.Request, app_id, commit=None) -> web.Response:
    """post_self_applications_app_id_instances_0

    

    :param app_id: 
    :type app_id: str
    :param commit: 
    :type commit: str

    """
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_0(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_dependencies_dependency_id_0(request: web.Request, dependency_id, app_id, id, body) -> web.Response:
    """put_organisations_id_applications_app_id_dependencies_dependency_id_0

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_env_0(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_env_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_env_env_name_0(request: web.Request, id, app_id, env_name, body) -> web.Response:
    """put_organisations_id_applications_app_id_env_env_name_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_tags_tag_0(request: web.Request, id, app_id, tag, body) -> web.Response:
    """put_organisations_id_applications_app_id_tags_tag_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_vhosts_domain_0(request: web.Request, id, app_id, domain, body) -> web.Response:
    """put_organisations_id_applications_app_id_vhosts_domain_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_vhosts_favourite_0(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_vhosts_favourite_0

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_0(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_0

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_env_0(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_env_0

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_env_env_name_0(request: web.Request, app_id, env_name, body) -> web.Response:
    """put_self_applications_app_id_env_env_name_0

    

    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_tags_tag_0(request: web.Request, app_id, tag, body) -> web.Response:
    """put_self_applications_app_id_tags_tag_0

    

    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_vhosts_domain_0(request: web.Request, app_id, domain, body) -> web.Response:
    """put_self_applications_app_id_vhosts_domain_0

    

    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_vhosts_favourite_0(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_vhosts_favourite_0

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def self_applications_app_id_branch_put_0(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_branch_put_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_branches_get_0(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_branches_get_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_buildflavor_put_0(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_buildflavor_put_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_dependencies_env_get_0(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_dependencies_env_get_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_deployments_deployment_id_get_0(request: web.Request, app_id, deployment_id) -> web.Response:
    """self_applications_app_id_deployments_deployment_id_get_0

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_exposed_env_get_0(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_exposed_env_get_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_exposed_env_put_0(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_exposed_env_put_0

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_instances_instance_id_get_0(request: web.Request, instance_id, app_id) -> web.Response:
    """self_applications_app_id_instances_instance_id_get_0

    

    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)
