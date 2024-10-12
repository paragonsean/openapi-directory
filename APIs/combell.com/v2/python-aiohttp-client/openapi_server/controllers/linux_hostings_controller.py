from typing import List, Dict
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
from openapi_server import util


async def add_scheduled_tasks(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Add a scheduled task

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScheduledTask.from_dict(body)
    return web.Response(status=200)


async def add_ssh_key(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Add a SSH key

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: SSH key public key.
    :type body: dict | bytes

    """
    body = AddSshKeyRequest.from_dict(body)
    return web.Response(status=200)


async def change_apcu(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Configure PHP APCu setting

    

    :param domain_name: Linux hosting domain name
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Php APcu config
    :type body: dict | bytes

    """
    body = UpdatePhpAPcuRequest.from_dict(body)
    return web.Response(status=200)


async def change_auto_redirect(request: web.Request, domain_name, hostname, domain_name2, body=None) -> web.Response:
    """Configure auto redirect

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param hostname: Specific hostname.
    :type hostname: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Auto redirect config.
    :type body: dict | bytes

    """
    body = AutoRedirectConfig.from_dict(body)
    return web.Response(status=200)


async def change_gzip_compression(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Enable/disable GZIP compression

    

    :param domain_name: Linux hosting domain name
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Whether GZIP compression is enabled or not.
    :type body: dict | bytes

    """
    body = GzipConfig.from_dict(body)
    return web.Response(status=200)


async def change_lets_encrypt(request: web.Request, domain_name, hostname, domain_name2, body=None) -> web.Response:
    """Configure let&#39;s encrypt

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param hostname: Specific hostname.
    :type hostname: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Let&#39;s encrypt config.
    :type body: dict | bytes

    """
    body = LetsEncryptConfig.from_dict(body)
    return web.Response(status=200)


async def change_php_memory_limit(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Configure PHP memory limit

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Memory limit config
    :type body: dict | bytes

    """
    body = UpdatePhpMemoryLimitRequest.from_dict(body)
    return web.Response(status=200)


async def change_php_version(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Change the Linux hosting PHP version.

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: The new PHP version.
    :type body: dict | bytes

    """
    body = PhpVersion.from_dict(body)
    return web.Response(status=200)


async def configure_ftp(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Configure FTP

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: 
    :type body: dict | bytes

    """
    body = FtpConfiguration.from_dict(body)
    return web.Response(status=200)


async def configure_http2(request: web.Request, domain_name, site_name, domain_name2, site_name2, body=None) -> web.Response:
    """Configure HTTP/2

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param site_name: Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled.
    :type site_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param site_name2: Automatically added
    :type site_name2: str
    :param body: 
    :type body: dict | bytes

    """
    body = Http2Configuration.from_dict(body)
    return web.Response(status=200)


async def configure_scheduled_task(request: web.Request, domain_name, scheduled_task_id, domain_name2, scheduled_task_id2, body=None) -> web.Response:
    """Configure a scheduled task

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param scheduled_task_id: Id of the scheduled task.
    :type scheduled_task_id: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param scheduled_task_id2: Automatically added
    :type scheduled_task_id2: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScheduledTask.from_dict(body)
    return web.Response(status=200)


async def configure_ssh(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Configure SSH

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: 
    :type body: dict | bytes

    """
    body = SshConfiguration.from_dict(body)
    return web.Response(status=200)


async def create_host_header(request: web.Request, domain_name, site_name, domain_name2, site_name2, body=None) -> web.Response:
    """Create a host header

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param site_name: Name of the site on the linux hosting.
    :type site_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param site_name2: Automatically added
    :type site_name2: str
    :param body: Add host header request
    :type body: dict | bytes

    """
    body = AddHostHeaderRequest.from_dict(body)
    return web.Response(status=200)


async def create_subsite(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Create a subsite

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Add subsite request
    :type body: dict | bytes

    """
    body = AddSubsiteRequest.from_dict(body)
    return web.Response(status=200)


async def delete_scheduled_task(request: web.Request, domain_name, scheduled_task_id, domain_name2, scheduled_task_id2) -> web.Response:
    """Delete a scheduled task

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param scheduled_task_id: Id of the scheduled task.
    :type scheduled_task_id: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param scheduled_task_id2: Automatically added
    :type scheduled_task_id2: str

    """
    return web.Response(status=200)


async def delete_ssh_key(request: web.Request, domain_name, fingerprint, domain_name2) -> web.Response:
    """Delete a SSH key

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param fingerprint: Fingerprint of public key.
    :type fingerprint: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def delete_subsite(request: web.Request, domain_name, site_name, domain_name2, site_name2) -> web.Response:
    """Delete a subsite

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param site_name: Name of the site on the linux hosting.
    :type site_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param site_name2: Automatically added
    :type site_name2: str

    """
    return web.Response(status=200)


async def get_available_php_versions(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Get the available PHP versions.

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def get_linux_hosting(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Linux hosting detail

    

    :param domain_name: The Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def get_linux_hostings(request: web.Request, skip=None, take=None) -> web.Response:
    """Overview of linux hostings

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)


async def get_scheduled_task(request: web.Request, domain_name, scheduled_task_id, domain_name2, scheduled_task_id2) -> web.Response:
    """Get scheduled task detail

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param scheduled_task_id: Id of the scheduled task.
    :type scheduled_task_id: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param scheduled_task_id2: Automatically added
    :type scheduled_task_id2: str

    """
    return web.Response(status=200)


async def get_scheduled_tasks(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Overview of scheduled tasks

    Manage scheduled tasks which are also manageable via the control panel.

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def get_ssh_keys(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Overview of SSH keys

    

    :param domain_name: Linux hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)
