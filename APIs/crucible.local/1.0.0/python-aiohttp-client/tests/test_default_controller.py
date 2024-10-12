# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_add_changeset_to_review(client):
    """Test case for add_changeset_to_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/addChangeset'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_file(client):
    """Test case for add_file

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/addFile'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_fisheye_review_item(client):
    """Test case for add_fisheye_review_item

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/reviewitems'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_general_comment(client):
    """Test case for add_general_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_patch_review0(client):
    """Test case for add_patch_review0

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/addPatch'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_patch_to_review(client):
    """Test case for add_patch_to_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/patch'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_reply(client):
    """Test case for add_reply

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}/replies'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_review_item(client):
    """Test case for add_review_item

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/details'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_review_item_revisions(client):
    """Test case for add_review_item_revisions

    
    """
    params = [('rev', 'rev_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}/revisions'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_review_items(client):
    """Test case for add_review_items

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/revisions'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_reviewers(client):
    """Test case for add_reviewers

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/reviewers'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_versioned_comment(client):
    """Test case for add_versioned_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}/comments'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_browse(client):
    """Test case for browse

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/browse/{repository}/{path}'.format(path='path_example', repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change(client):
    """Test case for change

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/change/{repository}/{revision}'.format(repository='repository_example', revision='revision_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_state(client):
    """Test case for change_state

    
    """
    params = [('action', 'action_example'),
                    ('ignoreWarnings', True)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/transition'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_changes(client):
    """Test case for changes

    
    """
    params = [('oldestCsid', 'oldest_csid_example'),
                    ('includeOldest', True),
                    ('newestCsid', 'newest_csid_example'),
                    ('includeNewest', True),
                    ('max', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/changes/{repository}/{path}'.format(path='path_example', repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_close_review_with_comment(client):
    """Test case for close_review_with_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/close'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_review(client):
    """Test case for complete_review

    
    """
    params = [('ignoreWarnings', True)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/complete'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_review(client):
    """Test case for create_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_review(client):
    """Test case for delete_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_details(client):
    """Test case for details

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/{repository}/{revision}/{path}'.format(path='path_example', repository='repository_example', revision='revision_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_comments(client):
    """Test case for get_all_comments

    
    """
    params = [('render', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/comments'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_detailed_reviews(client):
    """Test case for get_all_detailed_reviews

    
    """
    params = [('state', 'state_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_projects(client):
    """Test case for get_all_projects

    
    """
    params = [('excludeAllowedReviewers', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/projects-v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_repositories(client):
    """Test case for get_all_repositories

    
    """
    params = [('name', 'name_example'),
                    ('enabled', True),
                    ('available', True),
                    ('type', 'type_example'),
                    ('limit', 10000)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_reviews(client):
    """Test case for get_all_reviews

    
    """
    params = [('state', 'state_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_actions(client):
    """Test case for get_available_actions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/actions'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_transitions(client):
    """Test case for get_available_transitions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/transitions'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comment(client):
    """Test case for get_comment

    
    """
    params = [('render', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_completed_reviewers(client):
    """Test case for get_completed_reviewers

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/reviewers/completed'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contents(client):
    """Test case for get_contents

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/content/{repository}/{revision}/{path}'.format(path='path_example', repository='repository_example', revision='revision_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_filter_reviews(client):
    """Test case for get_custom_filter_reviews

    
    """
    params = [('title', 'title_example'),
                    ('author', 'author_example'),
                    ('moderator', 'moderator_example'),
                    ('creator', 'creator_example'),
                    ('states', 'states_example'),
                    ('reviewer', 'reviewer_example'),
                    ('orRoles', True),
                    ('complete', True),
                    ('allReviewersComplete', True),
                    ('project', 'project_example'),
                    ('fromDate', 56),
                    ('toDate', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/filter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_detailed_custom_filter_reviews(client):
    """Test case for get_detailed_custom_filter_reviews

    
    """
    params = [('title', 'title_example'),
                    ('author', 'author_example'),
                    ('moderator', 'moderator_example'),
                    ('creator', 'creator_example'),
                    ('states', 'states_example'),
                    ('reviewer', 'reviewer_example'),
                    ('orRoles', True),
                    ('complete', True),
                    ('allReviewersComplete', True),
                    ('project', 'project_example'),
                    ('fromDate', 56),
                    ('toDate', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/filter/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_detailed_filtered_reviews_for_user(client):
    """Test case for get_detailed_filtered_reviews_for_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/filter/{filter}/details'.format(filter='filter_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_detailed_review(client):
    """Test case for get_detailed_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/details'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filtered_reviews_for_user(client):
    """Test case for get_filtered_reviews_for_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/filter/{filter}'.format(filter='filter_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_general_comments(client):
    """Test case for get_general_comments

    
    """
    params = [('render', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/comments/general'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mapped_user(client):
    """Test case for get_mapped_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/users-v1/{repository}/{username}'.format(repository='repository_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metrics(client):
    """Test case for get_metrics

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/metrics/{version}'.format(version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    
    """
    params = [('excludeAllowedReviewers', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/projects-v1/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replies(client):
    """Test case for get_replies

    
    """
    params = [('render', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}/replies'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repository_details(client):
    """Test case for get_repository_details

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_review(client):
    """Test case for get_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_review_item(client):
    """Test case for get_review_item

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_review_items_comments(client):
    """Test case for get_review_items_comments

    
    """
    params = [('render', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}/comments'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_review_items_for_review(client):
    """Test case for get_review_items_for_review

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/reviewitems'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_review_patches(client):
    """Test case for get_review_patches

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/patch'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviewers(client):
    """Test case for get_reviewers

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/reviewers'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviews_details_for_path(client):
    """Test case for get_reviews_details_for_path

    
    """
    params = [('path', 'path_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/search/{repository}/details'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviews_for_issue_key(client):
    """Test case for get_reviews_for_issue_key

    
    """
    params = [('jiraKey', 'jira_key_example'),
                    ('maxReturn', 'max_return_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/search-v1/reviewsForIssue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviews_for_path(client):
    """Test case for get_reviews_for_path

    
    """
    params = [('path', 'path_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/search/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviews_for_term(client):
    """Test case for get_reviews_for_term

    
    """
    params = [('term', 'term_example'),
                    ('maxReturn', 'max_return_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/search-v1/reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_svn_repository_details(client):
    """Test case for get_svn_repository_details

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/{repository}/svn'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_uncompleted_reviewers(client):
    """Test case for get_uncompleted_reviewers

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/reviewers/uncompleted'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_profile(client):
    """Test case for get_user_profile

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/users-v1/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/users-v1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version_info(client):
    """Test case for get_version_info

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/versionInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_versioned_comments(client):
    """Test case for get_versioned_comments

    
    """
    params = [('render', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/reviews-v1/{id}/comments/versioned'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history(client):
    """Test case for history

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/repositories-v1/history/{repository}/{revision}/{path}'.format(path='path_example', repository='repository_example', revision='revision_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    
    """
    params = [('userName', 'user_name_example'),
                    ('password', 'password_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service/auth-v1/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login_post(client):
    """Test case for login_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/auth-v1/login',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_all_comments_as_read(client):
    """Test case for mark_all_comments_as_read

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments/markAllAsRead'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_comment_as_leave_unread(client):
    """Test case for mark_comment_as_leave_unread

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}/markAsLeaveUnread'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_comment_as_read(client):
    """Test case for mark_comment_as_read

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}/markAsRead'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_custom_filter_reviews(client):
    """Test case for post_custom_filter_reviews

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/filter',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_detailed_custom_filter_reviews(client):
    """Test case for post_detailed_custom_filter_reviews

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/filter/details',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_all_comments(client):
    """Test case for publish_all_comments

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/publish'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_comment(client):
    """Test case for publish_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/publish/{c_id}'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remind_incomplete_reviewers(client):
    """Test case for remind_incomplete_reviewers

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/remind'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_comment(client):
    """Test case for remove_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_patch(client):
    """Test case for remove_patch

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}/patch/{patch_id}'.format(patch_id=56, id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_reply(client):
    """Test case for remove_reply

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}/replies/{r_id}'.format(id='id_example', r_id='r_id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_review_item(client):
    """Test case for remove_review_item

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_review_item_revisions(client):
    """Test case for remove_review_item_revisions

    
    """
    params = [('rev', 'rev_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}/revisions'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_reviewer(client):
    """Test case for remove_reviewer

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/context/rest-service/reviews-v1/{id}/reviewers/{username}'.format(id='id_example', username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_review_item(client):
    """Test case for set_review_item

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/context/rest-service/reviews-v1/{id}/reviewitems/{ri_id}/details'.format(ri_id='ri_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uncomplete_review(client):
    """Test case for uncomplete_review

    
    """
    params = [('ignoreWarnings', True)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/uncomplete'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_comment(client):
    """Test case for update_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}'.format(id='id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_reply(client):
    """Test case for update_reply

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service/reviews-v1/{id}/comments/{c_id}/replies/{r_id}'.format(id='id_example', r_id='r_id_example', c_id='c_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

