from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_node_request import AssociateNodeRequest
from openapi_server.models.associate_node_response import AssociateNodeResponse
from openapi_server.models.create_backup_request import CreateBackupRequest
from openapi_server.models.create_backup_response import CreateBackupResponse
from openapi_server.models.create_server_request import CreateServerRequest
from openapi_server.models.create_server_response import CreateServerResponse
from openapi_server.models.delete_backup_request import DeleteBackupRequest
from openapi_server.models.delete_server_request import DeleteServerRequest
from openapi_server.models.describe_account_attributes_response import DescribeAccountAttributesResponse
from openapi_server.models.describe_backups_request import DescribeBackupsRequest
from openapi_server.models.describe_backups_response import DescribeBackupsResponse
from openapi_server.models.describe_events_request import DescribeEventsRequest
from openapi_server.models.describe_events_response import DescribeEventsResponse
from openapi_server.models.describe_node_association_status_request import DescribeNodeAssociationStatusRequest
from openapi_server.models.describe_node_association_status_response import DescribeNodeAssociationStatusResponse
from openapi_server.models.describe_servers_request import DescribeServersRequest
from openapi_server.models.describe_servers_response import DescribeServersResponse
from openapi_server.models.disassociate_node_request import DisassociateNodeRequest
from openapi_server.models.disassociate_node_response import DisassociateNodeResponse
from openapi_server.models.export_server_engine_attribute_request import ExportServerEngineAttributeRequest
from openapi_server.models.export_server_engine_attribute_response import ExportServerEngineAttributeResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.restore_server_request import RestoreServerRequest
from openapi_server.models.restore_server_response import RestoreServerResponse
from openapi_server.models.start_maintenance_request import StartMaintenanceRequest
from openapi_server.models.start_maintenance_response import StartMaintenanceResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_server_engine_attributes_request import UpdateServerEngineAttributesRequest
from openapi_server.models.update_server_engine_attributes_response import UpdateServerEngineAttributesResponse
from openapi_server.models.update_server_request import UpdateServerRequest
from openapi_server.models.update_server_response import UpdateServerResponse
from openapi_server import util


