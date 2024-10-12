from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_api_credential import CompanyApiCredential
from openapi_server.models.create_company_api_credential_request import CreateCompanyApiCredentialRequest
from openapi_server.models.create_company_api_credential_response import CreateCompanyApiCredentialResponse
from openapi_server.models.list_company_api_credentials_response import ListCompanyApiCredentialsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_company_api_credential_request import UpdateCompanyApiCredentialRequest
from openapi_server import util


async def get_companies_company_id_api_credentials(request: web.Request, company_id, page_number=None, page_size=None) -> web.Response:
    """Get a list of API credentials

    Returns the list of [API credentials](https://docs.adyen.com/development-resources/api-credentials) for the company account. The list is grouped into pages as defined by the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_companies_company_id_api_credentials_api_credential_id(request: web.Request, company_id, api_credential_id) -> web.Response:
    """Get an API credential

    Returns the [API credential](https://docs.adyen.com/development-resources/api-credentials) identified in the path.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str

    """
    return web.Response(status=200)


async def patch_companies_company_id_api_credentials_api_credential_id(request: web.Request, company_id, api_credential_id, body=None) -> web.Response:
    """Update an API credential.

    Changes the API credential&#39;s roles, merchant account access, or allowed origins. The request has the new values for the fields you want to change. The response contains the full updated API credential, including the new values from the request.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param api_credential_id: Unique identifier of the API credential.
    :type api_credential_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateCompanyApiCredentialRequest.from_dict(body)
    return web.Response(status=200)


async def post_companies_company_id_api_credentials(request: web.Request, company_id, body=None) -> web.Response:
    """Create an API credential.

    Creates an [API credential](https://docs.adyen.com/development-resources/api-credentials) for the company account identified in the path. In the request, you can specify which merchant accounts the new API credential will have access to, as well as its roles and allowed origins.  The response includes several types of authentication details: * [API key](https://docs.adyen.com/development-resources/api-authentication#api-key-authentication): used for API request authentication. * [Client key](https://docs.adyen.com/development-resources/client-side-authentication#how-it-works): public key used for client-side authentication. * [Username and password](https://docs.adyen.com/development-resources/api-authentication#using-basic-authentication): used for basic authentication.  &gt; Make sure you store the API key securely in your system. You won&#39;t be able to retrieve it later.  If your API key is lost or compromised, you need to [generate a new API key](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/apiCredentials/{apiCredentialId}/generateApiKey).  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—API credentials read and write

    :param company_id: The unique identifier of the company account.
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCompanyApiCredentialRequest.from_dict(body)
    return web.Response(status=200)
