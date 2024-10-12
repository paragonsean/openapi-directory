from typing import List, Dict
from aiohttp import web

from openapi_server.models.activate_key_signing_key_response import ActivateKeySigningKeyResponse
from openapi_server.models.associate_vpc_with_hosted_zone_request import AssociateVPCWithHostedZoneRequest
from openapi_server.models.associate_vpc_with_hosted_zone_response import AssociateVPCWithHostedZoneResponse
from openapi_server.models.change_cidr_collection_request import ChangeCidrCollectionRequest
from openapi_server.models.change_cidr_collection_response import ChangeCidrCollectionResponse
from openapi_server.models.change_tags_for_resource_request import ChangeTagsForResourceRequest
from openapi_server.models.create_cidr_collection_request import CreateCidrCollectionRequest
from openapi_server.models.create_cidr_collection_response import CreateCidrCollectionResponse
from openapi_server.models.create_health_check_request import CreateHealthCheckRequest
from openapi_server.models.create_health_check_response import CreateHealthCheckResponse
from openapi_server.models.create_hosted_zone_request import CreateHostedZoneRequest
from openapi_server.models.create_hosted_zone_response import CreateHostedZoneResponse
from openapi_server.models.create_key_signing_key_request import CreateKeySigningKeyRequest
from openapi_server.models.create_key_signing_key_response import CreateKeySigningKeyResponse
from openapi_server.models.create_query_logging_config_request import CreateQueryLoggingConfigRequest
from openapi_server.models.create_query_logging_config_response import CreateQueryLoggingConfigResponse
from openapi_server.models.create_reusable_delegation_set_request import CreateReusableDelegationSetRequest
from openapi_server.models.create_reusable_delegation_set_response import CreateReusableDelegationSetResponse
from openapi_server.models.create_traffic_policy_instance_request import CreateTrafficPolicyInstanceRequest
from openapi_server.models.create_traffic_policy_instance_response import CreateTrafficPolicyInstanceResponse
from openapi_server.models.create_traffic_policy_request import CreateTrafficPolicyRequest
from openapi_server.models.create_traffic_policy_response import CreateTrafficPolicyResponse
from openapi_server.models.create_traffic_policy_version_request import CreateTrafficPolicyVersionRequest
from openapi_server.models.create_traffic_policy_version_response import CreateTrafficPolicyVersionResponse
from openapi_server.models.create_vpc_association_authorization_request import CreateVPCAssociationAuthorizationRequest
from openapi_server.models.create_vpc_association_authorization_response import CreateVPCAssociationAuthorizationResponse
from openapi_server.models.deactivate_key_signing_key_response import DeactivateKeySigningKeyResponse
from openapi_server.models.delete_hosted_zone_response import DeleteHostedZoneResponse
from openapi_server.models.delete_key_signing_key_response import DeleteKeySigningKeyResponse
from openapi_server.models.disable_hosted_zone_dnssec_response import DisableHostedZoneDNSSECResponse
from openapi_server.models.disassociate_vpc_from_hosted_zone_request import DisassociateVPCFromHostedZoneRequest
from openapi_server.models.disassociate_vpc_from_hosted_zone_response import DisassociateVPCFromHostedZoneResponse
from openapi_server.models.enable_hosted_zone_dnssec_response import EnableHostedZoneDNSSECResponse
from openapi_server.models.get_account_limit_response import GetAccountLimitResponse
from openapi_server.models.get_change_response import GetChangeResponse
from openapi_server.models.get_checker_ip_ranges_response import GetCheckerIpRangesResponse
from openapi_server.models.get_dnssec_response import GetDNSSECResponse
from openapi_server.models.get_geo_location_response import GetGeoLocationResponse
from openapi_server.models.get_health_check_count_response import GetHealthCheckCountResponse
from openapi_server.models.get_health_check_last_failure_reason_response import GetHealthCheckLastFailureReasonResponse
from openapi_server.models.get_health_check_response import GetHealthCheckResponse
from openapi_server.models.get_health_check_status_response import GetHealthCheckStatusResponse
from openapi_server.models.get_hosted_zone_count_response import GetHostedZoneCountResponse
from openapi_server.models.get_hosted_zone_limit_response import GetHostedZoneLimitResponse
from openapi_server.models.get_hosted_zone_response import GetHostedZoneResponse
from openapi_server.models.get_query_logging_config_response import GetQueryLoggingConfigResponse
from openapi_server.models.get_reusable_delegation_set_limit_response import GetReusableDelegationSetLimitResponse
from openapi_server.models.get_reusable_delegation_set_response import GetReusableDelegationSetResponse
from openapi_server.models.get_traffic_policy_instance_count_response import GetTrafficPolicyInstanceCountResponse
from openapi_server.models.get_traffic_policy_instance_response import GetTrafficPolicyInstanceResponse
from openapi_server.models.get_traffic_policy_response import GetTrafficPolicyResponse
from openapi_server.models.list_cidr_blocks_response import ListCidrBlocksResponse
from openapi_server.models.list_cidr_collections_response import ListCidrCollectionsResponse
from openapi_server.models.list_cidr_locations_response import ListCidrLocationsResponse
from openapi_server.models.list_geo_locations_response import ListGeoLocationsResponse
from openapi_server.models.list_health_checks_response import ListHealthChecksResponse
from openapi_server.models.list_hosted_zones_by_name_response import ListHostedZonesByNameResponse
from openapi_server.models.list_hosted_zones_by_vpc_response import ListHostedZonesByVPCResponse
from openapi_server.models.list_hosted_zones_response import ListHostedZonesResponse
from openapi_server.models.list_query_logging_configs_response import ListQueryLoggingConfigsResponse
from openapi_server.models.list_resource_record_sets_response import ListResourceRecordSetsResponse
from openapi_server.models.list_reusable_delegation_sets_response import ListReusableDelegationSetsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_tags_for_resources_request import ListTagsForResourcesRequest
from openapi_server.models.list_tags_for_resources_response import ListTagsForResourcesResponse
from openapi_server.models.list_traffic_policies_response import ListTrafficPoliciesResponse
from openapi_server.models.list_traffic_policy_instances_by_hosted_zone_response import ListTrafficPolicyInstancesByHostedZoneResponse
from openapi_server.models.list_traffic_policy_instances_by_policy_response import ListTrafficPolicyInstancesByPolicyResponse
from openapi_server.models.list_traffic_policy_instances_response import ListTrafficPolicyInstancesResponse
from openapi_server.models.list_traffic_policy_versions_response import ListTrafficPolicyVersionsResponse
from openapi_server.models.list_vpc_association_authorizations_response import ListVPCAssociationAuthorizationsResponse
from openapi_server.models.test_dns_answer_response import TestDNSAnswerResponse
from openapi_server.models.update_health_check_request import UpdateHealthCheckRequest
from openapi_server.models.update_health_check_response import UpdateHealthCheckResponse
from openapi_server.models.update_hosted_zone_comment_request import UpdateHostedZoneCommentRequest
from openapi_server.models.update_hosted_zone_comment_response import UpdateHostedZoneCommentResponse
from openapi_server.models.update_traffic_policy_comment_request import UpdateTrafficPolicyCommentRequest
from openapi_server.models.update_traffic_policy_comment_response import UpdateTrafficPolicyCommentResponse
from openapi_server.models.update_traffic_policy_instance_request import UpdateTrafficPolicyInstanceRequest
from openapi_server.models.update_traffic_policy_instance_response import UpdateTrafficPolicyInstanceResponse
from openapi_server import util


