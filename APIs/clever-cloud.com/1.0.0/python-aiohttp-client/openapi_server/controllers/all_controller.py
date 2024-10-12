from typing import List, Dict
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.addon_migration import AddonMigration
from openapi_server.models.addon_provider_sso import AddonProviderSso
from openapi_server.models.app_instance import AppInstance
from openapi_server.models.application import Application
from openapi_server.models.avatar import Avatar
from openapi_server.models.body import Body
from openapi_server.models.change_password import ChangePassword
from openapi_server.models.conso import Conso
from openapi_server.models.consumer import Consumer
from openapi_server.models.country import Country
from openapi_server.models.credits import Credits
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_summary import DeploymentSummary
from openapi_server.models.env import Env
from openapi_server.models.error import Error
from openapi_server.models.feature import Feature
from openapi_server.models.instance import Instance
from openapi_server.models.key import Key
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.organisation import Organisation
from openapi_server.models.organisations_id_addons_addon_id_migrations_post_request import OrganisationsIdAddonsAddonIdMigrationsPostRequest
from openapi_server.models.payment_data import PaymentData
from openapi_server.models.payment_provider import PaymentProvider
from openapi_server.models.plan import Plan
from openapi_server.models.provider import Provider
from openapi_server.models.rights import Rights
from openapi_server.models.schema1 import Schema1
from openapi_server.models.schema2 import Schema2
from openapi_server.models.secret import Secret
from openapi_server.models.sso import Sso
from openapi_server.models.summary import Summary
from openapi_server.models.supernova_instance_view import SupernovaInstanceView
from openapi_server.models.token import Token
from openapi_server.models.transaction_id import TransactionId
from openapi_server.models.user import User
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_addon_billing import WannabeAddonBilling
from openapi_server.models.wannabe_addon_provider import WannabeAddonProvider
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_consumer import WannabeConsumer
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server.models.wannabe_feature import WannabeFeature
from openapi_server.models.wannabe_organisation import WannabeOrganisation
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server.models.wannabe_plan_feature import WannabePlanFeature
from openapi_server.models.wannabe_user import WannabeUser
from openapi_server.models.zone import Zone
from openapi_server import util


