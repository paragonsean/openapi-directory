# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.employer import Employer
from openapi_server.models.employer_secret import EmployerSecret
from openapi_server.models.employer_summary import EmployerSummary
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection


pytestmark = pytest.mark.asyncio

async def test_delete_employer(client):
    """Test case for delete_employer

    Delete an Employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employer_revision(client):
    """Test case for delete_employer_revision

    Delete an Employer revision matching the specified revision date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employer_revision_by_number(client):
    """Test case for delete_employer_revision_by_number

    Delete an Employer revision matching the specified revision number.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employer_secret(client):
    """Test case for delete_employer_secret

    Deletes employer secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Secret/{secret_id}'.format(employer_id='employer_id_example', secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_employer_tags_0(client):
    """Test case for get_all_employer_tags_0

    Get all employer tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employers/Tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer(client):
    """Test case for get_employer

    Gets the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_by_effective_date(client):
    """Test case for get_employer_by_effective_date

    Gets the employer at the specified effective
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_revision_by_number(client):
    """Test case for get_employer_revision_by_number

    Gets the employer by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_revision_summaries(client):
    """Test case for get_employer_revision_summaries

    Get all employer revision summaries
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Revisions/Summary'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_revision_summary_by_number(client):
    """Test case for get_employer_revision_summary_by_number

    Gets the employer summary by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Revision/{revision_number}/Summary'.format(employer_id='employer_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_revisions(client):
    """Test case for get_employer_revisions

    Gets the employer revisions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Revisions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_secret(client):
    """Test case for get_employer_secret

    Get employer secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Secret/{secret_id}'.format(employer_id='employer_id_example', secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_secrets(client):
    """Test case for get_employer_secrets

    Get all employer secret links
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Secrets'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_summaries(client):
    """Test case for get_employer_summaries

    Get employer summaries.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employers/Summary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_summaries_by_effective_date(client):
    """Test case for get_employer_summaries_by_effective_date

    Get employer summaries at a given effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employers/{effective_date}/Summary'.format(effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_summary(client):
    """Test case for get_employer_summary

    Get employer summary
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Summary'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_summary_by_effective_date(client):
    """Test case for get_employer_summary_by_effective_date

    Get employer summary by effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/{effective_date}/Summary'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employers(client):
    """Test case for get_employers

    Gets all employers
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employers_by_effective_date(client):
    """Test case for get_employers_by_effective_date

    Gets all employers at the specified effective date
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employers/{effective_date}'.format(effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employers_with_tag_0(client):
    """Test case for get_employers_with_tag_0

    Get employers with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employers/Tag/{tag_id}'.format(tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_employer(client):
    """Test case for patch_employer

    Patches the employer
    """
    body = {"Employer":{"CalculateApprenticeshipLevy":True,"ClaimEmploymentAllowance":True,"Territory":"UnitedKingdom","AutoEnrolment":{"Pension":{"@title":"@title","@rel":"@rel","@href":"@href"},"PrimaryAddress":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"PrimaryLastName":"PrimaryLastName","SecondaryTelephone":"SecondaryTelephone","SecondaryAddress":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"PrimaryTelephone":"PrimaryTelephone","PrimaryEmail":"PrimaryEmail","RecentOptOutReEnrolmentExcluded":True,"StagingDate":"2000-01-23","SecondaryJobTitle":"SecondaryJobTitle","SecondaryLastName":"SecondaryLastName","PostponementDate":"2000-01-23","SecondaryFirstName":"SecondaryFirstName","SecondaryEmail":"SecondaryEmail","ReEnrolmentMonthOffset":1,"PrimaryJobTitle":"PrimaryJobTitle","PrimaryFirstName":"PrimaryFirstName","ReEnrolmentDayOffset":6},"Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"HmrcSettings":{"ContactTelephone":"ContactTelephone","SenderId":"SenderId","StateAidSector":"Agriculture","ContactLastName":"ContactLastName","Sender":"Employer","TaxOfficeNumber":"TaxOfficeNumber","SAUTR":"SAUTR","ContactEmail":"ContactEmail","ContactFax":"ContactFax","COTAXRef":"COTAXRef","ContactFirstName":"ContactFirstName","TaxOfficeReference":"TaxOfficeReference","AccountingOfficeRef":"AccountingOfficeRef","EmploymentAllowanceOverride":5.962133916683182,"Password":"Password"},"BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"ClaimSmallEmployerRelief":True,"ApprenticeshipLevyAllowance":0.8008281904610115,"Name":"Name","NextRevisionDate":"2000-01-23","Revision":5,"MetaData":"{}","Region":"NotSet","RuleExclusions":"None","BacsServiceUserNumber":"BacsServiceUserNumber","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_employer(client):
    """Test case for post_employer

    Create a new Employer
    """
    body = {"Employer":{"CalculateApprenticeshipLevy":True,"ClaimEmploymentAllowance":True,"Territory":"UnitedKingdom","AutoEnrolment":{"Pension":{"@title":"@title","@rel":"@rel","@href":"@href"},"PrimaryAddress":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"PrimaryLastName":"PrimaryLastName","SecondaryTelephone":"SecondaryTelephone","SecondaryAddress":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"PrimaryTelephone":"PrimaryTelephone","PrimaryEmail":"PrimaryEmail","RecentOptOutReEnrolmentExcluded":True,"StagingDate":"2000-01-23","SecondaryJobTitle":"SecondaryJobTitle","SecondaryLastName":"SecondaryLastName","PostponementDate":"2000-01-23","SecondaryFirstName":"SecondaryFirstName","SecondaryEmail":"SecondaryEmail","ReEnrolmentMonthOffset":1,"PrimaryJobTitle":"PrimaryJobTitle","PrimaryFirstName":"PrimaryFirstName","ReEnrolmentDayOffset":6},"Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"HmrcSettings":{"ContactTelephone":"ContactTelephone","SenderId":"SenderId","StateAidSector":"Agriculture","ContactLastName":"ContactLastName","Sender":"Employer","TaxOfficeNumber":"TaxOfficeNumber","SAUTR":"SAUTR","ContactEmail":"ContactEmail","ContactFax":"ContactFax","COTAXRef":"COTAXRef","ContactFirstName":"ContactFirstName","TaxOfficeReference":"TaxOfficeReference","AccountingOfficeRef":"AccountingOfficeRef","EmploymentAllowanceOverride":5.962133916683182,"Password":"Password"},"BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"ClaimSmallEmployerRelief":True,"ApprenticeshipLevyAllowance":0.8008281904610115,"Name":"Name","NextRevisionDate":"2000-01-23","Revision":5,"MetaData":"{}","Region":"NotSet","RuleExclusions":"None","BacsServiceUserNumber":"BacsServiceUserNumber","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_employer_secret(client):
    """Test case for post_employer_secret

    Create a new employer secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/Secrets'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_employer(client):
    """Test case for put_employer

    Updates the Employer
    """
    body = {"Employer":{"CalculateApprenticeshipLevy":True,"ClaimEmploymentAllowance":True,"Territory":"UnitedKingdom","AutoEnrolment":{"Pension":{"@title":"@title","@rel":"@rel","@href":"@href"},"PrimaryAddress":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"PrimaryLastName":"PrimaryLastName","SecondaryTelephone":"SecondaryTelephone","SecondaryAddress":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"PrimaryTelephone":"PrimaryTelephone","PrimaryEmail":"PrimaryEmail","RecentOptOutReEnrolmentExcluded":True,"StagingDate":"2000-01-23","SecondaryJobTitle":"SecondaryJobTitle","SecondaryLastName":"SecondaryLastName","PostponementDate":"2000-01-23","SecondaryFirstName":"SecondaryFirstName","SecondaryEmail":"SecondaryEmail","ReEnrolmentMonthOffset":1,"PrimaryJobTitle":"PrimaryJobTitle","PrimaryFirstName":"PrimaryFirstName","ReEnrolmentDayOffset":6},"Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"HmrcSettings":{"ContactTelephone":"ContactTelephone","SenderId":"SenderId","StateAidSector":"Agriculture","ContactLastName":"ContactLastName","Sender":"Employer","TaxOfficeNumber":"TaxOfficeNumber","SAUTR":"SAUTR","ContactEmail":"ContactEmail","ContactFax":"ContactFax","COTAXRef":"COTAXRef","ContactFirstName":"ContactFirstName","TaxOfficeReference":"TaxOfficeReference","AccountingOfficeRef":"AccountingOfficeRef","EmploymentAllowanceOverride":5.962133916683182,"Password":"Password"},"BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"ClaimSmallEmployerRelief":True,"ApprenticeshipLevyAllowance":0.8008281904610115,"Name":"Name","NextRevisionDate":"2000-01-23","Revision":5,"MetaData":"{}","Region":"NotSet","RuleExclusions":"None","BacsServiceUserNumber":"BacsServiceUserNumber","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_employer_secret(client):
    """Test case for put_employer_secret

    Create a new employer secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/Secret/{secret_id}'.format(employer_id='employer_id_example', secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

