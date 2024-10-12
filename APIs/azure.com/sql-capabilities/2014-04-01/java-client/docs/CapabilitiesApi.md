# CapabilitiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**capabilitiesListByLocation**](CapabilitiesApi.md#capabilitiesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationId}/capabilities |  |


<a id="capabilitiesListByLocation"></a>
# **capabilitiesListByLocation**
> LocationCapabilities capabilitiesListByLocation(apiVersion, subscriptionId, locationId)



Gets the capabilities available for the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    CapabilitiesApi apiInstance = new CapabilitiesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String locationId = "locationId_example"; // String | The location id whose capabilities are retrieved.
    try {
      LocationCapabilities result = apiInstance.capabilitiesListByLocation(apiVersion, subscriptionId, locationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapabilitiesApi#capabilitiesListByLocation");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **locationId** | **String**| The location id whose capabilities are retrieved. | |

### Return type

[**LocationCapabilities**](LocationCapabilities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

