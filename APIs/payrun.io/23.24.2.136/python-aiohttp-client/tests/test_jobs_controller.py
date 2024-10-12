# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_job_instruction import BatchJobInstruction
from openapi_server.models.cis_job_instruction_base import CisJobInstructionBase
from openapi_server.models.dps_job_instruction import DpsJobInstruction
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.job_info import JobInfo
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_run_job_instruction import PayRunJobInstruction
from openapi_server.models.rti_job_instruction import RtiJobInstruction
from openapi_server.models.third_party_job_instruction import ThirdPartyJobInstruction


pytestmark = pytest.mark.asyncio

async def test_delete_batch_job(client):
    """Test case for delete_batch_job

    Delete the Batch job
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Jobs/Batch/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_job(client):
    """Test case for delete_cis_job

    Delete the CIS job
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Jobs/Cis/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_dps_job(client):
    """Test case for delete_dps_job

    Delete the DPS job
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Jobs/Dps/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pay_run_job(client):
    """Test case for delete_pay_run_job

    Delete the pay run job
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Jobs/PayRuns/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_rti_job(client):
    """Test case for delete_rti_job

    Delete the RTI job
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Jobs/Rti/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_third_party_job(client):
    """Test case for delete_third_party_job

    Delete the Third Party job
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Jobs/ThirdParty/{job_id}'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_job_info(client):
    """Test case for get_batch_job_info

    Get the Batch job information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Batch/{job_id}/Info'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_job_progress(client):
    """Test case for get_batch_job_progress

    Get the Batch job progress
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Batch/{job_id}/Progress'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_job_status(client):
    """Test case for get_batch_job_status

    Get the Batch job status
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Batch/{job_id}/Status'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_jobs(client):
    """Test case for get_batch_jobs

    Get all Batch jobs
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Batch',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_job_info(client):
    """Test case for get_cis_job_info

    Get the CIS job information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Cis/{job_id}/Info'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_job_progress(client):
    """Test case for get_cis_job_progress

    Get the CIS job progress
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Cis/{job_id}/Progress'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_job_status(client):
    """Test case for get_cis_job_status

    Get the CIS job status
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Cis/{job_id}/Status'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_jobs(client):
    """Test case for get_cis_jobs

    Get all CIS jobs
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Cis',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_job_info(client):
    """Test case for get_dps_job_info

    Get the DPS job information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Dps/{job_id}/Info'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_job_progress(client):
    """Test case for get_dps_job_progress

    Get the DPS job progress
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Dps/{job_id}/Progress'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_job_status(client):
    """Test case for get_dps_job_status

    Get the DPS job status
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Dps/{job_id}/Status'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_jobs(client):
    """Test case for get_dps_jobs

    Get all DPS jobs
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Dps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_jobs(client):
    """Test case for get_employer_jobs

    Gets all jobs relating to the employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Employer/{employer_id}'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_run_job_info(client):
    """Test case for get_pay_run_job_info

    Get the pay run job information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/PayRuns/{job_id}/Info'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_run_job_progress(client):
    """Test case for get_pay_run_job_progress

    Get the pay run job progress
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/PayRuns/{job_id}/Progress'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_run_job_status(client):
    """Test case for get_pay_run_job_status

    Get the pay run job status
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/PayRuns/{job_id}/Status'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_run_jobs(client):
    """Test case for get_pay_run_jobs

    Get all PayRun jobs
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/PayRuns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_job_info(client):
    """Test case for get_rti_job_info

    Get the RTI job information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Rti/{job_id}/Info'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_job_progress(client):
    """Test case for get_rti_job_progress

    Get the RTI job progress
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Rti/{job_id}/Progress'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_job_status(client):
    """Test case for get_rti_job_status

    Get the RTI job status
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Rti/{job_id}/Status'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_jobs(client):
    """Test case for get_rti_jobs

    Get all RTI jobs
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/Rti',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_third_party_job_info(client):
    """Test case for get_third_party_job_info

    Get the Third Party job information
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/ThirdParty/{job_id}/Info'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_third_party_job_progress(client):
    """Test case for get_third_party_job_progress

    Get the Third Party job progress
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/ThirdParty/{job_id}/Progress'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_third_party_job_status(client):
    """Test case for get_third_party_job_status

    Get the Third Party job status
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/ThirdParty/{job_id}/Status'.format(job_id='job_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_third_party_jobs(client):
    """Test case for get_third_party_jobs

    Get all Third Party jobs
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Jobs/ThirdParty',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_batch_job(client):
    """Test case for post_new_batch_job

    Create new Batch job
    """
    body = {"BatchJobInstruction":{"ValidateOnly":True,"Instructions":{"DELETE":[{"@Href":"@Href"},{"@Href":"@Href"}]},"HoldingDate":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Jobs/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_cis_job(client):
    """Test case for post_new_cis_job

    Create new CIS job
    """
    body = {"CisJobInstructionBase":{"Employer":{"@title":"@title","@rel":"@rel","@href":"@href"},"SubContractors":{"SubContractor":[{"@title":"@title","@rel":"@rel","@href":"@href"},{"@title":"@title","@rel":"@rel","@href":"@href"}]},"HoldingDate":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Jobs/Cis',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_dps_job(client):
    """Test case for post_new_dps_job

    Create new DPS job
    """
    body = {"DpsJobInstruction":{"MessagesToProcess":{"Message":[{"@title":"@title","@rel":"@rel","@href":"@href"},{"@title":"@title","@rel":"@rel","@href":"@href"}]},"Retrieve":True,"Apply":True,"Employer":{"@title":"@title","@rel":"@rel","@href":"@href"},"MessageTypes":{"Type":["",""]},"FromDate":"2000-01-23","HoldingDate":"2000-01-23T04:56:07.000+00:00"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Jobs/Dps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_pay_run_job(client):
    """Test case for post_new_pay_run_job

    Create new PayRun job
    """
    body = {"PayRunJobInstruction":{"StartDate":"2000-01-23","PaymentDate":"2000-01-23","Employees":{"Employee":[{"@title":"@title","@rel":"@rel","@href":"@href"},{"@title":"@title","@rel":"@rel","@href":"@href"}]},"PaySchedule":{"@title":"@title","@rel":"@rel","@href":"@href"},"HoldingDate":"2000-01-23T04:56:07.000+00:00","EndDate":"2000-01-23","IsSupplementary":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Jobs/PayRuns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_rti_job(client):
    """Test case for post_new_rti_job

    Create new RTI job
    """
    body = {"RtiJobInstruction":{"TaxMonth":6,"RtiType":"RtiType","Transmit":True,"PaymentDate":"2000-01-23","Employer":{"@title":"@title","@rel":"@rel","@href":"@href"},"RtiTransaction":{"@title":"@title","@rel":"@rel","@href":"@href"},"LateReason":"A","PeriodOfInactivityFrom":"2000-01-23","Timestamp":"2000-01-23T04:56:07.000+00:00","PeriodOfInactivityTo":"2000-01-23","EarlierTaxYear":0,"Generate":True,"PaySchedule":{"@title":"@title","@rel":"@rel","@href":"@href"},"FinalSubmissionForYear":True,"NoPaymentForPeriodFrom":"2000-01-23","HoldingDate":"2000-01-23T04:56:07.000+00:00","SchemeCeased":"2000-01-23","TaxYear":1,"NoPaymentForPeriodTo":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Jobs/Rti',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_third_party_job(client):
    """Test case for post_new_third_party_job

    Create new Third Party job
    """
    body = {"ThirdPartyJobInstruction":{"InstructionType":"InstructionType","MetaData":"{}","PayLoad":"PayLoad","HoldingDate":"2000-01-23T04:56:07.000+00:00","EmployerHref":"EmployerHref"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Jobs/ThirdParty',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

