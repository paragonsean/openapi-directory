from typing import List, Dict
from aiohttp import web

from openapi_server.models.action import Action
from openapi_server.models.add_listener_certificates_input import AddListenerCertificatesInput
from openapi_server.models.add_listener_certificates_output import AddListenerCertificatesOutput
from openapi_server.models.add_tags_input import AddTagsInput
from openapi_server.models.certificate import Certificate
from openapi_server.models.create_listener_input import CreateListenerInput
from openapi_server.models.create_listener_output import CreateListenerOutput
from openapi_server.models.create_load_balancer_input import CreateLoadBalancerInput
from openapi_server.models.create_load_balancer_output import CreateLoadBalancerOutput
from openapi_server.models.create_rule_input import CreateRuleInput
from openapi_server.models.create_rule_output import CreateRuleOutput
from openapi_server.models.create_target_group_input import CreateTargetGroupInput
from openapi_server.models.create_target_group_output import CreateTargetGroupOutput
from openapi_server.models.delete_listener_input import DeleteListenerInput
from openapi_server.models.delete_load_balancer_input import DeleteLoadBalancerInput
from openapi_server.models.delete_rule_input import DeleteRuleInput
from openapi_server.models.delete_target_group_input import DeleteTargetGroupInput
from openapi_server.models.deregister_targets_input import DeregisterTargetsInput
from openapi_server.models.describe_account_limits_input import DescribeAccountLimitsInput
from openapi_server.models.describe_account_limits_output import DescribeAccountLimitsOutput
from openapi_server.models.describe_listener_certificates_input import DescribeListenerCertificatesInput
from openapi_server.models.describe_listener_certificates_output import DescribeListenerCertificatesOutput
from openapi_server.models.describe_listeners_input import DescribeListenersInput
from openapi_server.models.describe_listeners_output import DescribeListenersOutput
from openapi_server.models.describe_load_balancer_attributes_input import DescribeLoadBalancerAttributesInput
from openapi_server.models.describe_load_balancer_attributes_output import DescribeLoadBalancerAttributesOutput
from openapi_server.models.describe_load_balancers_input import DescribeLoadBalancersInput
from openapi_server.models.describe_load_balancers_output import DescribeLoadBalancersOutput
from openapi_server.models.describe_rules_input import DescribeRulesInput
from openapi_server.models.describe_rules_output import DescribeRulesOutput
from openapi_server.models.describe_ssl_policies_input import DescribeSSLPoliciesInput
from openapi_server.models.describe_ssl_policies_output import DescribeSSLPoliciesOutput
from openapi_server.models.describe_tags_input import DescribeTagsInput
from openapi_server.models.describe_tags_output import DescribeTagsOutput
from openapi_server.models.describe_target_group_attributes_input import DescribeTargetGroupAttributesInput
from openapi_server.models.describe_target_group_attributes_output import DescribeTargetGroupAttributesOutput
from openapi_server.models.describe_target_groups_input import DescribeTargetGroupsInput
from openapi_server.models.describe_target_groups_output import DescribeTargetGroupsOutput
from openapi_server.models.describe_target_health_input import DescribeTargetHealthInput
from openapi_server.models.describe_target_health_output import DescribeTargetHealthOutput
from openapi_server.models.get_create_target_group_matcher_parameter import GETCreateTargetGroupMatcherParameter
from openapi_server.models.load_balancer_attribute import LoadBalancerAttribute
from openapi_server.models.modify_listener_input import ModifyListenerInput
from openapi_server.models.modify_listener_output import ModifyListenerOutput
from openapi_server.models.modify_load_balancer_attributes_input import ModifyLoadBalancerAttributesInput
from openapi_server.models.modify_load_balancer_attributes_output import ModifyLoadBalancerAttributesOutput
from openapi_server.models.modify_rule_input import ModifyRuleInput
from openapi_server.models.modify_rule_output import ModifyRuleOutput
from openapi_server.models.modify_target_group_attributes_input import ModifyTargetGroupAttributesInput
from openapi_server.models.modify_target_group_attributes_output import ModifyTargetGroupAttributesOutput
from openapi_server.models.modify_target_group_input import ModifyTargetGroupInput
from openapi_server.models.modify_target_group_output import ModifyTargetGroupOutput
from openapi_server.models.register_targets_input import RegisterTargetsInput
from openapi_server.models.remove_listener_certificates_input import RemoveListenerCertificatesInput
from openapi_server.models.remove_tags_input import RemoveTagsInput
from openapi_server.models.rule_condition import RuleCondition
from openapi_server.models.rule_priority_pair import RulePriorityPair
from openapi_server.models.set_ip_address_type_input import SetIpAddressTypeInput
from openapi_server.models.set_ip_address_type_output import SetIpAddressTypeOutput
from openapi_server.models.set_rule_priorities_input import SetRulePrioritiesInput
from openapi_server.models.set_rule_priorities_output import SetRulePrioritiesOutput
from openapi_server.models.set_security_groups_input import SetSecurityGroupsInput
from openapi_server.models.set_security_groups_output import SetSecurityGroupsOutput
from openapi_server.models.set_subnets_input import SetSubnetsInput
from openapi_server.models.set_subnets_output import SetSubnetsOutput
from openapi_server.models.subnet_mapping import SubnetMapping
from openapi_server.models.tag import Tag
from openapi_server.models.target_description import TargetDescription
from openapi_server.models.target_group_attribute import TargetGroupAttribute
from openapi_server import util


