# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assays import Assays


pytestmark = pytest.mark.asyncio

async def test_get_assays_using_get(client):
    """Test case for get_assays_using_get

    Get ChEMBL assays
    """
    params = [('assayChemblId', ['assay_chembl_id_example']),
                    ('assayOrg', ['assay_org_example']),
                    ('assayType', ['assay_type_example']),
                    ('limit', 10),
                    ('page', 0),
                    ('targetChemblId', ['target_chembl_id_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/assays',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

