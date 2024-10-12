# LocationUsageApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usageListByLocation**](LocationUsageApi.md#usageListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Storage/locations/{location}/usages |  |


<a id="usageListByLocation"></a>
# **usageListByLocation**
> UsageListResult usageListByLocation(apiVersion, subscriptionId, location)



Gets the current usage count and the limit for the resources of the location under the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationUsageApi apiInstance = new LocationUsageApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String location = "location_example"; // String | The location of the Azure Storage resource.
    try {
      UsageListResult result = apiInstance.usageListByLocation(apiVersion, subscriptionId, location);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationUsageApi#usageListByLocation");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **location** | **String**| The location of the Azure Storage resource. | |

### Return type

[**UsageListResult**](UsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- current usage count and limit retrieved and returned successfully. |  -  |

