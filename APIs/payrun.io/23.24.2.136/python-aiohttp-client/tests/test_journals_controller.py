# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.journal_instruction import JournalInstruction
from openapi_server.models.journal_line import JournalLine
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection


pytestmark = pytest.mark.asyncio

async def test_delete_journal_instruction(client):
    """Test case for delete_journal_instruction

    Deletes a Journal instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/JournalInstruction/{journal_instruction_id}'.format(employer_id='employer_id_example', journal_instruction_id='journal_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_journal_instruction_template(client):
    """Test case for delete_journal_instruction_template

    Deletes a Journal instruction template
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/JournalInstruction/{journal_instruction_id}'.format(journal_instruction_id='journal_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_instruction_from_employer(client):
    """Test case for get_journal_instruction_from_employer

    Gets the specified journal instruction from the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/JournalInstruction/{journal_instruction_id}'.format(employer_id='employer_id_example', journal_instruction_id='journal_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_instruction_template(client):
    """Test case for get_journal_instruction_template

    Gets the Journal instructions template for the application
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/JournalInstruction/{journal_instruction_id}'.format(journal_instruction_id='journal_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_instruction_templates(client):
    """Test case for get_journal_instruction_templates

    Gets the Journal instructions templates for the application
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/JournalInstructions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_instructions_from_employer(client):
    """Test case for get_journal_instructions_from_employer

    Gets the Journal instructions from the specified employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/JournalInstructions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_line_from_employer(client):
    """Test case for get_journal_line_from_employer

    Gets the specified journal Line from the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/JournalLine/{journal_line_id}'.format(employer_id='employer_id_example', journal_line_id='journal_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_lines_from_employee(client):
    """Test case for get_journal_lines_from_employee

    Gets the journal Lines from the specified employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/JournalLines'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_lines_from_employer(client):
    """Test case for get_journal_lines_from_employer

    Gets the Journal Lines from the specified employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/JournalLines'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_lines_from_pay_run(client):
    """Test case for get_journal_lines_from_pay_run

    Gets the journal Lines from the specified pay run
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/JournalLines'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_lines_from_sub_contractor(client):
    """Test case for get_journal_lines_from_sub_contractor

    Gets the journal Lines from the specified sub contractor
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/JournalLines'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_journal_instruction(client):
    """Test case for post_journal_instruction

    Creates a new Journal Instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/JournalInstructions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_journal_instruction_template(client):
    """Test case for post_journal_instruction_template

    Creates a new Journal Instruction template
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/JournalInstructions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_journal_instruction(client):
    """Test case for put_journal_instruction

    Update a Journal Instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/JournalInstruction/{journal_instruction_id}'.format(employer_id='employer_id_example', journal_instruction_id='journal_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_journal_instruction_template(client):
    """Test case for put_journal_instruction_template

    Update a Journal Instruction template
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/JournalInstruction/{journal_instruction_id}'.format(journal_instruction_id='journal_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

