from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.add_to_placement_group_request import AddToPlacementGroupRequest
from openapi_server.models.attach_to_network_request import AttachToNetworkRequest
from openapi_server.models.create_image_request import CreateImageRequest
from openapi_server.models.detach_from_network_request import DetachFromNetworkRequest
from openapi_server.models.rebuild_server_request import RebuildServerRequest
from openapi_server.models.servers_id_actions_attach_iso_post_request import ServersIdActionsAttachIsoPostRequest
from openapi_server.models.servers_id_actions_change_alias_ips_post_request import ServersIdActionsChangeAliasIpsPostRequest
from openapi_server.models.servers_id_actions_change_dns_ptr_post_request import ServersIdActionsChangeDnsPtrPostRequest
from openapi_server.models.servers_id_actions_change_protection_post_request import ServersIdActionsChangeProtectionPostRequest
from openapi_server.models.servers_id_actions_change_type_post_request import ServersIdActionsChangeTypePostRequest
from openapi_server.models.servers_id_actions_create_image_post201_response import ServersIdActionsCreateImagePost201Response
from openapi_server.models.servers_id_actions_enable_rescue_post201_response import ServersIdActionsEnableRescuePost201Response
from openapi_server.models.servers_id_actions_enable_rescue_post_request import ServersIdActionsEnableRescuePostRequest
from openapi_server.models.servers_id_actions_rebuild_post201_response import ServersIdActionsRebuildPost201Response
from openapi_server.models.servers_id_actions_request_console_post201_response import ServersIdActionsRequestConsolePost201Response
from openapi_server import util


