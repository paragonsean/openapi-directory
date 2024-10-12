from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_publish_response import BulkPublishResponse
from openapi_server.models.delete_dataset_response import DeleteDatasetResponse
from openapi_server.models.describe_dataset_response import DescribeDatasetResponse
from openapi_server.models.describe_identity_pool_usage_response import DescribeIdentityPoolUsageResponse
from openapi_server.models.describe_identity_usage_response import DescribeIdentityUsageResponse
from openapi_server.models.get_bulk_publish_details_response import GetBulkPublishDetailsResponse
from openapi_server.models.get_cognito_events_response import GetCognitoEventsResponse
from openapi_server.models.get_identity_pool_configuration_response import GetIdentityPoolConfigurationResponse
from openapi_server.models.list_datasets_response import ListDatasetsResponse
from openapi_server.models.list_identity_pool_usage_response import ListIdentityPoolUsageResponse
from openapi_server.models.list_records_response import ListRecordsResponse
from openapi_server.models.register_device_request import RegisterDeviceRequest
from openapi_server.models.register_device_response import RegisterDeviceResponse
from openapi_server.models.set_cognito_events_request import SetCognitoEventsRequest
from openapi_server.models.set_identity_pool_configuration_request import SetIdentityPoolConfigurationRequest
from openapi_server.models.set_identity_pool_configuration_response import SetIdentityPoolConfigurationResponse
from openapi_server.models.update_records_request import UpdateRecordsRequest
from openapi_server.models.update_records_response import UpdateRecordsResponse
from openapi_server import util


