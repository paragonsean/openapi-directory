# RegionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationGetCapabilities**](RegionsApi.md#locationGetCapabilities) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HDInsight/locations/{location}/capabilities |  |


<a id="locationGetCapabilities"></a>
# **locationGetCapabilities**
> CapabilitiesResult locationGetCapabilities(location, apiVersion, subscriptionId)



Gets the capabilities for the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegionsApi apiInstance = new RegionsApi(defaultClient);
    String location = "location_example"; // String | The location to get capabilities for.
    String apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      CapabilitiesResult result = apiInstance.locationGetCapabilities(location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegionsApi#locationGetCapabilities");
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
| **location** | **String**| The location to get capabilities for. | |
| **apiVersion** | **String**| The HDInsight client API Version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**CapabilitiesResult**](CapabilitiesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

