# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_document(client):
    """Test case for document

    Returns Document information
    """
    params = [('documentId', 'EPA-HQ-OAR-2011-0028-0108'),
                    ('federalRegisterNumber', 'federal_register_number_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/regulations/v3/document.{response_format}'.format(response_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents(client):
    """Test case for documents

    Search for Documents
    """
    params = [('countsOnly', 56),
                    ('encoded', 56),
                    ('s', 's_example'),
                    ('dct', 'dct_example'),
                    ('dktid', 'dktid_example'),
                    ('dkt', 'dkt_example'),
                    ('cp', 'cp_example'),
                    ('a', 'a_example'),
                    ('rpp', 'rpp_example'),
                    ('po', 56),
                    ('cs', 56),
                    ('np', 56),
                    ('cmsd', '2013-10-20'),
                    ('cmd', '2013-10-20'),
                    ('crd', '2013-10-20'),
                    ('rd', '2013-10-20'),
                    ('pd', '2013-10-20'),
                    ('cat', 'cat_example'),
                    ('sb', 'sb_example'),
                    ('so', 'so_example'),
                    ('dktst', 'dktst_example'),
                    ('dktst2', 'dktst2_example'),
                    ('docst', 'docst_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/regulations/v3/documents.{response_format}'.format(response_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