async def application_app_id_environment_get(request: web.Request, app_id, token=None) -> web.Response:
    """application_app_id_environment_get

    

    :param app_id: 
    :type app_id: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def application_app_id_environment_put(request: web.Request, app_id, token=None) -> web.Response:
    """application_app_id_environment_put

    

    :param app_id: 
    :type app_id: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def create_matomo(request: web.Request, body=None) -> web.Response:
    """Create Matomo addon

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_network_group(request: web.Request, owner_id, body=None) -> web.Response:
    """Create Network Group

    Creates a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_network_group_external_peer(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Add external peer

    Adds an external peer to a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_network_group_member(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Add member

    Adds a member to a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Schema2.from_dict(body)
    return web.Response(status=200)


async def delete_github_link(request: web.Request, ) -> web.Response:
    """delete_github_link

    


    """
    return web.Response(status=200)


async def delete_matomo(request: web.Request, matomo_id, body=None) -> web.Response:
    """Delete Matomo addon

    

    :param matomo_id: Automatically added
    :type matomo_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def delete_network_group(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Delete Network Group

    Deletes a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_network_group_external_peer(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Remove external peer

    Removes an external peer from a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_network_group_member(request: web.Request, owner_id, network_group_id, member_id, body=None) -> web.Response:
    """Remove member

    Removes a member from a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param member_id: Automatically added
    :type member_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_network_group_peer(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Remove peer

    Removes a peer from a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_organisations_id(request: web.Request, id) -> web.Response:
    """delete_organisations_id

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addonproviders_provider_id_features_feature_id(request: web.Request, id, feature_id, provider_id) -> web.Response:
    """delete_organisations_id_addonproviders_provider_id_features_feature_id

    

    :param id: 
    :type id: str
    :param feature_id: 
    :type feature_id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addonproviders_provider_id_plans_plan_id(request: web.Request, id, provider_id, plan_id) -> web.Response:
    """delete_organisations_id_addonproviders_provider_id_plans_plan_id

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name(request: web.Request, id, feature_name, provider_id, plan_id) -> web.Response:
    """delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name

    

    :param id: 
    :type id: str
    :param feature_name: 
    :type feature_name: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addons_addon_id(request: web.Request, id, addon_id) -> web.Response:
    """delete_organisations_id_addons_addon_id

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addons_addon_id_tags_tag(request: web.Request, id, tag, addon_id) -> web.Response:
    """delete_organisations_id_addons_addon_id_tags_tag

    

    :param id: 
    :type id: str
    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_addons_addon_id(request: web.Request, id, app_id, addon_id) -> web.Response:
    """delete_organisations_id_applications_app_id_addons_addon_id

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_dependencies_dependency_id(request: web.Request, dependency_id, app_id, id) -> web.Response:
    """delete_organisations_id_applications_app_id_dependencies_dependency_id

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_deployments_deployment_id_instances(request: web.Request, id, app_id, deployment_id) -> web.Response:
    """delete_organisations_id_applications_app_id_deployments_deployment_id_instances

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_env_env_name(request: web.Request, id, app_id, env_name) -> web.Response:
    """delete_organisations_id_applications_app_id_env_env_name

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_instances(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_instances

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_tags_tag(request: web.Request, id, app_id, tag) -> web.Response:
    """delete_organisations_id_applications_app_id_tags_tag

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_vhosts_domain(request: web.Request, id, app_id, domain) -> web.Response:
    """delete_organisations_id_applications_app_id_vhosts_domain

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_vhosts_favourite(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_vhosts_favourite

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_consumers_key(request: web.Request, id, key) -> web.Response:
    """delete_organisations_id_consumers_key

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def delete_organisations_id_members_user_id(request: web.Request, id, user_id) -> web.Response:
    """delete_organisations_id_members_user_id

    

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_payments_billings_bid(request: web.Request, id, bid) -> web.Response:
    """delete_organisations_id_payments_billings_bid

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def delete_organisations_id_payments_recurring(request: web.Request, id) -> web.Response:
    """delete_organisations_id_payments_recurring

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_self(request: web.Request, ) -> web.Response:
    """delete_self

    


    """
    return web.Response(status=200)


async def delete_self_addons_addon_id(request: web.Request, addon_id) -> web.Response:
    """delete_self_addons_addon_id

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_addons_addon_id_tags_tag(request: web.Request, tag, addon_id) -> web.Response:
    """delete_self_addons_addon_id_tags_tag

    

    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_addons_addon_id(request: web.Request, app_id, addon_id) -> web.Response:
    """delete_self_applications_app_id_addons_addon_id

    

    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_dependencies_dependency_id(request: web.Request, dependency_id, app_id) -> web.Response:
    """delete_self_applications_app_id_dependencies_dependency_id

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_deployments_deployment_id_instances(request: web.Request, app_id, deployment_id) -> web.Response:
    """delete_self_applications_app_id_deployments_deployment_id_instances

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_env_env_name(request: web.Request, app_id, env_name) -> web.Response:
    """delete_self_applications_app_id_env_env_name

    

    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_instances(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_instances

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_tags_tag(request: web.Request, app_id, tag) -> web.Response:
    """delete_self_applications_app_id_tags_tag

    

    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_vhosts_domain(request: web.Request, app_id, domain) -> web.Response:
    """delete_self_applications_app_id_vhosts_domain

    

    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str

    """
    return web.Response(status=200)


async def delete_self_applications_app_id_vhosts_favourite(request: web.Request, app_id) -> web.Response:
    """delete_self_applications_app_id_vhosts_favourite

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_self_consumers_key(request: web.Request, key) -> web.Response:
    """delete_self_consumers_key

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def delete_self_emails_email(request: web.Request, email) -> web.Response:
    """delete_self_emails_email

    

    :param email: 
    :type email: str

    """
    return web.Response(status=200)


async def delete_self_keys_key(request: web.Request, key) -> web.Response:
    """delete_self_keys_key

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def delete_self_payments_billings_bid(request: web.Request, bid) -> web.Response:
    """delete_self_payments_billings_bid

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def delete_self_payments_methods_mid(request: web.Request, m_id) -> web.Response:
    """delete_self_payments_methods_mid

    

    :param m_id: 
    :type m_id: str

    """
    return web.Response(status=200)


async def delete_self_payments_recurring(request: web.Request, ) -> web.Response:
    """delete_self_payments_recurring

    


    """
    return web.Response(status=200)


async def delete_self_tokens(request: web.Request, ) -> web.Response:
    """delete_self_tokens

    


    """
    return web.Response(status=200)


async def delete_self_tokens_token(request: web.Request, token) -> web.Response:
    """delete_self_tokens_token

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def events_event_socket_get(request: web.Request, ) -> web.Response:
    """events_event_socket_get

    Retrieve events as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message


    """
    return web.Response(status=200)


async def get_config_provider(request: web.Request, configuration_provider_id, body=None) -> web.Response:
    """Get Addon provider configuration

    

    :param configuration_provider_id: Automatically added
    :type configuration_provider_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_config_provider_env(request: web.Request, configuration_provider_id, body=None) -> web.Response:
    """Get provider&#39;s addon environment

    

    :param configuration_provider_id: Automatically added
    :type configuration_provider_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_github(request: web.Request, ) -> web.Response:
    """get_github

    


    """
    return web.Response(status=200)


async def get_github_applications(request: web.Request, ) -> web.Response:
    """get_github_applications

    


    """
    return web.Response(status=200)


async def get_github_callback(request: web.Request, code=None, state=None, error=None, error_description=None, error_uri=None, cookie=None) -> web.Response:
    """get_github_callback

    

    :param code: 
    :type code: str
    :param state: 
    :type state: str
    :param error: 
    :type error: str
    :param error_description: 
    :type error_description: str
    :param error_uri: 
    :type error_uri: str
    :param cookie: 
    :type cookie: str

    """
    return web.Response(status=200)


async def get_github_emails(request: web.Request, ) -> web.Response:
    """get_github_emails

    


    """
    return web.Response(status=200)


async def get_github_keys(request: web.Request, ) -> web.Response:
    """get_github_keys

    


    """
    return web.Response(status=200)


async def get_github_link(request: web.Request, transaction_id=None, redirect_url=None) -> web.Response:
    """get_github_link

    

    :param transaction_id: From GET /github
    :type transaction_id: str
    :param redirect_url: 
    :type redirect_url: str

    """
    return web.Response(status=200)


async def get_github_login(request: web.Request, redirect_url=None, from_authorize=None) -> web.Response:
    """get_github_login

    

    :param redirect_url: 
    :type redirect_url: str
    :param from_authorize: 
    :type from_authorize: str

    """
    return web.Response(status=200)


async def get_github_signup(request: web.Request, redirect_url=None, from_authorize=None) -> web.Response:
    """get_github_signup

    

    :param redirect_url: 
    :type redirect_url: str
    :param from_authorize: 
    :type from_authorize: str

    """
    return web.Response(status=200)


async def get_github_username(request: web.Request, ) -> web.Response:
    """get_github_username

    


    """
    return web.Response(status=200)


async def get_matomo(request: web.Request, matomo_id, body=None) -> web.Response:
    """Get Matomo addon

    

    :param matomo_id: Automatically added
    :type matomo_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_matomo_k_token_validation(request: web.Request, keycloak_token=None, body=None) -> web.Response:
    """Validate a keycloak token

    

    :param keycloak_token: Environment variable injected on the app with &#39;KEYCLOAK_TOKEN&#39; name
    :type keycloak_token: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def get_network_group(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Get Network Group

    Gets details of a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_member(request: web.Request, owner_id, network_group_id, member_id, body=None) -> web.Response:
    """Get member

    Gets details of a Network Group member.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param member_id: Automatically added
    :type member_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_peer(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Get peer

    Gets details of a Network Group peer.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_stream(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Network Group SSE

    Retrieves the current Network Group details as a Server Sent Event.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_wire_guard_configuration(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Get WireGuard® configuration

    Gets the current WireGuard® tunnel configuration file for a Network Group peer.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_wire_guard_configuration_stream(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Get WireGuard® configuration

    Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_newsfeed_engineering(request: web.Request, ) -> web.Response:
    """get_newsfeed_engineering

    


    """
    return web.Response(status=200)


async def get_newsfeeds_blog(request: web.Request, ) -> web.Response:
    """get_newsfeeds_blog

    


    """
    return web.Response(status=200)


async def get_oauth_authorize(request: web.Request, oauth_token=None, cookie=None) -> web.Response:
    """get_oauth_authorize

    

    :param oauth_token: 
    :type oauth_token: str
    :param cookie: 
    :type cookie: str

    """
    return web.Response(status=200)


async def get_oauth_rights(request: web.Request, ) -> web.Response:
    """get_oauth_rights

    


    """
    return web.Response(status=200)


async def get_organisations(request: web.Request, user=None) -> web.Response:
    """get_organisations

    

    :param user: 
    :type user: str

    """
    return web.Response(status=200)


async def get_organisations_id(request: web.Request, id) -> web.Response:
    """get_organisations_id

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders(request: web.Request, id) -> web.Response:
    """get_organisations_id_addonproviders

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_features(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_features

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_plans(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_plans

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_plans_plan_id(request: web.Request, id, provider_id, plan_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_plans_plan_id

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_tags(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_tags

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons(request: web.Request, id) -> web.Response:
    """get_organisations_id_addons

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_applications(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_applications

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_env(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_env

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_sso(request: web.Request, provider_id, id) -> web.Response:
    """get_organisations_id_addons_addon_id_sso

    

    :param provider_id: 
    :type provider_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_tags(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_tags

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications(request: web.Request, id) -> web.Response:
    """get_organisations_id_applications

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_env(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_env

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_dependencies(request: web.Request, app_id, id) -> web.Response:
    """get_organisations_id_applications_app_id_dependencies

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_dependents(request: web.Request, app_id, id) -> web.Response:
    """get_organisations_id_applications_app_id_dependents

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_deployments(request: web.Request, id, app_id, limit=None, offset=None, action=None) -> web.Response:
    """get_organisations_id_applications_app_id_deployments

    

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


async def get_organisations_id_applications_app_id_env(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_env

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_instances(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_instances

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_tags(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_tags

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_vhosts(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_vhosts

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_vhosts_favourite(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_vhosts_favourite

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumers(request: web.Request, id) -> web.Response:
    """get_organisations_id_consumers

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumers_key(request: web.Request, id, key) -> web.Response:
    """get_organisations_id_consumers_key

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumers_key_secret(request: web.Request, id, key) -> web.Response:
    """get_organisations_id_consumers_key_secret

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumptions(request: web.Request, id, app_id=None, _from=None, to=None) -> web.Response:
    """get_organisations_id_consumptions

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param _from: 
    :type _from: str
    :param to: 
    :type to: str

    """
    return web.Response(status=200)


async def get_organisations_id_credits(request: web.Request, id) -> web.Response:
    """get_organisations_id_credits

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_deployments(request: web.Request, id) -> web.Response:
    """get_organisations_id_deployments

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_instances(request: web.Request, id) -> web.Response:
    """get_organisations_id_instances

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_members(request: web.Request, id) -> web.Response:
    """get_organisations_id_members

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payment_info(request: web.Request, id) -> web.Response:
    """get_organisations_id_payment_info

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings(request: web.Request, id) -> web.Response:
    """get_organisations_id_payments_billings

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_bid(request: web.Request, id, bid) -> web.Response:
    """get_organisations_id_payments_billings_bid

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_bid_pdf(request: web.Request, id, bid, token=None) -> web.Response:
    """get_organisations_id_payments_billings_bid_pdf

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_full_price_price(request: web.Request, id, price) -> web.Response:
    """get_organisations_id_payments_full_price_price

    

    :param id: 
    :type id: str
    :param price: 
    :type price: str

    """
    return web.Response(status=200)


async def get_password_forgotten(request: web.Request, ) -> web.Response:
    """get_password_forgotten

    


    """
    return web.Response(status=200)


async def get_password_forgotten_key(request: web.Request, key) -> web.Response:
    """get_password_forgotten_key

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_payments_coupons_name(request: web.Request, name) -> web.Response:
    """get_payments_coupons_name

    

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_payments_providers(request: web.Request, ) -> web.Response:
    """get_payments_providers

    


    """
    return web.Response(status=200)


async def get_payments_tokens_stripe(request: web.Request, ) -> web.Response:
    """get_payments_tokens_stripe

    


    """
    return web.Response(status=200)


async def get_products_addon_providers(request: web.Request, ) -> web.Response:
    """get_products_addon_providers

    


    """
    return web.Response(status=200)


async def get_products_addon_providers_provider_id(request: web.Request, provider_id) -> web.Response:
    """get_products_addon_providers_provider_id

    

    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_products_countries(request: web.Request, ) -> web.Response:
    """get_products_countries

    


    """
    return web.Response(status=200)


async def get_products_countrycodes(request: web.Request, ) -> web.Response:
    """get_products_countrycodes

    


    """
    return web.Response(status=200)


async def get_products_instances(request: web.Request, _for=None) -> web.Response:
    """get_products_instances

    

    :param _for: 
    :type _for: str

    """
    return web.Response(status=200)


async def get_products_instances_type_version(request: web.Request, type, version, _for=None, app=None) -> web.Response:
    """get_products_instances_type_version

    

    :param type: 
    :type type: str
    :param version: 
    :type version: str
    :param _for: 
    :type _for: str
    :param app: 
    :type app: str

    """
    return web.Response(status=200)


async def get_products_packages(request: web.Request, coupon=None, orga_id=None, currency=None) -> web.Response:
    """get_products_packages

    

    :param coupon: 
    :type coupon: str
    :param orga_id: 
    :type orga_id: str
    :param currency: 
    :type currency: str

    """
    return web.Response(status=200)


async def get_products_prices(request: web.Request, ) -> web.Response:
    """get_products_prices

    


    """
    return web.Response(status=200)


async def get_products_zones(request: web.Request, ) -> web.Response:
    """get_products_zones

    


    """
    return web.Response(status=200)


async def get_self(request: web.Request, ) -> web.Response:
    """

    Get information about yourself


    """
    return web.Response(status=200)


async def get_self_addons(request: web.Request, ) -> web.Response:
    """Addon

    Get all the addons


    """
    return web.Response(status=200)


async def get_self_addons_addon_id(request: web.Request, addon_id) -> web.Response:
    """Specific addon

    Get a specific addon

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_applications(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_applications

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_env(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_env

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_sso(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_sso

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_addons_addon_id_tags(request: web.Request, addon_id) -> web.Response:
    """get_self_addons_addon_id_tags

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_self_applications(request: web.Request, ) -> web.Response:
    """get_self_applications

    


    """
    return web.Response(status=200)


async def get_self_applications_app_id(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_addons_env(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_addons_env

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_dependencies(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_dependencies

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_dependencies_dependency_id(request: web.Request, dependency_id, app_id, body) -> web.Response:
    """get_self_applications_app_id_dependencies_dependency_id

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def get_self_applications_app_id_dependents(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_dependents

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_deployments(request: web.Request, app_id, limit=None, offset=None, action=None) -> web.Response:
    """get_self_applications_app_id_deployments

    

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


async def get_self_applications_app_id_env(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_env

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_instances(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_instances

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_tags(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_tags

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_vhosts(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_vhosts

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_applications_app_id_vhosts_favourite(request: web.Request, app_id) -> web.Response:
    """get_self_applications_app_id_vhosts_favourite

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_self_confirmation_email(request: web.Request, ) -> web.Response:
    """get_self_confirmation_email

    


    """
    return web.Response(status=200)


async def get_self_consumers(request: web.Request, ) -> web.Response:
    """get_self_consumers

    


    """
    return web.Response(status=200)


async def get_self_consumers_key(request: web.Request, key) -> web.Response:
    """get_self_consumers_key

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_self_consumers_key_secret(request: web.Request, key) -> web.Response:
    """get_self_consumers_key_secret

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_self_consumptions(request: web.Request, app_id=None, _from=None, to=None) -> web.Response:
    """get_self_consumptions

    

    :param app_id: 
    :type app_id: str
    :param _from: 
    :type _from: str
    :param to: 
    :type to: str

    """
    return web.Response(status=200)


async def get_self_credits(request: web.Request, ) -> web.Response:
    """get_self_credits

    


    """
    return web.Response(status=200)


async def get_self_emails(request: web.Request, ) -> web.Response:
    """get_self_emails

    


    """
    return web.Response(status=200)


async def get_self_id(request: web.Request, ) -> web.Response:
    """get_self_id

    


    """
    return web.Response(status=200)


async def get_self_instances(request: web.Request, ) -> web.Response:
    """get_self_instances

    


    """
    return web.Response(status=200)


async def get_self_keys(request: web.Request, ) -> web.Response:
    """get_self_keys

    


    """
    return web.Response(status=200)


async def get_self_payment_info(request: web.Request, ) -> web.Response:
    """get_self_payment_info

    


    """
    return web.Response(status=200)


async def get_self_payments_billings(request: web.Request, ) -> web.Response:
    """get_self_payments_billings

    


    """
    return web.Response(status=200)


async def get_self_payments_billings_bid(request: web.Request, bid) -> web.Response:
    """get_self_payments_billings_bid

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def get_self_payments_billings_bid_pdf(request: web.Request, bid, token=None) -> web.Response:
    """get_self_payments_billings_bid_pdf

    

    :param bid: 
    :type bid: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_self_payments_fullprice_price(request: web.Request, price) -> web.Response:
    """get_self_payments_fullprice_price

    

    :param price: 
    :type price: str

    """
    return web.Response(status=200)


async def get_self_payments_methods(request: web.Request, ) -> web.Response:
    """get_self_payments_methods

    


    """
    return web.Response(status=200)


async def get_self_tokens(request: web.Request, ) -> web.Response:
    """get_self_tokens

    


    """
    return web.Response(status=200)


async def get_self_validate_email(request: web.Request, validation_key=None) -> web.Response:
    """get_self_validate_email

    

    :param validation_key: 
    :type validation_key: str

    """
    return web.Response(status=200)


async def get_summary(request: web.Request, ) -> web.Response:
    """get_summary

    


    """
    return web.Response(status=200)


async def get_users_id(request: web.Request, id) -> web.Response:
    """get_users_id

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_users_id_applications(request: web.Request, id) -> web.Response:
    """get_users_id_applications

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_users_user_id_git_info(request: web.Request, user_id) -> web.Response:
    """get_users_user_id_git_info

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_vendor_apps(request: web.Request, offset=None) -> web.Response:
    """get_vendor_apps

    

    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def get_vendor_apps_addon_id(request: web.Request, addon_id) -> web.Response:
    """get_vendor_apps_addon_id

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def list_network_group_members(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """List members

    Lists members in a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def list_network_group_peers(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """List peers

    Lists peers in a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def list_network_groups(request: web.Request, owner_id, body=None) -> web.Response:
    """List Network Groups

    Lists Network Groups from an owner.

    :param owner_id: Automatically added
    :type owner_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def logs_app_id_drains_get(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_get

    Fetch the logs drains for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_drains_id_or_url_delete(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_id_or_url_delete

    Delete the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_drains_id_or_url_get(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_id_or_url_get

    Fetch the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_drains_post(request: web.Request, app_id) -> web.Response:
    """logs_app_id_drains_post

    Add a log drain for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_app_id_get(request: web.Request, app_id, limit=None, order=None, after=None, before=None, filter=None, deployment_id=None) -> web.Response:
    """logs_app_id_get

    Fetch the logs for a given application

    :param app_id: Application Id
    :type app_id: str
    :param limit: Number of lines to return
    :type limit: int
    :param order: Logs order
    :type order: str
    :param after: Lowest bound for logs date, ISO 8601
    :type after: str
    :param before: Highest bounds for logs date, ISO 8601
    :type before: str
    :param filter: A pattern to filter with
    :type filter: str
    :param deployment_id: Only fetch logs emitted by this deployment
    :type deployment_id: str

    """
    after = util.deserialize_datetime(after)
    before = util.deserialize_datetime(before)
    return web.Response(status=200)


async def logs_app_id_sse_get(request: web.Request, app_id) -> web.Response:
    """logs_app_id_sse_get

    Retrieve logs as they come through a sse connection. To have authorization, you have to add &#x60;authorization&#x3D;oAuthAuthorizationString&#x60; as query param.

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def logs_drains_drain_id_put(request: web.Request, drain_id) -> web.Response:
    """logs_drains_drain_id_put

    Fetch all the logs drains (ccadmin dedicated route)

    :param drain_id: Automatically added
    :type drain_id: str

    """
    return web.Response(status=200)


async def logs_drains_get(request: web.Request, ) -> web.Response:
    """logs_drains_get

    Fetch all the logs drains (ccadmin dedicated route)


    """
    return web.Response(status=200)


async def logs_logs_chunked_app_id_get(request: web.Request, app_id, download=None) -> web.Response:
    """logs_logs_chunked_app_id_get

    Retrieve logs as they come through a chunked, never-ending response

    :param app_id: Application Id
    :type app_id: str
    :param download: Tell the user-agent to download the body as a file
    :type download: bool

    """
    return web.Response(status=200)


async def logs_logs_socket_app_id_get(request: web.Request, app_id, since=None, filter=None, deployment_id=None) -> web.Response:
    """logs_logs_socket_app_id_get

    Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

    :param app_id: Application Id
    :type app_id: str
    :param since: Only fetch logs newer than this (ISO-8601 formatted) date
    :type since: str
    :param filter: A pattern to filter with
    :type filter: str
    :param deployment_id: Only fetch logs emitted by this deployment
    :type deployment_id: str

    """
    since = util.deserialize_datetime(since)
    return web.Response(status=200)


async def logs_socket_app_id_get(request: web.Request, app_id) -> web.Response:
    """logs_socket_app_id_get

    WebSocket to get logs for :appID. Optional queryString arg bind_to_es&#x3D;true to bind WS on log storage and not real time AMQP broker

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def notifications_emailhooks_owner_id_get(request: web.Request, owner_id) -> web.Response:
    """notifications_emailhooks_owner_id_get

    list created e-mail hooks

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_emailhooks_owner_id_id_delete(request: web.Request, owner_id) -> web.Response:
    """notifications_emailhooks_owner_id_id_delete

    delete an e-mail hook

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_emailhooks_owner_id_id_put(request: web.Request, owner_id) -> web.Response:
    """notifications_emailhooks_owner_id_id_put

    edit an e-mail hook

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_emailhooks_owner_id_post(request: web.Request, owner_id) -> web.Response:
    """notifications_emailhooks_owner_id_post

    create a hook for e-mail notifications

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_info_events_get(request: web.Request, ) -> web.Response:
    """notifications_info_events_get

    list available events


    """
    return web.Response(status=200)


async def notifications_info_webhookformats_get(request: web.Request, ) -> web.Response:
    """notifications_info_webhookformats_get

    list available webhook formats


    """
    return web.Response(status=200)


async def notifications_webhooks_owner_id_get(request: web.Request, owner_id) -> web.Response:
    """notifications_webhooks_owner_id_get

    list created hooks

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_webhooks_owner_id_id_delete(request: web.Request, owner_id) -> web.Response:
    """notifications_webhooks_owner_id_id_delete

    delete a hook

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_webhooks_owner_id_id_put(request: web.Request, owner_id) -> web.Response:
    """notifications_webhooks_owner_id_id_put

    edit a hook

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def notifications_webhooks_owner_id_post(request: web.Request, owner_id) -> web.Response:
    """notifications_webhooks_owner_id_post

    create a hook for notifications

    :param owner_id: Automatically added
    :type owner_id: str

    """
    return web.Response(status=200)


async def oauth_access_token_query_post(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """oauth_access_token_query_post

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def oauth_request_token_query_post(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """oauth_request_token_query_post

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def openapi_get(request: web.Request, ) -> web.Response:
    """openapi_get

    


    """
    return web.Response(status=200)


async def openapi_type_get(request: web.Request, type) -> web.Response:
    """Get the swagger for this API as {type}

    Get the swagger for this API as {type}. Type can be either \&quot;yml\&quot; or \&quot;json\&quot;.

    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def organisations_id_addonproviders_provider_id_delete(request: web.Request, id, provider_id) -> web.Response:
    """Remove an add-on provider

    Remove a given add-on provider. providerId must be owned by organisation {id}.

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_instances_get(request: web.Request, id, addon_id, deployment_id=None, with_deleted=None) -> web.Response:
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


async def organisations_id_addons_addon_id_instances_instance_id_get(request: web.Request, instance_id, id, addon_id) -> web.Response:
    """Get a specific instance for {addonId}

    

    :param instance_id: 
    :type instance_id: str
    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_get(request: web.Request, id, addon_id) -> web.Response:
    """Get past migrations from add-on.

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_migration_id_get(request: web.Request, migration_id, id, addon_id) -> web.Response:
    """Get a given migration

    

    :param migration_id: 
    :type migration_id: str
    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_post(request: web.Request, id, addon_id, body) -> web.Response:
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


async def organisations_id_addons_addon_id_sso_get(request: web.Request, id, addon_id) -> web.Response:
    """organisations_id_addons_addon_id_sso_get

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_preorders_post(request: web.Request, id, body) -> web.Response:
    """organisations_id_addons_preorders_post

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def organisations_id_applications_app_id_branch_put(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_branch_put

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_branches_get(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_branches_get

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_buildflavor_put(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_buildflavor_put

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_dependencies_env_get(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_dependencies_env_get

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_deployments_deployment_id_get(request: web.Request, app_id, deployment_id, id) -> web.Response:
    """organisations_id_applications_app_id_deployments_deployment_id_get

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_exposed_env_get(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_exposed_env_get

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_exposed_env_put(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_exposed_env_put

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_instances_instance_id_get(request: web.Request, instance_id, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_instances_instance_id_get

    

    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_billings_unpaid_get(request: web.Request, id) -> web.Response:
    """organisations_id_payments_billings_unpaid_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_default_get(request: web.Request, id) -> web.Response:
    """organisations_id_payments_methods_default_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_default_put(request: web.Request, id, body) -> web.Response:
    """organisations_id_payments_methods_default_put

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentData.from_dict(body)
    return web.Response(status=200)


async def organisations_id_payments_methods_get(request: web.Request, id) -> web.Response:
    """organisations_id_payments_methods_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_mid_delete(request: web.Request, m_id, id) -> web.Response:
    """organisations_id_payments_methods_mid_delete

    

    :param m_id: 
    :type m_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_post(request: web.Request, id, body) -> web.Response:
    """organisations_id_payments_methods_post

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def organisations_id_payments_monthlyinvoice_get(request: web.Request, id) -> web.Response:
    """organisations_id_payments_monthlyinvoice_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_monthlyinvoice_maxcredit_put(request: web.Request, id) -> web.Response:
    """organisations_id_payments_monthlyinvoice_maxcredit_put

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_recurring_get(request: web.Request, id) -> web.Response:
    """organisations_id_payments_recurring_get

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def payments_assets_pay_button_token_button_png_get(request: web.Request, token) -> web.Response:
    """payments_assets_pay_button_token_button_png_get

    

    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def payments_bid_end_stripe_post(request: web.Request, bid) -> web.Response:
    """payments_bid_end_stripe_post

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def post_authorize(request: web.Request, ) -> web.Response:
    """post_authorize

    Handled by our API.


    """
    return web.Response(status=200)


async def post_github_redeploy(request: web.Request, user_agent=None, x_github_event=None, x_hub_signature=None) -> web.Response:
    """post_github_redeploy

    

    :param user_agent: 
    :type user_agent: str
    :param x_github_event: 
    :type x_github_event: str
    :param x_hub_signature: 
    :type x_hub_signature: str

    """
    return web.Response(status=200)


async def post_github_signup(request: web.Request, transaction_id=None, name=None, other_id=None, other_email=None, password=None, auto_link=None, terms=None) -> web.Response:
    """post_github_signup

    

    :param transaction_id: 
    :type transaction_id: str
    :param name: 
    :type name: str
    :param other_id: 
    :type other_id: str
    :param other_email: 
    :type other_email: str
    :param password: 
    :type password: str
    :param auto_link: 
    :type auto_link: str
    :param terms: 
    :type terms: str

    """
    return web.Response(status=200)


async def post_oauth_access_token(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """post_oauth_access_token

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def post_oauth_authorize(request: web.Request, almighty=None, access_organisations=None, manage_organisations=None, manage_organisations_services=None, manage_organisations_applications=None, manage_organisations_members=None, access_organisations_bills=None, access_organisations_credit_count=None, access_organisations_consumption_statistics=None, access_personal_information=None, manage_personal_information=None, manage_ssh_keys=None, manage_services=None, manage_applications=None, access_bills=None, access_credit_count=None, access_consumption_statistics=None, cookie=None) -> web.Response:
    """post_oauth_authorize

    

    :param almighty: 
    :type almighty: str
    :param access_organisations: 
    :type access_organisations: str
    :param manage_organisations: 
    :type manage_organisations: str
    :param manage_organisations_services: 
    :type manage_organisations_services: str
    :param manage_organisations_applications: 
    :type manage_organisations_applications: str
    :param manage_organisations_members: 
    :type manage_organisations_members: str
    :param access_organisations_bills: 
    :type access_organisations_bills: str
    :param access_organisations_credit_count: 
    :type access_organisations_credit_count: str
    :param access_organisations_consumption_statistics: 
    :type access_organisations_consumption_statistics: str
    :param access_personal_information: 
    :type access_personal_information: str
    :param manage_personal_information: 
    :type manage_personal_information: str
    :param manage_ssh_keys: 
    :type manage_ssh_keys: str
    :param manage_services: 
    :type manage_services: str
    :param manage_applications: 
    :type manage_applications: str
    :param access_bills: 
    :type access_bills: str
    :param access_credit_count: 
    :type access_credit_count: str
    :param access_consumption_statistics: 
    :type access_consumption_statistics: str
    :param cookie: 
    :type cookie: str

    """
    return web.Response(status=200)


async def post_oauth_request_token(request: web.Request, oauth_consumer_key=None, oauth_token=None, oauth_signature_method=None, oauth_signature=None, oauth_timestamp=None, oauth_nonce=None, oauth_version=None, oauth_verifier=None, oauth_callback=None, oauth_token_secret=None, oauth_callback_confirmed=None) -> web.Response:
    """post_oauth_request_token

    

    :param oauth_consumer_key: 
    :type oauth_consumer_key: str
    :param oauth_token: 
    :type oauth_token: str
    :param oauth_signature_method: 
    :type oauth_signature_method: str
    :param oauth_signature: 
    :type oauth_signature: str
    :param oauth_timestamp: 
    :type oauth_timestamp: str
    :param oauth_nonce: 
    :type oauth_nonce: str
    :param oauth_version: 
    :type oauth_version: str
    :param oauth_verifier: 
    :type oauth_verifier: str
    :param oauth_callback: 
    :type oauth_callback: str
    :param oauth_token_secret: 
    :type oauth_token_secret: str
    :param oauth_callback_confirmed: 
    :type oauth_callback_confirmed: str

    """
    return web.Response(status=200)


async def post_organisations(request: web.Request, body) -> web.Response:
    """post_organisations

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeOrganisation.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_addonproviders

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddonProvider.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_provider_id_features(request: web.Request, id, provider_id, body) -> web.Response:
    """post_organisations_id_addonproviders_provider_id_features

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeFeature.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_provider_id_plans(request: web.Request, id, provider_id, body) -> web.Response:
    """post_organisations_id_addonproviders_provider_id_plans

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlan.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_provider_id_testers(request: web.Request, id, provider_id) -> web.Response:
    """post_organisations_id_addonproviders_provider_id_testers

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def post_organisations_id_addons(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_addons

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_applications

    Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_addons(request: web.Request, id, app_id, body) -> web.Response:
    """post_organisations_id_applications_app_id_addons

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_instances(request: web.Request, id, app_id, commit=None) -> web.Response:
    """post_organisations_id_applications_app_id_instances

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param commit: 
    :type commit: str

    """
    return web.Response(status=200)


async def post_organisations_id_consumers(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_consumers

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_members(request: web.Request, id, body, invitation_key=None) -> web.Response:
    """post_organisations_id_members

    

    :param id: 
    :type id: str
    :param body: 
    :type body: 
    :param invitation_key: 
    :type invitation_key: str

    """
    return web.Response(status=200)


async def post_organisations_id_payments_billings(request: web.Request, id) -> web.Response:
    """post_organisations_id_payments_billings

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_password_forgotten(request: web.Request, login=None, drop_tokens=None, tester_pass=None) -> web.Response:
    """post_password_forgotten

    

    :param login: 
    :type login: str
    :param drop_tokens: 
    :type drop_tokens: str
    :param tester_pass: 
    :type tester_pass: str

    """
    return web.Response(status=200)


async def post_password_forgotten_key(request: web.Request, key, _pass=None, pass2=None) -> web.Response:
    """post_password_forgotten_key

    

    :param key: 
    :type key: str
    :param _pass: 
    :type _pass: str
    :param pass2: 
    :type pass2: str

    """
    return web.Response(status=200)


async def post_self_addons(request: web.Request, body) -> web.Response:
    """post_self_addons

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_self_applications(request: web.Request, body) -> web.Response:
    """post_self_applications

    Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_addons(request: web.Request, app_id, body) -> web.Response:
    """post_self_applications_app_id_addons

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_self_applications_app_id_instances(request: web.Request, app_id, commit=None) -> web.Response:
    """post_self_applications_app_id_instances

    

    :param app_id: 
    :type app_id: str
    :param commit: 
    :type commit: str

    """
    return web.Response(status=200)


async def post_self_consumers(request: web.Request, body) -> web.Response:
    """post_self_consumers

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def post_self_payments_billings(request: web.Request, ) -> web.Response:
    """post_self_payments_billings

    


    """
    return web.Response(status=200)


async def post_self_payments_methods(request: web.Request, ) -> web.Response:
    """post_self_payments_methods

    


    """
    return web.Response(status=200)


async def post_users(request: web.Request, body, invitation_key=None, addon_beta_invitation_key=None, email=None, _pass=None, url_next=None, terms=None) -> web.Response:
    """post_users

    

    :param body: 
    :type body: dict | bytes
    :param invitation_key: 
    :type invitation_key: str
    :param addon_beta_invitation_key: 
    :type addon_beta_invitation_key: str
    :param email: 
    :type email: str
    :param _pass: 
    :type _pass: str
    :param url_next: 
    :type url_next: str
    :param terms: 
    :type terms: str

    """
    body = WannabeUser.from_dict(body)
    return web.Response(status=200)


async def post_vendor_billing_owner_id(request: web.Request, addon_id, body) -> web.Response:
    """post_vendor_billing_owner_id

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddonBilling.from_dict(body)
    return web.Response(status=200)


async def products_addonproviders_provider_id_versions_get(request: web.Request, provider_id) -> web.Response:
    """products_addonproviders_provider_id_versions_get

    

    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def products_mfa_kinds_get(request: web.Request, ) -> web.Response:
    """products_mfa_kinds_get

    


    """
    return web.Response(status=200)


async def put_organisations_id(request: web.Request, id, body) -> web.Response:
    """put_organisations_id

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeOrganisation.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addonproviders_provider_id(request: web.Request, id, provider_id, body) -> web.Response:
    """put_organisations_id_addonproviders_provider_id

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddonProvider.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addonproviders_provider_id_plans_plan_id(request: web.Request, id, provider_id, plan_id, body) -> web.Response:
    """put_organisations_id_addonproviders_provider_id_plans_plan_id

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlan.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name(request: web.Request, id, feature_name, provider_id, plan_id, body) -> web.Response:
    """put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name

    

    :param id: 
    :type id: str
    :param feature_name: 
    :type feature_name: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlanFeature.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addons_addon_id(request: web.Request, id, addon_id, body) -> web.Response:
    """put_organisations_id_addons_addon_id

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addons_addon_id_tags_tag(request: web.Request, id, tag, addon_id, body) -> web.Response:
    """put_organisations_id_addons_addon_id_tags_tag

    

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


async def put_organisations_id_applications_app_id(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_dependencies_dependency_id(request: web.Request, dependency_id, app_id, id, body) -> web.Response:
    """put_organisations_id_applications_app_id_dependencies_dependency_id

    

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


async def put_organisations_id_applications_app_id_env(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_env

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_env_env_name(request: web.Request, id, app_id, env_name, body) -> web.Response:
    """put_organisations_id_applications_app_id_env_env_name

    

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


async def put_organisations_id_applications_app_id_tags_tag(request: web.Request, id, app_id, tag, body) -> web.Response:
    """put_organisations_id_applications_app_id_tags_tag

    

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


async def put_organisations_id_applications_app_id_vhosts_domain(request: web.Request, id, app_id, domain, body) -> web.Response:
    """put_organisations_id_applications_app_id_vhosts_domain

    

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


async def put_organisations_id_applications_app_id_vhosts_favourite(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_vhosts_favourite

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_avatar(request: web.Request, id) -> web.Response:
    """put_organisations_id_avatar

    If you want to upload an image from your computer, send the image in the body of the request without anything else.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def put_organisations_id_consumers_key(request: web.Request, id, key, body) -> web.Response:
    """put_organisations_id_consumers_key

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_members_user_id(request: web.Request, id, user_id, body) -> web.Response:
    """put_organisations_id_members_user_id

    

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def put_organisations_id_payments_billings_bid(request: web.Request, id, bid) -> web.Response:
    """put_organisations_id_payments_billings_bid

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def put_self(request: web.Request, body) -> web.Response:
    """put_self

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeUser.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id(request: web.Request, addon_id, body) -> web.Response:
    """put_self_addons_addon_id

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_plan(request: web.Request, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_plan

    

    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlan.from_dict(body)
    return web.Response(status=200)


async def put_self_addons_addon_id_tags_tag(request: web.Request, tag, addon_id, body) -> web.Response:
    """put_self_addons_addon_id_tags_tag

    

    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_env(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_env

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_env_env_name(request: web.Request, app_id, env_name, body) -> web.Response:
    """put_self_applications_app_id_env_env_name

    

    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_tags_tag(request: web.Request, app_id, tag, body) -> web.Response:
    """put_self_applications_app_id_tags_tag

    

    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_vhosts_domain(request: web.Request, app_id, domain, body) -> web.Response:
    """put_self_applications_app_id_vhosts_domain

    

    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_self_applications_app_id_vhosts_favourite(request: web.Request, app_id, body) -> web.Response:
    """put_self_applications_app_id_vhosts_favourite

    

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_self_avatar(request: web.Request, body) -> web.Response:
    """put_self_avatar

    

    :param body: 
    :type body: dict | bytes

    """
    body = Avatar.from_dict(body)
    return web.Response(status=200)


async def put_self_change_password(request: web.Request, ) -> web.Response:
    """put_self_change_password

    


    """
    return web.Response(status=200)


async def put_self_consumers_key(request: web.Request, key, body) -> web.Response:
    """put_self_consumers_key

    

    :param key: 
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def put_self_emails_email(request: web.Request, email, body) -> web.Response:
    """put_self_emails_email

    

    :param email: 
    :type email: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_keys_key(request: web.Request, key, body) -> web.Response:
    """put_self_keys_key

    

    :param key: 
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def put_self_payments_billings_bid(request: web.Request, bid) -> web.Response:
    """put_self_payments_billings_bid

    

    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def put_vendor_apps_addon_id(request: web.Request, addon_id) -> web.Response:
    """put_vendor_apps_addon_id

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def self_addons_preorders_post(request: web.Request, body) -> web.Response:
    """self_addons_preorders_post

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def self_applications_app_id_branch_put(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_branch_put

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_branches_get(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_branches_get

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_buildflavor_put(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_buildflavor_put

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_dependencies_env_get(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_dependencies_env_get

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_deployments_deployment_id_get(request: web.Request, app_id, deployment_id) -> web.Response:
    """self_applications_app_id_deployments_deployment_id_get

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_exposed_env_get(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_exposed_env_get

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_exposed_env_put(request: web.Request, app_id) -> web.Response:
    """self_applications_app_id_exposed_env_put

    

    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_applications_app_id_instances_instance_id_get(request: web.Request, instance_id, app_id) -> web.Response:
    """self_applications_app_id_instances_instance_id_get

    

    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def self_cli_tokens_get(request: web.Request, cli_token=None) -> web.Response:
    """self_cli_tokens_get

    

    :param cli_token: 
    :type cli_token: str

    """
    return web.Response(status=200)


async def self_mfa_kind_backupcodes_get(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_backupcodes_get

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_confirmation_post(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_confirmation_post

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_delete(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_delete

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_post(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_post

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_mfa_kind_put(request: web.Request, kind) -> web.Response:
    """self_mfa_kind_put

    

    :param kind: 
    :type kind: str

    """
    return web.Response(status=200)


async def self_payments_methods_default_get(request: web.Request, ) -> web.Response:
    """self_payments_methods_default_get

    


    """
    return web.Response(status=200)


async def self_payments_methods_default_put(request: web.Request, ) -> web.Response:
    """self_payments_methods_default_put

    


    """
    return web.Response(status=200)


async def self_payments_monthlyinvoice_get(request: web.Request, ) -> web.Response:
    """self_payments_monthlyinvoice_get

    


    """
    return web.Response(status=200)


async def self_payments_monthlyinvoice_maxcredit_put(request: web.Request, ) -> web.Response:
    """self_payments_monthlyinvoice_maxcredit_put

    


    """
    return web.Response(status=200)


async def self_payments_recurring_get(request: web.Request, ) -> web.Response:
    """self_payments_recurring_get

    


    """
    return web.Response(status=200)


async def self_payments_tokens_stripe_get(request: web.Request, ) -> web.Response:
    """self_payments_tokens_stripe_get

    


    """
    return web.Response(status=200)


async def update_config_provider_env(request: web.Request, configuration_provider_id, body) -> web.Response:
    """Update provider&#39;s addon environment

    

    :param configuration_provider_id: Automatically added
    :type configuration_provider_id: str
    :param body: 
    :type body: List[]

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_get(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_get

    Fetch the logs drains for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_id_or_url_delete(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_id_or_url_delete

    Delete the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_id_or_url_get(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_id_or_url_get

    Fetch the logs drain by id or url for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_drains_post(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_drains_post

    Add a log drain for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_get(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_get

    Fetch the logs for a given application

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_logs_chunked_get(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_logs_chunked_get

    Retrieve logs as they come through a chunked, never-ending response

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def v3_logs_app_id_logs_socket_get(request: web.Request, app_id) -> web.Response:
    """v3_logs_app_id_logs_socket_get

    Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

    :param app_id: Automatically added
    :type app_id: str

    """
    return web.Response(status=200)


async def vendor_addons_post(request: web.Request, ) -> web.Response:
    """vendor_addons_post

    


    """
    return web.Response(status=200)


async def vendor_apps_addon_id_logscollector_get(request: web.Request, addon_id) -> web.Response:
    """vendor_apps_addon_id_logscollector_get

    

    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def vendor_apps_addon_id_migration_callback_put(request: web.Request, addon_id, plan_id=None, region=None) -> web.Response:
    """vendor_apps_addon_id_migration_callback_put

    

    :param addon_id: 
    :type addon_id: str
    :param plan_id: 
    :type plan_id: str
    :param region: 
    :type region: str

    """
    return web.Response(status=200)
