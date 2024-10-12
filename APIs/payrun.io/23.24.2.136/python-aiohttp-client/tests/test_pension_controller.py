# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pension import Pension


pytestmark = pytest.mark.asyncio

async def test_delete_pension(client):
    """Test case for delete_pension

    Delete a Pension
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Pension/{pension_id}'.format(employer_id='employer_id_example', pension_id='pension_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pension_revision(client):
    """Test case for delete_pension_revision

    Delete an Pension revision matching the specified revision date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Pension/{pension_id}/{effective_date}'.format(employer_id='employer_id_example', pension_id='pension_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pension_revision_by_number(client):
    """Test case for delete_pension_revision_by_number

    Delete an Pension revision matching the specified revision number.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Pension/{pension_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', pension_id='pension_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pension_by_effective_date(client):
    """Test case for get_pension_by_effective_date

    Get pension by effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Pension/{pension_id}/{effective_date}'.format(employer_id='employer_id_example', pension_id='pension_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pension_from_employer(client):
    """Test case for get_pension_from_employer

    Get pension from employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Pension/{pension_id}'.format(employer_id='employer_id_example', pension_id='pension_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pension_revision_by_number(client):
    """Test case for get_pension_revision_by_number

    Gets the pension by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Pension/{pension_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', pension_id='pension_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pension_revisions(client):
    """Test case for get_pension_revisions

    Get all pension revisions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Pension/{pension_id}/Revisions'.format(employer_id='employer_id_example', pension_id='pension_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pensions_by_effective_date(client):
    """Test case for get_pensions_by_effective_date

    Get pensions from employer at a given effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Pensions/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pensions_from_employer(client):
    """Test case for get_pensions_from_employer

    Get pensions from employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Pensions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_pension(client):
    """Test case for patch_pension

    Patches the pension
    """
    body = {"Pension":{"Group":"Group","EmployerNiSaving":True,"EmployerContributionPercent":5.637376656633329,"UseAEThresholds":True,"RasRoundingOverride":"NotSet","AECompatible":True,"EmployerContributionCash":5.962133916683182,"NextRevisionDate":"2000-01-23","ProRataMethod":"NotSet","PensionablePayCodes":{"PayCode":["PayCode","PayCode"]},"MetaData":"{}","EmployeeContributionPercent":1.4658129805029452,"EmployeeContributionCash":6.027456183070403,"TaxationMethod":"NotSet","SubGroup":"SubGroup","Code":"Code","RoundingOption":"NotSet","Certification":"NotSet","ProviderName":"ProviderName","QualifyingPayCodes":{"PayCode":["PayCode","PayCode"]},"EmployerNiSavingPercentage":2.3021358869347655,"LowerThreshold":7.061401241503109,"Revision":9,"ProviderEmployerRef":"ProviderEmployerRef","ContributionDeductionDay":0,"SchemeName":"SchemeName","SalarySacrifice":True,"UpperThreshold":3.616076749251911,"EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/Pension/{pension_id}'.format(employer_id='employer_id_example', pension_id='pension_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_pension_into_employer(client):
    """Test case for post_pension_into_employer

    Create a new Pension
    """
    body = {"Pension":{"Group":"Group","EmployerNiSaving":True,"EmployerContributionPercent":5.637376656633329,"UseAEThresholds":True,"RasRoundingOverride":"NotSet","AECompatible":True,"EmployerContributionCash":5.962133916683182,"NextRevisionDate":"2000-01-23","ProRataMethod":"NotSet","PensionablePayCodes":{"PayCode":["PayCode","PayCode"]},"MetaData":"{}","EmployeeContributionPercent":1.4658129805029452,"EmployeeContributionCash":6.027456183070403,"TaxationMethod":"NotSet","SubGroup":"SubGroup","Code":"Code","RoundingOption":"NotSet","Certification":"NotSet","ProviderName":"ProviderName","QualifyingPayCodes":{"PayCode":["PayCode","PayCode"]},"EmployerNiSavingPercentage":2.3021358869347655,"LowerThreshold":7.061401241503109,"Revision":9,"ProviderEmployerRef":"ProviderEmployerRef","ContributionDeductionDay":0,"SchemeName":"SchemeName","SalarySacrifice":True,"UpperThreshold":3.616076749251911,"EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/Pensions'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_pension_into_employer(client):
    """Test case for put_pension_into_employer

    Updates the Pension
    """
    body = {"Pension":{"Group":"Group","EmployerNiSaving":True,"EmployerContributionPercent":5.637376656633329,"UseAEThresholds":True,"RasRoundingOverride":"NotSet","AECompatible":True,"EmployerContributionCash":5.962133916683182,"NextRevisionDate":"2000-01-23","ProRataMethod":"NotSet","PensionablePayCodes":{"PayCode":["PayCode","PayCode"]},"MetaData":"{}","EmployeeContributionPercent":1.4658129805029452,"EmployeeContributionCash":6.027456183070403,"TaxationMethod":"NotSet","SubGroup":"SubGroup","Code":"Code","RoundingOption":"NotSet","Certification":"NotSet","ProviderName":"ProviderName","QualifyingPayCodes":{"PayCode":["PayCode","PayCode"]},"EmployerNiSavingPercentage":2.3021358869347655,"LowerThreshold":7.061401241503109,"Revision":9,"ProviderEmployerRef":"ProviderEmployerRef","ContributionDeductionDay":0,"SchemeName":"SchemeName","SalarySacrifice":True,"UpperThreshold":3.616076749251911,"EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/Pension/{pension_id}'.format(employer_id='employer_id_example', pension_id='pension_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

