from typing import List, Dict
from aiohttp import web

from openapi_server.models.describe_report_creation_output import DescribeReportCreationOutput
from openapi_server.models.get_compliance_summary_input import GetComplianceSummaryInput
from openapi_server.models.get_compliance_summary_output import GetComplianceSummaryOutput
from openapi_server.models.get_resources_input import GetResourcesInput
from openapi_server.models.get_resources_output import GetResourcesOutput
from openapi_server.models.get_tag_keys_input import GetTagKeysInput
from openapi_server.models.get_tag_keys_output import GetTagKeysOutput
from openapi_server.models.get_tag_values_input import GetTagValuesInput
from openapi_server.models.get_tag_values_output import GetTagValuesOutput
from openapi_server.models.start_report_creation_input import StartReportCreationInput
from openapi_server.models.tag_resources_input import TagResourcesInput
from openapi_server.models.tag_resources_output import TagResourcesOutput
from openapi_server.models.untag_resources_input import UntagResourcesInput
from openapi_server.models.untag_resources_output import UntagResourcesOutput
from openapi_server import util


async def describe_report_creation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_report_creation

    &lt;p&gt;Describes the status of the &lt;code&gt;StartReportCreation&lt;/code&gt; operation. &lt;/p&gt; &lt;p&gt;You can call this operation only from the organization&#39;s management account and from the us-east-1 Region.&lt;/p&gt;

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


async def get_compliance_summary(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, pagination_token=None) -> web.Response:
    """get_compliance_summary

    &lt;p&gt;Returns a table that shows counts of resources that are noncompliant with their tag policies.&lt;/p&gt; &lt;p&gt;For more information on tag policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html\&quot;&gt;Tag Policies&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can call this operation only from the organization&#39;s management account and from the us-east-1 Region.&lt;/p&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    :param pagination_token: Pagination token
    :type pagination_token: str

    """
    body = GetComplianceSummaryInput.from_dict(body)
    return web.Response(status=200)


async def get_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, resources_per_page=None, pagination_token=None) -> web.Response:
    """get_resources

    &lt;p&gt;Returns all the tagged or previously tagged resources that are located in the specified Amazon Web Services Region for the account.&lt;/p&gt; &lt;p&gt;Depending on what information you want returned, you can also specify the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Filters&lt;/i&gt; that specify what tags and resource types you want returned. The response includes all tags that are associated with the requested resources.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Information about compliance with the account&#39;s effective tag policy. For more information on tag policies, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html\&quot;&gt;Tag Policies&lt;/a&gt; in the &lt;i&gt;Organizations User Guide.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    :param resources_per_page: Pagination limit
    :type resources_per_page: str
    :param pagination_token: Pagination token
    :type pagination_token: str

    """
    body = GetResourcesInput.from_dict(body)
    return web.Response(status=200)


async def get_tag_keys(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, pagination_token=None) -> web.Response:
    """get_tag_keys

    &lt;p&gt;Returns all tag keys currently in use in the specified Amazon Web Services Region for the calling account.&lt;/p&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    :param pagination_token: Pagination token
    :type pagination_token: str

    """
    body = GetTagKeysInput.from_dict(body)
    return web.Response(status=200)


async def get_tag_values(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, pagination_token=None) -> web.Response:
    """get_tag_values

    &lt;p&gt;Returns all tag values for the specified key that are used in the specified Amazon Web Services Region for the calling account.&lt;/p&gt; &lt;p&gt;This operation supports pagination, where the response can be sent in multiple pages. You should check the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter to determine if there are additional results available to return. Repeat the query, passing the &lt;code&gt;PaginationToken&lt;/code&gt; response parameter value as an input to the next request until you recieve a &lt;code&gt;null&lt;/code&gt; value. A null value for &lt;code&gt;PaginationToken&lt;/code&gt; indicates that there are no more results waiting to be returned.&lt;/p&gt;

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
    :param pagination_token: Pagination token
    :type pagination_token: str

    """
    body = GetTagValuesInput.from_dict(body)
    return web.Response(status=200)


async def start_report_creation(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """start_report_creation

    &lt;p&gt;Generates a report that lists all tagged resources in the accounts across your organization and tells whether each resource is compliant with the effective tag policy. Compliance data is refreshed daily. The report is generated asynchronously.&lt;/p&gt; &lt;p&gt;The generated report is saved to the following location:&lt;/p&gt; &lt;p&gt; &lt;code&gt;s3://example-bucket/AwsTagPolicies/o-exampleorgid/YYYY-MM-ddTHH:mm:ssZ/report.csv&lt;/code&gt; &lt;/p&gt; &lt;p&gt;You can call this operation only from the organization&#39;s management account and from the us-east-1 Region.&lt;/p&gt;

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
    body = StartReportCreationInput.from_dict(body)
    return web.Response(status=200)


async def tag_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resources

    &lt;p&gt;Applies one or more tags to the specified resources. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Not all resources can have tags. For a list of services with resources that support tagging using this operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html\&quot;&gt;Services that support the Resource Groups Tagging API&lt;/a&gt;. If the resource doesn&#39;t yet support this operation, the resource&#39;s service might support tagging using its own API operations. For more information, refer to the documentation for that service.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each resource can have up to 50 tags. For other limits, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions\&quot;&gt;Tag Naming and Usage Conventions&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference.&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can only tag resources that are located in the specified Amazon Web Services Region for the Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;In addition to the &lt;code&gt;tag:TagResources&lt;/code&gt; permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag an Amazon EC2 instance using the &lt;code&gt;TagResources&lt;/code&gt; operation, you must have both of the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:TagResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:CreateTags&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = TagResourcesInput.from_dict(body)
    return web.Response(status=200)


async def untag_resources(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resources

    &lt;p&gt;Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can only tag resources that are located in the specified Amazon Web Services Region for the calling Amazon Web Services account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Minimum permissions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;In addition to the &lt;code&gt;tag:UntagResources&lt;/code&gt; permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the &lt;code&gt;UntagResources&lt;/code&gt; operation, you must have both of the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;tag:UntagResource&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ec2:DeleteTags&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = UntagResourcesInput.from_dict(body)
    return web.Response(status=200)
