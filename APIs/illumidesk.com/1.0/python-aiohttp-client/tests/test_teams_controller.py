# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.group_data import GroupData
from openapi_server.models.group_error import GroupError
from openapi_server.models.group_user import GroupUser
from openapi_server.models.group_user_error import GroupUserError
from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_item import InvoiceItem
from openapi_server.models.not_found import NotFound
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_data import SubscriptionData
from openapi_server.models.subscription_error import SubscriptionError
from openapi_server.models.team import Team
from openapi_server.models.team_data import TeamData
from openapi_server.models.team_error import TeamError


pytestmark = pytest.mark.asyncio

async def test_teams_billing_invoice_items_list(client):
    """Test case for teams_billing_invoice_items_list

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

async def test_teams_billing_invoice_items_read(client):
    """Test case for teams_billing_invoice_items_read

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

async def test_teams_billing_invoices_list(client):
    """Test case for teams_billing_invoices_list

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

async def test_teams_billing_invoices_read(client):
    """Test case for teams_billing_invoices_read

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

async def test_teams_billing_subscriptions_create(client):
    """Test case for teams_billing_subscriptions_create

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

async def test_teams_billing_subscriptions_delete(client):
    """Test case for teams_billing_subscriptions_delete

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

async def test_teams_billing_subscriptions_list(client):
    """Test case for teams_billing_subscriptions_list

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

async def test_teams_billing_subscriptions_read(client):
    """Test case for teams_billing_subscriptions_read

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


pytestmark = pytest.mark.asyncio

async def test_teams_create(client):
    """Test case for teams_create

    Create a new team
    """
    team_data = {"website":"website","avatar_url":"avatar_url","name":"name","description":"description","location":"location","avatar":"avatar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/teams/',
        headers=headers,
        json=team_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_delete(client):
    """Test case for teams_delete

    Delete a team
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/teams/{team}'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_add_to_group(client):
    """Test case for teams_groups_add_to_group

    Add user to group
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/teams/{team}/groups/{group}/add'.format(team='team_example', group='group_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_delete(client):
    """Test case for teams_groups_delete

    Delete team group
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/teams/{team}/groups/{group}'.format(team='team_example', group='group_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_list(client):
    """Test case for teams_groups_list

    Get team groups
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/groups'.format(team='team_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_read(client):
    """Test case for teams_groups_read

    Get team group
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}/groups/{group}'.format(team='team_example', group='group_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_remove_from_group(client):
    """Test case for teams_groups_remove_from_group

    User removed from group
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/teams/{team}/groups/{group}/remove'.format(team='team_example', group='group_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_replace(client):
    """Test case for teams_groups_replace

    Patch team group
    """
    group_data = {"parent":"parent","private":True,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/teams/{team}/groups/{group}'.format(team='team_example', group='group_example'),
        headers=headers,
        json=group_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_groups_update(client):
    """Test case for teams_groups_update

    Patch team group
    """
    group_data = {"parent":"parent","private":True,"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/teams/{team}/groups/{group}'.format(team='team_example', group='group_example'),
        headers=headers,
        json=group_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_list(client):
    """Test case for teams_list

    Get teams
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_read(client):
    """Test case for teams_read

    Get a team
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/teams/{team}'.format(team='team_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_replace(client):
    """Test case for teams_replace

    Replace a team
    """
    team_data = {"website":"website","avatar_url":"avatar_url","name":"name","description":"description","location":"location","avatar":"avatar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/teams/{team}'.format(team='team_example'),
        headers=headers,
        json=team_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_teams_update(client):
    """Test case for teams_update

    Update a team
    """
    team_data = {"website":"website","avatar_url":"avatar_url","name":"name","description":"description","location":"location","avatar":"avatar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/teams/{team}'.format(team='team_example'),
        headers=headers,
        json=team_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

