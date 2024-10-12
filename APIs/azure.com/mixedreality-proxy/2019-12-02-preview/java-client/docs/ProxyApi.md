# ProxyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkNameAvailabilityLocal**](ProxyApi.md#checkNameAvailabilityLocal) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/locations/{location}/checkNameAvailability |  |
| [**operationsList**](ProxyApi.md#operationsList) | **GET** /providers/Microsoft.MixedReality/operations |  |


<a id="checkNameAvailabilityLocal"></a>
# **checkNameAvailabilityLocal**
> CheckNameAvailabilityResponse checkNameAvailabilityLocal(subscriptionId, location, apiVersion, checkNameAvailability)



Check Name Availability for local uniqueness

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String location = "location_example"; // String | The location in which uniqueness will be verified.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    CheckNameAvailabilityRequest checkNameAvailability = new CheckNameAvailabilityRequest(); // CheckNameAvailabilityRequest | Check Name Availability Request.
    try {
      CheckNameAvailabilityResponse result = apiInstance.checkNameAvailabilityLocal(subscriptionId, location, apiVersion, checkNameAvailability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#checkNameAvailabilityLocal");
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
| **subscriptionId** | **String**| Azure subscription ID. | |
| **location** | **String**| The location in which uniqueness will be verified. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **checkNameAvailability** | [**CheckNameAvailabilityRequest**](CheckNameAvailabilityRequest.md)| Check Name Availability Request. | |

### Return type

[**CheckNameAvailabilityResponse**](CheckNameAvailabilityResponse.md)

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

<a id="operationsList"></a>
# **operationsList**
> OperationPage operationsList(apiVersion)



Exposing Available Operations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      OperationPage result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#operationsList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**OperationPage**](OperationPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

