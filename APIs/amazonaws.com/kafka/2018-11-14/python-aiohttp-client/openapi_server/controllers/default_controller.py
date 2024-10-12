from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_associate_scram_secret_request import BatchAssociateScramSecretRequest
from openapi_server.models.batch_associate_scram_secret_response import BatchAssociateScramSecretResponse
from openapi_server.models.batch_disassociate_scram_secret_response import BatchDisassociateScramSecretResponse
from openapi_server.models.create_cluster_request import CreateClusterRequest
from openapi_server.models.create_cluster_response import CreateClusterResponse
from openapi_server.models.create_cluster_v2_request import CreateClusterV2Request
from openapi_server.models.create_cluster_v2_response import CreateClusterV2Response
from openapi_server.models.create_configuration_request import CreateConfigurationRequest
from openapi_server.models.create_configuration_response import CreateConfigurationResponse
from openapi_server.models.create_vpc_connection_request import CreateVpcConnectionRequest
from openapi_server.models.create_vpc_connection_response import CreateVpcConnectionResponse
from openapi_server.models.delete_cluster_response import DeleteClusterResponse
from openapi_server.models.delete_configuration_response import DeleteConfigurationResponse
from openapi_server.models.delete_vpc_connection_response import DeleteVpcConnectionResponse
from openapi_server.models.describe_cluster_operation_response import DescribeClusterOperationResponse
from openapi_server.models.describe_cluster_operation_v2_response import DescribeClusterOperationV2Response
from openapi_server.models.describe_cluster_response import DescribeClusterResponse
from openapi_server.models.describe_cluster_v2_response import DescribeClusterV2Response
from openapi_server.models.describe_configuration_response import DescribeConfigurationResponse
from openapi_server.models.describe_configuration_revision_response import DescribeConfigurationRevisionResponse
from openapi_server.models.describe_vpc_connection_response import DescribeVpcConnectionResponse
from openapi_server.models.get_bootstrap_brokers_response import GetBootstrapBrokersResponse
from openapi_server.models.get_cluster_policy_response import GetClusterPolicyResponse
from openapi_server.models.get_compatible_kafka_versions_response import GetCompatibleKafkaVersionsResponse
from openapi_server.models.list_client_vpc_connections_response import ListClientVpcConnectionsResponse
from openapi_server.models.list_cluster_operations_response import ListClusterOperationsResponse
from openapi_server.models.list_cluster_operations_v2_response import ListClusterOperationsV2Response
from openapi_server.models.list_clusters_response import ListClustersResponse
from openapi_server.models.list_clusters_v2_response import ListClustersV2Response
from openapi_server.models.list_configuration_revisions_response import ListConfigurationRevisionsResponse
from openapi_server.models.list_configurations_response import ListConfigurationsResponse
from openapi_server.models.list_kafka_versions_response import ListKafkaVersionsResponse
from openapi_server.models.list_nodes_response import ListNodesResponse
from openapi_server.models.list_scram_secrets_response import ListScramSecretsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_vpc_connections_response import ListVpcConnectionsResponse
from openapi_server.models.put_cluster_policy_request import PutClusterPolicyRequest
from openapi_server.models.put_cluster_policy_response import PutClusterPolicyResponse
from openapi_server.models.reboot_broker_request import RebootBrokerRequest
from openapi_server.models.reboot_broker_response import RebootBrokerResponse
from openapi_server.models.reject_client_vpc_connection_request import RejectClientVpcConnectionRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_broker_count_request import UpdateBrokerCountRequest
from openapi_server.models.update_broker_count_response import UpdateBrokerCountResponse
from openapi_server.models.update_broker_storage_request import UpdateBrokerStorageRequest
from openapi_server.models.update_broker_storage_response import UpdateBrokerStorageResponse
from openapi_server.models.update_broker_type_request import UpdateBrokerTypeRequest
from openapi_server.models.update_broker_type_response import UpdateBrokerTypeResponse
from openapi_server.models.update_cluster_configuration_request import UpdateClusterConfigurationRequest
from openapi_server.models.update_cluster_configuration_response import UpdateClusterConfigurationResponse
from openapi_server.models.update_cluster_kafka_version_request import UpdateClusterKafkaVersionRequest
from openapi_server.models.update_cluster_kafka_version_response import UpdateClusterKafkaVersionResponse
from openapi_server.models.update_configuration_request import UpdateConfigurationRequest
from openapi_server.models.update_configuration_response import UpdateConfigurationResponse
from openapi_server.models.update_connectivity_request import UpdateConnectivityRequest
from openapi_server.models.update_connectivity_response import UpdateConnectivityResponse
from openapi_server.models.update_monitoring_request import UpdateMonitoringRequest
from openapi_server.models.update_monitoring_response import UpdateMonitoringResponse
from openapi_server.models.update_security_request import UpdateSecurityRequest
from openapi_server.models.update_security_response import UpdateSecurityResponse
from openapi_server.models.update_storage_request import UpdateStorageRequest
from openapi_server.models.update_storage_response import UpdateStorageResponse
from openapi_server import util


