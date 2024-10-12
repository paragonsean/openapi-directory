# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.offer_statuses_get200_response import OfferStatusesGet200Response
from openapi_server.models.offer_statuses_offer_status_id_get200_response import OfferStatusesOfferStatusIdGet200Response
from openapi_server.models.offer_statuses_post_request import OfferStatusesPostRequest


pytestmark = pytest.mark.asyncio

async def test_offer_statuses_bulk_delete_delete(client):
    """Test case for offer_statuses_bulk_delete_delete

    Bulk delete offer statuses
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/offer_statuses/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_statuses_get(client):
    """Test case for offer_statuses_get

    Get list of offer statuses
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/offer_statuses',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_statuses_offer_status_id_delete(client):
    """Test case for offer_statuses_offer_status_id_delete

    Delete a offer status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/offer_statuses/{offer_status_id}'.format(offer_status_id='offer_status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_statuses_offer_status_id_get(client):
    """Test case for offer_statuses_offer_status_id_get

    Get a single offer status
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/offer_statuses/{offer_status_id}'.format(offer_status_id='offer_status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_statuses_offer_status_id_put(client):
    """Test case for offer_statuses_offer_status_id_put

    Edit a offer status
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/offer_statuses/{offer_status_id}'.format(offer_status_id='offer_status_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offer_statuses_post(client):
    """Test case for offer_statuses_post

    Create a new offer status
    """
    body = openapi_server.OfferStatusesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/offer_statuses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

