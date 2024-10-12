from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_messaging_configuration_response import ListMessagingConfigurationResponse
from openapi_server.models.verify_v2_service_messaging_configuration import VerifyV2ServiceMessagingConfiguration
from openapi_server import util


async def create_messaging_configuration(request: web.Request, service_sid, country, messaging_service_sid) -> web.Response:
    """create_messaging_configuration

    Create a new MessagingConfiguration for a service.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
    :type service_sid: str
    :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value &#x60;all&#x60;.
    :type country: str
    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.
    :type messaging_service_sid: str

    """
    return web.Response(status=200)


async def delete_messaging_configuration(request: web.Request, service_sid, country) -> web.Response:
    """delete_messaging_configuration

    Delete a specific MessagingConfiguration.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
    :type service_sid: str
    :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value &#x60;all&#x60;.
    :type country: str

    """
    return web.Response(status=200)


async def fetch_messaging_configuration(request: web.Request, service_sid, country) -> web.Response:
    """fetch_messaging_configuration

    Fetch a specific MessagingConfiguration.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
    :type service_sid: str
    :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value &#x60;all&#x60;.
    :type country: str

    """
    return web.Response(status=200)


async def list_messaging_configuration(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_messaging_configuration

    Retrieve a list of all Messaging Configurations for a Service.

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_messaging_configuration(request: web.Request, service_sid, country, messaging_service_sid) -> web.Response:
    """update_messaging_configuration

    Update a specific MessagingConfiguration

    :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) that the resource is associated with.
    :type service_sid: str
    :param country: The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country this configuration will be applied to. If this is a global configuration, Country will take the value &#x60;all&#x60;.
    :type country: str
    :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to be used to send SMS to the country of this configuration.
    :type messaging_service_sid: str

    """
    return web.Response(status=200)
