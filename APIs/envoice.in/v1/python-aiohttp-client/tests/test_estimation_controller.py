# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.estimation_change_status_api_model import EstimationChangeStatusApiModel
from openapi_server.models.estimation_create_api_model import EstimationCreateApiModel
from openapi_server.models.estimation_delete_api_model import EstimationDeleteApiModel
from openapi_server.models.estimation_full_details_api_model import EstimationFullDetailsApiModel
from openapi_server.models.estimation_update_api_model import EstimationUpdateApiModel
from openapi_server.models.estimation_uri_api_model import EstimationUriApiModel
from openapi_server.models.invoice_full_details_api_model import InvoiceFullDetailsApiModel
from openapi_server.models.list_result_estimation_details_api_model import ListResultEstimationDetailsApiModel
from openapi_server.models.send_estimation_to_client_api_model import SendEstimationToClientApiModel


pytestmark = pytest.mark.asyncio

async def test_estimation_api_all(client):
    """Test case for estimation_api_all

    Return all estimation for the account
    """
    params = [('queryOptions.page', 56),
                    ('queryOptions.pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/estimation/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimation_api_change_status(client):
    """Test case for estimation_api_change_status

    Change estimation status
    """
    body = {"Status":"Draft","Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/estimation/changestatus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimation_api_convert(client):
    """Test case for estimation_api_convert

    Convert the estimation to an invoice
    """
    body = 56
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/estimation/convert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimation_api_delete(client):
    """Test case for estimation_api_delete

    Delete an existing estimation
    """
    body = {"Id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/estimation/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_estimation_api_details(client):
    """Test case for estimation_api_details

    Return estimation data
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/estimation/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimation_api_new(client):
    """Test case for estimation_api_new

    Create an estimation
    """
    body = {"Status":"Draft","ClonedFromId":1,"PoNumber":"PoNumber","ExpiresOn":"2000-01-23T04:56:07.000+00:00","Terms":"Terms","Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":5,"Number":"Number","IssuedOn":"2000-01-23T04:56:07.000+00:00","PaymentGateways":[{"Name":"Name"},{"Name":"Name"}],"ClientId":6,"Items":[{"WorkTypeId":2,"Description":"Description","DiscountPercentage":2.3021358869347655,"TaxPercentage":3.616076749251911,"Quantity":7.061401241503109,"TaxId":9,"Cost":5.637376656633329},{"WorkTypeId":2,"Description":"Description","DiscountPercentage":2.3021358869347655,"TaxPercentage":3.616076749251911,"Quantity":7.061401241503109,"TaxId":9,"Cost":5.637376656633329}],"Notes":"Notes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/estimation/new',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimation_api_send_to_client(client):
    """Test case for estimation_api_send_to_client

    Send the provided estimation to the client
    """
    body = {"Message":"Message","SendToSelf":True,"EstimationId":0,"AttachPdf":True,"Id":6,"Subject":"Subject"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/estimation/sendtoclient',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_estimation_api_status(client):
    """Test case for estimation_api_status

    Retrieve the status of the estimation
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/estimation/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_estimation_api_update(client):
    """Test case for estimation_api_update

    Update an existing estimation
    """
    body = {"Status":"Draft","ClonedFromId":5,"PoNumber":"PoNumber","ExpiresOn":"2000-01-23T04:56:07.000+00:00","Terms":"Terms","Attachments":[{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"},{"Type":"External","OriginalFileName":"OriginalFileName","Size":6,"Id":0,"Link":"Link","ObfuscatedFileName":"ObfuscatedFileName"}],"CurrencyId":5,"Number":"Number","IssuedOn":"2000-01-23T04:56:07.000+00:00","PaymentGateways":[{"Name":"Name"},{"Name":"Name"}],"ClientId":1,"Items":[{"WorkTypeId":1,"Description":"Description","DiscountPercentage":9.301444243932576,"TaxPercentage":7.386281948385884,"Quantity":2.027123023002322,"Id":3,"TaxId":4,"Cost":7.061401241503109},{"WorkTypeId":1,"Description":"Description","DiscountPercentage":9.301444243932576,"TaxPercentage":7.386281948385884,"Quantity":2.027123023002322,"Id":3,"TaxId":4,"Cost":7.061401241503109}],"Id":2,"Notes":"Notes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='POST',
        path='/api/estimation/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_estimation_api_uri(client):
    """Test case for estimation_api_uri

    Return the unique url to the client's invoice
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/estimation/uri',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

