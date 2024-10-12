# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.card_data_post import CardDataPost
from openapi_server.models.card_data_putand_patch import CardDataPutandPatch
from openapi_server.models.card_error import CardError
from openapi_server.models.card_update_error import CardUpdateError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.not_found import NotFound
from openapi_server.models.plan import Plan
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_data import SubscriptionData
from openapi_server.models.subscription_error import SubscriptionError


pytestmark = pytest.mark.asyncio

async def test_billing_cards_create(client):
    """Test case for billing_cards_create

    Create new credit card
    """
    card_data = {"address_line2":"address_line2","address_line1":"address_line1","address_country":"address_country","address_state":"address_state","name":"name","exp_month":0,"address_zip":"address_zip","exp_year":6,"address_city":"address_city","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/billing/cards'.format(namespace='namespace_example'),
        headers=headers,
        json=card_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_cards_delete(client):
    """Test case for billing_cards_delete

    Delete a credit card
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/billing/cards/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_cards_list(client):
    """Test case for billing_cards_list

    Get credit cards
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/cards'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_cards_read(client):
    """Test case for billing_cards_read

    Get credit card by id
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/cards/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_cards_replace(client):
    """Test case for billing_cards_replace

    Replace a credit card
    """
    card_data = {"address_line2":"address_line2","address_line1":"address_line1","address_country":"address_country","address_state":"address_state","name":"name","exp_month":0,"address_zip":"address_zip","exp_year":6,"address_city":"address_city"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/{namespace}/billing/cards/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        json=card_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_cards_update(client):
    """Test case for billing_cards_update

    Update a credit card
    """
    card_data = {"address_line2":"address_line2","address_line1":"address_line1","address_country":"address_country","address_state":"address_state","name":"name","exp_month":0,"address_zip":"address_zip","exp_year":6,"address_city":"address_city"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/billing/cards/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        json=card_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_invoice_items_list(client):
    """Test case for billing_invoice_items_list

    Get invoice items for a given invoice.
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/invoices/{invoice_id}/invoice-items'.format(namespace='namespace_example', invoice_id='invoice_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_invoice_items_read(client):
    """Test case for billing_invoice_items_read

    Get a specific InvoiceItem.
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/invoices/{invoice_id}/invoice-items/{id}'.format(namespace='namespace_example', invoice_id='invoice_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_invoices_list(client):
    """Test case for billing_invoices_list

    Get invoices
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/invoices'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_invoices_read(client):
    """Test case for billing_invoices_read

    Get an invoice
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/invoices/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_plans_list(client):
    """Test case for billing_plans_list

    Get billing plans
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/plans'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_plans_read(client):
    """Test case for billing_plans_read

    Get a billing plan
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/plans/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_subscriptions_create(client):
    """Test case for billing_subscriptions_create

    Create a new subscription
    """
    subscription_data = {"plan":"plan"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/billing/subscriptions'.format(namespace='namespace_example'),
        headers=headers,
        json=subscription_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_subscriptions_delete(client):
    """Test case for billing_subscriptions_delete

    Delete a subscription
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/{namespace}/billing/subscriptions/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_subscriptions_list(client):
    """Test case for billing_subscriptions_list

    Get active subscriptons
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/subscriptions'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_billing_subscriptions_read(client):
    """Test case for billing_subscriptions_read

    Get a subscriptions
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/billing/subscriptions/{id}'.format(namespace='namespace_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_invoice_items_list_0(client):
    """Test case for teams_billing_invoice_items_list_0

    Get team invoice items for a given invoice.
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items'.format(team='team_example', invoice_id='invoice_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_invoice_items_read_0(client):
    """Test case for teams_billing_invoice_items_read_0

    Get a specific team InvoiceItem.
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/billing/invoices/{invoice_id}/invoice-items/{id}'.format(team='team_example', invoice_id='invoice_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_invoices_list_0(client):
    """Test case for teams_billing_invoices_list_0

    Get team invoices
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/billing/invoices'.format(team='team_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_invoices_read_0(client):
    """Test case for teams_billing_invoices_read_0

    Get an invoice
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/billing/invoices/{id}'.format(team='team_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_subscriptions_create_0(client):
    """Test case for teams_billing_subscriptions_create_0

    Create a new team subscription
    """
    subscription_data = {"plan":"plan"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/teams/{team}/billing/subscriptions'.format(team='team_example'),
        headers=headers,
        json=subscription_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_subscriptions_delete_0(client):
    """Test case for teams_billing_subscriptions_delete_0

    Delete a subscription
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/teams/{team}/billing/subscriptions/{id}'.format(team='team_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_subscriptions_list_0(client):
    """Test case for teams_billing_subscriptions_list_0

    Get active team subscriptons
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/billing/subscriptions'.format(team='team_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_billing_subscriptions_read_0(client):
    """Test case for teams_billing_subscriptions_read_0

    Get team subscriptions
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/billing/subscriptions/{id}'.format(team='team_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