async def activate_key_signing_key(request: web.Request, hosted_zone_id, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """activate_key_signing_key

    Activates a key-signing key (KSK) so that it can be used for signing by DNSSEC. This operation changes the KSK status to &lt;code&gt;ACTIVE&lt;/code&gt;.

    :param hosted_zone_id: A unique string used to identify a hosted zone.
    :type hosted_zone_id: str
    :param name: A string used to identify a key-signing key (KSK). &lt;code&gt;Name&lt;/code&gt; can include numbers, letters, and underscores (_). &lt;code&gt;Name&lt;/code&gt; must be unique for each key-signing key in the same hosted zone.
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def associate_vpc_with_hosted_zone(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_vpc_with_hosted_zone

    &lt;p&gt;Associates an Amazon VPC with a private hosted zone. &lt;/p&gt; &lt;important&gt; &lt;p&gt;To perform the association, the VPC and the private hosted zone must already exist. You can&#39;t convert a public hosted zone into a private hosted zone.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;If you want to associate a VPC that was created by using one Amazon Web Services account with a private hosted zone that was created by using a different account, the Amazon Web Services account that created the private hosted zone must first submit a &lt;code&gt;CreateVPCAssociationAuthorization&lt;/code&gt; request. Then the account that created the VPC must submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;When granting access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param id: &lt;p&gt;The ID of the private hosted zone that you want to associate an Amazon VPC with.&lt;/p&gt; &lt;p&gt;Note that you can&#39;t associate a VPC with a hosted zone that doesn&#39;t have an existing VPC association.&lt;/p&gt;
    :type id: str
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
    body = AssociateVPCWithHostedZoneRequest.from_dict(body)
    return web.Response(status=200)


async def change_cidr_collection(request: web.Request, cidr_collection_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """change_cidr_collection

    &lt;p&gt;Creates, changes, or deletes CIDR blocks within a collection. Contains authoritative IP information mapping blocks to one or multiple locations.&lt;/p&gt; &lt;p&gt;A change request can update multiple locations in a collection at a time, which is helpful if you want to move one or more CIDR blocks from one location to another in one transaction, without downtime. &lt;/p&gt; &lt;p&gt; &lt;b&gt;Limits&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The max number of CIDR blocks included in the request is 1000. As a result, big updates require multiple API calls.&lt;/p&gt; &lt;p&gt; &lt;b&gt; PUT and DELETE_IF_EXISTS&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Use &lt;code&gt;ChangeCidrCollection&lt;/code&gt; to perform the following actions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PUT&lt;/code&gt;: Create a CIDR block within the specified collection.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt; DELETE_IF_EXISTS&lt;/code&gt;: Delete an existing CIDR block from the collection.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param cidr_collection_id: The UUID of the CIDR collection to update.
    :type cidr_collection_id: str
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
    body = ChangeCidrCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def change_tags_for_resource(request: web.Request, resource_type, resource_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """change_tags_for_resource

    &lt;p&gt;Adds, edits, or deletes tags for a health check or a hosted zone.&lt;/p&gt; &lt;p&gt;For information about using tags for cost allocation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

    :param resource_type: &lt;p&gt;The type of the resource.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The resource type for health checks is &lt;code&gt;healthcheck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The resource type for hosted zones is &lt;code&gt;hostedzone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_type: str
    :param resource_id: The ID of the resource for which you want to add, change, or delete tags.
    :type resource_id: str
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
    body = ChangeTagsForResourceRequest.from_dict(body)
    return web.Response(status=200)


async def create_cidr_collection(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cidr_collection

    Creates a CIDR collection in the current Amazon Web Services account.

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
    body = CreateCidrCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def create_health_check(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_health_check

    &lt;p&gt;Creates a new health check.&lt;/p&gt; &lt;p&gt;For information about adding health checks to resource record sets, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html#Route53-Type-ResourceRecordSet-HealthCheckId\&quot;&gt;HealthCheckId&lt;/a&gt; in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html\&quot;&gt;ChangeResourceRecordSets&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; &lt;b&gt;ELB Load Balancers&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If you&#39;re registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to a Route 53 health check.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Private Hosted Zones&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can associate health checks with failover resource record sets in a private hosted zone. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 &lt;code&gt;StatusCheckFailed&lt;/code&gt; metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html\&quot;&gt;Amazon CloudWatch User Guide&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateHealthCheckRequest.from_dict(body)
    return web.Response(status=200)


async def create_hosted_zone(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_hosted_zone

    &lt;p&gt;Creates a new public or private hosted zone. You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs). &lt;/p&gt; &lt;important&gt; &lt;p&gt;You can&#39;t convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about charges for hosted zones, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/route53/pricing/\&quot;&gt;Amazon Route 53 Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can&#39;t create a hosted zone for a top-level domain (TLD) such as .com.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For public hosted zones, Route 53 automatically creates a default SOA record and four NS records for the zone. For more information about SOA and NS records, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/SOA-NSrecords.html\&quot;&gt;NS and SOA Records that Route 53 Creates for a Hosted Zone&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you want to use the same name servers for multiple public hosted zones, you can optionally associate a reusable delegation set with the hosted zone. See the &lt;code&gt;DelegationSetId&lt;/code&gt; element.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html\&quot;&gt;Migrating DNS Service for an Existing Domain to Amazon Route 53&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;When you submit a &lt;code&gt;CreateHostedZone&lt;/code&gt; request, the initial status of the hosted zone is &lt;code&gt;PENDING&lt;/code&gt;. For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to &lt;code&gt;INSYNC&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;CreateHostedZone&lt;/code&gt; request requires the caller to have an &lt;code&gt;ec2:DescribeVpcs&lt;/code&gt; permission.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = CreateHostedZoneRequest.from_dict(body)
    return web.Response(status=200)


async def create_key_signing_key(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_key_signing_key

    Creates a new key-signing key (KSK) associated with a hosted zone. You can only have two KSKs per hosted zone.

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
    body = CreateKeySigningKeyRequest.from_dict(body)
    return web.Response(status=200)


async def create_query_logging_config(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_query_logging_config

    &lt;p&gt;Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.&lt;/p&gt; &lt;p&gt;DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Route 53 edge location that responded to the DNS query&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Domain or subdomain that was requested&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DNS record type, such as A or AAAA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;DNS response code, such as &lt;code&gt;NoError&lt;/code&gt; or &lt;code&gt;ServFail&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;dl&gt; &lt;dt&gt;Log Group and Resource Policy&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Before you create a query logging configuration, perform the following operations.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically.&lt;/p&gt; &lt;/note&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must create the log group in the us-east-1 region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must use the same Amazon Web Services account to create the log group and the hosted zone that you want to configure query logging for.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When you create log groups for query logging, we recommend that you use a consistent prefix, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;/aws/route53/&lt;i&gt;hosted zone name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;In the next step, you&#39;ll create a resource policy, which controls access to one or more log groups and the associated Amazon Web Services resources, such as Route 53 hosted zones. There&#39;s a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. For the value of &lt;code&gt;Resource&lt;/code&gt;, specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with &lt;code&gt;*&lt;/code&gt;, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*&lt;/code&gt; &lt;/p&gt; &lt;p&gt;To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;aws:SourceArn&lt;/code&gt;, supply the hosted zone ARN used in creating the query logging configuration. For example, &lt;code&gt;aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For &lt;code&gt;aws:SourceAccount&lt;/code&gt;, supply the account ID for the account that creates the query logging configuration. For example, &lt;code&gt;aws:SourceAccount:111111111111&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html\&quot;&gt;The confused deputy problem&lt;/a&gt; in the &lt;i&gt;Amazon Web Services IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the Amazon Web Services SDKs, or the CLI.&lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/dd&gt; &lt;dt&gt;Log Streams and Edge Locations&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;When Route 53 finishes creating the configuration for DNS query logging, it does the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Begins to send query logs to the applicable log stream.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The name of each log stream is in the following format:&lt;/p&gt; &lt;p&gt; &lt;code&gt; &lt;i&gt;hosted zone ID&lt;/i&gt;/&lt;i&gt;edge location code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see \&quot;The Route 53 Global Network\&quot; on the &lt;a href&#x3D;\&quot;http://aws.amazon.com/route53/details/\&quot;&gt;Route 53 Product Details&lt;/a&gt; page.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Queries That Are Logged&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn&#39;t forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html\&quot;&gt;Routing Internet Traffic to Your Website or Web Application&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Log File Format&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;For a list of the values in each query log and the format of each value, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html\&quot;&gt;Logging DNS Queries&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;Pricing&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;For information about charges for query logs, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;How to Stop Logging&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html\&quot;&gt;DeleteQueryLoggingConfig&lt;/a&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt;

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
    body = CreateQueryLoggingConfigRequest.from_dict(body)
    return web.Response(status=200)


async def create_reusable_delegation_set(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_reusable_delegation_set

    &lt;p&gt;Creates a delegation set (a group of four name servers) that can be reused by multiple hosted zones that were created by the same Amazon Web Services account. &lt;/p&gt; &lt;p&gt;You can also create a reusable delegation set that uses the four name servers that are associated with an existing hosted zone. Specify the hosted zone ID in the &lt;code&gt;CreateReusableDelegationSet&lt;/code&gt; request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t associate a reusable delegation set with a private hosted zone.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;For information about using a reusable delegation set to configure white label name servers, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/white-label-name-servers.html\&quot;&gt;Configuring White Label Name Servers&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The process for migrating existing hosted zones to use a reusable delegation set is comparable to the process for configuring white label name servers. You need to perform the following steps:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Create a reusable delegation set.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Recreate hosted zones, and reduce the TTL to 60 seconds or less.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Recreate resource record sets in the new hosted zones.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change the registrar&#39;s name servers to use the name servers for the new hosted zones.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Monitor traffic for the website or application.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change TTLs back to their original values.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;If you want to migrate existing hosted zones to use a reusable delegation set, the existing hosted zones can&#39;t use any of the name servers that are assigned to the reusable delegation set. If one or more hosted zones do use one or more name servers that are assigned to the reusable delegation set, you can do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For small numbers of hosted zones—up to a few hundred—it&#39;s relatively easy to create reusable delegation sets until you get one that has four name servers that don&#39;t overlap with any of the name servers in your hosted zones.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For larger numbers of hosted zones, the easiest solution is to use more than one reusable delegation set.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For larger numbers of hosted zones, you can also migrate hosted zones that have overlapping name servers to hosted zones that don&#39;t have overlapping name servers, then migrate the hosted zones again to use the reusable delegation set.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateReusableDelegationSetRequest.from_dict(body)
    return web.Response(status=200)


async def create_traffic_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_traffic_policy

    Creates a traffic policy, which you use to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com).

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
    body = CreateTrafficPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_traffic_policy_instance(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_traffic_policy_instance

    Creates resource record sets in a specified hosted zone based on the settings in a specified traffic policy version. In addition, &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; associates the resource record sets with a specified domain name (such as example.com) or subdomain name (such as www.example.com). Amazon Route 53 responds to DNS queries for the domain or subdomain name by using the resource record sets that &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; created.

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
    body = CreateTrafficPolicyInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def create_traffic_policy_version(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_traffic_policy_version

    Creates a new version of an existing traffic policy. When you create a new version of a traffic policy, you specify the ID of the traffic policy that you want to update and a JSON-formatted document that describes the new version. You use traffic policies to create multiple DNS resource record sets for one domain name (such as example.com) or one subdomain name (such as www.example.com). You can create a maximum of 1000 versions of a traffic policy. If you reach the limit and need to create another version, you&#39;ll need to start a new traffic policy.

    :param id: The ID of the traffic policy for which you want to create a new version.
    :type id: str
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
    body = CreateTrafficPolicyVersionRequest.from_dict(body)
    return web.Response(status=200)


async def create_vpc_association_authorization(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_vpc_association_authorization

    &lt;p&gt;Authorizes the Amazon Web Services account that created a specified VPC to submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request to associate the VPC with a specified hosted zone that was created by a different account. To submit a &lt;code&gt;CreateVPCAssociationAuthorization&lt;/code&gt; request, you must use the account that created the hosted zone. After you authorize the association, use the account that created the VPC to submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to associate multiple VPCs that you created by using one account with a hosted zone that you created by using a different account, you must submit one authorization request for each VPC.&lt;/p&gt; &lt;/note&gt;

    :param id: The ID of the private hosted zone that you want to authorize associating a VPC with.
    :type id: str
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
    body = CreateVPCAssociationAuthorizationRequest.from_dict(body)
    return web.Response(status=200)


async def deactivate_key_signing_key(request: web.Request, hosted_zone_id, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """deactivate_key_signing_key

    Deactivates a key-signing key (KSK) so that it will not be used for signing by DNSSEC. This operation changes the KSK status to &lt;code&gt;INACTIVE&lt;/code&gt;.

    :param hosted_zone_id: A unique string used to identify a hosted zone.
    :type hosted_zone_id: str
    :param name: A string used to identify a key-signing key (KSK).
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_cidr_collection(request: web.Request, cidr_collection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_cidr_collection

    Deletes a CIDR collection in the current Amazon Web Services account. The collection must be empty before it can be deleted.

    :param cidr_collection_id: The UUID of the collection to delete.
    :type cidr_collection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_health_check(request: web.Request, health_check_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_health_check

    &lt;p&gt;Deletes a health check.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Amazon Route 53 does not prevent you from deleting a health check even if the health check is associated with one or more resource record sets. If you delete a health check and you don&#39;t update the associated resource record sets, the future status of the health check can&#39;t be predicted and may change. This will affect the routing of DNS queries for your DNS failover configuration. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html#health-checks-deleting.html\&quot;&gt;Replacing and Deleting Health Checks&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you&#39;re using Cloud Map and you configured Cloud Map to create a Route 53 health check when you register an instance, you can&#39;t use the Route 53 &lt;code&gt;DeleteHealthCheck&lt;/code&gt; command to delete the health check. The health check is deleted automatically when you deregister the instance; there can be a delay of several hours before the health check is deleted from Route 53. &lt;/p&gt;

    :param health_check_id: The ID of the health check that you want to delete.
    :type health_check_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_hosted_zone(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_hosted_zone

    &lt;p&gt;Deletes a hosted zone.&lt;/p&gt; &lt;p&gt;If the hosted zone was created by another service, such as Cloud Map, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DeleteHostedZone.html#delete-public-hosted-zone-created-by-another-service\&quot;&gt;Deleting Public Hosted Zones That Were Created by Another Service&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt; for information about how to delete it. (The process is the same for public and private hosted zones that were created by another service.)&lt;/p&gt; &lt;p&gt;If you want to keep your domain registration but you want to stop routing internet traffic to your website or web application, we recommend that you delete resource record sets in the hosted zone instead of deleting the hosted zone.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you delete a hosted zone, you can&#39;t undelete it. You must create a new hosted zone and update the name servers for your domain registration, which can require up to 48 hours to take effect. (If you delegated responsibility for a subdomain to a hosted zone and you delete the child hosted zone, you must update the name servers in the parent hosted zone.) In addition, if you delete a hosted zone, someone could hijack the domain and route traffic to their own resources using your domain name.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;If you want to avoid the monthly charge for the hosted zone, you can transfer DNS service for the domain to a free DNS service. When you transfer DNS service, you have to update the name servers for the domain registration. If the domain is registered with Route 53, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_UpdateDomainNameservers.html\&quot;&gt;UpdateDomainNameservers&lt;/a&gt; for information about how to replace Route 53 name servers with name servers for the new DNS service. If the domain is registered with another registrar, use the method provided by the registrar to update name servers for the domain registration. For more information, perform an internet search on \&quot;free DNS service.\&quot;&lt;/p&gt; &lt;p&gt;You can delete a hosted zone only if it contains only the default SOA record and NS resource record sets. If the hosted zone contains other resource record sets, you must delete them before you can delete the hosted zone. If you try to delete a hosted zone that contains other resource record sets, the request fails, and Route 53 returns a &lt;code&gt;HostedZoneNotEmpty&lt;/code&gt; error. For information about deleting records from your hosted zone, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html\&quot;&gt;ChangeResourceRecordSets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To verify that the hosted zone has been deleted, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;GetHostedZone&lt;/code&gt; action to request information about the hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the &lt;code&gt;ListHostedZones&lt;/code&gt; action to get a list of the hosted zones associated with the current Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param id: The ID of the hosted zone you want to delete.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_key_signing_key(request: web.Request, hosted_zone_id, name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_key_signing_key

    &lt;p&gt;Deletes a key-signing key (KSK). Before you can delete a KSK, you must deactivate it. The KSK must be deactivated before you can delete it regardless of whether the hosted zone is enabled for DNSSEC signing.&lt;/p&gt; &lt;p&gt;You can use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeactivateKeySigningKey.html\&quot;&gt;DeactivateKeySigningKey&lt;/a&gt; to deactivate the key before you delete it.&lt;/p&gt; &lt;p&gt;Use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetDNSSEC.html\&quot;&gt;GetDNSSEC&lt;/a&gt; to verify that the KSK is in an &lt;code&gt;INACTIVE&lt;/code&gt; status.&lt;/p&gt;

    :param hosted_zone_id: A unique string used to identify a hosted zone.
    :type hosted_zone_id: str
    :param name: A string used to identify a key-signing key (KSK).
    :type name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_query_logging_config(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_query_logging_config

    &lt;p&gt;Deletes a configuration for DNS query logging. If you delete a configuration, Amazon Route 53 stops sending query logs to CloudWatch Logs. Route 53 doesn&#39;t delete any logs that are already in CloudWatch Logs.&lt;/p&gt; &lt;p&gt;For more information about DNS query logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html\&quot;&gt;CreateQueryLoggingConfig&lt;/a&gt;.&lt;/p&gt;

    :param id: The ID of the configuration that you want to delete. 
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_reusable_delegation_set(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_reusable_delegation_set

    &lt;p&gt;Deletes a reusable delegation set.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You can delete a reusable delegation set only if it isn&#39;t associated with any hosted zones.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;To verify that the reusable delegation set is not associated with any hosted zones, submit a &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetReusableDelegationSet.html\&quot;&gt;GetReusableDelegationSet&lt;/a&gt; request and specify the ID of the reusable delegation set that you want to delete.&lt;/p&gt;

    :param id: The ID of the reusable delegation set that you want to delete.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_traffic_policy(request: web.Request, id, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_traffic_policy

    &lt;p&gt;Deletes a traffic policy.&lt;/p&gt; &lt;p&gt;When you delete a traffic policy, Route 53 sets a flag on the policy to indicate that it has been deleted. However, Route 53 never fully deletes the traffic policy. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Deleted traffic policies aren&#39;t listed if you run &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListTrafficPolicies.html\&quot;&gt;ListTrafficPolicies&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; There&#39;s no way to get a list of deleted policies.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you retain the ID of the policy, you can get information about the policy, including the traffic policy document, by running &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetTrafficPolicy.html\&quot;&gt;GetTrafficPolicy&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param id: The ID of the traffic policy that you want to delete.
    :type id: str
    :param version: The version number of the traffic policy that you want to delete.
    :type version: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_traffic_policy_instance(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_traffic_policy_instance

    &lt;p&gt;Deletes a traffic policy instance and all of the resource record sets that Amazon Route 53 created when you created the instance.&lt;/p&gt; &lt;note&gt; &lt;p&gt;In the Route 53 console, traffic policy instances are known as policy records.&lt;/p&gt; &lt;/note&gt;

    :param id: &lt;p&gt;The ID of the traffic policy instance that you want to delete. &lt;/p&gt; &lt;important&gt; &lt;p&gt;When you delete a traffic policy instance, Amazon Route 53 also deletes all of the resource record sets that were created when you created the traffic policy instance.&lt;/p&gt; &lt;/important&gt;
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def delete_vpc_association_authorization(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_vpc_association_authorization

    &lt;p&gt;Removes authorization to submit an &lt;code&gt;AssociateVPCWithHostedZone&lt;/code&gt; request to associate a specified VPC with a hosted zone that was created by a different account. You must use the account that created the hosted zone to submit a &lt;code&gt;DeleteVPCAssociationAuthorization&lt;/code&gt; request.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Sending this request only prevents the Amazon Web Services account that created the VPC from associating the VPC with the Amazon Route 53 hosted zone in the future. If the VPC is already associated with the hosted zone, &lt;code&gt;DeleteVPCAssociationAuthorization&lt;/code&gt; won&#39;t disassociate the VPC from the hosted zone. If you want to delete an existing association, use &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

    :param id: When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, the ID of the hosted zone.
    :type id: str
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
    body = CreateVPCAssociationAuthorizationRequest.from_dict(body)
    return web.Response(status=200)


async def disable_hosted_zone_dnssec(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_hosted_zone_dnssec

    Disables DNSSEC signing in a specific hosted zone. This action does not deactivate any key-signing keys (KSKs) that are active in the hosted zone.

    :param id: A unique string used to identify a hosted zone.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def disassociate_vpc_from_hosted_zone(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_vpc_from_hosted_zone

    &lt;p&gt;Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route 53 private hosted zone. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You can&#39;t disassociate the last Amazon VPC from a private hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can&#39;t convert a private hosted zone into a public hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can submit a &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt; request using either the account that created the hosted zone or the account that created the Amazon VPC.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Some services, such as Cloud Map and Amazon Elastic File System (Amazon EFS) automatically create hosted zones and associate VPCs with the hosted zones. A service can create a hosted zone using your account or using its own account. You can disassociate a VPC from a hosted zone only if the service created the hosted zone using your account.&lt;/p&gt; &lt;p&gt;When you run &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListHostedZonesByVPC.html\&quot;&gt;DisassociateVPCFromHostedZone&lt;/a&gt;, if the hosted zone has a value for &lt;code&gt;OwningAccount&lt;/code&gt;, you can use &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt;. If the hosted zone has a value for &lt;code&gt;OwningService&lt;/code&gt;, you can&#39;t use &lt;code&gt;DisassociateVPCFromHostedZone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;When revoking access, the hosted zone and the Amazon VPC must belong to the same partition. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param id: The ID of the private hosted zone that you want to disassociate a VPC from.
    :type id: str
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
    body = DisassociateVPCFromHostedZoneRequest.from_dict(body)
    return web.Response(status=200)


async def enable_hosted_zone_dnssec(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_hosted_zone_dnssec

    Enables DNSSEC signing in a specific hosted zone.

    :param id: A unique string used to identify a hosted zone.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_account_limit(request: web.Request, type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_account_limit

    &lt;p&gt;Gets the specified limit for the current account, for example, the maximum number of health checks that you can create using the account.&lt;/p&gt; &lt;p&gt;For the default limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. To request a higher limit, &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-route53\&quot;&gt;open a case&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You can also view account limits in Amazon Web Services Trusted Advisor. Sign in to the Amazon Web Services Management Console and open the Trusted Advisor console at &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/trustedadvisor\&quot;&gt;https://console.aws.amazon.com/trustedadvisor/&lt;/a&gt;. Then choose &lt;b&gt;Service limits&lt;/b&gt; in the navigation pane.&lt;/p&gt; &lt;/note&gt;

    :param type: &lt;p&gt;The limit that you want to get. Valid values include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_HEALTH_CHECKS_BY_OWNER&lt;/b&gt;: The maximum number of health checks that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_HOSTED_ZONES_BY_OWNER&lt;/b&gt;: The maximum number of hosted zones that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_REUSABLE_DELEGATION_SETS_BY_OWNER&lt;/b&gt;: The maximum number of reusable delegation sets that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_TRAFFIC_POLICIES_BY_OWNER&lt;/b&gt;: The maximum number of traffic policies that you can create using the current account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER&lt;/b&gt;: The maximum number of traffic policy instances that you can create using the current account. (Traffic policy instances are referred to as traffic flow policy records in the Amazon Route 53 console.)&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type type: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_change(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_change

    &lt;p&gt;Returns the current status of a change batch request. The status is one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PENDING&lt;/code&gt; indicates that the changes in this request have not propagated to all Amazon Route 53 DNS servers managing the hosted zone. This is the initial status of all change batch requests.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;INSYNC&lt;/code&gt; indicates that the changes have propagated to all Route 53 DNS servers managing the hosted zone. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param id: The ID of the change batch request. The value that you specify here is the value that &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; returned in the &lt;code&gt;Id&lt;/code&gt; element when you submitted the request.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_checker_ip_ranges(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_checker_ip_ranges

    &lt;p&gt;Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;code&gt;GetCheckerIpRanges&lt;/code&gt; still works, but we recommend that you download ip-ranges.json, which includes IP address ranges for all Amazon Web Services services. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-ip-addresses.html\&quot;&gt;IP Address Ranges of Amazon Route 53 Servers&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_dnssec(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_dnssec

    Returns information about DNSSEC for a specific hosted zone, including the key-signing keys (KSKs) in the hosted zone.

    :param id: A unique string used to identify a hosted zone.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_geo_location(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, continentcode=None, countrycode=None, subdivisioncode=None) -> web.Response:
    """get_geo_location

    &lt;p&gt;Gets information about whether a specified geographic location is supported for Amazon Route 53 geolocation resource record sets.&lt;/p&gt; &lt;p&gt;Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.&lt;/p&gt; &lt;p&gt;Use the following syntax to determine whether a continent is supported for geolocation:&lt;/p&gt; &lt;p&gt; &lt;code&gt;GET /2013-04-01/geolocation?continentcode&#x3D;&lt;i&gt;two-letter abbreviation for a continent&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;Use the following syntax to determine whether a country is supported for geolocation:&lt;/p&gt; &lt;p&gt; &lt;code&gt;GET /2013-04-01/geolocation?countrycode&#x3D;&lt;i&gt;two-character country code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;Use the following syntax to determine whether a subdivision of a country is supported for geolocation:&lt;/p&gt; &lt;p&gt; &lt;code&gt;GET /2013-04-01/geolocation?countrycode&#x3D;&lt;i&gt;two-character country code&lt;/i&gt;&amp;amp;subdivisioncode&#x3D;&lt;i&gt;subdivision code&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param continentcode: &lt;p&gt;For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Amazon Route 53 supports the following continent codes:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;AF&lt;/b&gt;: Africa&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;AN&lt;/b&gt;: Antarctica&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;AS&lt;/b&gt;: Asia&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;EU&lt;/b&gt;: Europe&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;OC&lt;/b&gt;: Oceania&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;NA&lt;/b&gt;: North America&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;SA&lt;/b&gt;: South America&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type continentcode: str
    :param countrycode: Amazon Route 53 uses the two-letter country codes that are specified in &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\&quot;&gt;ISO standard 3166-1 alpha-2&lt;/a&gt;.
    :type countrycode: str
    :param subdivisioncode: The code for the subdivision, such as a particular state within the United States. For a list of US state abbreviations, see &lt;a href&#x3D;\&quot;https://pe.usps.com/text/pub28/28apb.htm\&quot;&gt;Appendix B: Two–Letter State and Possession Abbreviations&lt;/a&gt; on the United States Postal Service website. For a list of all supported subdivision codes, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListGeoLocations.html\&quot;&gt;ListGeoLocations&lt;/a&gt; API.
    :type subdivisioncode: str

    """
    return web.Response(status=200)


async def get_health_check(request: web.Request, health_check_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_health_check

    Gets information about a specified health check.

    :param health_check_id: The identifier that Amazon Route 53 assigned to the health check when you created it. When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.
    :type health_check_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_health_check_count(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_health_check_count

    Retrieves the number of health checks that are associated with the current Amazon Web Services account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_health_check_last_failure_reason(request: web.Request, health_check_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_health_check_last_failure_reason

    Gets the reason that a specified health check failed most recently.

    :param health_check_id: &lt;p&gt;The ID for the health check for which you want the last failure reason. When you created the health check, &lt;code&gt;CreateHealthCheck&lt;/code&gt; returned the ID in the response, in the &lt;code&gt;HealthCheckId&lt;/code&gt; element.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to get the last failure reason for a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can&#39;t use &lt;code&gt;GetHealthCheckLastFailureReason&lt;/code&gt; for a calculated health check.&lt;/p&gt; &lt;/note&gt;
    :type health_check_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_health_check_status(request: web.Request, health_check_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_health_check_status

    &lt;p&gt;Gets status of a specified health check. &lt;/p&gt; &lt;important&gt; &lt;p&gt;This API is intended for use during development to diagnose behavior. It doesn’t support production use-cases with high query rates that require immediate and actionable responses.&lt;/p&gt; &lt;/important&gt;

    :param health_check_id: &lt;p&gt;The ID for the health check that you want the current status for. When you created the health check, &lt;code&gt;CreateHealthCheck&lt;/code&gt; returned the ID in the response, in the &lt;code&gt;HealthCheckId&lt;/code&gt; element.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If you want to check the status of a calculated health check, you must use the Amazon Route 53 console or the CloudWatch console. You can&#39;t use &lt;code&gt;GetHealthCheckStatus&lt;/code&gt; to get the status of a calculated health check.&lt;/p&gt; &lt;/note&gt;
    :type health_check_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_hosted_zone(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_hosted_zone

    Gets information about a specified hosted zone including the four name servers assigned to the hosted zone.

    :param id: The ID of the hosted zone that you want to get information about.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_hosted_zone_count(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_hosted_zone_count

    Retrieves the number of hosted zones that are associated with the current Amazon Web Services account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_hosted_zone_limit(request: web.Request, type, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_hosted_zone_limit

    &lt;p&gt;Gets the specified limit for a specified hosted zone, for example, the maximum number of records that you can create in the hosted zone. &lt;/p&gt; &lt;p&gt;For the default limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. To request a higher limit, &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-route53\&quot;&gt;open a case&lt;/a&gt;.&lt;/p&gt;

    :param type: &lt;p&gt;The limit that you want to get. Valid values include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_RRSETS_BY_ZONE&lt;/b&gt;: The maximum number of records that you can create in the specified hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;MAX_VPCS_ASSOCIATED_BY_ZONE&lt;/b&gt;: The maximum number of Amazon VPCs that you can associate with the specified private hosted zone.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type type: str
    :param id: The ID of the hosted zone that you want to get a limit for.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_query_logging_config(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_query_logging_config

    &lt;p&gt;Gets information about a specified configuration for DNS query logging.&lt;/p&gt; &lt;p&gt;For more information about DNS query logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html\&quot;&gt;CreateQueryLoggingConfig&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html\&quot;&gt;Logging DNS Queries&lt;/a&gt;.&lt;/p&gt;

    :param id: The ID of the configuration for DNS query logging that you want to get information about.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_reusable_delegation_set(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_reusable_delegation_set

    Retrieves information about a specified reusable delegation set, including the four name servers that are assigned to the delegation set.

    :param id: The ID of the reusable delegation set that you want to get a list of name servers for.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_reusable_delegation_set_limit(request: web.Request, type, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_reusable_delegation_set_limit

    &lt;p&gt;Gets the maximum number of hosted zones that you can associate with the specified reusable delegation set.&lt;/p&gt; &lt;p&gt;For the default limit, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html\&quot;&gt;Limits&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;. To request a higher limit, &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create?issueType&#x3D;service-limit-increase&amp;amp;limitType&#x3D;service-code-route53\&quot;&gt;open a case&lt;/a&gt;.&lt;/p&gt;

    :param type: Specify &lt;code&gt;MAX_ZONES_BY_REUSABLE_DELEGATION_SET&lt;/code&gt; to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.
    :type type: str
    :param id: The ID of the delegation set that you want to get the limit for.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_traffic_policy(request: web.Request, id, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_traffic_policy

    &lt;p&gt;Gets information about a specific traffic policy version.&lt;/p&gt; &lt;p&gt;For information about how of deleting a traffic policy affects the response from &lt;code&gt;GetTrafficPolicy&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html\&quot;&gt;DeleteTrafficPolicy&lt;/a&gt;. &lt;/p&gt;

    :param id: The ID of the traffic policy that you want to get information about.
    :type id: str
    :param version: The version number of the traffic policy that you want to get information about.
    :type version: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_traffic_policy_instance(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_traffic_policy_instance

    &lt;p&gt;Gets information about a specified traffic policy instance.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit a &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; or an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;In the Route 53 console, traffic policy instances are known as policy records.&lt;/p&gt; &lt;/note&gt;

    :param id: The ID of the traffic policy instance that you want to get information about.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def get_traffic_policy_instance_count(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_traffic_policy_instance_count

    Gets the number of traffic policy instances that are associated with the current Amazon Web Services account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_cidr_blocks(request: web.Request, cidr_collection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, location=None, nexttoken=None, maxresults=None, max_results=None, next_token=None) -> web.Response:
    """list_cidr_blocks

    Returns a paginated list of location objects and their CIDR blocks.

    :param cidr_collection_id: The UUID of the CIDR collection.
    :type cidr_collection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param location: The name of the CIDR collection location.
    :type location: str
    :param nexttoken: An opaque pagination token to indicate where the service is to begin enumerating results.
    :type nexttoken: str
    :param maxresults: Maximum number of results you want returned.
    :type maxresults: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_cidr_collections(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, nexttoken=None, maxresults=None, max_results=None, next_token=None) -> web.Response:
    """list_cidr_collections

    Returns a paginated list of CIDR collections in the Amazon Web Services account (metadata only).

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param nexttoken: &lt;p&gt;An opaque pagination token to indicate where the service is to begin enumerating results.&lt;/p&gt; &lt;p&gt;If no value is provided, the listing of results starts from the beginning.&lt;/p&gt;
    :type nexttoken: str
    :param maxresults: The maximum number of CIDR collections to return in the response.
    :type maxresults: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_cidr_locations(request: web.Request, cidr_collection_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, nexttoken=None, maxresults=None, max_results=None, next_token=None) -> web.Response:
    """list_cidr_locations

    Returns a paginated list of CIDR locations for the given collection (metadata only, does not include CIDR blocks).

    :param cidr_collection_id: The CIDR collection ID.
    :type cidr_collection_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param nexttoken: &lt;p&gt;An opaque pagination token to indicate where the service is to begin enumerating results.&lt;/p&gt; &lt;p&gt;If no value is provided, the listing of results starts from the beginning.&lt;/p&gt;
    :type nexttoken: str
    :param maxresults: The maximum number of CIDR collection locations to return in the response.
    :type maxresults: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_geo_locations(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, startcontinentcode=None, startcountrycode=None, startsubdivisioncode=None, maxitems=None) -> web.Response:
    """list_geo_locations

    &lt;p&gt;Retrieves a list of supported geographic locations.&lt;/p&gt; &lt;p&gt;Countries are listed first, and continents are listed last. If Amazon Route 53 supports subdivisions for a country (for example, states or provinces), the subdivisions for that country are listed in alphabetical order immediately after the corresponding country.&lt;/p&gt; &lt;p&gt;Route 53 does not perform authorization for this API because it retrieves information that is already available to the public.&lt;/p&gt; &lt;p&gt;For a list of supported geolocation codes, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html\&quot;&gt;GeoLocation&lt;/a&gt; data type.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param startcontinentcode: &lt;p&gt;The code for the continent with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if &lt;code&gt;IsTruncated&lt;/code&gt; is true, and if &lt;code&gt;NextContinentCode&lt;/code&gt; from the previous response has a value, enter that value in &lt;code&gt;startcontinentcode&lt;/code&gt; to return the next page of results.&lt;/p&gt; &lt;p&gt;Include &lt;code&gt;startcontinentcode&lt;/code&gt; only if you want to list continents. Don&#39;t include &lt;code&gt;startcontinentcode&lt;/code&gt; when you&#39;re listing countries or countries with their subdivisions.&lt;/p&gt;
    :type startcontinentcode: str
    :param startcountrycode: The code for the country with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;, and if &lt;code&gt;NextCountryCode&lt;/code&gt; from the previous response has a value, enter that value in &lt;code&gt;startcountrycode&lt;/code&gt; to return the next page of results.
    :type startcountrycode: str
    :param startsubdivisioncode: &lt;p&gt;The code for the state of the United States with which you want to start listing locations that Amazon Route 53 supports for geolocation. If Route 53 has already returned a page or more of results, if &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;, and if &lt;code&gt;NextSubdivisionCode&lt;/code&gt; from the previous response has a value, enter that value in &lt;code&gt;startsubdivisioncode&lt;/code&gt; to return the next page of results.&lt;/p&gt; &lt;p&gt;To list subdivisions (U.S. states), you must include both &lt;code&gt;startcountrycode&lt;/code&gt; and &lt;code&gt;startsubdivisioncode&lt;/code&gt;.&lt;/p&gt;
    :type startsubdivisioncode: str
    :param maxitems: (Optional) The maximum number of geolocations to be included in the response body for this request. If more than &lt;code&gt;maxitems&lt;/code&gt; geolocations remain to be listed, then the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_health_checks(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, maxitems=None, max_items=None, marker2=None) -> web.Response:
    """list_health_checks

    Retrieve a list of the health checks that are associated with the current Amazon Web Services account. 

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more health checks. To get another group, submit another &lt;code&gt;ListHealthChecks&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the previous response, which is the ID of the first health check that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more health checks to get.&lt;/p&gt;
    :type marker: str
    :param maxitems: The maximum number of health checks that you want &lt;code&gt;ListHealthChecks&lt;/code&gt; to return in response to the current request. Amazon Route 53 returns a maximum of 100 items. If you set &lt;code&gt;MaxItems&lt;/code&gt; to a value greater than 100, Route 53 returns only the first 100 health checks. 
    :type maxitems: str
    :param max_items: Pagination limit
    :type max_items: str
    :param marker2: Pagination token
    :type marker2: str

    """
    return web.Response(status=200)


async def list_hosted_zones(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, maxitems=None, delegationsetid=None, max_items=None, marker2=None) -> web.Response:
    """list_hosted_zones

    &lt;p&gt;Retrieves a list of the public and private hosted zones that are associated with the current Amazon Web Services account. The response includes a &lt;code&gt;HostedZones&lt;/code&gt; child element for each hosted zone.&lt;/p&gt; &lt;p&gt;Amazon Route 53 returns a maximum of 100 items in each response. If you have a lot of hosted zones, you can use the &lt;code&gt;maxitems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more hosted zones. To get more hosted zones, submit another &lt;code&gt;ListHostedZones&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the previous response, which is the ID of the first hosted zone that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more hosted zones to get.&lt;/p&gt;
    :type marker: str
    :param maxitems: (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If you have more than &lt;code&gt;maxitems&lt;/code&gt; hosted zones, the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is &lt;code&gt;true&lt;/code&gt;, and the value of &lt;code&gt;NextMarker&lt;/code&gt; is the hosted zone ID of the first hosted zone that Route 53 will return if you submit another request.
    :type maxitems: str
    :param delegationsetid: If you&#39;re using reusable delegation sets and you want to list all of the hosted zones that are associated with a reusable delegation set, specify the ID of that reusable delegation set. 
    :type delegationsetid: str
    :param max_items: Pagination limit
    :type max_items: str
    :param marker2: Pagination token
    :type marker2: str

    """
    return web.Response(status=200)


async def list_hosted_zones_by_name(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, dnsname=None, hostedzoneid=None, maxitems=None) -> web.Response:
    """list_hosted_zones_by_name

    &lt;p&gt;Retrieves a list of your hosted zones in lexicographic order. The response includes a &lt;code&gt;HostedZones&lt;/code&gt; child element for each hosted zone created by the current Amazon Web Services account. &lt;/p&gt; &lt;p&gt; &lt;code&gt;ListHostedZonesByName&lt;/code&gt; sorts hosted zones by name with the labels reversed. For example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;com.example.www.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Note the trailing dot, which can change the sort order in some circumstances.&lt;/p&gt; &lt;p&gt;If the domain name includes escape characters or Punycode, &lt;code&gt;ListHostedZonesByName&lt;/code&gt; alphabetizes the domain name using the escaped or Punycoded value, which is the format that Amazon Route 53 saves in its database. For example, to create a hosted zone for exämple.com, you specify ex\\344mple.com for the domain name. &lt;code&gt;ListHostedZonesByName&lt;/code&gt; alphabetizes it as:&lt;/p&gt; &lt;p&gt; &lt;code&gt;com.ex\\344mple.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The labels are reversed and alphabetized using the escaped value. For more information about valid domain name formats, including internationalized domain names, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html\&quot;&gt;DNS Domain Name Format&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Route 53 returns up to 100 items in each response. If you have a lot of hosted zones, use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100. The response includes values that help navigate from one group of &lt;code&gt;MaxItems&lt;/code&gt; hosted zones to the next:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;DNSName&lt;/code&gt; and &lt;code&gt;HostedZoneId&lt;/code&gt; elements in the response contain the values, if any, specified for the &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters in the request that produced the current response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;MaxItems&lt;/code&gt; element in the response contains the value, if any, that you specified for the &lt;code&gt;maxitems&lt;/code&gt; parameter in the request that produced the current response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is true, there are more hosted zones associated with the current Amazon Web Services account. &lt;/p&gt; &lt;p&gt;If &lt;code&gt;IsTruncated&lt;/code&gt; is false, this response includes the last hosted zone that is associated with the current account. The &lt;code&gt;NextDNSName&lt;/code&gt; element and &lt;code&gt;NextHostedZoneId&lt;/code&gt; elements are omitted from the response.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;NextDNSName&lt;/code&gt; and &lt;code&gt;NextHostedZoneId&lt;/code&gt; elements in the response contain the domain name and the hosted zone ID of the next hosted zone that is associated with the current Amazon Web Services account. If you want to list more hosted zones, make another call to &lt;code&gt;ListHostedZonesByName&lt;/code&gt;, and specify the value of &lt;code&gt;NextDNSName&lt;/code&gt; and &lt;code&gt;NextHostedZoneId&lt;/code&gt; in the &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters, respectively.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param dnsname: (Optional) For your first request to &lt;code&gt;ListHostedZonesByName&lt;/code&gt;, include the &lt;code&gt;dnsname&lt;/code&gt; parameter only if you want to specify the name of the first hosted zone in the response. If you don&#39;t include the &lt;code&gt;dnsname&lt;/code&gt; parameter, Amazon Route 53 returns all of the hosted zones that were created by the current Amazon Web Services account, in ASCII order. For subsequent requests, include both &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters. For &lt;code&gt;dnsname&lt;/code&gt;, specify the value of &lt;code&gt;NextDNSName&lt;/code&gt; from the previous response.
    :type dnsname: str
    :param hostedzoneid: &lt;p&gt;(Optional) For your first request to &lt;code&gt;ListHostedZonesByName&lt;/code&gt;, do not include the &lt;code&gt;hostedzoneid&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have more hosted zones than the value of &lt;code&gt;maxitems&lt;/code&gt;, &lt;code&gt;ListHostedZonesByName&lt;/code&gt; returns only the first &lt;code&gt;maxitems&lt;/code&gt; hosted zones. To get the next group of &lt;code&gt;maxitems&lt;/code&gt; hosted zones, submit another request to &lt;code&gt;ListHostedZonesByName&lt;/code&gt; and include both &lt;code&gt;dnsname&lt;/code&gt; and &lt;code&gt;hostedzoneid&lt;/code&gt; parameters. For the value of &lt;code&gt;hostedzoneid&lt;/code&gt;, specify the value of the &lt;code&gt;NextHostedZoneId&lt;/code&gt; element from the previous response.&lt;/p&gt;
    :type hostedzoneid: str
    :param maxitems: The maximum number of hosted zones to be included in the response body for this request. If you have more than &lt;code&gt;maxitems&lt;/code&gt; hosted zones, then the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is true, and the values of &lt;code&gt;NextDNSName&lt;/code&gt; and &lt;code&gt;NextHostedZoneId&lt;/code&gt; specify the first hosted zone in the next group of &lt;code&gt;maxitems&lt;/code&gt; hosted zones. 
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_hosted_zones_by_vpc(request: web.Request, vpcid, vpcregion, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, maxitems=None, nexttoken=None) -> web.Response:
    """list_hosted_zones_by_vpc

    &lt;p&gt;Lists all the private hosted zones that a specified VPC is associated with, regardless of which Amazon Web Services account or Amazon Web Services service owns the hosted zones. The &lt;code&gt;HostedZoneOwner&lt;/code&gt; structure in the response contains one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;OwningAccount&lt;/code&gt; element, which contains the account number of either the current Amazon Web Services account or another Amazon Web Services account. Some services, such as Cloud Map, create hosted zones using the current account. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An &lt;code&gt;OwningService&lt;/code&gt; element, which identifies the Amazon Web Services service that created and owns the hosted zone. For example, if a hosted zone was created by Amazon Elastic File System (Amazon EFS), the value of &lt;code&gt;Owner&lt;/code&gt; is &lt;code&gt;efs.amazonaws.com&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;When listing private hosted zones, the hosted zone and the Amazon VPC must belong to the same partition where the hosted zones were created. A partition is a group of Amazon Web Services Regions. Each Amazon Web Services account is scoped to one partition.&lt;/p&gt; &lt;p&gt;The following are the supported partitions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws&lt;/code&gt; - Amazon Web Services Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-cn&lt;/code&gt; - China Regions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;aws-us-gov&lt;/code&gt; - Amazon Web Services GovCloud (US) Region&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;Access Management&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param vpcid: The ID of the Amazon VPC that you want to list hosted zones for.
    :type vpcid: str
    :param vpcregion: For the Amazon VPC that you specified for &lt;code&gt;VPCId&lt;/code&gt;, the Amazon Web Services Region that you created the VPC in. 
    :type vpcregion: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param maxitems: (Optional) The maximum number of hosted zones that you want Amazon Route 53 to return. If the specified VPC is associated with more than &lt;code&gt;MaxItems&lt;/code&gt; hosted zones, the response includes a &lt;code&gt;NextToken&lt;/code&gt; element. &lt;code&gt;NextToken&lt;/code&gt; contains an encrypted token that identifies the first hosted zone that Route 53 will return if you submit another request.
    :type maxitems: str
    :param nexttoken: &lt;p&gt;If the previous response included a &lt;code&gt;NextToken&lt;/code&gt; element, the specified VPC is associated with more hosted zones. To get more hosted zones, submit another &lt;code&gt;ListHostedZonesByVPC&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;NextToken&lt;/code&gt;, specify the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response.&lt;/p&gt; &lt;p&gt;If the previous response didn&#39;t include a &lt;code&gt;NextToken&lt;/code&gt; element, there are no more hosted zones to get.&lt;/p&gt;
    :type nexttoken: str

    """
    return web.Response(status=200)


async def list_query_logging_configs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, hostedzoneid=None, nexttoken=None, maxresults=None, max_results=None, next_token=None) -> web.Response:
    """list_query_logging_configs

    &lt;p&gt;Lists the configurations for DNS query logging that are associated with the current Amazon Web Services account or the configuration that is associated with a specified hosted zone.&lt;/p&gt; &lt;p&gt;For more information about DNS query logs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateQueryLoggingConfig.html\&quot;&gt;CreateQueryLoggingConfig&lt;/a&gt;. Additional information, including the format of DNS query logs, appears in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html\&quot;&gt;Logging DNS Queries&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param hostedzoneid: &lt;p&gt;(Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in &lt;code&gt;HostedZoneId&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;If you don&#39;t specify a hosted zone ID, &lt;code&gt;ListQueryLoggingConfigs&lt;/code&gt; returns all of the configurations that are associated with the current Amazon Web Services account.&lt;/p&gt;
    :type hostedzoneid: str
    :param nexttoken: &lt;p&gt;(Optional) If the current Amazon Web Services account has more than &lt;code&gt;MaxResults&lt;/code&gt; query logging configurations, use &lt;code&gt;NextToken&lt;/code&gt; to get the second and subsequent pages of results.&lt;/p&gt; &lt;p&gt;For the first &lt;code&gt;ListQueryLoggingConfigs&lt;/code&gt; request, omit this value.&lt;/p&gt; &lt;p&gt;For the second and subsequent requests, get the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response and specify that value for &lt;code&gt;NextToken&lt;/code&gt; in the request.&lt;/p&gt;
    :type nexttoken: str
    :param maxresults: &lt;p&gt;(Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current Amazon Web Services account has more than &lt;code&gt;MaxResults&lt;/code&gt; configurations, use the value of &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html#API_ListQueryLoggingConfigs_RequestSyntax\&quot;&gt;NextToken&lt;/a&gt; in the response to get the next page of results.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for &lt;code&gt;MaxResults&lt;/code&gt;, Route 53 returns up to 100 configurations.&lt;/p&gt;
    :type maxresults: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    return web.Response(status=200)


async def list_resource_record_sets(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, name=None, type=None, identifier=None, maxitems=None, max_items=None, start_record_name=None, start_record_type=None, start_record_identifier=None) -> web.Response:
    """list_resource_record_sets

    &lt;p&gt;Lists the resource record sets in a specified hosted zone.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListResourceRecordSets&lt;/code&gt; returns up to 300 resource record sets at a time in ASCII order, beginning at a position specified by the &lt;code&gt;name&lt;/code&gt; and &lt;code&gt;type&lt;/code&gt; elements.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Sort order&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;ListResourceRecordSets&lt;/code&gt; sorts results first by DNS name with the labels reversed, for example:&lt;/p&gt; &lt;p&gt; &lt;code&gt;com.example.www.&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Note the trailing dot, which can change the sort order when the record name contains characters that appear before &lt;code&gt;.&lt;/code&gt; (decimal 46) in the ASCII table. These characters include the following: &lt;code&gt;! \&quot; # $ % &amp;amp; &#39; ( ) * + , -&lt;/code&gt; &lt;/p&gt; &lt;p&gt;When multiple records have the same DNS name, &lt;code&gt;ListResourceRecordSets&lt;/code&gt; sorts results by the record type.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Specifying where to start listing records&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can use the name and type elements to specify the resource record set that the list begins with:&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;If you do not specify Name or Type&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The results begin with the first resource record set that the hosted zone contains.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;If you specify Name but not Type&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The results begin with the first resource record set in the list whose name is greater than or equal to &lt;code&gt;Name&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;If you specify Type but not Name&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Amazon Route 53 returns the &lt;code&gt;InvalidInput&lt;/code&gt; error.&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;If you specify both Name and Type&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;The results begin with the first resource record set in the list whose name is greater than or equal to &lt;code&gt;Name&lt;/code&gt;, and whose type is greater than or equal to &lt;code&gt;Type&lt;/code&gt;.&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;p&gt; &lt;b&gt;Resource record sets that are PENDING&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This action returns the most current version of the records. This includes records that are &lt;code&gt;PENDING&lt;/code&gt;, and that are not yet available on all Route 53 DNS servers.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Changing resource record sets&lt;/b&gt; &lt;/p&gt; &lt;p&gt;To ensure that you get an accurate listing of the resource record sets for a hosted zone at a point in time, do not submit a &lt;code&gt;ChangeResourceRecordSets&lt;/code&gt; request while you&#39;re paging through the results of a &lt;code&gt;ListResourceRecordSets&lt;/code&gt; request. If you do, some pages may display results without the latest changes while other pages display results with the latest changes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Displaying the next page of results&lt;/b&gt; &lt;/p&gt; &lt;p&gt;If a &lt;code&gt;ListResourceRecordSets&lt;/code&gt; command returns more than one page of results, the value of &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. To display the next page of results, get the values of &lt;code&gt;NextRecordName&lt;/code&gt;, &lt;code&gt;NextRecordType&lt;/code&gt;, and &lt;code&gt;NextRecordIdentifier&lt;/code&gt; (if any) from the response. Then submit another &lt;code&gt;ListResourceRecordSets&lt;/code&gt; request, and specify those values for &lt;code&gt;StartRecordName&lt;/code&gt;, &lt;code&gt;StartRecordType&lt;/code&gt;, and &lt;code&gt;StartRecordIdentifier&lt;/code&gt;.&lt;/p&gt;

    :param id: The ID of the hosted zone that contains the resource record sets that you want to list.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param name: The first name in the lexicographic ordering of resource record sets that you want to list. If the specified record name doesn&#39;t exist, the results begin with the first resource record set that has a name greater than the value of &lt;code&gt;name&lt;/code&gt;.
    :type name: str
    :param type: &lt;p&gt;The type of resource record set to begin the record listing from.&lt;/p&gt; &lt;p&gt;Valid values for basic resource record sets: &lt;code&gt;A&lt;/code&gt; | &lt;code&gt;AAAA&lt;/code&gt; | &lt;code&gt;CAA&lt;/code&gt; | &lt;code&gt;CNAME&lt;/code&gt; | &lt;code&gt;MX&lt;/code&gt; | &lt;code&gt;NAPTR&lt;/code&gt; | &lt;code&gt;NS&lt;/code&gt; | &lt;code&gt;PTR&lt;/code&gt; | &lt;code&gt;SOA&lt;/code&gt; | &lt;code&gt;SPF&lt;/code&gt; | &lt;code&gt;SRV&lt;/code&gt; | &lt;code&gt;TXT&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Values for weighted, latency, geolocation, and failover resource record sets: &lt;code&gt;A&lt;/code&gt; | &lt;code&gt;AAAA&lt;/code&gt; | &lt;code&gt;CAA&lt;/code&gt; | &lt;code&gt;CNAME&lt;/code&gt; | &lt;code&gt;MX&lt;/code&gt; | &lt;code&gt;NAPTR&lt;/code&gt; | &lt;code&gt;PTR&lt;/code&gt; | &lt;code&gt;SPF&lt;/code&gt; | &lt;code&gt;SRV&lt;/code&gt; | &lt;code&gt;TXT&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Values for alias resource record sets: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;API Gateway custom regional API or edge-optimized API&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;CloudFront distribution&lt;/b&gt;: A or AAAA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Elastic Beanstalk environment that has a regionalized subdomain&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Elastic Load Balancing load balancer&lt;/b&gt;: A | AAAA&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;S3 bucket&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;VPC interface VPC endpoint&lt;/b&gt;: A&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Another resource record set in this hosted zone:&lt;/b&gt; The type of the resource record set that the alias references.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Constraint: Specifying &lt;code&gt;type&lt;/code&gt; without specifying &lt;code&gt;name&lt;/code&gt; returns an &lt;code&gt;InvalidInput&lt;/code&gt; error.&lt;/p&gt;
    :type type: str
    :param identifier:  &lt;i&gt;Resource record sets that have a routing policy other than simple:&lt;/i&gt; If results were truncated for a given DNS name and type, specify the value of &lt;code&gt;NextRecordIdentifier&lt;/code&gt; from the previous response to get the next resource record set that has the current DNS name and type.
    :type identifier: str
    :param maxitems: (Optional) The maximum number of resource records sets to include in the response body for this request. If the response includes more than &lt;code&gt;maxitems&lt;/code&gt; resource record sets, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of the &lt;code&gt;NextRecordName&lt;/code&gt; and &lt;code&gt;NextRecordType&lt;/code&gt; elements in the response identify the first resource record set in the next group of &lt;code&gt;maxitems&lt;/code&gt; resource record sets.
    :type maxitems: str
    :param max_items: Pagination limit
    :type max_items: str
    :param start_record_name: Pagination token
    :type start_record_name: str
    :param start_record_type: Pagination token
    :type start_record_type: str
    :param start_record_identifier: Pagination token
    :type start_record_identifier: str

    """
    return web.Response(status=200)


async def list_reusable_delegation_sets(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, marker=None, maxitems=None) -> web.Response:
    """list_reusable_delegation_sets

    Retrieves a list of the reusable delegation sets that are associated with the current Amazon Web Services account.

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param marker: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more reusable delegation sets. To get another group, submit another &lt;code&gt;ListReusableDelegationSets&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;marker&lt;/code&gt;, specify the value of &lt;code&gt;NextMarker&lt;/code&gt; from the previous response, which is the ID of the first reusable delegation set that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more reusable delegation sets to get.&lt;/p&gt;
    :type marker: str
    :param maxitems: The number of reusable delegation sets that you want Amazon Route 53 to return in the response to this request. If you specify a value greater than 100, Route 53 returns only the first 100 reusable delegation sets.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_type, resource_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    &lt;p&gt;Lists tags for one health check or hosted zone. &lt;/p&gt; &lt;p&gt;For information about using tags for cost allocation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

    :param resource_type: &lt;p&gt;The type of the resource.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The resource type for health checks is &lt;code&gt;healthcheck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The resource type for hosted zones is &lt;code&gt;hostedzone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_type: str
    :param resource_id: The ID of the resource for which you want to retrieve tags.
    :type resource_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
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


async def list_tags_for_resources(request: web.Request, resource_type, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resources

    &lt;p&gt;Lists tags for up to 10 health checks or hosted zones.&lt;/p&gt; &lt;p&gt;For information about using tags for cost allocation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html\&quot;&gt;Using Cost Allocation Tags&lt;/a&gt; in the &lt;i&gt;Billing and Cost Management User Guide&lt;/i&gt;.&lt;/p&gt;

    :param resource_type: &lt;p&gt;The type of the resources.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The resource type for health checks is &lt;code&gt;healthcheck&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The resource type for hosted zones is &lt;code&gt;hostedzone&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type resource_type: str
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
    body = ListTagsForResourcesRequest.from_dict(body)
    return web.Response(status=200)


async def list_traffic_policies(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, trafficpolicyid=None, maxitems=None) -> web.Response:
    """list_traffic_policies

    &lt;p&gt;Gets information about the latest version for every traffic policy that is associated with the current Amazon Web Services account. Policies are listed in the order that they were created in. &lt;/p&gt; &lt;p&gt;For information about how of deleting a traffic policy affects the response from &lt;code&gt;ListTrafficPolicies&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteTrafficPolicy.html\&quot;&gt;DeleteTrafficPolicy&lt;/a&gt;. &lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param trafficpolicyid: &lt;p&gt;(Conditional) For your first request to &lt;code&gt;ListTrafficPolicies&lt;/code&gt;, don&#39;t include the &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have more traffic policies than the value of &lt;code&gt;MaxItems&lt;/code&gt;, &lt;code&gt;ListTrafficPolicies&lt;/code&gt; returns only the first &lt;code&gt;MaxItems&lt;/code&gt; traffic policies. To get the next group of policies, submit another request to &lt;code&gt;ListTrafficPolicies&lt;/code&gt;. For the value of &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt; that was returned in the previous response.&lt;/p&gt;
    :type trafficpolicyid: str
    :param maxitems: (Optional) The maximum number of traffic policies that you want Amazon Route 53 to return in response to this request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policies, the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is &lt;code&gt;true&lt;/code&gt;, and the value of &lt;code&gt;TrafficPolicyIdMarker&lt;/code&gt; is the ID of the first traffic policy that Route 53 will return if you submit another request.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_traffic_policy_instances(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, hostedzoneid=None, trafficpolicyinstancename=None, trafficpolicyinstancetype=None, maxitems=None) -> web.Response:
    """list_traffic_policy_instances

    &lt;p&gt;Gets information about the traffic policy instances that you created by using the current Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param hostedzoneid: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;HostedZoneId&lt;/code&gt;, specify the value of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt; from the previous response, which is the hosted zone ID of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type hostedzoneid: str
    :param trafficpolicyinstancename: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancename&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type trafficpolicyinstancename: str
    :param trafficpolicyinstancetype: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancetype&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type trafficpolicyinstancetype: str
    :param maxitems: The maximum number of traffic policy instances that you want Amazon Route 53 to return in response to a &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt;, &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt;, and &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; represent the first traffic policy instance in the next group of &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_traffic_policy_instances_by_hosted_zone(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, trafficpolicyinstancename=None, trafficpolicyinstancetype=None, maxitems=None) -> web.Response:
    """list_traffic_policy_instances_by_hosted_zone

    &lt;p&gt;Gets information about the traffic policy instances that you created in a specified hosted zone.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit a &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; or an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

    :param id: The ID of the hosted zone that you want to list traffic policy instances for.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param trafficpolicyinstancename: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancename&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type trafficpolicyinstancename: str
    :param trafficpolicyinstancetype: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response is true, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstances&lt;/code&gt; request. For the value of &lt;code&gt;trafficpolicyinstancetype&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; from the previous response, which is the type of the first traffic policy instance in the next group of traffic policy instances.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type trafficpolicyinstancetype: str
    :param maxitems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt;, &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt;, and &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_traffic_policy_instances_by_policy(request: web.Request, id, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, hostedzoneid=None, trafficpolicyinstancename=None, trafficpolicyinstancetype=None, maxitems=None) -> web.Response:
    """list_traffic_policy_instances_by_policy

    &lt;p&gt;Gets information about the traffic policy instances that you created by using a specify traffic policy version.&lt;/p&gt; &lt;note&gt; &lt;p&gt;After you submit a &lt;code&gt;CreateTrafficPolicyInstance&lt;/code&gt; or an &lt;code&gt;UpdateTrafficPolicyInstance&lt;/code&gt; request, there&#39;s a brief delay while Amazon Route 53 creates the resource record sets that are specified in the traffic policy definition. For more information, see the &lt;code&gt;State&lt;/code&gt; response element.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Route 53 returns a maximum of 100 items in each response. If you have a lot of traffic policy instances, you can use the &lt;code&gt;MaxItems&lt;/code&gt; parameter to list them in groups of up to 100.&lt;/p&gt;

    :param id: The ID of the traffic policy for which you want to list traffic policy instances.
    :type id: str
    :param version: The version of the traffic policy for which you want to list traffic policy instances. The version must be associated with the traffic policy that is specified by &lt;code&gt;TrafficPolicyId&lt;/code&gt;.
    :type version: int
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param hostedzoneid: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstancesByPolicy&lt;/code&gt; request. &lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;hostedzoneid&lt;/code&gt;, specify the value of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt; from the previous response, which is the hosted zone ID of the first traffic policy instance that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type hostedzoneid: str
    :param trafficpolicyinstancename: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstancesByPolicy&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;trafficpolicyinstancename&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type trafficpolicyinstancename: str
    :param trafficpolicyinstancetype: &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;true&lt;/code&gt;, you have more traffic policy instances. To get more traffic policy instances, submit another &lt;code&gt;ListTrafficPolicyInstancesByPolicy&lt;/code&gt; request.&lt;/p&gt; &lt;p&gt;For the value of &lt;code&gt;trafficpolicyinstancetype&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; from the previous response, which is the name of the first traffic policy instance that Amazon Route 53 will return if you submit another request.&lt;/p&gt; &lt;p&gt;If the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the previous response was &lt;code&gt;false&lt;/code&gt;, there are no more traffic policy instances to get.&lt;/p&gt;
    :type trafficpolicyinstancetype: str
    :param maxitems: The maximum number of traffic policy instances to be included in the response body for this request. If you have more than &lt;code&gt;MaxItems&lt;/code&gt; traffic policy instances, the value of the &lt;code&gt;IsTruncated&lt;/code&gt; element in the response is &lt;code&gt;true&lt;/code&gt;, and the values of &lt;code&gt;HostedZoneIdMarker&lt;/code&gt;, &lt;code&gt;TrafficPolicyInstanceNameMarker&lt;/code&gt;, and &lt;code&gt;TrafficPolicyInstanceTypeMarker&lt;/code&gt; represent the first traffic policy instance that Amazon Route 53 will return if you submit another request.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_traffic_policy_versions(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, trafficpolicyversion=None, maxitems=None) -> web.Response:
    """list_traffic_policy_versions

    &lt;p&gt;Gets information about all of the versions for a specified traffic policy.&lt;/p&gt; &lt;p&gt;Traffic policy versions are listed in numerical order by &lt;code&gt;VersionNumber&lt;/code&gt;.&lt;/p&gt;

    :param id: Specify the value of &lt;code&gt;Id&lt;/code&gt; of the traffic policy for which you want to list all versions.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param trafficpolicyversion: &lt;p&gt;For your first request to &lt;code&gt;ListTrafficPolicyVersions&lt;/code&gt;, don&#39;t include the &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;If you have more traffic policy versions than the value of &lt;code&gt;MaxItems&lt;/code&gt;, &lt;code&gt;ListTrafficPolicyVersions&lt;/code&gt; returns only the first group of &lt;code&gt;MaxItems&lt;/code&gt; versions. To get more traffic policy versions, submit another &lt;code&gt;ListTrafficPolicyVersions&lt;/code&gt; request. For the value of &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt;, specify the value of &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt; in the previous response.&lt;/p&gt;
    :type trafficpolicyversion: str
    :param maxitems: The maximum number of traffic policy versions that you want Amazon Route 53 to include in the response body for this request. If the specified traffic policy has more than &lt;code&gt;MaxItems&lt;/code&gt; versions, the value of &lt;code&gt;IsTruncated&lt;/code&gt; in the response is &lt;code&gt;true&lt;/code&gt;, and the value of the &lt;code&gt;TrafficPolicyVersionMarker&lt;/code&gt; element is the ID of the first version that Route 53 will return if you submit another request.
    :type maxitems: str

    """
    return web.Response(status=200)


async def list_vpc_association_authorizations(request: web.Request, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, nexttoken=None, maxresults=None) -> web.Response:
    """list_vpc_association_authorizations

    &lt;p&gt;Gets a list of the VPCs that were created by other accounts and that can be associated with a specified hosted zone because you&#39;ve submitted one or more &lt;code&gt;CreateVPCAssociationAuthorization&lt;/code&gt; requests. &lt;/p&gt; &lt;p&gt;The response includes a &lt;code&gt;VPCs&lt;/code&gt; element with a &lt;code&gt;VPC&lt;/code&gt; child element for each VPC that can be associated with the hosted zone.&lt;/p&gt;

    :param id: The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param nexttoken:  &lt;i&gt;Optional&lt;/i&gt;: If a response includes a &lt;code&gt;NextToken&lt;/code&gt; element, there are more VPCs that can be associated with the specified hosted zone. To get the next page of results, submit another request, and include the value of &lt;code&gt;NextToken&lt;/code&gt; from the response in the &lt;code&gt;nexttoken&lt;/code&gt; parameter in another &lt;code&gt;ListVPCAssociationAuthorizations&lt;/code&gt; request.
    :type nexttoken: str
    :param maxresults:  &lt;i&gt;Optional&lt;/i&gt;: An integer that specifies the maximum number of VPCs that you want Amazon Route 53 to return. If you don&#39;t specify a value for &lt;code&gt;MaxResults&lt;/code&gt;, Route 53 returns up to 50 VPCs per page.
    :type maxresults: str

    """
    return web.Response(status=200)


async def test_dns_answer(request: web.Request, hostedzoneid, recordname, recordtype, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, resolverip=None, edns0clientsubnetip=None, edns0clientsubnetmask=None) -> web.Response:
    """test_dns_answer

    &lt;p&gt;Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DNS resolver, an EDNS0 client subnet IP address, and a subnet mask. &lt;/p&gt; &lt;p&gt;This call only supports querying public hosted zones.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;TestDnsAnswer &lt;/code&gt; returns information similar to what you would expect from the answer section of the &lt;code&gt;dig&lt;/code&gt; command. Therefore, if you query for the name servers of a subdomain that point to the parent name servers, those will not be returned.&lt;/p&gt; &lt;/note&gt;

    :param hostedzoneid: The ID of the hosted zone that you want Amazon Route 53 to simulate a query for.
    :type hostedzoneid: str
    :param recordname: The name of the resource record set that you want Amazon Route 53 to simulate a query for.
    :type recordname: str
    :param recordtype: The type of the resource record set.
    :type recordtype: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param resolverip: If you want to simulate a request from a specific DNS resolver, specify the IP address for that resolver. If you omit this value, &lt;code&gt;TestDnsAnswer&lt;/code&gt; uses the IP address of a DNS resolver in the Amazon Web Services US East (N. Virginia) Region (&lt;code&gt;us-east-1&lt;/code&gt;).
    :type resolverip: str
    :param edns0clientsubnetip: If the resolver that you specified for resolverip supports EDNS0, specify the IPv4 or IPv6 address of a client in the applicable location, for example, &lt;code&gt;192.0.2.44&lt;/code&gt; or &lt;code&gt;2001:db8:85a3::8a2e:370:7334&lt;/code&gt;.
    :type edns0clientsubnetip: str
    :param edns0clientsubnetmask: &lt;p&gt;If you specify an IP address for &lt;code&gt;edns0clientsubnetip&lt;/code&gt;, you can optionally specify the number of bits of the IP address that you want the checking tool to include in the DNS query. For example, if you specify &lt;code&gt;192.0.2.44&lt;/code&gt; for &lt;code&gt;edns0clientsubnetip&lt;/code&gt; and &lt;code&gt;24&lt;/code&gt; for &lt;code&gt;edns0clientsubnetmask&lt;/code&gt;, the checking tool will simulate a request from 192.0.2.0/24. The default value is 24 bits for IPv4 addresses and 64 bits for IPv6 addresses.&lt;/p&gt; &lt;p&gt;The range of valid values depends on whether &lt;code&gt;edns0clientsubnetip&lt;/code&gt; is an IPv4 or an IPv6 address:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;IPv4&lt;/b&gt;: Specify a value between 0 and 32&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;IPv6&lt;/b&gt;: Specify a value between 0 and 128&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type edns0clientsubnetmask: str

    """
    return web.Response(status=200)


async def update_health_check(request: web.Request, health_check_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_health_check

    &lt;p&gt;Updates an existing health check. Note that some values can&#39;t be updated. &lt;/p&gt; &lt;p&gt;For more information about updating health checks, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating-deleting.html\&quot;&gt;Creating, Updating, and Deleting Health Checks&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt;

    :param health_check_id: The ID for the health check for which you want detailed information. When you created the health check, &lt;code&gt;CreateHealthCheck&lt;/code&gt; returned the ID in the response, in the &lt;code&gt;HealthCheckId&lt;/code&gt; element.
    :type health_check_id: str
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
    body = UpdateHealthCheckRequest.from_dict(body)
    return web.Response(status=200)


async def update_hosted_zone_comment(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_hosted_zone_comment

    Updates the comment for a specified hosted zone.

    :param id: The ID for the hosted zone that you want to update the comment for.
    :type id: str
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
    body = UpdateHostedZoneCommentRequest.from_dict(body)
    return web.Response(status=200)


async def update_traffic_policy_comment(request: web.Request, id, version, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_traffic_policy_comment

    Updates the comment for a specified traffic policy version.

    :param id: The value of &lt;code&gt;Id&lt;/code&gt; for the traffic policy that you want to update the comment for.
    :type id: str
    :param version: The value of &lt;code&gt;Version&lt;/code&gt; for the traffic policy that you want to update the comment for.
    :type version: int
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
    body = UpdateTrafficPolicyCommentRequest.from_dict(body)
    return web.Response(status=200)


async def update_traffic_policy_instance(request: web.Request, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_traffic_policy_instance

    &lt;p&gt;Updates the resource record sets in a specified hosted zone that were created based on the settings in a specified traffic policy version.&lt;/p&gt; &lt;p&gt;When you update a traffic policy instance, Amazon Route 53 continues to respond to DNS queries for the root resource record set name (such as example.com) while it replaces one group of resource record sets with another. Route 53 performs the following operations:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Route 53 creates a new group of resource record sets based on the specified traffic policy. This is true regardless of how significant the differences are between the existing resource record sets and the new resource record sets. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When all of the new resource record sets have been created, Route 53 starts to respond to DNS queries for the root resource record set name (such as example.com) by using the new resource record sets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Route 53 deletes the old group of resource record sets that are associated with the root resource record set name.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt;

    :param id: The ID of the traffic policy instance that you want to update.
    :type id: str
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
    body = UpdateTrafficPolicyInstanceRequest.from_dict(body)
    return web.Response(status=200)