async def bulk_publish(request: web.Request, identity_pool_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """bulk_publish

    &lt;p&gt;Initiates a bulk publish of all existing datasets for an Identity Pool to the configured stream. Customers are limited to one successful bulk publish per 24 hours. Bulk publish is an asynchronous request, customers can see the status of the request via the GetBulkPublishDetails operation.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def delete_dataset(request: web.Request, identity_pool_id, identity_id, dataset_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_dataset

    &lt;p&gt;Deletes the specific dataset. The dataset will be deleted permanently, and the action can&#39;t be undone. Datasets that this dataset was merged with will no longer report the merge. Any subsequent operation on this dataset will result in a ResourceNotFoundException.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_id: str
    :param dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot).
    :type dataset_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_dataset(request: web.Request, identity_pool_id, identity_id, dataset_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_dataset

    &lt;p&gt;Gets meta data about a dataset by identity and dataset name. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_id: str
    :param dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot).
    :type dataset_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_identity_pool_usage(request: web.Request, identity_pool_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_identity_pool_usage

    &lt;p&gt;Gets usage details (for example, data storage) about a particular identity pool.&lt;/p&gt; &lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def describe_identity_usage(request: web.Request, identity_pool_id, identity_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_identity_usage

    &lt;p&gt;Gets usage information for an identity, including number of datasets and data usage.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_bulk_publish_details(request: web.Request, identity_pool_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_bulk_publish_details

    &lt;p&gt;Get the status of the last BulkPublish operation for an identity pool.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_cognito_events(request: web.Request, identity_pool_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_cognito_events

    &lt;p&gt;Gets the events and the corresponding Lambda functions associated with an identity pool.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: The Cognito Identity Pool ID for the request
    :type identity_pool_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def get_identity_pool_configuration(request: web.Request, identity_pool_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_identity_pool_configuration

    &lt;p&gt;Gets the configuration settings of an identity pool.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool for which to return a configuration.
    :type identity_pool_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def list_datasets(request: web.Request, identity_pool_id, identity_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_datasets

    &lt;p&gt;Lists datasets for an identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.&lt;/p&gt; &lt;p&gt;ListDatasets can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use the Cognito Identity credentials to make this API call.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for obtaining the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to be returned.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_identity_pool_usage(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_identity_pool_usage

    &lt;p&gt;Gets a list of identity pools registered with Cognito.&lt;/p&gt; &lt;p&gt;ListIdentityPoolUsage can only be called with developer credentials. You cannot make this API call with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: A pagination token for obtaining the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to be returned.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_records(request: web.Request, identity_pool_id, identity_id, dataset_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, last_sync_count=None, next_token=None, max_results=None, sync_session_token=None) -> web.Response:
    """list_records

    &lt;p&gt;Gets paginated records, optionally changed after a particular sync count for a dataset and identity. With Amazon Cognito Sync, each identity has access only to its own data. Thus, the credentials used to make this API call need to have access to the identity data.&lt;/p&gt; &lt;p&gt;ListRecords can be called with temporary user credentials provided by Cognito Identity or with developer credentials. You should use Cognito Identity credentials to make this API call.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_id: str
    :param dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot).
    :type dataset_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param last_sync_count: The last server sync count for this record.
    :type last_sync_count: int
    :param next_token: A pagination token for obtaining the next page of results.
    :type next_token: str
    :param max_results: The maximum number of results to be returned.
    :type max_results: int
    :param sync_session_token: A token containing a session ID, identity ID, and expiration.
    :type sync_session_token: str

    """
    return web.Response(status=200)


async def register_device(request: web.Request, identity_pool_id, identity_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """register_device

    &lt;p&gt;Registers a device to receive push sync notifications.&lt;/p&gt;&lt;p&gt;This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. Here, the ID of the pool that the identity belongs to.
    :type identity_pool_id: str
    :param identity_id: The unique ID for this identity.
    :type identity_id: str
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
    body = RegisterDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def set_cognito_events(request: web.Request, identity_pool_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_cognito_events

    &lt;p&gt;Sets the AWS Lambda function for a given event type for an identity pool. This request only updates the key/value pair specified. Other key/values pairs are not updated. To remove a key value pair, pass a empty value for the particular key.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: The Cognito Identity Pool to use when configuring Cognito Events
    :type identity_pool_id: str
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
    body = SetCognitoEventsRequest.from_dict(body)
    return web.Response(status=200)


async def set_identity_pool_configuration(request: web.Request, identity_pool_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """set_identity_pool_configuration

    &lt;p&gt;Sets the necessary configuration for push sync.&lt;/p&gt;&lt;p&gt;This API can only be called with developer credentials. You cannot call this API with the temporary user credentials provided by Cognito Identity.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. This is the ID of the pool to modify.
    :type identity_pool_id: str
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
    body = SetIdentityPoolConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def subscribe_to_dataset(request: web.Request, identity_pool_id, identity_id, dataset_name, device_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """subscribe_to_dataset

    &lt;p&gt;Subscribes to receive notifications when a dataset is modified by another device.&lt;/p&gt;&lt;p&gt;This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which the identity belongs.
    :type identity_pool_id: str
    :param identity_id: Unique ID for this identity.
    :type identity_id: str
    :param dataset_name: The name of the dataset to subcribe to.
    :type dataset_name: str
    :param device_id: The unique ID generated for this device by Cognito.
    :type device_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def unsubscribe_from_dataset(request: web.Request, identity_pool_id, identity_id, dataset_name, device_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """unsubscribe_from_dataset

    &lt;p&gt;Unsubscribes from receiving notifications when a dataset is modified by another device.&lt;/p&gt;&lt;p&gt;This API can only be called with temporary credentials provided by Cognito Identity. You cannot call this API with developer credentials.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. The ID of the pool to which this identity belongs.
    :type identity_pool_id: str
    :param identity_id: Unique ID for this identity.
    :type identity_id: str
    :param dataset_name: The name of the dataset from which to unsubcribe.
    :type dataset_name: str
    :param device_id: The unique ID generated for this device by Cognito.
    :type device_id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
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


async def update_records(request: web.Request, identity_pool_id, identity_id, dataset_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, x_amz_client_context=None) -> web.Response:
    """update_records

    &lt;p&gt;Posts updates to records and adds and deletes records for a dataset and user.&lt;/p&gt; &lt;p&gt;The sync count in the record patch is your last known sync count for that record. The server will reject an UpdateRecords request with a ResourceConflictException if you try to patch a record with a new value but a stale sync count.&lt;/p&gt;&lt;p&gt;For example, if the sync count on the server is 5 for a key called highScore and you try and submit a new highScore with sync count of 4, the request will be rejected. To obtain the current sync count for a record, call ListRecords. On a successful update of the record, the response returns the new sync count for that record. You should present that sync count the next time you try to update that same record. When the record does not exist, specify the sync count as 0.&lt;/p&gt; &lt;p&gt;This API can be called with temporary user credentials provided by Cognito Identity or with developer credentials.&lt;/p&gt;

    :param identity_pool_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_pool_id: str
    :param identity_id: A name-spaced GUID (for example, us-east-1:23EC4050-6AEA-7089-A2DD-08002EXAMPLE) created by Amazon Cognito. GUID generation is unique within a region.
    :type identity_id: str
    :param dataset_name: A string of up to 128 characters. Allowed characters are a-z, A-Z, 0-9, &#39;_&#39; (underscore), &#39;-&#39; (dash), and &#39;.&#39; (dot).
    :type dataset_name: str
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
    :param x_amz_client_context: Intended to supply a device ID that will populate the lastModifiedBy field referenced in other methods. The ClientContext field is not yet implemented.
    :type x_amz_client_context: str

    """
    body = UpdateRecordsRequest.from_dict(body)
    return web.Response(status=200)
