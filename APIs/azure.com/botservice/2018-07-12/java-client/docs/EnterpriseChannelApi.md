# EnterpriseChannelApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**enterpriseChannelsCheckNameAvailability**](EnterpriseChannelApi.md#enterpriseChannelsCheckNameAvailability) | **POST** /providers/Microsoft.BotService/checkEnterpriseChannelNameAvailability |  |
| [**enterpriseChannelsCreate**](EnterpriseChannelApi.md#enterpriseChannelsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} |  |
| [**enterpriseChannelsDelete**](EnterpriseChannelApi.md#enterpriseChannelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} |  |
| [**enterpriseChannelsGet**](EnterpriseChannelApi.md#enterpriseChannelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} |  |
| [**enterpriseChannelsListByResourceGroup**](EnterpriseChannelApi.md#enterpriseChannelsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels |  |
| [**enterpriseChannelsUpdate**](EnterpriseChannelApi.md#enterpriseChannelsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} |  |


<a id="enterpriseChannelsCheckNameAvailability"></a>
# **enterpriseChannelsCheckNameAvailability**
> EnterpriseChannelCheckNameAvailabilityResponse enterpriseChannelsCheckNameAvailability(apiVersion, parameters)



Check whether an Enterprise Channel name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EnterpriseChannelApi apiInstance = new EnterpriseChannelApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    EnterpriseChannelCheckNameAvailabilityRequest parameters = new EnterpriseChannelCheckNameAvailabilityRequest(); // EnterpriseChannelCheckNameAvailabilityRequest | The parameters to provide for the Enterprise Channel check name availability request.
    try {
      EnterpriseChannelCheckNameAvailabilityResponse result = apiInstance.enterpriseChannelsCheckNameAvailability(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseChannelApi#enterpriseChannelsCheckNameAvailability");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**EnterpriseChannelCheckNameAvailabilityRequest**](EnterpriseChannelCheckNameAvailabilityRequest.md)| The parameters to provide for the Enterprise Channel check name availability request. | |

### Return type

[**EnterpriseChannelCheckNameAvailabilityResponse**](EnterpriseChannelCheckNameAvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses. If a resource provider does not support paging, it should return the same body but leave nextLink empty for future compatibility. For a detailed explanation of each field in the response body, please refer to the request body description in the PUT resource section. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="enterpriseChannelsCreate"></a>
# **enterpriseChannelsCreate**
> EnterpriseChannel enterpriseChannelsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Creates an Enterprise Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EnterpriseChannelApi apiInstance = new EnterpriseChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    EnterpriseChannel parameters = new EnterpriseChannel(); // EnterpriseChannel | The parameters to provide for the new Enterprise Channel.
    try {
      EnterpriseChannel result = apiInstance.enterpriseChannelsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseChannelApi#enterpriseChannelsCreate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**EnterpriseChannel**](EnterpriseChannel.md)| The parameters to provide for the new Enterprise Channel. | |

### Return type

[**EnterpriseChannel**](EnterpriseChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created successfully or already existed, the service should return 200 (OK). |  -  |
| **201** | If resource is created successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="enterpriseChannelsDelete"></a>
# **enterpriseChannelsDelete**
> enterpriseChannelsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId)



Deletes an Enterprise Channel from the resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EnterpriseChannelApi apiInstance = new EnterpriseChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      apiInstance.enterpriseChannelsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseChannelApi#enterpriseChannelsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 (OK) should be returned if the object exists and was deleted successfully; |  -  |
| **204** | a 204 (NoContent) should be used if the resource does not exist and the request is well formed. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="enterpriseChannelsGet"></a>
# **enterpriseChannelsGet**
> EnterpriseChannel enterpriseChannelsGet(resourceGroupName, resourceName, apiVersion, subscriptionId)



Returns an Enterprise Channel specified by the parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EnterpriseChannelApi apiInstance = new EnterpriseChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      EnterpriseChannel result = apiInstance.enterpriseChannelsGet(resourceGroupName, resourceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseChannelApi#enterpriseChannelsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**EnterpriseChannel**](EnterpriseChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

<a id="enterpriseChannelsListByResourceGroup"></a>
# **enterpriseChannelsListByResourceGroup**
> EnterpriseChannelResponseList enterpriseChannelsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Returns all the resources of a particular type belonging to a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EnterpriseChannelApi apiInstance = new EnterpriseChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      EnterpriseChannelResponseList result = apiInstance.enterpriseChannelsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseChannelApi#enterpriseChannelsListByResourceGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**EnterpriseChannelResponseList**](EnterpriseChannelResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses here. If a resource provider does not support paging, it should return the same body (JSON object with “value” property) but omit nextLink entirely (or set to null, *not* empty string) for future compatibility. The nextLink should be implemented using following query parameters: · skipToken: opaque token that allows the resource provider to skip resources already enumerated. This value is defined and returned by the RP after first request via nextLink. · top: the optional client query parameter which defines the maximum number of records to be returned by the server. Implementation details: · NextLink may include all the query parameters (specifically OData $filter) used by the client in the first query.  · Server may return less records than requested with nextLink. Returning zero records with NextLink is an acceptable response.  Clients must fetch records until the nextLink is not returned back / null. Clients should never rely on number of returned records to determinate if pagination is completed. |  -  |
| **0** | Error response describing why the operation failed. If the resource group does not exist, 404 (NotFound) will be returned. |  -  |

<a id="enterpriseChannelsUpdate"></a>
# **enterpriseChannelsUpdate**
> EnterpriseChannel enterpriseChannelsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Updates an Enterprise Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnterpriseChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EnterpriseChannelApi apiInstance = new EnterpriseChannelApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    EnterpriseChannel parameters = new EnterpriseChannel(); // EnterpriseChannel | The parameters to provide to update the Enterprise Channel.
    try {
      EnterpriseChannel result = apiInstance.enterpriseChannelsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnterpriseChannelApi#enterpriseChannelsUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**EnterpriseChannel**](EnterpriseChannel.md)| The parameters to provide to update the Enterprise Channel. | |

### Return type

[**EnterpriseChannel**](EnterpriseChannel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created successfully or already existed, the service should return 200 (OK). |  -  |
| **201** | If resource is created successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed |  -  |

