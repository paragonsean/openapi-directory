from typing import List, Dict
from aiohttp import web

from openapi_server.models.collaborator import Collaborator
from openapi_server.models.collaborator_data import CollaboratorData
from openapi_server.models.collaborator_error import CollaboratorError
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_data import DeploymentData
from openapi_server.models.deployment_error import DeploymentError
from openapi_server.models.jwt import JWT
from openapi_server.models.not_found import NotFound
from openapi_server.models.project import Project
from openapi_server.models.project_copy_check_request import ProjectCopyCheckRequest
from openapi_server.models.project_copy_request import ProjectCopyRequest
from openapi_server.models.project_data import ProjectData
from openapi_server.models.project_error import ProjectError
from openapi_server.models.project_file import ProjectFile
from openapi_server.models.project_file_error import ProjectFileError
from openapi_server.models.server import Server
from openapi_server.models.server_action import ServerAction
from openapi_server.models.server_action_data import ServerActionData
from openapi_server.models.server_action_error import ServerActionError
from openapi_server.models.server_data import ServerData
from openapi_server.models.server_error import ServerError
from openapi_server.models.server_run_statistics import ServerRunStatistics
from openapi_server.models.server_run_statistics_data import ServerRunStatisticsData
from openapi_server.models.server_run_statistics_error import ServerRunStatisticsError
from openapi_server.models.server_statistics import ServerStatistics
from openapi_server.models.server_statistics_data import ServerStatisticsData
from openapi_server.models.server_statistics_error import ServerStatisticsError
from openapi_server.models.server_status import ServerStatus
from openapi_server.models.ssh_tunnel import SshTunnel
from openapi_server.models.ssh_tunnel_data import SshTunnelData
from openapi_server.models.ssh_tunnel_error import SshTunnelError
from openapi_server import util


async def project_copy(request: web.Request, namespace, project_copy_data) -> web.Response:
    """Copy a project to your own account.

    

    :param namespace: User or team name.
    :type namespace: str
    :param project_copy_data: 
    :type project_copy_data: dict | bytes

    """
    project_copy_data = ProjectCopyRequest.from_dict(project_copy_data)
    return web.Response(status=200)


async def project_copy_check(request: web.Request, namespace, project_copy_data) -> web.Response:
    """Check if you are able to copy a project to your account.

    

    :param namespace: User or team name.
    :type namespace: str
    :param project_copy_data: 
    :type project_copy_data: dict | bytes

    """
    project_copy_data = ProjectCopyCheckRequest.from_dict(project_copy_data)
    return web.Response(status=200)


async def projects_collaborators_create(request: web.Request, project, namespace, collaborator_data=None) -> web.Response:
    """Create project collaborators

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param collaborator_data: 
    :type collaborator_data: dict | bytes

    """
    collaborator_data = CollaboratorData.from_dict(collaborator_data)
    return web.Response(status=200)


async def projects_collaborators_delete(request: web.Request, project, namespace, collaborator) -> web.Response:
    """Delete a project collaborator

    

    :param project: Project unique identifier.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param collaborator: Collaborator unique identifier.
    :type collaborator: str

    """
    return web.Response(status=200)


