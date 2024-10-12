# MediaV1PlaybackGrantApi

All URIs are relative to *https://media.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPlayerStreamerPlaybackGrant**](MediaV1PlaybackGrantApi.md#createPlayerStreamerPlaybackGrant) | **POST** /v1/PlayerStreamers/{Sid}/PlaybackGrant |  |
| [**fetchPlayerStreamerPlaybackGrant**](MediaV1PlaybackGrantApi.md#fetchPlayerStreamerPlaybackGrant) | **GET** /v1/PlayerStreamers/{Sid}/PlaybackGrant |  |


<a id="createPlayerStreamerPlaybackGrant"></a>
# **createPlayerStreamerPlaybackGrant**
> MediaV1PlayerStreamerPlayerStreamerPlaybackGrant createPlayerStreamerPlaybackGrant(sid, accessControlAllowOrigin, ttl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1PlaybackGrantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1PlaybackGrantApi apiInstance = new MediaV1PlaybackGrantApi(defaultClient);
    String sid = "sid_example"; // String | The unique string generated to identify the PlayerStreamer resource associated with this PlaybackGrant
    String accessControlAllowOrigin = "accessControlAllowOrigin_example"; // String | The full origin URL where the livestream can be streamed. If this is not provided, it can be streamed from any domain.
    Integer ttl = 56; // Integer | The time to live of the PlaybackGrant. Default value is 15 seconds. Maximum value is 60 seconds.
    try {
      MediaV1PlayerStreamerPlayerStreamerPlaybackGrant result = apiInstance.createPlayerStreamerPlaybackGrant(sid, accessControlAllowOrigin, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1PlaybackGrantApi#createPlayerStreamerPlaybackGrant");
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
| **sid** | **String**| The unique string generated to identify the PlayerStreamer resource associated with this PlaybackGrant | |
| **accessControlAllowOrigin** | **String**| The full origin URL where the livestream can be streamed. If this is not provided, it can be streamed from any domain. | [optional] |
| **ttl** | **Integer**| The time to live of the PlaybackGrant. Default value is 15 seconds. Maximum value is 60 seconds. | [optional] |

### Return type

[**MediaV1PlayerStreamerPlayerStreamerPlaybackGrant**](MediaV1PlayerStreamerPlayerStreamerPlaybackGrant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchPlayerStreamerPlaybackGrant"></a>
# **fetchPlayerStreamerPlaybackGrant**
> MediaV1PlayerStreamerPlayerStreamerPlaybackGrant fetchPlayerStreamerPlaybackGrant(sid)



**This method is not enabled.** Returns a single PlaybackGrant resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1PlaybackGrantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1PlaybackGrantApi apiInstance = new MediaV1PlaybackGrantApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the PlayerStreamer resource to fetch.
    try {
      MediaV1PlayerStreamerPlayerStreamerPlaybackGrant result = apiInstance.fetchPlayerStreamerPlaybackGrant(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1PlaybackGrantApi#fetchPlayerStreamerPlaybackGrant");
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
| **sid** | **String**| The SID of the PlayerStreamer resource to fetch. | |

### Return type

[**MediaV1PlayerStreamerPlayerStreamerPlaybackGrant**](MediaV1PlayerStreamerPlayerStreamerPlaybackGrant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

