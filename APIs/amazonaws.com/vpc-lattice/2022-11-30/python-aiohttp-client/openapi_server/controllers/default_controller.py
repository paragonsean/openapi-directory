from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_update_rule_request import BatchUpdateRuleRequest
from openapi_server.models.batch_update_rule_response import BatchUpdateRuleResponse
from openapi_server.models.create_access_log_subscription_request import CreateAccessLogSubscriptionRequest
from openapi_server.models.create_access_log_subscription_response import CreateAccessLogSubscriptionResponse
from openapi_server.models.create_listener_request import CreateListenerRequest
from openapi_server.models.create_listener_response import CreateListenerResponse
from openapi_server.models.create_rule_request import CreateRuleRequest
from openapi_server.models.create_rule_response import CreateRuleResponse
from openapi_server.models.create_service_network_request import CreateServiceNetworkRequest
from openapi_server.models.create_service_network_response import CreateServiceNetworkResponse
from openapi_server.models.create_service_network_service_association_request import CreateServiceNetworkServiceAssociationRequest
from openapi_server.models.create_service_network_service_association_response import CreateServiceNetworkServiceAssociationResponse
from openapi_server.models.create_service_network_vpc_association_request import CreateServiceNetworkVpcAssociationRequest
from openapi_server.models.create_service_network_vpc_association_response import CreateServiceNetworkVpcAssociationResponse
from openapi_server.models.create_service_request import CreateServiceRequest
from openapi_server.models.create_service_response import CreateServiceResponse
from openapi_server.models.create_target_group_request import CreateTargetGroupRequest
from openapi_server.models.create_target_group_response import CreateTargetGroupResponse
from openapi_server.models.delete_service_network_service_association_response import DeleteServiceNetworkServiceAssociationResponse
from openapi_server.models.delete_service_network_vpc_association_response import DeleteServiceNetworkVpcAssociationResponse
from openapi_server.models.delete_service_response import DeleteServiceResponse
from openapi_server.models.delete_target_group_response import DeleteTargetGroupResponse
from openapi_server.models.deregister_targets_request import DeregisterTargetsRequest
from openapi_server.models.deregister_targets_response import DeregisterTargetsResponse
from openapi_server.models.get_access_log_subscription_response import GetAccessLogSubscriptionResponse
from openapi_server.models.get_auth_policy_response import GetAuthPolicyResponse
from openapi_server.models.get_listener_response import GetListenerResponse
from openapi_server.models.get_resource_policy_response import GetResourcePolicyResponse
from openapi_server.models.get_rule_response import GetRuleResponse
from openapi_server.models.get_service_network_response import GetServiceNetworkResponse
from openapi_server.models.get_service_network_service_association_response import GetServiceNetworkServiceAssociationResponse
from openapi_server.models.get_service_network_vpc_association_response import GetServiceNetworkVpcAssociationResponse
from openapi_server.models.get_service_response import GetServiceResponse
from openapi_server.models.get_target_group_response import GetTargetGroupResponse
from openapi_server.models.list_access_log_subscriptions_response import ListAccessLogSubscriptionsResponse
from openapi_server.models.list_listeners_response import ListListenersResponse
from openapi_server.models.list_rules_response import ListRulesResponse
from openapi_server.models.list_service_network_service_associations_response import ListServiceNetworkServiceAssociationsResponse
from openapi_server.models.list_service_network_vpc_associations_response import ListServiceNetworkVpcAssociationsResponse
from openapi_server.models.list_service_networks_response import ListServiceNetworksResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_target_groups_response import ListTargetGroupsResponse
from openapi_server.models.list_targets_request import ListTargetsRequest
from openapi_server.models.list_targets_response import ListTargetsResponse
from openapi_server.models.put_auth_policy_request import PutAuthPolicyRequest
from openapi_server.models.put_auth_policy_response import PutAuthPolicyResponse
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.register_targets_request import RegisterTargetsRequest
from openapi_server.models.register_targets_response import RegisterTargetsResponse
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_access_log_subscription_request import UpdateAccessLogSubscriptionRequest
from openapi_server.models.update_access_log_subscription_response import UpdateAccessLogSubscriptionResponse
from openapi_server.models.update_listener_request import UpdateListenerRequest
from openapi_server.models.update_listener_response import UpdateListenerResponse
from openapi_server.models.update_rule_request import UpdateRuleRequest
from openapi_server.models.update_rule_response import UpdateRuleResponse
from openapi_server.models.update_service_network_request import UpdateServiceNetworkRequest
from openapi_server.models.update_service_network_response import UpdateServiceNetworkResponse
from openapi_server.models.update_service_network_vpc_association_request import UpdateServiceNetworkVpcAssociationRequest
from openapi_server.models.update_service_network_vpc_association_response import UpdateServiceNetworkVpcAssociationResponse
from openapi_server.models.update_service_request import UpdateServiceRequest
from openapi_server.models.update_service_response import UpdateServiceResponse
from openapi_server.models.update_target_group_request import UpdateTargetGroupRequest
from openapi_server.models.update_target_group_response import UpdateTargetGroupResponse
from openapi_server import util