async def servers_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Server

    Returns a specific Action object for a Server.

    :param id: ID of the Server
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def servers_id_actions_add_to_placement_group_post(request: web.Request, id, body=None) -> web.Response:
    """Add a Server to a Placement Group

    Adds a Server to a Placement Group.  Server must be powered off for this command to succeed.  #### Call specific error codes  | Code                          | Description                                                          | |-------------------------------|----------------------------------------------------------------------| | &#x60;server_not_stopped&#x60;          | The action requires a stopped server                                 | 

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddToPlacementGroupRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_attach_iso_post(request: web.Request, id, body=None) -> web.Response:
    """Attach an ISO to a Server

    Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already attached ISO will automatically be detached before the new ISO is attached.  Servers with attached ISOs have a modified boot order: They will try to boot from the ISO first before falling back to hard disk. 

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServersIdActionsAttachIsoPostRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_attach_to_network_post(request: web.Request, id, body=None) -> web.Response:
    """Attach a Server to a Network

    Attaches a Server to a network. This will complement the fixed public Server interface by adding an additional ethernet interface to the Server which is connected to the specified network.  The Server will get an IP auto assigned from a subnet of type &#x60;server&#x60; in the same &#x60;network_zone&#x60;.  Using the &#x60;alias_ips&#x60; attribute you can also define one or more additional IPs to the Servers. Please note that you will have to configure these IPs by hand on your Server since only the primary IP will be given out by DHCP.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;server_already_attached&#x60;        | The server is already attached to the network                         | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Server within the network        | | &#x60;networks_overlap&#x60;               | The network IP range overlaps with one of the server networks         | 

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AttachToNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_change_alias_ips_post(request: web.Request, id, body=None) -> web.Response:
    """Change alias IPs of a Network

    Changes the alias IPs of an already attached Network. Note that the existing aliases for the specified Network will be replaced with these provided in the request body. So if you want to add an alias IP, you have to provide the existing ones from the Network plus the new alias IP in the request body.

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServersIdActionsChangeAliasIpsPostRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_change_dns_ptr_post(request: web.Request, id, body=None) -> web.Response:
    """Change reverse DNS entry for this Server

    Changes the hostname that will appear when getting the hostname belonging to the primary IPs (IPv4 and IPv6) of this Server.  Floating IPs assigned to the Server are not affected by this. 

    :param id: ID of the Server
    :type id: int
    :param body: Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;.
    :type body: dict | bytes

    """
    body = ServersIdActionsChangeDnsPtrPostRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Server Protection

    Changes the protection configuration of the Server.

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServersIdActionsChangeProtectionPostRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_change_type_post(request: web.Request, id, body=None) -> web.Response:
    """Change the Type of a Server

    Changes the type (Cores, RAM and disk sizes) of a Server.  Server must be powered off for this command to succeed.  This copies the content of its disk, and starts it again.  You can only migrate to Server types with the same &#x60;storage_type&#x60; and equal or bigger disks. Shrinking disks is not possible as it might destroy data.  If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to downgrade the Server type, set &#x60;upgrade_disk&#x60; to &#x60;false&#x60;.  #### Call specific error codes  | Code                          | Description                                                          | |-------------------------------|----------------------------------------------------------------------| | &#x60;invalid_server_type&#x60;         | The server type does not fit for the given server or is deprecated   | | &#x60;server_not_stopped&#x60;          | The action requires a stopped server                                 | 

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServersIdActionsChangeTypePostRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_create_image_post(request: web.Request, id, body=None) -> web.Response:
    """Create Image from a Server

    Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates a snapshot of the current state of the disk and copies it into an Image. If the Server is currently running you must make sure that its disk content is consistent. Otherwise, the created Image may not be readable.  To make sure disk content is consistent, we recommend to shut down the Server prior to creating an Image.  You can either create a &#x60;backup&#x60; Image that is bound to the Server and therefore will be deleted when the Server is deleted, or you can create an &#x60;snapshot&#x60; Image which is completely independent of the Server it was created from and will survive Server deletion. Backup Images are only available when the backup option is enabled for the Server. Snapshot Images are billed on a per GB basis. 

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CreateImageRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_detach_from_network_post(request: web.Request, id, body=None) -> web.Response:
    """Detach a Server from a Network

    Detaches a Server from a network. The interface for this network will vanish.

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DetachFromNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_detach_iso_post(request: web.Request, id) -> web.Response:
    """Detach an ISO from a Server

    Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of the returned Action is immediately set to &#x60;success&#x60;

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_disable_backup_post(request: web.Request, id) -> web.Response:
    """Disable Backups for a Server

    Disables the automatic backup option and deletes all existing Backups for a Server. No more additional charges for backups will be made.  Caution: This immediately removes all existing backups for the Server! 

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_disable_rescue_post(request: web.Request, id) -> web.Response:
    """Disable Rescue Mode for a Server

    Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on next reboot.  Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.  Disabling rescue mode will not reboot your Server — you will have to do this yourself. 

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_enable_backup_post(request: web.Request, id) -> web.Response:
    """Enable and Configure Backups for a Server

    Enables and configures the automatic daily backup option for the Server. Enabling automatic backups will increase the price of the Server by 20%. In return, you will get seven slots where Images of type backup can be stored.  Backups are automatically created daily. 

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_enable_rescue_post(request: web.Request, id, body=None) -> web.Response:
    """Enable Rescue Mode for a Server

    Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue mode boots it will start a special minimal Linux distribution designed for repair and reinstall.  In case a Server cannot boot on its own you can use this to access a Server’s disks.  Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.  Enabling rescue mode will not [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server — you will have to do this yourself. 

    :param id: ID of the Server
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServersIdActionsEnableRescuePostRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Server

    Returns all Action objects for a Server. You can &#x60;sort&#x60; the results by using the sort URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Resource
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def servers_id_actions_poweroff_post(request: web.Request, id) -> web.Response:
    """Power off a Server

    Cuts power to the Server. This forcefully stops it without giving the Server operating system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord. Power off should only be used when shutdown does not work.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_poweron_post(request: web.Request, id) -> web.Response:
    """Power on a Server

    Starts a Server by turning its power on.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_reboot_post(request: web.Request, id) -> web.Response:
    """Soft-reboot a Server

    Reboots a Server gracefully by sending an ACPI request. The Server operating system must support ACPI and react to the request, otherwise the Server will not reboot.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_rebuild_post(request: web.Request, id, body=None) -> web.Response:
    """Rebuild a Server from an Image

    Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying all data** on the target Server  The Image can either be one you have created earlier (&#x60;backup&#x60; or &#x60;snapshot&#x60; Image) or it can be a completely fresh &#x60;system&#x60; Image provided by us. You can get a list of all available Images with &#x60;GET /images&#x60;.  Your Server will automatically be powered off before the rebuild command executes. 

    :param id: ID of the Server
    :type id: int
    :param body: To select which Image to rebuild from you can either pass an ID or a name as the &#x60;image&#x60; argument. Passing a name only works for &#x60;system&#x60; Images since the other Image types do not have a name set.
    :type body: dict | bytes

    """
    body = RebuildServerRequest.from_dict(body)
    return web.Response(status=200)


async def servers_id_actions_remove_from_placement_group_post(request: web.Request, id) -> web.Response:
    """Remove from Placement Group

    Removes a Server from a Placement Group. 

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_request_console_post(request: web.Request, id) -> web.Response:
    """Request Console for a Server

    Requests credentials for remote access via VNC over websocket to keyboard, monitor, and mouse for a Server. The provided URL is valid for 1 minute, after this period a new url needs to be created to connect to the Server. How long the connection is open after the initial connect is not subject to this timeout.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_reset_password_post(request: web.Request, id) -> web.Response:
    """Reset root Password of a Server

    Resets the root password. Only works for Linux systems that are running the qemu guest agent. Server must be powered on (status &#x60;running&#x60;) in order for this operation to succeed.  This will generate a new password for this Server and return it.  If this does not succeed you can use the rescue system to netboot the Server and manually change your Server password by hand. 

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_reset_post(request: web.Request, id) -> web.Response:
    """Reset a Server

    Cuts power to a Server and starts it again. This forcefully stops it without giving the Server operating system time to gracefully stop. This may lead to data loss, it’s equivalent to pulling the power cord and plugging it in again. Reset should only be used when reboot does not work.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)


async def servers_id_actions_shutdown_post(request: web.Request, id) -> web.Response:
    """Shutdown a Server

    Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating system must support ACPI and react to the request, otherwise the Server will not shut down.

    :param id: ID of the Server
    :type id: int

    """
    return web.Response(status=200)
