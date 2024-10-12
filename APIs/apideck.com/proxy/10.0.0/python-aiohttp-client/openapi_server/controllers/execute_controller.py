from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_proxy401_response import GetProxy401Response
from openapi_server.models.post_proxy_request import PostProxyRequest
from openapi_server.models.put_proxy_request import PutProxyRequest
from openapi_server import util


async def delete_proxy(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id, x_apideck_downstream_url, x_apideck_downstream_authorization=None) -> web.Response:
    """DELETE

    Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param x_apideck_downstream_url: Downstream URL
    :type x_apideck_downstream_url: str
    :param x_apideck_downstream_authorization: Downstream authorization header. This will skip the Vault token injection.
    :type x_apideck_downstream_authorization: str

    """
    return web.Response(status=200)


async def get_proxy(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id, x_apideck_downstream_url, x_apideck_downstream_authorization=None) -> web.Response:
    """GET

    Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param x_apideck_downstream_url: Downstream URL
    :type x_apideck_downstream_url: str
    :param x_apideck_downstream_authorization: Downstream authorization header. This will skip the Vault token injection.
    :type x_apideck_downstream_authorization: str

    """
    return web.Response(status=200)


async def options_proxy(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id, x_apideck_downstream_url, x_apideck_downstream_authorization=None) -> web.Response:
    """OPTIONS

    Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param x_apideck_downstream_url: Downstream URL
    :type x_apideck_downstream_url: str
    :param x_apideck_downstream_authorization: Downstream authorization header. This will skip the Vault token injection.
    :type x_apideck_downstream_authorization: str

    """
    return web.Response(status=200)


async def patch_proxy(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id, x_apideck_downstream_url, x_apideck_downstream_authorization=None, body=None) -> web.Response:
    """PATCH

    Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param x_apideck_downstream_url: Downstream URL
    :type x_apideck_downstream_url: str
    :param x_apideck_downstream_authorization: Downstream authorization header. This will skip the Vault token injection.
    :type x_apideck_downstream_authorization: str
    :param body: Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
    :type body: dict | bytes

    """
    body = PostProxyRequest.from_dict(body)
    return web.Response(status=200)


async def post_proxy(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id, x_apideck_downstream_url, x_apideck_downstream_authorization=None, body=None) -> web.Response:
    """POST

    Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param x_apideck_downstream_url: Downstream URL
    :type x_apideck_downstream_url: str
    :param x_apideck_downstream_authorization: Downstream authorization header. This will skip the Vault token injection.
    :type x_apideck_downstream_authorization: str
    :param body: Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
    :type body: dict | bytes

    """
    body = PostProxyRequest.from_dict(body)
    return web.Response(status=200)


async def put_proxy(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id, x_apideck_downstream_url, x_apideck_downstream_authorization=None, body=None) -> web.Response:
    """PUT

    Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param x_apideck_downstream_url: Downstream URL
    :type x_apideck_downstream_url: str
    :param x_apideck_downstream_authorization: Downstream authorization header. This will skip the Vault token injection.
    :type x_apideck_downstream_authorization: str
    :param body: Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
    :type body: dict | bytes

    """
    body = PutProxyRequest.from_dict(body)
    return web.Response(status=200)
