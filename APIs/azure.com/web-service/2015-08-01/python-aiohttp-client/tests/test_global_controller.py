# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_collection import CertificateCollection
from openapi_server.models.classic_mobile_service_collection import ClassicMobileServiceCollection
from openapi_server.models.geo_region_collection import GeoRegionCollection
from openapi_server.models.hosting_environment_collection import HostingEnvironmentCollection
from openapi_server.models.managed_hosting_environment_collection import ManagedHostingEnvironmentCollection
from openapi_server.models.resource_name_availability import ResourceNameAvailability
from openapi_server.models.resource_name_availability_request import ResourceNameAvailabilityRequest
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_check_name_availability(client):
    """Test case for global_check_name_availability

    Check if resource name is available
    """
    request = {"name":"name","type":"type","isFqdn":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/checknameavailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_all_certificates(client):
    """Test case for global_get_all_certificates

    Get all certificates for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/certificates'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_all_classic_mobile_services(client):
    """Test case for global_get_all_classic_mobile_services

    Gets all mobile services for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/classicMobileServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_all_hosting_environments(client):
    """Test case for global_get_all_hosting_environments

    Gets all hostingEnvironments (App Service Environment) for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/hostingEnvironments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_all_managed_hosting_environments(client):
    """Test case for global_get_all_managed_hosting_environments

    Gets all managed hosting environments for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/managedHostingEnvironments'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_all_server_farms(client):
    """Test case for global_get_all_server_farms

    Gets all App Service Plans for a subscription
    """
    params = [('detailed', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/serverfarms'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_all_sites(client):
    """Test case for global_get_all_sites

    Gets all Web Apps for a subscription
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/sites'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_subscription_geo_regions(client):
    """Test case for global_get_subscription_geo_regions

    Gets list of available geo regions
    """
    params = [('sku', 'sku_example'),
                    ('linuxWorkersEnabled', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/geoRegions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_get_subscription_publishing_credentials(client):
    """Test case for global_get_subscription_publishing_credentials

    Gets publishing credentials for the subscription owner
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/publishingCredentials'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_is_hosting_environment_name_available(client):
    """Test case for global_is_hosting_environment_name_available

    Whether hosting environment name is available
    """
    params = [('name', 'name_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/ishostingenvironmentnameavailable'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_is_hosting_environment_with_legacy_name_available(client):
    """Test case for global_is_hosting_environment_with_legacy_name_available

    Whether hosting environment name is available
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/ishostingenvironmentnameavailable/{name}'.format(name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_global_list_premier_add_on_offers(client):
    """Test case for global_list_premier_add_on_offers

    List premier add on offers
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/premieraddonoffers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_update_subscription_publishing_credentials(client):
    """Test case for global_update_subscription_publishing_credentials

    Updates publishing credentials for the subscription owner
    """
    request_message = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/publishingCredentials'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=request_message,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

