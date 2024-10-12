# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.column_dto import ColumnDTO
from openapi_server.models.filter_dto import FilterDTO
from openapi_server.models.filter_property_dto import FilterPropertyDTO
from openapi_server.models.local_settings_dto import LocalSettingsDTO
from openapi_server.models.order_dto import OrderDTO
from openapi_server.models.permissions_dto import PermissionsDTO
from openapi_server.models.settings_dto import SettingsDTO
from openapi_server.models.view_dto import ViewDTO
from openapi_server.models.view_details_dto import ViewDetailsDTO
from openapi_server.models.view_with_id_dto import ViewWithIdDTO
from openapi_server.models.views_brief_dto import ViewsBriefDTO


pytestmark = pytest.mark.asyncio

async def test_browse_csv(client):
    """Test case for browse_csv

    Searches for data (ie. customer, task, etc) and returns it in a CSV form.
    """
    params = [('viewId', 56),
                    ('separator', 'separator_example'),
                    ('secondarySeparator', 'secondary_separator_example'),
                    ('additionalOrder', 'additional_order_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/csv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_browse_json(client):
    """Test case for browse_json

    Searches for data (ie. customer, task, etc) and returns it in a tabular form.
    """
    params = [('viewId', 56),
                    ('page', 0),
                    ('additionalOrder', 'additional_order_example'),
                    ('useDeferredColumns', 'use_deferred_columns_example'),
                    ('maxRows', 0)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_create(client):
    """Test case for create

    Creates view for given class.
    """
    body = openapi_server.ViewDTO()
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/browser/views/for/{class_name}'.format(class_name='class_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    Removes a view.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/browser/views/{view_id}'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_column(client):
    """Test case for delete_column

    Deletes a single column from view.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/browser/views/{view_id}/columns/{column_name}'.format(view_id=56, column_name='column_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    Returns all view's information.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_column_settings(client):
    """Test case for get_column_settings

    Returns column's specific settings.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/columns/{column_name}/settings'.format(view_id=56, column_name='column_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_columns(client):
    """Test case for get_columns

    Returns columns defined in view.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/columns'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_current_view_details(client):
    """Test case for get_current_view_details

    Returns current view's detailed information, suitable for browser.
    """
    params = [('placeName', 'default')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/details/for/{class_name}'.format(class_name='class_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filter(client):
    """Test case for get_filter

    Returns view's filter.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/filter'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_local_settings(client):
    """Test case for get_local_settings

    Returns view's local settings (for current user).
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/settings/local'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_order(client):
    """Test case for get_order

    Returns view's order settings.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/order'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permissions(client):
    """Test case for get_permissions

    Returns view's permissions.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/permissions'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settings(client):
    """Test case for get_settings

    Returns view's settings.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/{view_id}/settings'.format(view_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_view_details(client):
    """Test case for get_view_details

    Returns view's detailed information, suitable for browser.
    """
    params = [('placeName', 'default')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/details/for/{class_name}/{view_id}'.format(class_name='class_name_example', view_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_views_brief(client):
    """Test case for get_views_brief

    Returns views' brief.
    """
    params = [('placeName', 'default')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/browser/views/for/{class_name}'.format(class_name='class_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_select_view_and_get_its_details(client):
    """Test case for select_view_and_get_its_details

    Selects given view as current and returns its detailed information, suitable for browser.
    """
    params = [('place name (denotes specific place in system with the table)', 'default')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/browser/views/details/for/{class_name}/{view_id}'.format(class_name='class_name_example', view_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update(client):
    """Test case for update

    Updates all view's information.
    """
    body = openapi_server.ViewDTO()
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_column_settings(client):
    """Test case for update_column_settings

    Updates column's specific settings.
    """
    body = /home-api/assets/examples/browsers/views/updateColumnSettings.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/columns/{column_name}/settings'.format(view_id=56, column_name='column_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update_columns(client):
    """Test case for update_columns

    Updates columns in view.
    """
    body = /home-api/assets/examples/browsers/views/updateColumns.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/columns'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update_filter(client):
    """Test case for update_filter

    Updates view's filter.
    """
    body = /home-api/assets/examples/browsers/views/updateFilter.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/filter'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_filter_property(client):
    """Test case for update_filter_property

    Updates view's filter property.
    """
    body = {"settings":"{}","settingsPresent":True,"name":"name","type":"type"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/filter/{filter_property}'.format(view_id=56, filter_property='filter_property_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_local_settings(client):
    """Test case for update_local_settings

    Updates view's local settings (for current user).
    """
    body = {"maxLinesInRow":6,"maxRows":1}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/settings/local'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update_order(client):
    """Test case for update_order

    Updates view's order settings.
    """
    body = /home-api/assets/examples/browsers/views/updateOrder.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/order'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_permissions(client):
    """Test case for update_permissions

    Updates view's permissions.
    """
    body = {"sharedGroups":[0,0]}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/permissions'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_settings(client):
    """Test case for update_settings

    Updates view's settings.
    """
    body = {"name":"name","local":{"maxLinesInRow":6,"maxRows":1}}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/browser/views/{view_id}/settings'.format(view_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

