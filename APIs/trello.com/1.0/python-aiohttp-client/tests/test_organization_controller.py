# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.organizations import Organizations
from openapi_server.models.organizations_desc import OrganizationsDesc
from openapi_server.models.organizations_display_name import OrganizationsDisplayName
from openapi_server.models.organizations_logo import OrganizationsLogo
from openapi_server.models.organizations_members import OrganizationsMembers
from openapi_server.models.organizations_members_deactivated import OrganizationsMembersDeactivated
from openapi_server.models.organizations_memberships import OrganizationsMemberships
from openapi_server.models.organizations_name import OrganizationsName
from openapi_server.models.organizations_website import OrganizationsWebsite
from openapi_server.models.prefs_associated_domain import PrefsAssociatedDomain
from openapi_server.models.prefs_board_visibility_restrict import PrefsBoardVisibilityRestrict
from openapi_server.models.prefs_external_members_disabled import PrefsExternalMembersDisabled
from openapi_server.models.prefs_google_apps_version import PrefsGoogleAppsVersion
from openapi_server.models.prefs_org_invite_restrict import PrefsOrgInviteRestrict
from openapi_server.models.prefs_permission_level import PrefsPermissionLevel


pytestmark = pytest.mark.asyncio

async def test_add_organizations(client):
    """Test case for add_organizations

    addOrganizations()
    """
    body = openapi_server.Organizations()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/organizations',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_organizations_logo_by_id_org(client):
    """Test case for add_organizations_logo_by_id_org

    addOrganizationsLogoByIdOrg()
    """
    body = openapi_server.OrganizationsLogo()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/organizations/{id_org}/logo'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organizations_by_id_org(client):
    """Test case for delete_organizations_by_id_org

    deleteOrganizationsByIdOrg()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/organizations/{id_org}'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organizations_logo_by_id_org(client):
    """Test case for delete_organizations_logo_by_id_org

    deleteOrganizationsLogoByIdOrg()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/organizations/{id_org}/logo'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organizations_members_all_by_id_org_by_id_member(client):
    """Test case for delete_organizations_members_all_by_id_org_by_id_member

    deleteOrganizationsMembersAllByIdOrgByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/organizations/{id_org}/members/{id_member}/all'.format(id_org='id_org_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organizations_members_by_id_org_by_id_member(client):
    """Test case for delete_organizations_members_by_id_org_by_id_member

    deleteOrganizationsMembersByIdOrgByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/organizations/{id_org}/members/{id_member}'.format(id_org='id_org_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organizations_prefs_associated_domain_by_id_org(client):
    """Test case for delete_organizations_prefs_associated_domain_by_id_org

    deleteOrganizationsPrefsAssociatedDomainByIdOrg()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/organizations/{id_org}/prefs/associatedDomain'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organizations_prefs_org_invite_restrict_by_id_org(client):
    """Test case for delete_organizations_prefs_org_invite_restrict_by_id_org

    deleteOrganizationsPrefsOrgInviteRestrictByIdOrg()
    """
    params = [('value', 'value_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/organizations/{id_org}/prefs/orgInviteRestrict'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_actions_by_id_org(client):
    """Test case for get_organizations_actions_by_id_org

    getOrganizationsActionsByIdOrg()
    """
    params = [('entities', 'entities_example'),
                    ('display', 'display_example'),
                    ('filter', 'all'),
                    ('fields', 'all'),
                    ('limit', '50'),
                    ('format', 'list'),
                    ('since', 'since_example'),
                    ('before', 'before_example'),
                    ('page', '0'),
                    ('idModels', 'id_models_example'),
                    ('member', 'member_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('memberCreator', 'member_creator_example'),
                    ('memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/actions'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_boards_by_id_org(client):
    """Test case for get_organizations_boards_by_id_org

    getOrganizationsBoardsByIdOrg()
    """
    params = [('filter', 'all'),
                    ('fields', 'all'),
                    ('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_limit', '50'),
                    ('actions_format', 'list'),
                    ('actions_since', 'actions_since_example'),
                    ('action_fields', 'all'),
                    ('memberships', 'none'),
                    ('organization', 'organization_example'),
                    ('organization_fields', 'name and displayName'),
                    ('lists', 'none'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/boards'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_boards_by_id_org_by_filter(client):
    """Test case for get_organizations_boards_by_id_org_by_filter

    getOrganizationsBoardsByIdOrgByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/boards/{filter}'.format(id_org='id_org_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_by_id_org(client):
    """Test case for get_organizations_by_id_org

    getOrganizationsByIdOrg()
    """
    params = [('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_display', 'actions_display_example'),
                    ('actions_limit', '50'),
                    ('action_fields', 'all'),
                    ('memberships', 'none'),
                    ('memberships_member', 'memberships_member_example'),
                    ('memberships_member_fields', 'fullName and username'),
                    ('members', 'none'),
                    ('member_fields', 'avatarHash, fullName, initials, username and confirmed'),
                    ('member_activity', 'member_activity_example'),
                    ('membersInvited', 'none'),
                    ('membersInvited_fields', 'avatarHash, initials, fullName and username'),
                    ('boards', 'none'),
                    ('board_fields', 'all'),
                    ('board_actions', 'board_actions_example'),
                    ('board_actions_entities', 'board_actions_entities_example'),
                    ('board_actions_display', 'board_actions_display_example'),
                    ('board_actions_format', 'list'),
                    ('board_actions_since', 'board_actions_since_example'),
                    ('board_actions_limit', '50'),
                    ('board_action_fields', 'all'),
                    ('board_lists', 'none'),
                    ('paid_account', 'paid_account_example'),
                    ('fields', 'name, displayName, desc, descData, url, website, logoHash, products and powerUps'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_by_id_org_by_field(client):
    """Test case for get_organizations_by_id_org_by_field

    getOrganizationsByIdOrgByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/{_field}'.format(id_org='id_org_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_deltas_by_id_org(client):
    """Test case for get_organizations_deltas_by_id_org

    getOrganizationsDeltasByIdOrg()
    """
    params = [('tags', 'tags_example'),
                    ('ixLastUpdate', 'ix_last_update_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/deltas'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_members_by_id_org(client):
    """Test case for get_organizations_members_by_id_org

    getOrganizationsMembersByIdOrg()
    """
    params = [('filter', 'all'),
                    ('fields', 'fullName and username'),
                    ('activity', 'activity_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/members'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_members_by_id_org_by_filter(client):
    """Test case for get_organizations_members_by_id_org_by_filter

    getOrganizationsMembersByIdOrgByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/members/{filter}'.format(id_org='id_org_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_members_cards_by_id_org_by_id_member(client):
    """Test case for get_organizations_members_cards_by_id_org_by_id_member

    getOrganizationsMembersCardsByIdOrgByIdMember()
    """
    params = [('actions', 'actions_example'),
                    ('attachments', 'attachments_example'),
                    ('attachment_fields', 'all'),
                    ('members', 'members_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('checkItemStates', 'check_item_states_example'),
                    ('checklists', 'none'),
                    ('board', 'board_example'),
                    ('board_fields', 'name, desc, closed, idOrganization, pinned, url and prefs'),
                    ('list', 'list_example'),
                    ('list_fields', 'all'),
                    ('filter', 'visible'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/members/{id_member}/cards'.format(id_org='id_org_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_members_invited_by_id_org(client):
    """Test case for get_organizations_members_invited_by_id_org

    getOrganizationsMembersInvitedByIdOrg()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/membersInvited'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_members_invited_by_id_org_by_field(client):
    """Test case for get_organizations_members_invited_by_id_org_by_field

    getOrganizationsMembersInvitedByIdOrgByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/membersInvited/{_field}'.format(id_org='id_org_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_memberships_by_id_org(client):
    """Test case for get_organizations_memberships_by_id_org

    getOrganizationsMembershipsByIdOrg()
    """
    params = [('filter', 'all'),
                    ('member', 'member_example'),
                    ('member_fields', 'fullName and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/memberships'.format(id_org='id_org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_memberships_by_id_org_by_id_membership(client):
    """Test case for get_organizations_memberships_by_id_org_by_id_membership

    getOrganizationsMembershipsByIdOrgByIdMembership()
    """
    params = [('member', 'member_example'),
                    ('member_fields', 'fullName and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/organizations/{id_org}/memberships/{id_membership}'.format(id_org='id_org_example', id_membership='id_membership_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_by_id_org(client):
    """Test case for update_organizations_by_id_org

    updateOrganizationsByIdOrg()
    """
    body = openapi_server.Organizations()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_desc_by_id_org(client):
    """Test case for update_organizations_desc_by_id_org

    updateOrganizationsDescByIdOrg()
    """
    body = openapi_server.OrganizationsDesc()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/desc'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_display_name_by_id_org(client):
    """Test case for update_organizations_display_name_by_id_org

    updateOrganizationsDisplayNameByIdOrg()
    """
    body = openapi_server.OrganizationsDisplayName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/displayName'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_members_by_id_org(client):
    """Test case for update_organizations_members_by_id_org

    updateOrganizationsMembersByIdOrg()
    """
    body = openapi_server.OrganizationsMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/members'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_members_by_id_org_by_id_member(client):
    """Test case for update_organizations_members_by_id_org_by_id_member

    updateOrganizationsMembersByIdOrgByIdMember()
    """
    body = openapi_server.OrganizationsMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/members/{id_member}'.format(id_org='id_org_example', id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_members_deactivated_by_id_org_by_id_member(client):
    """Test case for update_organizations_members_deactivated_by_id_org_by_id_member

    updateOrganizationsMembersDeactivatedByIdOrgByIdMember()
    """
    body = openapi_server.OrganizationsMembersDeactivated()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/members/{id_member}/deactivated'.format(id_org='id_org_example', id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_memberships_by_id_org_by_id_membership(client):
    """Test case for update_organizations_memberships_by_id_org_by_id_membership

    updateOrganizationsMembershipsByIdOrgByIdMembership()
    """
    body = openapi_server.OrganizationsMemberships()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/memberships/{id_membership}'.format(id_org='id_org_example', id_membership='id_membership_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_name_by_id_org(client):
    """Test case for update_organizations_name_by_id_org

    updateOrganizationsNameByIdOrg()
    """
    body = openapi_server.OrganizationsName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/name'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_associated_domain_by_id_org(client):
    """Test case for update_organizations_prefs_associated_domain_by_id_org

    updateOrganizationsPrefsAssociatedDomainByIdOrg()
    """
    body = openapi_server.PrefsAssociatedDomain()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/associatedDomain'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_board_visibility_restrict_org_by_id_org(client):
    """Test case for update_organizations_prefs_board_visibility_restrict_org_by_id_org

    updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg()
    """
    body = openapi_server.PrefsBoardVisibilityRestrict()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/boardVisibilityRestrict/org'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_board_visibility_restrict_private_by_id_org(client):
    """Test case for update_organizations_prefs_board_visibility_restrict_private_by_id_org

    updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg()
    """
    body = openapi_server.PrefsBoardVisibilityRestrict()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/boardVisibilityRestrict/private'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_board_visibility_restrict_public_by_id_org(client):
    """Test case for update_organizations_prefs_board_visibility_restrict_public_by_id_org

    updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg()
    """
    body = openapi_server.PrefsBoardVisibilityRestrict()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/boardVisibilityRestrict/public'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_external_members_disabled_by_id_org(client):
    """Test case for update_organizations_prefs_external_members_disabled_by_id_org

    updateOrganizationsPrefsExternalMembersDisabledByIdOrg()
    """
    body = openapi_server.PrefsExternalMembersDisabled()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/externalMembersDisabled'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_google_apps_version_by_id_org(client):
    """Test case for update_organizations_prefs_google_apps_version_by_id_org

    updateOrganizationsPrefsGoogleAppsVersionByIdOrg()
    """
    body = openapi_server.PrefsGoogleAppsVersion()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/googleAppsVersion'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_org_invite_restrict_by_id_org(client):
    """Test case for update_organizations_prefs_org_invite_restrict_by_id_org

    updateOrganizationsPrefsOrgInviteRestrictByIdOrg()
    """
    body = openapi_server.PrefsOrgInviteRestrict()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/orgInviteRestrict'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_prefs_permission_level_by_id_org(client):
    """Test case for update_organizations_prefs_permission_level_by_id_org

    updateOrganizationsPrefsPermissionLevelByIdOrg()
    """
    body = openapi_server.PrefsPermissionLevel()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/prefs/permissionLevel'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organizations_website_by_id_org(client):
    """Test case for update_organizations_website_by_id_org

    updateOrganizationsWebsiteByIdOrg()
    """
    body = openapi_server.OrganizationsWebsite()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/organizations/{id_org}/website'.format(id_org='id_org_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

