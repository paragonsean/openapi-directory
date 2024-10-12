# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.reporting_property_mortgage_model_results import ReportingPropertyMortgageModelResults
from openapi_server.models.reporting_receivership_case_model_results import ReportingReceivershipCaseModelResults


pytestmark = pytest.mark.asyncio

async def test_reporting_controller_mortgages_by_created_date(client):
    """Test case for reporting_controller_mortgages_by_created_date

    Return a collection of mortgages by created date from a specific date
    """
    params = [('branchID', 'branch_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/reporting/{short_name}/mortgagesbycreateddate'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_controller_mortgages_by_updated_date(client):
    """Test case for reporting_controller_mortgages_by_updated_date

    Return a collection of all mortgages updated from a specific date
    """
    params = [('branchID', 'branch_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/reporting/{short_name}/mortgagesbyupdateddate'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_controller_repossessions_by_created_date(client):
    """Test case for reporting_controller_repossessions_by_created_date

    Return a collection of repossessions by created date from a specific date
    """
    params = [('branchID', 'branch_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/reporting/{short_name}/repossesionsbycreateddate'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reporting_controller_repossessions_by_updated_date(client):
    """Test case for reporting_controller_repossessions_by_updated_date

    Return a collection of all reposessions updated from a specific date
    """
    params = [('branchID', 'branch_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/reporting/{short_name}/repossesionsbyupdateddate'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

