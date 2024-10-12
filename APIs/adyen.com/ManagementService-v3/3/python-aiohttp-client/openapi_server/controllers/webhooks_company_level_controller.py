from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_company_webhook_request import CreateCompanyWebhookRequest
from openapi_server.models.generate_hmac_key_response import GenerateHmacKeyResponse
from openapi_server.models.list_webhooks_response import ListWebhooksResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.test_company_webhook_request import TestCompanyWebhookRequest
from openapi_server.models.test_webhook_response import TestWebhookResponse
from openapi_server.models.update_company_webhook_request import UpdateCompanyWebhookRequest
from openapi_server.models.webhook import Webhook
from openapi_server import util


async def delete_companies_company_id_webhooks_webhook_id(request: web.Request, company_id, webhook_id) -> web.Response:
    """Remove a webhook

    Remove the configuration for the webhook identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param webhook_id: Unique identifier of the webhook configuration.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def get_companies_company_id_webhooks(request: web.Request, company_id, page_number=None, page_size=None) -> web.Response:
    """List all webhooks

    Lists all webhook configurations for the company account.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

    :param company_id: Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    :type company_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_companies_company_id_webhooks_webhook_id(request: web.Request, company_id, webhook_id) -> web.Response:
    """Get a webhook

    Returns the configuration for the webhook identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read * Management API—Webhooks read and write

    :param company_id: Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    :type company_id: str
    :param webhook_id: Unique identifier of the webhook configuration.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def patch_companies_company_id_webhooks_webhook_id(request: web.Request, company_id, webhook_id, body=None) -> web.Response:
    """Update a webhook

    Make changes to the configuration of the webhook identified in the path. The request contains the new values you want to have in the webhook configuration. The response contains the full configuration for the webhook, which includes the new values from the request.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param webhook_id: Unique identifier of the webhook configuration.
    :type webhook_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCompanyWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def post_companies_company_id_webhooks(request: web.Request, company_id, body=None) -> web.Response:
    """Set up a webhook

    Subscribe to receive webhook notifications about events related to your company account. You can add basic authentication to make sure the data is secure.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

    :param company_id: Unique identifier of the [company account](https://docs.adyen.com/account/account-structure#company-account).
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCompanyWebhookRequest.from_dict(body)
    return web.Response(status=200)


async def post_companies_company_id_webhooks_webhook_id_generate_hmac(request: web.Request, company_id, webhook_id) -> web.Response:
    """Generate an HMAC key

    Returns an [HMAC key](https://en.wikipedia.org/wiki/HMAC) for the webhook identified in the path. This key allows you to check the integrity and the origin of the notifications you receive.By creating an HMAC key, you start receiving [HMAC-signed notifications](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures#enable-hmac-signatures) from Adyen. Find out more about how to [verify HMAC signatures](https://docs.adyen.com/development-resources/webhooks/verify-hmac-signatures).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param webhook_id: Unique identifier of the webhook configuration.
    :type webhook_id: str

    """
    return web.Response(status=200)


async def post_companies_company_id_webhooks_webhook_id_test(request: web.Request, company_id, webhook_id, body=None) -> web.Response:
    """Test a webhook

    Sends sample notifications to test if the webhook is set up correctly.  We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the webhook is configured for more than 20 merchant accounts, use the &#x60;merchantIds&#x60; array to specify a subset of the merchant accounts for which to send test notifications.  We send four test notifications for each event code you choose. They cover success and failure scenarios for the hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom notifications, we only send the specified custom notification.  The response describes the result of the test. The &#x60;status&#x60; field tells you if the test was successful or not. You can use the other response fields to troubleshoot unsuccessful tests.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Webhooks read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param webhook_id: Unique identifier of the webhook configuration.
    :type webhook_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestCompanyWebhookRequest.from_dict(body)
    return web.Response(status=200)
