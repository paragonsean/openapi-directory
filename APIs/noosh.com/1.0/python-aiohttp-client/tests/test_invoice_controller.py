# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.file_list_response_vo import FileListResponseVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.invoice_detail_list_expand_vo import InvoiceDetailListExpandVO
from openapi_server.models.invoice_expand_vo import InvoiceExpandVO


pytestmark = pytest.mark.asyncio

async def test_get_invoice(client):
    """Test case for get_invoice

    List a specific invoice of project Level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice_files(client):
    """Test case for get_invoice_files

    List files of invoice Level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/{invoice_id}/files'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoices(client):
    """Test case for get_invoices

    List invoices by a specific order
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/invoices/orders/{order_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

