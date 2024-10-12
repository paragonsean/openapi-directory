from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentication_execution_info_representation import AuthenticationExecutionInfoRepresentation
from openapi_server.models.authentication_execution_representation import AuthenticationExecutionRepresentation
from openapi_server.models.authentication_flow_representation import AuthenticationFlowRepresentation
from openapi_server.models.authenticator_config_info_representation import AuthenticatorConfigInfoRepresentation
from openapi_server.models.authenticator_config_representation import AuthenticatorConfigRepresentation
from openapi_server.models.required_action_provider_representation import RequiredActionProviderRepresentation
from openapi_server import util


async def realm_authentication_authenticator_providers_get(request: web.Request, realm) -> web.Response:
    """Get authenticator providers   Returns a list of authenticator providers.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_client_authenticator_providers_get(request: web.Request, realm) -> web.Response:
    """Get client authenticator providers   Returns a list of client authenticator providers.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_config_description_provider_id_get(request: web.Request, realm, provider_id) -> web.Response:
    """Get authenticator provider’s configuration description

    

    :param realm: realm name (not id!)
    :type realm: str
    :param provider_id: 
    :type provider_id: str

    """
    return web.Response(status=200)


async def realm_authentication_config_id_delete(request: web.Request, realm, id) -> web.Response:
    """Delete authenticator configuration

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: Configuration id
    :type id: str

    """
    return web.Response(status=200)


async def realm_authentication_config_id_get(request: web.Request, realm, id) -> web.Response:
    """Get authenticator configuration

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: Configuration id
    :type id: str

    """
    return web.Response(status=200)


async def realm_authentication_config_id_put(request: web.Request, realm, id, body) -> web.Response:
    """Update authenticator configuration

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: Configuration id
    :type id: str
    :param body: JSON describing new state of authenticator configuration
    :type body: dict | bytes

    """
    body = AuthenticatorConfigRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_executions_execution_id_config_post(request: web.Request, realm, execution_id, body) -> web.Response:
    """Update execution with new configuration

    

    :param realm: realm name (not id!)
    :type realm: str
    :param execution_id: Execution id
    :type execution_id: str
    :param body: JSON with new configuration
    :type body: dict | bytes

    """
    body = AuthenticatorConfigRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_executions_execution_id_delete(request: web.Request, realm, execution_id) -> web.Response:
    """Delete execution

    

    :param realm: realm name (not id!)
    :type realm: str
    :param execution_id: Execution id
    :type execution_id: str

    """
    return web.Response(status=200)


async def realm_authentication_executions_execution_id_get(request: web.Request, realm, execution_id) -> web.Response:
    """Get Single Execution

    

    :param realm: realm name (not id!)
    :type realm: str
    :param execution_id: Execution id
    :type execution_id: str

    """
    return web.Response(status=200)


async def realm_authentication_executions_execution_id_lower_priority_post(request: web.Request, realm, execution_id) -> web.Response:
    """Lower execution’s priority

    

    :param realm: realm name (not id!)
    :type realm: str
    :param execution_id: Execution id
    :type execution_id: str

    """
    return web.Response(status=200)


async def realm_authentication_executions_execution_id_raise_priority_post(request: web.Request, realm, execution_id) -> web.Response:
    """Raise execution’s priority

    

    :param realm: realm name (not id!)
    :type realm: str
    :param execution_id: Execution id
    :type execution_id: str

    """
    return web.Response(status=200)


