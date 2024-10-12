from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancel_cluster_request import CancelClusterRequest
from openapi_server.models.cancel_job_request import CancelJobRequest
from openapi_server.models.create_address_request import CreateAddressRequest
from openapi_server.models.create_address_result import CreateAddressResult
from openapi_server.models.create_cluster_request import CreateClusterRequest
from openapi_server.models.create_cluster_result import CreateClusterResult
from openapi_server.models.create_job_request import CreateJobRequest
from openapi_server.models.create_job_result import CreateJobResult
from openapi_server.models.create_long_term_pricing_request import CreateLongTermPricingRequest
from openapi_server.models.create_long_term_pricing_result import CreateLongTermPricingResult
from openapi_server.models.create_return_shipping_label_request import CreateReturnShippingLabelRequest
from openapi_server.models.create_return_shipping_label_result import CreateReturnShippingLabelResult
from openapi_server.models.describe_address_request import DescribeAddressRequest
from openapi_server.models.describe_address_result import DescribeAddressResult
from openapi_server.models.describe_addresses_request import DescribeAddressesRequest
from openapi_server.models.describe_addresses_result import DescribeAddressesResult
from openapi_server.models.describe_cluster_request import DescribeClusterRequest
from openapi_server.models.describe_cluster_result import DescribeClusterResult
from openapi_server.models.describe_job_request import DescribeJobRequest
from openapi_server.models.describe_job_result import DescribeJobResult
from openapi_server.models.describe_return_shipping_label_request import DescribeReturnShippingLabelRequest
from openapi_server.models.describe_return_shipping_label_result import DescribeReturnShippingLabelResult
from openapi_server.models.get_job_manifest_request import GetJobManifestRequest
from openapi_server.models.get_job_manifest_result import GetJobManifestResult
from openapi_server.models.get_job_unlock_code_request import GetJobUnlockCodeRequest
from openapi_server.models.get_job_unlock_code_result import GetJobUnlockCodeResult
from openapi_server.models.get_snowball_usage_result import GetSnowballUsageResult
from openapi_server.models.get_software_updates_request import GetSoftwareUpdatesRequest
from openapi_server.models.get_software_updates_result import GetSoftwareUpdatesResult
from openapi_server.models.list_cluster_jobs_request import ListClusterJobsRequest
from openapi_server.models.list_cluster_jobs_result import ListClusterJobsResult
from openapi_server.models.list_clusters_request import ListClustersRequest
from openapi_server.models.list_clusters_result import ListClustersResult
from openapi_server.models.list_compatible_images_request import ListCompatibleImagesRequest
from openapi_server.models.list_compatible_images_result import ListCompatibleImagesResult
from openapi_server.models.list_jobs_request import ListJobsRequest
from openapi_server.models.list_jobs_result import ListJobsResult
from openapi_server.models.list_long_term_pricing_request import ListLongTermPricingRequest
from openapi_server.models.list_long_term_pricing_result import ListLongTermPricingResult
from openapi_server.models.list_pickup_locations_request import ListPickupLocationsRequest
from openapi_server.models.list_pickup_locations_result import ListPickupLocationsResult
from openapi_server.models.list_service_versions_request import ListServiceVersionsRequest
from openapi_server.models.list_service_versions_result import ListServiceVersionsResult
from openapi_server.models.update_cluster_request import UpdateClusterRequest
from openapi_server.models.update_job_request import UpdateJobRequest
from openapi_server.models.update_job_shipment_state_request import UpdateJobShipmentStateRequest
from openapi_server.models.update_long_term_pricing_request import UpdateLongTermPricingRequest
from openapi_server import util


