# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_licensing_coterm_licenses200_response_inner import GetOrganizationLicensingCotermLicenses200ResponseInner
from openapi_server.models.move_organization_licensing_coterm_licenses200_response import MoveOrganizationLicensingCotermLicenses200Response
from openapi_server.models.move_organization_licensing_coterm_licenses_request import MoveOrganizationLicensingCotermLicensesRequest


pytestmark = pytest.mark.asyncio

async def test_get_organization_licensing_coterm_licenses(client):
    """Test case for get_organization_licensing_coterm_licenses

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

async def test_move_organization_licensing_coterm_licenses(client):
    """Test case for move_organization_licensing_coterm_licenses

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