async def associate_node(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_node

    &lt;p&gt; Associates a new node with the server. For more information about how to disassociate a node, see &lt;a&gt;DisassociateNode&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; On a Chef server: This command is an alternative to &lt;code&gt;knife bootstrap&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; Example (Chef): &lt;code&gt;aws opsworks-cm associate-node --server-name &lt;i&gt;MyServer&lt;/i&gt; --node-name &lt;i&gt;MyManagedNode&lt;/i&gt; --engine-attributes \&quot;Name&#x3D;&lt;i&gt;CHEF_ORGANIZATION&lt;/i&gt;,Value&#x3D;default\&quot; \&quot;Name&#x3D;&lt;i&gt;CHEF_NODE_PUBLIC_KEY&lt;/i&gt;,Value&#x3D;&lt;i&gt;public-key-pem&lt;/i&gt;\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; On a Puppet server, this command is an alternative to the &lt;code&gt;puppet cert sign&lt;/code&gt; command that signs a Puppet node CSR. &lt;/p&gt; &lt;p&gt; Example (Puppet): &lt;code&gt;aws opsworks-cm associate-node --server-name &lt;i&gt;MyServer&lt;/i&gt; --node-name &lt;i&gt;MyManagedNode&lt;/i&gt; --engine-attributes \&quot;Name&#x3D;&lt;i&gt;PUPPET_NODE_CSR&lt;/i&gt;,Value&#x3D;&lt;i&gt;csr-pem&lt;/i&gt;\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; A node can can only be associated with servers that are in a &lt;code&gt;HEALTHY&lt;/code&gt; state. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. The AssociateNode API call can be integrated into Auto Scaling configurations, AWS Cloudformation templates, or the user data of a server&#39;s instance. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = AssociateNodeRequest.from_dict(body)
    return web.Response(status=200)


async def create_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_backup

    &lt;p&gt; Creates an application-level backup of a server. While the server is in the &lt;code&gt;BACKING_UP&lt;/code&gt; state, the server cannot be changed, and no additional backup can be created. &lt;/p&gt; &lt;p&gt; Backups can be created for servers in &lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;HEALTHY&lt;/code&gt;, and &lt;code&gt;UNHEALTHY&lt;/code&gt; states. By default, you can create a maximum of 50 manual backups. &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;LimitExceededException&lt;/code&gt; is thrown when the maximum number of manual backups is reached. An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when the server is not in any of the following states: RUNNING, HEALTHY, or UNHEALTHY. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server is not found. A &lt;code&gt;ValidationException&lt;/code&gt; is thrown when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateBackupRequest.from_dict(body)
    return web.Response(status=200)


async def create_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_server

    &lt;p&gt; Creates and immedately starts a new server. The server is ready to use when it is in the &lt;code&gt;HEALTHY&lt;/code&gt; state. By default, you can create a maximum of 10 servers. &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;LimitExceededException&lt;/code&gt; is thrown when you have created the maximum number of servers (10). A &lt;code&gt;ResourceAlreadyExistsException&lt;/code&gt; is thrown when a server with the same name already exists in the account. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when you specify a backup ID that is not valid or is for a backup that does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is thrown when parameters of the request are not valid. &lt;/p&gt; &lt;p&gt; If you do not specify a security group by adding the &lt;code&gt;SecurityGroupIds&lt;/code&gt; parameter, AWS OpsWorks creates a new security group. &lt;/p&gt; &lt;p&gt; &lt;i&gt;Chef Automate:&lt;/i&gt; The default security group opens the Chef server to the world on TCP port 443. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22. &lt;/p&gt; &lt;p&gt; &lt;i&gt;Puppet Enterprise:&lt;/i&gt; The default security group opens TCP ports 22, 443, 4433, 8140, 8142, 8143, and 8170. If a KeyName is present, AWS OpsWorks enables SSH access. SSH is also open to the world on TCP port 22. &lt;/p&gt; &lt;p&gt;By default, your server is accessible from any IP address. We recommend that you update your security group rules to allow access from known IP addresses and address ranges only. To edit security group rules, open Security Groups in the navigation pane of the EC2 management console. &lt;/p&gt; &lt;p&gt;To specify your own domain for a server, and provide your own self-signed or CA-signed certificate and private key, specify values for &lt;code&gt;CustomDomain&lt;/code&gt;, &lt;code&gt;CustomCertificate&lt;/code&gt;, and &lt;code&gt;CustomPrivateKey&lt;/code&gt;.&lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = CreateServerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_backup(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_backup

    &lt;p&gt; Deletes a backup. You can delete both manual and automated backups. This operation is asynchronous. &lt;/p&gt; &lt;p&gt; An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when a backup deletion is already in progress. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the backup does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is thrown when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteBackupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_server

    &lt;p&gt; Deletes the server and the underlying AWS CloudFormation stacks (including the server&#39;s EC2 instance). When you run this command, the server state is updated to &lt;code&gt;DELETING&lt;/code&gt;. After the server is deleted, it is no longer returned by &lt;code&gt;DescribeServer&lt;/code&gt; requests. If the AWS CloudFormation stack cannot be deleted, the server cannot be deleted. &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when a server deletion is already in progress. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt; &lt;p&gt; &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteServerRequest.from_dict(body)
    return web.Response(status=200)


async def describe_account_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_account_attributes

    &lt;p&gt; Describes your OpsWorks-CM account attributes. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: 
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def describe_backups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_backups

    &lt;p&gt; Describes backups. The results are ordered by time, with newest backups first. If you do not specify a BackupId or ServerName, the command returns all backups. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the backup does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeBackupsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_events(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_events

    &lt;p&gt; Describes events for a specified server. Results are ordered by time, with newest events first. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeEventsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_node_association_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_node_association_status

    &lt;p&gt; Returns the current status of an existing association or disassociation request. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when no recent association or disassociation request with the specified token is found, or when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DescribeNodeAssociationStatusRequest.from_dict(body)
    return web.Response(status=200)


async def describe_servers(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_servers

    &lt;p&gt; Lists all configuration management servers that are identified with your account. Only the stored results from Amazon DynamoDB are returned. AWS OpsWorks CM does not query other services. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = DescribeServersRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_node(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_node

    &lt;p&gt; Disassociates a node from an AWS OpsWorks CM server, and removes the node from the server&#39;s managed nodes. After a node is disassociated, the node key pair is no longer valid for accessing the configuration manager&#39;s API. For more information about how to associate a node, see &lt;a&gt;AssociateNode&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;A node can can only be disassociated from a server that is in a &lt;code&gt;HEALTHY&lt;/code&gt; state. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisassociateNodeRequest.from_dict(body)
    return web.Response(status=200)


async def export_server_engine_attribute(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """export_server_engine_attribute

    &lt;p&gt; Exports a specified server engine attribute as a base64-encoded string. For example, you can export user data that you can use in EC2 to associate nodes with a server. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt; &lt;p&gt; A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when the server is in any of the following states: CREATING, TERMINATED, FAILED or DELETING. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExportServerEngineAttributeRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    Returns a list of tags that are applied to the specified AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise servers or backups.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def restore_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """restore_server

    &lt;p&gt; Restores a backup to a server that is in a &lt;code&gt;CONNECTION_LOST&lt;/code&gt;, &lt;code&gt;HEALTHY&lt;/code&gt;, &lt;code&gt;RUNNING&lt;/code&gt;, &lt;code&gt;UNHEALTHY&lt;/code&gt;, or &lt;code&gt;TERMINATED&lt;/code&gt; state. When you run RestoreServer, the server&#39;s EC2 instance is deleted, and a new EC2 instance is configured. RestoreServer maintains the existing server endpoint, so configuration management of the server&#39;s client devices (nodes) should continue to work. &lt;/p&gt; &lt;p&gt;Restoring from a backup is performed by creating a new EC2 instance. If restoration is successful, and the server is in a &lt;code&gt;HEALTHY&lt;/code&gt; state, AWS OpsWorks CM switches traffic over to the new instance. After restoration is finished, the old EC2 instance is maintained in a &lt;code&gt;Running&lt;/code&gt; or &lt;code&gt;Stopped&lt;/code&gt; state, but is eventually terminated.&lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; An &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown when the server is not in a valid state. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RestoreServerRequest.from_dict(body)
    return web.Response(status=200)


async def start_maintenance(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_maintenance

    &lt;p&gt; Manually starts server maintenance. This command can be useful if an earlier maintenance attempt failed, and the underlying cause of maintenance failure has been resolved. The server is in an &lt;code&gt;UNDER_MAINTENANCE&lt;/code&gt; state while maintenance is in progress. &lt;/p&gt; &lt;p&gt; Maintenance can only be started on servers in &lt;code&gt;HEALTHY&lt;/code&gt; and &lt;code&gt;UNHEALTHY&lt;/code&gt; states. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is thrown. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = StartMaintenanceRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Applies tags to an AWS OpsWorks for Chef Automate or AWS OpsWorks for Puppet Enterprise server, or to server backups.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes specified tags from an AWS OpsWorks-CM server or backup.

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UntagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def update_server(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_server

    &lt;p&gt; Updates settings for a server. &lt;/p&gt; &lt;p&gt; This operation is synchronous. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServerRequest.from_dict(body)
    return web.Response(status=200)


async def update_server_engine_attributes(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_server_engine_attributes

    &lt;p&gt; Updates engine-specific attributes on a specified server. The server enters the &lt;code&gt;MODIFYING&lt;/code&gt; state when this operation is in progress. Only one update can occur at a time. You can use this command to reset a Chef server&#39;s public key (&lt;code&gt;CHEF_PIVOTAL_KEY&lt;/code&gt;) or a Puppet server&#39;s admin password (&lt;code&gt;PUPPET_ADMIN_PASSWORD&lt;/code&gt;). &lt;/p&gt; &lt;p&gt; This operation is asynchronous. &lt;/p&gt; &lt;p&gt; This operation can only be called for servers in &lt;code&gt;HEALTHY&lt;/code&gt; or &lt;code&gt;UNHEALTHY&lt;/code&gt; states. Otherwise, an &lt;code&gt;InvalidStateException&lt;/code&gt; is raised. A &lt;code&gt;ResourceNotFoundException&lt;/code&gt; is thrown when the server does not exist. A &lt;code&gt;ValidationException&lt;/code&gt; is raised when parameters of the request are not valid. &lt;/p&gt;

    :param x_amz_target: 
    :type x_amz_target: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = UpdateServerEngineAttributesRequest.from_dict(body)
    return web.Response(status=200)