async def cancel_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_cluster

    Cancels a cluster job. You can only cancel a cluster job while it&#39;s in the &lt;code&gt;AwaitingQuorum&lt;/code&gt; status. You&#39;ll have at least an hour after creating a cluster job to cancel it.

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
    body = CancelClusterRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """cancel_job

    Cancels the specified job. You can only cancel a job before its &lt;code&gt;JobState&lt;/code&gt; value changes to &lt;code&gt;PreparingAppliance&lt;/code&gt;. Requesting the &lt;code&gt;ListJobs&lt;/code&gt; or &lt;code&gt;DescribeJob&lt;/code&gt; action returns a job&#39;s &lt;code&gt;JobState&lt;/code&gt; as part of the response element data returned.

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
    body = CancelJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_address(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_address

    Creates an address for a Snow device to be shipped to. In most regions, addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.

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
    body = CreateAddressRequest.from_dict(body)
    return web.Response(status=200)


async def create_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_cluster

    Creates an empty cluster. Each cluster supports five nodes. You use the &lt;a&gt;CreateJob&lt;/a&gt; action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.

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
    body = CreateClusterRequest.from_dict(body)
    return web.Response(status=200)


async def create_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_job

    &lt;p&gt;Creates a job to import or export data between Amazon S3 and your on-premises data center. Your Amazon Web Services account must have the right trust policies and permissions in place to create a job for a Snow device. If you&#39;re creating a job for a node in a cluster, you only need to provide the &lt;code&gt;clusterId&lt;/code&gt; value; the other job attributes are inherited from the cluster. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the Snowball; Edge device type is supported when ordering clustered jobs.&lt;/p&gt; &lt;p&gt;The device capacity is optional.&lt;/p&gt; &lt;p&gt;Availability of device types differ by Amazon Web Services Region. For more information about Region availability, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p&#x3D;ngi&amp;amp;loc&#x3D;4\&quot;&gt;Amazon Web Services Regional Services&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Snow Family devices and their capacities.&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;SNC1_SSD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T14&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowcone &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;SNC1_HDD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowcone &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE_S&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T98&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Storage Optimized for data transfer only &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE_CG&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T42&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Compute Optimized with GPU&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE_C&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T42&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Compute Optimized without GPU&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T100&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Storage Optimized with EC2 Compute&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;This device is replaced with T98.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;STANDARD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T50&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Original Snowball device&lt;/p&gt; &lt;note&gt; &lt;p&gt;This device is only available in the Ningxia, Beijing, and Singapore Amazon Web Services Region &lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;STANDARD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T80&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Original Snowball device&lt;/p&gt; &lt;note&gt; &lt;p&gt;This device is only available in the Ningxia, Beijing, and Singapore Amazon Web Services Region. &lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Snow Family device type: &lt;b&gt;RACK_5U_C&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T13 &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowblade.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;V3_5S&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T240&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Storage Optimized 210TB&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

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
    body = CreateJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_long_term_pricing(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_long_term_pricing

    Creates a job with the long-term usage option for a device. The long-term usage is a 1-year or 3-year long-term pricing type for the device. You are billed upfront, and Amazon Web Services provides discounts for long-term pricing. 

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
    body = CreateLongTermPricingRequest.from_dict(body)
    return web.Response(status=200)


async def create_return_shipping_label(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_return_shipping_label

    Creates a shipping label that will be used to return the Snow device to Amazon Web Services.

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
    body = CreateReturnShippingLabelRequest.from_dict(body)
    return web.Response(status=200)


async def describe_address(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_address

    Takes an &lt;code&gt;AddressId&lt;/code&gt; and returns specific details about that address in the form of an &lt;code&gt;Address&lt;/code&gt; object.

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
    body = DescribeAddressRequest.from_dict(body)
    return web.Response(status=200)


async def describe_addresses(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """describe_addresses

    Returns a specified number of &lt;code&gt;ADDRESS&lt;/code&gt; objects. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.

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
    body = DescribeAddressesRequest.from_dict(body)
    return web.Response(status=200)


async def describe_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_cluster

    Returns information about a specific cluster including shipping information, cluster status, and other important metadata.

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
    body = DescribeClusterRequest.from_dict(body)
    return web.Response(status=200)


async def describe_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_job

    Returns information about a specific job including shipping information, job status, and other important metadata. 

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
    body = DescribeJobRequest.from_dict(body)
    return web.Response(status=200)