async def projects_collaborators_list(request: web.Request, project, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Get project collaborators

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit when retrieving items.
    :type limit: str
    :param offset: Offset when retrieving items.
    :type offset: str
    :param ordering: Ordering when retrieving items.
    :type ordering: str

    """
    return web.Response(status=200)


async def projects_collaborators_read(request: web.Request, project, namespace, collaborator) -> web.Response:
    """Get a project collaborator

    

    :param project: Project unique identifier.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param collaborator: Collaborator unique identifier expressed as UUID or name.
    :type collaborator: str

    """
    return web.Response(status=200)


async def projects_collaborators_update(request: web.Request, project, namespace, collaborator, collaborator_data=None) -> web.Response:
    """Update project collaborator

    

    :param project: 
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param collaborator: 
    :type collaborator: str
    :param collaborator_data: 
    :type collaborator_data: dict | bytes

    """
    collaborator_data = CollaboratorData.from_dict(collaborator_data)
    return web.Response(status=200)


async def projects_create(request: web.Request, namespace, project_data=None) -> web.Response:
    """Create a new project

    

    :param namespace: User or team name.
    :type namespace: str
    :param project_data: 
    :type project_data: dict | bytes

    """
    project_data = ProjectData.from_dict(project_data)
    return web.Response(status=200)


async def projects_delete(request: web.Request, namespace, project) -> web.Response:
    """Delete a project

    

    :param namespace: User or team name.
    :type namespace: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str

    """
    return web.Response(status=200)


async def projects_deployment_delete(request: web.Request, project, namespace, deployment) -> web.Response:
    """Delete a deployment

    

    :param project: Project unique identifier.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param deployment: User unique identifier.
    :type deployment: str

    """
    return web.Response(status=200)


async def projects_deployments_create(request: web.Request, project, namespace, deployment_data=None) -> web.Response:
    """Create a new deployment

    

    :param project: Project unique identifer expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param deployment_data: 
    :type deployment_data: dict | bytes

    """
    deployment_data = DeploymentData.from_dict(deployment_data)
    return web.Response(status=200)


async def projects_deployments_deploy(request: web.Request, project, namespace, deployment) -> web.Response:
    """Deploy an existing model

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param deployment: Deployment unique identifier expressed as UUID or name.
    :type deployment: str

    """
    return web.Response(status=200)


async def projects_deployments_list(request: web.Request, project, namespace, limit=None, offset=None, name=None, ordering=None) -> web.Response:
    """Retrieve deployments

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit results when getting deployment list.
    :type limit: str
    :param offset: Offset results when getting deployment list.
    :type offset: str
    :param name: Server name.
    :type name: str
    :param ordering: Ordering option when getting deployment list.
    :type ordering: str

    """
    return web.Response(status=200)


async def projects_deployments_read(request: web.Request, project, namespace, deployment) -> web.Response:
    """Retrieve a deployment

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param deployment: Deployment unique identifier expressed as UUID or name.
    :type deployment: str

    """
    return web.Response(status=200)


async def projects_deployments_replace(request: web.Request, project, namespace, deployment, deployment_data=None) -> web.Response:
    """Replace a deployment

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param deployment: Deployment unique identifier expressed as UUID or name.
    :type deployment: str
    :param deployment_data: 
    :type deployment_data: dict | bytes

    """
    deployment_data = DeploymentData.from_dict(deployment_data)
    return web.Response(status=200)


async def projects_deployments_update(request: web.Request, project, namespace, deployment, deployment_data=None) -> web.Response:
    """Update a deployment

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param deployment: Deployment unique identifier expressed as UUID or name.
    :type deployment: str
    :param deployment_data: 
    :type deployment_data: dict | bytes

    """
    deployment_data = DeploymentData.from_dict(deployment_data)
    return web.Response(status=200)


async def projects_list(request: web.Request, namespace, limit=None, offset=None, private=None, name=None, ordering=None) -> web.Response:
    """Get available projects

    

    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit when getting data.
    :type limit: str
    :param offset: Offset when getting data.
    :type offset: str
    :param private: Private project or public project.
    :type private: str
    :param name: Project name.
    :type name: str
    :param ordering: Ordering when getting projects.
    :type ordering: str

    """
    return web.Response(status=200)


async def projects_project_files_create(request: web.Request, project, namespace, file=None, base64_data=None, name=None, path=None) -> web.Response:
    """Create project files

    

    :param project: Project unique identifier.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param file: File to send, to create new file. This parameter is only used with form data and may include multiple files.
    :type file: str
    :param base64_data: Fila data, represented as base64.
    :type base64_data: str
    :param name: File name. May include path when creating file with base64 field.
    :type name: str
    :param path: File path. Defaults to (/).
    :type path: str

    """
    return web.Response(status=200)


async def projects_project_files_delete(request: web.Request, project, namespace, id) -> web.Response:
    """Delete a project file

    

    :param project: Project unique identifer.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: File unique identifier.
    :type id: str

    """
    return web.Response(status=200)


async def projects_project_files_list(request: web.Request, project, namespace, limit=None, offset=None, ordering=None, filename=None, content=None) -> web.Response:
    """Get project files

    

    :param project: Unique identifier for project file expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit when getting project file list.
    :type limit: str
    :param offset: Offset when getting project file list.
    :type offset: str
    :param ordering: Ordering of list values when getting project file list.
    :type ordering: str
    :param filename: Exact file name, relative to the project root. If no such file is found, an empty list will be returned.
    :type filename: str
    :param content: Determines whether or not content is returned as base64. Defaults to false.
    :type content: str

    """
    return web.Response(status=200)


async def projects_project_files_read(request: web.Request, project, namespace, id, content=None) -> web.Response:
    """Get a project file

    

    :param project: Project unique identifer.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: File unique identifier.
    :type id: str
    :param content: Determines whether or not content is returned as base64. Defaults to false.
    :type content: str

    """
    return web.Response(status=200)


async def projects_project_files_replace(request: web.Request, project, namespace, id, file=None, base64_data=None, name=None, path=None) -> web.Response:
    """Replace a project file

    

    :param project: Project unique identifer.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: File unique identifier.
    :type id: str
    :param file: File to send, to create new file. This parameter is only used with form data and may include multiple files.
    :type file: str
    :param base64_data: Fila data, represented as base64.
    :type base64_data: str
    :param name: File name. May include path when creating file with base64 field.
    :type name: str
    :param path: File path. Defaults to (/).
    :type path: str

    """
    return web.Response(status=200)


async def projects_project_files_update(request: web.Request, project, namespace, id, file=None, base64_data=None, name=None, path=None) -> web.Response:
    """Update a project file

    

    :param project: Project unique identifer.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: File unique identifier.
    :type id: str
    :param file: File to send, to create new file. This parameter is only used with form data and may include multiple files.
    :type file: str
    :param base64_data: Fila data, represented as base64.
    :type base64_data: str
    :param name: File name. May include path when creating file with base64 field.
    :type name: str
    :param path: File path. Defaults to (/).
    :type path: str

    """
    return web.Response(status=200)


async def projects_read(request: web.Request, namespace, project) -> web.Response:
    """Get a project

    

    :param namespace: User or team name.
    :type namespace: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str

    """
    return web.Response(status=200)


async def projects_replace(request: web.Request, namespace, project, project_data=None) -> web.Response:
    """Replace a project

    

    :param namespace: User or team namespace.
    :type namespace: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param project_data: 
    :type project_data: dict | bytes

    """
    project_data = ProjectData.from_dict(project_data)
    return web.Response(status=200)


async def projects_servers_api_key(request: web.Request, project, namespace, server) -> web.Response:
    """Get server API key

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str

    """
    return web.Response(status=200)


async def projects_servers_auth(request: web.Request, project, namespace, server) -> web.Response:
    """Server api key validation

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str

    """
    return web.Response(status=200)


async def projects_servers_create(request: web.Request, project, namespace, server_data=None) -> web.Response:
    """Create a new server

    

    :param project: Project unique identifer expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server_data: 
    :type server_data: dict | bytes

    """
    server_data = ServerData.from_dict(server_data)
    return web.Response(status=200)


async def projects_servers_delete(request: web.Request, project, namespace, server) -> web.Response:
    """Delete a server

    

    :param project: Project unique identifier.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: User unique identifier.
    :type server: str

    """
    return web.Response(status=200)


async def projects_servers_list(request: web.Request, project, namespace, limit=None, offset=None, name=None, ordering=None) -> web.Response:
    """Retrieve servers

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit results when getting server list.
    :type limit: str
    :param offset: Offset results when getting server list.
    :type offset: str
    :param name: Server name.
    :type name: str
    :param ordering: Ordering option when getting server list.
    :type ordering: str

    """
    return web.Response(status=200)


async def projects_servers_read(request: web.Request, project, namespace, server) -> web.Response:
    """Retrieve a server

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str

    """
    return web.Response(status=200)


async def projects_servers_replace(request: web.Request, project, namespace, server, server_data=None) -> web.Response:
    """Replace a server

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param server_data: 
    :type server_data: dict | bytes

    """
    server_data = ServerData.from_dict(server_data)
    return web.Response(status=200)


async def projects_servers_run_stats_create(request: web.Request, server, project, namespace, serverrunstats_data=None) -> web.Response:
    """Create a new server&#39;s run statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param serverrunstats_data: 
    :type serverrunstats_data: dict | bytes

    """
    serverrunstats_data = ServerRunStatisticsData.from_dict(serverrunstats_data)
    return web.Response(status=200)


async def projects_servers_run_stats_delete(request: web.Request, server, project, namespace, id) -> web.Response:
    """Delete a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Server run statistics unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def projects_servers_run_stats_read(request: web.Request, server, project, namespace, id) -> web.Response:
    """Retrieve statistics for a server

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Run statistics unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def projects_servers_run_stats_replace(request: web.Request, server, project, namespace, id, serverrunstats_data=None) -> web.Response:
    """Replace a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Server run statistics expressed as UUID.
    :type id: str
    :param serverrunstats_data: 
    :type serverrunstats_data: dict | bytes

    """
    serverrunstats_data = ServerRunStatisticsData.from_dict(serverrunstats_data)
    return web.Response(status=200)


async def projects_servers_run_stats_update(request: web.Request, server, project, namespace, id, serverrunstats_data=None) -> web.Response:
    """Update a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Server run statistics unique identifier expressed as UUID.
    :type id: str
    :param serverrunstats_data: 
    :type serverrunstats_data: dict | bytes

    """
    serverrunstats_data = ServerRunStatisticsData.from_dict(serverrunstats_data)
    return web.Response(status=200)


async def projects_servers_ssh_tunnels_create(request: web.Request, server, project, namespace, sshtunnel_data=None) -> web.Response:
    """Create SSH Tunnel associated to a server

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param sshtunnel_data: 
    :type sshtunnel_data: dict | bytes

    """
    sshtunnel_data = SshTunnelData.from_dict(sshtunnel_data)
    return web.Response(status=200)


async def projects_servers_ssh_tunnels_delete(request: web.Request, server, project, namespace, tunnel) -> web.Response:
    """Delete an SSH Tunnel associated to a server

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param tunnel: SSH tunnel unique identifier expressed as UUID or name.
    :type tunnel: str

    """
    return web.Response(status=200)


async def projects_servers_ssh_tunnels_list(request: web.Request, server, project, namespace, limit=None, offset=None, ordering=None) -> web.Response:
    """Get SSH Tunnels associated to a server

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param limit: Limit retrieved items.
    :type limit: str
    :param offset: Offset retrieved items.
    :type offset: str
    :param ordering: Order retrieved items.
    :type ordering: str

    """
    return web.Response(status=200)


async def projects_servers_ssh_tunnels_read(request: web.Request, server, project, namespace, tunnel) -> web.Response:
    """Get an SSH Tunnel associated to a server

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param tunnel: SSH tunnel unique identifier expressed as UUID or name.
    :type tunnel: str

    """
    return web.Response(status=200)


async def projects_servers_ssh_tunnels_replace(request: web.Request, server, project, namespace, tunnel, sshtunnel_data=None) -> web.Response:
    """Replace SSH Tunnel associated to a server

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param tunnel: SSH tunnel unique identifier expressed as UUID or name.
    :type tunnel: str
    :param sshtunnel_data: 
    :type sshtunnel_data: dict | bytes

    """
    sshtunnel_data = SshTunnelData.from_dict(sshtunnel_data)
    return web.Response(status=200)


async def projects_servers_ssh_tunnels_update(request: web.Request, server, project, namespace, tunnel, sshtunnel_data=None) -> web.Response:
    """Update an SSH Tunnel associated to a server

    

    :param server: 
    :type server: str
    :param project: 
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param tunnel: 
    :type tunnel: str
    :param sshtunnel_data: 
    :type sshtunnel_data: dict | bytes

    """
    sshtunnel_data = SshTunnelData.from_dict(sshtunnel_data)
    return web.Response(status=200)


async def projects_servers_start(request: web.Request, project, namespace, server) -> web.Response:
    """Start a server

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str

    """
    return web.Response(status=200)


async def projects_servers_stats_delete(request: web.Request, server, project, namespace, id) -> web.Response:
    """Delete a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Stats unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def projects_servers_stats_read(request: web.Request, server, project, namespace, id) -> web.Response:
    """Retrieve a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Server statistics unique identifier expressed as UUID.
    :type id: str

    """
    return web.Response(status=200)


async def projects_servers_stats_replace(request: web.Request, server, project, namespace, id, serverstats_data=None) -> web.Response:
    """Replace a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Server statistics unique identifier expressed as UUID.
    :type id: str
    :param serverstats_data: 
    :type serverstats_data: dict | bytes

    """
    serverstats_data = ServerStatisticsData.from_dict(serverstats_data)
    return web.Response(status=200)


async def projects_servers_stats_update(request: web.Request, server, project, namespace, id, serverstats_data=None) -> web.Response:
    """Update a server&#39;s statistics

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param id: Server statistics unique identifier expressed as UUID.
    :type id: str
    :param serverstats_data: 
    :type serverstats_data: dict | bytes

    """
    serverstats_data = ServerStatisticsData.from_dict(serverstats_data)
    return web.Response(status=200)


async def projects_servers_statuses(request: web.Request, project, namespace) -> web.Response:
    """Retrieve server statuses

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str

    """
    return web.Response(status=200)


async def projects_servers_stop(request: web.Request, project, namespace, server) -> web.Response:
    """Stop a server

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str

    """
    return web.Response(status=200)


async def projects_servers_update(request: web.Request, project, namespace, server, server_data=None) -> web.Response:
    """Update a server

    

    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param server_data: 
    :type server_data: dict | bytes

    """
    server_data = ServerData.from_dict(server_data)
    return web.Response(status=200)


async def projects_update(request: web.Request, namespace, project, project_data=None) -> web.Response:
    """Update a project

    

    :param namespace: User or team name.
    :type namespace: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param project_data: 
    :type project_data: dict | bytes

    """
    project_data = ProjectData.from_dict(project_data)
    return web.Response(status=200)


async def service_trigger_create(request: web.Request, server, project, namespace, server_action=None) -> web.Response:
    """Create a new server trigger

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param server_action: Server action.
    :type server_action: dict | bytes

    """
    server_action = ServerActionData.from_dict(server_action)
    return web.Response(status=200)


async def service_trigger_delete(request: web.Request, server, project, namespace, trigger) -> web.Response:
    """Delete a server trigger

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param trigger: Trigger identifier expressed as UUID or name.
    :type trigger: str

    """
    return web.Response(status=200)


async def service_trigger_list(request: web.Request, server, project, namespace, name=None, limit=None, offset=None, ordering=None) -> web.Response:
    """Retrieve server triggers

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param name: Trigger name.
    :type name: str
    :param limit: Limit when getting triggers.
    :type limit: str
    :param offset: Offset when getting triggers.
    :type offset: str
    :param ordering: Ordering when getting triggers.
    :type ordering: str

    """
    return web.Response(status=200)


async def service_trigger_read(request: web.Request, server, project, namespace, trigger) -> web.Response:
    """Get a server trigger

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param trigger: Trigger unique identifier.
    :type trigger: str

    """
    return web.Response(status=200)


async def service_trigger_replace(request: web.Request, server, project, namespace, trigger, server_action=None) -> web.Response:
    """Replace a server trigger

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param trigger: Trigger unique identifier.
    :type trigger: str
    :param server_action: 
    :type server_action: dict | bytes

    """
    server_action = ServerActionData.from_dict(server_action)
    return web.Response(status=200)


async def service_trigger_update(request: web.Request, server, project, namespace, trigger, server_action=None) -> web.Response:
    """Update a server trigger

    

    :param server: Server unique identifier expressed as UUID or name.
    :type server: str
    :param project: Project unique identifier expressed as UUID or name.
    :type project: str
    :param namespace: User or team name.
    :type namespace: str
    :param trigger: Trigger identifier expressed as UUID or name.
    :type trigger: str
    :param server_action: 
    :type server_action: dict | bytes

    """
    server_action = ServerActionData.from_dict(server_action)
    return web.Response(status=200)
