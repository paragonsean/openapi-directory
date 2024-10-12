# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_invoice_model import CreateInvoiceModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.invoice_output_model import InvoiceOutputModel
from openapi_server.models.invoice_row_output_model import InvoiceRowOutputModel
from openapi_server.models.invoice_settings_output_model import InvoiceSettingsOutputModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.project_invoice_settings_input_model import ProjectInvoiceSettingsInputModel
from openapi_server.models.project_invoice_settings_output_model import ProjectInvoiceSettingsOutputModel


pytestmark = pytest.mark.asyncio

async def test_invoice_rows_patch_invoice_row(client):
    """Test case for invoice_rows_patch_invoice_row

    Update (Patch) a invoice row or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/invoicerows/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_settings_patch_invoice_settings(client):
    """Test case for invoice_settings_patch_invoice_settings

    Update (Patch) invoice setting
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/invoicesettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_patch_invoice(client):
    """Test case for invoices_patch_invoice

    Update (Patch) an invoice or a part of it
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/invoices/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_post_invoice_creation(client):
    """Test case for invoices_post_invoice_creation

    Add an invoice to project(s)
    """
    body = {"date":"2000-01-23","projects":[{"guid":"guid"},{"guid":"guid"}],"billingCustomerGuid":"billingCustomerGuid","groupProjects":True,"invoiceStatusGuid":"invoiceStatusGuid"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/invoices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_patch_project_invoice_settings(client):
    """Test case for project_invoice_settings_patch_project_invoice_settings

    Update (Patch) project invoice settings.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projectinvoicesettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_post_project_invoice_settings(client):
    """Test case for project_invoice_settings_post_project_invoice_settings

    Create a new project invoice settings.
    """
    body = {"projectFeeDescriptionFormat":"projectFeeDescriptionFormat","showReferenceNumber":True,"showLogoAndTitle":True,"showAttachmentPriceExcludingValueAddedTax":True,"projectTravelExpensePrimaryGroupBy":"projectTravelExpensePrimaryGroupBy","showQuantity":True,"project":{"guid":"guid"},"htmlText2":{"tagContext":"tagContext","value":"value","allowTags":True},"htmlText1":{"tagContext":"tagContext","value":"value","allowTags":True},"showFooter":True,"freeText1":{"tagContext":"tagContext","value":"value","allowTags":True},"freeText2":{"tagContext":"tagContext","value":"value","allowTags":True},"projectFeeGrouping":"OneByOne","projectTravelExpenseSecondaryGroupBy":"projectTravelExpenseSecondaryGroupBy","showAttachmentUnitPrice":True,"workHourPrimaryGroupBy":"workHourPrimaryGroupBy","showAttachmentValueAddedTax":True,"showPriceExcludingValueAddedTax":True,"showAttachmentUnit":True,"showUnitPrice":True,"workHourDescriptionFormat":"workHourDescriptionFormat","projectFeeSecondaryGroupBy":"projectFeeSecondaryGroupBy","workHourSecondaryGroupBy":"workHourSecondaryGroupBy","showUnit":True,"showCategories":True,"projectTravelExpenseDescriptionFormat":"projectTravelExpenseDescriptionFormat","projectFeePrimaryGroupBy":"projectFeePrimaryGroupBy","showValueAddedTax":True,"style":"BlackAndWhite"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projectinvoicesettings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

