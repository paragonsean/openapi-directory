# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provisioning_job_completion import ProvisioningJobCompletion
from openapi_server.models.provisioning_job_info import ProvisioningJobInfo


pytestmark = pytest.mark.asyncio

async def test_provisioningjobs_job_id_get(client):
    """Test case for provisioningjobs_job_id_get

    Detail of a provisioning job
    """
    params = [('job_id', 'job_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/provisioningjobs/{job_id}'.format(job_id2='job_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

