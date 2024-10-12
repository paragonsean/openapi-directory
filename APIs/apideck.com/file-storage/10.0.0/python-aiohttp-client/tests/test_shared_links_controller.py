# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_shared_link_response import CreateSharedLinkResponse
from openapi_server.models.delete_shared_link_response import DeleteSharedLinkResponse
from openapi_server.models.get_shared_link_response import GetSharedLinkResponse
from openapi_server.models.get_shared_links_response import GetSharedLinksResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.shared_link import SharedLink
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_shared_link_response import UpdateSharedLinkResponse


pytestmark = pytest.mark.asyncio

async def test_shared_links_add(client):
    """Test case for shared_links_add

    Create Shared Link
    """
    body = {"password":"password","expires_at":"2022-09-30T07:43:32Z","updated_at":"2020-09-30T07:43:32Z","password_protected":True,"scope":"company","download_url":"https://www.box.com/shared/static/rh935iit6ewrmw0unyul.jpeg","created_at":"2020-09-30T07:43:32Z","target_id":"target_id","url":"https://www.box.com/s/vspke7y05sb214wjokpk","target":{"name":"sample.jpg","id":"12345","type":"file"}}
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
        path='/file-storage/shared-links',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_links_all(client):
    """Test case for shared_links_all

    List SharedLinks
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
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
        path='/file-storage/shared-links',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_links_delete(client):
    """Test case for shared_links_delete

    Delete Shared Link
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
        path='/file-storage/shared-links/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_links_one(client):
    """Test case for shared_links_one

    Get Shared Link
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
        path='/file-storage/shared-links/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shared_links_update(client):
    """Test case for shared_links_update

    Update Shared Link
    """
    body = {"password":"password","expires_at":"2022-09-30T07:43:32Z","updated_at":"2020-09-30T07:43:32Z","password_protected":True,"scope":"company","download_url":"https://www.box.com/shared/static/rh935iit6ewrmw0unyul.jpeg","created_at":"2020-09-30T07:43:32Z","target_id":"target_id","url":"https://www.box.com/s/vspke7y05sb214wjokpk","target":{"name":"sample.jpg","id":"12345","type":"file"}}
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
        path='/file-storage/shared-links/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

