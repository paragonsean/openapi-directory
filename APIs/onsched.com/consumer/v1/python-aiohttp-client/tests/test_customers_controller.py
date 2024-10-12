# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.booking_field_list_view_model import BookingFieldListViewModel
from openapi_server.models.country_view_model import CountryViewModel
from openapi_server.models.custom_field_definition_list_view_model import CustomFieldDefinitionListViewModel
from openapi_server.models.customer_input_model import CustomerInputModel
from openapi_server.models.customer_list_view_model import CustomerListViewModel
from openapi_server.models.customer_update_model import CustomerUpdateModel
from openapi_server.models.customer_view_model import CustomerViewModel
from openapi_server.models.state_view_model import StateViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_bookingfields_get(client):
    """Test case for consumer_v1_customers_bookingfields_get

    Get Customer Booking Fields
    """
    params = [('locationId', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/customers/bookingfields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_countries_get(client):
    """Test case for consumer_v1_customers_countries_get

    List Country Codes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/customers/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_customfields_get(client):
    """Test case for consumer_v1_customers_customfields_get

    Get Customer Custom Fields
    """
    params = [('locationId', 'location_id_example'),
                    ('leadQuestions', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/customers/customfields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_get(client):
    """Test case for consumer_v1_customers_get

    List Customers
    """
    params = [('locationId', 'location_id_example'),
                    ('groupId', 'group_id_example'),
                    ('email', 'email_example'),
                    ('lastname', 'lastname_example'),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_id_delete(client):
    """Test case for consumer_v1_customers_id_delete

    Delete Customer
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/consumer/v1/customers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_id_get(client):
    """Test case for consumer_v1_customers_id_get

    Get Customer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/customers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_customers_id_put(client):
    """Test case for consumer_v1_customers_id_put

    Update Customer
    """
    body = {"firstname":"firstname","address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"locationId":"locationId","contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","notificationType":"notificationType","stripeCustomerId":"stripeCustomerId","type":0,"email":"email","lastname":"lastname"}
    headers = { 
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/customers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_customers_post(client):
    """Test case for consumer_v1_customers_post

    Create Customer
    """
    body = {"firstname":"firstname","address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"locationId":"locationId","contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","notificationType":"notificationType","stripeCustomerId":"stripeCustomerId","type":0,"sendLeadNotification":True,"email":"email","lastname":"lastname"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/consumer/v1/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_customers_states_get(client):
    """Test case for consumer_v1_customers_states_get

    List Country States
    """
    params = [('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/customers/states',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

