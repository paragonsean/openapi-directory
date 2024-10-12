# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.landlord_accounting_model import LandlordAccountingModel
from openapi_server.models.landlord_crm_entry import LandlordCrmEntry
from openapi_server.models.landlord_maintenance_model import LandlordMaintenanceModel
from openapi_server.models.landlord_profit_loss_model import LandlordProfitLossModel
from openapi_server.models.landlord_rent_arrears_model import LandlordRentArrearsModel
from openapi_server.models.landlord_settings_model import LandlordSettingsModel
from openapi_server.models.landlord_summary_model import LandlordSummaryModel
from openapi_server.models.landlord_tenancy_model import LandlordTenancyModel


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_create_maintenance_preference(client):
    """Test case for landlord_controller_create_maintenance_preference

    Post tenancy maintenance preferences:-
    """
    params = [('token', 'token_example'),
                    ('tenancyID', 'tenancy_id_example'),
                    ('name', 'name_example'),
                    ('notes', 'notes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/customer/{short_name}/landlord/tenancy/maintenance/preference'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_accounts(client):
    """Test case for landlord_controller_get_accounts

    Get the accounting details for the landlord.
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/accounting'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_document(client):
    """Test case for landlord_controller_get_document

    Download a Document
    """
    params = [('token', 'token_example'),
                    ('ID', 'id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/document'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_invetory_report(client):
    """Test case for landlord_controller_get_invetory_report

    Generate a Inventory PDF for a tenancy
    """
    params = [('token', 'token_example'),
                    ('tenancyID', 'tenancy_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/inventory'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_invoice(client):
    """Test case for landlord_controller_get_invoice

    Get an invoice pdf belonging to the landlord.
    """
    params = [('token', 'token_example'),
                    ('invoiceID', 'invoice_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/invoice'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_landlord_crm_entries(client):
    """Test case for landlord_controller_get_landlord_crm_entries

    Retrieve landlord's CRM ID
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/landlordcrmentries'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_maintenance_jobs(client):
    """Test case for landlord_controller_get_maintenance_jobs

    Get Active maintenance jobs.
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/maintenance'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_profit_loss_report(client):
    """Test case for landlord_controller_get_profit_loss_report

    Generate a Profit and Loss Report
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/profitloss'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_rent_arrears(client):
    """Test case for landlord_controller_get_rent_arrears

    Rent Arrears
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/rentarrears'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_sas_report(client):
    """Test case for landlord_controller_get_sas_report

    Generate a Self Assessment Tax Report
    """
    params = [('token', 'token_example'),
                    ('yearEnd', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/sas'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_settings(client):
    """Test case for landlord_controller_get_settings

    Get contact details of all linked landlords.
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/settings'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_summary_details(client):
    """Test case for landlord_controller_get_summary_details

    Get the summary details for the landlord.
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/summary'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_tenancy(client):
    """Test case for landlord_controller_get_tenancy

    Get tenancy details.
    """
    params = [('token', 'token_example'),
                    ('tenancyID', 'tenancy_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/tenancy'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_landlord_controller_get_tenancy_agreement_report(client):
    """Test case for landlord_controller_get_tenancy_agreement_report

    Generate a Tenancy Agreement Copy (PDF)
    """
    params = [('token', 'token_example'),
                    ('tenancyID', 'tenancy_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/customer/{short_name}/landlord/tenancyagreement'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

