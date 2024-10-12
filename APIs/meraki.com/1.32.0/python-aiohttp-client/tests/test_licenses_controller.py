# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_organization_licenses_seats200_response import AssignOrganizationLicensesSeats200Response
from openapi_server.models.assign_organization_licenses_seats_request import AssignOrganizationLicensesSeatsRequest
from openapi_server.models.get_organization_licenses200_response_inner import GetOrganizationLicenses200ResponseInner
from openapi_server.models.get_organization_licensing_coterm_licenses200_response_inner import GetOrganizationLicensingCotermLicenses200ResponseInner
from openapi_server.models.move_organization_licenses200_response import MoveOrganizationLicenses200Response
from openapi_server.models.move_organization_licenses_request import MoveOrganizationLicensesRequest
from openapi_server.models.move_organization_licenses_seats200_response import MoveOrganizationLicensesSeats200Response
from openapi_server.models.move_organization_licenses_seats_request import MoveOrganizationLicensesSeatsRequest
from openapi_server.models.move_organization_licensing_coterm_licenses200_response import MoveOrganizationLicensingCotermLicenses200Response
from openapi_server.models.move_organization_licensing_coterm_licenses_request import MoveOrganizationLicensingCotermLicensesRequest
from openapi_server.models.renew_organization_licenses_seats_request import RenewOrganizationLicensesSeatsRequest
from openapi_server.models.update_organization_license_request import UpdateOrganizationLicenseRequest


pytestmark = pytest.mark.asyncio

async def test_assign_organization_licenses_seats_1(client):
    """Test case for assign_organization_licenses_seats_1

    Assign SM seats to a network
    """
    body = openapi_server.AssignOrganizationLicensesSeatsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/assignSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_license_1(client):
    """Test case for get_organization_license_1

    Display a license
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licenses/{license_id}'.format(organization_id='organization_id_example', license_id='license_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_licenses_1(client):
    """Test case for get_organization_licenses_1

    List the licenses for an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('networkId', 'network_id_example'),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licenses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_licenses_overview_1(client):
    """Test case for get_organization_licenses_overview_1

    Return an overview of the license state for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licenses/overview'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_licensing_coterm_licenses_2(client):
    """Test case for get_organization_licensing_coterm_licenses_2

    List the licenses in a coterm organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('invalidated', True),
                    ('expired', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/licensing/coterm/licenses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_organization_licenses_1(client):
    """Test case for move_organization_licenses_1

    Move licenses to another organization
    """
    body = openapi_server.MoveOrganizationLicensesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/move'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_organization_licenses_seats_1(client):
    """Test case for move_organization_licenses_seats_1

    Move SM seats to another organization
    """
    body = openapi_server.MoveOrganizationLicensesSeatsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/moveSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_organization_licensing_coterm_licenses_2(client):
    """Test case for move_organization_licensing_coterm_licenses_2

    Moves a license to a different organization (coterm only)
    """
    body = openapi_server.MoveOrganizationLicensingCotermLicensesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licensing/coterm/licenses/move'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_renew_organization_licenses_seats_1(client):
    """Test case for renew_organization_licenses_seats_1

    Renew SM seats of a license
    """
    body = openapi_server.RenewOrganizationLicensesSeatsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/licenses/renewSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_license_1(client):
    """Test case for update_organization_license_1

    Update a license
    """
    body = openapi_server.UpdateOrganizationLicenseRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/licenses/{license_id}'.format(organization_id='organization_id_example', license_id='license_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

