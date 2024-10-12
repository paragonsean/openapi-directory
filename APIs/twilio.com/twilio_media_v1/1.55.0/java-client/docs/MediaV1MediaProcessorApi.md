# MediaV1MediaProcessorApi

All URIs are relative to *https://media.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMediaProcessor**](MediaV1MediaProcessorApi.md#createMediaProcessor) | **POST** /v1/MediaProcessors |  |
| [**fetchMediaProcessor**](MediaV1MediaProcessorApi.md#fetchMediaProcessor) | **GET** /v1/MediaProcessors/{Sid} |  |
| [**listMediaProcessor**](MediaV1MediaProcessorApi.md#listMediaProcessor) | **GET** /v1/MediaProcessors |  |
| [**updateMediaProcessor**](MediaV1MediaProcessorApi.md#updateMediaProcessor) | **POST** /v1/MediaProcessors/{Sid} |  |


<a id="createMediaProcessor"></a>
# **createMediaProcessor**
> MediaV1MediaProcessor createMediaProcessor(extension, extensionContext, extensionEnvironment, maxDuration, statusCallback, statusCallbackMethod)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaProcessorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaProcessorApi apiInstance = new MediaV1MediaProcessorApi(defaultClient);
    String extension = "extension_example"; // String | The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: `video-composer-v2`
    String extensionContext = "extensionContext_example"; // String | The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send.
    Object extensionEnvironment = null; // Object | User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this.
    Integer maxDuration = 56; // Integer | The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.
    URI statusCallback = new URI(); // URI | The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
    try {
      MediaV1MediaProcessor result = apiInstance.createMediaProcessor(extension, extensionContext, extensionEnvironment, maxDuration, statusCallback, statusCallbackMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaProcessorApi#createMediaProcessor");
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
| **extension** | **String**| The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: &#x60;video-composer-v2&#x60; | |
| **extensionContext** | **String**| The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send. | |
| **extensionEnvironment** | [**Object**](Object.md)| User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this. | [optional] |
| **maxDuration** | **Integer**| The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming. | [optional] |
| **statusCallback** | **URI**| The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |

### Return type

[**MediaV1MediaProcessor**](MediaV1MediaProcessor.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchMediaProcessor"></a>
# **fetchMediaProcessor**
> MediaV1MediaProcessor fetchMediaProcessor(sid)



Returns a single MediaProcessor resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaProcessorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaProcessorApi apiInstance = new MediaV1MediaProcessorApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the MediaProcessor resource to fetch.
    try {
      MediaV1MediaProcessor result = apiInstance.fetchMediaProcessor(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaProcessorApi#fetchMediaProcessor");
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
| **sid** | **String**| The SID of the MediaProcessor resource to fetch. | |

### Return type

[**MediaV1MediaProcessor**](MediaV1MediaProcessor.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMediaProcessor"></a>
# **listMediaProcessor**
> ListMediaProcessorResponse listMediaProcessor(order, status, pageSize, page, pageToken)



Returns a list of MediaProcessors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaProcessorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaProcessorApi apiInstance = new MediaV1MediaProcessorApi(defaultClient);
    MediaProcessorEnumOrder order = MediaProcessorEnumOrder.fromValue("asc"); // MediaProcessorEnumOrder | The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
    MediaProcessorEnumStatus status = MediaProcessorEnumStatus.fromValue("failed"); // MediaProcessorEnumStatus | Status to filter by, with possible values `started`, `ended` or `failed`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMediaProcessorResponse result = apiInstance.listMediaProcessor(order, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaProcessorApi#listMediaProcessor");
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
| **order** | **MediaProcessorEnumOrder**| The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default. | [optional] [enum: asc, desc] |
| **status** | **MediaProcessorEnumStatus**| Status to filter by, with possible values &#x60;started&#x60;, &#x60;ended&#x60; or &#x60;failed&#x60;. | [optional] [enum: failed, started, ended] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMediaProcessorResponse**](ListMediaProcessorResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateMediaProcessor"></a>
# **updateMediaProcessor**
> MediaV1MediaProcessor updateMediaProcessor(sid, status)



Updates a MediaProcessor resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaProcessorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaProcessorApi apiInstance = new MediaV1MediaProcessorApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the MediaProcessor resource to update.
    MediaProcessorEnumUpdateStatus status = MediaProcessorEnumUpdateStatus.fromValue("ended"); // MediaProcessorEnumUpdateStatus | 
    try {
      MediaV1MediaProcessor result = apiInstance.updateMediaProcessor(sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaProcessorApi#updateMediaProcessor");
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
| **sid** | **String**| The SID of the MediaProcessor resource to update. | |
| **status** | **MediaProcessorEnumUpdateStatus**|  | [enum: ended] |

### Return type

[**MediaV1MediaProcessor**](MediaV1MediaProcessor.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

