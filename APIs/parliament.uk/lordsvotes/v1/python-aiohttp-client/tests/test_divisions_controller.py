# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comparators import Comparators
from openapi_server.models.division_group_by_party_view_model import DivisionGroupByPartyViewModel
from openapi_server.models.division_view_model import DivisionViewModel
from openapi_server.models.member_voting_record_view_model import MemberVotingRecordViewModel


pytestmark = pytest.mark.asyncio

async def test_data_divisions_division_id_get(client):
    """Test case for data_divisions_division_id_get

    Return a Division
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/Divisions/{division_id}'.format(division_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_divisions_groupedbyparty_get(client):
    """Test case for data_divisions_groupedbyparty_get

    Return Divisions results grouped by party
    """
    params = [('SearchTerm', 'search_term_example'),
                    ('MemberId', 56),
                    ('IncludeWhenMemberWasTeller', True),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('DivisionNumber', 56),
                    ('TotalVotesCast.Comparator', openapi_server.Comparators()),
                    ('TotalVotesCast.ValueToCompare', 56),
                    ('Majority.Comparator', openapi_server.Comparators()),
                    ('Majority.ValueToCompare', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/Divisions/groupedbyparty',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_divisions_membervoting_get(client):
    """Test case for data_divisions_membervoting_get

    Return voting records for a Member
    """
    params = [('MemberId', 56),
                    ('SearchTerm', 'search_term_example'),
                    ('IncludeWhenMemberWasTeller', True),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('DivisionNumber', 56),
                    ('TotalVotesCast.Comparator', openapi_server.Comparators()),
                    ('TotalVotesCast.ValueToCompare', 56),
                    ('Majority.Comparator', openapi_server.Comparators()),
                    ('Majority.ValueToCompare', 56),
                    ('skip', 0),
                    ('take', 25)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/Divisions/membervoting',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_divisions_search_get(client):
    """Test case for data_divisions_search_get

    Return a list of Divisions
    """
    params = [('SearchTerm', 'search_term_example'),
                    ('MemberId', 56),
                    ('IncludeWhenMemberWasTeller', True),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('DivisionNumber', 56),
                    ('TotalVotesCast.Comparator', openapi_server.Comparators()),
                    ('TotalVotesCast.ValueToCompare', 56),
                    ('Majority.Comparator', openapi_server.Comparators()),
                    ('Majority.ValueToCompare', 56),
                    ('skip', 0),
                    ('take', 25)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/Divisions/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_divisions_search_total_results_get(client):
    """Test case for data_divisions_search_total_results_get

    Return total results count
    """
    params = [('SearchTerm', 'search_term_example'),
                    ('MemberId', 56),
                    ('IncludeWhenMemberWasTeller', True),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('DivisionNumber', 56),
                    ('TotalVotesCast.Comparator', openapi_server.Comparators()),
                    ('TotalVotesCast.ValueToCompare', 56),
                    ('Majority.Comparator', openapi_server.Comparators()),
                    ('Majority.ValueToCompare', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/data/Divisions/searchTotalResults',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

