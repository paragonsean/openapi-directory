# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_acknowledge_errors(client):
    """Test case for acknowledge_errors

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/cluster/zdu/retryUpgrade',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_actor_users(client):
    """Test case for add_actor_users

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_attachment(client):
    """Test case for add_attachment

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/attachments'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_comment(client):
    """Test case for add_comment

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/comment'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_field(client):
    """Test case for add_field

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}/fields'.format(screen_id=56, tab_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_field_to_default_screen(client):
    """Test case for add_field_to_default_screen

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/screens/addToDefault/{field_id}'.format(field_id='field_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_project_role_actors_to_role(client):
    """Test case for add_project_role_actors_to_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/role/{id}/actors'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_record(client):
    """Test case for add_record

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/auditing/record',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_share_permission(client):
    """Test case for add_share_permission

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/filter/{id}/permission'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_tab(client):
    """Test case for add_tab

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/screens/{screen_id}/tabs'.format(screen_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_user_to_application(client):
    """Test case for add_user_to_application

    
    """
    params = [('username', 'username_example'),
                    ('applicationKey', 'application_key_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/user/application',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_user_to_group(client):
    """Test case for add_user_to_group

    
    """
    params = [('groupname', 'groupname_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/group/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_vote(client):
    """Test case for add_vote

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/votes'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_watcher(client):
    """Test case for add_watcher

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/watchers'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_worklog(client):
    """Test case for add_worklog

    
    """
    params = [('adjustEstimate', 'adjust_estimate_example'),
                    ('newEstimate', 'new_estimate_example'),
                    ('reduceBy', 'reduce_by_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/worklog'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_application_properties_get(client):
    """Test case for api2_application_properties_get

    
    """
    params = [('key', 'key_example'),
                    ('permissionLevel', 'permission_level_example'),
                    ('keyFilter', 'key_filter_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/application-properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_avatar_type_temporary_crop_post(client):
    """Test case for api2_avatar_type_temporary_crop_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/avatar/{type}/temporaryCrop'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_comment_comment_id_properties_get(client):
    """Test case for api2_comment_comment_id_properties_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/comment/{comment_id}/properties'.format(comment_id='comment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_comment_comment_id_properties_property_key_delete(client):
    """Test case for api2_comment_comment_id_properties_property_key_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/comment/{comment_id}/properties/{property_key}'.format(comment_id='comment_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_comment_comment_id_properties_property_key_get(client):
    """Test case for api2_comment_comment_id_properties_property_key_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/comment/{comment_id}/properties/{property_key}'.format(comment_id='comment_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_comment_comment_id_properties_property_key_put(client):
    """Test case for api2_comment_comment_id_properties_property_key_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/comment/{comment_id}/properties/{property_key}'.format(comment_id='comment_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_component_id_delete(client):
    """Test case for api2_component_id_delete

    
    """
    params = [('moveIssuesTo', 'move_issues_to_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/component/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_dashboard_dashboard_id_items_item_id_properties_get(client):
    """Test case for api2_dashboard_dashboard_id_items_item_id_properties_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/dashboard/{dashboard_id}/items/{item_id}/properties'.format(item_id='item_id_example', dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_dashboard_dashboard_id_items_item_id_properties_property_key_delete(client):
    """Test case for api2_dashboard_dashboard_id_items_item_id_properties_property_key_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}'.format(item_id='item_id_example', dashboard_id='dashboard_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_dashboard_dashboard_id_items_item_id_properties_property_key_get(client):
    """Test case for api2_dashboard_dashboard_id_items_item_id_properties_property_key_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}'.format(item_id='item_id_example', dashboard_id='dashboard_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_dashboard_dashboard_id_items_item_id_properties_property_key_put(client):
    """Test case for api2_dashboard_dashboard_id_items_item_id_properties_property_key_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}'.format(item_id='item_id_example', dashboard_id='dashboard_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_filter_id_columns_delete(client):
    """Test case for api2_filter_id_columns_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/filter/{id}/columns'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_filter_id_columns_get(client):
    """Test case for api2_filter_id_columns_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/filter/{id}/columns'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_filter_id_columns_put(client):
    """Test case for api2_filter_id_columns_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/filter/{id}/columns'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issue_issue_id_or_key_properties_get(client):
    """Test case for api2_issue_issue_id_or_key_properties_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/properties'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issue_issue_id_or_key_properties_property_key_delete(client):
    """Test case for api2_issue_issue_id_or_key_properties_property_key_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issue_issue_id_or_key_properties_property_key_get(client):
    """Test case for api2_issue_issue_id_or_key_properties_property_key_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issue_issue_id_or_key_properties_property_key_put(client):
    """Test case for api2_issue_issue_id_or_key_properties_property_key_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/properties/{property_key}'.format(issue_id_or_key='issue_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuesecurityschemes_id_get(client):
    """Test case for api2_issuesecurityschemes_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuesecurityschemes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_id_avatar_post(client):
    """Test case for api2_issuetype_id_avatar_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issuetype/{id}/avatar'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_id_avatar_temporary_post(client):
    """Test case for api2_issuetype_id_avatar_temporary_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issuetype/{id}/avatar/temporary'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_id_delete(client):
    """Test case for api2_issuetype_id_delete

    
    """
    params = [('alternativeIssueTypeId', 'alternative_issue_type_id_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issuetype/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_id_get(client):
    """Test case for api2_issuetype_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuetype/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_issue_type_id_properties_property_key_delete(client):
    """Test case for api2_issuetype_issue_type_id_properties_property_key_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issuetype/{issue_type_id}/properties/{property_key}'.format(issue_type_id='issue_type_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_issue_type_id_properties_property_key_get(client):
    """Test case for api2_issuetype_issue_type_id_properties_property_key_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuetype/{issue_type_id}/properties/{property_key}'.format(issue_type_id='issue_type_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_issuetype_issue_type_id_properties_property_key_put(client):
    """Test case for api2_issuetype_issue_type_id_properties_property_key_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issuetype/{issue_type_id}/properties/{property_key}'.format(issue_type_id='issue_type_id_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_myself_get(client):
    """Test case for api2_myself_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/myself',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_myself_put(client):
    """Test case for api2_myself_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/myself',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_notificationscheme_id_get(client):
    """Test case for api2_notificationscheme_id_get

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/notificationscheme/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_avatar_id_delete(client):
    """Test case for api2_project_project_id_or_key_avatar_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/project/{project_id_or_key}/avatar/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_avatar_post(client):
    """Test case for api2_project_project_id_or_key_avatar_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/project/{project_id_or_key}/avatar'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_avatar_put(client):
    """Test case for api2_project_project_id_or_key_avatar_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/project/{project_id_or_key}/avatar'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_avatar_temporary_post(client):
    """Test case for api2_project_project_id_or_key_avatar_temporary_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/project/{project_id_or_key}/avatar/temporary'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_avatars_get(client):
    """Test case for api2_project_project_id_or_key_avatars_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/avatars'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_get(client):
    """Test case for api2_project_project_id_or_key_get

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_properties_get(client):
    """Test case for api2_project_project_id_or_key_properties_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/properties'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_properties_property_key_delete(client):
    """Test case for api2_project_project_id_or_key_properties_property_key_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/project/{project_id_or_key}/properties/{property_key}'.format(project_id_or_key='project_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_properties_property_key_get(client):
    """Test case for api2_project_project_id_or_key_properties_property_key_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/properties/{property_key}'.format(project_id_or_key='project_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_properties_property_key_put(client):
    """Test case for api2_project_project_id_or_key_properties_property_key_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/project/{project_id_or_key}/properties/{property_key}'.format(project_id_or_key='project_id_or_key_example', property_key='property_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_id_or_key_role_get(client):
    """Test case for api2_project_project_id_or_key_role_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/role'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_key_or_id_issuesecuritylevelscheme_get(client):
    """Test case for api2_project_project_key_or_id_issuesecuritylevelscheme_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_key_or_id}/issuesecuritylevelscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_project_project_key_or_id_notificationscheme_get(client):
    """Test case for api2_project_project_key_or_id_notificationscheme_get

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_key_or_id}/notificationscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_projectvalidate_key_get(client):
    """Test case for api2_projectvalidate_key_get

    
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/projectvalidate/key',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_role_get(client):
    """Test case for api2_role_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/role',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_universal_avatar_type_type_owner_owning_object_id_avatar_id_delete(client):
    """Test case for api2_universal_avatar_type_type_owner_owning_object_id_avatar_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/universal_avatar/type/{type}/owner/{owning_object_id}/avatar/{id}'.format(id=56, type='type_example', owning_object_id='owning_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_universal_avatar_type_type_owner_owning_object_id_avatar_post(client):
    """Test case for api2_universal_avatar_type_type_owner_owning_object_id_avatar_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/universal_avatar/type/{type}/owner/{owning_object_id}/avatar'.format(type='type_example', owning_object_id='owning_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_universal_avatar_type_type_owner_owning_object_id_temp_post(client):
    """Test case for api2_universal_avatar_type_type_owner_owning_object_id_temp_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/universal_avatar/type/{type}/owner/{owning_object_id}/temp'.format(type='type_example', owning_object_id='owning_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_avatar_id_delete(client):
    """Test case for api2_user_avatar_id_delete

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/user/avatar/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_avatar_post(client):
    """Test case for api2_user_avatar_post

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/user/avatar',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_avatar_put(client):
    """Test case for api2_user_avatar_put

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/user/avatar',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_avatar_temporary_post(client):
    """Test case for api2_user_avatar_temporary_post

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/user/avatar/temporary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_avatars_get(client):
    """Test case for api2_user_avatars_get

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/avatars',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_columns_delete(client):
    """Test case for api2_user_columns_delete

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/user/columns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_columns_get(client):
    """Test case for api2_user_columns_get

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/columns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_columns_put(client):
    """Test case for api2_user_columns_put

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/user/columns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_get(client):
    """Test case for api2_user_get

    
    """
    params = [('username', 'username_example'),
                    ('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_properties_get(client):
    """Test case for api2_user_properties_get

    
    """
    params = [('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/properties/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_properties_property_key_delete(client):
    """Test case for api2_user_properties_property_key_delete

    
    """
    params = [('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/user/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_properties_property_key_get(client):
    """Test case for api2_user_properties_property_key_get

    
    """
    params = [('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_properties_property_key_put(client):
    """Test case for api2_user_properties_property_key_put

    
    """
    params = [('userKey', 'user_key_example'),
                    ('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/user/properties/{property_key}'.format(property_key='property_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_user_put(client):
    """Test case for api2_user_put

    
    """
    params = [('username', 'username_example'),
                    ('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_version_id_delete(client):
    """Test case for api2_version_id_delete

    
    """
    params = [('moveFixIssuesTo', 'move_fix_issues_to_example'),
                    ('moveAffectedIssuesTo', 'move_affected_issues_to_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/version/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_version_id_remove_and_swap_post(client):
    """Test case for api2_version_id_remove_and_swap_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/version/{id}/removeAndSwap'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_version_version_id_remotelink_global_id_post(client):
    """Test case for api2_version_version_id_remotelink_global_id_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/version/{version_id}/remotelink/{global_id}'.format(version_id='version_id_example', global_id='global_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_version_version_id_remotelink_post(client):
    """Test case for api2_version_version_id_remotelink_post

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/version/{version_id}/remotelink'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_workflow_api2_transitions_id_properties_delete(client):
    """Test case for api2_workflow_api2_transitions_id_properties_delete

    
    """
    params = [('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', 'workflow_mode_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflow/api/2/transitions/{id}/properties'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_workflowscheme_id_issuetype_issue_type_delete(client):
    """Test case for api2_workflowscheme_id_issuetype_issue_type_delete

    
    """
    params = [('updateDraftIfNeeded', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/issuetype/{issue_type}'.format(issue_type='issue_type_example', id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api2_workflowscheme_id_issuetype_issue_type_get(client):
    """Test case for api2_workflowscheme_id_issuetype_issue_type_get

    
    """
    params = [('returnDraftIfExists', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/issuetype/{issue_type}'.format(issue_type='issue_type_example', id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_approve_upgrade(client):
    """Test case for approve_upgrade

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/cluster/zdu/approve',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_are_metrics_exposed(client):
    """Test case for are_metrics_exposed

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/monitoring/jmx/areMetricsExposed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign(client):
    """Test case for assign

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/assignee'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_assign_permission_scheme(client):
    """Test case for assign_permission_scheme

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/project/{project_key_or_id}/permissionscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_can_move_sub_task(client):
    """Test case for can_move_sub_task

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/subtask/move'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_upgrade(client):
    """Test case for cancel_upgrade

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/cluster/zdu/cancel',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_my_password(client):
    """Test case for change_my_password

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/myself/password',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_user_password(client):
    """Test case for change_user_password

    
    """
    params = [('username', 'username_example'),
                    ('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/user/password',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_component(client):
    """Test case for create_component

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/component',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_custom_field(client):
    """Test case for create_custom_field

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/field',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_draft_for_parent(client):
    """Test case for create_draft_for_parent

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/workflowscheme/{id}/createdraft'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_filter(client):
    """Test case for create_filter

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/filter',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/group',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue(client):
    """Test case for create_issue

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue_link_type(client):
    """Test case for create_issue_link_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issueLinkType',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issue_type(client):
    """Test case for create_issue_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issuetype',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_issues(client):
    """Test case for create_issues

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/bulk',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_or_update_remote_issue_link(client):
    """Test case for create_or_update_remote_issue_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/remotelink'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_permission_grant(client):
    """Test case for create_permission_grant

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}/permission'.format(scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_permission_scheme(client):
    """Test case for create_permission_scheme

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/permissionscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_project(client):
    """Test case for create_project

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/project',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_project_category(client):
    """Test case for create_project_category

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/projectCategory',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_project_role(client):
    """Test case for create_project_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/role',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_property(client):
    """Test case for create_property

    
    """
    params = [('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', 'workflow_mode_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/workflow/api/2/transitions/{id}/properties'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_scheme(client):
    """Test case for create_scheme

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/workflowscheme',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_version(client):
    """Test case for create_version

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_current_user(client):
    """Test case for current_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/auth/1/session',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_actor(client):
    """Test case for delete_actor

    
    """
    params = [('user', 'user_example'),
                    ('group', 'group_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_comment(client):
    """Test case for delete_comment

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/comment/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_default(client):
    """Test case for delete_default

    
    """
    params = [('updateDraftIfNeeded', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/default'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_draft_by_id(client):
    """Test case for delete_draft_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/draft'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_draft_default(client):
    """Test case for delete_draft_default

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/default'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_draft_issue_type(client):
    """Test case for delete_draft_issue_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/issuetype/{issue_type}'.format(issue_type='issue_type_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_draft_workflow_mapping(client):
    """Test case for delete_draft_workflow_mapping

    
    """
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_filter(client):
    """Test case for delete_filter

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/filter/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue(client):
    """Test case for delete_issue

    
    """
    params = [('deleteSubtasks', 'delete_subtasks_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_link(client):
    """Test case for delete_issue_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issueLink/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_issue_link_type(client):
    """Test case for delete_issue_link_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issueLinkType/{issue_link_type_id}'.format(issue_link_type_id='issue_link_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme(client):
    """Test case for delete_permission_scheme

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}'.format(scheme_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_entity(client):
    """Test case for delete_permission_scheme_entity

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}/permission/{permission_id}'.format(permission_id=56, scheme_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/project/{project_id_or_key}'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_role(client):
    """Test case for delete_project_role

    
    """
    params = [('swap', 56)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/role/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_role_actors_from_role(client):
    """Test case for delete_project_role_actors_from_role

    
    """
    params = [('user', 'user_example'),
                    ('group', 'group_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/role/{id}/actors'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_issue_link_by_global_id(client):
    """Test case for delete_remote_issue_link_by_global_id

    
    """
    params = [('globalId', 'global_id_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/remotelink'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_issue_link_by_id(client):
    """Test case for delete_remote_issue_link_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/remotelink/{link_id}'.format(link_id='link_id_example', issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_version_link(client):
    """Test case for delete_remote_version_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/version/{version_id}/remotelink/{global_id}'.format(version_id='version_id_example', global_id='global_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_remote_version_links_by_version_id(client):
    """Test case for delete_remote_version_links_by_version_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/version/{version_id}/remotelink'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_scheme(client):
    """Test case for delete_scheme

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tab(client):
    """Test case for delete_tab

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}'.format(screen_id=56, tab_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow_mapping(client):
    """Test case for delete_workflow_mapping

    
    """
    params = [('workflowName', 'workflow_name_example'),
                    ('updateDraftIfNeeded', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/workflowscheme/{id}/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_worklog(client):
    """Test case for delete_worklog

    
    """
    params = [('adjustEstimate', 'adjust_estimate_example'),
                    ('newEstimate', 'new_estimate_example'),
                    ('increaseBy', 'increase_by_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/worklog/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_transition(client):
    """Test case for do_transition

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/transitions'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_filter(client):
    """Test case for edit_filter

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/filter/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_issue(client):
    """Test case for edit_issue

    
    """
    params = [('notifyUsers', True)]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issue/{issue_id_or_key}'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expand_for_humans(client):
    """Test case for expand_for_humans

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/attachment/{id}/expand/human'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expand_for_machines(client):
    """Test case for expand_for_machines

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/attachment/{id}/expand/raw'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_assignable_users(client):
    """Test case for find_assignable_users

    
    """
    params = [('username', 'username_example'),
                    ('project', 'project_example'),
                    ('issueKey', 'issue_key_example'),
                    ('startAt', 56),
                    ('maxResults', 56),
                    ('actionDescriptorId', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/assignable/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_bulk_assignable_users(client):
    """Test case for find_bulk_assignable_users

    
    """
    params = [('username', 'username_example'),
                    ('projectKeys', 'project_keys_example'),
                    ('startAt', 56),
                    ('maxResults', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/assignable/multiProjectSearch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_groups(client):
    """Test case for find_groups

    
    """
    params = [('query', 'query_example'),
                    ('exclude', 'exclude_example'),
                    ('maxResults', 56),
                    ('userName', 'user_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/groups/picker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users(client):
    """Test case for find_users

    
    """
    params = [('username', 'username_example'),
                    ('startAt', 56),
                    ('maxResults', 56),
                    ('includeActive', True),
                    ('includeInactive', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_and_groups(client):
    """Test case for find_users_and_groups

    
    """
    params = [('query', 'query_example'),
                    ('maxResults', 56),
                    ('showAvatar', True),
                    ('fieldId', 'field_id_example'),
                    ('projectId', 'project_id_example'),
                    ('issueTypeId', 'issue_type_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/groupuserpicker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_for_picker(client):
    """Test case for find_users_for_picker

    
    """
    params = [('query', 'query_example'),
                    ('maxResults', 56),
                    ('showAvatar', True),
                    ('exclude', 'exclude_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/picker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_with_all_permissions(client):
    """Test case for find_users_with_all_permissions

    
    """
    params = [('username', 'username_example'),
                    ('permissions', 'permissions_example'),
                    ('issueKey', 'issue_key_example'),
                    ('projectKey', 'project_key_example'),
                    ('startAt', 56),
                    ('maxResults', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/permission/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users_with_browse_permission(client):
    """Test case for find_users_with_browse_permission

    
    """
    params = [('username', 'username_example'),
                    ('issueKey', 'issue_key_example'),
                    ('projectKey', 'project_key_example'),
                    ('startAt', 56),
                    ('maxResults', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/user/viewissue/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fully_update_project_role(client):
    """Test case for fully_update_project_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/role/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get(client):
    """Test case for get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/applicationrole/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_accessible_project_type_by_key(client):
    """Test case for get_accessible_project_type_by_key

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/type/{project_type_key}/accessible'.format(project_type_key='project_type_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_advanced_settings(client):
    """Test case for get_advanced_settings

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/application-properties/advanced-settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all(client):
    """Test case for get_all

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/applicationrole',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_fields(client):
    """Test case for get_all_fields

    
    """
    params = [('projectKey', 'project_key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}/fields'.format(screen_id=56, tab_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_permissions(client):
    """Test case for get_all_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/permissions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_project_categories(client):
    """Test case for get_all_project_categories

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/projectCategory',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_project_types(client):
    """Test case for get_all_project_types

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/type',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_projects(client):
    """Test case for get_all_projects

    
    """
    params = [('expand', 'expand_example'),
                    ('recent', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_statuses(client):
    """Test case for get_all_statuses

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/statuses'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_system_avatars(client):
    """Test case for get_all_system_avatars

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/avatar/{type}/system'.format(type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_tabs(client):
    """Test case for get_all_tabs

    
    """
    params = [('projectKey', 'project_key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/screens/{screen_id}/tabs'.format(screen_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_workflows(client):
    """Test case for get_all_workflows

    
    """
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflow',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_alternative_issue_types(client):
    """Test case for get_alternative_issue_types

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuetype/{id}/alternatives'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_assigned_permission_scheme(client):
    """Test case for get_assigned_permission_scheme

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_key_or_id}/permissionscheme'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attachment(client):
    """Test case for get_attachment

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/attachment/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attachment_meta(client):
    """Test case for get_attachment_meta

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/attachment/meta',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_auto_complete(client):
    """Test case for get_auto_complete

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/jql/autocompletedata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_metrics(client):
    """Test case for get_available_metrics

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/monitoring/jmx/getAvailableMetrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_avatars(client):
    """Test case for get_avatars

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/universal_avatar/type/{type}/owner/{owning_object_id}'.format(type='type_example', owning_object_id='owning_object_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id(client):
    """Test case for get_by_id

    
    """
    params = [('returnDraftIfExists', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comment(client):
    """Test case for get_comment

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/comment/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments(client):
    """Test case for get_comments

    
    """
    params = [('startAt', 56),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/comment'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_component(client):
    """Test case for get_component

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/component/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_component_related_issues(client):
    """Test case for get_component_related_issues

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/component/{id}/relatedIssueCounts'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_configuration(client):
    """Test case for get_configuration

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_create_issue_meta(client):
    """Test case for get_create_issue_meta

    
    """
    params = [('projectIds', 'project_ids_example'),
                    ('projectKeys', 'project_keys_example'),
                    ('issuetypeIds', 'issuetype_ids_example'),
                    ('issuetypeNames', 'issuetype_names_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/createmeta',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_field_option(client):
    """Test case for get_custom_field_option

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/customFieldOption/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dashboard(client):
    """Test case for get_dashboard

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/dashboard/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default(client):
    """Test case for get_default

    
    """
    params = [('returnDraftIfExists', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/default'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_share_scope(client):
    """Test case for get_default_share_scope

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/filter/defaultShareScope',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_draft_by_id(client):
    """Test case for get_draft_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/draft'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_draft_default(client):
    """Test case for get_draft_default

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/default'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_draft_issue_type(client):
    """Test case for get_draft_issue_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/issuetype/{issue_type}'.format(issue_type='issue_type_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_draft_workflow(client):
    """Test case for get_draft_workflow

    
    """
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_edit_issue_meta(client):
    """Test case for get_edit_issue_meta

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/editmeta'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_favourite_filters(client):
    """Test case for get_favourite_filters

    
    """
    params = [('expand', 'expand_example'),
                    ('enableSharedUsers', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/filter/favourite',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_field_auto_complete_for_query_string(client):
    """Test case for get_field_auto_complete_for_query_string

    
    """
    params = [('fieldName', 'field_name_example'),
                    ('fieldValue', 'field_value_example'),
                    ('predicateName', 'predicate_name_example'),
                    ('predicateValue', 'predicate_value_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/jql/autocompletedata/suggestions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields(client):
    """Test case for get_fields

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/field',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_fields_to_add(client):
    """Test case for get_fields_to_add

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/screens/{screen_id}/availableFields'.format(screen_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filter(client):
    """Test case for get_filter

    
    """
    params = [('expand', 'expand_example'),
                    ('enableSharedUsers', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/filter/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group(client):
    """Test case for get_group

    
    """
    params = [('groupname', 'groupname_example'),
                    ('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ids_of_worklogs_deleted_since(client):
    """Test case for get_ids_of_worklogs_deleted_since

    
    """
    params = [('since', 0)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/worklog/deleted',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ids_of_worklogs_modified_since(client):
    """Test case for get_ids_of_worklogs_modified_since

    
    """
    params = [('since', 0)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/worklog/updated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_index_summary(client):
    """Test case for get_index_summary

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/index/summary',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue(client):
    """Test case for get_issue

    
    """
    params = [('fields', 'fields_example'),
                    ('expand', 'expand_example'),
                    ('properties', 'properties_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_all_types(client):
    """Test case for get_issue_all_types

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuetype',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_link(client):
    """Test case for get_issue_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issueLink/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_link_type(client):
    """Test case for get_issue_link_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issueLinkType/{issue_link_type_id}'.format(issue_link_type_id='issue_link_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_link_types(client):
    """Test case for get_issue_link_types

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issueLinkType',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_navigator_default_columns(client):
    """Test case for get_issue_navigator_default_columns

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/settings/columns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_picker_resource(client):
    """Test case for get_issue_picker_resource

    
    """
    params = [('query', 'query_example'),
                    ('currentJQL', 'current_jql_example'),
                    ('currentIssueKey', 'current_issue_key_example'),
                    ('currentProjectId', 'current_project_id_example'),
                    ('showSubTasks', True),
                    ('showSubTaskParent', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/picker',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_security_schemes(client):
    """Test case for get_issue_security_schemes

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuesecurityschemes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_watchers(client):
    """Test case for get_issue_watchers

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/watchers'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_worklog(client):
    """Test case for get_issue_worklog

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/worklog'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issuesecuritylevel(client):
    """Test case for get_issuesecuritylevel

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/securitylevel/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_schemes(client):
    """Test case for get_notification_schemes

    
    """
    params = [('startAt', 56),
                    ('maxResults', 56),
                    ('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/notificationscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_password_policy(client):
    """Test case for get_password_policy

    
    """
    params = [('hasOldPassword', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/password/policy',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_scheme(client):
    """Test case for get_permission_scheme

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}'.format(scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_scheme_grant(client):
    """Test case for get_permission_scheme_grant

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}/permission/{permission_id}'.format(permission_id=56, scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_scheme_grants(client):
    """Test case for get_permission_scheme_grants

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}/permission'.format(scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_schemes(client):
    """Test case for get_permission_schemes

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/permissionscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permissions(client):
    """Test case for get_permissions

    
    """
    params = [('projectKey', 'project_key_example'),
                    ('projectId', 'project_id_example'),
                    ('issueKey', 'issue_key_example'),
                    ('issueId', 'issue_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/mypermissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_preference(client):
    """Test case for get_preference

    
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/mypreferences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_priorities(client):
    """Test case for get_priorities

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/priority',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_priority(client):
    """Test case for get_priority

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/priority/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_progress(client):
    """Test case for get_progress

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/reindex/request/{request_id}'.format(request_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_progress_bulk(client):
    """Test case for get_progress_bulk

    
    """
    params = [('requestId', 'request_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/reindex/request/bulk',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_category_by_id(client):
    """Test case for get_project_category_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/projectCategory/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_components(client):
    """Test case for get_project_components

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/components'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_role(client):
    """Test case for get_project_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_role_actors_for_role(client):
    """Test case for get_project_role_actors_for_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/role/{id}/actors'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_roles_by_id(client):
    """Test case for get_project_roles_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/role/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_type_by_key(client):
    """Test case for get_project_type_by_key

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/type/{project_type_key}'.format(project_type_key='project_type_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_versions(client):
    """Test case for get_project_versions

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/versions'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_versions_paginated(client):
    """Test case for get_project_versions_paginated

    
    """
    params = [('startAt', 56),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_id_or_key}/version'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_properties(client):
    """Test case for get_properties

    
    """
    params = [('includeReservedKeys', True),
                    ('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', 'workflow_mode_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflow/api/2/transitions/{id}/properties'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_property_keys(client):
    """Test case for get_property_keys

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issuetype/{issue_type_id}/properties'.format(issue_type_id='issue_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_records(client):
    """Test case for get_records

    
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example'),
                    ('projectIds', 'project_ids_example'),
                    ('userIds', 'user_ids_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/auditing/record',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reindex_info(client):
    """Test case for get_reindex_info

    
    """
    params = [('taskId', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/reindex',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reindex_progress(client):
    """Test case for get_reindex_progress

    
    """
    params = [('taskId', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/reindex/progress',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_issue_link_by_id(client):
    """Test case for get_remote_issue_link_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/remotelink/{link_id}'.format(link_id='link_id_example', issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_issue_links(client):
    """Test case for get_remote_issue_links

    
    """
    params = [('globalId', 'global_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/remotelink'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_version_link(client):
    """Test case for get_remote_version_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/version/{version_id}/remotelink/{global_id}'.format(version_id='version_id_example', global_id='global_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_version_links(client):
    """Test case for get_remote_version_links

    
    """
    params = [('globalId', 'global_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/version/remotelink',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_version_links_by_version_id(client):
    """Test case for get_remote_version_links_by_version_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/version/{version_id}/remotelink'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_resolution(client):
    """Test case for get_resolution

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/resolution/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_resolutions(client):
    """Test case for get_resolutions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/resolution',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scheme_attribute(client):
    """Test case for get_scheme_attribute

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/permissionscheme/{permission_scheme_id}/attribute/{attribute_key}'.format(permission_scheme_id=56, attribute_key='attribute_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_security_levels_for_project(client):
    """Test case for get_security_levels_for_project

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/project/{project_key_or_id}/securitylevel'.format(project_key_or_id='project_key_or_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_info(client):
    """Test case for get_server_info

    
    """
    params = [('doHealthCheck', True)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/serverInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_share_permission(client):
    """Test case for get_share_permission

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/filter/{id}/permission/{permission_id}'.format(permission_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_share_permissions(client):
    """Test case for get_share_permissions

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/filter/{id}/permission'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_state(client):
    """Test case for get_state

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/cluster/zdu/state',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/status/{id_or_name}'.format(id_or_name='id_or_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status_categories(client):
    """Test case for get_status_categories

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/statuscategory',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status_category(client):
    """Test case for get_status_category

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/statuscategory/{id_or_key}'.format(id_or_key='id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_statuses(client):
    """Test case for get_statuses

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sub_tasks(client):
    """Test case for get_sub_tasks

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/subtask'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transitions(client):
    """Test case for get_transitions

    
    """
    params = [('transitionId', 'transition_id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/transitions'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_upgrade_result(client):
    """Test case for get_upgrade_result

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/upgrade',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_from_group(client):
    """Test case for get_users_from_group

    
    """
    params = [('groupname', 'groupname_example'),
                    ('includeInactiveUsers', False),
                    ('startAt', 0),
                    ('maxResults', 50)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/group/member',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/version/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version_related_issues(client):
    """Test case for get_version_related_issues

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/version/{id}/relatedIssueCounts'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version_unresolved_issues(client):
    """Test case for get_version_unresolved_issues

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/version/{id}/unresolvedIssueCount'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_votes(client):
    """Test case for get_votes

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/votes'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workflow(client):
    """Test case for get_workflow

    
    """
    params = [('workflowName', 'workflow_name_example'),
                    ('returnDraftIfExists', False)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/workflowscheme/{id}/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_worklog(client):
    """Test case for get_worklog

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/worklog/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_worklogs_for_ids(client):
    """Test case for get_worklogs_for_ids

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/worklog/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_link_issues(client):
    """Test case for link_issues

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issueLink',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    
    """
    params = [('filter', 'filter_example'),
                    ('startAt', 56),
                    ('maxResults', 56)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/dashboard',
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
        path='/jira/rest/auth/1/session',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/auth/1/session',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_merge(client):
    """Test case for merge

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/version/{id}/mergeto/{move_issues_to}'.format(move_issues_to='move_issues_to_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_field(client):
    """Test case for move_field

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}/fields/{id}/move'.format(screen_id=56, tab_id=56, id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_sub_tasks(client):
    """Test case for move_sub_tasks

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/subtask/move'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_tab(client):
    """Test case for move_tab

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}/move/{pos}'.format(screen_id=56, tab_id=56, pos=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_version(client):
    """Test case for move_version

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/version/{id}/move'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify(client):
    """Test case for notify

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/notify'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_partial_update_project_role(client):
    """Test case for partial_update_project_role

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/role/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_check_create_user(client):
    """Test case for policy_check_create_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/password/policy/createUser',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_policy_check_update_user(client):
    """Test case for policy_check_update_user

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/password/policy/updateUser',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_process_requests(client):
    """Test case for process_requests

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/reindex/request',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put(client):
    """Test case for put

    
    """
    headers = { 
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/applicationrole/{key}'.format(key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_bulk(client):
    """Test case for put_bulk

    
    """
    headers = { 
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/applicationrole',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex(client):
    """Test case for reindex

    
    """
    params = [('type', 'type_example'),
                    ('indexComments', False),
                    ('indexChangeHistory', False),
                    ('indexWorklogs', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/reindex',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reindex_issues(client):
    """Test case for reindex_issues

    
    """
    params = [('issueId', 'issue_id_example'),
                    ('indexComments', False),
                    ('indexChangeHistory', False),
                    ('indexWorklogs', False)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/reindex/issue',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_release(client):
    """Test case for release

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/auth/1/websudo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_attachment(client):
    """Test case for remove_attachment

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/attachment/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_field(client):
    """Test case for remove_field

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}/fields/{id}'.format(screen_id=56, tab_id=56, id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_group(client):
    """Test case for remove_group

    
    """
    params = [('groupname', 'groupname_example'),
                    ('swapGroup', 'swap_group_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/group',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_preference(client):
    """Test case for remove_preference

    
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/mypreferences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_project_category(client):
    """Test case for remove_project_category

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/projectCategory/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user(client):
    """Test case for remove_user

    
    """
    params = [('username', 'username_example'),
                    ('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_from_application(client):
    """Test case for remove_user_from_application

    
    """
    params = [('username', 'username_example'),
                    ('applicationKey', 'application_key_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/user/application',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_from_group(client):
    """Test case for remove_user_from_group

    
    """
    params = [('groupname', 'groupname_example'),
                    ('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/group/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_vote(client):
    """Test case for remove_vote

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/votes'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_watcher(client):
    """Test case for remove_watcher

    
    """
    params = [('username', 'username_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/watchers'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_tab(client):
    """Test case for rename_tab

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/screens/{screen_id}/tabs/{tab_id}'.format(screen_id=56, tab_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_upgrades_now(client):
    """Test case for run_upgrades_now

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/upgrade',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    
    """
    params = [('jql', 'jql_example'),
                    ('startAt', 56),
                    ('maxResults', 56),
                    ('validateQuery', True),
                    ('fields', 'fields_example'),
                    ('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/jira/rest/api/2/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_using_search_request(client):
    """Test case for search_using_search_request

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/search',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_actors(client):
    """Test case for set_actors

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/project/{project_id_or_key}/role/{id}'.format(project_id_or_key='project_id_or_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_base_url(client):
    """Test case for set_base_url

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/settings/baseUrl',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_default_share_scope(client):
    """Test case for set_default_share_scope

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/filter/defaultShareScope',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_draft_issue_type(client):
    """Test case for set_draft_issue_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/issuetype/{issue_type}'.format(issue_type='issue_type_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_issue_navigator_default_columns(client):
    """Test case for set_issue_navigator_default_columns

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/settings/columns',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_issue_type(client):
    """Test case for set_issue_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/issuetype/{issue_type}'.format(issue_type='issue_type_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_preference(client):
    """Test case for set_preference

    
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/mypreferences',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_property_via_restful_table(client):
    """Test case for set_property_via_restful_table

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/application-properties/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_ready_to_upgrade(client):
    """Test case for set_ready_to_upgrade

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/cluster/zdu/start',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_scheme_attribute(client):
    """Test case for set_scheme_attribute

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/permissionscheme/{permission_scheme_id}/attribute/{key}'.format(permission_scheme_id=56, key='key_example'),
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
        method='GET',
        path='/jira/rest/api/2/monitoring/jmx/startExposing',
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
        method='GET',
        path='/jira/rest/api/2/monitoring/jmx/stopExposing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_store_temporary_avatar(client):
    """Test case for store_temporary_avatar

    
    """
    params = [('filename', 'filename_example'),
                    ('size', 56)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/avatar/{type}/temporary'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update(client):
    """Test case for update

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_comment(client):
    """Test case for update_comment

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/comment/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_component(client):
    """Test case for update_component

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/component/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_default(client):
    """Test case for update_default

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/default'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_draft(client):
    """Test case for update_draft

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/draft'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_draft_default(client):
    """Test case for update_draft_default

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/default'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_draft_workflow_mapping(client):
    """Test case for update_draft_workflow_mapping

    
    """
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/draft/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_link_type(client):
    """Test case for update_issue_link_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issueLinkType/{issue_link_type_id}'.format(issue_link_type_id='issue_link_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_issue_type(client):
    """Test case for update_issue_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issuetype/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_permission_scheme(client):
    """Test case for update_permission_scheme

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/permissionscheme/{scheme_id}'.format(scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project(client):
    """Test case for update_project

    
    """
    params = [('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/project/{project_id_or_key}'.format(project_id_or_key='project_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_category(client):
    """Test case for update_project_category

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/projectCategory/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_type(client):
    """Test case for update_project_type

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/project/{project_id_or_key}/type/{new_project_type_key}'.format(project_id_or_key='project_id_or_key_example', new_project_type_key='new_project_type_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_property(client):
    """Test case for update_property

    
    """
    params = [('key', 'key_example'),
                    ('workflowName', 'workflow_name_example'),
                    ('workflowMode', 'workflow_mode_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflow/api/2/transitions/{id}/properties'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_remote_issue_link(client):
    """Test case for update_remote_issue_link

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/remotelink/{link_id}'.format(link_id='link_id_example', issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_version(client):
    """Test case for update_version

    
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/version/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workflow_mapping(client):
    """Test case for update_workflow_mapping

    
    """
    params = [('workflowName', 'workflow_name_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/workflowscheme/{id}/workflow'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_worklog(client):
    """Test case for update_worklog

    
    """
    params = [('adjustEstimate', 'adjust_estimate_example'),
                    ('newEstimate', 'new_estimate_example')]
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/jira/rest/api/2/issue/{issue_id_or_key}/worklog/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate(client):
    """Test case for validate

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/jira/rest/api/2/licenseValidator',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

