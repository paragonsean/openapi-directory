# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billable_period import BillablePeriod
from openapi_server.models.deleted_project_fee_model import DeletedProjectFeeModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flat_rate_output_model import FlatRateOutputModel
from openapi_server.models.product_type import ProductType
from openapi_server.models.project_fee_output_model import ProjectFeeOutputModel
from openapi_server.models.project_recurring_fee_rule_output_model import ProjectRecurringFeeRuleOutputModel


pytestmark = pytest.mark.asyncio

async def test_flat_rates_get_all_flat_rates(client):
    """Test case for flat_rates_get_all_flat_rates

    Get all flat rates
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('invoiceGuid', 'invoice_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/flatrates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flat_rates_get_flatrate(client):
    """Test case for flat_rates_get_flatrate

    Get flat rate.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/flatrates/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flat_rates_get_flatrates_for_project(client):
    """Test case for flat_rates_get_flatrates_for_project

    Get project's flat rates.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/flatrates'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_deleted_project_fees(client):
    """Test case for project_fees_get_deleted_project_fees

    Get the deleted project fees.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('projectGuids', ['project_guids_example']),
                    ('userGuids', ['user_guids_example']),
                    ('deletedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/deletedprojectfees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_project_fee(client):
    """Test case for project_fees_get_project_fee

    Get projectFee by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectfees/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_project_fees_by_token(client):
    """Test case for project_fees_get_project_fees_by_token

    Get the project fees.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectfees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_project_fees_for_project(client):
    """Test case for project_fees_get_project_fees_for_project

    Get all the project fees for a project
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('productType', openapi_server.ProductType()),
                    ('isBillable', True),
                    ('isBilled', True),
                    ('invoiceableDate', '2013-10-20T19:20:30+01:00'),
                    ('includeRecurringRules', False),
                    ('isBillablePeriodInFuture', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectfees'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_user_project_fees(client):
    """Test case for project_fees_get_user_project_fees

    Get all the projectFees for a user
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('productType', openapi_server.ProductType()),
                    ('isBillable', True),
                    ('isBilled', True),
                    ('invoiceableDate', '2013-10-20T19:20:30+01:00'),
                    ('hasPhase', True),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/projectfees'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_recurring_fee_rules_get_project_recurring_fee_rule(client):
    """Test case for project_recurring_fee_rules_get_project_recurring_fee_rule

    Get project's RecurringFeeRule by ID.
    """
    params = [('includeInactive', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectrecurringfeerules/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_recurring_fee_rules_get_project_recurring_fee_rules(client):
    """Test case for project_recurring_fee_rules_get_project_recurring_fee_rules

    Get the recurring fee rules.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('productType', openapi_server.ProductType()),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectrecurringfeerules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_recurring_fee_rules_get_project_recurring_fee_rules_for_project(client):
    """Test case for project_recurring_fee_rules_get_project_recurring_fee_rules_for_project

    Get all the Recurring Fee Rules for a project
    """
    params = [('productType', openapi_server.ProductType()),
                    ('firstRow', 0),
                    ('rowCount', 56),
                    ('isBillablePeriodInFuture', True),
                    ('billableTimePeriod', openapi_server.BillablePeriod())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectrecurringfeerules'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

