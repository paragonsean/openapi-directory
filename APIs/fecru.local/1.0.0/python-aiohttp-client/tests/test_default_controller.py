# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_add_allowed_reviewer_group(client):
    """Test case for add_allowed_reviewer_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_allowed_reviewer_user(client):
    """Test case for add_allowed_reviewer_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/projects/{key}/allowed-reviewer-users'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_default_reviewer_group(client):
    """Test case for add_default_reviewer_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/projects/{key}/default-reviewer-groups'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_default_reviewer_user(client):
    """Test case for add_default_reviewer_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/projects/{key}/default-reviewer-users'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_group_to_permissions(client):
    """Test case for add_group_to_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/permissions/groups'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_permission_scheme_anonymous_users(client):
    """Test case for add_permission_scheme_anonymous_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/anonymous-users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_permission_scheme_group(client):
    """Test case for add_permission_scheme_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/groups'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_permission_scheme_logged_users(client):
    """Test case for add_permission_scheme_logged_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/logged-in-users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_permission_scheme_review_role(client):
    """Test case for add_permission_scheme_review_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/review-roles'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_permission_scheme_user(client):
    """Test case for add_permission_scheme_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_repository(client):
    """Test case for add_repository

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_allowed_reviewer_groups(client):
    """Test case for allowed_reviewer_groups

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_allowed_reviewer_users(client):
    """Test case for allowed_reviewer_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/projects/{key}/allowed-reviewer-users'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_default_permissions(client):
    """Test case for default_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/repositories/~defaults/permissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_default_reviewer_groups(client):
    """Test case for default_reviewer_groups

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/projects/{key}/default-reviewer-groups'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_allowed_reviewer_group(client):
    """Test case for delete_allowed_reviewer_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_allowed_reviewer_user(client):
    """Test case for delete_allowed_reviewer_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/projects/{key}/allowed-reviewer-users'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_default_reviewer_group(client):
    """Test case for delete_default_reviewer_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/projects/{key}/default-reviewer-groups'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_default_reviewer_user(client):
    """Test case for delete_default_reviewer_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/projects/{key}/default-reviewer-users'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_anonymous_users(client):
    """Test case for delete_permission_scheme_anonymous_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/anonymous-users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_group(client):
    """Test case for delete_permission_scheme_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/groups'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_logged_users(client):
    """Test case for delete_permission_scheme_logged_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/logged-in-users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_role(client):
    """Test case for delete_permission_scheme_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/review-roles'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_user(client):
    """Test case for delete_permission_scheme_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_repository(client):
    """Test case for delete_repository

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_repository(client):
    """Test case for disable_repository

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/disable'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_review_revision_reindex(client):
    """Test case for do_review_revision_reindex

    
    """
    params = [('synchronous', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/reindex-reviews'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_share_content(client):
    """Test case for do_share_content

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/share-content-v1/share',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_repository(client):
    """Test case for enable_repository

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/enable'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_full_incremental_index(client):
    """Test case for full_incremental_index

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/full-incremental-index'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_global_pref(client):
    """Test case for get_global_pref

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/user-prefs-v1/{_property}'.format(_property='_property_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/server-v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent(client):
    """Test case for get_recent

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_detailed(client):
    """Test case for get_recent_detailed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/detailed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_projects(client):
    """Test case for get_recent_projects

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_projects_detailed(client):
    """Test case for get_recent_projects_detailed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/projects/detailed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_repositories(client):
    """Test case for get_recent_repositories

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/repositories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_repositories_detailed(client):
    """Test case for get_recent_repositories_detailed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/repositories/detailed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_reviews(client):
    """Test case for get_recent_reviews

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/reviews',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_reviews_detailed(client):
    """Test case for get_recent_reviews_detailed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/reviews/detailed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_snippets(client):
    """Test case for get_recent_snippets

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/snippets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_snippets_detailed(client):
    """Test case for get_recent_snippets_detailed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/snippets/detailed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_users(client):
    """Test case for get_recent_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recent_users_detailed(client):
    """Test case for get_recent_users_detailed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/recently-visited-v1/users/detailed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repo_pref(client):
    """Test case for get_repo_pref

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/user-prefs-v1/{repository}/{_property}'.format(_property='_property_example', repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_incremental_index(client):
    """Test case for incremental_index

    
    """
    params = [('wait', False)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/incremental-index'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_anonymous_users_principal_association(client):
    """Test case for list_anonymous_users_principal_association

    
    """
    params = [('action', 'action_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/anonymous-users'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_default_reviewer_users(client):
    """Test case for list_default_reviewer_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/projects/{key}/default-reviewer-users'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_group_principal_association(client):
    """Test case for list_group_principal_association

    
    """
    params = [('name2', 'name_example'),
                    ('action', 'action_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/groups'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_group_users(client):
    """Test case for list_group_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/groups/{name}/users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_logged_users_principal_association(client):
    """Test case for list_logged_users_principal_association

    
    """
    params = [('action', 'action_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/logged-in-users'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_projects(client):
    """Test case for list_projects

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/projects'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_roles_principal_association(client):
    """Test case for list_roles_principal_association

    
    """
    params = [('name2', 'name_example'),
                    ('action', 'action_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/review-roles'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_groups(client):
    """Test case for list_user_groups

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/users/{name}/groups'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_user_principal_association(client):
    """Test case for list_user_principal_association

    
    """
    params = [('name2', 'name_example'),
                    ('action', 'action_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}/users'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/auth/login',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_all_reviews(client):
    """Test case for move_all_reviews

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/projects/{source_project_key}/move-reviews/{destination_project_key}'.format(source_project_key='source_project_key_example', destination_project_key='destination_project_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions(client):
    """Test case for permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/repositories/{repository}/permissions'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_groups(client):
    """Test case for permissions_groups

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/repositories/{repository}/permissions/groups'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rebuild_search_index(client):
    """Test case for rebuild_search_index

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/reindex-search'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex_changeset_comments(client):
    """Test case for reindex_changeset_comments

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/reindex-discussions'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex_changeset_discussion(client):
    """Test case for reindex_changeset_discussion

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/reindex-changeset-discussion'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex_reviews(client):
    """Test case for reindex_reviews

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/reindex-reviews'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex_search(client):
    """Test case for reindex_search

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/reindex-search'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group_to_permissions(client):
    """Test case for remove_group_to_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/repositories/{repository}/permissions/groups'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repository_updates(client):
    """Test case for repository_updates

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/repositories/{repository}/updates'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_get(client):
    """Test case for rest_service_fecru_admin_groups_get

    
    """
    params = [('prefix', 'prefix_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_name_delete(client):
    """Test case for rest_service_fecru_admin_groups_name_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/groups/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_name_get(client):
    """Test case for rest_service_fecru_admin_groups_name_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/groups/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_name_put(client):
    """Test case for rest_service_fecru_admin_groups_name_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/groups/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_name_users_delete(client):
    """Test case for rest_service_fecru_admin_groups_name_users_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/groups/{name}/users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_name_users_put(client):
    """Test case for rest_service_fecru_admin_groups_name_users_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/groups/{name}/users'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_groups_post(client):
    """Test case for rest_service_fecru_admin_groups_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_permission_schemes_get(client):
    """Test case for rest_service_fecru_admin_permission_schemes_get

    
    """
    params = [('name', 'name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_permission_schemes_name_delete(client):
    """Test case for rest_service_fecru_admin_permission_schemes_name_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_permission_schemes_name_get(client):
    """Test case for rest_service_fecru_admin_permission_schemes_name_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_permission_schemes_name_put(client):
    """Test case for rest_service_fecru_admin_permission_schemes_name_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/permission-schemes/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_permission_schemes_post(client):
    """Test case for rest_service_fecru_admin_permission_schemes_post

    
    """
    params = [('copyFrom', 'copy_from_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/permission-schemes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_projects_get(client):
    """Test case for rest_service_fecru_admin_projects_get

    
    """
    params = [('name', 'name_example'),
                    ('key', 'key_example'),
                    ('defaultRepositoryName', 'default_repository_name_example'),
                    ('permissionSchemeName', 'permission_scheme_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_projects_key_delete(client):
    """Test case for rest_service_fecru_admin_projects_key_delete

    
    """
    params = [('deleteProjectReviews', False)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/projects/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_projects_key_get(client):
    """Test case for rest_service_fecru_admin_projects_key_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/projects/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_projects_key_put(client):
    """Test case for rest_service_fecru_admin_projects_key_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/projects/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_projects_post(client):
    """Test case for rest_service_fecru_admin_projects_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_get(client):
    """Test case for rest_service_fecru_admin_repositories_get

    
    """
    params = [('type', 'type_example'),
                    ('enabled', True),
                    ('started', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/repositories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_post(client):
    """Test case for rest_service_fecru_admin_repositories_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_repository_delete(client):
    """Test case for rest_service_fecru_admin_repositories_repository_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/repositories/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_repository_get(client):
    """Test case for rest_service_fecru_admin_repositories_repository_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/repositories/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_repository_put(client):
    """Test case for rest_service_fecru_admin_repositories_repository_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_repository_reindex_linecount_put(client):
    """Test case for rest_service_fecru_admin_repositories_repository_reindex_linecount_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/reindex-linecount'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_repository_reindex_source_put(client):
    """Test case for rest_service_fecru_admin_repositories_repository_reindex_source_put

    
    """
    params = [('clone', False)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/reindex-source'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_repository_rescan_metadata_put(client):
    """Test case for rest_service_fecru_admin_repositories_repository_rescan_metadata_put

    
    """
    params = [('from', '_from_example'),
                    ('to', 'to_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/rescan-metadata'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_v1_repository_reindex_linecount_post(client):
    """Test case for rest_service_fecru_admin_repositories_v1_repository_reindex_linecount_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/reindex-linecount'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_v1_repository_reindex_source_post(client):
    """Test case for rest_service_fecru_admin_repositories_v1_repository_reindex_source_post

    
    """
    params = [('clone', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/reindex-source'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_repositories_v1_repository_rescan_metadata_post(client):
    """Test case for rest_service_fecru_admin_repositories_v1_repository_rescan_metadata_post

    
    """
    params = [('from', 56),
                    ('to', 56)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/rescan-metadata'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_get(client):
    """Test case for rest_service_fecru_admin_users_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/users/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_name_delete(client):
    """Test case for rest_service_fecru_admin_users_name_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/users/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_name_get(client):
    """Test case for rest_service_fecru_admin_users_name_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/admin/users/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_name_groups_delete(client):
    """Test case for rest_service_fecru_admin_users_name_groups_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service-fecru/admin/users/{name}/groups'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_name_groups_put(client):
    """Test case for rest_service_fecru_admin_users_name_groups_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/users/{name}/groups'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_name_put(client):
    """Test case for rest_service_fecru_admin_users_name_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/users/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_admin_users_post(client):
    """Test case for rest_service_fecru_admin_users_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/users/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_service_fecru_indexing_status_v1_status_repository_get(client):
    """Test case for rest_service_fecru_indexing_status_v1_status_repository_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fecru/indexing-status-v1/status/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scan(client):
    """Test case for scan

    
    """
    params = [('synchronous', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/scan'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scan_cvs(client):
    """Test case for scan_cvs

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/scan-cvs'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_pref(client):
    """Test case for set_pref

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/user-prefs-v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start(client):
    """Test case for start

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/start'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_repository(client):
    """Test case for start_repository

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/start'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop(client):
    """Test case for stop

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/stop'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_repository(client):
    """Test case for stop_repository

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fecru/admin/repositories-v1/{repository}/stop'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_default_permissions(client):
    """Test case for update_default_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/~defaults/permissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_permissions(client):
    """Test case for update_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/permissions'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_repository_updates(client):
    """Test case for update_repository_updates

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service-fecru/admin/repositories/{repository}/updates'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

