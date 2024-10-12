# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_timeline_custom_event import CustomerTimelineCustomEvent
from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.lead_source import LeadSource


pytestmark = pytest.mark.asyncio

async def test_delete_customer(client):
    """Test case for delete_customer

    Merge and delete a customer
    """
    params = [('targetCustomerId', 'target_customer_id_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_lead_source(client):
    """Test case for delete_customer_lead_source

    Delete a Lead Source for a customer
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/customers/{id}/lead-source'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer(client):
    """Test case for get_customer

    Retrieve a customer
    """
    params = [('expand', 'expand_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customers/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_collection(client):
    """Test case for get_customer_collection

    Retrieve a list of customers
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('q', 'q_example'),
                    ('expand', 'expand_example'),
                    ('fields', 'fields_example'),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_lead_source(client):
    """Test case for get_customer_lead_source

    Retrieve a customer's Lead Source
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/customers/{id}/lead-source'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_customer(client):
    """Test case for post_customer

    Create a customer (without an ID)
    """
    body = {"lastName":"lastName","updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"lifetimeRevenue":{"amount":4.145608029883936,"amountUsd":7.386281948385884,"currency":""},"invoiceCount":2,"defaultPaymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"revision":1,"tags":[{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""},{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""}],"averageValue":{"amount":9.301444243932576,"amountUsd":3.616076749251911,"currency":""},"paymentToken":"paymentToken","firstName":"firstName","websiteId":"","lastPaymentTime":"","_embedded":[{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}},{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}}],"createdTime":"","id":"","primaryAddress":{"emails":[{"label":"main","value":"rebilly@example.com","primary":True},{"label":"main","value":"rebilly@example.com","primary":True}],"country":"GB","firstName":"Benjamin","lastName":"Franklin","address":"36 Craven St","address2":"address2","city":"London","organization":"{\"$ref\":\"#/components/schemas/ReadyToPayMethods/example/2/feature\"}","postalCode":"WC2N 5NF","region":"London","hash":"056ae6d97c788b9e98b049ebafd7b229bf852221","phoneNumbers":[{"label":"main","value":"512-710-1640","primary":True},{"label":"main","value":"512-710-1640","primary":True}]},"paymentCount":1,"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_customer_timeline_custom_event_type(client):
    """Test case for post_customer_timeline_custom_event_type

    Create Customer Timeline custom event type
    """
    body = {"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"name","createdTime":"","id":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/customer-timeline-custom-events',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_customer(client):
    """Test case for put_customer

    Upsert a customer with predefined ID
    """
    body = {"lastName":"lastName","updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"customFields":{"foo":"bar"},"lifetimeRevenue":{"amount":4.145608029883936,"amountUsd":7.386281948385884,"currency":""},"invoiceCount":2,"defaultPaymentInstrument":{"method":"payment-card","paymentInstrumentId":""},"revision":1,"tags":[{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""},{"updatedTime":"","_links":[{"rel":"self"},{"rel":"self"}],"name":"New","createdTime":"","id":""}],"averageValue":{"amount":9.301444243932576,"amountUsd":3.616076749251911,"currency":""},"paymentToken":"paymentToken","firstName":"firstName","websiteId":"","lastPaymentTime":"","_embedded":[{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}},{"leadSource":{"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}}],"createdTime":"","id":"","primaryAddress":{"emails":[{"label":"main","value":"rebilly@example.com","primary":True},{"label":"main","value":"rebilly@example.com","primary":True}],"country":"GB","firstName":"Benjamin","lastName":"Franklin","address":"36 Craven St","address2":"address2","city":"London","organization":"{\"$ref\":\"#/components/schemas/ReadyToPayMethods/example/2/feature\"}","postalCode":"WC2N 5NF","region":"London","hash":"056ae6d97c788b9e98b049ebafd7b229bf852221","phoneNumbers":[{"label":"main","value":"512-710-1640","primary":True},{"label":"main","value":"512-710-1640","primary":True}]},"paymentCount":1,"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/customers/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_customer_lead_source(client):
    """Test case for put_customer_lead_source

    Create a Lead Source for a customer
    """
    body = {"original":"","_links":[{"rel":"self"},{"rel":"self"}],"clickId":"clickId","medium":"medium","source":"source","content":"content","path":"path","referrer":"referrer","salesAgent":"salesAgent","campaign":"campaign","createdTime":"","term":"term","affiliate":"affiliate","subAffiliate":"subAffiliate"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/customers/{id}/lead-source'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

