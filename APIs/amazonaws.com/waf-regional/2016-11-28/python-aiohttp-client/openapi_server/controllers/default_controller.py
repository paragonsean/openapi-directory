from typing import List, Dict
from aiohttp import web

from openapi_server.models.associate_web_acl_request import AssociateWebACLRequest
from openapi_server.models.create_byte_match_set_request import CreateByteMatchSetRequest
from openapi_server.models.create_byte_match_set_response import CreateByteMatchSetResponse
from openapi_server.models.create_geo_match_set_request import CreateGeoMatchSetRequest
from openapi_server.models.create_geo_match_set_response import CreateGeoMatchSetResponse
from openapi_server.models.create_ip_set_request import CreateIPSetRequest
from openapi_server.models.create_ip_set_response import CreateIPSetResponse
from openapi_server.models.create_rate_based_rule_request import CreateRateBasedRuleRequest
from openapi_server.models.create_rate_based_rule_response import CreateRateBasedRuleResponse
from openapi_server.models.create_regex_match_set_request import CreateRegexMatchSetRequest
from openapi_server.models.create_regex_match_set_response import CreateRegexMatchSetResponse
from openapi_server.models.create_regex_pattern_set_request import CreateRegexPatternSetRequest
from openapi_server.models.create_regex_pattern_set_response import CreateRegexPatternSetResponse
from openapi_server.models.create_rule_group_request import CreateRuleGroupRequest
from openapi_server.models.create_rule_group_response import CreateRuleGroupResponse
from openapi_server.models.create_rule_request import CreateRuleRequest
from openapi_server.models.create_rule_response import CreateRuleResponse
from openapi_server.models.create_size_constraint_set_request import CreateSizeConstraintSetRequest
from openapi_server.models.create_size_constraint_set_response import CreateSizeConstraintSetResponse
from openapi_server.models.create_sql_injection_match_set_request import CreateSqlInjectionMatchSetRequest
from openapi_server.models.create_sql_injection_match_set_response import CreateSqlInjectionMatchSetResponse
from openapi_server.models.create_web_acl_migration_stack_request import CreateWebACLMigrationStackRequest
from openapi_server.models.create_web_acl_migration_stack_response import CreateWebACLMigrationStackResponse
from openapi_server.models.create_web_acl_request import CreateWebACLRequest
from openapi_server.models.create_web_acl_response import CreateWebACLResponse
from openapi_server.models.create_xss_match_set_request import CreateXssMatchSetRequest
from openapi_server.models.create_xss_match_set_response import CreateXssMatchSetResponse
from openapi_server.models.delete_byte_match_set_request import DeleteByteMatchSetRequest
from openapi_server.models.delete_byte_match_set_response import DeleteByteMatchSetResponse
from openapi_server.models.delete_geo_match_set_request import DeleteGeoMatchSetRequest
from openapi_server.models.delete_geo_match_set_response import DeleteGeoMatchSetResponse
from openapi_server.models.delete_ip_set_request import DeleteIPSetRequest
from openapi_server.models.delete_ip_set_response import DeleteIPSetResponse
from openapi_server.models.delete_logging_configuration_request import DeleteLoggingConfigurationRequest
from openapi_server.models.delete_permission_policy_request import DeletePermissionPolicyRequest
from openapi_server.models.delete_rate_based_rule_request import DeleteRateBasedRuleRequest
from openapi_server.models.delete_rate_based_rule_response import DeleteRateBasedRuleResponse
from openapi_server.models.delete_regex_match_set_request import DeleteRegexMatchSetRequest
from openapi_server.models.delete_regex_match_set_response import DeleteRegexMatchSetResponse
from openapi_server.models.delete_regex_pattern_set_request import DeleteRegexPatternSetRequest
from openapi_server.models.delete_regex_pattern_set_response import DeleteRegexPatternSetResponse
from openapi_server.models.delete_rule_group_request import DeleteRuleGroupRequest
from openapi_server.models.delete_rule_group_response import DeleteRuleGroupResponse
from openapi_server.models.delete_rule_request import DeleteRuleRequest
from openapi_server.models.delete_rule_response import DeleteRuleResponse
from openapi_server.models.delete_size_constraint_set_request import DeleteSizeConstraintSetRequest
from openapi_server.models.delete_size_constraint_set_response import DeleteSizeConstraintSetResponse
from openapi_server.models.delete_sql_injection_match_set_request import DeleteSqlInjectionMatchSetRequest
from openapi_server.models.delete_sql_injection_match_set_response import DeleteSqlInjectionMatchSetResponse
from openapi_server.models.delete_web_acl_request import DeleteWebACLRequest
from openapi_server.models.delete_web_acl_response import DeleteWebACLResponse
from openapi_server.models.delete_xss_match_set_request import DeleteXssMatchSetRequest
from openapi_server.models.delete_xss_match_set_response import DeleteXssMatchSetResponse
from openapi_server.models.disassociate_web_acl_request import DisassociateWebACLRequest
from openapi_server.models.get_byte_match_set_request import GetByteMatchSetRequest
from openapi_server.models.get_byte_match_set_response import GetByteMatchSetResponse
from openapi_server.models.get_change_token_response import GetChangeTokenResponse
from openapi_server.models.get_change_token_status_request import GetChangeTokenStatusRequest
from openapi_server.models.get_change_token_status_response import GetChangeTokenStatusResponse
from openapi_server.models.get_geo_match_set_request import GetGeoMatchSetRequest
from openapi_server.models.get_geo_match_set_response import GetGeoMatchSetResponse
from openapi_server.models.get_ip_set_request import GetIPSetRequest
from openapi_server.models.get_ip_set_response import GetIPSetResponse
from openapi_server.models.get_logging_configuration_request import GetLoggingConfigurationRequest
from openapi_server.models.get_logging_configuration_response import GetLoggingConfigurationResponse
from openapi_server.models.get_permission_policy_request import GetPermissionPolicyRequest
from openapi_server.models.get_permission_policy_response import GetPermissionPolicyResponse
from openapi_server.models.get_rate_based_rule_managed_keys_request import GetRateBasedRuleManagedKeysRequest
from openapi_server.models.get_rate_based_rule_managed_keys_response import GetRateBasedRuleManagedKeysResponse
from openapi_server.models.get_rate_based_rule_request import GetRateBasedRuleRequest
from openapi_server.models.get_rate_based_rule_response import GetRateBasedRuleResponse
from openapi_server.models.get_regex_match_set_request import GetRegexMatchSetRequest
from openapi_server.models.get_regex_match_set_response import GetRegexMatchSetResponse
from openapi_server.models.get_regex_pattern_set_request import GetRegexPatternSetRequest
from openapi_server.models.get_regex_pattern_set_response import GetRegexPatternSetResponse
from openapi_server.models.get_rule_group_request import GetRuleGroupRequest
from openapi_server.models.get_rule_group_response import GetRuleGroupResponse
from openapi_server.models.get_rule_request import GetRuleRequest
from openapi_server.models.get_rule_response import GetRuleResponse
from openapi_server.models.get_sampled_requests_request import GetSampledRequestsRequest
from openapi_server.models.get_sampled_requests_response import GetSampledRequestsResponse
from openapi_server.models.get_size_constraint_set_request import GetSizeConstraintSetRequest
from openapi_server.models.get_size_constraint_set_response import GetSizeConstraintSetResponse
from openapi_server.models.get_sql_injection_match_set_request import GetSqlInjectionMatchSetRequest
from openapi_server.models.get_sql_injection_match_set_response import GetSqlInjectionMatchSetResponse
from openapi_server.models.get_web_acl_for_resource_request import GetWebACLForResourceRequest
from openapi_server.models.get_web_acl_for_resource_response import GetWebACLForResourceResponse
from openapi_server.models.get_web_acl_request import GetWebACLRequest
from openapi_server.models.get_web_acl_response import GetWebACLResponse
from openapi_server.models.get_xss_match_set_request import GetXssMatchSetRequest
from openapi_server.models.get_xss_match_set_response import GetXssMatchSetResponse
from openapi_server.models.list_activated_rules_in_rule_group_request import ListActivatedRulesInRuleGroupRequest
from openapi_server.models.list_activated_rules_in_rule_group_response import ListActivatedRulesInRuleGroupResponse
from openapi_server.models.list_byte_match_sets_request import ListByteMatchSetsRequest
from openapi_server.models.list_byte_match_sets_response import ListByteMatchSetsResponse
from openapi_server.models.list_geo_match_sets_request import ListGeoMatchSetsRequest
from openapi_server.models.list_geo_match_sets_response import ListGeoMatchSetsResponse
from openapi_server.models.list_ip_sets_request import ListIPSetsRequest
from openapi_server.models.list_ip_sets_response import ListIPSetsResponse
from openapi_server.models.list_logging_configurations_request import ListLoggingConfigurationsRequest
from openapi_server.models.list_logging_configurations_response import ListLoggingConfigurationsResponse
from openapi_server.models.list_rate_based_rules_request import ListRateBasedRulesRequest
from openapi_server.models.list_rate_based_rules_response import ListRateBasedRulesResponse
from openapi_server.models.list_regex_match_sets_request import ListRegexMatchSetsRequest
from openapi_server.models.list_regex_match_sets_response import ListRegexMatchSetsResponse
from openapi_server.models.list_regex_pattern_sets_request import ListRegexPatternSetsRequest
from openapi_server.models.list_regex_pattern_sets_response import ListRegexPatternSetsResponse
from openapi_server.models.list_resources_for_web_acl_request import ListResourcesForWebACLRequest
from openapi_server.models.list_resources_for_web_acl_response import ListResourcesForWebACLResponse
from openapi_server.models.list_rule_groups_request import ListRuleGroupsRequest
from openapi_server.models.list_rule_groups_response import ListRuleGroupsResponse
from openapi_server.models.list_rules_request import ListRulesRequest
from openapi_server.models.list_rules_response import ListRulesResponse
from openapi_server.models.list_size_constraint_sets_request import ListSizeConstraintSetsRequest
from openapi_server.models.list_size_constraint_sets_response import ListSizeConstraintSetsResponse
from openapi_server.models.list_sql_injection_match_sets_request import ListSqlInjectionMatchSetsRequest
from openapi_server.models.list_sql_injection_match_sets_response import ListSqlInjectionMatchSetsResponse
from openapi_server.models.list_subscribed_rule_groups_request import ListSubscribedRuleGroupsRequest
from openapi_server.models.list_subscribed_rule_groups_response import ListSubscribedRuleGroupsResponse
from openapi_server.models.list_tags_for_resource_request import ListTagsForResourceRequest
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_web_acls_request import ListWebACLsRequest
from openapi_server.models.list_web_acls_response import ListWebACLsResponse
from openapi_server.models.list_xss_match_sets_request import ListXssMatchSetsRequest
from openapi_server.models.list_xss_match_sets_response import ListXssMatchSetsResponse
from openapi_server.models.put_logging_configuration_request import PutLoggingConfigurationRequest
from openapi_server.models.put_logging_configuration_response import PutLoggingConfigurationResponse
from openapi_server.models.put_permission_policy_request import PutPermissionPolicyRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.untag_resource_request import UntagResourceRequest
from openapi_server.models.update_byte_match_set_request import UpdateByteMatchSetRequest
from openapi_server.models.update_byte_match_set_response import UpdateByteMatchSetResponse
from openapi_server.models.update_geo_match_set_request import UpdateGeoMatchSetRequest
from openapi_server.models.update_geo_match_set_response import UpdateGeoMatchSetResponse
from openapi_server.models.update_ip_set_request import UpdateIPSetRequest
from openapi_server.models.update_ip_set_response import UpdateIPSetResponse
from openapi_server.models.update_rate_based_rule_request import UpdateRateBasedRuleRequest
from openapi_server.models.update_rate_based_rule_response import UpdateRateBasedRuleResponse
from openapi_server.models.update_regex_match_set_request import UpdateRegexMatchSetRequest
from openapi_server.models.update_regex_match_set_response import UpdateRegexMatchSetResponse
from openapi_server.models.update_regex_pattern_set_request import UpdateRegexPatternSetRequest
from openapi_server.models.update_regex_pattern_set_response import UpdateRegexPatternSetResponse
from openapi_server.models.update_rule_group_request import UpdateRuleGroupRequest
from openapi_server.models.update_rule_group_response import UpdateRuleGroupResponse
from openapi_server.models.update_rule_request import UpdateRuleRequest
from openapi_server.models.update_rule_response import UpdateRuleResponse
from openapi_server.models.update_size_constraint_set_request import UpdateSizeConstraintSetRequest
from openapi_server.models.update_size_constraint_set_response import UpdateSizeConstraintSetResponse
from openapi_server.models.update_sql_injection_match_set_request import UpdateSqlInjectionMatchSetRequest
from openapi_server.models.update_sql_injection_match_set_response import UpdateSqlInjectionMatchSetResponse
from openapi_server.models.update_web_acl_request import UpdateWebACLRequest
from openapi_server.models.update_web_acl_response import UpdateWebACLResponse
from openapi_server.models.update_xss_match_set_request import UpdateXssMatchSetRequest
from openapi_server.models.update_xss_match_set_response import UpdateXssMatchSetResponse
from openapi_server import util


