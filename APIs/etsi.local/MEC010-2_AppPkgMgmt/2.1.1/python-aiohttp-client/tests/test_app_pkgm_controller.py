# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app_d import AppD
from openapi_server.models.app_pkg_info import AppPkgInfo
from openapi_server.models.app_pkg_info_modifications import AppPkgInfoModifications
from openapi_server.models.app_pkg_subscription import AppPkgSubscription
from openapi_server.models.app_pkg_subscription_info import AppPkgSubscriptionInfo
from openapi_server.models.app_pkg_subscription_link_list import AppPkgSubscriptionLinkList
from openapi_server.models.create_app_pkg import CreateAppPkg
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_app_dget(client):
    """Test case for app_dget

    Reads the content of the AppD of on-boarded individual application package resources.
    """
    params = [('filter', 'filter_example'),
                    ('all_fields', 'all_fields_example'),
                    ('fields', 'fields_example'),
                    ('exclude_fields', 'exclude_fields_example'),
                    ('exclude_default', 'exclude_default_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/onboarded_app_packages/{app_did}/appd'.format(app_did='app_did_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_did_get(client):
    """Test case for app_did_get

    Fetch the onboarded application package content identified by appPkgId or appDId.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/onboarded_app_packages/{app_did}/package_content'.format(app_did='app_did_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/zip not supported by Connexion")
async def test_app_did_put(client):
    """Test case for app_did_put

    Uploads the content of application package.
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/zip',
    }
    response = await client.request(
        method='PUT',
        path='/onboarded_app_packages/{app_did}/package_content'.format(app_did='app_did_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_package_delete(client):
    """Test case for app_package_delete

    Deletes an individual application package resources
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/app_packages/{app_pkg_id}'.format(app_pkg_id='app_pkg_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_package_get(client):
    """Test case for app_package_get

    Queries the information related to individual application package resources
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app_packages/{app_pkg_id}'.format(app_pkg_id='app_pkg_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_package_patch(client):
    """Test case for app_package_patch

    Updates the operational state of an individual application package resource
    """
    body = {"operationState":"DISABLED"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/app_packages/{app_pkg_id}'.format(app_pkg_id='app_pkg_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_packages_get(client):
    """Test case for app_packages_get

    Queries information relating to on-boarded application packages in the MEO
    """
    params = [('filter', 'filter_example'),
                    ('all_fields', 'all_fields_example'),
                    ('fields', 'fields_example'),
                    ('exclude_fields', 'exclude_fields_example'),
                    ('exclude_default', 'exclude_default_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app_packages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_packages_post(client):
    """Test case for app_packages_post

    Create a resource for on-boarding an application package to a MEO
    """
    body = {"appPkgPath":"appPkgPath","appPkgName":"appPkgName","checksum":{"hash":"hash","algorithm":"algorithm"},"appProvider":"appProvider","appPkgVersion":"appPkgVersion","userDefinedData":{"key":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/app_packages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_pkg_get(client):
    """Test case for app_pkg_get

    Fetch the onboarded application package content identified by appPkgId or appDId.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app_packages/{app_pkg_id}/package_content'.format(app_pkg_id='app_pkg_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_app_pkg_id_get(client):
    """Test case for app_pkg_id_get

    Reads the content of the AppD of on-boarded individual application package resources.
    """
    params = [('filter', 'filter_example'),
                    ('all_fields', 'all_fields_example'),
                    ('fields', 'fields_example'),
                    ('exclude_fields', 'exclude_fields_example'),
                    ('exclude_default', 'exclude_default_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/app_packages/{app_pkg_id}/appd'.format(app_pkg_id='app_pkg_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/zip not supported by Connexion")
async def test_app_pkg_put(client):
    """Test case for app_pkg_put

    Uploads the content of application package.
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/zip',
    }
    response = await client.request(
        method='PUT',
        path='/app_packages/{app_pkg_id}/package_content'.format(app_pkg_id='app_pkg_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individual_subscription_delete(client):
    """Test case for individual_subscription_delete

    Deletes the individual subscription to notifications about application package changes in MEO.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_individual_subscription_get(client):
    """Test case for individual_subscription_get

    Used to represent an individual subscription to notifications about application package changes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_get(client):
    """Test case for subscriptions_get

    used to retrieve the information of subscriptions to individual application package resource in MEO
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_post(client):
    """Test case for subscriptions_post

    Subscribe to notifications about on-boarding an application package
    """
    body = {"subsctiptionType":"AppPackageOnBoarding","callbackUri":"https://openapi-generator.tech","appPkgFilter":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

