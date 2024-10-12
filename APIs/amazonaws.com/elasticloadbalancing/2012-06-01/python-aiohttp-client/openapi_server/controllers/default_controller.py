from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_availability_zones_input import AddAvailabilityZonesInput
from openapi_server.models.add_availability_zones_output import AddAvailabilityZonesOutput
from openapi_server.models.add_tags_input import AddTagsInput
from openapi_server.models.apply_security_groups_to_load_balancer_input import ApplySecurityGroupsToLoadBalancerInput
from openapi_server.models.apply_security_groups_to_load_balancer_output import ApplySecurityGroupsToLoadBalancerOutput
from openapi_server.models.attach_load_balancer_to_subnets_input import AttachLoadBalancerToSubnetsInput
from openapi_server.models.attach_load_balancer_to_subnets_output import AttachLoadBalancerToSubnetsOutput
from openapi_server.models.configure_health_check_input import ConfigureHealthCheckInput
from openapi_server.models.configure_health_check_output import ConfigureHealthCheckOutput
from openapi_server.models.create_access_point_input import CreateAccessPointInput
from openapi_server.models.create_access_point_output import CreateAccessPointOutput
from openapi_server.models.create_app_cookie_stickiness_policy_input import CreateAppCookieStickinessPolicyInput
from openapi_server.models.create_lb_cookie_stickiness_policy_input import CreateLBCookieStickinessPolicyInput
from openapi_server.models.create_load_balancer_listener_input import CreateLoadBalancerListenerInput
from openapi_server.models.create_load_balancer_policy_input import CreateLoadBalancerPolicyInput
from openapi_server.models.delete_access_point_input import DeleteAccessPointInput
from openapi_server.models.delete_load_balancer_listener_input import DeleteLoadBalancerListenerInput
from openapi_server.models.delete_load_balancer_policy_input import DeleteLoadBalancerPolicyInput
from openapi_server.models.deregister_end_points_input import DeregisterEndPointsInput
from openapi_server.models.deregister_end_points_output import DeregisterEndPointsOutput
from openapi_server.models.describe_access_points_input import DescribeAccessPointsInput
from openapi_server.models.describe_access_points_output import DescribeAccessPointsOutput
from openapi_server.models.describe_account_limits_input import DescribeAccountLimitsInput
from openapi_server.models.describe_account_limits_output import DescribeAccountLimitsOutput
from openapi_server.models.describe_end_point_state_input import DescribeEndPointStateInput
from openapi_server.models.describe_end_point_state_output import DescribeEndPointStateOutput
from openapi_server.models.describe_load_balancer_attributes_input import DescribeLoadBalancerAttributesInput
from openapi_server.models.describe_load_balancer_attributes_output import DescribeLoadBalancerAttributesOutput
from openapi_server.models.describe_load_balancer_policies_input import DescribeLoadBalancerPoliciesInput
from openapi_server.models.describe_load_balancer_policies_output import DescribeLoadBalancerPoliciesOutput
from openapi_server.models.describe_load_balancer_policy_types_input import DescribeLoadBalancerPolicyTypesInput
from openapi_server.models.describe_load_balancer_policy_types_output import DescribeLoadBalancerPolicyTypesOutput
from openapi_server.models.describe_tags_input import DescribeTagsInput
from openapi_server.models.describe_tags_output import DescribeTagsOutput
from openapi_server.models.detach_load_balancer_from_subnets_input import DetachLoadBalancerFromSubnetsInput
from openapi_server.models.detach_load_balancer_from_subnets_output import DetachLoadBalancerFromSubnetsOutput
from openapi_server.models.get_configure_health_check_health_check_parameter import GETConfigureHealthCheckHealthCheckParameter
from openapi_server.models.get_modify_load_balancer_attributes_load_balancer_attributes_parameter import GETModifyLoadBalancerAttributesLoadBalancerAttributesParameter
from openapi_server.models.instance import Instance
from openapi_server.models.listener import Listener
from openapi_server.models.modify_load_balancer_attributes_input import ModifyLoadBalancerAttributesInput
from openapi_server.models.modify_load_balancer_attributes_output import ModifyLoadBalancerAttributesOutput
from openapi_server.models.policy_attribute import PolicyAttribute
from openapi_server.models.register_end_points_input import RegisterEndPointsInput
from openapi_server.models.register_end_points_output import RegisterEndPointsOutput
from openapi_server.models.remove_availability_zones_input import RemoveAvailabilityZonesInput
from openapi_server.models.remove_availability_zones_output import RemoveAvailabilityZonesOutput
from openapi_server.models.remove_tags_input import RemoveTagsInput
from openapi_server.models.set_load_balancer_listener_ssl_certificate_input import SetLoadBalancerListenerSSLCertificateInput
from openapi_server.models.set_load_balancer_policies_for_backend_server_input import SetLoadBalancerPoliciesForBackendServerInput
from openapi_server.models.set_load_balancer_policies_of_listener_input import SetLoadBalancerPoliciesOfListenerInput
from openapi_server.models.tag import Tag
from openapi_server.models.tag_key_only import TagKeyOnly
from openapi_server import util


