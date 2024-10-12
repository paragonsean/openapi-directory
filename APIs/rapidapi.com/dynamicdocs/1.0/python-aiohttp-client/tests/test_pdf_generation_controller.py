# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_compile(client):
    """Test case for compile

    Compile New Document PDF
    """
    body = {"amount":"ZAR 100 000","client":{"address":"xx Long Street","company":"ABC Company Pty Ltd","firstName":"John","lastName":"Smith","location":"Cape Town, South Africa"},"consultant":{"address":"xx Rivonia Road","company":"XYZ Company Pty Ltd","firstName":"Kobus","lastName":"van der Merwe","location":"Sandton, South Africa"},"effectiveDate":"1 February 2021","servicesDescription":"perform analysis on the company's clients and identify existing market segments"}
    params = [('doc-url-expires-in', 3600),
                    ('latex-compiler', 'latex_compiler_example'),
                    ('latex-runs ', 56),
                    ('main-file-name', 'inputFile.tex'),
                    ('doc-file-name', 'brilliantDocument')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'Adv-Security-Token': 'special-key',
        'X-RapidAPI-Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/templates/{template_token}/compile'.format(template_token='7a582350acb835ed'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

