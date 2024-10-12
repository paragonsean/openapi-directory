# AvailabilityStatusesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**availabilityStatusesGetByResource**](AvailabilityStatusesApi.md#availabilityStatusesGetByResource) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/availabilityStatuses/current |  |
| [**availabilityStatusesList**](AvailabilityStatusesApi.md#availabilityStatusesList) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/availabilityStatuses |  |
| [**availabilityStatusesListByResourceGroup**](AvailabilityStatusesApi.md#availabilityStatusesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ResourceHealth/availabilityStatuses |  |
| [**availabilityStatusesListBySubscriptionId**](AvailabilityStatusesApi.md#availabilityStatusesListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/availabilityStatuses |  |


<a id="availabilityStatusesGetByResource"></a>
# **availabilityStatusesGetByResource**
> AvailabilityStatus availabilityStatusesGetByResource(resourceUri, apiVersion, $filter, $expand)



Gets current availability status for a single resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityStatusesApi apiInstance = new AvailabilityStatusesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatus result = apiInstance.availabilityStatusesGetByResource(resourceUri, apiVersion, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityStatusesApi#availabilityStatusesGetByResource");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |
| **$expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] |

### Return type

[**AvailabilityStatus**](AvailabilityStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the current availability status for a single resource |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="availabilityStatusesList"></a>
# **availabilityStatusesList**
> AvailabilityStatusListResult availabilityStatusesList(resourceUri, apiVersion, $filter, $expand)



Lists all historical availability transitions and impacting events for a single resource. Use the nextLink property in the response to get the next page of availability status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityStatusesApi apiInstance = new AvailabilityStatusesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatusListResult result = apiInstance.availabilityStatusesList(resourceUri, apiVersion, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityStatusesApi#availabilityStatusesList");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |
| **$expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] |

### Return type

[**AvailabilityStatusListResult**](AvailabilityStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the list of the historical availability statuses for a single resource |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="availabilityStatusesListByResourceGroup"></a>
# **availabilityStatusesListByResourceGroup**
> AvailabilityStatusListResult availabilityStatusesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $expand)



Lists the current availability status for all the resources in the resource group. Use the nextLink property in the response to get the next page of availability statuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityStatusesApi apiInstance = new AvailabilityStatusesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatusListResult result = apiInstance.availabilityStatusesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityStatusesApi#availabilityStatusesListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |
| **$expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] |

### Return type

[**AvailabilityStatusListResult**](AvailabilityStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the list of the current availability status for all the resources in the resource group |  -  |
| **0** | DefaultErrorResponse |  -  |

<a id="availabilityStatusesListBySubscriptionId"></a>
# **availabilityStatusesListBySubscriptionId**
> AvailabilityStatusListResult availabilityStatusesListBySubscriptionId(apiVersion, subscriptionId, $filter, $expand)



Lists the current availability status for all the resources in the subscription. Use the nextLink property in the response to get the next page of availability statuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityStatusesApi apiInstance = new AvailabilityStatusesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatusListResult result = apiInstance.availabilityStatusesListBySubscriptionId(apiVersion, subscriptionId, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityStatusesApi#availabilityStatusesListBySubscriptionId");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] |
| **$expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] |

### Return type

[**AvailabilityStatusListResult**](AvailabilityStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The body contains the list of the current availability status for all the resources in the subscription |  -  |
| **0** | DefaultErrorResponse |  -  |

