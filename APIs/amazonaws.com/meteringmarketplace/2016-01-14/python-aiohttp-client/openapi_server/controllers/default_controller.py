from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_meter_usage_request import BatchMeterUsageRequest
from openapi_server.models.batch_meter_usage_result import BatchMeterUsageResult
from openapi_server.models.meter_usage_request import MeterUsageRequest
from openapi_server.models.meter_usage_result import MeterUsageResult
from openapi_server.models.register_usage_request import RegisterUsageRequest
from openapi_server.models.register_usage_result import RegisterUsageResult
from openapi_server.models.resolve_customer_request import ResolveCustomerRequest
from openapi_server.models.resolve_customer_result import ResolveCustomerResult
from openapi_server import util


async def batch_meter_usage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_meter_usage

    &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; is called from a SaaS application listed on AWS Marketplace to post metering records for a set of customers.&lt;/p&gt; &lt;p&gt;For identical requests, the API is idempotent; requests can be retried with the same records or a subset of the input records.&lt;/p&gt; &lt;p&gt;Every request to &lt;code&gt;BatchMeterUsage&lt;/code&gt; is for one product. If you need to meter usage for multiple products, you must make multiple calls to &lt;code&gt;BatchMeterUsage&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Usage records are expected to be submitted as quickly as possible after the event that is being recorded, and are not accepted more than 6 hours after the event.&lt;/p&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; can process up to 25 &lt;code&gt;UsageRecords&lt;/code&gt; at a time.&lt;/p&gt; &lt;p&gt;A &lt;code&gt;UsageRecord&lt;/code&gt; can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define (or allow the customer to define).&lt;/p&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; returns a list of &lt;code&gt;UsageRecordResult&lt;/code&gt; objects, showing the result for each &lt;code&gt;UsageRecord&lt;/code&gt;, as well as a list of &lt;code&gt;UnprocessedRecords&lt;/code&gt;, indicating errors in the service side that you should retry.&lt;/p&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; requests must be less than 1MB in size.&lt;/p&gt; &lt;note&gt; &lt;p&gt;For an example of using &lt;code&gt;BatchMeterUsage&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-example\&quot;&gt; BatchMeterUsage code example&lt;/a&gt; in the &lt;i&gt;AWS Marketplace Seller Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = BatchMeterUsageRequest.from_dict(body)
    return web.Response(status=200)


async def meter_usage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """meter_usage

    &lt;p&gt;API to emit metering records. For identical requests, the API is idempotent. It simply returns the metering record ID.&lt;/p&gt; &lt;p&gt; &lt;code&gt;MeterUsage&lt;/code&gt; is authenticated on the buyer&#39;s AWS account using credentials from the EC2 instance, ECS task, or EKS pod.&lt;/p&gt; &lt;p&gt; &lt;code&gt;MeterUsage&lt;/code&gt; can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define (or allow the customer to define).&lt;/p&gt; &lt;p&gt;Usage records are expected to be submitted as quickly as possible after the event that is being recorded, and are not accepted more than 6 hours after the event.&lt;/p&gt;

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
    body = MeterUsageRequest.from_dict(body)
    return web.Response(status=200)


async def register_usage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_usage

    &lt;p&gt;Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the &lt;code&gt;RegisterUsage&lt;/code&gt; operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren&#39;t required to call &lt;code&gt;RegisterUsage&lt;/code&gt;, but you may choose to do so if you would like to receive usage data in your seller reports. The sections below explain the behavior of &lt;code&gt;RegisterUsage&lt;/code&gt;. &lt;code&gt;RegisterUsage&lt;/code&gt; performs two primary functions: metering and entitlement.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Entitlement&lt;/i&gt;: &lt;code&gt;RegisterUsage&lt;/code&gt; allows you to verify that the customer running your paid software is subscribed to your product on AWS Marketplace, enabling you to guard against unauthorized use. Your container image that integrates with &lt;code&gt;RegisterUsage&lt;/code&gt; is only required to guard against unauthorized use at container startup, as such a &lt;code&gt;CustomerNotSubscribedException&lt;/code&gt; or &lt;code&gt;PlatformNotSupportedException&lt;/code&gt; will only be thrown on the initial call to &lt;code&gt;RegisterUsage&lt;/code&gt;. Subsequent calls from the same Amazon ECS task instance (e.g. task-id) or Amazon EKS pod will not throw a &lt;code&gt;CustomerNotSubscribedException&lt;/code&gt;, even if the customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Metering&lt;/i&gt;: &lt;code&gt;RegisterUsage&lt;/code&gt; meters software use per ECS task, per hour, or per pod for Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will launch a task on all 10 cluster nodes and the customer will be charged: (10 * hourly_rate). Metering for software use is automatically handled by the AWS Marketplace Metering Control Plane -- your software is not required to perform any metering specific actions, other than call &lt;code&gt;RegisterUsage&lt;/code&gt; once for metering of software use to commence. The AWS Marketplace Metering Control Plane will also continue to bill customers for running ECS tasks and Amazon EKS pods, regardless of the customers subscription state, removing the need for your software to perform entitlement checks at runtime.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = RegisterUsageRequest.from_dict(body)
    return web.Response(status=200)


async def resolve_customer(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """resolve_customer

    &lt;p&gt; &lt;code&gt;ResolveCustomer&lt;/code&gt; is called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a registration token through their browser. The registration token is resolved through this API to obtain a &lt;code&gt;CustomerIdentifier&lt;/code&gt; along with the &lt;code&gt;CustomerAWSAccountId&lt;/code&gt; and &lt;code&gt;ProductCode&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The API needs to called from the seller account id used to publish the SaaS application to successfully resolve the token.&lt;/p&gt; &lt;p&gt;For an example of using &lt;code&gt;ResolveCustomer&lt;/code&gt;, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-resolvecustomer-example\&quot;&gt; ResolveCustomer code example&lt;/a&gt; in the &lt;i&gt;AWS Marketplace Seller Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

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
    body = ResolveCustomerRequest.from_dict(body)
    return web.Response(status=200)
