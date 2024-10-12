from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.failed_property_batch_info import FailedPropertyBatchInfo
from openapi_server.models.name_description import NameDescription
from openapi_server.models.paged_property_info_list import PagedPropertyInfoList
from openapi_server.models.paged_sub_name_info_list import PagedSubNameInfoList
from openapi_server.models.property_batch_description_list import PropertyBatchDescriptionList
from openapi_server.models.property_description import PropertyDescription
from openapi_server.models.property_info import PropertyInfo
from openapi_server.models.successful_property_batch_info import SuccessfulPropertyBatchInfo
from openapi_server import util


async def create_name(request: web.Request, api_version, name_description, timeout=None) -> web.Response:
    """Creates a Service Fabric name.

    Creates the specified Service Fabric name.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_description: Describes the Service Fabric name to be created.
    :type name_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    name_description = NameDescription.from_dict(name_description)
    return web.Response(status=200)


async def delete_name(request: web.Request, api_version, name_id, timeout=None) -> web.Response:
    """Deletes a Service Fabric name.

    Deletes the specified Service Fabric name. A name must be created before it can be deleted. Deleting a name with child properties will fail.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def delete_property(request: web.Request, api_version, name_id, property_name, timeout=None) -> web.Response:
    """Deletes the specified Service Fabric property.

    Deletes the specified Service Fabric property under a given name. A property must be created before it can be deleted.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param property_name: Specifies the name of the property to get.
    :type property_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_name_exists_info(request: web.Request, api_version, name_id, timeout=None) -> web.Response:
    """Returns whether the Service Fabric name exists.

    Returns whether the specified Service Fabric name exists.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_property_info(request: web.Request, api_version, name_id, property_name, timeout=None) -> web.Response:
    """Gets the specified Service Fabric property.

    Gets the specified Service Fabric property under a given name. This will always return both value and metadata.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param property_name: Specifies the name of the property to get.
    :type property_name: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_property_info_list(request: web.Request, api_version, name_id, include_values=None, continuation_token=None, timeout=None) -> web.Response:
    """Gets information on all Service Fabric properties under a given name.

    Gets information on all Service Fabric properties under a given name.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param include_values: Allows specifying whether to include the values of the properties returned. True if values should be returned with the metadata; False to return only property metadata.
    :type include_values: bool
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def get_sub_name_info_list(request: web.Request, api_version, name_id, recursive=None, continuation_token=None, timeout=None) -> web.Response:
    """Enumerates all the Service Fabric names under a given name.

    Enumerates all the Service Fabric names under a given name. If the subnames do not fit in a page, one page of results is returned as well as a continuation token which can be used to get the next page. Querying a name that doesn&#39;t exist will fail.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param recursive: Allows specifying that the search performed should be recursive.
    :type recursive: bool
    :param continuation_token: The continuation token parameter is used to obtain next set of results. A continuation token with a non empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    :type continuation_token: str
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    return web.Response(status=200)


async def put_property(request: web.Request, api_version, name_id, property_description, timeout=None) -> web.Response:
    """Creates or updates a Service Fabric property.

    Creates or updates the specified Service Fabric property under a given name.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param property_description: Describes the Service Fabric property to be created.
    :type property_description: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    property_description = PropertyDescription.from_dict(property_description)
    return web.Response(status=200)


async def submit_property_batch(request: web.Request, api_version, name_id, property_batch_description_list, timeout=None) -> web.Response:
    """Submits a property batch.

    Submits a batch of property operations. Either all or none of the operations will be committed.

    :param api_version: The version of the API. This is a required parameter and it&#39;s value must be \&quot;6.0\&quot;.
    :type api_version: str
    :param name_id: The Service Fabric name, without the &#39;fabric:&#39; URI scheme.
    :type name_id: str
    :param property_batch_description_list: Describes the property batch operations to be submitted.
    :type property_batch_description_list: dict | bytes
    :param timeout: The server timeout for performing the operation in seconds. This specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    :type timeout: int

    """
    property_batch_description_list = PropertyBatchDescriptionList.from_dict(property_batch_description_list)
    return web.Response(status=200)
