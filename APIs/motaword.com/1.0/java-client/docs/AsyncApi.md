# AsyncApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadAsync**](AsyncApi.md#downloadAsync) | **GET** /async/download | Download result of an async operation |


<a id="downloadAsync"></a>
# **downloadAsync**
> File downloadAsync(asyncRequestKey)

Download result of an async operation

Download the result of an async operation that you have requested in other endpoints.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AsyncApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    AsyncApi apiInstance = new AsyncApi(defaultClient);
    String asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
    try {
      File result = apiInstance.downloadAsync(asyncRequestKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AsyncApi#downloadAsync");
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
| **asyncRequestKey** | **String**| Async operation key | |

### Return type

[**File**](File.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **404** | ProjectNotFound |  -  |

