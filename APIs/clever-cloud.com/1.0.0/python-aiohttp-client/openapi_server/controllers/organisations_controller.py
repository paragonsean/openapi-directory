from typing import List, Dict
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.addon_migration import AddonMigration
from openapi_server.models.addon_provider_sso import AddonProviderSso
from openapi_server.models.app_instance import AppInstance
from openapi_server.models.application import Application
from openapi_server.models.body import Body
from openapi_server.models.conso import Conso
from openapi_server.models.consumer import Consumer
from openapi_server.models.credits import Credits
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_summary import DeploymentSummary
from openapi_server.models.env import Env
from openapi_server.models.error import Error
from openapi_server.models.feature import Feature
from openapi_server.models.linked_app_env import LinkedAppEnv
from openapi_server.models.list_env import ListEnv
from openapi_server.models.organisation import Organisation
from openapi_server.models.organisations_id_addons_addon_id_migrations_post_request import OrganisationsIdAddonsAddonIdMigrationsPostRequest
from openapi_server.models.payment_data import PaymentData
from openapi_server.models.plan import Plan
from openapi_server.models.provider import Provider
from openapi_server.models.schema1 import Schema1
from openapi_server.models.schema2 import Schema2
from openapi_server.models.secret import Secret
from openapi_server.models.sso import Sso
from openapi_server.models.supernova_instance_view import SupernovaInstanceView
from openapi_server.models.vhost import Vhost
from openapi_server.models.wannabe_addon import WannabeAddon
from openapi_server.models.wannabe_addon_provider import WannabeAddonProvider
from openapi_server.models.wannabe_application import WannabeApplication
from openapi_server.models.wannabe_consumer import WannabeConsumer
from openapi_server.models.wannabe_env import WannabeEnv
from openapi_server.models.wannabe_feature import WannabeFeature
from openapi_server.models.wannabe_organisation import WannabeOrganisation
from openapi_server.models.wannabe_plan import WannabePlan
from openapi_server.models.wannabe_plan_feature import WannabePlanFeature
from openapi_server import util


async def create_network_group_0(request: web.Request, owner_id, body=None) -> web.Response:
    """Create Network Group

    Creates a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_network_group_external_peer_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def create_network_group_member_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def delete_network_group_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def delete_network_group_external_peer_0(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
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


async def delete_network_group_member_0(request: web.Request, owner_id, network_group_id, member_id, body=None) -> web.Response:
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


async def delete_network_group_peer_0(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
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


async def delete_organisations_id_0(request: web.Request, id) -> web.Response:
    """delete_organisations_id_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addonproviders_provider_id_features_feature_id_0(request: web.Request, id, feature_id, provider_id) -> web.Response:
    """delete_organisations_id_addonproviders_provider_id_features_feature_id_0

    

    :param id: 
    :type id: str
    :param feature_id: 
    :type feature_id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addonproviders_provider_id_plans_plan_id_0(request: web.Request, id, provider_id, plan_id) -> web.Response:
    """delete_organisations_id_addonproviders_provider_id_plans_plan_id_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0(request: web.Request, id, feature_name, provider_id, plan_id) -> web.Response:
    """delete_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0

    

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


async def delete_organisations_id_addons_addon_id_1(request: web.Request, id, addon_id) -> web.Response:
    """delete_organisations_id_addons_addon_id_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_addons_addon_id_tags_tag_1(request: web.Request, id, tag, addon_id) -> web.Response:
    """delete_organisations_id_addons_addon_id_tags_tag_1

    

    :param id: 
    :type id: str
    :param tag: 
    :type tag: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_1(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_addons_addon_id_2(request: web.Request, id, app_id, addon_id) -> web.Response:
    """delete_organisations_id_applications_app_id_addons_addon_id_2

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_dependencies_dependency_id_1(request: web.Request, dependency_id, app_id, id) -> web.Response:
    """delete_organisations_id_applications_app_id_dependencies_dependency_id_1

    

    :param dependency_id: 
    :type dependency_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_deployments_deployment_id_instances_1(request: web.Request, id, app_id, deployment_id) -> web.Response:
    """delete_organisations_id_applications_app_id_deployments_deployment_id_instances_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_env_env_name_1(request: web.Request, id, app_id, env_name) -> web.Response:
    """delete_organisations_id_applications_app_id_env_env_name_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param env_name: 
    :type env_name: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_instances_1(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_instances_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_tags_tag_1(request: web.Request, id, app_id, tag) -> web.Response:
    """delete_organisations_id_applications_app_id_tags_tag_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param tag: 
    :type tag: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_vhosts_domain_1(request: web.Request, id, app_id, domain) -> web.Response:
    """delete_organisations_id_applications_app_id_vhosts_domain_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param domain: 
    :type domain: str

    """
    return web.Response(status=200)


