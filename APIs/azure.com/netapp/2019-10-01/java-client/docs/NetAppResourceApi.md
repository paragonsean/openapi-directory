# NetAppResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**netAppResourceCheckFilePathAvailability**](NetAppResourceApi.md#netAppResourceCheckFilePathAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkFilePathAvailability | Check file path availability |
| [**netAppResourceCheckNameAvailability**](NetAppResourceApi.md#netAppResourceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkNameAvailability | Check resource name availability |


<a id="netAppResourceCheckFilePathAvailability"></a>
# **netAppResourceCheckFilePathAvailability**
> ResourceNameAvailability netAppResourceCheckFilePathAvailability(subscriptionId, location, apiVersion, body)

Check file path availability

Check if a file path is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppResourceApi apiInstance = new NetAppResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The location
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    ResourceNameAvailabilityRequest body = new ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | File path availability request.
    try {
      ResourceNameAvailability result = apiInstance.netAppResourceCheckFilePathAvailability(subscriptionId, location, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppResourceApi#netAppResourceCheckFilePathAvailability");
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
| **location** | **String**| The location | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| File path availability request. | |

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="netAppResourceCheckNameAvailability"></a>
# **netAppResourceCheckNameAvailability**
> ResourceNameAvailability netAppResourceCheckNameAvailability(subscriptionId, location, apiVersion, body)

Check resource name availability

Check if a resource name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetAppResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NetAppResourceApi apiInstance = new NetAppResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | The location
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    ResourceNameAvailabilityRequest body = new ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | Name availability request.
    try {
      ResourceNameAvailability result = apiInstance.netAppResourceCheckNameAvailability(subscriptionId, location, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetAppResourceApi#netAppResourceCheckNameAvailability");
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
| **location** | **String**| The location | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| Name availability request. | |

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

