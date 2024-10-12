# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.biography_experience_list_item import BiographyExperienceListItem
from openapi_server.models.contact_information_list_item import ContactInformationListItem
from openapi_server.models.debate_contribution_members_service_search_result import DebateContributionMembersServiceSearchResult
from openapi_server.models.early_day_motion_members_service_search_result import EarlyDayMotionMembersServiceSearchResult
from openapi_server.models.election_result_item import ElectionResultItem
from openapi_server.models.house import House
from openapi_server.models.member_biography_item import MemberBiographyItem
from openapi_server.models.member_focus_list_item import MemberFocusListItem
from openapi_server.models.member_history_item import MemberHistoryItem
from openapi_server.models.member_item import MemberItem
from openapi_server.models.member_members_service_search_result import MemberMembersServiceSearchResult
from openapi_server.models.portrait_crop_enum import PortraitCropEnum
from openapi_server.models.registered_interest_category_list_item import RegisteredInterestCategoryListItem
from openapi_server.models.staff_list_item import StaffListItem
from openapi_server.models.string_item import StringItem
from openapi_server.models.vote_members_service_search_result import VoteMembersServiceSearchResult
from openapi_server.models.written_question_members_service_search_result import WrittenQuestionMembersServiceSearchResult


pytestmark = pytest.mark.asyncio

async def test_api_members_history_get(client):
    """Test case for api_members_history_get

    Return members by ID with list of their historical names, parties and memberships
    """
    params = [('ids', [56])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/History',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_biography_get(client):
    """Test case for api_members_id_biography_get

    Return biography of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Biography'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_contact_get(client):
    """Test case for api_members_id_contact_get

    Return list of contact details of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Contact'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_contribution_summary_get(client):
    """Test case for api_members_id_contribution_summary_get

    Return contribution summary of member by ID
    """
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/ContributionSummary'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_edms_get(client):
    """Test case for api_members_id_edms_get

    Return list of early day motions of member by ID
    """
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Edms'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_experience_get(client):
    """Test case for api_members_id_experience_get

    Return experience of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Experience'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_focus_get(client):
    """Test case for api_members_id_focus_get

    Return list of areas of focus of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Focus'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_get(client):
    """Test case for api_members_id_get

    Return member by ID
    """
    params = [('detailsForDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_latest_election_result_get(client):
    """Test case for api_members_id_latest_election_result_get

    Return latest election result of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/LatestElectionResult'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_portrait_get(client):
    """Test case for api_members_id_portrait_get

    Return portrait of member by ID
    """
    params = [('cropType', openapi_server.PortraitCropEnum()),
                    ('webVersion', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Portrait'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_portrait_url_get(client):
    """Test case for api_members_id_portrait_url_get

    Return portrait url of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/PortraitUrl'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_registered_interests_get(client):
    """Test case for api_members_id_registered_interests_get

    Return list of registered interests of member by ID
    """
    params = [('house', openapi_server.House())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/RegisteredInterests'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_staff_get(client):
    """Test case for api_members_id_staff_get

    Return list of staff of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Staff'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_synopsis_get(client):
    """Test case for api_members_id_synopsis_get

    Return synopsis of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Synopsis'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_thumbnail_get(client):
    """Test case for api_members_id_thumbnail_get

    Return thumbnail of member by ID
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Thumbnail'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_thumbnail_url_get(client):
    """Test case for api_members_id_thumbnail_url_get

    Return thumbnail url of member by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/ThumbnailUrl'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_voting_get(client):
    """Test case for api_members_id_voting_get

    Return list of votes by member by ID
    """
    params = [('house', openapi_server.House()),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/Voting'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_id_written_questions_get(client):
    """Test case for api_members_id_written_questions_get

    Return list of written questions by member by ID
    """
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/{id}/WrittenQuestions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_search_get(client):
    """Test case for api_members_search_get

    Returns a list of current members of the Commons or Lords
    """
    params = [('Name', 'name_example'),
                    ('Location', 'location_example'),
                    ('PostTitle', 'post_title_example'),
                    ('PartyId', 56),
                    ('House', openapi_server.House()),
                    ('ConstituencyId', 56),
                    ('NameStartsWith', 'name_starts_with_example'),
                    ('Gender', 'gender_example'),
                    ('MembershipStartedSince', '2013-10-20T19:20:30+01:00'),
                    ('MembershipEnded.MembershipEndedSince', '2013-10-20T19:20:30+01:00'),
                    ('MembershipEnded.MembershipEndReasonIds', [56]),
                    ('MembershipInDateRange.WasMemberOnOrAfter', '2013-10-20T19:20:30+01:00'),
                    ('MembershipInDateRange.WasMemberOnOrBefore', '2013-10-20T19:20:30+01:00'),
                    ('MembershipInDateRange.WasMemberOfHouse', openapi_server.House()),
                    ('IsEligible', True),
                    ('IsCurrentMember', True),
                    ('PolicyInterestId', 56),
                    ('Experience', 'experience_example'),
                    ('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_members_search_historical_get(client):
    """Test case for api_members_search_historical_get

    Returns a list of members of the Commons or Lords
    """
    params = [('name', 'name_example'),
                    ('dateToSearchFor', '2013-10-20T19:20:30+01:00'),
                    ('skip', 0),
                    ('take', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Members/SearchHistorical',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

