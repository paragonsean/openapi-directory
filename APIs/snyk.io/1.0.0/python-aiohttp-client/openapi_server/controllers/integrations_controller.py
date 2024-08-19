from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_new_integration_request import AddNewIntegrationRequest
from openapi_server.models.clone_an_integration_with_settings_and_credentials_request import CloneAnIntegrationWithSettingsAndCredentialsRequest
from openapi_server.models.get_existing_integration_by_type200_response import GetExistingIntegrationByType200Response
from openapi_server.models.retrieve200_response import Retrieve200Response
from openapi_server.models.update_existing_integration_request import UpdateExistingIntegrationRequest
from openapi_server.models.update_request import UpdateRequest
from openapi_server import util


async def add_new_integration(request: web.Request, org_id, body=None) -> web.Response:
    """Add new integration

    Add new integration for given organization.

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddNewIntegrationRequest.from_dict(body)
    return web.Response(status=200)


async def clone_an_integration_with_settings_and_credentials(request: web.Request, org_id, integration_id, body=None) -> web.Response:
    """Clone an integration (with settings and credentials)

    Clone an integration, including all of its settings and credentials from one organization to another organization in the same group. This API supports both brokered and non-brokered integrations.  Use this API for when you want to share a Broker token between several Snyk organizations (integrations).

    :param org_id: Source organization public ID to clone integration settings from. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param integration_id: Source integration public ID to clone.
    :type integration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CloneAnIntegrationWithSettingsAndCredentialsRequest.from_dict(body)
    return web.Response(status=200)


async def delete_credentials(request: web.Request, org_id, integration_id) -> web.Response:
    """Delete credentials

    Removes any credentials set for this integration. If this is a brokered connection the operation will have no effect.

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param integration_id: The integration ID.
    :type integration_id: str

    """
    return web.Response(status=200)


async def get_existing_integration_by_type(request: web.Request, org_id, type) -> web.Response:
    """Get existing integration by type

    

    :param org_id: The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param type: Integration type.
    :type type: str

    """
    return web.Response(status=200)


async def list(request: web.Request, org_id) -> web.Response:
    """List

    

    :param org_id: The organization public ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str

    """
    return web.Response(status=200)


async def provision_new_broker_token(request: web.Request, org_id, integration_id) -> web.Response:
    """Provision new broker token

    Issue a new and unique provisional broker token for the brokered integration.  Used for zero down-time token rotation with the Snyk Broker. Once provisioned, the token can be used to initialize a new broker client before using the switch API to update the token in use by the integration.  The new provisional token will fail to be created if the integration, or any other integration in the same group, already has one provisioned.

    :param org_id: The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param integration_id: 
    :type integration_id: str

    """
    return web.Response(status=200)


async def retrieve(request: web.Request, org_id, integration_id) -> web.Response:
    """Retrieve

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param integration_id: The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    :type integration_id: str

    """
    return web.Response(status=200)


async def switch_between_broker_tokens(request: web.Request, org_id, integration_id) -> web.Response:
    """Switch between broker tokens

    Switch the existing broker token with the provisioned token for this integration and any other in the same group. Only perform this action when you have a Broker client running with the provisioned token. This action will fail if there is no token provisioned for this integration or any integration in the same group.

    :param org_id: The &#x60;API_KEY&#x60; must have access to this organization.
    :type org_id: str
    :param integration_id: 
    :type integration_id: str

    """
    return web.Response(status=200)


async def update(request: web.Request, org_id, integration_id, body=None) -> web.Response:
    """Update

    

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param integration_id: The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    :type integration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateRequest.from_dict(body)
    return web.Response(status=200)


async def update_existing_integration(request: web.Request, org_id, integration_id, body=None) -> web.Response:
    """Update existing integration

    + Update integration&#39;s credentials for given organization. Integration must be **not brokered**  + Enable or disable brokered integration for given organization. *Credentials required for disabling brokered integration*  Examples in right section:  1. Set up a broker for an existing integration  2. Update credentials for an existing non-brokered integration  3. Disable broker for an existing integration

    :param org_id: The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization.
    :type org_id: str
    :param integration_id: The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    :type integration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateExistingIntegrationRequest.from_dict(body)
    return web.Response(status=200)
