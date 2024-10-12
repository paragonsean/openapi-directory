# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_code import PayCode


pytestmark = pytest.mark.asyncio

async def test_delete_pay_code(client):
    """Test case for delete_pay_code

    Deletes a pay code
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pay_code_revision(client):
    """Test case for delete_pay_code_revision

    Deletes a pay code revision
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}/{effective_date}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pay_code_revision_by_number(client):
    """Test case for delete_pay_code_revision_by_number

    Delete an PayCode revision matching the specified revision number.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_pay_code_tags_0(client):
    """Test case for get_all_pay_code_tags_0

    Get all pay code tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCodes/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_code_by_effective_date(client):
    """Test case for get_pay_code_by_effective_date

    Gets pay code for specified date
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}/{effective_date}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_code_from_employer(client):
    """Test case for get_pay_code_from_employer

    Gets the specified pay code from the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_code_revision_by_number(client):
    """Test case for get_pay_code_revision_by_number

    Gets the pay code by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_code_revisions(client):
    """Test case for get_pay_code_revisions

    Get all revisions of the Pay Code
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}/Revisions'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_codes_by_effective_date(client):
    """Test case for get_pay_codes_by_effective_date

    Gets all pay codes for specified date
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCodes/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_codes_from_employer(client):
    """Test case for get_pay_codes_from_employer

    Gets the pay codes from the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCodes'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_codes_from_nominal_code(client):
    """Test case for get_pay_codes_from_nominal_code

    Gets the pay codes by nominal code
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/NominalCode/{nominal_code_id}/PayCodes'.format(employer_id='employer_id_example', nominal_code_id='nominal_code_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_codes_with_tag_0(client):
    """Test case for get_pay_codes_with_tag_0

    Get pay codes with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PayCodes/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_pay_code(client):
    """Test case for patch_pay_code

    Patches the pay code
    """
    body = {"PayCode":{"Territory":"UnitedKingdom","Description":"Description","NominalCode":{"@title":"@title","@rel":"@rel","@href":"@href"},"Benefit":True,"Code":"Code","NextRevisionDate":"2000-01-23","Type":"NotSet","NonArrestable":True,"Readonly":True,"Revision":0,"MetaData":"{}","Region":"NotSet","Niable":True,"Notional":True,"EffectiveDate":"2000-01-23","Taxable":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_pay_code(client):
    """Test case for post_pay_code

    Create a new pay code
    """
    body = {"PayCode":{"Territory":"UnitedKingdom","Description":"Description","NominalCode":{"@title":"@title","@rel":"@rel","@href":"@href"},"Benefit":True,"Code":"Code","NextRevisionDate":"2000-01-23","Type":"NotSet","NonArrestable":True,"Readonly":True,"Revision":0,"MetaData":"{}","Region":"NotSet","Niable":True,"Notional":True,"EffectiveDate":"2000-01-23","Taxable":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/PayCodes'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_pay_code(client):
    """Test case for put_pay_code

    Updates a pay code
    """
    body = {"PayCode":{"Territory":"UnitedKingdom","Description":"Description","NominalCode":{"@title":"@title","@rel":"@rel","@href":"@href"},"Benefit":True,"Code":"Code","NextRevisionDate":"2000-01-23","Type":"NotSet","NonArrestable":True,"Readonly":True,"Revision":0,"MetaData":"{}","Region":"NotSet","Niable":True,"Notional":True,"EffectiveDate":"2000-01-23","Taxable":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/PayCode/{pay_code_id}'.format(employer_id='employer_id_example', pay_code_id='pay_code_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

