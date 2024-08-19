# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activities import Activities


pytestmark = pytest.mark.asyncio

async def test_get_activities_using_get(client):
    """Test case for get_activities_using_get

    Get ChEMBL activities
    """
    params = [('assayChemblId', ['assay_chembl_id_example']),
                    ('limit', 10),
                    ('moleculeChemblId', ['molecule_chembl_id_example']),
                    ('page', 0),
                    ('pchemblValue', 3.4),
                    ('targetChemblId', ['target_chembl_id_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Tools/crossbar/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

