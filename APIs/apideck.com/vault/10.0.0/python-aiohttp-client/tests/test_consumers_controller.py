# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.consumer import Consumer
from openapi_server.models.consumer_request_counts_in_date_range_response import ConsumerRequestCountsInDateRangeResponse
from openapi_server.models.create_consumer_response import CreateConsumerResponse
from openapi_server.models.delete_consumer_response import DeleteConsumerResponse
from openapi_server.models.get_consumer_response import GetConsumerResponse
from openapi_server.models.get_consumers_response import GetConsumersResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_consumer_request import UpdateConsumerRequest
from openapi_server.models.update_consumer_response import UpdateConsumerResponse


pytestmark = pytest.mark.asyncio

async def test_consumer_request_counts_all(client):
    """Test case for consumer_request_counts_all

    Consumer request counts
    """
    params = [('start_datetime', '2021-05-01T12:00:00.000Z'),
                    ('end_datetime', '2021-05-30T12:00:00.000Z')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/consumers/{consumer_id}/stats'.format(consumer_id='test_user_id'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumers_add(client):
    """Test case for consumers_add

    Create consumer
    """
    body = {"consumer_id":"test_consumer_id","metadata":{"image":"https://www.spacex.com/static/images/share.jpg","user_name":"Elon Musk","account_name":"SpaceX","email":"elon@musk.com"},"request_counts":{"proxy":10,"unify":100,"vault":21},"created":"2021-05-07T12:55:42.242Z","request_count_updated":"2021-05-07T12:55:42.242Z","aggregated_request_count":101,"modified":"2021-05-07T12:55:42.242Z","services":["salesforce","stripe"],"application_id":"dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX","connections":[{"settings":{"instance_url":"https://eu28.salesforce.com"},"auth_type":"oauth2","metadata":{"account":{"id":"c01458a5-7276-41ce-bc19-639906b0450a","name":"My Company"},"plan":"enterprise"},"website":"https://www.salesforce.com","icon":"https://res.cloudinary.com/apideck/image/upload/v1529456047/catalog/salesforce/icon128x128.png","created_at":"2020-09-19T12:18:37.071Z","tag_line":"CRM software solutions and enterprise cloud computing from Salesforce, the leader in customer relationship management (CRM) and PaaS. Free 30 day trial.","enabled":True,"consumer_id":"test_user_id","updated_at":"2020-09-19T12:18:37.071Z","service_id":"teamleader","name":"Salesforce","logo":"https://c1.sfdcstatic.com/content/dam/web/en_us/www/images/home/logo-salesforce-m.svg","id":"1111+test_user_id","state":"authorized","unified_api":"crm"},{"settings":{"instance_url":"https://eu28.salesforce.com"},"auth_type":"oauth2","metadata":{"account":{"id":"c01458a5-7276-41ce-bc19-639906b0450a","name":"My Company"},"plan":"enterprise"},"website":"https://www.salesforce.com","icon":"https://res.cloudinary.com/apideck/image/upload/v1529456047/catalog/salesforce/icon128x128.png","created_at":"2020-09-19T12:18:37.071Z","tag_line":"CRM software solutions and enterprise cloud computing from Salesforce, the leader in customer relationship management (CRM) and PaaS. Free 30 day trial.","enabled":True,"consumer_id":"test_user_id","updated_at":"2020-09-19T12:18:37.071Z","service_id":"teamleader","name":"Salesforce","logo":"https://c1.sfdcstatic.com/content/dam/web/en_us/www/images/home/logo-salesforce-m.svg","id":"1111+test_user_id","state":"authorized","unified_api":"crm"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vault/consumers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumers_all(client):
    """Test case for consumers_all

    Get all consumers
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/consumers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumers_delete(client):
    """Test case for consumers_delete

    Delete consumer
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/vault/consumers/{consumer_id}'.format(consumer_id='test_user_id'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumers_one(client):
    """Test case for consumers_one

    Get consumer
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/vault/consumers/{consumer_id}'.format(consumer_id='test_user_id'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumers_update(client):
    """Test case for consumers_update

    Update consumer
    """
    body = {"metadata":{"image":"https://www.spacex.com/static/images/share.jpg","user_name":"Elon Musk","account_name":"SpaceX","email":"elon@musk.com"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/vault/consumers/{consumer_id}'.format(consumer_id='test_user_id'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

