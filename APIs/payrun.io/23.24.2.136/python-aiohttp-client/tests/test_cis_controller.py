# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cis_instruction import CisInstruction
from openapi_server.models.cis_line import CisLine
from openapi_server.models.cis_line_type import CisLineType
from openapi_server.models.cis_transaction import CisTransaction
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_delete_cis_instruction(client):
    """Test case for delete_cis_instruction

    Delete a CIS instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_instruction_tag_0(client):
    """Test case for delete_cis_instruction_tag_0

    Delete CIS instruction tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_line(client):
    """Test case for delete_cis_line

    Delete a CIS line
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLine/{cis_line_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_line_id='cis_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_line_tag_0(client):
    """Test case for delete_cis_line_tag_0

    Delete CIS line tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLine/{cis_line_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_line_id='cis_line_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_line_type(client):
    """Test case for delete_cis_line_type

    Delete an CIS line type
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_line_type_tag_0(client):
    """Test case for delete_cis_line_type_tag_0

    Delete CIS line type tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_cis_transaction(client):
    """Test case for delete_cis_transaction

    Delete the CIS transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/CisTransaction/{cis_transaction_id}'.format(employer_id='employer_id_example', cis_transaction_id='cis_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sub_contractor_tag_0(client):
    """Test case for delete_sub_contractor_tag_0

    Delete sub contractor tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_cis_instruction_tags_0(client):
    """Test case for get_all_cis_instruction_tags_0

    Get all CIS instruction tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstructions/Tags'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_cis_line_tags_0(client):
    """Test case for get_all_cis_line_tags_0

    Get all CIS line tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLines/Tags'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_cis_line_type_tags_0(client):
    """Test case for get_all_cis_line_type_tags_0

    Get all CIS line type tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisLineTypes/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_sub_contractor_tags_0(client):
    """Test case for get_all_sub_contractor_tags_0

    Get all sub contractor tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractors/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_instruction_from_sub_contractor(client):
    """Test case for get_cis_instruction_from_sub_contractor

    Get CIS instruction from sub contractor
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_instructions_from_sub_contractor(client):
    """Test case for get_cis_instructions_from_sub_contractor

    Get CIS instructions from sub contractor.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstructions'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_instructions_with_tag_0(client):
    """Test case for get_cis_instructions_with_tag_0

    Get CIS instructions with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstructions/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_line_from_sub_contractor(client):
    """Test case for get_cis_line_from_sub_contractor

    Get CIS line from sub contractor
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLine/{cis_line_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_line_id='cis_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_line_type_from_employer(client):
    """Test case for get_cis_line_type_from_employer

    Get CIS line type from employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_line_types_from_employer(client):
    """Test case for get_cis_line_types_from_employer

    Get CIS line types from employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisLineTypes'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_line_types_with_tag_0(client):
    """Test case for get_cis_line_types_with_tag_0

    Get CIS line types with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisLineTypes/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_lines_from_sub_contractor(client):
    """Test case for get_cis_lines_from_sub_contractor

    Get CIS lines from sub contractor.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLines'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_lines_with_tag_0(client):
    """Test case for get_cis_lines_with_tag_0

    Get CIS lines with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLines/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_transaction_from_employer(client):
    """Test case for get_cis_transaction_from_employer

    Get the CIS transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisTransaction/{cis_transaction_id}'.format(employer_id='employer_id_example', cis_transaction_id='cis_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cis_transactions_from_employer(client):
    """Test case for get_cis_transactions_from_employer

    Get all CIS transactions for the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisTransactions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractors_with_tag_0(client):
    """Test case for get_sub_contractors_with_tag_0

    Get sub contractors with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractors/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_cis_instruction_0(client):
    """Test case for get_tag_from_cis_instruction_0

    Get CIS instruction tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_cis_line_0(client):
    """Test case for get_tag_from_cis_line_0

    Get CIS line tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLine/{cis_line_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_line_id='cis_line_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_cis_line_type_0(client):
    """Test case for get_tag_from_cis_line_type_0

    Get CIS line type tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_sub_contractor_0(client):
    """Test case for get_tag_from_sub_contractor_0

    Get sub contractor tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_sub_contractor_revision_0(client):
    """Test case for get_tag_from_sub_contractor_revision_0

    Get sub contractor revision tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Tag/{tag_id}/{effective_date}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', tag_id='tag_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_cis_instruction_0(client):
    """Test case for get_tags_from_cis_instruction_0

    Get all tags from the CIS instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}/Tags'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_cis_line_0(client):
    """Test case for get_tags_from_cis_line_0

    Get all tags from the CIS line
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLine/{cis_line_id}/Tags'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_line_id='cis_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_cis_line_type_0(client):
    """Test case for get_tags_from_cis_line_type_0

    Get all tags from the CIS line type
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}/Tags'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_sub_contractor_0(client):
    """Test case for get_tags_from_sub_contractor_0

    Get all tags from the sub contractor
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Tags'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_sub_contractor_revision_0(client):
    """Test case for get_tags_from_sub_contractor_revision_0

    Get all sub contractor revision tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Tags/{effective_date}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_cis_instruction(client):
    """Test case for patch_cis_instruction

    Patches the CIS instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_cis_instruction_into_sub_contractor(client):
    """Test case for post_cis_instruction_into_sub_contractor

    Create a new CIS instruction
    """
    body = {"CisInstruction":{"UOM":"NotSet","Description":"Description","PayFrequency":"Monthly","CisLineType":"CisLineType","PeriodStart":6,"TaxYearEnd":1,"TaxYearStart":5,"VAT":2.3021358869347655,"Value":7.061401241503109,"CisLineTag":"CisLineTag","PeriodEnd":0,"Units":5.637376656633329}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstructions'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_cis_line_type_into_employer(client):
    """Test case for post_cis_line_type_into_employer

    Create a new CIS line type
    """
    body = {"CisLineType":{"Description":"Description","NominalCode":{"@title":"@title","@rel":"@rel","@href":"@href"},"TaxTreatment":"Taxable","LineType":"LineType"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/CisLineTypes'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_cis_instruction_into_sub_contractor(client):
    """Test case for put_cis_instruction_into_sub_contractor

    Updates the CIS instruction
    """
    body = {"CisInstruction":{"UOM":"NotSet","Description":"Description","PayFrequency":"Monthly","CisLineType":"CisLineType","PeriodStart":6,"TaxYearEnd":1,"TaxYearStart":5,"VAT":2.3021358869347655,"Value":7.061401241503109,"CisLineTag":"CisLineTag","PeriodEnd":0,"Units":5.637376656633329}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_cis_instruction_tag_0(client):
    """Test case for put_cis_instruction_tag_0

    Insert CIS instruction tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisInstruction/{cis_instruction_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_instruction_id='cis_instruction_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_cis_line_tag_0(client):
    """Test case for put_cis_line_tag_0

    Insert CIS line tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/CisLine/{cis_line_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', cis_line_id='cis_line_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_cis_line_type_into_employer(client):
    """Test case for put_cis_line_type_into_employer

    Updates the CIS line type
    """
    body = {"CisLineType":{"Description":"Description","NominalCode":{"@title":"@title","@rel":"@rel","@href":"@href"},"TaxTreatment":"Taxable","LineType":"LineType"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_cis_line_type_tag_0(client):
    """Test case for put_cis_line_type_tag_0

    Insert CIS line type tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/CisLineType/{cis_line_type_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', cis_line_type_id='cis_line_type_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_sub_contractor_tag_0(client):
    """Test case for put_sub_contractor_tag_0

    Insert sub contractor tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

