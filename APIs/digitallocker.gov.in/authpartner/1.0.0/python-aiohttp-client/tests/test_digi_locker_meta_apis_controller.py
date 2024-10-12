# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.doc_type_response import DocTypeResponse
from openapi_server.models.get_device_code_id401_response import GetDeviceCodeId401Response
from openapi_server.models.get_list_of_documents_provided_by_an_issuer_id400_response import GetListOfDocumentsProvidedByAnIssuerId400Response
from openapi_server.models.get_list_of_issuers_id400_response import GetListOfIssuersId400Response
from openapi_server.models.get_search_parameters_for_a_document_id400_response import GetSearchParametersForADocumentId400Response
from openapi_server.models.get_statistics_id400_response import GetStatisticsId400Response
from openapi_server.models.get_statistics_response import GetStatisticsResponse
from openapi_server.models.issuer_response import IssuerResponse
from openapi_server.models.push_urito_account_id400_response import PushURIToAccountId400Response
from openapi_server.models.push_urito_account_id401_response import PushURIToAccountId401Response
from openapi_server.models.push_urito_account_id404_response import PushURIToAccountId404Response
from openapi_server.models.push_urito_account_id500_response import PushURIToAccountId500Response
from openapi_server.models.search_parameters_response_inner import SearchParametersResponseInner
from openapi_server.models.verify_account_id400_response import VerifyAccountId400Response
from openapi_server.models.verify_account_id500_response import VerifyAccountId500Response
from openapi_server.models.verify_account_response import VerifyAccountResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_list_of_documents_provided_by_an_issuer_id(client):
    """Test case for get_list_of_documents_provided_by_an_issuer_id

    Get List of Documents Provided by an Issuer
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'clientid': 'clientid_example',
        'hmac': '/path/to/file',
        'orgid': 'orgid_example',
        'ts': 'ts_example'
        }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/pull/doctype',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_list_of_issuers_id(client):
    """Test case for get_list_of_issuers_id

    Get List of Issuers
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'clientid': 'clientid_example',
        'hmac': '/path/to/file',
        'ts': 'ts_example'
        }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/pull/issuers',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_search_parameters_for_a_document_id(client):
    """Test case for get_search_parameters_for_a_document_id

    Get Search Parameters for a Document
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'clientid': 'clientid_example',
        'doctype': 'doctype_example',
        'hmac': '/path/to/file',
        'orgid': 'orgid_example',
        'ts': 'ts_example'
        }
    response = await client.request(
        method='POST',
        path='/public/oauth2/1/pull/parameters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_get_statistics_id(client):
    """Test case for get_statistics_id

    Get Statistics
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('clientid', 'clientid_example')
    data.add_field('hmac', '/path/to/file')
    data.add_field('ts', 'ts_example')
    response = await client.request(
        method='POST',
        path='/public/statistics/1/counts',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_push_uri_to_account_id(client):
    """Test case for push_uri_to_account_id

    Push URI to Account
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('action', 'action_example')
    data.add_field('clientid', 'clientid_example')
    data.add_field('digilockerid', 56)
    data.add_field('docid', 'docid_example')
    data.add_field('hmac', '/path/to/file')
    data.add_field('issuedate', 'issuedate_example')
    data.add_field('ts', 'ts_example')
    data.add_field('uri', 'uri_example')
    data.add_field('validfrom', 56)
    data.add_field('validto', 'validto_example')
    response = await client.request(
        method='POST',
        path='/public/account/1/pushuri',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_verify_account_id(client):
    """Test case for verify_account_id

    Verify Account
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('clientid', 'clientid_example')
    data.add_field('hmac', '/path/to/file')
    data.add_field('mobile', 56)
    data.add_field('ts', 'ts_example')
    data.add_field('uid', 56)
    response = await client.request(
        method='POST',
        path='/public/account/2/verify',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

