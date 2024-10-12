# ExpressRoutePortsLocationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expressRoutePortsLocationsGet**](ExpressRoutePortsLocationsApi.md#expressRoutePortsLocationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePortsLocations/{locationName} |  |
| [**expressRoutePortsLocationsList**](ExpressRoutePortsLocationsApi.md#expressRoutePortsLocationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePortsLocations |  |


<a id="expressRoutePortsLocationsGet"></a>
# **expressRoutePortsLocationsGet**
> ExpressRoutePortsLocation expressRoutePortsLocationsGet(subscriptionId, apiVersion, locationName)



Retrieves a single ExpressRoutePort peering location, including the list of available bandwidths available at said peering location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsLocationsApi apiInstance = new ExpressRoutePortsLocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String locationName = "locationName_example"; // String | Name of the requested ExpressRoutePort peering location.
    try {
      ExpressRoutePortsLocation result = apiInstance.expressRoutePortsLocationsGet(subscriptionId, apiVersion, locationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsLocationsApi#expressRoutePortsLocationsGet");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **locationName** | **String**| Name of the requested ExpressRoutePort peering location. | |

### Return type

[**ExpressRoutePortsLocation**](ExpressRoutePortsLocation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the requested ExpressRoutePort peering location. |  -  |

<a id="expressRoutePortsLocationsList"></a>
# **expressRoutePortsLocationsList**
> ExpressRoutePortsLocationListResult expressRoutePortsLocationsList(subscriptionId, apiVersion)



Retrieves all ExpressRoutePort peering locations. Does not return available bandwidths for each location. Available bandwidths can only be obtained when retrieving a specific peering location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpressRoutePortsLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExpressRoutePortsLocationsApi apiInstance = new ExpressRoutePortsLocationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ExpressRoutePortsLocationListResult result = apiInstance.expressRoutePortsLocationsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpressRoutePortsLocationsApi#expressRoutePortsLocationsList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ExpressRoutePortsLocationListResult**](ExpressRoutePortsLocationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the list of all ExpressRoutePort peering locations. |  -  |

