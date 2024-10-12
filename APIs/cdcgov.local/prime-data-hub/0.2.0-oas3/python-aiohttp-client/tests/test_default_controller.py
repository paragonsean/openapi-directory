# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organization import Organization
from openapi_server.models.receiver import Receiver
from openapi_server.models.report import Report
from openapi_server.models.sender import Sender


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/csv not supported by Connexion")
async def test_reports_post(client):
    """Test case for reports_post

    Post a report to the data hub
    """
    body = header1, header2
value1, value2
    params = [('client', 'simple_report'),
                    ('option', 'ValidatePayload'),
                    ('default', ['processing_mode_code%3AD']),
                    ('routeTo', ['fl-phd.elr,fl-phd.download'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/csv',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/reports',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_get(client):
    """Test case for settings_organizations_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/organizations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_head(client):
    """Test case for settings_organizations_head

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/settings/organizations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_delete(client):
    """Test case for settings_organizations_organization_name_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/settings/organizations/{organization_name}'.format(organization_name='organization_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_get(client):
    """Test case for settings_organizations_organization_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/organizations/{organization_name}'.format(organization_name='organization_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_put(client):
    """Test case for settings_organizations_organization_name_put

    
    """
    body = {"meta":{"createdAt":"createdAt","createdBy":"jj@phd.gov","version":11},"jurisdiction":"National","name":"az-phd","description":"Arizona PHD","stateCode":"AZ","countyName":"Pima"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/settings/organizations/{organization_name}'.format(organization_name='organization_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_receivers_get(client):
    """Test case for settings_organizations_organization_name_receivers_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/organizations/{organization_name}/receivers'.format(organization_name='az-phd'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_receivers_receiver_name_delete(client):
    """Test case for settings_organizations_organization_name_receivers_receiver_name_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/settings/organizations/{organization_name}/receivers/{receiver_name}'.format(organization_name='az-phd', receiver_name='elr'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_receivers_receiver_name_get(client):
    """Test case for settings_organizations_organization_name_receivers_receiver_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/organizations/{organization_name}/receivers/{receiver_name}'.format(organization_name='az-phd', receiver_name='elr'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_receivers_receiver_name_put(client):
    """Test case for settings_organizations_organization_name_receivers_receiver_name_put

    
    """
    body = {"organizationName":"az-phd","meta":{"createdAt":"createdAt","createdBy":"jj@phd.gov","version":11},"timing":{"dailyAt":0.8008281904610115,"frequency":"REAL_TIME"},"translations":[{"nameFormat":"standard","receivingOrganization":"receivingOrganization","format":"CSV","transport":{"port":22,"filePath":"/in/test","host":"sftp.phd.gov","type":"SFTP"},"schemaName":"schemaName","type":"CUSTOM"},{"nameFormat":"standard","receivingOrganization":"receivingOrganization","format":"CSV","transport":{"port":22,"filePath":"/in/test","host":"sftp.phd.gov","type":"SFTP"},"schemaName":"schemaName","type":"CUSTOM"}],"jurisdictionalFilters":[{"matchFields":"FACILITY_OR_PATIENT_ADDRESS","doesNotMatch":False,"matchValues":["matchValues","matchValues"]},{"matchFields":"FACILITY_OR_PATIENT_ADDRESS","doesNotMatch":False,"matchValues":["matchValues","matchValues"]}],"name":"az-phd.elr","description":"Arizona PHD ELR feed","topic":"covid-19"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/settings/organizations/{organization_name}/receivers/{receiver_name}'.format(organization_name='az-phd', receiver_name='elr'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_senders_get(client):
    """Test case for settings_organizations_organization_name_senders_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/organizations/{organization_name}/senders'.format(organization_name='az-phd'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_senders_sender_name_delete(client):
    """Test case for settings_organizations_organization_name_senders_sender_name_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/settings/organizations/{organization_name}/senders/{sender_name}'.format(organization_name='az-phd', sender_name='default'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_senders_sender_name_get(client):
    """Test case for settings_organizations_organization_name_senders_sender_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/organizations/{organization_name}/senders/{sender_name}'.format(organization_name='az-phd', sender_name='default'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_settings_organizations_organization_name_senders_sender_name_put(client):
    """Test case for settings_organizations_organization_name_senders_sender_name_put

    
    """
    body = {"schema":"az-phd-covid-19","organizationName":"az-phd","meta":{"createdAt":"createdAt","createdBy":"jj@phd.gov","version":11},"format":"CSV","name":"simple_report.default","description":"description","topic":"covid-19"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/settings/organizations/{organization_name}/senders/{sender_name}'.format(organization_name='az-phd', sender_name='default'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

