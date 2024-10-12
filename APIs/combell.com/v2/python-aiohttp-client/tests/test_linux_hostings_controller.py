# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_host_header_request import AddHostHeaderRequest
from openapi_server.models.add_ssh_key_request import AddSshKeyRequest
from openapi_server.models.add_subsite_request import AddSubsiteRequest
from openapi_server.models.auto_redirect_config import AutoRedirectConfig
from openapi_server.models.ftp_configuration import FtpConfiguration
from openapi_server.models.gzip_config import GzipConfig
from openapi_server.models.http2_configuration import Http2Configuration
from openapi_server.models.lets_encrypt_config import LetsEncryptConfig
from openapi_server.models.linux_hosting import LinuxHosting
from openapi_server.models.linux_hosting_detail import LinuxHostingDetail
from openapi_server.models.php_version import PhpVersion
from openapi_server.models.scheduled_task import ScheduledTask
from openapi_server.models.ssh_configuration import SshConfiguration
from openapi_server.models.ssh_key import SshKey
from openapi_server.models.update_php_a_pcu_request import UpdatePhpAPcuRequest
from openapi_server.models.update_php_memory_limit_request import UpdatePhpMemoryLimitRequest


pytestmark = pytest.mark.asyncio

async def test_add_scheduled_tasks(client):
    """Test case for add_scheduled_tasks

    Add a scheduled task
    """
    body = {"cron_expression":"cron_expression","id":"id","script_location":"script_location","enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/linuxhostings/{domain_name}/scheduledtasks'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_ssh_key(client):
    """Test case for add_ssh_key

    Add a SSH key
    """
    body = {"public_key":"public_key"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/linuxhostings/{domain_name}/ssh/keys'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_apcu(client):
    """Test case for change_apcu

    Configure PHP APCu setting
    """
    body = {"apcu_size":0,"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/phpsettings/apcu'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_auto_redirect(client):
    """Test case for change_auto_redirect

    Configure auto redirect
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/sslsettings/{hostname}/autoredirect'.format(hostname='hostname_example', domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_gzip_compression(client):
    """Test case for change_gzip_compression

    Enable/disable GZIP compression
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/settings/gzipcompression'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_lets_encrypt(client):
    """Test case for change_lets_encrypt

    Configure let's encrypt
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/sslsettings/{hostname}/letsencrypt'.format(hostname='hostname_example', domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_php_memory_limit(client):
    """Test case for change_php_memory_limit

    Configure PHP memory limit
    """
    body = {"memory_limit":0}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/phpsettings/memorylimit'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_php_version(client):
    """Test case for change_php_version

    Change the Linux hosting PHP version.
    """
    body = {"version":"version"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/phpsettings/version'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_ftp(client):
    """Test case for configure_ftp

    Configure FTP
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/ftp/configuration'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_http2(client):
    """Test case for configure_http2

    Configure HTTP/2
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example'),
                    ('site_name', 'site_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/sites/{site_name}/http2/configuration'.format(domain_name2='domain_name_example', site_name2='site_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_scheduled_task(client):
    """Test case for configure_scheduled_task

    Configure a scheduled task
    """
    body = {"cron_expression":"cron_expression","id":"id","script_location":"script_location","enabled":True}
    params = [('domain_name', 'domain_name_example'),
                    ('scheduled_task_id', 'scheduled_task_id_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/scheduledtasks/{scheduled_task_id}'.format(domain_name2='domain_name_example', scheduled_task_id2='scheduled_task_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configure_ssh(client):
    """Test case for configure_ssh

    Configure SSH
    """
    body = {"enabled":True}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/linuxhostings/{domain_name}/ssh/configuration'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_host_header(client):
    """Test case for create_host_header

    Create a host header
    """
    body = {"domain_name":"domain_name"}
    params = [('domain_name', 'domain_name_example'),
                    ('site_name', 'site_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/linuxhostings/{domain_name}/sites/{site_name}/hostheaders'.format(domain_name2='domain_name_example', site_name2='site_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subsite(client):
    """Test case for create_subsite

    Create a subsite
    """
    body = {"path":"path","domain_name":"domain_name"}
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/linuxhostings/{domain_name}/subsites'.format(domain_name2='domain_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_scheduled_task(client):
    """Test case for delete_scheduled_task

    Delete a scheduled task
    """
    params = [('domain_name', 'domain_name_example'),
                    ('scheduled_task_id', 'scheduled_task_id_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/linuxhostings/{domain_name}/scheduledtasks/{scheduled_task_id}'.format(domain_name2='domain_name_example', scheduled_task_id2='scheduled_task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_ssh_key(client):
    """Test case for delete_ssh_key

    Delete a SSH key
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/linuxhostings/{domain_name}/ssh/keys/{fingerprint}'.format(fingerprint='fingerprint_example', domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subsite(client):
    """Test case for delete_subsite

    Delete a subsite
    """
    params = [('domain_name', 'domain_name_example'),
                    ('site_name', 'site_name_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/linuxhostings/{domain_name}/subsites/{site_name}'.format(domain_name2='domain_name_example', site_name2='site_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_available_php_versions(client):
    """Test case for get_available_php_versions

    Get the available PHP versions.
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/linuxhostings/{domain_name}/phpsettings/availableversions'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_linux_hosting(client):
    """Test case for get_linux_hosting

    Linux hosting detail
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/linuxhostings/{domain_name}'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_linux_hostings(client):
    """Test case for get_linux_hostings

    Overview of linux hostings
    """
    params = [('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/linuxhostings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scheduled_task(client):
    """Test case for get_scheduled_task

    Get scheduled task detail
    """
    params = [('domain_name', 'domain_name_example'),
                    ('scheduled_task_id', 'scheduled_task_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/linuxhostings/{domain_name}/scheduledtasks/{scheduled_task_id}'.format(domain_name2='domain_name_example', scheduled_task_id2='scheduled_task_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scheduled_tasks(client):
    """Test case for get_scheduled_tasks

    Overview of scheduled tasks
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/linuxhostings/{domain_name}/scheduledtasks'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ssh_keys(client):
    """Test case for get_ssh_keys

    Overview of SSH keys
    """
    params = [('domain_name', 'domain_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/linuxhostings/{domain_name}/ssh/keys'.format(domain_name2='domain_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

