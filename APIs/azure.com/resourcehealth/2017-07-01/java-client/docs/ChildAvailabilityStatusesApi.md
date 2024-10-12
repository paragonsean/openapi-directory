# ChildAvailabilityStatusesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**childAvailabilityStatusesGetByResource**](ChildAvailabilityStatusesApi.md#childAvailabilityStatusesGetByResource) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/childAvailabilityStatuses/current |  |
| [**childAvailabilityStatusesList**](ChildAvailabilityStatusesApi.md#childAvailabilityStatusesList) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/childAvailabilityStatuses |  |


<a id="childAvailabilityStatusesGetByResource"></a>
# **childAvailabilityStatusesGetByResource**
> AvailabilityStatus childAvailabilityStatusesGetByResource(resourceUri, apiVersion, $filter, $expand)



Gets current availability status for a single resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChildAvailabilityStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChildAvailabilityStatusesApi apiInstance = new ChildAvailabilityStatusesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatus result = apiInstance.childAvailabilityStatusesGetByResource(resourceUri, apiVersion, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChildAvailabilityStatusesApi#childAvailabilityStatusesGetByResource");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | |
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

<a id="childAvailabilityStatusesList"></a>
# **childAvailabilityStatusesList**
> AvailabilityStatusListResult childAvailabilityStatusesList(resourceUri, apiVersion, $filter, $expand)



Lists the historical availability statuses for a single child resource. Use the nextLink property in the response to get the next page of availability status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChildAvailabilityStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChildAvailabilityStatusesApi apiInstance = new ChildAvailabilityStatusesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatusListResult result = apiInstance.childAvailabilityStatusesList(resourceUri, apiVersion, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChildAvailabilityStatusesApi#childAvailabilityStatusesList");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | |
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
| **200** | The body contains the list of the historical availability statuses for a single child resource |  -  |
| **0** | DefaultErrorResponse |  -  |

