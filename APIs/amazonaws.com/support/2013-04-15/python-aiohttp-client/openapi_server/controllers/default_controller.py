from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_attachments_to_set_request import AddAttachmentsToSetRequest
from openapi_server.models.add_attachments_to_set_response import AddAttachmentsToSetResponse
from openapi_server.models.add_communication_to_case_request import AddCommunicationToCaseRequest
from openapi_server.models.add_communication_to_case_response import AddCommunicationToCaseResponse
from openapi_server.models.create_case_request import CreateCaseRequest
from openapi_server.models.create_case_response import CreateCaseResponse
from openapi_server.models.describe_attachment_request import DescribeAttachmentRequest
from openapi_server.models.describe_attachment_response import DescribeAttachmentResponse
from openapi_server.models.describe_cases_request import DescribeCasesRequest
from openapi_server.models.describe_cases_response import DescribeCasesResponse
from openapi_server.models.describe_communications_request import DescribeCommunicationsRequest
from openapi_server.models.describe_communications_response import DescribeCommunicationsResponse
from openapi_server.models.describe_create_case_options_request import DescribeCreateCaseOptionsRequest
from openapi_server.models.describe_create_case_options_response import DescribeCreateCaseOptionsResponse
from openapi_server.models.describe_services_request import DescribeServicesRequest
from openapi_server.models.describe_services_response import DescribeServicesResponse
from openapi_server.models.describe_severity_levels_request import DescribeSeverityLevelsRequest
from openapi_server.models.describe_severity_levels_response import DescribeSeverityLevelsResponse
from openapi_server.models.describe_supported_languages_request import DescribeSupportedLanguagesRequest
from openapi_server.models.describe_supported_languages_response import DescribeSupportedLanguagesResponse
from openapi_server.models.describe_trusted_advisor_check_refresh_statuses_request import DescribeTrustedAdvisorCheckRefreshStatusesRequest
from openapi_server.models.describe_trusted_advisor_check_refresh_statuses_response import DescribeTrustedAdvisorCheckRefreshStatusesResponse
from openapi_server.models.describe_trusted_advisor_check_result_request import DescribeTrustedAdvisorCheckResultRequest
from openapi_server.models.describe_trusted_advisor_check_result_response import DescribeTrustedAdvisorCheckResultResponse
from openapi_server.models.describe_trusted_advisor_check_summaries_request import DescribeTrustedAdvisorCheckSummariesRequest
from openapi_server.models.describe_trusted_advisor_check_summaries_response import DescribeTrustedAdvisorCheckSummariesResponse
from openapi_server.models.describe_trusted_advisor_checks_request import DescribeTrustedAdvisorChecksRequest
from openapi_server.models.describe_trusted_advisor_checks_response import DescribeTrustedAdvisorChecksResponse
from openapi_server.models.refresh_trusted_advisor_check_request import RefreshTrustedAdvisorCheckRequest
from openapi_server.models.refresh_trusted_advisor_check_response import RefreshTrustedAdvisorCheckResponse
from openapi_server.models.resolve_case_request import ResolveCaseRequest
from openapi_server.models.resolve_case_response import ResolveCaseResponse
from openapi_server import util