async def associate_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic Regional&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Associates a web ACL with a resource, either an application load balancer or Amazon API Gateway stage.&lt;/p&gt;

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
    body = AssociateWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def create_byte_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_byte_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;code&gt;ByteMatchSet&lt;/code&gt;. You then use &lt;a&gt;UpdateByteMatchSet&lt;/a&gt; to identify the part of a web request that you want AWS WAF to inspect, such as the values of the &lt;code&gt;User-Agent&lt;/code&gt; header or the query string. For example, you can create a &lt;code&gt;ByteMatchSet&lt;/code&gt; that matches any requests with &lt;code&gt;User-Agent&lt;/code&gt; headers that contain the string &lt;code&gt;BadBot&lt;/code&gt;. You can then configure AWS WAF to reject those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;ByteMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateByteMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateByteMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateByteMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateByteMatchSet&lt;/a&gt; request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateByteMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_geo_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_geo_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates an &lt;a&gt;GeoMatchSet&lt;/a&gt;, which you use to specify which web requests you want to allow or block based on the country that the requests originate from. For example, if you&#39;re receiving a lot of requests from one or more countries and you want to block the requests, you can create an &lt;code&gt;GeoMatchSet&lt;/code&gt; that contains those countries and then configure AWS WAF to block the requests. &lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;GeoMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateGeoMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateGeoMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateGeoMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateGeoMatchSetSet&lt;/code&gt; request to specify the countries that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateGeoMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_ip_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_ip_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates an &lt;a&gt;IPSet&lt;/a&gt;, which you use to specify which web requests that you want to allow or block based on the IP addresses that the requests originate from. For example, if you&#39;re receiving a lot of requests from one or more individual IP addresses or one or more ranges of IP addresses and you want to block the requests, you can create an &lt;code&gt;IPSet&lt;/code&gt; that contains those IP addresses and then configure AWS WAF to block the requests. &lt;/p&gt; &lt;p&gt;To create and configure an &lt;code&gt;IPSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateIPSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateIPSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateIPSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateIPSet&lt;/code&gt; request to specify the IP addresses that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateIPSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_rate_based_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rate_based_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;a&gt;RateBasedRule&lt;/a&gt;. The &lt;code&gt;RateBasedRule&lt;/code&gt; contains a &lt;code&gt;RateLimit&lt;/code&gt;, which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The &lt;code&gt;RateBasedRule&lt;/code&gt; also contains the &lt;code&gt;IPSet&lt;/code&gt; objects, &lt;code&gt;ByteMatchSet&lt;/code&gt; objects, and other predicates that identify the requests that you want to count or block if these requests exceed the &lt;code&gt;RateLimit&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you add more than one predicate to a &lt;code&gt;RateBasedRule&lt;/code&gt;, a request not only must exceed the &lt;code&gt;RateLimit&lt;/code&gt;, but it also must match all the conditions to be counted or blocked. For example, suppose you add the following to a &lt;code&gt;RateBasedRule&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;IPSet&lt;/code&gt; that matches the IP address &lt;code&gt;192.0.2.44/32&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ByteMatchSet&lt;/code&gt; that matches &lt;code&gt;BadBot&lt;/code&gt; in the &lt;code&gt;User-Agent&lt;/code&gt; header&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Further, you specify a &lt;code&gt;RateLimit&lt;/code&gt; of 1,000.&lt;/p&gt; &lt;p&gt;You then add the &lt;code&gt;RateBasedRule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt; and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 &lt;i&gt;and&lt;/i&gt; the &lt;code&gt;User-Agent&lt;/code&gt; header in the request must contain the value &lt;code&gt;BadBot&lt;/code&gt;. Further, requests that match these two conditions must be received at a rate of more than 1,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 1,000 for a five-minute period, AWS WAF no longer blocks the requests.&lt;/p&gt; &lt;p&gt;As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a &lt;code&gt;RateBasedRule&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ByteMatchSet&lt;/code&gt; with &lt;code&gt;FieldToMatch&lt;/code&gt; of &lt;code&gt;URI&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;PositionalConstraint&lt;/code&gt; of &lt;code&gt;STARTS_WITH&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;TargetString&lt;/code&gt; of &lt;code&gt;login&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Further, you specify a &lt;code&gt;RateLimit&lt;/code&gt; of 1,000.&lt;/p&gt; &lt;p&gt;By adding this &lt;code&gt;RateBasedRule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt;, you could limit requests to your login page without affecting the rest of your site.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;RateBasedRule&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create and update the predicates that you want to include in the rule. For more information, see &lt;a&gt;CreateByteMatchSet&lt;/a&gt;, &lt;a&gt;CreateIPSet&lt;/a&gt;, and &lt;a&gt;CreateSqlInjectionMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateRateBasedRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateRule&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateRateBasedRule&lt;/code&gt; request to specify the predicates that you want to include in the rule.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create and update a &lt;code&gt;WebACL&lt;/code&gt; that contains the &lt;code&gt;RateBasedRule&lt;/code&gt;. For more information, see &lt;a&gt;CreateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateRateBasedRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_regex_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_regex_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;a&gt;RegexMatchSet&lt;/a&gt;. You then use &lt;a&gt;UpdateRegexMatchSet&lt;/a&gt; to identify the part of a web request that you want AWS WAF to inspect, such as the values of the &lt;code&gt;User-Agent&lt;/code&gt; header or the query string. For example, you can create a &lt;code&gt;RegexMatchSet&lt;/code&gt; that contains a &lt;code&gt;RegexMatchTuple&lt;/code&gt; that looks for any requests with &lt;code&gt;User-Agent&lt;/code&gt; headers that match a &lt;code&gt;RegexPatternSet&lt;/code&gt; with pattern &lt;code&gt;B[a@]dB[o0]t&lt;/code&gt;. You can then configure AWS WAF to reject those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;RegexMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateRegexMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateRegexMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateRegexMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateRegexMatchSet&lt;/a&gt; request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value, using a &lt;code&gt;RegexPatternSet&lt;/code&gt;, that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateRegexMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_regex_pattern_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_regex_pattern_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;code&gt;RegexPatternSet&lt;/code&gt;. You then use &lt;a&gt;UpdateRegexPatternSet&lt;/a&gt; to specify the regular expression (regex) pattern that you want AWS WAF to search for, such as &lt;code&gt;B[a@]dB[o0]t&lt;/code&gt;. You can then configure AWS WAF to reject those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;RegexPatternSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateRegexPatternSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateRegexPatternSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateRegexPatternSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateRegexPatternSet&lt;/a&gt; request to specify the string that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateRegexPatternSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;code&gt;Rule&lt;/code&gt;, which contains the &lt;code&gt;IPSet&lt;/code&gt; objects, &lt;code&gt;ByteMatchSet&lt;/code&gt; objects, and other predicates that identify the requests that you want to block. If you add more than one predicate to a &lt;code&gt;Rule&lt;/code&gt;, a request must match all of the specifications to be allowed or blocked. For example, suppose that you add the following to a &lt;code&gt;Rule&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;IPSet&lt;/code&gt; that matches the IP address &lt;code&gt;192.0.2.44/32&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ByteMatchSet&lt;/code&gt; that matches &lt;code&gt;BadBot&lt;/code&gt; in the &lt;code&gt;User-Agent&lt;/code&gt; header&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You then add the &lt;code&gt;Rule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt; and specify that you want to blocks requests that satisfy the &lt;code&gt;Rule&lt;/code&gt;. For a request to be blocked, it must come from the IP address 192.0.2.44 &lt;i&gt;and&lt;/i&gt; the &lt;code&gt;User-Agent&lt;/code&gt; header in the request must contain the value &lt;code&gt;BadBot&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;Rule&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create and update the predicates that you want to include in the &lt;code&gt;Rule&lt;/code&gt;. For more information, see &lt;a&gt;CreateByteMatchSet&lt;/a&gt;, &lt;a&gt;CreateIPSet&lt;/a&gt;, and &lt;a&gt;CreateSqlInjectionMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateRule&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateRule&lt;/code&gt; request to specify the predicates that you want to include in the &lt;code&gt;Rule&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create and update a &lt;code&gt;WebACL&lt;/code&gt; that contains the &lt;code&gt;Rule&lt;/code&gt;. For more information, see &lt;a&gt;CreateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def create_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_rule_group

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;code&gt;RuleGroup&lt;/code&gt;. A rule group is a collection of predefined rules that you add to a web ACL. You use &lt;a&gt;UpdateRuleGroup&lt;/a&gt; to add rules to the rule group.&lt;/p&gt; &lt;p&gt;Rule groups are subject to the following limits:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Three rule groups per account. You can request an increase to this limit by contacting customer support.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;One rule group per web ACL.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Ten rules per rule group.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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


