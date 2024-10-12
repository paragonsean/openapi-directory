from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_firewall_policy_request import AssociateFirewallPolicyRequest
from openapi_server.models.associate_firewall_policy_response import AssociateFirewallPolicyResponse
from openapi_server.models.associate_subnets_request import AssociateSubnetsRequest
from openapi_server.models.associate_subnets_response import AssociateSubnetsResponse
from openapi_server.models.create_firewall_policy_request import CreateFirewallPolicyRequest
from openapi_server.models.create_firewall_policy_response import CreateFirewallPolicyResponse
from openapi_server.models.create_firewall_request import CreateFirewallRequest
from openapi_server.models.create_firewall_response import CreateFirewallResponse
from openapi_server.models.create_rule_group_request import CreateRuleGroupRequest
from openapi_server.models.create_rule_group_response import CreateRuleGroupResponse
from openapi_server.models.create_tls_inspection_configuration_request import CreateTLSInspectionConfigurationRequest
from openapi_server.models.create_tls_inspection_configuration_response import CreateTLSInspectionConfigurationResponse
from openapi_server.models.delete_firewall_policy_request import DeleteFirewallPolicyRequest
from openapi_server.models.delete_firewall_policy_response import DeleteFirewallPolicyResponse
from openapi_server.models.delete_firewall_request import DeleteFirewallRequest
from openapi_server.models.delete_firewall_response import DeleteFirewallResponse
from openapi_server.models.delete_resource_policy_request import DeleteResourcePolicyRequest
from openapi_server.models.delete_rule_group_request import DeleteRuleGroupRequest
from openapi_server.models.delete_rule_group_response import DeleteRuleGroupResponse
from openapi_server.models.delete_tls_inspection_configuration_request import DeleteTLSInspectionConfigurationRequest
from openapi_server.models.delete_tls_inspection_configuration_response import DeleteTLSInspectionConfigurationResponse
from openapi_server.models.describe_firewall_policy_request import DescribeFirewallPolicyRequest
from openapi_server.models.describe_firewall_policy_response import DescribeFirewallPolicyResponse
from openapi_server.models.describe_firewall_request import DescribeFirewallRequest
from openapi_server.models.describe_firewall_response import DescribeFirewallResponse
from openapi_server.models.describe_logging_configuration_request import DescribeLoggingConfigurationRequest
from openapi_server.models.describe_logging_configuration_response import DescribeLoggingConfigurationResponse
from openapi_server.models.describe_resource_policy_request import DescribeResourcePolicyRequest
from openapi_server.models.describe_resource_policy_response import DescribeResourcePolicyResponse
from openapi_server.models.describe_rule_group_metadata_request import DescribeRuleGroupMetadataRequest
from openapi_server.models.describe_rule_group_metadata_response import DescribeRuleGroupMetadataResponse
from openapi_server.models.describe_rule_group_request import DescribeRuleGroupRequest
from openapi_server.models.describe_rule_group_response import DescribeRuleGroupResponse
from openapi_server.models.describe_tls_inspection_configuration_request import DescribeTLSInspectionConfigurationRequest
from openapi_server.models.describe_tls_inspection_configuration_response import DescribeTLSInspectionConfigurationResponse
from openapi_server.models.disassociate_subnets_request import DisassociateSubnetsRequest
from openapi_server.models.disassociate_subnets_response import DisassociateSubnetsResponse
from openapi_server.models.list_firewall_policies_request import ListFirewallPoliciesRequest
from openapi_server.models.list_firewall_policies_response import ListFirewallPoliciesResponse
from openapi_server.models.list_firewalls_request import ListFirewallsRequest
from openapi_server.models.list_firewalls_response import ListFirewallsResponse
from openapi_server.models.list_rule_groups_request import ListRuleGroupsRequest
from openapi_server.models.list_rule_groups_response import ListRuleGroupsResponse
from openapi_server.models.list_tls_inspection_configurations_request import ListTLSInspectionConfigurationsRequest
from openapi_server.models.list_tls_inspection_configurations_response import ListTLSInspectionConfigurationsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_resource_policy_request import PutResourcePolicyRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_firewall_delete_protection_request import UpdateFirewallDeleteProtectionRequest
from openapi_server.models.update_firewall_delete_protection_response import UpdateFirewallDeleteProtectionResponse
from openapi_server.models.update_firewall_description_request import UpdateFirewallDescriptionRequest
from openapi_server.models.update_firewall_description_response import UpdateFirewallDescriptionResponse
from openapi_server.models.update_firewall_encryption_configuration_request import UpdateFirewallEncryptionConfigurationRequest
from openapi_server.models.update_firewall_encryption_configuration_response import UpdateFirewallEncryptionConfigurationResponse
from openapi_server.models.update_firewall_policy_change_protection_request import UpdateFirewallPolicyChangeProtectionRequest
from openapi_server.models.update_firewall_policy_change_protection_response import UpdateFirewallPolicyChangeProtectionResponse
from openapi_server.models.update_firewall_policy_request import UpdateFirewallPolicyRequest
from openapi_server.models.update_firewall_policy_response import UpdateFirewallPolicyResponse
from openapi_server.models.update_logging_configuration_request import UpdateLoggingConfigurationRequest
from openapi_server.models.update_logging_configuration_response import UpdateLoggingConfigurationResponse
from openapi_server.models.update_rule_group_request import UpdateRuleGroupRequest
from openapi_server.models.update_rule_group_response import UpdateRuleGroupResponse
from openapi_server.models.update_subnet_change_protection_request import UpdateSubnetChangeProtectionRequest
from openapi_server.models.update_subnet_change_protection_response import UpdateSubnetChangeProtectionResponse
from openapi_server.models.update_tls_inspection_configuration_request import UpdateTLSInspectionConfigurationRequest
from openapi_server.models.update_tls_inspection_configuration_response import UpdateTLSInspectionConfigurationResponse
from openapi_server import util


