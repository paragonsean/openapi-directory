from typing import List, Dict
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.application import Application
from openapi_server.models.avatar import Avatar
from openapi_server.models.body import Body
from openapi_server.models.change_password import ChangePassword
from openapi_server.models.conso import Conso
from openapi_server.models.consumer import Consumer
from openapi_server.models.credits import Credits
from openapi_server.models.deployment import Deployment
from openapi_server.models.env import Env
from openapi_server.models.instance import Instance
from openapi_server.models.key import Key
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.secret import Secret
from openapi_server.models.sso import Sso
from openapi_server.models.token import Token
from openapi_server.models.user import User
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_consumer import WannabeConsumer
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server.models.wannabe_user import WannabeUser
from openapi_server import util


async def delete_self_0(request: web.Request, ) -> web.Response:
    """delete_self_0

    


    """
    return web.Response(status=200)


async def delete_self_addons_addon_id_1(request: web.Request, addon_id) -> web.Response:
    """delete_self_addons_addon_id_1

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_addons_addon_id_tags_tag_1(request: web.Request, tag, addon_id) -> web.Response:
    """delete_self_addons_addon_id_tags_tag_1

    

    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_1(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_addons_addon_id_2(request: web.Request, app_id, addon_id) -> web.Response:
    """delete_self_applications_app_id_addons_addon_id_2

    

    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_dependencies_dependency_id_1(request: web.Request, dependency_id, app_id) -> web.Response:
    """delete_self_applications_app_id_dependencies_dependency_id_1

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_deployments_deployment_id_instances_1(request: web.Request, app_id, deployment_id) -> web.Response:
    """delete_self_applications_app_id_deployments_deployment_id_instances_1

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_env_env_name_1(request: web.Request, app_id, env_name) -> web.Response:
    """delete_self_applications_app_id_env_env_name_1

    

    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_instances_1(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_instances_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_tags_tag_1(request: web.Request, app_id, tag) -> web.Response:
    """delete_self_applications_app_id_tags_tag_1

    

    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_vhosts_domain_1(request: web.Request, app_id, domain) -> web.Response:
    """delete_self_applications_app_id_vhosts_domain_1

    

    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_vhosts_favourite_1(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_vhosts_favourite_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_consumers_key_0(request: web.Request, key) -> web.Response:
    """delete_self_consumers_key_0

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def delete_self_emails_email_0(request: web.Request, email) -> web.Response:
    """delete_self_emails_email_0

    

    :param email: 
    :type email: str

    """
    return web.Response(status=200)


async def delete_self_keys_key_0(request: web.Request, key) -> web.Response:
    """delete_self_keys_key_0

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def delete_self_payments_billings_bid_1(request: web.Request, bid) -> web.Response:
    """delete_self_payments_billings_bid_1

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def delete_self_payments_methods_mid_1(request: web.Request, m_id) -> web.Response:
    """delete_self_payments_methods_mid_1

    

    :param m_id: 
    :type m_id: str

    """
    return web.Response(status=200)


async def delete_self_payments_recurring_1(request: web.Request, ) -> web.Response:
    """delete_self_payments_recurring_1

    


    """
    return web.Response(status=200)


async def delete_self_tokens_0(request: web.Request, ) -> web.Response:
    """delete_self_tokens_0

    


    """
    return web.Response(status=200)


async def delete_self_tokens_token_0(request: web.Request, token) -> web.Response:
    """delete_self_tokens_token_0

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_self_0(request: web.Request, ) -> web.Response:
    """

    Get information about yourself


    """
    return web.Response(status=200)


async def get_self_addons_1(request: web.Request, ) -> web.Response:
    """Addon

    Get all the addons


    """
    return web.Response(status=200)


async def get_self_addons_addon_id_1(request: web.Request, addon_id) -> web.Response:
    """Specific addon

    Get a specific addon

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_applications_2(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_applications_2

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_env_1(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_env_1

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_sso_1(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_sso_1

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_tags_1(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_tags_1

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_applications_1(request: web.Request, ) -> web.Response:
    """get_self_applications_1

    


    """
    return web.Response(status=200)


async def get_self_applications_app_id_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_2(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_2

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_env_2(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_env_2

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_dependencies_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_dependencies_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_dependencies_dependency_id_1(request: web.Request, dependency_id, app_id, body) -> web.Response:
    """get_self_applications_app_id_dependencies_dependency_id_1

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def get_self_applications_app_id_dependents_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_dependents_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_deployments_1(request: web.Request, app_id, limit=None, offset=None, action=None) -> web.Response:
    """get_self_applications_app_id_deployments_1

    

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


async def get_self_applications_app_id_env_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_env_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_instances_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_instances_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_tags_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_tags_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_vhosts_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_vhosts_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_vhosts_favourite_1(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_vhosts_favourite_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_confirmation_email_0(request: web.Request, ) -> web.Response:
    """get_self_confirmation_email_0

    


    """
    return web.Response(status=200)


async def get_self_consumers_0(request: web.Request, ) -> web.Response:
    """get_self_consumers_0

    


    """
    return web.Response(status=200)


async def get_self_consumers_key_0(request: web.Request, key) -> web.Response:
    """get_self_consumers_key_0

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_self_consumers_key_secret_0(request: web.Request, key) -> web.Response:
    """get_self_consumers_key_secret_0

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_self_consumptions_0(request: web.Request, app_id=None, _from=None, to=None) -> web.Response:
    """get_self_consumptions_0

    

    :param app_id: 
    :type app_id: str
    :param _from: 
    :type _from: str
    :param to: 
    :type to: str

    """
    return web.Response(status=200)


async def get_self_credits_0(request: web.Request, ) -> web.Response:
    """get_self_credits_0

    


    """
    return web.Response(status=200)


async def get_self_emails_0(request: web.Request, ) -> web.Response:
    """get_self_emails_0

    


    """
    return web.Response(status=200)


async def get_self_id_0(request: web.Request, ) -> web.Response:
    """get_self_id_0

    


    """
    return web.Response(status=200)


async def get_self_instances_0(request: web.Request, ) -> web.Response:
    """get_self_instances_0

    


    """
    return web.Response(status=200)


async def get_self_keys_0(request: web.Request, ) -> web.Response:
    """get_self_keys_0

    


    """
    return web.Response(status=200)


async def get_self_payment_info_0(request: web.Request, ) -> web.Response:
    """get_self_payment_info_0

    


    """
    return web.Response(status=200)


async def get_self_payments_billings_1(request: web.Request, ) -> web.Response:
    """get_self_payments_billings_1

    


    """
    return web.Response(status=200)


async def get_self_payments_billings_bid_1(request: web.Request, bid) -> web.Response:
    """get_self_payments_billings_bid_1

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def get_self_payments_billings_bid_pdf_1(request: web.Request, bid, token=None) -> web.Response:
    """get_self_payments_billings_bid_pdf_1

    

    :param bid: 
    :type bid: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_self_payments_fullprice_price_1(request: web.Request, price) -> web.Response:
    """get_self_payments_fullprice_price_1

    

    :param price: 
    :type price: str

    """
    return web.Response(status=200)


async def get_self_payments_methods_1(request: web.Request, ) -> web.Response:
    """get_self_payments_methods_1

    


    """
    return web.Response(status=200)


async def get_self_tokens_0(request: web.Request, ) -> web.Response:
    """get_self_tokens_0

    


    """
    return web.Response(status=200)


async def get_self_validate_email_0(request: web.Request, validation_key=None) -> web.Response:
    """get_self_validate_email_0

    

    :param validation_key: 
    :type validation_key: str

    """
    return web.Response(status=200)


async def post_self_addons_1(request: web.Request, body) -> web.Response:
    """post_self_addons_1

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_1(request: web.Request, body) -> web.Response:
    """post_self_applications_1

    Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_addons_2(request: web.Request, app_id, body) -> web.Response:
    """post_self_applications_app_id_addons_2

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_instances_1(request: web.Request, app_id, commit=None) -> web.Response:
    """post_self_applications_app_id_instances_1

    

    :param app_id: 
    :type app_id: str
    :param commit: 
    :type commit: str

    """
    return web.Response(status=200)


async def post_self_consumers_0(request: web.Request, body) -> web.Response:
    """post_self_consumers_0

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def post_self_payments_billings_1(request: web.Request, ) -> web.Response:
    """post_self_payments_billings_1

    


    """
    return web.Response(status=200)


async def post_self_payments_methods_1(request: web.Request, ) -> web.Response:
    """post_self_payments_methods_1

    


    """
    return web.Response(status=200)


async def put_self_0(request: web.Request, body) -> web.Response:
    """put_self_0

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeUser.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_1(request: web.Request, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_1

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_plan_1(request: web.Request, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_plan_1

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlan.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_tags_tag_1(request: web.Request, tag, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_tags_tag_1

    

    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_1(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_1

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_env_1(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_env_1

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_env_env_name_1(request: web.Request, app_id, env_name, body) -> web.Response:
    """put_self_applications_app_id_env_env_name_1

    

    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_tags_tag_1(request: web.Request, app_id, tag, body) -> web.Response:
    """put_self_applications_app_id_tags_tag_1

    

    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_vhosts_domain_1(request: web.Request, app_id, domain, body) -> web.Response:
    """put_self_applications_app_id_vhosts_domain_1

    

    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_vhosts_favourite_1(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_vhosts_favourite_1

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_self_avatar_0(request: web.Request, body) -> web.Response:
    """put_self_avatar_0

    

    :param body: 
    :type body: dict | bytes

    """
    body = Avatar.from_dict(body)
    return web.Response(status=200)


async def put_self_change_password_0(request: web.Request, ) -> web.Response:
    """put_self_change_password_0

    


    """
    return web.Response(status=200)


async def put_self_consumers_key_0(request: web.Request, key, body) -> web.Response:
    """put_self_consumers_key_0

    

    :param key: 
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def put_self_emails_email_0(request: web.Request, email, body) -> web.Response:
    """put_self_emails_email_0

    

    :param email: 
    :type email: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_keys_key_0(request: web.Request, key, body) -> web.Response:
    """put_self_keys_key_0

    

    :param key: 
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_payments_billings_bid_1(request: web.Request, bid) -> web.Response:
    """put_self_payments_billings_bid_1

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def self_addons_preorders_post_1(request: web.Request, body) -> web.Response:
    """self_addons_preorders_post_1

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def self_applications_app_id_branch_put_1(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_branch_put_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_branches_get_1(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_branches_get_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_buildflavor_put_1(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_buildflavor_put_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_dependencies_env_get_1(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_dependencies_env_get_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_deployments_deployment_id_get_1(request: web.Request, app_id, deployment_id) -> web.Response:
    """self_applications_app_id_deployments_deployment_id_get_1

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_exposed_env_get_1(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_exposed_env_get_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_exposed_env_put_1(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_exposed_env_put_1

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_instances_instance_id_get_1(request: web.Request, instance_id, app_id) -> web.Response:
    """self_applications_app_id_instances_instance_id_get_1

    

    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_cli_tokens_get_0(request: web.Request, cli_token=None) -> web.Response:
    """self_cli_tokens_get_0

    

    :param cli_token: 
    :type cli_token: str

    """
    return web.Response(status=200)


async def self_mfa_kind_backupcodes_get_0(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_backupcodes_get_0

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_confirmation_post_0(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_confirmation_post_0

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_delete_0(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_delete_0

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_post_0(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_post_0

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_put_0(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_put_0

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_payments_methods_default_get_1(request: web.Request, ) -> web.Response:
    """self_payments_methods_default_get_1

    


    """
    return web.Response(status=200)


async def self_payments_methods_default_put_1(request: web.Request, ) -> web.Response:
    """self_payments_methods_default_put_1

    


    """
    return web.Response(status=200)


async def self_payments_monthlyinvoice_get_1(request: web.Request, ) -> web.Response:
    """self_payments_monthlyinvoice_get_1

    


    """
    return web.Response(status=200)


async def self_payments_monthlyinvoice_maxcredit_put_1(request: web.Request, ) -> web.Response:
    """self_payments_monthlyinvoice_maxcredit_put_1

    


    """
    return web.Response(status=200)


async def self_payments_recurring_get_1(request: web.Request, ) -> web.Response:
    """self_payments_recurring_get_1

    


    """
    return web.Response(status=200)


async def self_payments_tokens_stripe_get_1(request: web.Request, ) -> web.Response:
    """self_payments_tokens_stripe_get_1

    


    """
    return web.Response(status=200)