async def describe_return_shipping_label(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_return_shipping_label

    Information on the shipping label of a Snow device that is being returned to Amazon Web Services.

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
    body = DescribeReturnShippingLabelRequest.from_dict(body)
    return web.Response(status=200)


async def get_job_manifest(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_job_manifest

    &lt;p&gt;Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified &lt;code&gt;JobId&lt;/code&gt; value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you&#39;ll have to make another call to the &lt;code&gt;GetJobManifest&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;The manifest is an encrypted file that you can download after your job enters the &lt;code&gt;WithCustomer&lt;/code&gt; status. This is the only valid status for calling this API as the manifest and &lt;code&gt;UnlockCode&lt;/code&gt; code value are used for securing your device and should only be used when you have the device. The manifest is decrypted by using the &lt;code&gt;UnlockCode&lt;/code&gt; code value, when you pass both values to the Snow device through the Snowball client when the client is started for the first time. &lt;/p&gt; &lt;p&gt;As a best practice, we recommend that you don&#39;t save a copy of an &lt;code&gt;UnlockCode&lt;/code&gt; value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.&lt;/p&gt; &lt;p&gt;The credentials of a given job, including its manifest file and unlock code, expire 360 days after the job is created.&lt;/p&gt;

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
    body = GetJobManifestRequest.from_dict(body)
    return web.Response(status=200)


async def get_job_unlock_code(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_job_unlock_code

    &lt;p&gt;Returns the &lt;code&gt;UnlockCode&lt;/code&gt; code value for the specified job. A particular &lt;code&gt;UnlockCode&lt;/code&gt; value can be accessed for up to 360 days after the associated job has been created.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;UnlockCode&lt;/code&gt; value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snow device through the Snowball client when the client is started for the first time. The only valid status for calling this API is &lt;code&gt;WithCustomer&lt;/code&gt; as the manifest and &lt;code&gt;Unlock&lt;/code&gt; code values are used for securing your device and should only be used when you have the device.&lt;/p&gt; &lt;p&gt;As a best practice, we recommend that you don&#39;t save a copy of the &lt;code&gt;UnlockCode&lt;/code&gt; in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.&lt;/p&gt;

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
    body = GetJobUnlockCodeRequest.from_dict(body)
    return web.Response(status=200)


async def get_snowball_usage(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_snowball_usage

    &lt;p&gt;Returns information about the Snow Family service limit for your account, and also the number of Snow devices your account has in use.&lt;/p&gt; &lt;p&gt;The default service limit for the number of Snow devices that you can have at one time is 1. If you want to increase your service limit, contact Amazon Web Services Support.&lt;/p&gt;

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


async def get_software_updates(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_software_updates

    Returns an Amazon S3 presigned URL for an update file associated with a specified &lt;code&gt;JobId&lt;/code&gt;.

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
    body = GetSoftwareUpdatesRequest.from_dict(body)
    return web.Response(status=200)


async def list_cluster_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_cluster_jobs

    Returns an array of &lt;code&gt;JobListEntry&lt;/code&gt; objects of the specified length. Each &lt;code&gt;JobListEntry&lt;/code&gt; object is for a job in the specified cluster and contains a job&#39;s state, a job&#39;s ID, and other information.

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
    body = ListClusterJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_clusters(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_clusters

    Returns an array of &lt;code&gt;ClusterListEntry&lt;/code&gt; objects of the specified length. Each &lt;code&gt;ClusterListEntry&lt;/code&gt; object contains a cluster&#39;s state, a cluster&#39;s ID, and other important status information.

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
    body = ListClustersRequest.from_dict(body)
    return web.Response(status=200)


async def list_compatible_images(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_compatible_images

    This action returns a list of the different Amazon EC2-compatible Amazon Machine Images (AMIs) that are owned by your Amazon Web Services accountthat would be supported for use on a Snow device. Currently, supported AMIs are based on the Amazon Linux-2, Ubuntu 20.04 LTS - Focal, or Ubuntu 22.04 LTS - Jammy images, available on the Amazon Web Services Marketplace. Ubuntu 16.04 LTS - Xenial (HVM) images are no longer supported in the Market, but still supported for use on devices through Amazon EC2 VM Import/Export and running locally in AMIs.

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
    body = ListCompatibleImagesRequest.from_dict(body)
    return web.Response(status=200)


async def list_jobs(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_jobs

    Returns an array of &lt;code&gt;JobListEntry&lt;/code&gt; objects of the specified length. Each &lt;code&gt;JobListEntry&lt;/code&gt; object contains a job&#39;s state, a job&#39;s ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.

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
    body = ListJobsRequest.from_dict(body)
    return web.Response(status=200)


async def list_long_term_pricing(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_long_term_pricing

    Lists all long-term pricing types.

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
    body = ListLongTermPricingRequest.from_dict(body)
    return web.Response(status=200)


async def list_pickup_locations(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_pickup_locations

    A list of locations from which the customer can choose to pickup a device.

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
    body = ListPickupLocationsRequest.from_dict(body)
    return web.Response(status=200)


async def list_service_versions(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_service_versions

    Lists all supported versions for Snow on-device services. Returns an array of &lt;code&gt;ServiceVersion&lt;/code&gt; object containing the supported versions for a particular service.

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
    body = ListServiceVersionsRequest.from_dict(body)
    return web.Response(status=200)


async def update_cluster(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_cluster

    While a cluster&#39;s &lt;code&gt;ClusterState&lt;/code&gt; value is in the &lt;code&gt;AwaitingQuorum&lt;/code&gt; state, you can update some of the information associated with a cluster. Once the cluster changes to a different job state, usually 60 minutes after the cluster being created, this action is no longer available.

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
    body = UpdateClusterRequest.from_dict(body)
    return web.Response(status=200)


async def update_job(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_job

    While a job&#39;s &lt;code&gt;JobState&lt;/code&gt; value is &lt;code&gt;New&lt;/code&gt;, you can update some of the information associated with a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.

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
    body = UpdateJobRequest.from_dict(body)
    return web.Response(status=200)


async def update_job_shipment_state(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_job_shipment_state

    Updates the state when a shipment state changes to a different state.

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
    body = UpdateJobShipmentStateRequest.from_dict(body)
    return web.Response(status=200)


async def update_long_term_pricing(request: web.Request, x_amz_target, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_long_term_pricing

    Updates the long-term pricing type.

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
    body = UpdateLongTermPricingRequest.from_dict(body)
    return web.Response(status=200)
