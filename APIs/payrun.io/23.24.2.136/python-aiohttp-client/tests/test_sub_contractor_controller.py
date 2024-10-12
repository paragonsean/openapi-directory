# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.sub_contractor import SubContractor


pytestmark = pytest.mark.asyncio

async def test_delete_sub_contractor(client):
    """Test case for delete_sub_contractor

    Delete an sub contractor
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sub_contractor_revision(client):
    """Test case for delete_sub_contractor_revision

    Delete an sub contractor revision matching the specified revision date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/{effective_date}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sub_contractor_revision_by_number(client):
    """Test case for delete_sub_contractor_revision_by_number

    Delete an SubContractor revision matching the specified revision number.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractor_by_effective_date(client):
    """Test case for get_sub_contractor_by_effective_date

    Get sub contractor by effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/{effective_date}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractor_from_employer(client):
    """Test case for get_sub_contractor_from_employer

    Get sub contractor from employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractor_revision_by_number(client):
    """Test case for get_sub_contractor_revision_by_number

    Gets the sub contractor by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractor_revisions(client):
    """Test case for get_sub_contractor_revisions

    Get all sub contractor revisions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}/Revisions'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractors_by_effective_date(client):
    """Test case for get_sub_contractors_by_effective_date

    Get sub contractors from employer at a given effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractors/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_contractors_from_employer(client):
    """Test case for get_sub_contractors_from_employer

    Get sub contractors from employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/SubContractors'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_sub_contractor(client):
    """Test case for patch_sub_contractor

    Patches the sub contractor
    """
    body = {"SubContractor":{"VerificationDate":"2000-01-23T04:56:07.000+00:00","NiNumber":"NiNumber","Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"Telephone":"Telephone","BusinessType":"SoleTrader","VatRegistrationNumber":"VatRegistrationNumber","CompanyRegistrationNumber":"CompanyRegistrationNumber","NextRevisionDate":"2000-01-23","CompanyName":"CompanyName","PayFrequency":"Monthly","MetaData":"{}","WorksNumber":"WorksNumber","PartnershipName":"PartnershipName","Territory":"UnitedKingdom","FirstName":"FirstName","UniqueTaxReference":"UniqueTaxReference","TaxationStatus":"Unmatched","Title":"Title","BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"Initials":"Initials","MiddleName":"MiddleName","VerificationNumber":"VerificationNumber","Revision":0,"Deactivated":True,"PaymentMethod":"NotSet","Region":"NotSet","TradingName":"TradingName","VatRegistered":True,"LastName":"LastName","PartnershipUniqueTaxReference":"PartnershipUniqueTaxReference","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_sub_contractor_into_employer(client):
    """Test case for post_sub_contractor_into_employer

    Create a new sub contractor
    """
    body = {"SubContractor":{"VerificationDate":"2000-01-23T04:56:07.000+00:00","NiNumber":"NiNumber","Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"Telephone":"Telephone","BusinessType":"SoleTrader","VatRegistrationNumber":"VatRegistrationNumber","CompanyRegistrationNumber":"CompanyRegistrationNumber","NextRevisionDate":"2000-01-23","CompanyName":"CompanyName","PayFrequency":"Monthly","MetaData":"{}","WorksNumber":"WorksNumber","PartnershipName":"PartnershipName","Territory":"UnitedKingdom","FirstName":"FirstName","UniqueTaxReference":"UniqueTaxReference","TaxationStatus":"Unmatched","Title":"Title","BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"Initials":"Initials","MiddleName":"MiddleName","VerificationNumber":"VerificationNumber","Revision":0,"Deactivated":True,"PaymentMethod":"NotSet","Region":"NotSet","TradingName":"TradingName","VatRegistered":True,"LastName":"LastName","PartnershipUniqueTaxReference":"PartnershipUniqueTaxReference","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/SubContractors'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_sub_contractor_into_employer(client):
    """Test case for put_sub_contractor_into_employer

    Updates the sub contractor
    """
    body = {"SubContractor":{"VerificationDate":"2000-01-23T04:56:07.000+00:00","NiNumber":"NiNumber","Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"Telephone":"Telephone","BusinessType":"SoleTrader","VatRegistrationNumber":"VatRegistrationNumber","CompanyRegistrationNumber":"CompanyRegistrationNumber","NextRevisionDate":"2000-01-23","CompanyName":"CompanyName","PayFrequency":"Monthly","MetaData":"{}","WorksNumber":"WorksNumber","PartnershipName":"PartnershipName","Territory":"UnitedKingdom","FirstName":"FirstName","UniqueTaxReference":"UniqueTaxReference","TaxationStatus":"Unmatched","Title":"Title","BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"Initials":"Initials","MiddleName":"MiddleName","VerificationNumber":"VerificationNumber","Revision":0,"Deactivated":True,"PaymentMethod":"NotSet","Region":"NotSet","TradingName":"TradingName","VatRegistered":True,"LastName":"LastName","PartnershipUniqueTaxReference":"PartnershipUniqueTaxReference","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/SubContractor/{sub_contractor_id}'.format(employer_id='employer_id_example', sub_contractor_id='sub_contractor_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

