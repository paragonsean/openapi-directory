# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attributes_response import AttributesResponse
from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.customer import Customer
from openapi_server.models.customer_attributes import CustomerAttributes
from openapi_server.models.customer_list import CustomerList
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event_type_list import EventTypeList
from openapi_server.models.new_customer_request import NewCustomerRequest
from openapi_server.models.new_customer_response import NewCustomerResponse
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.update_customer_request import UpdateCustomerRequest
from openapi_server.models.update_customer_response import UpdateCustomerResponse
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.user_list import UserList
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_list import WebhookList


pytestmark = pytest.mark.asyncio

async def test_create_customer(client):
    """Test case for create_customer

    Create customer
    """
    body = {"firstAdminUser":{"lastName":"lastName","needsToChangePassword":True,"gender":"n","receiverLanguage":"receiverLanguage","authData":{"password":"password","method":"method","adConfigId":0,"mustChangePassword":True,"login":"login","oidConfigId":6},"notifyUser":True,"language":"language","authMethods":[{"isEnabled":True,"options":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"authId":"authId"},{"isEnabled":True,"options":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"authId":"authId"}],"login":"login","title":"title","userName":"userName","needsToChangeUserName":False,"firstName":"firstName","password":"password","phone":"phone","email":"email"},"trialDays":6,"userMax":1,"customerAttributes":{"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]},"lockStatus":False,"webhooksMax":5,"companyName":"companyName","isLocked":False,"customerContractType":"demo","providerCustomerId":"providerCustomerId","activationCode":"activationCode","quotaMax":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/provisioning/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_tenant_webhook(client):
    """Test case for create_tenant_webhook

    Create tenant webhook
    """
    body = {"eventTypeNames":["eventTypeNames","eventTypeNames"],"isEnabled":True,"name":"name","secret":"secret","triggerExampleEvent":True,"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/provisioning/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_customer(client):
    """Test case for remove_customer

    Remove customer
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/provisioning/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_customer_attribute(client):
    """Test case for remove_customer_attribute

    Remove customer attribute
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/provisioning/customers/{customer_id}/customerAttributes/{key}'.format(customer_id=56, key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_tenant_webhook(client):
    """Test case for remove_tenant_webhook

    Remove tenant webhook
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/provisioning/webhooks/{webhook_id}'.format(webhook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_customer(client):
    """Test case for request_customer

    Get customer
    """
    params = [('include_attributes', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_customer_attributes(client):
    """Test case for request_customer_attributes

    Request customer attributes
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/customers/{customer_id}/customerAttributes'.format(customer_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_customer_users(client):
    """Test case for request_customer_users

    Request list of customer users
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('include_attributes', True),
                    ('include_roles', True),
                    ('include_manageable_rooms', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/customers/{customer_id}/users'.format(customer_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_customers(client):
    """Test case for request_customers

    Request list of customers
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('include_attributes', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_list_of_event_types_for_tenant(client):
    """Test case for request_list_of_event_types_for_tenant

    Request list of event types
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/webhooks/event_types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_list_of_tenant_webhooks(client):
    """Test case for request_list_of_tenant_webhooks

    Request list of tenant webhooks
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_tenant_webhook(client):
    """Test case for request_tenant_webhook

    Request tenant webhook
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/provisioning/webhooks/{webhook_id}'.format(webhook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_tenant_webhook_lifetime(client):
    """Test case for reset_tenant_webhook_lifetime

    Reset tenant webhook lifetime
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/provisioning/webhooks/{webhook_id}/reset_lifetime'.format(webhook_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_customer_attributes(client):
    """Test case for set_customer_attributes

    Set customer attributes
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/provisioning/customers/{customer_id}/customerAttributes'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_customer(client):
    """Test case for update_customer

    Update customer
    """
    body = {"userMax":6,"lockStatus":False,"webhooksMax":1,"companyName":"companyName","isLocked":False,"customerContractType":"demo","providerCustomerId":"providerCustomerId","quotaMax":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/provisioning/customers/{customer_id}'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_customer_attributes(client):
    """Test case for update_customer_attributes

    Add or edit customer attributes
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/provisioning/customers/{customer_id}/customerAttributes'.format(customer_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_tenant_webhook(client):
    """Test case for update_tenant_webhook

    Update tenant webhook
    """
    body = {"eventTypeNames":["eventTypeNames","eventTypeNames"],"isEnabled":True,"name":"name","secret":"secret","triggerExampleEvent":True,"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_service_token': 'x_sds_service_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/provisioning/webhooks/{webhook_id}'.format(webhook_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