async def associate_firewall_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_firewall_policy

    &lt;p&gt;Associates a &lt;a&gt;FirewallPolicy&lt;/a&gt; to a &lt;a&gt;Firewall&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;A firewall policy defines how to monitor and manage your VPC network traffic, using a collection of inspection rule groups and other settings. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls. &lt;/p&gt;

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
    body = AssociateFirewallPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def associate_subnets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_subnets

    &lt;p&gt;Associates the specified subnets in the Amazon VPC to the firewall. You can specify one subnet for each of the Availability Zones that the VPC spans. &lt;/p&gt; &lt;p&gt;This request creates an Network Firewall firewall endpoint in each of the subnets. To enable the firewall&#39;s protections, you must also modify the VPC&#39;s route tables for each subnet&#39;s Availability Zone, to redirect the traffic that&#39;s coming into and going out of the zone through the firewall endpoint. &lt;/p&gt;

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
    body = AssociateSubnetsRequest.from_dict(body)
    return web.Response(status=200)


async def create_firewall(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_firewall

    &lt;p&gt;Creates an Network Firewall &lt;a&gt;Firewall&lt;/a&gt; and accompanying &lt;a&gt;FirewallStatus&lt;/a&gt; for a VPC. &lt;/p&gt; &lt;p&gt;The firewall defines the configuration settings for an Network Firewall firewall. The settings that you can define at creation include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall Amazon Web Services resource. &lt;/p&gt; &lt;p&gt;After you create a firewall, you can provide additional settings, like the logging configuration. &lt;/p&gt; &lt;p&gt;To update the settings for a firewall, you use the operations that apply to the settings themselves, for example &lt;a&gt;UpdateLoggingConfiguration&lt;/a&gt;, &lt;a&gt;AssociateSubnets&lt;/a&gt;, and &lt;a&gt;UpdateFirewallDeleteProtection&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;To manage a firewall&#39;s tags, use the standard Amazon Web Services resource tagging operations, &lt;a&gt;ListTagsForResource&lt;/a&gt;, &lt;a&gt;TagResource&lt;/a&gt;, and &lt;a&gt;UntagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To retrieve information about firewalls, use &lt;a&gt;ListFirewalls&lt;/a&gt; and &lt;a&gt;DescribeFirewall&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateFirewallRequest.from_dict(body)
    return web.Response(status=200)


async def create_firewall_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_firewall_policy

    &lt;p&gt;Creates the firewall policy for the firewall according to the specifications. &lt;/p&gt; &lt;p&gt;An Network Firewall firewall policy defines the behavior of a firewall, in a collection of stateless and stateful rule groups and other settings. You can use one firewall policy for multiple firewalls. &lt;/p&gt;

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
    body = CreateFirewallPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rule_group

    &lt;p&gt;Creates the specified stateless or stateful rule group, which includes the rules for network traffic inspection, a capacity setting, and tags. &lt;/p&gt; &lt;p&gt;You provide your rule group specification in your request using either &lt;code&gt;RuleGroup&lt;/code&gt; or &lt;code&gt;Rules&lt;/code&gt;.&lt;/p&gt;

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
    body = CreateRuleGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_tls_inspection_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_tls_inspection_configuration

    &lt;p&gt;Creates an Network Firewall TLS inspection configuration. A TLS inspection configuration contains the Certificate Manager certificate references that Network Firewall uses to decrypt and re-encrypt inbound traffic.&lt;/p&gt; &lt;p&gt;After you create a TLS inspection configuration, you associate it with a firewall policy.&lt;/p&gt; &lt;p&gt;To update the settings for a TLS inspection configuration, use &lt;a&gt;UpdateTLSInspectionConfiguration&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To manage a TLS inspection configuration&#39;s tags, use the standard Amazon Web Services resource tagging operations, &lt;a&gt;ListTagsForResource&lt;/a&gt;, &lt;a&gt;TagResource&lt;/a&gt;, and &lt;a&gt;UntagResource&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To retrieve information about TLS inspection configurations, use &lt;a&gt;ListTLSInspectionConfigurations&lt;/a&gt; and &lt;a&gt;DescribeTLSInspectionConfiguration&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; For more information about TLS inspection configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html\&quot;&gt;Decrypting SSL/TLS traffic with TLS inspection configurations&lt;/a&gt; in the &lt;i&gt;Network Firewall Developer Guide&lt;/i&gt;. &lt;/p&gt;

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
    body = CreateTLSInspectionConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_firewall(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_firewall

    &lt;p&gt;Deletes the specified &lt;a&gt;Firewall&lt;/a&gt; and its &lt;a&gt;FirewallStatus&lt;/a&gt;. This operation requires the firewall&#39;s &lt;code&gt;DeleteProtection&lt;/code&gt; flag to be &lt;code&gt;FALSE&lt;/code&gt;. You can&#39;t revert this operation. &lt;/p&gt; &lt;p&gt;You can check whether a firewall is in use by reviewing the route tables for the Availability Zones where you have firewall subnet mappings. Retrieve the subnet mappings by calling &lt;a&gt;DescribeFirewall&lt;/a&gt;. You define and update the route tables through Amazon VPC. As needed, update the route tables for the zones to remove the firewall endpoints. When the route tables no longer use the firewall endpoints, you can remove the firewall safely.&lt;/p&gt; &lt;p&gt;To delete a firewall, remove the delete protection if you need to using &lt;a&gt;UpdateFirewallDeleteProtection&lt;/a&gt;, then delete the firewall by calling &lt;a&gt;DeleteFirewall&lt;/a&gt;. &lt;/p&gt;

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
    body = DeleteFirewallRequest.from_dict(body)
    return web.Response(status=200)


async def delete_firewall_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_firewall_policy

    Deletes the specified &lt;a&gt;FirewallPolicy&lt;/a&gt;. 

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
    body = DeleteFirewallPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_resource_policy

    Deletes a resource policy that you created in a &lt;a&gt;PutResourcePolicy&lt;/a&gt; request. 

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
    body = DeleteResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rule_group

    Deletes the specified &lt;a&gt;RuleGroup&lt;/a&gt;. 

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
    body = DeleteRuleGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_tls_inspection_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_tls_inspection_configuration

    Deletes the specified &lt;a&gt;TLSInspectionConfiguration&lt;/a&gt;.

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
    body = DeleteTLSInspectionConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_firewall(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_firewall

    Returns the data objects for the specified firewall. 

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
    body = DescribeFirewallRequest.from_dict(body)
    return web.Response(status=200)


async def describe_firewall_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_firewall_policy

    Returns the data objects for the specified firewall policy. 

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
    body = DescribeFirewallPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_logging_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_logging_configuration

    Returns the logging configuration for the specified firewall. 

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
    body = DescribeLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def describe_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_resource_policy

    Retrieves a resource policy that you created in a &lt;a&gt;PutResourcePolicy&lt;/a&gt; request. 

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
    body = DescribeResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_rule_group

    Returns the data objects for the specified rule group. 

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
    body = DescribeRuleGroupRequest.from_dict(body)
    return web.Response(status=200)


async def describe_rule_group_metadata(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_rule_group_metadata

    High-level information about a rule group, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a rule group. You can retrieve all objects for a rule group by calling &lt;a&gt;DescribeRuleGroup&lt;/a&gt;. 

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
    body = DescribeRuleGroupMetadataRequest.from_dict(body)
    return web.Response(status=200)


async def describe_tls_inspection_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_tls_inspection_configuration

    Returns the data objects for the specified TLS inspection configuration.

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
    body = DescribeTLSInspectionConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_subnets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_subnets

    Removes the specified subnet associations from the firewall. This removes the firewall endpoints from the subnets and removes any network filtering protections that the endpoints were providing. 

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
    body = DisassociateSubnetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_firewall_policies(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_firewall_policies

    Retrieves the metadata for the firewall policies that you have defined. Depending on your setting for max results and the number of firewall policies, a single call might not return the full list. 

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
    body = ListFirewallPoliciesRequest.from_dict(body)
    return web.Response(status=200)


async def list_firewalls(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_firewalls

    &lt;p&gt;Retrieves the metadata for the firewalls that you have defined. If you provide VPC identifiers in your request, this returns only the firewalls for those VPCs.&lt;/p&gt; &lt;p&gt;Depending on your setting for max results and the number of firewalls, a single call might not return the full list. &lt;/p&gt;

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
    body = ListFirewallsRequest.from_dict(body)
    return web.Response(status=200)


async def list_rule_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_rule_groups

    Retrieves the metadata for the rule groups that you have defined. Depending on your setting for max results and the number of rule groups, a single call might not return the full list. 

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
    body = ListRuleGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Retrieves the tags associated with the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to \&quot;customer\&quot; and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.&lt;/p&gt; &lt;p&gt;You can tag the Amazon Web Services resources that you manage through Network Firewall: firewalls, firewall policies, and rule groups. &lt;/p&gt;

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


async def list_tls_inspection_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_tls_inspection_configurations

    Retrieves the metadata for the TLS inspection configurations that you have defined. Depending on your setting for max results and the number of TLS inspection configurations, a single call might not return the full list.

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
    body = ListTLSInspectionConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def put_resource_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_resource_policy

    &lt;p&gt;Creates or updates an IAM policy for your rule group or firewall policy. Use this to share rule groups and firewall policies between accounts. This operation works in conjunction with the Amazon Web Services Resource Access Manager (RAM) service to manage resource sharing for Network Firewall. &lt;/p&gt; &lt;p&gt;Use this operation to create or update a resource policy for your rule group or firewall policy. In the policy, you specify the accounts that you want to share the resource with and the operations that you want the accounts to be able to perform. &lt;/p&gt; &lt;p&gt;When you add an account in the resource policy, you then run the following Resource Access Manager (RAM) operations to access and accept the shared rule group or firewall policy. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ram/latest/APIReference/API_GetResourceShareInvitations.html\&quot;&gt;GetResourceShareInvitations&lt;/a&gt; - Returns the Amazon Resource Names (ARNs) of the resource share invitations. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ram/latest/APIReference/API_AcceptResourceShareInvitation.html\&quot;&gt;AcceptResourceShareInvitation&lt;/a&gt; - Accepts the share invitation for a specified resource share. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For additional information about resource sharing using RAM, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ram/latest/userguide/what-is.html\&quot;&gt;Resource Access Manager User Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = PutResourcePolicyRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;p&gt;Adds the specified tags to the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to \&quot;customer\&quot; and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.&lt;/p&gt; &lt;p&gt;You can tag the Amazon Web Services resources that you manage through Network Firewall: firewalls, firewall policies, and rule groups. &lt;/p&gt;

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

    &lt;p&gt;Removes the tags with the specified keys from the specified resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to \&quot;customer\&quot; and the value to the customer name or ID. You can specify one or more tags to add to each Amazon Web Services resource, up to 50 tags for a resource.&lt;/p&gt; &lt;p&gt;You can manage tags for the Amazon Web Services resources that you manage through Network Firewall: firewalls, firewall policies, and rule groups. &lt;/p&gt;

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


async def update_firewall_delete_protection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_firewall_delete_protection

    Modifies the flag, &lt;code&gt;DeleteProtection&lt;/code&gt;, which indicates whether it is possible to delete the firewall. If the flag is set to &lt;code&gt;TRUE&lt;/code&gt;, the firewall is protected against deletion. This setting helps protect against accidentally deleting a firewall that&#39;s in use. 

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
    body = UpdateFirewallDeleteProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_firewall_description(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_firewall_description

    Modifies the description for the specified firewall. Use the description to help you identify the firewall when you&#39;re working with it. 

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
    body = UpdateFirewallDescriptionRequest.from_dict(body)
    return web.Response(status=200)


async def update_firewall_encryption_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_firewall_encryption_configuration

    A complex type that contains settings for encryption of your firewall resources.

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
    body = UpdateFirewallEncryptionConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_firewall_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_firewall_policy

    Updates the properties of the specified firewall policy.

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
    body = UpdateFirewallPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_firewall_policy_change_protection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_firewall_policy_change_protection

    Modifies the flag, &lt;code&gt;ChangeProtection&lt;/code&gt;, which indicates whether it is possible to change the firewall. If the flag is set to &lt;code&gt;TRUE&lt;/code&gt;, the firewall is protected from changes. This setting helps protect against accidentally changing a firewall that&#39;s in use.

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
    body = UpdateFirewallPolicyChangeProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_logging_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_logging_configuration

    &lt;p&gt;Sets the logging configuration for the specified firewall. &lt;/p&gt; &lt;p&gt;To change the logging configuration, retrieve the &lt;a&gt;LoggingConfiguration&lt;/a&gt; by calling &lt;a&gt;DescribeLoggingConfiguration&lt;/a&gt;, then change it and provide the modified object to this update call. You must change the logging configuration one &lt;a&gt;LogDestinationConfig&lt;/a&gt; at a time inside the retrieved &lt;a&gt;LoggingConfiguration&lt;/a&gt; object. &lt;/p&gt; &lt;p&gt;You can perform only one of the following actions in any call to &lt;code&gt;UpdateLoggingConfiguration&lt;/code&gt;: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Create a new log destination object by adding a single &lt;code&gt;LogDestinationConfig&lt;/code&gt; array element to &lt;code&gt;LogDestinationConfigs&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Delete a log destination object by removing a single &lt;code&gt;LogDestinationConfig&lt;/code&gt; array element from &lt;code&gt;LogDestinationConfigs&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change the &lt;code&gt;LogDestination&lt;/code&gt; setting in a single &lt;code&gt;LogDestinationConfig&lt;/code&gt; array element.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can&#39;t change the &lt;code&gt;LogDestinationType&lt;/code&gt; or &lt;code&gt;LogType&lt;/code&gt; in a &lt;code&gt;LogDestinationConfig&lt;/code&gt;. To change these settings, delete the existing &lt;code&gt;LogDestinationConfig&lt;/code&gt; object and create a new one, using two separate calls to this update operation.&lt;/p&gt;

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
    body = UpdateLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rule_group

    &lt;p&gt;Updates the rule settings for the specified rule group. You use a rule group by reference in one or more firewall policies. When you modify a rule group, you modify all firewall policies that use the rule group. &lt;/p&gt; &lt;p&gt;To update a rule group, first call &lt;a&gt;DescribeRuleGroup&lt;/a&gt; to retrieve the current &lt;a&gt;RuleGroup&lt;/a&gt; object, update the object as needed, and then provide the updated object to this call. &lt;/p&gt;

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
    body = UpdateRuleGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_subnet_change_protection(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_subnet_change_protection

    &lt;p/&gt;

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
    body = UpdateSubnetChangeProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_tls_inspection_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_tls_inspection_configuration

    &lt;p&gt;Updates the TLS inspection configuration settings for the specified TLS inspection configuration. You use a TLS inspection configuration by reference in one or more firewall policies. When you modify a TLS inspection configuration, you modify all firewall policies that use the TLS inspection configuration. &lt;/p&gt; &lt;p&gt;To update a TLS inspection configuration, first call &lt;a&gt;DescribeTLSInspectionConfiguration&lt;/a&gt; to retrieve the current &lt;a&gt;TLSInspectionConfiguration&lt;/a&gt; object, update the object as needed, and then provide the updated object to this call. &lt;/p&gt;

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
    body = UpdateTLSInspectionConfigurationRequest.from_dict(body)
    return web.Response(status=200)