async def g_et_add_tags(request: web.Request, load_balancer_names, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_add_tags

    &lt;p&gt;Adds the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, &lt;code&gt;AddTags&lt;/code&gt; updates its value.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html\&quot;&gt;Tag Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_names: The name of the load balancer. You can specify one load balancer only.
    :type load_balancer_names: List[str]
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


async def g_et_apply_security_groups_to_load_balancer(request: web.Request, load_balancer_name, security_groups, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_apply_security_groups_to_load_balancer

    &lt;p&gt;Associates one or more security groups with your load balancer in a virtual private cloud (VPC). The specified security groups override the previously associated security groups.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups\&quot;&gt;Security Groups for Load Balancers in a VPC&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param security_groups: The IDs of the security groups to associate with the load balancer. Note that you cannot specify the name of the security group.
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


async def g_et_attach_load_balancer_to_subnets(request: web.Request, load_balancer_name, subnets, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_attach_load_balancer_to_subnets

    &lt;p&gt;Adds one or more subnets to the set of configured subnets for the specified load balancer.&lt;/p&gt; &lt;p&gt;The load balancer evenly distributes requests across all registered subnets. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html\&quot;&gt;Add or Remove Subnets for Your Load Balancer in a VPC&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param subnets: The IDs of the subnets to add. You can add only one subnet per Availability Zone.
    :type subnets: List[str]
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


async def g_et_configure_health_check(request: web.Request, load_balancer_name, health_check, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_configure_health_check

    &lt;p&gt;Specifies the health check settings to use when evaluating the health state of your EC2 instances.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html\&quot;&gt;Configure Health Checks for Your Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param health_check: The configuration information.
    :type health_check: dict | bytes
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
    health_check = .from_dict(health_check)
    return web.Response(status=200)


async def g_et_create_app_cookie_stickiness_policy(request: web.Request, load_balancer_name, policy_name, cookie_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_app_cookie_stickiness_policy

    &lt;p&gt;Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners.&lt;/p&gt; &lt;p&gt;This policy is similar to the policy created by &lt;a&gt;CreateLBCookieStickinessPolicy&lt;/a&gt;, except that the lifetime of the special Elastic Load Balancing cookie, &lt;code&gt;AWSELB&lt;/code&gt;, follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.&lt;/p&gt; &lt;p&gt;If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application\&quot;&gt;Application-Controlled Session Stickiness&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param policy_name: The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
    :type policy_name: str
    :param cookie_name: The name of the application cookie used for stickiness.
    :type cookie_name: str
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


async def g_et_create_lb_cookie_stickiness_policy(request: web.Request, load_balancer_name, policy_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, cookie_expiration_period=None) -> web.Response:
    """g_et_create_lb_cookie_stickiness_policy

    &lt;p&gt;Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners.&lt;/p&gt; &lt;p&gt;When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.&lt;/p&gt; &lt;p&gt;A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration\&quot;&gt;Duration-Based Session Stickiness&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param policy_name: The name of the policy being created. Policy names must consist of alphanumeric characters and dashes (-). This name must be unique within the set of policies for this load balancer.
    :type policy_name: str
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
    :param cookie_expiration_period: The time period, in seconds, after which the cookie should be considered stale. If you do not specify this parameter, the default value is 0, which indicates that the sticky session should last for the duration of the browser session.
    :type cookie_expiration_period: int

    """
    return web.Response(status=200)


async def g_et_create_load_balancer(request: web.Request, load_balancer_name, listeners, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, availability_zones=None, subnets=None, security_groups=None, scheme=None, tags=None) -> web.Response:
    """g_et_create_load_balancer

    &lt;p&gt;Creates a Classic Load Balancer.&lt;/p&gt; &lt;p&gt;You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using &lt;a&gt;CreateLoadBalancerListeners&lt;/a&gt;, &lt;a&gt;ApplySecurityGroupsToLoadBalancer&lt;/a&gt;, &lt;a&gt;AttachLoadBalancerToSubnets&lt;/a&gt;, and &lt;a&gt;AddTags&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To describe your current load balancers, see &lt;a&gt;DescribeLoadBalancers&lt;/a&gt;. When you are finished with a load balancer, you can delete it using &lt;a&gt;DeleteLoadBalancer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html\&quot;&gt;Limits for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: &lt;p&gt;The name of the load balancer.&lt;/p&gt; &lt;p&gt;This name must be unique within your set of load balancers for the region, must have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and cannot begin or end with a hyphen.&lt;/p&gt;
    :type load_balancer_name: str
    :param listeners: &lt;p&gt;The listeners.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html\&quot;&gt;Listeners for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;
    :type listeners: list | bytes
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
    :param availability_zones: &lt;p&gt;One or more Availability Zones from the same region as the load balancer.&lt;/p&gt; &lt;p&gt;You must specify at least one Availability Zone.&lt;/p&gt; &lt;p&gt;You can add more Availability Zones after you create the load balancer using &lt;a&gt;EnableAvailabilityZonesForLoadBalancer&lt;/a&gt;.&lt;/p&gt;
    :type availability_zones: List[str]
    :param subnets: The IDs of the subnets in your VPC to attach to the load balancer. Specify one subnet per Availability Zone specified in &lt;code&gt;AvailabilityZones&lt;/code&gt;.
    :type subnets: List[str]
    :param security_groups: The IDs of the security groups to assign to the load balancer.
    :type security_groups: List[str]
    :param scheme: &lt;p&gt;The type of a load balancer. Valid only for load balancers in a VPC.&lt;/p&gt; &lt;p&gt;By default, Elastic Load Balancing creates an Internet-facing load balancer with a DNS name that resolves to public IP addresses. For more information about Internet-facing and Internal load balancers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#load-balancer-scheme\&quot;&gt;Load Balancer Scheme&lt;/a&gt; in the &lt;i&gt;Elastic Load Balancing User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Specify &lt;code&gt;internal&lt;/code&gt; to create a load balancer with a DNS name that resolves to private IP addresses.&lt;/p&gt;
    :type scheme: str
    :param tags: &lt;p&gt;A list of tags to assign to the load balancer.&lt;/p&gt; &lt;p&gt;For more information about tagging your load balancer, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html\&quot;&gt;Tag Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;
    :type tags: list | bytes

    """
    listeners = [Listener.from_dict(d) for d in listeners]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_create_load_balancer_listeners(request: web.Request, load_balancer_name, listeners, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_create_load_balancer_listeners

    &lt;p&gt;Creates one or more listeners for the specified load balancer. If a listener with the specified port does not already exist, it is created; otherwise, the properties of the new listener must match the properties of the existing listener.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html\&quot;&gt;Listeners for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param listeners: The listeners.
    :type listeners: list | bytes
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
    listeners = [Listener.from_dict(d) for d in listeners]
    return web.Response(status=200)


async def g_et_create_load_balancer_policy(request: web.Request, load_balancer_name, policy_name, policy_type_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, policy_attributes=None) -> web.Response:
    """g_et_create_load_balancer_policy

    &lt;p&gt;Creates a policy with the specified attributes for the specified load balancer.&lt;/p&gt; &lt;p&gt;Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param policy_name: The name of the load balancer policy to be created. This name must be unique within the set of policies for this load balancer.
    :type policy_name: str
    :param policy_type_name: The name of the base policy type. To get the list of policy types, use &lt;a&gt;DescribeLoadBalancerPolicyTypes&lt;/a&gt;.
    :type policy_type_name: str
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
    :param policy_attributes: The policy attributes.
    :type policy_attributes: list | bytes

    """
    policy_attributes = [PolicyAttribute.from_dict(d) for d in policy_attributes]
    return web.Response(status=200)


async def g_et_delete_load_balancer(request: web.Request, load_balancer_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_load_balancer

    &lt;p&gt;Deletes the specified load balancer.&lt;/p&gt; &lt;p&gt;If you are attempting to recreate a load balancer, you must reconfigure all settings. The DNS name associated with a deleted load balancer are no longer usable. The name and associated DNS record of the deleted load balancer no longer exist and traffic sent to any of its IP addresses is no longer delivered to your instances.&lt;/p&gt; &lt;p&gt;If the load balancer does not exist or has already been deleted, the call to &lt;code&gt;DeleteLoadBalancer&lt;/code&gt; still succeeds.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
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


async def g_et_delete_load_balancer_listeners(request: web.Request, load_balancer_name, load_balancer_ports, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_load_balancer_listeners

    Deletes the specified listeners from the specified load balancer.

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param load_balancer_ports: The client port numbers of the listeners.
    :type load_balancer_ports: List[int]
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


async def g_et_delete_load_balancer_policy(request: web.Request, load_balancer_name, policy_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_load_balancer_policy

    Deletes the specified policy from the specified load balancer. This policy must not be enabled for any listeners.

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param policy_name: The name of the policy.
    :type policy_name: str
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


async def g_et_deregister_instances_from_load_balancer(request: web.Request, load_balancer_name, instances, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_deregister_instances_from_load_balancer

    &lt;p&gt;Deregisters the specified instances from the specified load balancer. After the instance is deregistered, it no longer receives traffic from the load balancer.&lt;/p&gt; &lt;p&gt;You can use &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; to verify that the instance is deregistered from the load balancer.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html\&quot;&gt;Register or De-Register EC2 Instances&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param instances: The IDs of the instances.
    :type instances: list | bytes
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
    instances = [Instance.from_dict(d) for d in instances]
    return web.Response(status=200)


async def g_et_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_account_limits

    &lt;p&gt;Describes the current Elastic Load Balancing resource limits for your AWS account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html\&quot;&gt;Limits for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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


async def g_et_describe_instance_health(request: web.Request, load_balancer_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, instances=None) -> web.Response:
    """g_et_describe_instance_health

    Describes the state of the specified instances with respect to the specified load balancer. If no instances are specified, the call describes the state of all instances that are currently registered with the load balancer. If instances are specified, their state is returned even if they are no longer registered with the load balancer. The state of terminated instances is not returned.

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
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
    :param instances: The IDs of the instances.
    :type instances: list | bytes

    """
    instances = [Instance.from_dict(d) for d in instances]
    return web.Response(status=200)


async def g_et_describe_load_balancer_attributes(request: web.Request, load_balancer_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_load_balancer_attributes

    Describes the attributes for the specified load balancer.

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
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


async def g_et_describe_load_balancer_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, load_balancer_name=None, policy_names=None) -> web.Response:
    """g_et_describe_load_balancer_policies

    &lt;p&gt;Describes the specified policies.&lt;/p&gt; &lt;p&gt;If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don&#39;t specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the &lt;code&gt;ELBSample-&lt;/code&gt; prefix.&lt;/p&gt;

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
    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param policy_names: The names of the policies.
    :type policy_names: List[str]

    """
    return web.Response(status=200)


async def g_et_describe_load_balancer_policy_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, policy_type_names=None) -> web.Response:
    """g_et_describe_load_balancer_policy_types

    &lt;p&gt;Describes the specified load balancer policy types or all load balancer policy types.&lt;/p&gt; &lt;p&gt;The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.&lt;/p&gt; &lt;p&gt;You can use &lt;a&gt;CreateLoadBalancerPolicy&lt;/a&gt; to create a policy configuration for any of these policy types. Then, depending on the policy type, use either &lt;a&gt;SetLoadBalancerPoliciesOfListener&lt;/a&gt; or &lt;a&gt;SetLoadBalancerPoliciesForBackendServer&lt;/a&gt; to set the policy.&lt;/p&gt;

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
    :param policy_type_names: The names of the policy types. If no names are specified, describes all policy types defined by Elastic Load Balancing.
    :type policy_type_names: List[str]

    """
    return web.Response(status=200)


async def g_et_describe_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, load_balancer_names=None, marker=None, page_size=None) -> web.Response:
    """g_et_describe_load_balancers

    Describes the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers.

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
    :param load_balancer_names: The names of the load balancers.
    :type load_balancer_names: List[str]
    :param marker: The marker for the next set of results. (You received this marker from a previous call.)
    :type marker: str
    :param page_size: The maximum number of results to return with this call (a number from 1 to 400). The default is 400.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_describe_tags(request: web.Request, load_balancer_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_describe_tags

    Describes the tags associated with the specified load balancers.

    :param load_balancer_names: The names of the load balancers.
    :type load_balancer_names: List[str]
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


async def g_et_detach_load_balancer_from_subnets(request: web.Request, load_balancer_name, subnets, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_detach_load_balancer_from_subnets

    &lt;p&gt;Removes the specified subnets from the set of configured subnets for the load balancer.&lt;/p&gt; &lt;p&gt;After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the &lt;code&gt;OutOfService&lt;/code&gt; state. Then, the load balancer balances the traffic among the remaining routable subnets.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param subnets: The IDs of the subnets.
    :type subnets: List[str]
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


async def g_et_disable_availability_zones_for_load_balancer(request: web.Request, load_balancer_name, availability_zones, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_disable_availability_zones_for_load_balancer

    &lt;p&gt;Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.&lt;/p&gt; &lt;p&gt;For load balancers in a non-default VPC, use &lt;a&gt;DetachLoadBalancerFromSubnets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the &lt;code&gt;OutOfService&lt;/code&gt; state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html\&quot;&gt;Add or Remove Availability Zones&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param availability_zones: The Availability Zones.
    :type availability_zones: List[str]
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


async def g_et_enable_availability_zones_for_load_balancer(request: web.Request, load_balancer_name, availability_zones, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_enable_availability_zones_for_load_balancer

    &lt;p&gt;Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.&lt;/p&gt; &lt;p&gt;For load balancers in a non-default VPC, use &lt;a&gt;AttachLoadBalancerToSubnets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The load balancer evenly distributes requests across all its registered Availability Zones that contain instances. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html\&quot;&gt;Add or Remove Availability Zones&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param availability_zones: The Availability Zones. These must be in the same region as the load balancer.
    :type availability_zones: List[str]
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


async def g_et_modify_load_balancer_attributes(request: web.Request, load_balancer_name, load_balancer_attributes, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_modify_load_balancer_attributes

    &lt;p&gt;Modifies the attributes of the specified load balancer.&lt;/p&gt; &lt;p&gt;You can modify the load balancer attributes, such as &lt;code&gt;AccessLogs&lt;/code&gt;, &lt;code&gt;ConnectionDraining&lt;/code&gt;, and &lt;code&gt;CrossZoneLoadBalancing&lt;/code&gt; by either enabling or disabling them. Or, you can modify the load balancer attribute &lt;code&gt;ConnectionSettings&lt;/code&gt; by specifying an idle connection timeout value for your load balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html\&quot;&gt;Cross-Zone Load Balancing&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html\&quot;&gt;Connection Draining&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html\&quot;&gt;Access Logs&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html\&quot;&gt;Idle Connection Timeout&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param load_balancer_attributes: The attributes for the load balancer.
    :type load_balancer_attributes: dict | bytes
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
    load_balancer_attributes = .from_dict(load_balancer_attributes)
    return web.Response(status=200)


async def g_et_register_instances_with_load_balancer(request: web.Request, load_balancer_name, instances, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_register_instances_with_load_balancer

    &lt;p&gt;Adds the specified instances to the specified load balancer.&lt;/p&gt; &lt;p&gt;The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.&lt;/p&gt; &lt;p&gt;Note that &lt;code&gt;RegisterInstanceWithLoadBalancer&lt;/code&gt; completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; or &lt;a&gt;DescribeInstanceHealth&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the &lt;code&gt;OutOfService&lt;/code&gt; state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the &lt;code&gt;InService&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;To deregister instances from a load balancer, use &lt;a&gt;DeregisterInstancesFromLoadBalancer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html\&quot;&gt;Register or De-Register EC2 Instances&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param instances: The IDs of the instances.
    :type instances: list | bytes
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
    instances = [Instance.from_dict(d) for d in instances]
    return web.Response(status=200)


async def g_et_remove_tags(request: web.Request, load_balancer_names, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_remove_tags

    Removes one or more tags from the specified load balancer.

    :param load_balancer_names: The name of the load balancer. You can specify a maximum of one load balancer name.
    :type load_balancer_names: List[str]
    :param tags: The list of tag keys to remove.
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
    tags = [TagKeyOnly.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_set_load_balancer_listener_ssl_certificate(request: web.Request, load_balancer_name, load_balancer_port, ssl_certificate_id, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_load_balancer_listener_ssl_certificate

    &lt;p&gt;Sets the certificate that terminates the specified listener&#39;s SSL connections. The specified certificate replaces any prior certificate that was used on the same load balancer and port.&lt;/p&gt; &lt;p&gt;For more information about updating your SSL certificate, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-update-ssl-cert.html\&quot;&gt;Replace the SSL Certificate for Your Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param load_balancer_port: The port that uses the specified SSL certificate.
    :type load_balancer_port: int
    :param ssl_certificate_id: The Amazon Resource Name (ARN) of the SSL certificate.
    :type ssl_certificate_id: str
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


async def g_et_set_load_balancer_policies_for_backend_server(request: web.Request, load_balancer_name, instance_port, policy_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_load_balancer_policies_for_backend_server

    &lt;p&gt;Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies. At this time, only the back-end server authentication policy type can be applied to the instance ports; this policy type is composed of multiple public key policies.&lt;/p&gt; &lt;p&gt;Each time you use &lt;code&gt;SetLoadBalancerPoliciesForBackendServer&lt;/code&gt; to enable the policies, use the &lt;code&gt;PolicyNames&lt;/code&gt; parameter to list the policies that you want to enable.&lt;/p&gt; &lt;p&gt;You can use &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; or &lt;a&gt;DescribeLoadBalancerPolicies&lt;/a&gt; to verify that the policy is associated with the EC2 instance.&lt;/p&gt; &lt;p&gt;For more information about enabling back-end instance authentication, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#configure_backendauth_clt\&quot;&gt;Configure Back-end Instance Authentication&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;. For more information about Proxy Protocol, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html\&quot;&gt;Configure Proxy Protocol Support&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param instance_port: The port number associated with the EC2 instance.
    :type instance_port: int
    :param policy_names: The names of the policies. If the list is empty, then all current polices are removed from the EC2 instance.
    :type policy_names: List[str]
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


async def g_et_set_load_balancer_policies_of_listener(request: web.Request, load_balancer_name, load_balancer_port, policy_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_set_load_balancer_policies_of_listener

    &lt;p&gt;Replaces the current set of policies for the specified load balancer port with the specified set of policies.&lt;/p&gt; &lt;p&gt;To enable back-end server authentication, use &lt;a&gt;SetLoadBalancerPoliciesForBackendServer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about setting policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html\&quot;&gt;Update the SSL Negotiation Configuration&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration\&quot;&gt;Duration-Based Session Stickiness&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application\&quot;&gt;Application-Controlled Session Stickiness&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

    :param load_balancer_name: The name of the load balancer.
    :type load_balancer_name: str
    :param load_balancer_port: The external port of the load balancer.
    :type load_balancer_port: int
    :param policy_names: The names of the policies. This list must include all policies to be enabled. If you omit a policy that is currently enabled, it is disabled. If the list is empty, all current policies are disabled.
    :type policy_names: List[str]
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


async def p_ost_add_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_add_tags

    &lt;p&gt;Adds the specified tags to the specified load balancer. Each load balancer can have a maximum of 10 tags.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and an optional value. If a tag with the same key is already associated with the load balancer, &lt;code&gt;AddTags&lt;/code&gt; updates its value.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/add-remove-tags.html\&quot;&gt;Tag Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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


async def p_ost_apply_security_groups_to_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_apply_security_groups_to_load_balancer

    &lt;p&gt;Associates one or more security groups with your load balancer in a virtual private cloud (VPC). The specified security groups override the previously associated security groups.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html#elb-vpc-security-groups\&quot;&gt;Security Groups for Load Balancers in a VPC&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = ApplySecurityGroupsToLoadBalancerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_attach_load_balancer_to_subnets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_attach_load_balancer_to_subnets

    &lt;p&gt;Adds one or more subnets to the set of configured subnets for the specified load balancer.&lt;/p&gt; &lt;p&gt;The load balancer evenly distributes requests across all registered subnets. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html\&quot;&gt;Add or Remove Subnets for Your Load Balancer in a VPC&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = AttachLoadBalancerToSubnetsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_configure_health_check(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_configure_health_check

    &lt;p&gt;Specifies the health check settings to use when evaluating the health state of your EC2 instances.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html\&quot;&gt;Configure Health Checks for Your Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = ConfigureHealthCheckInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_app_cookie_stickiness_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_app_cookie_stickiness_policy

    &lt;p&gt;Generates a stickiness policy with sticky session lifetimes that follow that of an application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners.&lt;/p&gt; &lt;p&gt;This policy is similar to the policy created by &lt;a&gt;CreateLBCookieStickinessPolicy&lt;/a&gt;, except that the lifetime of the special Elastic Load Balancing cookie, &lt;code&gt;AWSELB&lt;/code&gt;, follows the lifetime of the application-generated cookie specified in the policy configuration. The load balancer only inserts a new stickiness cookie when the application response includes a new application cookie.&lt;/p&gt; &lt;p&gt;If the application cookie is explicitly removed or expires, the session stops being sticky until a new application cookie is issued.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application\&quot;&gt;Application-Controlled Session Stickiness&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateAppCookieStickinessPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_lb_cookie_stickiness_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_lb_cookie_stickiness_policy

    &lt;p&gt;Generates a stickiness policy with sticky session lifetimes controlled by the lifetime of the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners.&lt;/p&gt; &lt;p&gt;When a load balancer implements this policy, the load balancer uses a special cookie to track the instance for each request. When the load balancer receives a request, it first checks to see if this cookie is present in the request. If so, the load balancer sends the request to the application server specified in the cookie. If not, the load balancer sends the request to a server that is chosen based on the existing load-balancing algorithm.&lt;/p&gt; &lt;p&gt;A cookie is inserted into the response for binding subsequent requests from the same user to that server. The validity of the cookie is based on the cookie expiration time, which is specified in the policy configuration.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration\&quot;&gt;Duration-Based Session Stickiness&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateLBCookieStickinessPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_load_balancer

    &lt;p&gt;Creates a Classic Load Balancer.&lt;/p&gt; &lt;p&gt;You can add listeners, security groups, subnets, and tags when you create your load balancer, or you can add them later using &lt;a&gt;CreateLoadBalancerListeners&lt;/a&gt;, &lt;a&gt;ApplySecurityGroupsToLoadBalancer&lt;/a&gt;, &lt;a&gt;AttachLoadBalancerToSubnets&lt;/a&gt;, and &lt;a&gt;AddTags&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To describe your current load balancers, see &lt;a&gt;DescribeLoadBalancers&lt;/a&gt;. When you are finished with a load balancer, you can delete it using &lt;a&gt;DeleteLoadBalancer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can create up to 20 load balancers per region per account. You can request an increase for the number of load balancers for your account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html\&quot;&gt;Limits for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateAccessPointInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_load_balancer_listeners(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_load_balancer_listeners

    &lt;p&gt;Creates one or more listeners for the specified load balancer. If a listener with the specified port does not already exist, it is created; otherwise, the properties of the new listener must match the properties of the existing listener.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html\&quot;&gt;Listeners for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = CreateLoadBalancerListenerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_create_load_balancer_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_create_load_balancer_policy

    &lt;p&gt;Creates a policy with the specified attributes for the specified load balancer.&lt;/p&gt; &lt;p&gt;Policies are settings that are saved for your load balancer and that can be applied to the listener or the application server, depending on the policy type.&lt;/p&gt;

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
    body = CreateLoadBalancerPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_load_balancer

    &lt;p&gt;Deletes the specified load balancer.&lt;/p&gt; &lt;p&gt;If you are attempting to recreate a load balancer, you must reconfigure all settings. The DNS name associated with a deleted load balancer are no longer usable. The name and associated DNS record of the deleted load balancer no longer exist and traffic sent to any of its IP addresses is no longer delivered to your instances.&lt;/p&gt; &lt;p&gt;If the load balancer does not exist or has already been deleted, the call to &lt;code&gt;DeleteLoadBalancer&lt;/code&gt; still succeeds.&lt;/p&gt;

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
    body = DeleteAccessPointInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_load_balancer_listeners(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_load_balancer_listeners

    Deletes the specified listeners from the specified load balancer.

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
    body = DeleteLoadBalancerListenerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_load_balancer_policy(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_load_balancer_policy

    Deletes the specified policy from the specified load balancer. This policy must not be enabled for any listeners.

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
    body = DeleteLoadBalancerPolicyInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_deregister_instances_from_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_deregister_instances_from_load_balancer

    &lt;p&gt;Deregisters the specified instances from the specified load balancer. After the instance is deregistered, it no longer receives traffic from the load balancer.&lt;/p&gt; &lt;p&gt;You can use &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; to verify that the instance is deregistered from the load balancer.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html\&quot;&gt;Register or De-Register EC2 Instances&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DeregisterEndPointsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_account_limits(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_account_limits

    &lt;p&gt;Describes the current Elastic Load Balancing resource limits for your AWS account.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-limits.html\&quot;&gt;Limits for Your Classic Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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


async def p_ost_describe_instance_health(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_instance_health

    Describes the state of the specified instances with respect to the specified load balancer. If no instances are specified, the call describes the state of all instances that are currently registered with the load balancer. If instances are specified, their state is returned even if they are no longer registered with the load balancer. The state of terminated instances is not returned.

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
    body = DescribeEndPointStateInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancer_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_load_balancer_attributes

    Describes the attributes for the specified load balancer.

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


async def p_ost_describe_load_balancer_policies(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_load_balancer_policies

    &lt;p&gt;Describes the specified policies.&lt;/p&gt; &lt;p&gt;If you specify a load balancer name, the action returns the descriptions of all policies created for the load balancer. If you specify a policy name associated with your load balancer, the action returns the description of that policy. If you don&#39;t specify a load balancer name, the action returns descriptions of the specified sample policies, or descriptions of all sample policies. The names of the sample policies have the &lt;code&gt;ELBSample-&lt;/code&gt; prefix.&lt;/p&gt;

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
    body = DescribeLoadBalancerPoliciesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancer_policy_types(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_load_balancer_policy_types

    &lt;p&gt;Describes the specified load balancer policy types or all load balancer policy types.&lt;/p&gt; &lt;p&gt;The description of each type indicates how it can be used. For example, some policies can be used only with layer 7 listeners, some policies can be used only with layer 4 listeners, and some policies can be used only with your EC2 instances.&lt;/p&gt; &lt;p&gt;You can use &lt;a&gt;CreateLoadBalancerPolicy&lt;/a&gt; to create a policy configuration for any of these policy types. Then, depending on the policy type, use either &lt;a&gt;SetLoadBalancerPoliciesOfListener&lt;/a&gt; or &lt;a&gt;SetLoadBalancerPoliciesForBackendServer&lt;/a&gt; to set the policy.&lt;/p&gt;

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
    body = DescribeLoadBalancerPolicyTypesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_load_balancers(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, body=None) -> web.Response:
    """p_ost_describe_load_balancers

    Describes the specified the load balancers. If no load balancers are specified, the call describes all of your load balancers.

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
    body = DescribeAccessPointsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_tags

    Describes the tags associated with the specified load balancers.

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


async def p_ost_detach_load_balancer_from_subnets(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_detach_load_balancer_from_subnets

    &lt;p&gt;Removes the specified subnets from the set of configured subnets for the load balancer.&lt;/p&gt; &lt;p&gt;After a subnet is removed, all EC2 instances registered with the load balancer in the removed subnet go into the &lt;code&gt;OutOfService&lt;/code&gt; state. Then, the load balancer balances the traffic among the remaining routable subnets.&lt;/p&gt;

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
    body = DetachLoadBalancerFromSubnetsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_disable_availability_zones_for_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disable_availability_zones_for_load_balancer

    &lt;p&gt;Removes the specified Availability Zones from the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.&lt;/p&gt; &lt;p&gt;For load balancers in a non-default VPC, use &lt;a&gt;DetachLoadBalancerFromSubnets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;There must be at least one Availability Zone registered with a load balancer at all times. After an Availability Zone is removed, all instances registered with the load balancer that are in the removed Availability Zone go into the &lt;code&gt;OutOfService&lt;/code&gt; state. Then, the load balancer attempts to equally balance the traffic among its remaining Availability Zones.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html\&quot;&gt;Add or Remove Availability Zones&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RemoveAvailabilityZonesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_enable_availability_zones_for_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enable_availability_zones_for_load_balancer

    &lt;p&gt;Adds the specified Availability Zones to the set of Availability Zones for the specified load balancer in EC2-Classic or a default VPC.&lt;/p&gt; &lt;p&gt;For load balancers in a non-default VPC, use &lt;a&gt;AttachLoadBalancerToSubnets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The load balancer evenly distributes requests across all its registered Availability Zones that contain instances. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-az.html\&quot;&gt;Add or Remove Availability Zones&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = AddAvailabilityZonesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_modify_load_balancer_attributes(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_modify_load_balancer_attributes

    &lt;p&gt;Modifies the attributes of the specified load balancer.&lt;/p&gt; &lt;p&gt;You can modify the load balancer attributes, such as &lt;code&gt;AccessLogs&lt;/code&gt;, &lt;code&gt;ConnectionDraining&lt;/code&gt;, and &lt;code&gt;CrossZoneLoadBalancing&lt;/code&gt; by either enabling or disabling them. Or, you can modify the load balancer attribute &lt;code&gt;ConnectionSettings&lt;/code&gt; by specifying an idle connection timeout value for your load balancer.&lt;/p&gt; &lt;p&gt;For more information, see the following in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html\&quot;&gt;Cross-Zone Load Balancing&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html\&quot;&gt;Connection Draining&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html\&quot;&gt;Access Logs&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html\&quot;&gt;Idle Connection Timeout&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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


async def p_ost_register_instances_with_load_balancer(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_register_instances_with_load_balancer

    &lt;p&gt;Adds the specified instances to the specified load balancer.&lt;/p&gt; &lt;p&gt;The instance must be a running instance in the same network as the load balancer (EC2-Classic or the same VPC). If you have EC2-Classic instances and a load balancer in a VPC with ClassicLink enabled, you can link the EC2-Classic instances to that VPC and then register the linked EC2-Classic instances with the load balancer in the VPC.&lt;/p&gt; &lt;p&gt;Note that &lt;code&gt;RegisterInstanceWithLoadBalancer&lt;/code&gt; completes when the request has been registered. Instance registration takes a little time to complete. To check the state of the registered instances, use &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; or &lt;a&gt;DescribeInstanceHealth&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;After the instance is registered, it starts receiving traffic and requests from the load balancer. Any instance that is not in one of the Availability Zones registered for the load balancer is moved to the &lt;code&gt;OutOfService&lt;/code&gt; state. If an Availability Zone is added to the load balancer later, any instances registered with the load balancer move to the &lt;code&gt;InService&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;To deregister instances from a load balancer, use &lt;a&gt;DeregisterInstancesFromLoadBalancer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-deregister-register-instances.html\&quot;&gt;Register or De-Register EC2 Instances&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RegisterEndPointsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_remove_tags(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_remove_tags

    Removes one or more tags from the specified load balancer.

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


async def p_ost_set_load_balancer_listener_ssl_certificate(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_load_balancer_listener_ssl_certificate

    &lt;p&gt;Sets the certificate that terminates the specified listener&#39;s SSL connections. The specified certificate replaces any prior certificate that was used on the same load balancer and port.&lt;/p&gt; &lt;p&gt;For more information about updating your SSL certificate, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-update-ssl-cert.html\&quot;&gt;Replace the SSL Certificate for Your Load Balancer&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = SetLoadBalancerListenerSSLCertificateInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_load_balancer_policies_for_backend_server(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_load_balancer_policies_for_backend_server

    &lt;p&gt;Replaces the set of policies associated with the specified port on which the EC2 instance is listening with a new set of policies. At this time, only the back-end server authentication policy type can be applied to the instance ports; this policy type is composed of multiple public key policies.&lt;/p&gt; &lt;p&gt;Each time you use &lt;code&gt;SetLoadBalancerPoliciesForBackendServer&lt;/code&gt; to enable the policies, use the &lt;code&gt;PolicyNames&lt;/code&gt; parameter to list the policies that you want to enable.&lt;/p&gt; &lt;p&gt;You can use &lt;a&gt;DescribeLoadBalancers&lt;/a&gt; or &lt;a&gt;DescribeLoadBalancerPolicies&lt;/a&gt; to verify that the policy is associated with the EC2 instance.&lt;/p&gt; &lt;p&gt;For more information about enabling back-end instance authentication, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#configure_backendauth_clt\&quot;&gt;Configure Back-end Instance Authentication&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;. For more information about Proxy Protocol, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-proxy-protocol.html\&quot;&gt;Configure Proxy Protocol Support&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = SetLoadBalancerPoliciesForBackendServerInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_load_balancer_policies_of_listener(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_load_balancer_policies_of_listener

    &lt;p&gt;Replaces the current set of policies for the specified load balancer port with the specified set of policies.&lt;/p&gt; &lt;p&gt;To enable back-end server authentication, use &lt;a&gt;SetLoadBalancerPoliciesForBackendServer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about setting policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/ssl-config-update.html\&quot;&gt;Update the SSL Negotiation Configuration&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-duration\&quot;&gt;Duration-Based Session Stickiness&lt;/a&gt;, and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html#enable-sticky-sessions-application\&quot;&gt;Application-Controlled Session Stickiness&lt;/a&gt; in the &lt;i&gt;Classic Load Balancers Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = SetLoadBalancerPoliciesOfListenerInput.from_dict(body)
    return web.Response(status=200)
