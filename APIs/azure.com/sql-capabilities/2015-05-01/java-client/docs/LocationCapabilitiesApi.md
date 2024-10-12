# LocationCapabilitiesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**capabilitiesListByLocation**](LocationCapabilitiesApi.md#capabilitiesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/capabilities |  |


<a id="capabilitiesListByLocation"></a>
# **capabilitiesListByLocation**
> LocationCapabilities capabilitiesListByLocation(locationName, subscriptionId, apiVersion)



Gets the subscription capabilities available for the specified location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationCapabilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    LocationCapabilitiesApi apiInstance = new LocationCapabilitiesApi(defaultClient);
    String locationName = "locationName_example"; // String | The location name whose capabilities are retrieved.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      LocationCapabilities result = apiInstance.capabilitiesListByLocation(locationName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationCapabilitiesApi#capabilitiesListByLocation");
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
| **locationName** | **String**| The location name whose capabilities are retrieved. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

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
| **200** | Successfully retrieved the subscription location capabilities. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidLocation - An invalid location was specified.   * 400 SubscriptionNotFound - The requested subscription was not found. |  -  |

