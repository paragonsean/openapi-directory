# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_organization_licenses_seats_request import AssignOrganizationLicensesSeatsRequest
from openapi_server.models.move_organization_licenses_seats_request import MoveOrganizationLicensesSeatsRequest
from openapi_server.models.renew_organization_licenses_seats_request import RenewOrganizationLicensesSeatsRequest


pytestmark = pytest.mark.asyncio

async def test_assign_organization_licenses_seats(client):
    """Test case for assign_organization_licenses_seats

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
        path='/api/v0/organizations/{organization_id}/licenses/assignSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_license(client):
    """Test case for get_organization_license

    Display a license
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/licenses/{license_id}'.format(organization_id='organization_id_example', license_id='license_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_license_state(client):
    """Test case for get_organization_license_state

    Return an overview of the license state for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/licenseState'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_licenses(client):
    """Test case for get_organization_licenses

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
        path='/api/v0/organizations/{organization_id}/licenses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_organization_licenses_seats(client):
    """Test case for move_organization_licenses_seats

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
        path='/api/v0/organizations/{organization_id}/licenses/moveSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_renew_organization_licenses_seats(client):
    """Test case for renew_organization_licenses_seats

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
        path='/api/v0/organizations/{organization_id}/licenses/renewSeats'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

