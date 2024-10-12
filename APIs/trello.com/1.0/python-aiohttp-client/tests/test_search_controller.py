# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_search(client):
    """Test case for get_search

    getSearch()
    """
    params = [('query', 'query_example'),
                    ('idBoards', 'mine'),
                    ('idOrganizations', 'id_organizations_example'),
                    ('idCards', 'id_cards_example'),
                    ('modelTypes', 'all'),
                    ('board_fields', 'name and idOrganization'),
                    ('boards_limit', '10'),
                    ('card_fields', 'all'),
                    ('cards_limit', '10'),
                    ('cards_page', '0'),
                    ('card_board', 'card_board_example'),
                    ('card_list', 'card_list_example'),
                    ('card_members', 'card_members_example'),
                    ('card_stickers', 'card_stickers_example'),
                    ('card_attachments', 'card_attachments_example'),
                    ('organization_fields', 'name and displayName'),
                    ('organizations_limit', '10'),
                    ('member_fields', 'avatarHash, fullName, initials, username and confirmed'),
                    ('members_limit', '10'),
                    ('partial', 'partial_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search_members(client):
    """Test case for get_search_members

    getSearchMembers()
    """
    params = [('query', 'query_example'),
                    ('limit', '8'),
                    ('idBoard', 'id_board_example'),
                    ('idOrganization', 'id_organization_example'),
                    ('onlyOrgMembers', 'only_org_members_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/search/members',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

