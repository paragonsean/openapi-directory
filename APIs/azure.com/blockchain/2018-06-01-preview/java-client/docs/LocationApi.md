# LocationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locationsCheckNameAvailability**](LocationApi.md#locationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/locations/{locationName}/checkNameAvailability |  |
| [**locationsListConsortiums**](LocationApi.md#locationsListConsortiums) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/locations/{locationName}/listConsortiums |  |


<a id="locationsCheckNameAvailability"></a>
# **locationsCheckNameAvailability**
> NameAvailability locationsCheckNameAvailability(locationName, apiVersion, subscriptionId, nameAvailabilityRequest)



To check whether a resource name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationApi apiInstance = new LocationApi(defaultClient);
    String locationName = "locationName_example"; // String | Location Name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    NameAvailabilityRequest nameAvailabilityRequest = new NameAvailabilityRequest(); // NameAvailabilityRequest | Name availability request payload.
    try {
      NameAvailability result = apiInstance.locationsCheckNameAvailability(locationName, apiVersion, subscriptionId, nameAvailabilityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#locationsCheckNameAvailability");
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
| **locationName** | **String**| Location Name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |
| **nameAvailabilityRequest** | [**NameAvailabilityRequest**](NameAvailabilityRequest.md)| Name availability request payload. | [optional] |

### Return type

[**NameAvailability**](NameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="locationsListConsortiums"></a>
# **locationsListConsortiums**
> ConsortiumCollection locationsListConsortiums(locationName, apiVersion, subscriptionId)



Lists the available consortiums for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    LocationApi apiInstance = new LocationApi(defaultClient);
    String locationName = "locationName_example"; // String | Location Name.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    try {
      ConsortiumCollection result = apiInstance.locationsListConsortiums(locationName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationApi#locationsListConsortiums");
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
| **locationName** | **String**| Location Name. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |

### Return type

[**ConsortiumCollection**](ConsortiumCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