async def delete_organisations_id_applications_app_id_vhosts_favourite_1(request: web.Request, id, app_id) -> web.Response:
    """delete_organisations_id_applications_app_id_vhosts_favourite_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_consumers_key_0(request: web.Request, id, key) -> web.Response:
    """delete_organisations_id_consumers_key_0

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def delete_organisations_id_members_user_id_0(request: web.Request, id, user_id) -> web.Response:
    """delete_organisations_id_members_user_id_0

    

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def delete_organisations_id_payments_billings_bid_0(request: web.Request, id, bid) -> web.Response:
    """delete_organisations_id_payments_billings_bid_0

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def delete_organisations_id_payments_recurring_0(request: web.Request, id) -> web.Response:
    """delete_organisations_id_payments_recurring_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_network_group_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def get_network_group_member_0(request: web.Request, owner_id, network_group_id, member_id, body=None) -> web.Response:
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


async def get_network_group_peer_0(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
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


async def get_network_group_stream_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def get_network_group_wire_guard_configuration_0(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
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


async def get_network_group_wire_guard_configuration_stream_0(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
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


async def get_organisations_0(request: web.Request, user=None) -> web.Response:
    """get_organisations_0

    

    :param user: 
    :type user: str

    """
    return web.Response(status=200)


async def get_organisations_id_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_addonproviders_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_0(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_features_0(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_features_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_plans_0(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_plans_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_plans_plan_id_0(request: web.Request, id, provider_id, plan_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_plans_plan_id_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param plan_id: 
    :type plan_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addonproviders_provider_id_tags_0(request: web.Request, id, provider_id) -> web.Response:
    """get_organisations_id_addonproviders_provider_id_tags_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_1(request: web.Request, id) -> web.Response:
    """get_organisations_id_addons_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_1(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_applications_2(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_applications_2

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_env_1(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_env_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_sso_0(request: web.Request, provider_id, id) -> web.Response:
    """get_organisations_id_addons_addon_id_sso_0

    

    :param provider_id: 
    :type provider_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_addons_addon_id_tags_1(request: web.Request, id, addon_id) -> web.Response:
    """get_organisations_id_addons_addon_id_tags_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_1(request: web.Request, id) -> web.Response:
    """get_organisations_id_applications_1

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_2(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_2

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_addons_env_2(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_addons_env_2

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_dependencies_1(request: web.Request, app_id, id) -> web.Response:
    """get_organisations_id_applications_app_id_dependencies_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_dependents_1(request: web.Request, app_id, id) -> web.Response:
    """get_organisations_id_applications_app_id_dependents_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_deployments_1(request: web.Request, id, app_id, limit=None, offset=None, action=None) -> web.Response:
    """get_organisations_id_applications_app_id_deployments_1

    

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


async def get_organisations_id_applications_app_id_env_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_env_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_instances_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_instances_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_tags_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_tags_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_vhosts_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_vhosts_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_applications_app_id_vhosts_favourite_1(request: web.Request, id, app_id) -> web.Response:
    """get_organisations_id_applications_app_id_vhosts_favourite_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumers_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_consumers_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumers_key_0(request: web.Request, id, key) -> web.Response:
    """get_organisations_id_consumers_key_0

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumers_key_secret_0(request: web.Request, id, key) -> web.Response:
    """get_organisations_id_consumers_key_secret_0

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def get_organisations_id_consumptions_0(request: web.Request, id, app_id=None, _from=None, to=None) -> web.Response:
    """get_organisations_id_consumptions_0

    

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


async def get_organisations_id_credits_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_credits_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_deployments_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_deployments_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_instances_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_instances_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_members_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_members_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payment_info_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_payment_info_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_0(request: web.Request, id) -> web.Response:
    """get_organisations_id_payments_billings_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_bid_0(request: web.Request, id, bid) -> web.Response:
    """get_organisations_id_payments_billings_bid_0

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_billings_bid_pdf_0(request: web.Request, id, bid, token=None) -> web.Response:
    """get_organisations_id_payments_billings_bid_pdf_0

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str
    :param token: 
    :type token: str

    """
    return web.Response(status=200)


async def get_organisations_id_payments_full_price_price_0(request: web.Request, id, price) -> web.Response:
    """get_organisations_id_payments_full_price_price_0

    

    :param id: 
    :type id: str
    :param price: 
    :type price: str

    """
    return web.Response(status=200)


async def list_network_group_members_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def list_network_group_peers_0(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
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


async def list_network_groups_0(request: web.Request, owner_id, body=None) -> web.Response:
    """List Network Groups

    Lists Network Groups from an owner.

    :param owner_id: Automatically added
    :type owner_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def organisations_id_addonproviders_provider_id_delete_0(request: web.Request, id, provider_id) -> web.Response:
    """Remove an add-on provider

    Remove a given add-on provider. providerId must be owned by organisation {id}.

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_instances_get_1(request: web.Request, id, addon_id, deployment_id=None, with_deleted=None) -> web.Response:
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


async def organisations_id_addons_addon_id_instances_instance_id_get_1(request: web.Request, instance_id, id, addon_id) -> web.Response:
    """Get a specific instance for {addonId}

    

    :param instance_id: 
    :type instance_id: str
    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_get_1(request: web.Request, id, addon_id) -> web.Response:
    """Get past migrations from add-on.

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_migration_id_get_1(request: web.Request, migration_id, id, addon_id) -> web.Response:
    """Get a given migration

    

    :param migration_id: 
    :type migration_id: str
    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_addon_id_migrations_post_1(request: web.Request, id, addon_id, body) -> web.Response:
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


async def organisations_id_addons_addon_id_sso_get_1(request: web.Request, id, addon_id) -> web.Response:
    """organisations_id_addons_addon_id_sso_get_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str

    """
    return web.Response(status=200)


async def organisations_id_addons_preorders_post_1(request: web.Request, id, body) -> web.Response:
    """organisations_id_addons_preorders_post_1

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def organisations_id_applications_app_id_branch_put_1(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_branch_put_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_branches_get_1(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_branches_get_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_buildflavor_put_1(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_buildflavor_put_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_dependencies_env_get_1(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_dependencies_env_get_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_deployments_deployment_id_get_1(request: web.Request, app_id, deployment_id, id) -> web.Response:
    """organisations_id_applications_app_id_deployments_deployment_id_get_1

    

    :param app_id: 
    :type app_id: str
    :param deployment_id: 
    :type deployment_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_exposed_env_get_1(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_exposed_env_get_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_exposed_env_put_1(request: web.Request, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_exposed_env_put_1

    

    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_applications_app_id_instances_instance_id_get_1(request: web.Request, instance_id, app_id, id) -> web.Response:
    """organisations_id_applications_app_id_instances_instance_id_get_1

    

    :param instance_id: 
    :type instance_id: str
    :param app_id: 
    :type app_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_billings_unpaid_get_0(request: web.Request, id) -> web.Response:
    """organisations_id_payments_billings_unpaid_get_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_default_get_0(request: web.Request, id) -> web.Response:
    """organisations_id_payments_methods_default_get_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_default_put_0(request: web.Request, id, body) -> web.Response:
    """organisations_id_payments_methods_default_put_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PaymentData.from_dict(body)
    return web.Response(status=200)


async def organisations_id_payments_methods_get_0(request: web.Request, id) -> web.Response:
    """organisations_id_payments_methods_get_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_mid_delete_0(request: web.Request, m_id, id) -> web.Response:
    """organisations_id_payments_methods_mid_delete_0

    

    :param m_id: 
    :type m_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_methods_post_0(request: web.Request, id, body) -> web.Response:
    """organisations_id_payments_methods_post_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def organisations_id_payments_monthlyinvoice_get_0(request: web.Request, id) -> web.Response:
    """organisations_id_payments_monthlyinvoice_get_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_monthlyinvoice_maxcredit_put_0(request: web.Request, id) -> web.Response:
    """organisations_id_payments_monthlyinvoice_maxcredit_put_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def organisations_id_payments_recurring_get_0(request: web.Request, id) -> web.Response:
    """organisations_id_payments_recurring_get_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def post_organisations_0(request: web.Request, body) -> web.Response:
    """post_organisations_0

    

    :param body: 
    :type body: dict | bytes

    """
    body = WannabeOrganisation.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_0(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_addonproviders_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddonProvider.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_provider_id_features_0(request: web.Request, id, provider_id, body) -> web.Response:
    """post_organisations_id_addonproviders_provider_id_features_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeFeature.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_provider_id_plans_0(request: web.Request, id, provider_id, body) -> web.Response:
    """post_organisations_id_addonproviders_provider_id_plans_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabePlan.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_addonproviders_provider_id_testers_0(request: web.Request, id, provider_id) -> web.Response:
    """post_organisations_id_addonproviders_provider_id_testers_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def post_organisations_id_addons_1(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_addons_1

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_1(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_applications_1

    Creates an application. If you want to create a Github app, you need to replace the oauthApp field with what you will find here: https://github.com/CleverCloud/doc.clever-cloud.com/issues/179

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_addons_2(request: web.Request, id, app_id, body) -> web.Response:
    """post_organisations_id_applications_app_id_addons_2

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Body.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_applications_app_id_instances_1(request: web.Request, id, app_id, commit=None) -> web.Response:
    """post_organisations_id_applications_app_id_instances_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param commit: 
    :type commit: str

    """
    return web.Response(status=200)


async def post_organisations_id_consumers_0(request: web.Request, id, body) -> web.Response:
    """post_organisations_id_consumers_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def post_organisations_id_members_0(request: web.Request, id, body, invitation_key=None) -> web.Response:
    """post_organisations_id_members_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: 
    :param invitation_key: 
    :type invitation_key: str

    """
    return web.Response(status=200)


async def post_organisations_id_payments_billings_0(request: web.Request, id) -> web.Response:
    """post_organisations_id_payments_billings_0

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def put_organisations_id_0(request: web.Request, id, body) -> web.Response:
    """put_organisations_id_0

    

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeOrganisation.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addonproviders_provider_id_0(request: web.Request, id, provider_id, body) -> web.Response:
    """put_organisations_id_addonproviders_provider_id_0

    

    :param id: 
    :type id: str
    :param provider_id: 
    :type provider_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddonProvider.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addonproviders_provider_id_plans_plan_id_0(request: web.Request, id, provider_id, plan_id, body) -> web.Response:
    """put_organisations_id_addonproviders_provider_id_plans_plan_id_0

    

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


async def put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0(request: web.Request, id, feature_name, provider_id, plan_id, body) -> web.Response:
    """put_organisations_id_addonproviders_provider_id_plans_plan_id_features_feature_name_0

    

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


async def put_organisations_id_addons_addon_id_1(request: web.Request, id, addon_id, body) -> web.Response:
    """put_organisations_id_addons_addon_id_1

    

    :param id: 
    :type id: str
    :param addon_id: 
    :type addon_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeAddon.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_addons_addon_id_tags_tag_1(request: web.Request, id, tag, addon_id, body) -> web.Response:
    """put_organisations_id_addons_addon_id_tags_tag_1

    

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


async def put_organisations_id_applications_app_id_1(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeApplication.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_dependencies_dependency_id_1(request: web.Request, dependency_id, app_id, id, body) -> web.Response:
    """put_organisations_id_applications_app_id_dependencies_dependency_id_1

    

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


async def put_organisations_id_applications_app_id_env_1(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_env_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeEnv.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_applications_app_id_env_env_name_1(request: web.Request, id, app_id, env_name, body) -> web.Response:
    """put_organisations_id_applications_app_id_env_env_name_1

    

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


async def put_organisations_id_applications_app_id_tags_tag_1(request: web.Request, id, app_id, tag, body) -> web.Response:
    """put_organisations_id_applications_app_id_tags_tag_1

    

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


async def put_organisations_id_applications_app_id_vhosts_domain_1(request: web.Request, id, app_id, domain, body) -> web.Response:
    """put_organisations_id_applications_app_id_vhosts_domain_1

    

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


async def put_organisations_id_applications_app_id_vhosts_favourite_1(request: web.Request, id, app_id, body) -> web.Response:
    """put_organisations_id_applications_app_id_vhosts_favourite_1

    

    :param id: 
    :type id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Vhost.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_avatar_0(request: web.Request, id) -> web.Response:
    """put_organisations_id_avatar_0

    If you want to upload an image from your computer, send the image in the body of the request without anything else.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def put_organisations_id_consumers_key_0(request: web.Request, id, key, body) -> web.Response:
    """put_organisations_id_consumers_key_0

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str
    :param body: 
    :type body: dict | bytes

    """
    body = WannabeConsumer.from_dict(body)
    return web.Response(status=200)


async def put_organisations_id_members_user_id_0(request: web.Request, id, user_id, body) -> web.Response:
    """put_organisations_id_members_user_id_0

    

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def put_organisations_id_payments_billings_bid_0(request: web.Request, id, bid) -> web.Response:
    """put_organisations_id_payments_billings_bid_0

    

    :param id: 
    :type id: str
    :param bid: 
    :type bid: str

    """
    return web.Response(status=200)