async def create_size_constraint_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_size_constraint_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;code&gt;SizeConstraintSet&lt;/code&gt;. You then use &lt;a&gt;UpdateSizeConstraintSet&lt;/a&gt; to identify the part of a web request that you want AWS WAF to check for length, such as the length of the &lt;code&gt;User-Agent&lt;/code&gt; header or the length of the query string. For example, you can create a &lt;code&gt;SizeConstraintSet&lt;/code&gt; that matches any requests that have a query string that is longer than 100 bytes. You can then configure AWS WAF to reject those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;SizeConstraintSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateSizeConstraintSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateSizeConstraintSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateSizeConstraintSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateSizeConstraintSet&lt;/a&gt; request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateSizeConstraintSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_sql_injection_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_sql_injection_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;a&gt;SqlInjectionMatchSet&lt;/a&gt;, which you use to allow, block, or count requests that contain snippets of SQL code in a specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateSqlInjectionMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateSqlInjectionMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateSqlInjectionMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateSqlInjectionMatchSet&lt;/a&gt; request to specify the parts of web requests in which you want to allow, block, or count malicious SQL code.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateSqlInjectionMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates a &lt;code&gt;WebACL&lt;/code&gt;, which contains the &lt;code&gt;Rules&lt;/code&gt; that identify the CloudFront web requests that you want to allow, block, or count. AWS WAF evaluates &lt;code&gt;Rules&lt;/code&gt; in order based on the value of &lt;code&gt;Priority&lt;/code&gt; for each &lt;code&gt;Rule&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You also specify a default action, either &lt;code&gt;ALLOW&lt;/code&gt; or &lt;code&gt;BLOCK&lt;/code&gt;. If a web request doesn&#39;t match any of the &lt;code&gt;Rules&lt;/code&gt; in a &lt;code&gt;WebACL&lt;/code&gt;, AWS WAF responds to the request with the default action. &lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;WebACL&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create and update the &lt;code&gt;ByteMatchSet&lt;/code&gt; objects and other predicates that you want to include in &lt;code&gt;Rules&lt;/code&gt;. For more information, see &lt;a&gt;CreateByteMatchSet&lt;/a&gt;, &lt;a&gt;UpdateByteMatchSet&lt;/a&gt;, &lt;a&gt;CreateIPSet&lt;/a&gt;, &lt;a&gt;UpdateIPSet&lt;/a&gt;, &lt;a&gt;CreateSqlInjectionMatchSet&lt;/a&gt;, and &lt;a&gt;UpdateSqlInjectionMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create and update the &lt;code&gt;Rules&lt;/code&gt; that you want to include in the &lt;code&gt;WebACL&lt;/code&gt;. For more information, see &lt;a&gt;CreateRule&lt;/a&gt; and &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateWebACL&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateWebACL&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateWebACL&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateWebACL&lt;/a&gt; request to specify the &lt;code&gt;Rules&lt;/code&gt; that you want to include in the &lt;code&gt;WebACL&lt;/code&gt;, to specify the default action, and to associate the &lt;code&gt;WebACL&lt;/code&gt; with a CloudFront distribution.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def create_web_acl_migration_stack(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_web_acl_migration_stack

    &lt;p&gt;Creates an AWS CloudFormation WAFV2 template for the specified web ACL in the specified Amazon S3 bucket. Then, in CloudFormation, you create a stack from the template, to create the web ACL and its resources in AWS WAFV2. Use this to migrate your AWS WAF Classic web ACL to the latest version of AWS WAF.&lt;/p&gt; &lt;p&gt;This is part of a larger migration procedure for web ACLs from AWS WAF Classic to the latest version of AWS WAF. For the full procedure, including caveats and manual steps to complete the migration and switch over to the new web ACL, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-migrating-from-classic.html\&quot;&gt;Migrating your AWS WAF Classic resources to AWS WAF&lt;/a&gt; in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. &lt;/p&gt;

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
    body = CreateWebACLMigrationStackRequest.from_dict(body)
    return web.Response(status=200)