async def realm_authentication_executions_post(request: web.Request, realm, body) -> web.Response:
    """Add new authentication execution

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: JSON model describing authentication execution
    :type body: dict | bytes

    """
    body = AuthenticationExecutionRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_flows_flow_alias_copy_post(request: web.Request, realm, flow_alias, body) -> web.Response:
    """Copy existing authentication flow under a new name   The new name is given as &#39;newName&#39; attribute of the passed JSON object

    

    :param realm: realm name (not id!)
    :type realm: str
    :param flow_alias: Name of the existing authentication flow
    :type flow_alias: str
    :param body: JSON containing &#39;newName&#39; attribute
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def realm_authentication_flows_flow_alias_executions_execution_post(request: web.Request, realm, flow_alias, body) -> web.Response:
    """Add new authentication execution to a flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param flow_alias: Alias of parent flow
    :type flow_alias: str
    :param body: New execution JSON data containing &#39;provider&#39; attribute
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def realm_authentication_flows_flow_alias_executions_flow_post(request: web.Request, realm, flow_alias, body) -> web.Response:
    """Add new flow with new execution to existing flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param flow_alias: Alias of parent authentication flow
    :type flow_alias: str
    :param body: New authentication flow / execution JSON data containing &#39;alias&#39;, &#39;type&#39;, &#39;provider&#39;, and &#39;description&#39; attributes
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def realm_authentication_flows_flow_alias_executions_get(request: web.Request, realm, flow_alias) -> web.Response:
    """Get authentication executions for a flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param flow_alias: Flow alias
    :type flow_alias: str

    """
    return web.Response(status=200)


async def realm_authentication_flows_flow_alias_executions_put(request: web.Request, realm, flow_alias, body) -> web.Response:
    """Update authentication executions of a flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param flow_alias: Flow alias
    :type flow_alias: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticationExecutionInfoRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_flows_get(request: web.Request, realm) -> web.Response:
    """Get authentication flows   Returns a list of authentication flows.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_flows_id_delete(request: web.Request, realm, id) -> web.Response:
    """Delete an authentication flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: Flow id
    :type id: str

    """
    return web.Response(status=200)


async def realm_authentication_flows_id_get(request: web.Request, realm, id) -> web.Response:
    """Get authentication flow for id

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: Flow id
    :type id: str

    """
    return web.Response(status=200)


async def realm_authentication_flows_id_put(request: web.Request, realm, id, body) -> web.Response:
    """Update an authentication flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: Flow id
    :type id: str
    :param body: Authentication flow representation
    :type body: dict | bytes

    """
    body = AuthenticationFlowRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_flows_post(request: web.Request, realm, body) -> web.Response:
    """Create a new authentication flow

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: Authentication flow representation
    :type body: dict | bytes

    """
    body = AuthenticationFlowRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_form_action_providers_get(request: web.Request, realm) -> web.Response:
    """Get form action providers   Returns a list of form action providers.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_form_providers_get(request: web.Request, realm) -> web.Response:
    """Get form providers   Returns a list of form providers.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_per_client_config_description_get(request: web.Request, realm) -> web.Response:
    """Get configuration descriptions for all clients

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_register_required_action_post(request: web.Request, realm, body) -> web.Response:
    """Register a new required actions

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: JSON containing &#39;providerId&#39;, and &#39;name&#39; attributes.
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def realm_authentication_required_actions_alias_delete(request: web.Request, realm, alias) -> web.Response:
    """Delete required action

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: Alias of required action
    :type alias: str

    """
    return web.Response(status=200)


async def realm_authentication_required_actions_alias_get(request: web.Request, realm, alias) -> web.Response:
    """Get required action for alias

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: Alias of required action
    :type alias: str

    """
    return web.Response(status=200)


async def realm_authentication_required_actions_alias_lower_priority_post(request: web.Request, realm, alias) -> web.Response:
    """Lower required action’s priority

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: Alias of required action
    :type alias: str

    """
    return web.Response(status=200)


async def realm_authentication_required_actions_alias_put(request: web.Request, realm, alias, body) -> web.Response:
    """Update required action

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: Alias of required action
    :type alias: str
    :param body: JSON describing new state of required action
    :type body: dict | bytes

    """
    body = RequiredActionProviderRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_authentication_required_actions_alias_raise_priority_post(request: web.Request, realm, alias) -> web.Response:
    """Raise required action’s priority

    

    :param realm: realm name (not id!)
    :type realm: str
    :param alias: Alias of required action
    :type alias: str

    """
    return web.Response(status=200)


async def realm_authentication_required_actions_get(request: web.Request, realm) -> web.Response:
    """Get required actions   Returns a list of required actions.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_authentication_unregistered_required_actions_get(request: web.Request, realm) -> web.Response:
    """Get unregistered required actions   Returns a list of unregistered required actions.

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)
