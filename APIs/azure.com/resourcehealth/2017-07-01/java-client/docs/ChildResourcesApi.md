# ChildResourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**childResourcesList**](ChildResourcesApi.md#childResourcesList) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/childResources |  |


<a id="childResourcesList"></a>
# **childResourcesList**
> AvailabilityStatusListResult childResourcesList(resourceUri, apiVersion, $filter, $expand)



Lists the all the children and its current health status for a parent resource. Use the nextLink property in the response to get the next page of children current health

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChildResourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ChildResourcesApi apiInstance = new ChildResourcesApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support not nested parent resource type: /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
    String $expand = "$expand_example"; // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
    try {
      AvailabilityStatusListResult result = apiInstance.childResourcesList(resourceUri, apiVersion, $filter, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChildResourcesApi#childResourcesList");
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
| **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support not nested parent resource type: /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} | |
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
| **200** | The body contains the list of the children&#39;s current availability statuses for a single resource which contains children |  -  |
| **0** | DefaultErrorResponse |  -  |