async def create_xss_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_xss_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Creates an &lt;a&gt;XssMatchSet&lt;/a&gt;, which you use to allow, block, or count requests that contain cross-site scripting attacks in the specified part of web requests. AWS WAF searches for character sequences that are likely to be malicious strings.&lt;/p&gt; &lt;p&gt;To create and configure an &lt;code&gt;XssMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;CreateXssMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;CreateXssMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateXssMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;a&gt;UpdateXssMatchSet&lt;/a&gt; request to specify the parts of web requests in which you want to allow, block, or count cross-site scripting attacks.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = CreateXssMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_byte_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_byte_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;ByteMatchSet&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;ByteMatchSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still includes any &lt;a&gt;ByteMatchTuple&lt;/a&gt; objects (any filters).&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;ByteMatchSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;ByteMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;ByteMatchSet&lt;/code&gt; to remove filters, if any. For more information, see &lt;a&gt;UpdateByteMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteByteMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteByteMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteByteMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_geo_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_geo_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;GeoMatchSet&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;GeoMatchSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still includes any countries.&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;GeoMatchSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;GeoMatchSet&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;GeoMatchSet&lt;/code&gt; to remove any countries. For more information, see &lt;a&gt;UpdateGeoMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteGeoMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteGeoMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteGeoMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_ip_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_ip_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes an &lt;a&gt;IPSet&lt;/a&gt;. You can&#39;t delete an &lt;code&gt;IPSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still includes any IP addresses.&lt;/p&gt; &lt;p&gt;If you just want to remove an &lt;code&gt;IPSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete an &lt;code&gt;IPSet&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;IPSet&lt;/code&gt; to remove IP address ranges, if any. For more information, see &lt;a&gt;UpdateIPSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteIPSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteIPSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteIPSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_logging_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_logging_configuration

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes the &lt;a&gt;LoggingConfiguration&lt;/a&gt; from the specified web ACL.&lt;/p&gt;

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
    body = DeleteLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_permission_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_permission_policy

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes an IAM policy from the specified RuleGroup.&lt;/p&gt; &lt;p&gt;The user making the request must be the owner of the RuleGroup.&lt;/p&gt;

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
    body = DeletePermissionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_rate_based_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rate_based_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;RateBasedRule&lt;/a&gt;. You can&#39;t delete a rule if it&#39;s still used in any &lt;code&gt;WebACL&lt;/code&gt; objects or if it still includes any predicates, such as &lt;code&gt;ByteMatchSet&lt;/code&gt; objects.&lt;/p&gt; &lt;p&gt;If you just want to remove a rule from a &lt;code&gt;WebACL&lt;/code&gt;, use &lt;a&gt;UpdateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;RateBasedRule&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;RateBasedRule&lt;/code&gt; to remove predicates, if any. For more information, see &lt;a&gt;UpdateRateBasedRule&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteRateBasedRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteRateBasedRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteRateBasedRuleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_regex_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_regex_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;RegexMatchSet&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;RegexMatchSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still includes any &lt;code&gt;RegexMatchTuples&lt;/code&gt; objects (any filters).&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;RegexMatchSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;RegexMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;RegexMatchSet&lt;/code&gt; to remove filters, if any. For more information, see &lt;a&gt;UpdateRegexMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteRegexMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteRegexMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteRegexMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_regex_pattern_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_regex_pattern_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;RegexPatternSet&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;RegexPatternSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;RegexMatchSet&lt;/code&gt; or if the &lt;code&gt;RegexPatternSet&lt;/code&gt; is not empty. &lt;/p&gt;

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
    body = DeleteRegexPatternSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;Rule&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;Rule&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;WebACL&lt;/code&gt; objects or if it still includes any predicates, such as &lt;code&gt;ByteMatchSet&lt;/code&gt; objects.&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;Rule&lt;/code&gt; from a &lt;code&gt;WebACL&lt;/code&gt;, use &lt;a&gt;UpdateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;Rule&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;Rule&lt;/code&gt; to remove predicates, if any. For more information, see &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteRule&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteRuleRequest.from_dict(body)
    return web.Response(status=200)


async def delete_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_rule_group

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;RuleGroup&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;RuleGroup&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;WebACL&lt;/code&gt; objects or if it still includes any rules.&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;RuleGroup&lt;/code&gt; from a &lt;code&gt;WebACL&lt;/code&gt;, use &lt;a&gt;UpdateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;RuleGroup&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;RuleGroup&lt;/code&gt; to remove rules, if any. For more information, see &lt;a&gt;UpdateRuleGroup&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteRuleGroup&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteRuleGroup&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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


