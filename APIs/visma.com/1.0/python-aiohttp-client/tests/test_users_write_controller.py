# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.flextime_adjustment_input_model import FlextimeAdjustmentInputModel
from openapi_server.models.flextime_adjustment_output_model import FlextimeAdjustmentOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.user_custom_value_input_model import UserCustomValueInputModel
from openapi_server.models.user_custom_value_output_model import UserCustomValueOutputModel
from openapi_server.models.user_input_model import UserInputModel
from openapi_server.models.user_keyword_model import UserKeywordModel
from openapi_server.models.user_output_model import UserOutputModel
from openapi_server.models.work_contract_input_model import WorkContractInputModel
from openapi_server.models.work_contract_output_model import WorkContractOutputModel
from openapi_server.models.workday_model import WorkdayModel


pytestmark = pytest.mark.asyncio

async def test_flextime_adjustments_delete_flextime_adjustment(client):
    """Test case for flextime_adjustments_delete_flextime_adjustment

    Delete an flextime adjustment.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/flextimeadjustments/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flextime_adjustments_patch_flextime_adjustment(client):
    """Test case for flextime_adjustments_patch_flextime_adjustment

    Update (Patch) an Flextime Adjustment or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/flextimeadjustments/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flextime_adjustments_post_flextime_adjustment(client):
    """Test case for flextime_adjustments_post_flextime_adjustment

    Insert a flextime adjustment.
    """
    body = {"adjustmentDate":"2000-01-23","amount":0.8008281904610115,"notes":"notes","user":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/flextimeadjustments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_link_keyword_to_user(client):
    """Test case for keywords_link_keyword_to_user

    Link existing keyword to user
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/users/{user_guid}/keywords/{guid}'.format(user_guid='user_guid_example', guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_values_patch_user_custom_value(client):
    """Test case for user_custom_values_patch_user_custom_value

    Update (Patch) a user custom value or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/users/customvalues/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_custom_values_post_user_custom_value(client):
    """Test case for user_custom_values_post_user_custom_value

    Insert a user custom value.
    """
    body = {"user":{"guid":"guid"},"value":"value","customProperty":{"guid":"guid"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/users/customvalues',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_patch_user(client):
    """Test case for users_patch_user

    Update (Patch) an user or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/users/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_post_user(client):
    """Test case for users_post_user

    Insert an user.
    """
    body = {"country":{"guid":"guid"},"lastName":"lastName","businessUnit":{"guid":"guid"},"code":"code","notes":"notes","city":"city","socialSecurityNumber":"socialSecurityNumber","timezone":{"systemName":"systemName","name":"name","guid":"guid","ianaName":"ianaName"},"permissionProfile":{"guid":"guid"},"postalCode":"postalCode","language":{"guid":"guid"},"isActive":True,"bankAccountNumber":"bankAccountNumber","superiorUser":{"guid":"guid"},"email":"email","defaultActivityType":{"guid":"guid"},"address":"address","countryRegion":{"guid":"guid"},"satisfaction":"Unsatisfied","birthDate":"2000-01-23T04:56:07.000+00:00","createDefaultWorkContract":True,"firstName":"firstName","phone":"phone","culture":{"guid":"guid"},"workType":{"guid":"guid"},"salutation":"Mr.","userType":"FullUser"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_patch_work_contract_0(client):
    """Test case for work_contracts_patch_work_contract_0

    Update (Patch) a work contract or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/workcontracts/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_contracts_post_work_contract_0(client):
    """Test case for work_contracts_post_work_contract_0

    Insert a work contract.
    """
    body = {"flextimeLimitPerDay":6.027456183070403,"workWeek":["Monday","Monday"],"role":{"guid":"guid"},"endDate":"2000-01-23","dailyHours":0.8008281904610115,"hourCost":{"amount":1.4658129805029452,"currencyCode":"currencyCode"},"isFlextimeActive":True,"isOvertimeAllowed":True,"title":"title","user":{"guid":"guid"},"startDate":"2000-01-23"}
    params = [('resetFlextime', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/workcontracts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workdays_patch_work_day(client):
    """Test case for workdays_patch_work_day

    Update (Patch) a workday or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/users/{user_guid}/workdays/{_date}'.format(user_guid='user_guid_example', _date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

