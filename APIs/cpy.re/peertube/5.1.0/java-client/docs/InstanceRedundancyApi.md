# InstanceRedundancyApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1ServerRedundancyHostPut**](InstanceRedundancyApi.md#apiV1ServerRedundancyHostPut) | **PUT** /api/v1/server/redundancy/{host} | Update a server redundancy policy |


<a id="apiV1ServerRedundancyHostPut"></a>
# **apiV1ServerRedundancyHostPut**
> apiV1ServerRedundancyHostPut(host, apiV1ServerRedundancyHostPutRequest)

Update a server redundancy policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceRedundancyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstanceRedundancyApi apiInstance = new InstanceRedundancyApi(defaultClient);
    String host = "host_example"; // String | server domain to mirror
    ApiV1ServerRedundancyHostPutRequest apiV1ServerRedundancyHostPutRequest = new ApiV1ServerRedundancyHostPutRequest(); // ApiV1ServerRedundancyHostPutRequest | 
    try {
      apiInstance.apiV1ServerRedundancyHostPut(host, apiV1ServerRedundancyHostPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceRedundancyApi#apiV1ServerRedundancyHostPut");
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
| **host** | **String**| server domain to mirror | |
| **apiV1ServerRedundancyHostPutRequest** | [**ApiV1ServerRedundancyHostPutRequest**](ApiV1ServerRedundancyHostPutRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | server is not already known |  -  |

