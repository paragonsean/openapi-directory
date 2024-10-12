# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_list_result import AlertListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_alerts_get_alert_by_management_groups(client):
    """Test case for alerts_get_alert_by_management_groups

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.CostManagement/alerts/{alert_id}'.format(management_group_id='management_group_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_by_account(client):
    """Test case for alerts_get_by_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.CostManagement/alerts/{alert_id}'.format(billing_account_id='billing_account_id_example', enrollment_account_id='enrollment_account_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_by_department(client):
    """Test case for alerts_get_by_department

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/departments/{department_id}/providers/Microsoft.CostManagement/alerts/{alert_id}'.format(billing_account_id='billing_account_id_example', department_id='department_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_by_enrollment(client):
    """Test case for alerts_get_by_enrollment

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/alerts/{alert_id}'.format(billing_account_id='billing_account_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_by_resource_group_name(client):
    """Test case for alerts_get_by_resource_group_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/alerts/{alert_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_get_by_subscription(client):
    """Test case for alerts_get_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/alerts/{alert_id}'.format(subscription_id='subscription_id_example', alert_id='alert_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list(client):
    """Test case for alerts_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/alerts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_by_account(client):
    """Test case for alerts_list_by_account

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.CostManagement/alerts'.format(billing_account_id='billing_account_id_example', enrollment_account_id='enrollment_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_by_department(client):
    """Test case for alerts_list_by_department

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/departments/{department_id}/providers/Microsoft.CostManagement/alerts'.format(billing_account_id='billing_account_id_example', department_id='department_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_by_enrollment(client):
    """Test case for alerts_list_by_enrollment

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/alerts'.format(billing_account_id='billing_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_by_management_groups(client):
    """Test case for alerts_list_by_management_groups

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.CostManagement/alerts'.format(management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_list_by_resource_group_name(client):
    """Test case for alerts_list_by_resource_group_name

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/alerts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_billing_account_alert_status(client):
    """Test case for alerts_update_billing_account_alert_status

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"costEntityId":"costEntityId","creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","scope":"scope","closeTime":"2000-01-23T04:56:07.000+00:00","description":"description","definition":{"criteria":"CostThresholdExceeded","category":"Cost","type":"Budget"},"details":{"key":"details"},"modificationUsername":"modificationUsername","source":"Preset","statusModificationTime":"2000-01-23T04:56:07.000+00:00","status":"Active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/providers/Microsoft.CostManagement/alerts/{alert_id}/updateStatus'.format(billing_account_id='billing_account_id_example', alert_id='alert_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_departments_alert_status(client):
    """Test case for alerts_update_departments_alert_status

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"costEntityId":"costEntityId","creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","scope":"scope","closeTime":"2000-01-23T04:56:07.000+00:00","description":"description","definition":{"criteria":"CostThresholdExceeded","category":"Cost","type":"Budget"},"details":{"key":"details"},"modificationUsername":"modificationUsername","source":"Preset","statusModificationTime":"2000-01-23T04:56:07.000+00:00","status":"Active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/departments/{department_id}/providers/Microsoft.CostManagement/alerts/{alert_id}/updateStatus'.format(billing_account_id='billing_account_id_example', department_id='department_id_example', alert_id='alert_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_enrollment_account_alert_status(client):
    """Test case for alerts_update_enrollment_account_alert_status

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"costEntityId":"costEntityId","creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","scope":"scope","closeTime":"2000-01-23T04:56:07.000+00:00","description":"description","definition":{"criteria":"CostThresholdExceeded","category":"Cost","type":"Budget"},"details":{"key":"details"},"modificationUsername":"modificationUsername","source":"Preset","statusModificationTime":"2000-01-23T04:56:07.000+00:00","status":"Active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Billing/billingAccounts/{billing_account_id}/enrollmentAccounts/{enrollment_account_id}/providers/Microsoft.CostManagement/alerts/{alert_id}/updateStatus'.format(billing_account_id='billing_account_id_example', enrollment_account_id='enrollment_account_id_example', alert_id='alert_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_management_group_alert_status(client):
    """Test case for alerts_update_management_group_alert_status

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"costEntityId":"costEntityId","creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","scope":"scope","closeTime":"2000-01-23T04:56:07.000+00:00","description":"description","definition":{"criteria":"CostThresholdExceeded","category":"Cost","type":"Budget"},"details":{"key":"details"},"modificationUsername":"modificationUsername","source":"Preset","statusModificationTime":"2000-01-23T04:56:07.000+00:00","status":"Active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Management/managementGroups/{management_group_id}/providers/Microsoft.CostManagement/alerts/{alert_id}/UpdateStatus'.format(management_group_id='management_group_id_example', alert_id='alert_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_resource_group_name_alert_status(client):
    """Test case for alerts_update_resource_group_name_alert_status

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"costEntityId":"costEntityId","creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","scope":"scope","closeTime":"2000-01-23T04:56:07.000+00:00","description":"description","definition":{"criteria":"CostThresholdExceeded","category":"Cost","type":"Budget"},"details":{"key":"details"},"modificationUsername":"modificationUsername","source":"Preset","statusModificationTime":"2000-01-23T04:56:07.000+00:00","status":"Active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CostManagement/alerts/{alert_id}/updateStatus'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', alert_id='alert_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_alerts_update_subscription_alert_status(client):
    """Test case for alerts_update_subscription_alert_status

    
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"costEntityId":"costEntityId","creationTime":"2000-01-23T04:56:07.000+00:00","modificationTime":"2000-01-23T04:56:07.000+00:00","scope":"scope","closeTime":"2000-01-23T04:56:07.000+00:00","description":"description","definition":{"criteria":"CostThresholdExceeded","category":"Cost","type":"Budget"},"details":{"key":"details"},"modificationUsername":"modificationUsername","source":"Preset","statusModificationTime":"2000-01-23T04:56:07.000+00:00","status":"Active"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/alerts/{alert_id}/updateStatus'.format(subscription_id='subscription_id_example', alert_id='alert_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

