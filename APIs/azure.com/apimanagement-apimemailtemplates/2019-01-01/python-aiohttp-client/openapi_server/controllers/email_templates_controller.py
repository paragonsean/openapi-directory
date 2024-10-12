from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_template_create_or_update_request import EmailTemplateCreateOrUpdateRequest
from openapi_server.models.email_template_get200_response import EmailTemplateGet200Response
from openapi_server.models.email_template_list_by_service_default_response import EmailTemplateListByServiceDefaultResponse
from openapi_server import util


async def email_template_create_or_update(request: web.Request, resource_group_name, service_name, template_name, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """email_template_create_or_update

    Updates an Email Template.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param template_name: Email Template Name Identifier.
    :type template_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Email Template update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = EmailTemplateCreateOrUpdateRequest.from_dict(parameters)
    return web.Response(status=200)


async def email_template_delete(request: web.Request, resource_group_name, service_name, template_name, if_match, api_version, subscription_id) -> web.Response:
    """email_template_delete

    Reset the Email Template to default template provided by the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param template_name: Email Template Name Identifier.
    :type template_name: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def email_template_get(request: web.Request, resource_group_name, service_name, template_name, api_version, subscription_id) -> web.Response:
    """email_template_get

    Gets the details of the email template specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param template_name: Email Template Name Identifier.
    :type template_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def email_template_get_entity_tag(request: web.Request, resource_group_name, service_name, template_name, api_version, subscription_id) -> web.Response:
    """email_template_get_entity_tag

    Gets the entity state (Etag) version of the email template specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param template_name: Email Template Name Identifier.
    :type template_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def email_template_update(request: web.Request, resource_group_name, service_name, template_name, if_match, api_version, subscription_id, parameters) -> web.Response:
    """email_template_update

    Updates the specific Email Template.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param template_name: Email Template Name Identifier.
    :type template_name: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = EmailTemplateCreateOrUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
