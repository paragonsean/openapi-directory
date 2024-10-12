# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.holiday_scheme import HolidayScheme
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_delete_holiday_scheme(client):
    """Test case for delete_holiday_scheme

    Delete an holiday scheme
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_holiday_scheme_revision(client):
    """Test case for delete_holiday_scheme_revision

    Delete an holiday scheme revision matching the specified revision date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/{effective_date}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_holiday_scheme_revision_by_number(client):
    """Test case for delete_holiday_scheme_revision_by_number

    Delete an HolidayScheme revision matching the specified revision number.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_holiday_scheme_tag_0(client):
    """Test case for delete_holiday_scheme_tag_0

    Delete holiday scheme tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_holiday_scheme_tags_0(client):
    """Test case for get_all_holiday_scheme_tags_0

    Get all holiday scheme tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidaySchemes/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_scheme_by_effective_date(client):
    """Test case for get_holiday_scheme_by_effective_date

    Get holiday scheme by effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/{effective_date}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_scheme_from_employer(client):
    """Test case for get_holiday_scheme_from_employer

    Get holiday scheme from employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_scheme_revision_by_number(client):
    """Test case for get_holiday_scheme_revision_by_number

    Gets the holiday scheme revision by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_scheme_revisions(client):
    """Test case for get_holiday_scheme_revisions

    Get all holiday scheme revisions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Revisions'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_schemes_by_effective_date(client):
    """Test case for get_holiday_schemes_by_effective_date

    Get holiday schemes from employer at a given effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidaySchemes/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_schemes_from_employer(client):
    """Test case for get_holiday_schemes_from_employer

    Get holiday schemes from employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidaySchemes'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_schemes_with_tag_0(client):
    """Test case for get_holiday_schemes_with_tag_0

    Get holiday schemes with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidaySchemes/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_holiday_scheme_0(client):
    """Test case for get_tag_from_holiday_scheme_0

    Get holiday scheme tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tag_from_holiday_scheme_revision_0(client):
    """Test case for get_tag_from_holiday_scheme_revision_0

    Get holiday scheme revision tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Tag/{tag_id}/{effective_date}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', tag_id='tag_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_holiday_scheme_0(client):
    """Test case for get_tags_from_holiday_scheme_0

    Get all tags from the holiday scheme
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Tags'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tags_from_holiday_scheme_revision_0(client):
    """Test case for get_tags_from_holiday_scheme_revision_0

    Get all holiday scheme revision tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Tags/{effective_date}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_holiday_scheme(client):
    """Test case for patch_holiday_scheme

    Patches the holiday scheme
    """
    body = {"HolidayScheme":{"AllowNegativeBalance":True,"BankHolidayInclusive":True,"OffsetPayment":True,"SchemeCeasedDate":"2000-01-23","Code":"Code","SchemeKey":"SchemeKey","AllowExceedAnnualEntitlement":True,"NextRevisionDate":"2000-01-23","AnnualEntitlementWeeks":0.8008281904610115,"Revision":1,"MaxCarryOverDays":6.027456183070403,"YearStartDay":5,"SchemeName":"SchemeName","YearStartMonth":5,"AccrualPayCodes":{"PayCode":["PayCode","PayCode"]},"EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_holiday_scheme_into_employer(client):
    """Test case for post_holiday_scheme_into_employer

    Create a new holiday scheme
    """
    body = {"HolidayScheme":{"AllowNegativeBalance":True,"BankHolidayInclusive":True,"OffsetPayment":True,"SchemeCeasedDate":"2000-01-23","Code":"Code","SchemeKey":"SchemeKey","AllowExceedAnnualEntitlement":True,"NextRevisionDate":"2000-01-23","AnnualEntitlementWeeks":0.8008281904610115,"Revision":1,"MaxCarryOverDays":6.027456183070403,"YearStartDay":5,"SchemeName":"SchemeName","YearStartMonth":5,"AccrualPayCodes":{"PayCode":["PayCode","PayCode"]},"EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/HolidaySchemes'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_holiday_scheme_into_employer(client):
    """Test case for put_holiday_scheme_into_employer

    Updates the holiday scheme
    """
    body = {"HolidayScheme":{"AllowNegativeBalance":True,"BankHolidayInclusive":True,"OffsetPayment":True,"SchemeCeasedDate":"2000-01-23","Code":"Code","SchemeKey":"SchemeKey","AllowExceedAnnualEntitlement":True,"NextRevisionDate":"2000-01-23","AnnualEntitlementWeeks":0.8008281904610115,"Revision":1,"MaxCarryOverDays":6.027456183070403,"YearStartDay":5,"SchemeName":"SchemeName","YearStartMonth":5,"AccrualPayCodes":{"PayCode":["PayCode","PayCode"]},"EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_holiday_scheme_tag_0(client):
    """Test case for put_holiday_scheme_tag_0

    Insert holiday scheme tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/HolidayScheme/{holiday_scheme_id}/Tag/{tag_id}'.format(employer_id='employer_id_example', holiday_scheme_id='holiday_scheme_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

