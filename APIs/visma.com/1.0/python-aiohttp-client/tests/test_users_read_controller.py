# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flextime_adjustment_output_model import FlextimeAdjustmentOutputModel
from openapi_server.models.flextime_model import FlextimeModel
from openapi_server.models.get_users_purpose import GetUsersPurpose
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.project_member_cost_exception_output_model import ProjectMemberCostExceptionOutputModel
from openapi_server.models.user_custom_value_output_model import UserCustomValueOutputModel
from openapi_server.models.user_keyword_model import UserKeywordModel
from openapi_server.models.user_output_model import UserOutputModel
from openapi_server.models.work_contract_output_model import WorkContractOutputModel
from openapi_server.models.workday_model import WorkdayModel


pytestmark = pytest.mark.asyncio

async def test_flextime_adjustments_get_flextime_adjustment(client):
    """Test case for flextime_adjustments_get_flextime_adjustment

    Get Flextime Adjustment by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/flextimeadjustments/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flextime_adjustments_get_flextime_adjustments(client):
    """Test case for flextime_adjustments_get_flextime_adjustments

    Get the Flextime Adjustments.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/flextimeadjustments'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flextime_get_flextime(client):
    """Test case for flextime_get_flextime

    Get the flextime balance for a user for a specified date. Total balance is returned for the given date. Month balance is the balance for the month of the given date. Values are returned only if the advanced time tracking add-on is active.
    """
    params = [('eventDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/flextime'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_get_user_keywords(client):
    """Test case for keywords_get_user_keywords

    Get all the keywords for user.
    """
    params = [('active', True),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/keywords'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_member_cost_exceptions_get_project_member_cost_exceptions_for_user(client):
    """Test case for project_member_cost_exceptions_get_project_member_cost_exceptions_for_user

    Get all cost exceptions of project members for user.
    """
    params = [('isProjectClosed', True),
                    ('firstRow', 0),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/projectmembercostexceptions'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_values_get_user_custom_value(client):
    """Test case for user_custom_values_get_user_custom_value

    Get user custom value by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/customvalues/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_values_get_user_custom_values(client):
    """Test case for user_custom_values_get_user_custom_values

    Get the user custom values.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isActive', True),
                    ('targets', ['targets_example']),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/customvalues'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_user(client):
    """Test case for users_get_user

    Get user by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_users(client):
    """Test case for users_get_users

    Get users
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isActive', True),
                    ('businessUnitGuids', ['business_unit_guids_example']),
                    ('keywordGuids', ['keyword_guids_example']),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('supervisorUserGuids', ['supervisor_user_guids_example']),
                    ('code', ''),
                    ('email', ''),
                    ('purpose', openapi_server.GetUsersPurpose())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_get_current_work_contract_for_user(client):
    """Test case for work_contracts_get_current_work_contract_for_user

    Gets current work contract for the user
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/workcontracts/current'.format(user_guid='user_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_get_work_contract_0(client):
    """Test case for work_contracts_get_work_contract_0

    Get work contract by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/workcontracts/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_get_work_contracts_for_user(client):
    """Test case for work_contracts_get_work_contracts_for_user

    Get all the work contracts for the user.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/workcontracts'.format(user_guid='user_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workdays_get_workdays(client):
    """Test case for workdays_get_workdays

    Get workdays for a user.
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/workdays'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

