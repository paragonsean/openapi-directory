# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_meter_collection import BillingMeterCollection
from openapi_server.models.csm_move_resource_envelope import CsmMoveResourceEnvelope
from openapi_server.models.deployment_locations import DeploymentLocations
from openapi_server.models.geo_region_collection import GeoRegionCollection
from openapi_server.models.get_publishing_user200_response import GetPublishingUser200Response
from openapi_server.models.get_publishing_user_default_response import GetPublishingUserDefaultResponse
from openapi_server.models.list_site_identifiers_assigned_to_host_name200_response import ListSiteIdentifiersAssignedToHostName200Response
from openapi_server.models.list_site_identifiers_assigned_to_host_name_request import ListSiteIdentifiersAssignedToHostNameRequest
from openapi_server.models.premier_add_on_offer_collection import PremierAddOnOfferCollection
from openapi_server.models.resource_name_availability import ResourceNameAvailability
from openapi_server.models.resource_name_availability_request import ResourceNameAvailabilityRequest
from openapi_server.models.sku_infos import SkuInfos
from openapi_server.models.source_control import SourceControl
from openapi_server.models.source_control_collection import SourceControlCollection
from openapi_server.models.validate_request import ValidateRequest
from openapi_server.models.validate_response import ValidateResponse
from openapi_server.models.vnet_parameters import VnetParameters
from openapi_server.models.vnet_validation_failure_details import VnetValidationFailureDetails


pytestmark = pytest.mark.asyncio

async def test_check_name_availability(client):
    """Test case for check_name_availability

    Check if a resource name is available.
    """
    request = {"name":"name","type":"Site","isFqdn":True}
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

async def test_get_publishing_user(client):
    """Test case for get_publishing_user

    Gets publishing user
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/publishingUsers/web',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_control(client):
    """Test case for get_source_control

    Gets source control token
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/sourcecontrols/{source_control_type}'.format(source_control_type='source_control_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_deployment_locations(client):
    """Test case for get_subscription_deployment_locations

    Gets list of available geo regions plus ministamps
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/deploymentLocations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_billing_meters(client):
    """Test case for list_billing_meters

    Gets a list of meters for a given location.
    """
    params = [('billingLocation', 'billing_location_example'),
                    ('osType', 'os_type_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/billingMeters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_geo_regions(client):
    """Test case for list_geo_regions

    Get a list of available geographical regions.
    """
    params = [('sku', 'sku_example'),
                    ('linuxWorkersEnabled', True),
                    ('xenonWorkersEnabled', True),
                    ('linuxDynamicWorkersEnabled', True),
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

async def test_list_premier_add_on_offers(client):
    """Test case for list_premier_add_on_offers

    List all premier add-on offers.
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

async def test_list_site_identifiers_assigned_to_host_name(client):
    """Test case for list_site_identifiers_assigned_to_host_name

    List all apps that are assigned to a hostname.
    """
    name_identifier = openapi_server.ListSiteIdentifiersAssignedToHostNameRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/listSitesAssignedToHostName'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=name_identifier,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_skus(client):
    """Test case for list_skus

    List all SKUs.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/skus'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_source_controls(client):
    """Test case for list_source_controls

    Gets the source controls available for Azure websites.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/sourcecontrols',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move(client):
    """Test case for move

    Move resources between resource groups.
    """
    move_resource_envelope = {"targetResourceGroup":"targetResourceGroup","resources":["resources","resources"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/moveResources'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=move_resource_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_publishing_user(client):
    """Test case for update_publishing_user

    Updates publishing user
    """
    user_details = openapi_server.GetPublishingUser200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Web/publishingUsers/web',
        headers=headers,
        json=user_details,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_source_control(client):
    """Test case for update_source_control

    Updates source control token
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
        path='/providers/Microsoft.Web/sourcecontrols/{source_control_type}'.format(source_control_type='source_control_type_example'),
        headers=headers,
        json=request_message,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate(client):
    """Test case for validate

    Validate if a resource can be created.
    """
    validate_request = {"name":"name","location":"location","type":"ServerFarm","properties":{"isSpot":True,"containerImagePlatform":"containerImagePlatform","isXenon":True,"containerRegistryBaseUrl":"containerRegistryBaseUrl","needLinuxWorkers":True,"containerImageTag":"containerImageTag","capacity":1,"containerRegistryUsername":"containerRegistryUsername","serverFarmId":"serverFarmId","skuName":"skuName","containerImageRepository":"containerImageRepository","containerRegistryPassword":"containerRegistryPassword","hostingEnvironment":"hostingEnvironment"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/validate'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=validate_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_move(client):
    """Test case for validate_move

    Validate whether a resource can be moved.
    """
    move_resource_envelope = {"targetResourceGroup":"targetResourceGroup","resources":["resources","resources"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/validateMoveResources'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=move_resource_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_hosting_environment_vnet(client):
    """Test case for verify_hosting_environment_vnet

    Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.
    """
    parameters = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/verifyHostingEnvironmentVnet'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

