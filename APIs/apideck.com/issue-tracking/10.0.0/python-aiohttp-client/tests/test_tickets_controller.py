# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_ticket_response import CreateTicketResponse
from openapi_server.models.delete_ticket_response import DeleteTicketResponse
from openapi_server.models.get_ticket_response import GetTicketResponse
from openapi_server.models.get_tickets_response import GetTicketsResponse
from openapi_server.models.issues_filter import IssuesFilter
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.ticket import Ticket
from openapi_server.models.tickets_sort import TicketsSort
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_ticket_response import UpdateTicketResponse


pytestmark = pytest.mark.asyncio

async def test_collection_tickets_add(client):
    """Test case for collection_tickets_add

    Create Ticket
    """
    body = {"subject":"Technical Support Request","due_date":"2020-09-30T07:43:32Z","assignees":[{"id":"12345","username":"Cocoa"},{"id":"12345","username":"Cocoa"}],"created_at":"2020-09-30T07:43:32Z","description":"I am facing issues with my internet connection","priority":"high","type":"Technical","created_by":"12345","custom_mappings":"{}","tags":[{"name":"User Experience","id":"12345","custom_mappings":"{}"},{"name":"User Experience","id":"12345","custom_mappings":"{}"}],"collection_id":"12345","completed_at":"2020-09-30T07:43:32Z","updated_at":"2020-09-30T07:43:32Z","parent_id":"12345","id":"12345","status":"open"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/issue-tracking/collections/{collection_id}/tickets'.format(collection_id='apideck-io'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_tickets_all(client):
    """Test case for collection_tickets_all

    List Tickets
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('sort', openapi_server.TicketsSort()),
                    ('filter', openapi_server.IssuesFilter()),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/issue-tracking/collections/{collection_id}/tickets'.format(collection_id='apideck-io'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_tickets_delete(client):
    """Test case for collection_tickets_delete

    Delete Ticket
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}'.format(ticket_id='ticket_id_example', collection_id='apideck-io'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_tickets_one(client):
    """Test case for collection_tickets_one

    Get Ticket
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}'.format(ticket_id='ticket_id_example', collection_id='apideck-io'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_tickets_update(client):
    """Test case for collection_tickets_update

    Update Ticket
    """
    body = {"subject":"Technical Support Request","due_date":"2020-09-30T07:43:32Z","assignees":[{"id":"12345","username":"Cocoa"},{"id":"12345","username":"Cocoa"}],"created_at":"2020-09-30T07:43:32Z","description":"I am facing issues with my internet connection","priority":"high","type":"Technical","created_by":"12345","custom_mappings":"{}","tags":[{"name":"User Experience","id":"12345","custom_mappings":"{}"},{"name":"User Experience","id":"12345","custom_mappings":"{}"}],"collection_id":"12345","completed_at":"2020-09-30T07:43:32Z","updated_at":"2020-09-30T07:43:32Z","parent_id":"12345","id":"12345","status":"open"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}'.format(ticket_id='ticket_id_example', collection_id='apideck-io'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

