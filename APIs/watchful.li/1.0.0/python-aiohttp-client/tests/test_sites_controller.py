# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit import Audit
from openapi_server.models.extension import Extension
from openapi_server.models.log import Log
from openapi_server.models.post_log import PostLog
from openapi_server.models.post_site import PostSite
from openapi_server.models.site import Site
from openapi_server.models.tag import Tag


pytestmark = pytest.mark.asyncio

async def test_add_site_to_backup_queue(client):
    """Test case for add_site_to_backup_queue

    Add the site to the backup queue
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/backupnow'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_audits(client):
    """Test case for create_audits

    Create an audit for the site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/audits'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_log(client):
    """Test case for create_log

    Create a custom log for a specific website
    """
    body = openapi_server.PostLog()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/logs'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_site(client):
    """Test case for create_site

    Create a site
    """
    body = openapi_server.PostSite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_monitor(client):
    """Test case for delete_monitor

    Delete uptime monitor
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{id}/monitor'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_backup_profiles(client):
    """Test case for get_backup_profiles

    Return backup profile
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/backupprofiles'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_backups(client):
    """Test case for get_list_backups

    List of latest backups
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/backups'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_audits(client):
    """Test case for get_site_audits

    Return audits for a specific website
    """
    params = [('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/audits'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_by_id(client):
    """Test case for get_site_by_id

    Find sites by ID
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sites(client):
    """Test case for get_sites

    Get a list of Sites
    """
    params = [('siteids', 'siteids_example'),
                    ('name', 'name_example'),
                    ('access_url', 'access_url_example'),
                    ('j_version', 'j_version_example'),
                    ('ip', 'ip_example'),
                    ('jUpdate', 56),
                    ('canUpdate', 56),
                    ('published', 56),
                    ('error', 'error_example'),
                    ('nbUpdates', 'nb_updates_example'),
                    ('up', 56),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_uptime(client):
    """Test case for get_uptime

    Return uptime data
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/uptime'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_install_extension(client):
    """Test case for install_extension

    Install extension
    """
    params = [('url', 'url_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/extensions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_monitor(client):
    """Test case for post_monitor

    Post uptime monitor
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/monitor'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_tags(client):
    """Test case for post_tags

    Add tags for a specific website
    """
    body = openapi_server.Tag()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/tags'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scanner(client):
    """Test case for scanner

    Scan the site for malware
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/scanner'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_seo_analyze(client):
    """Test case for seo_analyze

    SEO analyze for a page
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/seo'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_id_delete(client):
    """Test case for sites_id_delete

    Delete a specific Site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_id_extensions_get(client):
    """Test case for sites_id_extensions_get

    Get extensions for a site
    """
    params = [('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/extensions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_id_logs_get(client):
    """Test case for sites_id_logs_get

    Return logs for a specific website
    """
    params = [('log_entry', 'log_entry_example'),
                    ('log_type', 'log_type_example'),
                    ('from', '_from_example'),
                    ('to', 'to_example'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/logs'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_sites_id_put(client):
    """Test case for sites_id_put

    Update a site
    """
    body = openapi_server.PostSite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_id_tags_get(client):
    """Test case for sites_id_tags_get

    Return tags for a specific website
    """
    params = [('name', 'name_example'),
                    ('type', 'type_example'),
                    ('fields', 'fields_example'),
                    ('limit', 56),
                    ('limitstart', 56),
                    ('order', 'order_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/tags'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_metadata_get(client):
    """Test case for sites_metadata_get

    Get the list of fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/metadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_site_backup(client):
    """Test case for start_site_backup

    Start a remote backup for the site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/backupstart'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_step_site_backup(client):
    """Test case for step_site_backup

    Step (continue) a remote backup for the site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/backupstep'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_joomla(client):
    """Test case for update_joomla

    Update Joomla core on the remote site
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{id}/updatejoomla'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_debug_site(client):
    """Test case for validate_debug_site

    validate the site, return the debug information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/validatedebug'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_site(client):
    """Test case for validate_site

    validate the site, return the new logs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{id}/validate'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