async def g_et_add_listener_certificates(request: web.Request, listener_arn, certificates, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_listener_certificates

    &lt;p&gt;Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener.&lt;/p&gt; &lt;p&gt;If the certificate in already in the certificate list, the call is successful but the certificate is not added again.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html\&quot;&gt;HTTPS listeners&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html\&quot;&gt;TLS listeners&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param listener_arn: The Amazon Resource Name (ARN) of the listener.
    :type listener_arn: str
    :param certificates: The certificate to add. You can specify one certificate per call. Set &lt;code&gt;CertificateArn&lt;/code&gt; to the certificate ARN but do not set &lt;code&gt;IsDefault&lt;/code&gt;.
    :type certificates: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    certificates = [Certificate.from_dict(d) for d in certificates]
    return web.Response(status=200)


async def g_et_add_tags(request: web.Request, resource_arns, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_tags

    &lt;p&gt;Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, and rules.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and an optional value. If a resource already has a tag with the same key, &lt;code&gt;AddTags&lt;/code&gt; updates its value.&lt;/p&gt;

    :param resource_arns: The Amazon Resource Name (ARN) of the resource.
    :type resource_arns: List[str]
    :param tags: The tags.
    :type tags: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_listener(request: web.Request, load_balancer_arn, default_actions, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, protocol=None, port=None, ssl_policy=None, certificates=None, alpn_policy=None, tags=None) -> web.Response:
    """g_et_create_listener

    &lt;p&gt;Creates a listener for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html\&quot;&gt;Listeners for your Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html\&quot;&gt;Listeners for your Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html\&quot;&gt;Listeners for your Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.&lt;/p&gt;

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param default_actions: The actions for the default rule.
    :type default_actions: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param protocol: The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, and TCP_UDP. You can’t specify the UDP or TCP_UDP protocol if dual-stack mode is enabled. You cannot specify a protocol for a Gateway Load Balancer.
    :type protocol: str
    :param port: The port on which the load balancer is listening. You cannot specify a port for a Gateway Load Balancer.
    :type port: int
    :param ssl_policy: &lt;p&gt;[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;
    :type ssl_policy: str
    :param certificates: [HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set &lt;code&gt;CertificateArn&lt;/code&gt; to the certificate ARN but do not set &lt;code&gt;IsDefault&lt;/code&gt;.
    :type certificates: list | bytes
    :param alpn_policy: &lt;p&gt;[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP1Only&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP2Only&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP2Optional&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP2Preferred&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;None&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#alpn-policies\&quot;&gt;ALPN policies&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;
    :type alpn_policy: List[str]
    :param tags: The tags to assign to the listener.
    :type tags: list | bytes

    """
    default_actions = [Action.from_dict(d) for d in default_actions]
    certificates = [Certificate.from_dict(d) for d in certificates]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_load_balancer(request: web.Request, name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, subnets=None, subnet_mappings=None, security_groups=None, scheme=None, tags=None, type=None, ip_address_type=None, customer_owned_ipv4_pool=None) -> web.Response:
    """g_et_create_load_balancer

    &lt;p&gt;Creates an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html\&quot;&gt;Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html\&quot;&gt;Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html\&quot;&gt;Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.&lt;/p&gt;

    :param name: &lt;p&gt;The name of the load balancer.&lt;/p&gt; &lt;p&gt;This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, must not begin or end with a hyphen, and must not begin with \&quot;internal-\&quot;.&lt;/p&gt;
    :type name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param subnets: &lt;p&gt;The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both. To specify an Elastic IP address, specify subnet mappings instead of subnets.&lt;/p&gt; &lt;p&gt;[Application Load Balancers] You must specify subnets from at least two Availability Zones.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Outposts] You must specify one Outpost subnet.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.&lt;/p&gt; &lt;p&gt;[Network Load Balancers] You can specify subnets from one or more Availability Zones.&lt;/p&gt; &lt;p&gt;[Gateway Load Balancers] You can specify subnets from one or more Availability Zones.&lt;/p&gt;
    :type subnets: List[str]
    :param subnet_mappings: &lt;p&gt;The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings, but not both.&lt;/p&gt; &lt;p&gt;[Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Outposts] You must specify one Outpost subnet.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.&lt;/p&gt; &lt;p&gt;[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.&lt;/p&gt; &lt;p&gt;[Gateway Load Balancers] You can specify subnets from one or more Availability Zones. You cannot specify Elastic IP addresses for your subnets.&lt;/p&gt;
    :type subnet_mappings: list | bytes
    :param security_groups: [Application Load Balancers] The IDs of the security groups for the load balancer.
    :type security_groups: List[str]
    :param scheme: &lt;p&gt;The nodes of an Internet-facing load balancer have public IP addresses. The DNS name of an Internet-facing load balancer is publicly resolvable to the public IP addresses of the nodes. Therefore, Internet-facing load balancers can route requests from clients over the internet.&lt;/p&gt; &lt;p&gt;The nodes of an internal load balancer have only private IP addresses. The DNS name of an internal load balancer is publicly resolvable to the private IP addresses of the nodes. Therefore, internal load balancers can route requests only from clients with access to the VPC for the load balancer.&lt;/p&gt; &lt;p&gt;The default is an Internet-facing load balancer.&lt;/p&gt; &lt;p&gt;You cannot specify a scheme for a Gateway Load Balancer.&lt;/p&gt;
    :type scheme: str
    :param tags: The tags to assign to the load balancer.
    :type tags: list | bytes
    :param type: The type of load balancer. The default is &lt;code&gt;application&lt;/code&gt;.
    :type type: str
    :param ip_address_type: The type of IP addresses used by the subnets for your load balancer. The possible values are &lt;code&gt;ipv4&lt;/code&gt; (for IPv4 addresses) and &lt;code&gt;dualstack&lt;/code&gt; (for IPv4 and IPv6 addresses). 
    :type ip_address_type: str
    :param customer_owned_ipv4_pool: [Application Load Balancers on Outposts] The ID of the customer-owned address pool (CoIP pool).
    :type customer_owned_ipv4_pool: str

    """
    subnet_mappings = [SubnetMapping.from_dict(d) for d in subnet_mappings]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_rule(request: web.Request, listener_arn, conditions, priority, actions, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, tags=None) -> web.Response:
    """g_et_create_rule

    &lt;p&gt;Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer.&lt;/p&gt; &lt;p&gt;Each rule consists of a priority, one or more actions, and one or more conditions. Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, its actions are performed. If the conditions for no rules are met, the actions for the default rule are performed. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param listener_arn: The Amazon Resource Name (ARN) of the listener.
    :type listener_arn: str
    :param conditions: The conditions.
    :type conditions: list | bytes
    :param priority: The rule priority. A listener can&#39;t have multiple rules with the same priority.
    :type priority: int
    :param actions: The actions.
    :type actions: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param tags: The tags to assign to the rule.
    :type tags: list | bytes

    """
    conditions = [RuleCondition.from_dict(d) for d in conditions]
    actions = [Action.from_dict(d) for d in actions]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_target_group(request: web.Request, name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, protocol=None, protocol_version=None, port=None, vpc_id=None, health_check_protocol=None, health_check_port=None, health_check_enabled=None, health_check_path=None, health_check_interval_seconds=None, health_check_timeout_seconds=None, healthy_threshold_count=None, unhealthy_threshold_count=None, matcher=None, target_type=None, tags=None, ip_address_type=None) -> web.Response:
    """g_et_create_target_group

    &lt;p&gt;Creates a target group.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html\&quot;&gt;Target groups for your Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html\&quot;&gt;Target groups for your Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html\&quot;&gt;Target groups for your Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.&lt;/p&gt;

    :param name: &lt;p&gt;The name of the target group.&lt;/p&gt; &lt;p&gt;This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.&lt;/p&gt;
    :type name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param protocol: The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, or TCP_UDP. For Gateway Load Balancers, the supported protocol is GENEVE. A TCP_UDP listener must be associated with a TCP_UDP target group. If the target is a Lambda function, this parameter does not apply.
    :type protocol: str
    :param protocol_version: [HTTP/HTTPS protocol] The protocol version. Specify &lt;code&gt;GRPC&lt;/code&gt; to send requests to targets using gRPC. Specify &lt;code&gt;HTTP2&lt;/code&gt; to send requests to targets using HTTP/2. The default is &lt;code&gt;HTTP1&lt;/code&gt;, which sends requests to targets using HTTP/1.1.
    :type protocol_version: str
    :param port: The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.
    :type port: int
    :param vpc_id: The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply. Otherwise, this parameter is required.
    :type vpc_id: str
    :param health_check_protocol: The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. The GENEVE, TLS, UDP, and TCP_UDP protocols are not supported for health checks.
    :type health_check_protocol: str
    :param health_check_port: The port the load balancer uses when performing health checks on targets. If the protocol is HTTP, HTTPS, TCP, TLS, UDP, or TCP_UDP, the default is &lt;code&gt;traffic-port&lt;/code&gt;, which is the port on which each target receives traffic from the load balancer. If the protocol is GENEVE, the default is port 80.
    :type health_check_port: str
    :param health_check_enabled: Indicates whether health checks are enabled. If the target type is &lt;code&gt;lambda&lt;/code&gt;, health checks are disabled by default but can be enabled. If the target type is &lt;code&gt;instance&lt;/code&gt;, &lt;code&gt;ip&lt;/code&gt;, or &lt;code&gt;alb&lt;/code&gt;, health checks are always enabled and cannot be disabled.
    :type health_check_enabled: bool
    :param health_check_path: &lt;p&gt;[HTTP/HTTPS health checks] The destination for health checks on the targets.&lt;/p&gt; &lt;p&gt;[HTTP1 or HTTP2 protocol version] The ping path. The default is /.&lt;/p&gt; &lt;p&gt;[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.&lt;/p&gt;
    :type health_check_path: str
    :param health_check_interval_seconds: The approximate amount of time, in seconds, between health checks of an individual target. The range is 5-300. If the target group protocol is TCP, TLS, UDP, TCP_UDP, HTTP or HTTPS, the default is 30 seconds. If the target group protocol is GENEVE, the default is 10 seconds. If the target type is &lt;code&gt;lambda&lt;/code&gt;, the default is 35 seconds.
    :type health_check_interval_seconds: int
    :param health_check_timeout_seconds: The amount of time, in seconds, during which no response from a target means a failed health check. The range is 2–120 seconds. For target groups with a protocol of HTTP, the default is 6 seconds. For target groups with a protocol of TCP, TLS or HTTPS, the default is 10 seconds. For target groups with a protocol of GENEVE, the default is 5 seconds. If the target type is &lt;code&gt;lambda&lt;/code&gt;, the default is 30 seconds.
    :type health_check_timeout_seconds: int
    :param healthy_threshold_count: The number of consecutive health check successes required before considering a target healthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, HTTP or HTTPS, the default is 5. For target groups with a protocol of GENEVE, the default is 5. If the target type is &lt;code&gt;lambda&lt;/code&gt;, the default is 5.
    :type healthy_threshold_count: int
    :param unhealthy_threshold_count: The number of consecutive health check failures required before considering a target unhealthy. The range is 2-10. If the target group protocol is TCP, TCP_UDP, UDP, TLS, HTTP or HTTPS, the default is 2. For target groups with a protocol of GENEVE, the default is 2. If the target type is &lt;code&gt;lambda&lt;/code&gt;, the default is 5.
    :type unhealthy_threshold_count: int
    :param matcher: [HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.
    :type matcher: dict | bytes
    :param target_type: &lt;p&gt;The type of target that you must specify when registering targets with this target group. You can&#39;t specify targets for a target group using more than one target type.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;instance&lt;/code&gt; - Register targets by instance ID. This is the default value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ip&lt;/code&gt; - Register targets by IP address. You can specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can&#39;t specify publicly routable IP addresses.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;lambda&lt;/code&gt; - Register a single Lambda function as a target.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;alb&lt;/code&gt; - Register a single Application Load Balancer as a target.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type target_type: str
    :param tags: The tags to assign to the target group.
    :type tags: list | bytes
    :param ip_address_type: The type of IP address used for this target group. The possible values are &lt;code&gt;ipv4&lt;/code&gt; and &lt;code&gt;ipv6&lt;/code&gt;. This is an optional parameter. If not specified, the IP address type defaults to &lt;code&gt;ipv4&lt;/code&gt;.
    :type ip_address_type: str

    """
    matcher = .from_dict(matcher)
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_delete_listener(request: web.Request, listener_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_listener

    &lt;p&gt;Deletes the specified listener.&lt;/p&gt; &lt;p&gt;Alternatively, your listener is deleted when you delete the load balancer to which it is attached.&lt;/p&gt;

    :param listener_arn: The Amazon Resource Name (ARN) of the listener.
    :type listener_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_delete_load_balancer(request: web.Request, load_balancer_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_load_balancer

    &lt;p&gt;Deletes the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. Deleting a load balancer also deletes its listeners.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.&lt;/p&gt; &lt;p&gt;Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.&lt;/p&gt;

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_delete_rule(request: web.Request, rule_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_rule

    &lt;p&gt;Deletes the specified rule.&lt;/p&gt; &lt;p&gt;You can&#39;t delete the default rule.&lt;/p&gt;

    :param rule_arn: The Amazon Resource Name (ARN) of the rule.
    :type rule_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_delete_target_group(request: web.Request, target_group_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_target_group

    &lt;p&gt;Deletes the specified target group.&lt;/p&gt; &lt;p&gt;You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks. Deleting a target group does not affect its registered targets. For example, any EC2 instances continue to run until you stop or terminate them.&lt;/p&gt;

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_deregister_targets(request: web.Request, target_group_arn, targets, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_deregister_targets

    Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param targets: The targets. If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.
    :type targets: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    targets = [TargetDescription.from_dict(d) for d in targets]
    return web.Response(status=200)


async def g_et_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_account_limits

    &lt;p&gt;Describes the current Elastic Load Balancing resource limits for your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html\&quot;&gt;Quotas for your Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html\&quot;&gt;Quotas for your Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/quotas-limits.html\&quot;&gt;Quotas for your Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_listener_certificates(request: web.Request, listener_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_listener_certificates

    &lt;p&gt;Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.&lt;/p&gt; &lt;p&gt;If the default certificate is also in the certificate list, it appears twice in the results (once with &lt;code&gt;IsDefault&lt;/code&gt; set to true and once with &lt;code&gt;IsDefault&lt;/code&gt; set to false).&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates\&quot;&gt;SSL certificates&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#tls-listener-certificate\&quot;&gt;Server certificates&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param listener_arn: The Amazon Resource Names (ARN) of the listener.
    :type listener_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_listeners(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, load_balancer_arn=None, listener_arns=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_listeners

    Describes the specified listeners or the listeners for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. You must specify either a load balancer or one or more listeners.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param listener_arns: The Amazon Resource Names (ARN) of the listeners.
    :type listener_arns: List[str]
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_load_balancer_attributes(request: web.Request, load_balancer_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_load_balancer_attributes

    &lt;p&gt;Describes the attributes for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes\&quot;&gt;Load balancer attributes&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#load-balancer-attributes\&quot;&gt;Load balancer attributes&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#load-balancer-attributes\&quot;&gt;Load balancer attributes&lt;/a&gt; in the &lt;i&gt;Gateway Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_describe_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, load_balancer_arns=None, names=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_load_balancers

    Describes the specified load balancers or all of your load balancers.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param load_balancer_arns: The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call.
    :type load_balancer_arns: List[str]
    :param names: The names of the load balancers.
    :type names: List[str]
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, listener_arn=None, rule_arns=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_rules

    Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param listener_arn: The Amazon Resource Name (ARN) of the listener.
    :type listener_arn: str
    :param rule_arns: The Amazon Resource Names (ARN) of the rules.
    :type rule_arns: List[str]
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_ssl_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, names=None, marker=None, page_size=None, load_balancer_type=None) -> web.Response:
    """g_et_describe_ssl_policies

    &lt;p&gt;Describes the specified policies or all policies used for SSL negotiation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param names: The names of the policies.
    :type names: List[str]
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int
    :param load_balancer_type:  The type of load balancer. The default lists the SSL policies for all load balancers.
    :type load_balancer_type: str

    """
    return web.Response(status=200)


async def g_et_describe_tags(request: web.Request, resource_arns, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_tags

    Describes the tags for the specified Elastic Load Balancing resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.

    :param resource_arns: The Amazon Resource Names (ARN) of the resources. You can specify up to 20 resources in a single call.
    :type resource_arns: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_describe_target_group_attributes(request: web.Request, target_group_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_target_group_attributes

    &lt;p&gt;Describes the attributes for the specified target group.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-attributes\&quot;&gt;Target group attributes&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-group-attributes\&quot;&gt;Target group attributes&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html#target-group-attributes\&quot;&gt;Target group attributes&lt;/a&gt; in the &lt;i&gt;Gateway Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_describe_target_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, load_balancer_arn=None, target_group_arns=None, names=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_target_groups

    Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param target_group_arns: The Amazon Resource Names (ARN) of the target groups.
    :type target_group_arns: List[str]
    :param names: The names of the target groups.
    :type names: List[str]
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_target_health(request: web.Request, target_group_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, targets=None) -> web.Response:
    """g_et_describe_target_health

    Describes the health of the specified targets or all of your targets.

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param targets: The targets.
    :type targets: list | bytes

    """
    targets = [TargetDescription.from_dict(d) for d in targets]
    return web.Response(status=200)


async def g_et_modify_listener(request: web.Request, listener_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, port=None, protocol=None, ssl_policy=None, certificates=None, default_actions=None, alpn_policy=None) -> web.Response:
    """g_et_modify_listener

    &lt;p&gt;Replaces the specified properties of the specified listener. Any properties that you do not specify remain unchanged.&lt;/p&gt; &lt;p&gt;Changing the protocol from HTTPS to HTTP, or from TLS to TCP, removes the security policy and default certificate properties. If you change the protocol from HTTP to HTTPS, or from TCP to TLS, you must add the security policy and default certificate properties.&lt;/p&gt; &lt;p&gt;To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.&lt;/p&gt;

    :param listener_arn: The Amazon Resource Name (ARN) of the listener.
    :type listener_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param port: The port for connections from clients to the load balancer. You cannot specify a port for a Gateway Load Balancer.
    :type port: int
    :param protocol: The protocol for connections from clients to the load balancer. Application Load Balancers support the HTTP and HTTPS protocols. Network Load Balancers support the TCP, TLS, UDP, and TCP_UDP protocols. You can’t change the protocol to UDP or TCP_UDP if dual-stack mode is enabled. You cannot specify a protocol for a Gateway Load Balancer.
    :type protocol: str
    :param ssl_policy: &lt;p&gt;[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;
    :type ssl_policy: str
    :param certificates: [HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set &lt;code&gt;CertificateArn&lt;/code&gt; to the certificate ARN but do not set &lt;code&gt;IsDefault&lt;/code&gt;.
    :type certificates: list | bytes
    :param default_actions: The actions for the default rule.
    :type default_actions: list | bytes
    :param alpn_policy: &lt;p&gt;[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP1Only&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP2Only&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP2Optional&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HTTP2Preferred&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;None&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#alpn-policies\&quot;&gt;ALPN policies&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;
    :type alpn_policy: List[str]

    """
    certificates = [Certificate.from_dict(d) for d in certificates]
    default_actions = [Action.from_dict(d) for d in default_actions]
    return web.Response(status=200)


async def g_et_modify_load_balancer_attributes(request: web.Request, load_balancer_arn, attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_load_balancer_attributes

    &lt;p&gt;Modifies the specified attributes of the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;If any of the specified attributes can&#39;t be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.&lt;/p&gt;

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param attributes: The load balancer attributes.
    :type attributes: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    attributes = [LoadBalancerAttribute.from_dict(d) for d in attributes]
    return web.Response(status=200)


async def g_et_modify_rule(request: web.Request, rule_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, conditions=None, actions=None) -> web.Response:
    """g_et_modify_rule

    &lt;p&gt;Replaces the specified properties of the specified rule. Any properties that you do not specify are unchanged.&lt;/p&gt; &lt;p&gt;To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.&lt;/p&gt;

    :param rule_arn: The Amazon Resource Name (ARN) of the rule.
    :type rule_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param conditions: The conditions.
    :type conditions: list | bytes
    :param actions: The actions.
    :type actions: list | bytes

    """
    conditions = [RuleCondition.from_dict(d) for d in conditions]
    actions = [Action.from_dict(d) for d in actions]
    return web.Response(status=200)


async def g_et_modify_target_group(request: web.Request, target_group_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, health_check_protocol=None, health_check_port=None, health_check_path=None, health_check_enabled=None, health_check_interval_seconds=None, health_check_timeout_seconds=None, healthy_threshold_count=None, unhealthy_threshold_count=None, matcher=None) -> web.Response:
    """g_et_modify_target_group

    Modifies the health checks used when evaluating the health state of the targets in the specified target group.

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param health_check_protocol: The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. It is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP_UDP. The GENEVE, TLS, UDP, and TCP_UDP protocols are not supported for health checks.
    :type health_check_protocol: str
    :param health_check_port: The port the load balancer uses when performing health checks on targets.
    :type health_check_port: str
    :param health_check_path: &lt;p&gt;[HTTP/HTTPS health checks] The destination for health checks on the targets.&lt;/p&gt; &lt;p&gt;[HTTP1 or HTTP2 protocol version] The ping path. The default is /.&lt;/p&gt; &lt;p&gt;[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /Amazon Web Services.ALB/healthcheck.&lt;/p&gt;
    :type health_check_path: str
    :param health_check_enabled: Indicates whether health checks are enabled.
    :type health_check_enabled: bool
    :param health_check_interval_seconds: The approximate amount of time, in seconds, between health checks of an individual target.
    :type health_check_interval_seconds: int
    :param health_check_timeout_seconds: [HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.
    :type health_check_timeout_seconds: int
    :param healthy_threshold_count: The number of consecutive health checks successes required before considering an unhealthy target healthy.
    :type healthy_threshold_count: int
    :param unhealthy_threshold_count: The number of consecutive health check failures required before considering the target unhealthy.
    :type unhealthy_threshold_count: int
    :param matcher: [HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP_UDP, UDP or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.
    :type matcher: dict | bytes

    """
    matcher = .from_dict(matcher)
    return web.Response(status=200)


async def g_et_modify_target_group_attributes(request: web.Request, target_group_arn, attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_target_group_attributes

    Modifies the specified attributes of the specified target group.

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param attributes: The attributes.
    :type attributes: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    attributes = [TargetGroupAttribute.from_dict(d) for d in attributes]
    return web.Response(status=200)


async def g_et_register_targets(request: web.Request, target_group_arn, targets, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_register_targets

    &lt;p&gt;Registers the specified targets with the specified target group.&lt;/p&gt; &lt;p&gt;If the target is an EC2 instance, it must be in the &lt;code&gt;running&lt;/code&gt; state when you register it.&lt;/p&gt; &lt;p&gt;By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.&lt;/p&gt; &lt;p&gt;With a Network Load Balancer, you cannot register instances by instance ID if they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by IP address.&lt;/p&gt;

    :param target_group_arn: The Amazon Resource Name (ARN) of the target group.
    :type target_group_arn: str
    :param targets: The targets.
    :type targets: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    targets = [TargetDescription.from_dict(d) for d in targets]
    return web.Response(status=200)


async def g_et_remove_listener_certificates(request: web.Request, listener_arn, certificates, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_listener_certificates

    Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.

    :param listener_arn: The Amazon Resource Name (ARN) of the listener.
    :type listener_arn: str
    :param certificates: The certificate to remove. You can specify one certificate per call. Set &lt;code&gt;CertificateArn&lt;/code&gt; to the certificate ARN but do not set &lt;code&gt;IsDefault&lt;/code&gt;.
    :type certificates: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    certificates = [Certificate.from_dict(d) for d in certificates]
    return web.Response(status=200)


async def g_et_remove_tags(request: web.Request, resource_arns, tag_keys, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_tags

    Removes the specified tags from the specified Elastic Load Balancing resources. You can remove the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.

    :param resource_arns: The Amazon Resource Name (ARN) of the resource.
    :type resource_arns: List[str]
    :param tag_keys: The tag keys for the tags to remove.
    :type tag_keys: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_set_ip_address_type(request: web.Request, load_balancer_arn, ip_address_type, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_ip_address_type

    Sets the type of IP addresses used by the subnets of the specified load balancer.

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param ip_address_type: The IP address type. The possible values are &lt;code&gt;ipv4&lt;/code&gt; (for IPv4 addresses) and &lt;code&gt;dualstack&lt;/code&gt; (for IPv4 and IPv6 addresses). You can’t specify &lt;code&gt;dualstack&lt;/code&gt; for a load balancer with a UDP or TCP_UDP listener.
    :type ip_address_type: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_set_rule_priorities(request: web.Request, rule_priorities, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_rule_priorities

    &lt;p&gt;Sets the priorities of the specified rules.&lt;/p&gt; &lt;p&gt;You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.&lt;/p&gt;

    :param rule_priorities: The rule priorities.
    :type rule_priorities: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    rule_priorities = [RulePriorityPair.from_dict(d) for d in rule_priorities]
    return web.Response(status=200)


async def g_et_set_security_groups(request: web.Request, load_balancer_arn, security_groups, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_security_groups

    &lt;p&gt;Associates the specified security groups with the specified Application Load Balancer. The specified security groups override the previously associated security groups.&lt;/p&gt; &lt;p&gt;You can&#39;t specify a security group for a Network Load Balancer or Gateway Load Balancer.&lt;/p&gt;

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param security_groups: The IDs of the security groups.
    :type security_groups: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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


async def g_et_set_subnets(request: web.Request, load_balancer_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, subnets=None, subnet_mappings=None, ip_address_type=None) -> web.Response:
    """g_et_set_subnets

    &lt;p&gt;Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer or Network Load Balancer. The specified subnets replace the previously enabled subnets.&lt;/p&gt; &lt;p&gt;When you specify subnets for a Network Load Balancer, you must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.&lt;/p&gt;

    :param load_balancer_arn: The Amazon Resource Name (ARN) of the load balancer.
    :type load_balancer_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param subnets: &lt;p&gt;The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.&lt;/p&gt; &lt;p&gt;[Application Load Balancers] You must specify subnets from at least two Availability Zones.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Outposts] You must specify one Outpost subnet.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.&lt;/p&gt; &lt;p&gt;[Network Load Balancers] You can specify subnets from one or more Availability Zones.&lt;/p&gt;
    :type subnets: List[str]
    :param subnet_mappings: &lt;p&gt;The IDs of the public subnets. You can specify only one subnet per Availability Zone. You must specify either subnets or subnet mappings.&lt;/p&gt; &lt;p&gt;[Application Load Balancers] You must specify subnets from at least two Availability Zones. You cannot specify Elastic IP addresses for your subnets.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Outposts] You must specify one Outpost subnet.&lt;/p&gt; &lt;p&gt;[Application Load Balancers on Local Zones] You can specify subnets from one or more Local Zones.&lt;/p&gt; &lt;p&gt;[Network Load Balancers] You can specify subnets from one or more Availability Zones. You can specify one Elastic IP address per subnet if you need static IP addresses for your internet-facing load balancer. For internal load balancers, you can specify one private IP address per subnet from the IPv4 range of the subnet. For internet-facing load balancer, you can specify one IPv6 address per subnet.&lt;/p&gt;
    :type subnet_mappings: list | bytes
    :param ip_address_type: [Network Load Balancers] The type of IP addresses used by the subnets for your load balancer. The possible values are &lt;code&gt;ipv4&lt;/code&gt; (for IPv4 addresses) and &lt;code&gt;dualstack&lt;/code&gt; (for IPv4 and IPv6 addresses). You can’t specify &lt;code&gt;dualstack&lt;/code&gt; for a load balancer with a UDP or TCP_UDP listener. .
    :type ip_address_type: str

    """
    subnet_mappings = [SubnetMapping.from_dict(d) for d in subnet_mappings]
    return web.Response(status=200)


async def p_ost_add_listener_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_listener_certificates

    &lt;p&gt;Adds the specified SSL server certificate to the certificate list for the specified HTTPS or TLS listener.&lt;/p&gt; &lt;p&gt;If the certificate in already in the certificate list, the call is successful but the certificate is not added again.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html\&quot;&gt;HTTPS listeners&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html\&quot;&gt;TLS listeners&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = AddListenerCertificatesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_add_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_tags

    &lt;p&gt;Adds the specified tags to the specified Elastic Load Balancing resource. You can tag your Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, and rules.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and an optional value. If a resource already has a tag with the same key, &lt;code&gt;AddTags&lt;/code&gt; updates its value.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = AddTagsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_listener(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_listener

    &lt;p&gt;Creates a listener for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html\&quot;&gt;Listeners for your Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html\&quot;&gt;Listeners for your Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html\&quot;&gt;Listeners for your Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateListenerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_load_balancer

    &lt;p&gt;Creates an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html\&quot;&gt;Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html\&quot;&gt;Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html\&quot;&gt;Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple load balancers with the same settings, each call succeeds.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateLoadBalancerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_rule

    &lt;p&gt;Creates a rule for the specified listener. The listener must be associated with an Application Load Balancer.&lt;/p&gt; &lt;p&gt;Each rule consists of a priority, one or more actions, and one or more conditions. Rules are evaluated in priority order, from the lowest value to the highest value. When the conditions for a rule are met, its actions are performed. If the conditions for no rules are met, the actions for the default rule are performed. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules\&quot;&gt;Listener rules&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateRuleInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_target_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_target_group

    &lt;p&gt;Creates a target group.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html\&quot;&gt;Target groups for your Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html\&quot;&gt;Target groups for your Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html\&quot;&gt;Target groups for your Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = CreateTargetGroupInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_listener(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_listener

    &lt;p&gt;Deletes the specified listener.&lt;/p&gt; &lt;p&gt;Alternatively, your listener is deleted when you delete the load balancer to which it is attached.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteListenerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_load_balancer

    &lt;p&gt;Deletes the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. Deleting a load balancer also deletes its listeners.&lt;/p&gt; &lt;p&gt;You can&#39;t delete a load balancer if deletion protection is enabled. If the load balancer does not exist or has already been deleted, the call succeeds.&lt;/p&gt; &lt;p&gt;Deleting a load balancer does not affect its registered targets. For example, your EC2 instances continue to run and are still registered to their target groups. If you no longer need these EC2 instances, you can stop or terminate them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteLoadBalancerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_rule

    &lt;p&gt;Deletes the specified rule.&lt;/p&gt; &lt;p&gt;You can&#39;t delete the default rule.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteRuleInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_target_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_target_group

    &lt;p&gt;Deletes the specified target group.&lt;/p&gt; &lt;p&gt;You can delete a target group if it is not referenced by any actions. Deleting a target group also deletes any associated health checks. Deleting a target group does not affect its registered targets. For example, any EC2 instances continue to run until you stop or terminate them.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteTargetGroupInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_deregister_targets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_deregister_targets

    Deregisters the specified targets from the specified target group. After the targets are deregistered, they no longer receive traffic from the load balancer.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DeregisterTargetsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_account_limits

    &lt;p&gt;Describes the current Elastic Load Balancing resource limits for your Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html\&quot;&gt;Quotas for your Application Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-limits.html\&quot;&gt;Quotas for your Network Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/quotas-limits.html\&quot;&gt;Quotas for your Gateway Load Balancers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAccountLimitsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_listener_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_listener_certificates

    &lt;p&gt;Describes the default certificate and the certificate list for the specified HTTPS or TLS listener.&lt;/p&gt; &lt;p&gt;If the default certificate is also in the certificate list, it appears twice in the results (once with &lt;code&gt;IsDefault&lt;/code&gt; set to true and once with &lt;code&gt;IsDefault&lt;/code&gt; set to false).&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#https-listener-certificates\&quot;&gt;SSL certificates&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#tls-listener-certificate\&quot;&gt;Server certificates&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeListenerCertificatesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_listeners(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_listeners

    Describes the specified listeners or the listeners for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. You must specify either a load balancer or one or more listeners.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeListenersInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancer_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_load_balancer_attributes

    &lt;p&gt;Describes the attributes for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#load-balancer-attributes\&quot;&gt;Load balancer attributes&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#load-balancer-attributes\&quot;&gt;Load balancer attributes&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#load-balancer-attributes\&quot;&gt;Load balancer attributes&lt;/a&gt; in the &lt;i&gt;Gateway Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeLoadBalancerAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_load_balancers

    Describes the specified load balancers or all of your load balancers.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeLoadBalancersInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_rules

    Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_ssl_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_ssl_policies

    &lt;p&gt;Describes the specified policies or all policies used for SSL negotiation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies\&quot;&gt;Security policies&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeSSLPoliciesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_tags

    Describes the tags for the specified Elastic Load Balancing resources. You can describe the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTagsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_target_group_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_target_group_attributes

    &lt;p&gt;Describes the attributes for the specified target group.&lt;/p&gt; &lt;p&gt;For more information, see the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#target-group-attributes\&quot;&gt;Target group attributes&lt;/a&gt; in the &lt;i&gt;Application Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#target-group-attributes\&quot;&gt;Target group attributes&lt;/a&gt; in the &lt;i&gt;Network Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html#target-group-attributes\&quot;&gt;Target group attributes&lt;/a&gt; in the &lt;i&gt;Gateway Load Balancers Guide&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTargetGroupAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_target_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_target_groups

    Describes the specified target groups or all of your target groups. By default, all target groups are described. Alternatively, you can specify one of the following to filter the results: the ARN of the load balancer, the names of one or more target groups, or the ARNs of one or more target groups.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param marker: Pagination token
    :type marker: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTargetGroupsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_target_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_target_health

    Describes the health of the specified targets or all of your targets.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeTargetHealthInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_listener(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_listener

    &lt;p&gt;Replaces the specified properties of the specified listener. Any properties that you do not specify remain unchanged.&lt;/p&gt; &lt;p&gt;Changing the protocol from HTTPS to HTTP, or from TLS to TCP, removes the security policy and default certificate properties. If you change the protocol from HTTP to HTTPS, or from TCP to TLS, you must add the security policy and default certificate properties.&lt;/p&gt; &lt;p&gt;To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyListenerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_load_balancer_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_load_balancer_attributes

    &lt;p&gt;Modifies the specified attributes of the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.&lt;/p&gt; &lt;p&gt;If any of the specified attributes can&#39;t be modified as requested, the call fails. Any existing attributes that you do not modify retain their current values.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyLoadBalancerAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_rule

    &lt;p&gt;Replaces the specified properties of the specified rule. Any properties that you do not specify are unchanged.&lt;/p&gt; &lt;p&gt;To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyRuleInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_target_group(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_target_group

    Modifies the health checks used when evaluating the health state of the targets in the specified target group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyTargetGroupInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_target_group_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_target_group_attributes

    Modifies the specified attributes of the specified target group.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyTargetGroupAttributesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_register_targets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_register_targets

    &lt;p&gt;Registers the specified targets with the specified target group.&lt;/p&gt; &lt;p&gt;If the target is an EC2 instance, it must be in the &lt;code&gt;running&lt;/code&gt; state when you register it.&lt;/p&gt; &lt;p&gt;By default, the load balancer routes requests to registered targets using the protocol and port for the target group. Alternatively, you can override the port for a target when you register it. You can register each EC2 instance or IP address with the same target group multiple times using different ports.&lt;/p&gt; &lt;p&gt;With a Network Load Balancer, you cannot register instances by instance ID if they have the following instance types: C1, CC1, CC2, CG1, CG2, CR1, CS1, G1, G2, HI1, HS1, M1, M2, M3, and T1. You can register instances of these types by IP address.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RegisterTargetsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_listener_certificates(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_listener_certificates

    Removes the specified certificate from the certificate list for the specified HTTPS or TLS listener.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveListenerCertificatesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_tags

    Removes the specified tags from the specified Elastic Load Balancing resources. You can remove the tags for one or more Application Load Balancers, Network Load Balancers, Gateway Load Balancers, target groups, listeners, or rules.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveTagsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_ip_address_type(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_ip_address_type

    Sets the type of IP addresses used by the subnets of the specified load balancer.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetIpAddressTypeInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_rule_priorities(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_rule_priorities

    &lt;p&gt;Sets the priorities of the specified rules.&lt;/p&gt; &lt;p&gt;You can reorder the rules as long as there are no priority conflicts in the new order. Any existing rules that you do not specify retain their current priority.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetRulePrioritiesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_security_groups(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_security_groups

    &lt;p&gt;Associates the specified security groups with the specified Application Load Balancer. The specified security groups override the previously associated security groups.&lt;/p&gt; &lt;p&gt;You can&#39;t specify a security group for a Network Load Balancer or Gateway Load Balancer.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetSecurityGroupsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_subnets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_subnets

    &lt;p&gt;Enables the Availability Zones for the specified public subnets for the specified Application Load Balancer or Network Load Balancer. The specified subnets replace the previously enabled subnets.&lt;/p&gt; &lt;p&gt;When you specify subnets for a Network Load Balancer, you must include all subnets that were enabled previously, with their existing configurations, plus any additional subnets.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
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
    :param body: 
    :type body: dict | bytes

    """
    body = SetSubnetsInput.from_dict(body)
    return web.Response(status=200)
