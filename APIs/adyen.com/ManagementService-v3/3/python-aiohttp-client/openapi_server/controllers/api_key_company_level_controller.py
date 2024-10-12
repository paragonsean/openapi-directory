from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_api_key_response import GenerateApiKeyResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def post_companies_company_id_api_credentials_api_credential_id_generate_api_key(request: web.Request, company_id, api_credential_id) -> web.Response:
    """Generate new API key

    Returns a new API key for the API credential. You can use the new API key a few minutes after generating it. The old API key stops working 24 hours after generating a new one.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str

    """
    return web.Response(status=200)
