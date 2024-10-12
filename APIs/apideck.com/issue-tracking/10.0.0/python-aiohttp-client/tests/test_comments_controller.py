# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.collection_ticket_comment import CollectionTicketComment
from openapi_server.models.comments_sort import CommentsSort
from openapi_server.models.create_comment_response import CreateCommentResponse
from openapi_server.models.delete_comment_response import DeleteCommentResponse
from openapi_server.models.get_comment_response import GetCommentResponse
from openapi_server.models.get_comments_response import GetCommentsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_comment_response import UpdateCommentResponse


pytestmark = pytest.mark.asyncio

async def test_collection_ticket_comments_add(client):
    """Test case for collection_ticket_comments_add

    Create Comment
    """
    body = {"updated_at":"2020-09-30T07:43:32Z","created_at":"2020-09-30T07:43:32Z","id":"12345","body":"What internet provider do you use?","created_by":"12345","custom_mappings":"{}"}
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
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments'.format(collection_id='apideck-io', ticket_id='ticket_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_ticket_comments_all(client):
    """Test case for collection_ticket_comments_all

    List Comments
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('sort', openapi_server.CommentsSort()),
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
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments'.format(collection_id='apideck-io', ticket_id='ticket_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_ticket_comments_delete(client):
    """Test case for collection_ticket_comments_delete

    Delete Comment
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
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id}'.format(id='id_example', collection_id='apideck-io', ticket_id='ticket_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_ticket_comments_one(client):
    """Test case for collection_ticket_comments_one

    Get Comment
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
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
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id}'.format(id='id_example', collection_id='apideck-io', ticket_id='ticket_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_ticket_comments_update(client):
    """Test case for collection_ticket_comments_update

    Update Comment
    """
    body = {"updated_at":"2020-09-30T07:43:32Z","created_at":"2020-09-30T07:43:32Z","id":"12345","body":"What internet provider do you use?","created_by":"12345","custom_mappings":"{}"}
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
        path='/issue-tracking/collections/{collection_id}/tickets/{ticket_id}/comments/{id}'.format(id='id_example', collection_id='apideck-io', ticket_id='ticket_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

