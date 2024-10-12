# MediaV1PlayerStreamerApi

All URIs are relative to *https://media.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPlayerStreamer**](MediaV1PlayerStreamerApi.md#createPlayerStreamer) | **POST** /v1/PlayerStreamers |  |
| [**fetchPlayerStreamer**](MediaV1PlayerStreamerApi.md#fetchPlayerStreamer) | **GET** /v1/PlayerStreamers/{Sid} |  |
| [**listPlayerStreamer**](MediaV1PlayerStreamerApi.md#listPlayerStreamer) | **GET** /v1/PlayerStreamers |  |
| [**updatePlayerStreamer**](MediaV1PlayerStreamerApi.md#updatePlayerStreamer) | **POST** /v1/PlayerStreamers/{Sid} |  |


<a id="createPlayerStreamer"></a>
# **createPlayerStreamer**
> MediaV1PlayerStreamer createPlayerStreamer(maxDuration, statusCallback, statusCallbackMethod, video)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1PlayerStreamerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1PlayerStreamerApi apiInstance = new MediaV1PlayerStreamerApi(defaultClient);
    Integer maxDuration = 56; // Integer | The maximum time, in seconds, that the PlayerStreamer is active (`created` or `started`) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming.
    URI statusCallback = new URI(); // URI | The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
    Boolean video = true; // Boolean | Specifies whether the PlayerStreamer is configured to stream video. Defaults to `true`.
    try {
      MediaV1PlayerStreamer result = apiInstance.createPlayerStreamer(maxDuration, statusCallback, statusCallbackMethod, video);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1PlayerStreamerApi#createPlayerStreamer");
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
| **maxDuration** | **Integer**| The maximum time, in seconds, that the PlayerStreamer is active (&#x60;created&#x60; or &#x60;started&#x60;) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming. | [optional] |
| **statusCallback** | **URI**| The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **video** | **Boolean**| Specifies whether the PlayerStreamer is configured to stream video. Defaults to &#x60;true&#x60;. | [optional] |

### Return type

[**MediaV1PlayerStreamer**](MediaV1PlayerStreamer.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchPlayerStreamer"></a>
# **fetchPlayerStreamer**
> MediaV1PlayerStreamer fetchPlayerStreamer(sid)



Returns a single PlayerStreamer resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1PlayerStreamerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1PlayerStreamerApi apiInstance = new MediaV1PlayerStreamerApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the PlayerStreamer resource to fetch.
    try {
      MediaV1PlayerStreamer result = apiInstance.fetchPlayerStreamer(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1PlayerStreamerApi#fetchPlayerStreamer");
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

[**MediaV1PlayerStreamer**](MediaV1PlayerStreamer.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listPlayerStreamer"></a>
# **listPlayerStreamer**
> ListPlayerStreamerResponse listPlayerStreamer(order, status, pageSize, page, pageToken)



Returns a list of PlayerStreamers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1PlayerStreamerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1PlayerStreamerApi apiInstance = new MediaV1PlayerStreamerApi(defaultClient);
    PlayerStreamerEnumOrder order = PlayerStreamerEnumOrder.fromValue("asc"); // PlayerStreamerEnumOrder | The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
    PlayerStreamerEnumStatus status = PlayerStreamerEnumStatus.fromValue("created"); // PlayerStreamerEnumStatus | Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListPlayerStreamerResponse result = apiInstance.listPlayerStreamer(order, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1PlayerStreamerApi#listPlayerStreamer");
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
| **order** | **PlayerStreamerEnumOrder**| The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default. | [optional] [enum: asc, desc] |
| **status** | **PlayerStreamerEnumStatus**| Status to filter by, with possible values &#x60;created&#x60;, &#x60;started&#x60;, &#x60;ended&#x60;, or &#x60;failed&#x60;. | [optional] [enum: created, started, ended, failed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListPlayerStreamerResponse**](ListPlayerStreamerResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updatePlayerStreamer"></a>
# **updatePlayerStreamer**
> MediaV1PlayerStreamer updatePlayerStreamer(sid, status)



Updates a PlayerStreamer resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1PlayerStreamerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1PlayerStreamerApi apiInstance = new MediaV1PlayerStreamerApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the PlayerStreamer resource to update.
    PlayerStreamerEnumUpdateStatus status = PlayerStreamerEnumUpdateStatus.fromValue("ended"); // PlayerStreamerEnumUpdateStatus | 
    try {
      MediaV1PlayerStreamer result = apiInstance.updatePlayerStreamer(sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1PlayerStreamerApi#updatePlayerStreamer");
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
| **sid** | **String**| The SID of the PlayerStreamer resource to update. | |
| **status** | **PlayerStreamerEnumUpdateStatus**|  | [enum: ended] |

### Return type

[**MediaV1PlayerStreamer**](MediaV1PlayerStreamer.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