async def batch_associate_scram_secret(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_associate_scram_secret

                 &lt;p&gt;Associates one or more Scram Secrets with an Amazon MSK cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = BatchAssociateScramSecretRequest.from_dict(body)
    return web.Response(status=200)


async def batch_disassociate_scram_secret(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_disassociate_scram_secret

                 &lt;p&gt;Disassociates one or more Scram Secrets from an Amazon MSK cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = BatchAssociateScramSecretRequest.from_dict(body)
    return web.Response(status=200)


async def create_cluster(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cluster

                 &lt;p&gt;Creates a new MSK cluster.&lt;/p&gt;          

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
    body = CreateClusterRequest.from_dict(body)
    return web.Response(status=200)


async def create_cluster_v2(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cluster_v2

                 &lt;p&gt;Creates a new MSK cluster.&lt;/p&gt;          

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
    body = CreateClusterV2Request.from_dict(body)
    return web.Response(status=200)


async def create_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_configuration

                 &lt;p&gt;Creates a new MSK configuration.&lt;/p&gt;          

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
    body = CreateConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def create_vpc_connection(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vpc_connection

                 &lt;p&gt;Creates a new MSK VPC connection.&lt;/p&gt;          

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
    body = CreateVpcConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_cluster(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, current_version=None) -> web.Response:
    """delete_cluster

                 &lt;p&gt;Deletes the MSK cluster specified by the Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    :param current_version:              &lt;p&gt;The current version of the MSK cluster.&lt;/p&gt;          
    :type current_version: str

    """
    return web.Response(status=200)


async def delete_cluster_policy(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_cluster_policy

                 &lt;p&gt;Deletes the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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


async def delete_configuration(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_configuration

                 &lt;p&gt;Deletes an MSK Configuration.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration.&lt;/p&gt;          
    :type arn: str
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


async def delete_vpc_connection(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vpc_connection

                 &lt;p&gt;Deletes a MSK VPC connection.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK VPC connection.&lt;/p&gt;          
    :type arn: str
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


async def describe_cluster(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cluster

                 &lt;p&gt;Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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


async def describe_cluster_operation(request: web.Request, cluster_operation_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cluster_operation

                 &lt;p&gt;Returns a description of the cluster operation specified by the ARN.&lt;/p&gt;          

    :param cluster_operation_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the MSK cluster operation.&lt;/p&gt;          
    :type cluster_operation_arn: str
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


async def describe_cluster_operation_v2(request: web.Request, cluster_operation_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cluster_operation_v2

                 &lt;p&gt;Returns a description of the cluster operation specified by the ARN.&lt;/p&gt; 

    :param cluster_operation_arn: ARN of the cluster operation to describe.
    :type cluster_operation_arn: str
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


async def describe_cluster_v2(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cluster_v2

                 &lt;p&gt;Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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


async def describe_configuration(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_configuration

                 &lt;p&gt;Returns a description of this MSK configuration.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.&lt;/p&gt;          
    :type arn: str
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


async def describe_configuration_revision(request: web.Request, arn, revision, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_configuration_revision

                 &lt;p&gt;Returns a description of this revision of the configuration.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.&lt;/p&gt;          
    :type arn: str
    :param revision:              &lt;p&gt;A string that uniquely identifies a revision of an MSK configuration.&lt;/p&gt;          
    :type revision: int
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


async def describe_vpc_connection(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_vpc_connection

                 &lt;p&gt;Returns a description of this MSK VPC connection.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies a MSK VPC connection.&lt;/p&gt;    
    :type arn: str
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


async def get_bootstrap_brokers(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_bootstrap_brokers

                 &lt;p&gt;A list of brokers that a client application can use to bootstrap.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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


async def get_cluster_policy(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cluster_policy

                 &lt;p&gt;Get the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;             
    :type cluster_arn: str
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


async def get_compatible_kafka_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_arn=None) -> web.Response:
    """get_compatible_kafka_versions

                 &lt;p&gt;Gets the Apache Kafka versions to which you can update the MSK cluster.&lt;/p&gt;          

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
    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster check.&lt;/p&gt;             
    :type cluster_arn: str

    """
    return web.Response(status=200)


async def list_client_vpc_connections(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_client_vpc_connections

                 &lt;p&gt;Returns a list of all the VPC connections in this Region.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_cluster_operations(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_cluster_operations

                 &lt;p&gt;Returns a list of all the operations that have been performed on the specified MSK cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_cluster_operations_v2(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_cluster_operations_v2

                 &lt;p&gt;Returns a list of all the operations that have been performed on the specified MSK cluster.&lt;/p&gt;          

    :param cluster_arn: The arn of the cluster whose operations are being requested.
    :type cluster_arn: str
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
    :param max_results: The maxResults of the query.
    :type max_results: int
    :param next_token: The nextToken of the query.
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_clusters(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_name_filter=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_clusters

                 &lt;p&gt;Returns a list of all the MSK clusters in the current Region.&lt;/p&gt;          

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
    :param cluster_name_filter:              &lt;p&gt;Specify a prefix of the name of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.&lt;/p&gt;          
    :type cluster_name_filter: str
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_clusters_v2(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cluster_name_filter=None, cluster_type_filter=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_clusters_v2

                 &lt;p&gt;Returns a list of all the MSK clusters in the current Region.&lt;/p&gt;          

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
    :param cluster_name_filter:              &lt;p&gt;Specify a prefix of the names of the clusters that you want to list. The service lists all the clusters whose names start with this prefix.&lt;/p&gt;          
    :type cluster_name_filter: str
    :param cluster_type_filter:              &lt;p&gt;Specify either PROVISIONED or SERVERLESS.&lt;/p&gt;          
    :type cluster_type_filter: str
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_configuration_revisions(request: web.Request, arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_configuration_revisions

                 &lt;p&gt;Returns a list of all the MSK configurations in this Region.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies an MSK configuration and all of its revisions.&lt;/p&gt;          
    :type arn: str
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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_configurations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_configurations

                 &lt;p&gt;Returns a list of all the MSK configurations in this Region.&lt;/p&gt;          

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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_kafka_versions(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_kafka_versions

                 &lt;p&gt;Returns a list of Apache Kafka versions.&lt;/p&gt;          

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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response. To get the next batch, provide this token in your next request.&lt;/p&gt;
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_nodes(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_nodes

                 &lt;p&gt;Returns a list of the broker nodes in the cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_scram_secrets(request: web.Request, cluster_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_scram_secrets

                 &lt;p&gt;Returns a list of the Scram Secrets associated with an Amazon MSK cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The arn of the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    :param max_results:              &lt;p&gt;The maxResults of the query.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The nextToken of the query.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

                 &lt;p&gt;Returns a list of the tags associated with the specified resource.&lt;/p&gt;          

    :param resource_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the resource that&#39;s associated with the tags.&lt;/p&gt;          
    :type resource_arn: str
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


async def list_vpc_connections(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, max_results2=None, next_token2=None) -> web.Response:
    """list_vpc_connections

                 &lt;p&gt;Returns a list of all the VPC connections in this Region.&lt;/p&gt;          

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
    :param max_results:              &lt;p&gt;The maximum number of results to return in the response. If there are more results, the response includes a NextToken parameter.&lt;/p&gt;          
    :type max_results: int
    :param next_token:              &lt;p&gt;The paginated results marker. When the result of the operation is truncated, the call returns NextToken in the response.              To get the next batch, provide this token in your next request.&lt;/p&gt;          
    :type next_token: str
    :param max_results2: Pagination limit
    :type max_results2: str
    :param next_token2: Pagination token
    :type next_token2: str

    """
    return web.Response(status=200)


async def put_cluster_policy(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_cluster_policy

                 &lt;p&gt;Creates or updates the MSK cluster policy specified by the cluster Amazon Resource Name (ARN) in the request.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = PutClusterPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def reboot_broker(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reboot_broker

    Reboots brokers.

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = RebootBrokerRequest.from_dict(body)
    return web.Response(status=200)


async def reject_client_vpc_connection(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """reject_client_vpc_connection

                 &lt;p&gt;Returns empty response.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = RejectClientVpcConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

                 &lt;p&gt;Adds tags to the specified MSK resource.&lt;/p&gt;          

    :param resource_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the resource that&#39;s associated with the tags.&lt;/p&gt;          
    :type resource_arn: str
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


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

                 &lt;p&gt;Removes the tags associated with the keys that are provided in the query.&lt;/p&gt;          

    :param resource_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the resource that&#39;s associated with the tags.&lt;/p&gt;          
    :type resource_arn: str
    :param tag_keys:              &lt;p&gt;Tag keys must be unique for a given cluster. In addition, the following restrictions apply:&lt;/p&gt;             &lt;ul&gt;                &lt;li&gt;                   &lt;p&gt;Each tag key must be unique. If you add a tag with a key that&#39;s already in                   use, your new tag overwrites the existing key-value pair. &lt;/p&gt;                &lt;/li&gt;                &lt;li&gt;                   &lt;p&gt;You can&#39;t start a tag key with aws: because this prefix is reserved for use                   by  AWS.  AWS creates tags that begin with this prefix on your behalf, but                   you can&#39;t edit or delete them.&lt;/p&gt;                &lt;/li&gt;                &lt;li&gt;                   &lt;p&gt;Tag keys must be between 1 and 128 Unicode characters in length.&lt;/p&gt;                &lt;/li&gt;                &lt;li&gt;                   &lt;p&gt;Tag keys must consist of the following characters: Unicode letters, digits,                   white space, and the following special characters: _ . / &#x3D; + -                      @.&lt;/p&gt;                &lt;/li&gt;             &lt;/ul&gt;          
    :type tag_keys: List[str]
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


async def update_broker_count(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_broker_count

                 &lt;p&gt;Updates the number of broker nodes in the cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateBrokerCountRequest.from_dict(body)
    return web.Response(status=200)


async def update_broker_storage(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_broker_storage

                 &lt;p&gt;Updates the EBS storage associated with MSK brokers.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateBrokerStorageRequest.from_dict(body)
    return web.Response(status=200)


async def update_broker_type(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_broker_type

                 &lt;p&gt;Updates EC2 instance type.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateBrokerTypeRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster_configuration(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster_configuration

                 &lt;p&gt;Updates the cluster with the configuration that is specified in the request body.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateClusterConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster_kafka_version(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster_kafka_version

                 &lt;p&gt;Updates the Apache Kafka version for the cluster.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;             
    :type cluster_arn: str
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
    body = UpdateClusterKafkaVersionRequest.from_dict(body)
    return web.Response(status=200)


async def update_configuration(request: web.Request, arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_configuration

                 &lt;p&gt;Updates an MSK configuration.&lt;/p&gt;          

    :param arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the configuration.&lt;/p&gt;          
    :type arn: str
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
    body = UpdateConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_connectivity(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_connectivity

                 &lt;p&gt;Updates the cluster&#39;s connectivity configuration.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the configuration.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateConnectivityRequest.from_dict(body)
    return web.Response(status=200)


async def update_monitoring(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_monitoring

                 &lt;p&gt;Updates the monitoring settings for the cluster. You can use this operation to specify which Apache Kafka metrics you want Amazon MSK to send to Amazon CloudWatch. You can also specify settings for open monitoring with Prometheus.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateMonitoringRequest.from_dict(body)
    return web.Response(status=200)


async def update_security(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_security

                 &lt;p&gt;Updates the security settings for the cluster. You can use this operation to specify encryption and authentication on existing clusters.&lt;/p&gt;          

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) that uniquely identifies the cluster.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateSecurityRequest.from_dict(body)
    return web.Response(status=200)


async def update_storage(request: web.Request, cluster_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_storage

    Updates cluster broker volume size (or) sets cluster storage mode to TIERED.

    :param cluster_arn:              &lt;p&gt;The Amazon Resource Name (ARN) of the cluster to be updated.&lt;/p&gt;          
    :type cluster_arn: str
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
    body = UpdateStorageRequest.from_dict(body)
    return web.Response(status=200)
