# RtcApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActiveSessions**](RtcApi.md#getActiveSessions) | **GET** /rtc/sessions | Gets a list of active sessions |


<a id="getActiveSessions"></a>
# **getActiveSessions**
> Label getActiveSessions()

Gets a list of active sessions

Gets a list of active RTCsessions OauthScopes: CALLS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RtcApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    RtcApi apiInstance = new RtcApi(defaultClient);
    try {
      Label result = apiInstance.getActiveSessions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RtcApi#getActiveSessions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of active RTCsessions was returned |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

