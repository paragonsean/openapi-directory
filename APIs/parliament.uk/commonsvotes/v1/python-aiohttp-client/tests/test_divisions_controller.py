# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.division_grouped_by_party import DivisionGroupedByParty
from openapi_server.models.member_voting_record import MemberVotingRecord
from openapi_server.models.published_division import PublishedDivision


pytestmark = pytest.mark.asyncio

async def test_divisions_get_division_by_id(client):
    """Test case for divisions_get_division_by_id

    Return a Division
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/division/{division_id_format}'.format(division_id=56, format='format_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_divisions_get_divisions_groups_by_party(client):
    """Test case for divisions_get_divisions_groups_by_party

    Return Divisions results grouped by party
    """
    params = [('queryParameters.searchTerm', 'query_parameters_search_term_example'),
                    ('queryParameters.memberId', 56),
                    ('queryParameters.includeWhenMemberWasTeller', True),
                    ('queryParameters.startDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.endDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.divisionNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/divisions.{format}/groupedbyparty'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_divisions_get_voting_records_for_member(client):
    """Test case for divisions_get_voting_records_for_member

    Return voting records for a Member
    """
    params = [('queryParameters.memberId', 56),
                    ('queryParameters.skip', 56),
                    ('queryParameters.take', 56),
                    ('queryParameters.searchTerm', 'query_parameters_search_term_example'),
                    ('queryParameters.includeWhenMemberWasTeller', True),
                    ('queryParameters.startDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.endDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.divisionNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/divisions.{format}/membervoting'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_divisions_search_divisions(client):
    """Test case for divisions_search_divisions

    Return a list of Divisions
    """
    params = [('queryParameters.skip', 56),
                    ('queryParameters.take', 56),
                    ('queryParameters.searchTerm', 'query_parameters_search_term_example'),
                    ('queryParameters.memberId', 56),
                    ('queryParameters.includeWhenMemberWasTeller', True),
                    ('queryParameters.startDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.endDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.divisionNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/divisions.{format}/search'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_divisions_search_total_results(client):
    """Test case for divisions_search_total_results

    Return total results count
    """
    params = [('queryParameters.searchTerm', 'query_parameters_search_term_example'),
                    ('queryParameters.memberId', 56),
                    ('queryParameters.includeWhenMemberWasTeller', True),
                    ('queryParameters.startDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.endDate', '2013-10-20T19:20:30+01:00'),
                    ('queryParameters.divisionNumber', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/divisions.{format}/searchTotalResults'.format(format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