async def batch_update_rule(request: web.Request, listener_identifier, service_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_update_rule

    Updates the listener rules in a batch. You can use this operation to change the priority of listener rules. This can be useful when bulk updating or swapping rule priority. 

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    body = BatchUpdateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_access_log_subscription(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_access_log_subscription

    Enables access logs to be sent to Amazon CloudWatch, Amazon S3, and Amazon Kinesis Data Firehose. The service network owner can use the access logs to audit the services in the network. The service network owner will only see access logs from clients and services that are associated with their service network. Access log entries represent traffic originated from VPCs associated with that network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html\&quot;&gt;Access logs&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

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
    body = CreateAccessLogSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def create_listener(request: web.Request, service_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_listener

    Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html\&quot;&gt;Listeners&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    body = CreateListenerRequest.from_dict(body)
    return web.Response(status=200)


async def create_rule(request: web.Request, listener_identifier, service_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rule

    Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    body = CreateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_service(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service

    &lt;p&gt;Creates a service. A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html\&quot;&gt;Services&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateServiceRequest.from_dict(body)
    return web.Response(status=200)


async def create_service_network(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_network

    &lt;p&gt;Creates a service network. A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html\&quot;&gt;Service networks&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateServiceNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def create_service_network_service_association(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_network_service_association

    &lt;p&gt;Associates a service with a service network.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation if the service and service network are already associated or if there is a disassociation or deletion in progress. If the association fails, you can retry the operation by deleting the association and recreating it.&lt;/p&gt; &lt;p&gt;You cannot associate a service and service network that are shared with a caller. The caller must own either the service or the service network.&lt;/p&gt; &lt;p&gt;As a result of this operation, the association is created in the service network account and the association owner account.&lt;/p&gt;

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
    body = CreateServiceNetworkServiceAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_service_network_vpc_association(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_service_network_vpc_association

    &lt;p&gt;Associates a VPC with a service network. When you associate a VPC with the service network, it enables all the resources within that VPC to be clients and communicate with other services in the service network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations\&quot;&gt;Manage VPC associations&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can&#39;t use this operation if there is a disassociation in progress. If the association fails, retry by deleting the association and recreating it.&lt;/p&gt; &lt;p&gt;As a result of this operation, the association gets created in the service network account and the VPC owner account.&lt;/p&gt; &lt;p&gt;If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.&lt;/p&gt;

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
    body = CreateServiceNetworkVpcAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def create_target_group(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_target_group

    &lt;p&gt;Creates a target group. A target group is a collection of targets, or compute resources, that run your application or service. A target group can only be used by a single service.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html\&quot;&gt;Target groups&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateTargetGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_access_log_subscription(request: web.Request, access_log_subscription_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_access_log_subscription

    Deletes the specified access log subscription.

    :param access_log_subscription_identifier: The ID or Amazon Resource Name (ARN) of the access log subscription.
    :type access_log_subscription_identifier: str
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


async def delete_auth_policy(request: web.Request, resource_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_auth_policy

    Deletes the specified auth policy. If an auth is set to &lt;code&gt;AWS_IAM&lt;/code&gt; and the auth policy is deleted, all requests will be denied by default. If you are trying to remove the auth policy completely, you must set the auth_type to &lt;code&gt;NONE&lt;/code&gt;. If auth is enabled on the resource, but no auth policy is set, all requests will be denied.

    :param resource_identifier: The ID or Amazon Resource Name (ARN) of the resource.
    :type resource_identifier: str
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


async def delete_listener(request: web.Request, listener_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_listener

    Deletes the specified listener.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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


async def delete_resource_policy(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    Deletes the specified resource policy.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
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


async def delete_rule(request: web.Request, listener_identifier, rule_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rule

    &lt;p&gt;Deletes a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions. You can delete additional listener rules, but you cannot delete the default rule.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.&lt;/p&gt;

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param rule_identifier: The ID or Amazon Resource Name (ARN) of the rule.
    :type rule_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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


async def delete_service(request: web.Request, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service

    Deletes a service. A service can&#39;t be deleted if it&#39;s associated with a service network. If you delete a service, all resources related to the service, such as the resource policy, auth policy, listeners, listener rules, and access log subscriptions, are also deleted. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#delete-service\&quot;&gt;Delete a service&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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


async def delete_service_network(request: web.Request, service_network_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_network

    Deletes a service network. You can only delete the service network if there is no service or VPC associated with it. If you delete a service network, all resources related to the service network, such as the resource policy, auth policy, and access log subscriptions, are also deleted. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html#delete-service-network\&quot;&gt;Delete a service network&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

    :param service_network_identifier: The Amazon Resource Name (ARN) or ID of the service network.
    :type service_network_identifier: str
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


async def delete_service_network_service_association(request: web.Request, service_network_service_association_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_network_service_association

    Deletes the association between a specified service and the specific service network. This request will fail if an association is still in progress.

    :param service_network_service_association_identifier: The ID or Amazon Resource Name (ARN) of the association.
    :type service_network_service_association_identifier: str
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


async def delete_service_network_vpc_association(request: web.Request, service_network_vpc_association_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_service_network_vpc_association

    Disassociates the VPC from the service network. You can&#39;t disassociate the VPC if there is a create or update association in progress.

    :param service_network_vpc_association_identifier: The ID or Amazon Resource Name (ARN) of the association.
    :type service_network_vpc_association_identifier: str
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


async def delete_target_group(request: web.Request, target_group_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_target_group

    Deletes a target group. You can&#39;t delete a target group if it is used in a listener rule or if the target group creation is in progress.

    :param target_group_identifier: The ID or Amazon Resource Name (ARN) of the target group.
    :type target_group_identifier: str
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


async def deregister_targets(request: web.Request, target_group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deregister_targets

    Deregisters the specified targets from the specified target group.

    :param target_group_identifier: The ID or Amazon Resource Name (ARN) of the target group.
    :type target_group_identifier: str
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
    body = DeregisterTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def get_access_log_subscription(request: web.Request, access_log_subscription_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_access_log_subscription

    Retrieves information about the specified access log subscription.

    :param access_log_subscription_identifier: The ID or Amazon Resource Name (ARN) of the access log subscription.
    :type access_log_subscription_identifier: str
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


async def get_auth_policy(request: web.Request, resource_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_auth_policy

    Retrieves information about the auth policy for the specified service or service network.

    :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service.
    :type resource_identifier: str
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


async def get_listener(request: web.Request, listener_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_listener

    Retrieves information about the specified listener for the specified service.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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


async def get_resource_policy(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_resource_policy

    Retrieves information about the resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the service network or service.
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


async def get_rule(request: web.Request, listener_identifier, rule_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rule

    Retrieves information about listener rules. You can also retrieve information about the default listener rule. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Amazon VPC Lattice User Guide&lt;/i&gt;.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param rule_identifier: The ID or Amazon Resource Name (ARN) of the listener rule.
    :type rule_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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


async def get_service(request: web.Request, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service

    Retrieves information about the specified service.

    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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


async def get_service_network(request: web.Request, service_network_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_network

    Retrieves information about the specified service network.

    :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network.
    :type service_network_identifier: str
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


async def get_service_network_service_association(request: web.Request, service_network_service_association_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_network_service_association

    Retrieves information about the specified association between a service network and a service.

    :param service_network_service_association_identifier: The ID or Amazon Resource Name (ARN) of the association.
    :type service_network_service_association_identifier: str
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


async def get_service_network_vpc_association(request: web.Request, service_network_vpc_association_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_service_network_vpc_association

    Retrieves information about the association between a service network and a VPC.

    :param service_network_vpc_association_identifier: The ID or Amazon Resource Name (ARN) of the association.
    :type service_network_vpc_association_identifier: str
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


async def get_target_group(request: web.Request, target_group_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_target_group

    Retrieves information about the specified target group.

    :param target_group_identifier: The ID or Amazon Resource Name (ARN) of the target group.
    :type target_group_identifier: str
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


async def list_access_log_subscriptions(request: web.Request, resource_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_access_log_subscriptions

    Lists all access log subscriptions for the specified service network or service.

    :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service.
    :type resource_identifier: str
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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_listeners(request: web.Request, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_listeners

    Lists the listeners for the specified service.

    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_rules(request: web.Request, listener_identifier, service_identifier, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_rules

    Lists the rules for the listener.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_service_network_service_associations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, service_identifier=None, service_network_identifier=None) -> web.Response:
    """list_service_network_service_associations

    &lt;p&gt;Lists the associations between the service network and the service. You can filter the list either by service or service network. You must provide either the service network identifier or the service identifier.&lt;/p&gt; &lt;p&gt;Every association in Amazon VPC Lattice is given a unique Amazon Resource Name (ARN), such as when a service network is associated with a VPC or when a service is associated with a service network. If the association is for a resource that is shared with another account, the association will include the local account ID as the prefix in the ARN for each account the resource is shared with.&lt;/p&gt;

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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
    :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network.
    :type service_network_identifier: str

    """
    return web.Response(status=200)


async def list_service_network_vpc_associations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, service_network_identifier=None, vpc_identifier=None) -> web.Response:
    """list_service_network_vpc_associations

    Lists the service network and VPC associations. You can filter the list either by VPC or service network. You must provide either the service network identifier or the VPC identifier.

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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str
    :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network.
    :type service_network_identifier: str
    :param vpc_identifier: The ID or Amazon Resource Name (ARN) of the VPC.
    :type vpc_identifier: str

    """
    return web.Response(status=200)


async def list_service_networks(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_service_networks

    Lists the service networks owned by the caller account or shared with the caller account. Also includes the account ID in the ARN to show which account owns the service network.

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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_services(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_services

    Lists the services owned by the caller account or shared with the caller account.

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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Lists the tags for the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
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


async def list_target_groups(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, target_group_type=None, vpc_identifier=None) -> web.Response:
    """list_target_groups

    Lists your target groups. You can narrow your search by using the filters below in your request.

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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str
    :param target_group_type: The target group type.
    :type target_group_type: str
    :param vpc_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type vpc_identifier: str

    """
    return web.Response(status=200)


async def list_targets(request: web.Request, target_group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_targets

    Lists the targets for the target group. By default, all targets are included. You can use this API to check the health status of targets. You can also ﬁlter the results by target. 

    :param target_group_identifier: The ID or Amazon Resource Name (ARN) of the target group.
    :type target_group_identifier: str
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
    :param max_results: The maximum number of results to return.
    :type max_results: int
    :param next_token: A pagination token for the next page of results.
    :type next_token: str

    """
    body = ListTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def put_auth_policy(request: web.Request, resource_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_auth_policy

    Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.

    :param resource_identifier: The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.
    :type resource_identifier: str
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
    body = PutAuthPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    Attaches a resource-based permission policy to a service or service network. The policy must contain the same actions and condition statements as the Amazon Web Services Resource Access Manager permission for sharing services and service networks.

    :param resource_arn: The ID or Amazon Resource Name (ARN) of the service network or service for which the policy is created.
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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def register_targets(request: web.Request, target_group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_targets

    Registers the targets with the target group. If it&#39;s a Lambda target, you can only have one target in a target group.

    :param target_group_identifier: The ID or Amazon Resource Name (ARN) of the target group.
    :type target_group_identifier: str
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
    body = RegisterTargetsRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds the specified tags to the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
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

    Removes the specified tags from the specified resource.

    :param resource_arn: The Amazon Resource Name (ARN) of the resource.
    :type resource_arn: str
    :param tag_keys: The tag keys of the tags to remove.
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


async def update_access_log_subscription(request: web.Request, access_log_subscription_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_access_log_subscription

    Updates the specified access log subscription.

    :param access_log_subscription_identifier: The ID or Amazon Resource Name (ARN) of the access log subscription.
    :type access_log_subscription_identifier: str
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
    body = UpdateAccessLogSubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def update_listener(request: web.Request, listener_identifier, service_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_listener

    Updates the specified listener for the specified service.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    body = UpdateListenerRequest.from_dict(body)
    return web.Response(status=200)


async def update_rule(request: web.Request, listener_identifier, rule_identifier, service_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rule

    Updates a rule for the listener. You can&#39;t modify a default listener rule. To modify a default listener rule, use &lt;code&gt;UpdateListener&lt;/code&gt;.

    :param listener_identifier: The ID or Amazon Resource Name (ARN) of the listener.
    :type listener_identifier: str
    :param rule_identifier: The ID or Amazon Resource Name (ARN) of the rule.
    :type rule_identifier: str
    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    body = UpdateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_service(request: web.Request, service_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service

    Updates the specified service.

    :param service_identifier: The ID or Amazon Resource Name (ARN) of the service.
    :type service_identifier: str
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
    body = UpdateServiceRequest.from_dict(body)
    return web.Response(status=200)


async def update_service_network(request: web.Request, service_network_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_network

    Updates the specified service network.

    :param service_network_identifier: The ID or Amazon Resource Name (ARN) of the service network.
    :type service_network_identifier: str
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
    body = UpdateServiceNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def update_service_network_vpc_association(request: web.Request, service_network_vpc_association_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_service_network_vpc_association

    Updates the service network and VPC association. If you add a security group to the service network and VPC association, the association must continue to always have at least one security group. You can add or edit security groups at any time. However, to remove all security groups, you must first delete the association and recreate it without security groups.

    :param service_network_vpc_association_identifier: The ID or Amazon Resource Name (ARN) of the association.
    :type service_network_vpc_association_identifier: str
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
    body = UpdateServiceNetworkVpcAssociationRequest.from_dict(body)
    return web.Response(status=200)


async def update_target_group(request: web.Request, target_group_identifier, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_target_group

    Updates the specified target group.

    :param target_group_identifier: The ID or Amazon Resource Name (ARN) of the target group.
    :type target_group_identifier: str
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
    body = UpdateTargetGroupRequest.from_dict(body)
    return web.Response(status=200)