async def delete_size_constraint_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_size_constraint_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;SizeConstraintSet&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;SizeConstraintSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still includes any &lt;a&gt;SizeConstraint&lt;/a&gt; objects (any filters).&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;SizeConstraintSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;SizeConstraintSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;SizeConstraintSet&lt;/code&gt; to remove filters, if any. For more information, see &lt;a&gt;UpdateSizeConstraintSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteSizeConstraintSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteSizeConstraintSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteSizeConstraintSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_sql_injection_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_sql_injection_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;SqlInjectionMatchSet&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still contains any &lt;a&gt;SqlInjectionMatchTuple&lt;/a&gt; objects.&lt;/p&gt; &lt;p&gt;If you just want to remove a &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete a &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt; to remove filters, if any. For more information, see &lt;a&gt;UpdateSqlInjectionMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteSqlInjectionMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteSqlInjectionMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteSqlInjectionMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def delete_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes a &lt;a&gt;WebACL&lt;/a&gt;. You can&#39;t delete a &lt;code&gt;WebACL&lt;/code&gt; if it still contains any &lt;code&gt;Rules&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;To delete a &lt;code&gt;WebACL&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;WebACL&lt;/code&gt; to remove &lt;code&gt;Rules&lt;/code&gt;, if any. For more information, see &lt;a&gt;UpdateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteWebACL&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteWebACL&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def delete_xss_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_xss_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Permanently deletes an &lt;a&gt;XssMatchSet&lt;/a&gt;. You can&#39;t delete an &lt;code&gt;XssMatchSet&lt;/code&gt; if it&#39;s still used in any &lt;code&gt;Rules&lt;/code&gt; or if it still contains any &lt;a&gt;XssMatchTuple&lt;/a&gt; objects.&lt;/p&gt; &lt;p&gt;If you just want to remove an &lt;code&gt;XssMatchSet&lt;/code&gt; from a &lt;code&gt;Rule&lt;/code&gt;, use &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To permanently delete an &lt;code&gt;XssMatchSet&lt;/code&gt; from AWS WAF, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Update the &lt;code&gt;XssMatchSet&lt;/code&gt; to remove filters, if any. For more information, see &lt;a&gt;UpdateXssMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of a &lt;code&gt;DeleteXssMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;code&gt;DeleteXssMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

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
    body = DeleteXssMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic Regional&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Removes a web ACL from the specified resource, either an application load balancer or Amazon API Gateway stage.&lt;/p&gt;

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
    body = DisassociateWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def get_byte_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_byte_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;ByteMatchSet&lt;/a&gt; specified by &lt;code&gt;ByteMatchSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetByteMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_change_token(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_change_token

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;When you want to create, update, or delete AWS WAF objects, get a change token and include the change token in the create, update, or delete request. Change tokens ensure that your application doesn&#39;t submit conflicting requests to AWS WAF.&lt;/p&gt; &lt;p&gt;Each create, update, or delete request must use a unique change token. If your application submits a &lt;code&gt;GetChangeToken&lt;/code&gt; request and then submits a second &lt;code&gt;GetChangeToken&lt;/code&gt; request before submitting a create, update, or delete request, the second &lt;code&gt;GetChangeToken&lt;/code&gt; request returns the same value as the first &lt;code&gt;GetChangeToken&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;When you use a change token in a create, update, or delete request, the status of the change token changes to &lt;code&gt;PENDING&lt;/code&gt;, which indicates that AWS WAF is propagating the change to all AWS WAF servers. Use &lt;code&gt;GetChangeTokenStatus&lt;/code&gt; to determine the status of your change token.&lt;/p&gt;

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


async def get_change_token_status(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_change_token_status

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the status of a &lt;code&gt;ChangeToken&lt;/code&gt; that you got by calling &lt;a&gt;GetChangeToken&lt;/a&gt;. &lt;code&gt;ChangeTokenStatus&lt;/code&gt; is one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PROVISIONED&lt;/code&gt;: You requested the change token by calling &lt;code&gt;GetChangeToken&lt;/code&gt;, but you haven&#39;t used it yet in a call to create, update, or delete an AWS WAF object.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PENDING&lt;/code&gt;: AWS WAF is propagating the create, update, or delete request to all AWS WAF servers.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;INSYNC&lt;/code&gt;: Propagation is complete.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = GetChangeTokenStatusRequest.from_dict(body)
    return web.Response(status=200)


async def get_geo_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_geo_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;GeoMatchSet&lt;/a&gt; that is specified by &lt;code&gt;GeoMatchSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetGeoMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_ip_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_ip_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;IPSet&lt;/a&gt; that is specified by &lt;code&gt;IPSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetIPSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_logging_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_logging_configuration

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;LoggingConfiguration&lt;/a&gt; for the specified web ACL.&lt;/p&gt;

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
    body = GetLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def get_permission_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_permission_policy

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the IAM policy attached to the RuleGroup.&lt;/p&gt;

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
    body = GetPermissionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def get_rate_based_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rate_based_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;RateBasedRule&lt;/a&gt; that is specified by the &lt;code&gt;RuleId&lt;/code&gt; that you included in the &lt;code&gt;GetRateBasedRule&lt;/code&gt; request.&lt;/p&gt;

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
    body = GetRateBasedRuleRequest.from_dict(body)
    return web.Response(status=200)


async def get_rate_based_rule_managed_keys(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rate_based_rule_managed_keys

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of IP addresses currently being blocked by the &lt;a&gt;RateBasedRule&lt;/a&gt; that is specified by the &lt;code&gt;RuleId&lt;/code&gt;. The maximum number of managed keys that will be blocked is 10,000. If more than 10,000 addresses exceed the rate limit, the 10,000 addresses with the highest rates will be blocked.&lt;/p&gt;

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
    body = GetRateBasedRuleManagedKeysRequest.from_dict(body)
    return web.Response(status=200)


async def get_regex_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_regex_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;RegexMatchSet&lt;/a&gt; specified by &lt;code&gt;RegexMatchSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetRegexMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_regex_pattern_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_regex_pattern_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;RegexPatternSet&lt;/a&gt; specified by &lt;code&gt;RegexPatternSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetRegexPatternSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;Rule&lt;/a&gt; that is specified by the &lt;code&gt;RuleId&lt;/code&gt; that you included in the &lt;code&gt;GetRule&lt;/code&gt; request.&lt;/p&gt;

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
    body = GetRuleRequest.from_dict(body)
    return web.Response(status=200)


async def get_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_rule_group

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;RuleGroup&lt;/a&gt; that is specified by the &lt;code&gt;RuleGroupId&lt;/code&gt; that you included in the &lt;code&gt;GetRuleGroup&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;To view the rules in a rule group, use &lt;a&gt;ListActivatedRulesInRuleGroup&lt;/a&gt;.&lt;/p&gt;

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
    body = GetRuleGroupRequest.from_dict(body)
    return web.Response(status=200)


async def get_sampled_requests(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sampled_requests

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Gets detailed information about a specified number of requests--a sample--that AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetSampledRequests&lt;/code&gt; returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, &lt;code&gt;GetSampledRequests&lt;/code&gt; returns an updated time range. This new time range indicates the actual period during which AWS WAF selected the requests in the sample.&lt;/p&gt;

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
    body = GetSampledRequestsRequest.from_dict(body)
    return web.Response(status=200)


async def get_size_constraint_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_size_constraint_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;SizeConstraintSet&lt;/a&gt; specified by &lt;code&gt;SizeConstraintSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetSizeConstraintSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_sql_injection_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_sql_injection_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;SqlInjectionMatchSet&lt;/a&gt; that is specified by &lt;code&gt;SqlInjectionMatchSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetSqlInjectionMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def get_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;WebACL&lt;/a&gt; that is specified by &lt;code&gt;WebACLId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def get_web_acl_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_web_acl_for_resource

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic Regional&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the web ACL for the specified resource, either an application load balancer or Amazon API Gateway stage.&lt;/p&gt;

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
    body = GetWebACLForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def get_xss_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_xss_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns the &lt;a&gt;XssMatchSet&lt;/a&gt; that is specified by &lt;code&gt;XssMatchSetId&lt;/code&gt;.&lt;/p&gt;

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
    body = GetXssMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def list_activated_rules_in_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_activated_rules_in_rule_group

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;ActivatedRule&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListActivatedRulesInRuleGroupRequest.from_dict(body)
    return web.Response(status=200)


async def list_byte_match_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_byte_match_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;ByteMatchSetSummary&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListByteMatchSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_geo_match_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_geo_match_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;GeoMatchSetSummary&lt;/a&gt; objects in the response.&lt;/p&gt;

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
    body = ListGeoMatchSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_ip_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_ip_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;IPSetSummary&lt;/a&gt; objects in the response.&lt;/p&gt;

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
    body = ListIPSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_logging_configurations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_logging_configurations

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;LoggingConfiguration&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListLoggingConfigurationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_rate_based_rules(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_rate_based_rules

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;RuleSummary&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListRateBasedRulesRequest.from_dict(body)
    return web.Response(status=200)


async def list_regex_match_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_regex_match_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;RegexMatchSetSummary&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListRegexMatchSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_regex_pattern_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_regex_pattern_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;RegexPatternSetSummary&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListRegexPatternSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_resources_for_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_resources_for_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic Regional&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of resources associated with the specified web ACL.&lt;/p&gt;

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
    body = ListResourcesForWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def list_rule_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_rule_groups

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;RuleGroup&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListRuleGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_rules(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_rules

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;RuleSummary&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListRulesRequest.from_dict(body)
    return web.Response(status=200)


async def list_size_constraint_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_size_constraint_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;SizeConstraintSetSummary&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListSizeConstraintSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_sql_injection_match_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_sql_injection_match_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;SqlInjectionMatchSet&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListSqlInjectionMatchSetsRequest.from_dict(body)
    return web.Response(status=200)


async def list_subscribed_rule_groups(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_subscribed_rule_groups

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;RuleGroup&lt;/a&gt; objects that you are subscribed to.&lt;/p&gt;

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
    body = ListSubscribedRuleGroupsRequest.from_dict(body)
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Retrieves the tags associated with the specified AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to \&quot;customer\&quot; and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.&lt;/p&gt; &lt;p&gt;Tagging is only available through the API, SDKs, and CLI. You can&#39;t manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules. &lt;/p&gt;

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
    body = ListTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def list_web_acls(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_web_acls

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;WebACLSummary&lt;/a&gt; objects in the response.&lt;/p&gt;

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
    body = ListWebACLsRequest.from_dict(body)
    return web.Response(status=200)


async def list_xss_match_sets(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_xss_match_sets

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Returns an array of &lt;a&gt;XssMatchSet&lt;/a&gt; objects.&lt;/p&gt;

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
    body = ListXssMatchSetsRequest.from_dict(body)
    return web.Response(status=200)


async def put_logging_configuration(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_logging_configuration

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Associates a &lt;a&gt;LoggingConfiguration&lt;/a&gt; with a specified web ACL.&lt;/p&gt; &lt;p&gt;You can access information about all traffic that AWS WAF inspects using the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create an Amazon Kinesis Data Firehose. &lt;/p&gt; &lt;p&gt;Create the data firehose with a PUT source and in the region that you are operating. However, if you are capturing logs for Amazon CloudFront, always create the firehose in US East (N. Virginia). &lt;/p&gt; &lt;note&gt; &lt;p&gt;Do not create the data firehose using a &lt;code&gt;Kinesis stream&lt;/code&gt; as your source.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Associate that firehose to your web ACL using a &lt;code&gt;PutLoggingConfiguration&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;When you successfully enable logging using a &lt;code&gt;PutLoggingConfiguration&lt;/code&gt; request, AWS WAF will create a service linked role with the necessary permissions to write logs to the Amazon Kinesis Data Firehose. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/logging.html\&quot;&gt;Logging Web ACL Traffic Information&lt;/a&gt; in the &lt;i&gt;AWS WAF Developer Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = PutLoggingConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_permission_policy(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_permission_policy

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Attaches an IAM policy to the specified resource. The only supported use for this action is to share a RuleGroup across accounts.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;PutPermissionPolicy&lt;/code&gt; is subject to the following restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can attach only one policy with each &lt;code&gt;PutPermissionPolicy&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The policy must include an &lt;code&gt;Effect&lt;/code&gt;, &lt;code&gt;Action&lt;/code&gt; and &lt;code&gt;Principal&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Effect&lt;/code&gt; must specify &lt;code&gt;Allow&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Action&lt;/code&gt; in the policy must be &lt;code&gt;waf:UpdateWebACL&lt;/code&gt;, &lt;code&gt;waf-regional:UpdateWebACL&lt;/code&gt;, &lt;code&gt;waf:GetRuleGroup&lt;/code&gt; and &lt;code&gt;waf-regional:GetRuleGroup&lt;/code&gt; . Any extra or wildcard actions in the policy will be rejected.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The policy cannot include a &lt;code&gt;Resource&lt;/code&gt; parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The ARN in the request must be a valid WAF RuleGroup ARN and the RuleGroup must exist in the same region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The user making the request must be the owner of the RuleGroup.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Your policy must be composed using IAM Policy version 2012-10-17.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html\&quot;&gt;IAM Policies&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;An example of a valid policy parameter is shown in the Examples section below.&lt;/p&gt;

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
    body = PutPermissionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Associates tags with the specified AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to \&quot;customer\&quot; and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.&lt;/p&gt; &lt;p&gt;Tagging is only available through the API, SDKs, and CLI. You can&#39;t manage or view tags through the AWS WAF Classic console. You can use this action to tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules. &lt;/p&gt;

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

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p/&gt;

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


async def update_byte_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_byte_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;ByteMatchTuple&lt;/a&gt; objects (filters) in a &lt;a&gt;ByteMatchSet&lt;/a&gt;. For each &lt;code&gt;ByteMatchTuple&lt;/code&gt; object, you specify the following values: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether to insert or delete the object from the array. If you want to change a &lt;code&gt;ByteMatchSetUpdate&lt;/code&gt; object, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the &lt;code&gt;User-Agent&lt;/code&gt; header. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The bytes (typically a string that corresponds with ASCII characters) that you want AWS WAF to look for. For more information, including how you specify the values for the AWS WAF API and the AWS CLI or SDKs, see &lt;code&gt;TargetString&lt;/code&gt; in the &lt;a&gt;ByteMatchTuple&lt;/a&gt; data type. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Where to look, such as at the beginning or the end of a query string.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example, you can add a &lt;code&gt;ByteMatchSetUpdate&lt;/code&gt; object that matches web requests in which &lt;code&gt;User-Agent&lt;/code&gt; headers contain the string &lt;code&gt;BadBot&lt;/code&gt;. You can then configure AWS WAF to block those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;ByteMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a &lt;code&gt;ByteMatchSet.&lt;/code&gt; For more information, see &lt;a&gt;CreateByteMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateByteMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateByteMatchSet&lt;/code&gt; request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateByteMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_geo_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_geo_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;GeoMatchConstraint&lt;/a&gt; objects in an &lt;code&gt;GeoMatchSet&lt;/code&gt;. For each &lt;code&gt;GeoMatchConstraint&lt;/code&gt; object, you specify the following values: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether to insert or delete the object from the array. If you want to change an &lt;code&gt;GeoMatchConstraint&lt;/code&gt; object, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Type&lt;/code&gt;. The only valid value for &lt;code&gt;Type&lt;/code&gt; is &lt;code&gt;Country&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Value&lt;/code&gt;, which is a two character code for the country to add to the &lt;code&gt;GeoMatchConstraint&lt;/code&gt; object. Valid codes are listed in &lt;a&gt;GeoMatchConstraint$Value&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To create and configure an &lt;code&gt;GeoMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;CreateGeoMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateGeoMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateGeoMatchSet&lt;/code&gt; request to specify the country that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;When you update an &lt;code&gt;GeoMatchSet&lt;/code&gt;, you specify the country that you want to add and/or the country that you want to delete. If you want to change a country, you delete the existing country and add the new one.&lt;/p&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateGeoMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_ip_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_ip_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;IPSetDescriptor&lt;/a&gt; objects in an &lt;code&gt;IPSet&lt;/code&gt;. For each &lt;code&gt;IPSetDescriptor&lt;/code&gt; object, you specify the following values: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether to insert or delete the object from the array. If you want to change an &lt;code&gt;IPSetDescriptor&lt;/code&gt; object, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The IP address version, &lt;code&gt;IPv4&lt;/code&gt; or &lt;code&gt;IPv6&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The IP address in CIDR notation, for example, &lt;code&gt;192.0.2.0/24&lt;/code&gt; (for the range of IP addresses from &lt;code&gt;192.0.2.0&lt;/code&gt; to &lt;code&gt;192.0.2.255&lt;/code&gt;) or &lt;code&gt;192.0.2.44/32&lt;/code&gt; (for the individual IP address &lt;code&gt;192.0.2.44&lt;/code&gt;). &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;AWS WAF supports IPv4 address ranges: /8 and any range between /16 through /32. AWS WAF supports IPv6 address ranges: /24, /32, /48, /56, /64, and /128. For more information about CIDR notation, see the Wikipedia entry &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing\&quot;&gt;Classless Inter-Domain Routing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;IPv6 addresses can be represented using any of the following formats:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;1111:0000:0000:0000:0000:0000:0000:0111/128&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;1111:0:0:0:0:0:0:0111/128&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;1111::0111/128&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;1111::111/128&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You use an &lt;code&gt;IPSet&lt;/code&gt; to specify which web requests you want to allow or block based on the IP addresses that the requests originated from. For example, if you&#39;re receiving a lot of requests from one or a small number of IP addresses and you want to block the requests, you can create an &lt;code&gt;IPSet&lt;/code&gt; that specifies those IP addresses, and then configure AWS WAF to block the requests. &lt;/p&gt; &lt;p&gt;To create and configure an &lt;code&gt;IPSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;CreateIPSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateIPSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateIPSet&lt;/code&gt; request to specify the IP addresses that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;When you update an &lt;code&gt;IPSet&lt;/code&gt;, you specify the IP addresses that you want to add and/or the IP addresses that you want to delete. If you want to change an IP address, you delete the existing IP address and add the new one.&lt;/p&gt; &lt;p&gt;You can insert a maximum of 1000 addresses in a single request.&lt;/p&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateIPSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_rate_based_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rate_based_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;Predicate&lt;/a&gt; objects in a rule and updates the &lt;code&gt;RateLimit&lt;/code&gt; in the rule. &lt;/p&gt; &lt;p&gt;Each &lt;code&gt;Predicate&lt;/code&gt; object identifies a predicate, such as a &lt;a&gt;ByteMatchSet&lt;/a&gt; or an &lt;a&gt;IPSet&lt;/a&gt;, that specifies the web requests that you want to block or count. The &lt;code&gt;RateLimit&lt;/code&gt; specifies the number of requests every five minutes that triggers the rule.&lt;/p&gt; &lt;p&gt;If you add more than one predicate to a &lt;code&gt;RateBasedRule&lt;/code&gt;, a request must match all the predicates and exceed the &lt;code&gt;RateLimit&lt;/code&gt; to be counted or blocked. For example, suppose you add the following to a &lt;code&gt;RateBasedRule&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;IPSet&lt;/code&gt; that matches the IP address &lt;code&gt;192.0.2.44/32&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ByteMatchSet&lt;/code&gt; that matches &lt;code&gt;BadBot&lt;/code&gt; in the &lt;code&gt;User-Agent&lt;/code&gt; header&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Further, you specify a &lt;code&gt;RateLimit&lt;/code&gt; of 1,000.&lt;/p&gt; &lt;p&gt;You then add the &lt;code&gt;RateBasedRule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt; and specify that you want to block requests that satisfy the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 &lt;i&gt;and&lt;/i&gt; the &lt;code&gt;User-Agent&lt;/code&gt; header in the request must contain the value &lt;code&gt;BadBot&lt;/code&gt;. Further, requests that match these two conditions much be received at a rate of more than 1,000 every five minutes. If the rate drops below this limit, AWS WAF no longer blocks the requests.&lt;/p&gt; &lt;p&gt;As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a &lt;code&gt;RateBasedRule&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ByteMatchSet&lt;/code&gt; with &lt;code&gt;FieldToMatch&lt;/code&gt; of &lt;code&gt;URI&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;PositionalConstraint&lt;/code&gt; of &lt;code&gt;STARTS_WITH&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;TargetString&lt;/code&gt; of &lt;code&gt;login&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Further, you specify a &lt;code&gt;RateLimit&lt;/code&gt; of 1,000.&lt;/p&gt; &lt;p&gt;By adding this &lt;code&gt;RateBasedRule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt;, you could limit requests to your login page without affecting the rest of your site.&lt;/p&gt;

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
    body = UpdateRateBasedRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_regex_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_regex_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;RegexMatchTuple&lt;/a&gt; objects (filters) in a &lt;a&gt;RegexMatchSet&lt;/a&gt;. For each &lt;code&gt;RegexMatchSetUpdate&lt;/code&gt; object, you specify the following values: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether to insert or delete the object from the array. If you want to change a &lt;code&gt;RegexMatchSetUpdate&lt;/code&gt; object, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The part of a web request that you want AWS WAF to inspectupdate, such as a query string or the value of the &lt;code&gt;User-Agent&lt;/code&gt; header. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see &lt;a&gt;RegexPatternSet&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; For example, you can create a &lt;code&gt;RegexPatternSet&lt;/code&gt; that matches any requests with &lt;code&gt;User-Agent&lt;/code&gt; headers that contain the string &lt;code&gt;B[a@]dB[o0]t&lt;/code&gt;. You can then configure AWS WAF to reject those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;RegexMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a &lt;code&gt;RegexMatchSet.&lt;/code&gt; For more information, see &lt;a&gt;CreateRegexMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateRegexMatchSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateRegexMatchSet&lt;/code&gt; request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the identifier of the &lt;code&gt;RegexPatternSet&lt;/code&gt; that contain the regular expression patters you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateRegexMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_regex_pattern_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_regex_pattern_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;code&gt;RegexPatternString&lt;/code&gt; objects in a &lt;a&gt;RegexPatternSet&lt;/a&gt;. For each &lt;code&gt;RegexPatternString&lt;/code&gt; object, you specify the following values: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether to insert or delete the &lt;code&gt;RegexPatternString&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The regular expression pattern that you want to insert or delete. For more information, see &lt;a&gt;RegexPatternSet&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; For example, you can create a &lt;code&gt;RegexPatternString&lt;/code&gt; such as &lt;code&gt;B[a@]dB[o0]t&lt;/code&gt;. AWS WAF will match this &lt;code&gt;RegexPatternString&lt;/code&gt; to:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;BadBot&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;BadB0t&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;B@dBot&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;B@dB0t&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To create and configure a &lt;code&gt;RegexPatternSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a &lt;code&gt;RegexPatternSet.&lt;/code&gt; For more information, see &lt;a&gt;CreateRegexPatternSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateRegexPatternSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateRegexPatternSet&lt;/code&gt; request to specify the regular expression pattern that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateRegexPatternSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_rule(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rule

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;Predicate&lt;/a&gt; objects in a &lt;code&gt;Rule&lt;/code&gt;. Each &lt;code&gt;Predicate&lt;/code&gt; object identifies a predicate, such as a &lt;a&gt;ByteMatchSet&lt;/a&gt; or an &lt;a&gt;IPSet&lt;/a&gt;, that specifies the web requests that you want to allow, block, or count. If you add more than one predicate to a &lt;code&gt;Rule&lt;/code&gt;, a request must match all of the specifications to be allowed, blocked, or counted. For example, suppose that you add the following to a &lt;code&gt;Rule&lt;/code&gt;: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ByteMatchSet&lt;/code&gt; that matches the value &lt;code&gt;BadBot&lt;/code&gt; in the &lt;code&gt;User-Agent&lt;/code&gt; header&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;IPSet&lt;/code&gt; that matches the IP address &lt;code&gt;192.0.2.44&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You then add the &lt;code&gt;Rule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt; and specify that you want to block requests that satisfy the &lt;code&gt;Rule&lt;/code&gt;. For a request to be blocked, the &lt;code&gt;User-Agent&lt;/code&gt; header in the request must contain the value &lt;code&gt;BadBot&lt;/code&gt; &lt;i&gt;and&lt;/i&gt; the request must originate from the IP address 192.0.2.44.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;Rule&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create and update the predicates that you want to include in the &lt;code&gt;Rule&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create the &lt;code&gt;Rule&lt;/code&gt;. See &lt;a&gt;CreateRule&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateRule&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateRule&lt;/code&gt; request to add predicates to the &lt;code&gt;Rule&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create and update a &lt;code&gt;WebACL&lt;/code&gt; that contains the &lt;code&gt;Rule&lt;/code&gt;. See &lt;a&gt;CreateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;If you want to replace one &lt;code&gt;ByteMatchSet&lt;/code&gt; or &lt;code&gt;IPSet&lt;/code&gt; with another, you delete the existing one and add the new one.&lt;/p&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateRuleRequest.from_dict(body)
    return web.Response(status=200)


async def update_rule_group(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_rule_group

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;ActivatedRule&lt;/a&gt; objects in a &lt;code&gt;RuleGroup&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can only insert &lt;code&gt;REGULAR&lt;/code&gt; rules into a rule group.&lt;/p&gt; &lt;p&gt;You can have a maximum of ten rules per rule group.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;RuleGroup&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create and update the &lt;code&gt;Rules&lt;/code&gt; that you want to include in the &lt;code&gt;RuleGroup&lt;/code&gt;. See &lt;a&gt;CreateRule&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateRuleGroup&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateRuleGroup&lt;/code&gt; request to add &lt;code&gt;Rules&lt;/code&gt; to the &lt;code&gt;RuleGroup&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create and update a &lt;code&gt;WebACL&lt;/code&gt; that contains the &lt;code&gt;RuleGroup&lt;/code&gt;. See &lt;a&gt;CreateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;If you want to replace one &lt;code&gt;Rule&lt;/code&gt; with another, you delete the existing one and add the new one.&lt;/p&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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


async def update_size_constraint_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_size_constraint_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;SizeConstraint&lt;/a&gt; objects (filters) in a &lt;a&gt;SizeConstraintSet&lt;/a&gt;. For each &lt;code&gt;SizeConstraint&lt;/code&gt; object, you specify the following values: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Whether to insert or delete the object from the array. If you want to change a &lt;code&gt;SizeConstraintSetUpdate&lt;/code&gt; object, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The part of a web request that you want AWS WAF to evaluate, such as the length of a query string or the length of the &lt;code&gt;User-Agent&lt;/code&gt; header.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Whether to perform any transformations on the request, such as converting it to lowercase, before checking its length. Note that transformations of the request body are not supported because the AWS resource forwards only the first &lt;code&gt;8192&lt;/code&gt; bytes of your request to AWS WAF.&lt;/p&gt; &lt;p&gt;You can only specify a single type of TextTransformation.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;ComparisonOperator&lt;/code&gt; used for evaluating the selected part of the request against the specified &lt;code&gt;Size&lt;/code&gt;, such as equals, greater than, less than, and so on.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The length, in bytes, that you want AWS WAF to watch for in selected part of the request. The length is computed after applying the transformation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example, you can add a &lt;code&gt;SizeConstraintSetUpdate&lt;/code&gt; object that matches web requests in which the length of the &lt;code&gt;User-Agent&lt;/code&gt; header is greater than 100 bytes. You can then configure AWS WAF to block those requests.&lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;SizeConstraintSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a &lt;code&gt;SizeConstraintSet.&lt;/code&gt; For more information, see &lt;a&gt;CreateSizeConstraintSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;code&gt;UpdateSizeConstraintSet&lt;/code&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateSizeConstraintSet&lt;/code&gt; request to specify the part of the request that you want AWS WAF to inspect (for example, the header or the URI) and the value that you want AWS WAF to watch for.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateSizeConstraintSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_sql_injection_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_sql_injection_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;SqlInjectionMatchTuple&lt;/a&gt; objects (filters) in a &lt;a&gt;SqlInjectionMatchSet&lt;/a&gt;. For each &lt;code&gt;SqlInjectionMatchTuple&lt;/code&gt; object, you specify the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Action&lt;/code&gt;: Whether to insert the object into or delete the object from the array. To change a &lt;code&gt;SqlInjectionMatchTuple&lt;/code&gt;, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FieldToMatch&lt;/code&gt;: The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TextTransformation&lt;/code&gt;: Which text transformation, if any, to perform on the web request before inspecting the request for snippets of malicious SQL code.&lt;/p&gt; &lt;p&gt;You can only specify a single type of TextTransformation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You use &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt; objects to specify which CloudFront requests that you want to allow, block, or count. For example, if you&#39;re receiving requests that contain snippets of SQL code in the query string and you want to block the requests, you can create a &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt; with the applicable settings, and then configure AWS WAF to block the requests. &lt;/p&gt; &lt;p&gt;To create and configure a &lt;code&gt;SqlInjectionMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;CreateSqlInjectionMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateIPSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateSqlInjectionMatchSet&lt;/code&gt; request to specify the parts of web requests that you want AWS WAF to inspect for snippets of SQL code.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateSqlInjectionMatchSetRequest.from_dict(body)
    return web.Response(status=200)


async def update_web_acl(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_web_acl

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;ActivatedRule&lt;/a&gt; objects in a &lt;code&gt;WebACL&lt;/code&gt;. Each &lt;code&gt;Rule&lt;/code&gt; identifies web requests that you want to allow, block, or count. When you update a &lt;code&gt;WebACL&lt;/code&gt;, you specify the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A default action for the &lt;code&gt;WebACL&lt;/code&gt;, either &lt;code&gt;ALLOW&lt;/code&gt; or &lt;code&gt;BLOCK&lt;/code&gt;. AWS WAF performs the default action if a request doesn&#39;t match the criteria in any of the &lt;code&gt;Rules&lt;/code&gt; in a &lt;code&gt;WebACL&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Rules&lt;/code&gt; that you want to add or delete. If you want to replace one &lt;code&gt;Rule&lt;/code&gt; with another, you delete the existing &lt;code&gt;Rule&lt;/code&gt; and add the new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For each &lt;code&gt;Rule&lt;/code&gt;, whether you want AWS WAF to allow requests, block requests, or count requests that match the conditions in the &lt;code&gt;Rule&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The order in which you want AWS WAF to evaluate the &lt;code&gt;Rules&lt;/code&gt; in a &lt;code&gt;WebACL&lt;/code&gt;. If you add more than one &lt;code&gt;Rule&lt;/code&gt; to a &lt;code&gt;WebACL&lt;/code&gt;, AWS WAF evaluates each request against the &lt;code&gt;Rules&lt;/code&gt; in order based on the value of &lt;code&gt;Priority&lt;/code&gt;. (The &lt;code&gt;Rule&lt;/code&gt; that has the lowest value for &lt;code&gt;Priority&lt;/code&gt; is evaluated first.) When a web request matches all the predicates (such as &lt;code&gt;ByteMatchSets&lt;/code&gt; and &lt;code&gt;IPSets&lt;/code&gt;) in a &lt;code&gt;Rule&lt;/code&gt;, AWS WAF immediately takes the corresponding action, allow or block, and doesn&#39;t evaluate the request against the remaining &lt;code&gt;Rules&lt;/code&gt; in the &lt;code&gt;WebACL&lt;/code&gt;, if any. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To create and configure a &lt;code&gt;WebACL&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create and update the predicates that you want to include in &lt;code&gt;Rules&lt;/code&gt;. For more information, see &lt;a&gt;CreateByteMatchSet&lt;/a&gt;, &lt;a&gt;UpdateByteMatchSet&lt;/a&gt;, &lt;a&gt;CreateIPSet&lt;/a&gt;, &lt;a&gt;UpdateIPSet&lt;/a&gt;, &lt;a&gt;CreateSqlInjectionMatchSet&lt;/a&gt;, and &lt;a&gt;UpdateSqlInjectionMatchSet&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create and update the &lt;code&gt;Rules&lt;/code&gt; that you want to include in the &lt;code&gt;WebACL&lt;/code&gt;. For more information, see &lt;a&gt;CreateRule&lt;/a&gt; and &lt;a&gt;UpdateRule&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create a &lt;code&gt;WebACL&lt;/code&gt;. See &lt;a&gt;CreateWebACL&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetChangeToken&lt;/code&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateWebACL&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateWebACL&lt;/code&gt; request to specify the &lt;code&gt;Rules&lt;/code&gt; that you want to include in the &lt;code&gt;WebACL&lt;/code&gt;, to specify the default action, and to associate the &lt;code&gt;WebACL&lt;/code&gt; with a CloudFront distribution. &lt;/p&gt; &lt;p&gt;The &lt;code&gt;ActivatedRule&lt;/code&gt; can be a rule group. If you specify a rule group as your &lt;code&gt;ActivatedRule&lt;/code&gt; , you can exclude specific rules from that rule group.&lt;/p&gt; &lt;p&gt;If you already have a rule group associated with a web ACL and want to submit an &lt;code&gt;UpdateWebACL&lt;/code&gt; request to exclude certain rules from that rule group, you must first remove the rule group from the web ACL, the re-insert it again, specifying the excluded rules. For details, see &lt;a&gt;ActivatedRule$ExcludedRules&lt;/a&gt; . &lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;Be aware that if you try to add a RATE_BASED rule to a web ACL without setting the rule type when first creating the rule, the &lt;a&gt;UpdateWebACL&lt;/a&gt; request will fail because the request tries to add a REGULAR rule (the default rule type) with the specified ID, which does not exist. &lt;/p&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateWebACLRequest.from_dict(body)
    return web.Response(status=200)


async def update_xss_match_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_xss_match_set

    &lt;note&gt; &lt;p&gt;This is &lt;b&gt;AWS WAF Classic&lt;/b&gt; documentation. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\&quot;&gt;AWS WAF Classic&lt;/a&gt; in the developer guide.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For the latest version of AWS WAF&lt;/b&gt;, use the AWS WAFV2 API and see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;. With the latest version, AWS WAF has a single set of endpoints for regional and global use. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;Inserts or deletes &lt;a&gt;XssMatchTuple&lt;/a&gt; objects (filters) in an &lt;a&gt;XssMatchSet&lt;/a&gt;. For each &lt;code&gt;XssMatchTuple&lt;/code&gt; object, you specify the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Action&lt;/code&gt;: Whether to insert the object into or delete the object from the array. To change an &lt;code&gt;XssMatchTuple&lt;/code&gt;, you delete the existing object and add a new one.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FieldToMatch&lt;/code&gt;: The part of web requests that you want AWS WAF to inspect and, if you want AWS WAF to inspect a header or custom query parameter, the name of the header or parameter.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TextTransformation&lt;/code&gt;: Which text transformation, if any, to perform on the web request before inspecting the request for cross-site scripting attacks.&lt;/p&gt; &lt;p&gt;You can only specify a single type of TextTransformation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You use &lt;code&gt;XssMatchSet&lt;/code&gt; objects to specify which CloudFront requests that you want to allow, block, or count. For example, if you&#39;re receiving requests that contain cross-site scripting attacks in the request body and you want to block the requests, you can create an &lt;code&gt;XssMatchSet&lt;/code&gt; with the applicable settings, and then configure AWS WAF to block the requests. &lt;/p&gt; &lt;p&gt;To create and configure an &lt;code&gt;XssMatchSet&lt;/code&gt;, perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Submit a &lt;a&gt;CreateXssMatchSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;a&gt;GetChangeToken&lt;/a&gt; to get the change token that you provide in the &lt;code&gt;ChangeToken&lt;/code&gt; parameter of an &lt;a&gt;UpdateIPSet&lt;/a&gt; request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Submit an &lt;code&gt;UpdateXssMatchSet&lt;/code&gt; request to specify the parts of web requests that you want AWS WAF to inspect for cross-site scripting attacks.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;For more information about how to use the AWS WAF API to allow or block HTTP requests, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/waf/latest/developerguide/\&quot;&gt;AWS WAF Developer Guide&lt;/a&gt;.&lt;/p&gt;

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
    body = UpdateXssMatchSetRequest.from_dict(body)
    return web.Response(status=200)