async def add_attachments_to_set(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_attachments_to_set

    &lt;p&gt;Adds one or more attachments to an attachment set. &lt;/p&gt; &lt;p&gt;An attachment set is a temporary container for attachments that you add to a case or case communication. The set is available for 1 hour after it&#39;s created. The &lt;code&gt;expiryTime&lt;/code&gt; returned in the response is when the set expires. &lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AddAttachmentsToSetRequest.from_dict(body)
    return web.Response(status=200)


async def add_communication_to_case(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """add_communication_to_case

    &lt;p&gt;Adds additional customer communication to an Amazon Web Services Support case. Use the &lt;code&gt;caseId&lt;/code&gt; parameter to identify the case to which to add communication. You can list a set of email addresses to copy on the communication by using the &lt;code&gt;ccEmailAddresses&lt;/code&gt; parameter. The &lt;code&gt;communicationBody&lt;/code&gt; value contains the text of the communication.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = AddCommunicationToCaseRequest.from_dict(body)
    return web.Response(status=200)


async def create_case(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_case

    &lt;p&gt;Creates a case in the Amazon Web Services Support Center. This operation is similar to how you create a case in the Amazon Web Services Support Center &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create\&quot;&gt;Create Case&lt;/a&gt; page.&lt;/p&gt; &lt;p&gt;The Amazon Web Services Support API doesn&#39;t support requesting service limit increases. You can submit a service limit increase in the following ways: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Submit a request from the Amazon Web Services Support Center &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create\&quot;&gt;Create Case&lt;/a&gt; page.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the Service Quotas &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/API_RequestServiceQuotaIncrease.html\&quot;&gt;RequestServiceQuotaIncrease&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;A successful &lt;code&gt;CreateCase&lt;/code&gt; request returns an Amazon Web Services Support case number. You can use the &lt;a&gt;DescribeCases&lt;/a&gt; operation and specify the case number to get existing Amazon Web Services Support cases. After you create a case, use the &lt;a&gt;AddCommunicationToCase&lt;/a&gt; operation to add additional communication or attachments to an existing case.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;caseId&lt;/code&gt; is separate from the &lt;code&gt;displayId&lt;/code&gt; that appears in the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support\&quot;&gt;Amazon Web Services Support Center&lt;/a&gt;. Use the &lt;a&gt;DescribeCases&lt;/a&gt; operation to get the &lt;code&gt;displayId&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = CreateCaseRequest.from_dict(body)
    return web.Response(status=200)


async def describe_attachment(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_attachment

    &lt;p&gt;Returns the attachment that has the specified ID. Attachments can include screenshots, error logs, or other files that describe your issue. Attachment IDs are generated by the case management system when you add an attachment to a case or case communication. Attachment IDs are returned in the &lt;a&gt;AttachmentDetails&lt;/a&gt; objects that are returned by the &lt;a&gt;DescribeCommunications&lt;/a&gt; operation.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeAttachmentRequest.from_dict(body)
    return web.Response(status=200)


async def describe_cases(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_cases

    &lt;p&gt;Returns a list of cases that you specify by passing one or more case IDs. You can use the &lt;code&gt;afterTime&lt;/code&gt; and &lt;code&gt;beforeTime&lt;/code&gt; parameters to filter the cases by date. You can set values for the &lt;code&gt;includeResolvedCases&lt;/code&gt; and &lt;code&gt;includeCommunications&lt;/code&gt; parameters to specify how much information to return.&lt;/p&gt; &lt;p&gt;The response returns the following in JSON format:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;One or more &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CaseDetails.html\&quot;&gt;CaseDetails&lt;/a&gt; data types.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;One or more &lt;code&gt;nextToken&lt;/code&gt; values, which specify where to paginate the returned records represented by the &lt;code&gt;CaseDetails&lt;/code&gt; objects.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request might return an error.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeCasesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_communications(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_communications

    &lt;p&gt;Returns communications and attachments for one or more support cases. Use the &lt;code&gt;afterTime&lt;/code&gt; and &lt;code&gt;beforeTime&lt;/code&gt; parameters to filter by date. You can use the &lt;code&gt;caseId&lt;/code&gt; parameter to restrict the results to a specific case.&lt;/p&gt; &lt;p&gt;Case data is available for 12 months after creation. If a case was created more than 12 months ago, a request for data might cause an error.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;maxResults&lt;/code&gt; and &lt;code&gt;nextToken&lt;/code&gt; parameters to control the pagination of the results. Set &lt;code&gt;maxResults&lt;/code&gt; to the number of cases that you want to display on each page, and use &lt;code&gt;nextToken&lt;/code&gt; to specify the resumption of pagination.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeCommunicationsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_create_case_options(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_create_case_options

    &lt;p&gt;Returns a list of CreateCaseOption types along with the corresponding supported hours and language availability. You can specify the &lt;code&gt;language&lt;/code&gt; &lt;code&gt;categoryCode&lt;/code&gt;, &lt;code&gt;issueType&lt;/code&gt; and &lt;code&gt;serviceCode&lt;/code&gt; used to retrieve the CreateCaseOptions.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeCreateCaseOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_services(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_services

    &lt;p&gt;Returns the current list of Amazon Web Services services and a list of service categories for each service. You then use service names and categories in your &lt;a&gt;CreateCase&lt;/a&gt; requests. Each Amazon Web Services service has its own set of categories.&lt;/p&gt; &lt;p&gt;The service codes and category codes correspond to the values that appear in the &lt;b&gt;Service&lt;/b&gt; and &lt;b&gt;Category&lt;/b&gt; lists on the Amazon Web Services Support Center &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home#/case/create\&quot;&gt;Create Case&lt;/a&gt; page. The values in those fields don&#39;t necessarily match the service codes and categories returned by the &lt;code&gt;DescribeServices&lt;/code&gt; operation. Always use the service codes and categories that the &lt;code&gt;DescribeServices&lt;/code&gt; operation returns, so that you have the most recent set of service and category codes.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeServicesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_severity_levels(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_severity_levels

    &lt;p&gt;Returns the list of severity levels that you can assign to a support case. The severity level for a case is also a field in the &lt;a&gt;CaseDetails&lt;/a&gt; data type that you include for a &lt;a&gt;CreateCase&lt;/a&gt; request.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeSeverityLevelsRequest.from_dict(body)
    return web.Response(status=200)


async def describe_supported_languages(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_supported_languages

    &lt;p&gt;Returns a list of supported languages for a specified &lt;code&gt;categoryCode&lt;/code&gt;, &lt;code&gt;issueType&lt;/code&gt; and &lt;code&gt;serviceCode&lt;/code&gt;. The returned supported languages will include a ISO 639-1 code for the &lt;code&gt;language&lt;/code&gt;, and the language display name.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = DescribeSupportedLanguagesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_trusted_advisor_check_refresh_statuses(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_trusted_advisor_check_refresh_statuses

    &lt;p&gt;Returns the refresh status of the Trusted Advisor checks that have the specified check IDs. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;Some checks are refreshed automatically, and you can&#39;t return their refresh statuses by using the &lt;code&gt;DescribeTrustedAdvisorCheckRefreshStatuses&lt;/code&gt; operation. If you call this operation for these checks, you might see an &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeTrustedAdvisorCheckRefreshStatusesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_trusted_advisor_check_result(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_trusted_advisor_check_result

    &lt;p&gt;Returns the results of the Trusted Advisor check that has the specified check ID. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;The response contains a &lt;a&gt;TrustedAdvisorCheckResult&lt;/a&gt; object, which contains these three objects:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TrustedAdvisorCategorySpecificSummary&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TrustedAdvisorResourceDetail&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;TrustedAdvisorResourcesSummary&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In addition, the response contains these fields:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;status&lt;/b&gt; - The alert status of the check can be &lt;code&gt;ok&lt;/code&gt; (green), &lt;code&gt;warning&lt;/code&gt; (yellow), &lt;code&gt;error&lt;/code&gt; (red), or &lt;code&gt;not_available&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;timestamp&lt;/b&gt; - The time of the last refresh of the check.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;checkId&lt;/b&gt; - The unique identifier for the check.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeTrustedAdvisorCheckResultRequest.from_dict(body)
    return web.Response(status=200)


async def describe_trusted_advisor_check_summaries(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_trusted_advisor_check_summaries

    &lt;p&gt;Returns the results for the Trusted Advisor check summaries for the check IDs that you specified. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;The response contains an array of &lt;a&gt;TrustedAdvisorCheckSummary&lt;/a&gt; objects.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeTrustedAdvisorCheckSummariesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_trusted_advisor_checks(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_trusted_advisor_checks

    &lt;p&gt;Returns information about all available Trusted Advisor checks, including the name, ID, category, description, and metadata. You must specify a language code.&lt;/p&gt; &lt;p&gt;The response contains a &lt;a&gt;TrustedAdvisorCheckDescription&lt;/a&gt; object for each check. You must set the Amazon Web Services Region to us-east-1.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The names and descriptions for Trusted Advisor checks are subject to change. We recommend that you specify the check ID in your code to uniquely identify a check.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = DescribeTrustedAdvisorChecksRequest.from_dict(body)
    return web.Response(status=200)


async def refresh_trusted_advisor_check(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """refresh_trusted_advisor_check

    &lt;p&gt;Refreshes the Trusted Advisor check that you specify using the check ID. You can get the check IDs by calling the &lt;a&gt;DescribeTrustedAdvisorChecks&lt;/a&gt; operation.&lt;/p&gt; &lt;p&gt;Some checks are refreshed automatically. If you call the &lt;code&gt;RefreshTrustedAdvisorCheck&lt;/code&gt; operation to refresh them, you might see the &lt;code&gt;InvalidParameterValue&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;The response contains a &lt;a&gt;TrustedAdvisorCheckRefreshStatus&lt;/a&gt; object.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints don&#39;t support the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;

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
    body = RefreshTrustedAdvisorCheckRequest.from_dict(body)
    return web.Response(status=200)


async def resolve_case(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resolve_case

    &lt;p&gt;Resolves a support case. This operation takes a &lt;code&gt;caseId&lt;/code&gt; and returns the initial and final state of the case.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

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
    body = ResolveCaseRequest.from_dict(body)
    return web.Response(status=200)
