# VideoV1RecordingApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRecording**](VideoV1RecordingApi.md#deleteRecording) | **DELETE** /v1/Recordings/{Sid} |  |
| [**fetchRecording**](VideoV1RecordingApi.md#fetchRecording) | **GET** /v1/Recordings/{Sid} |  |
| [**listRecording**](VideoV1RecordingApi.md#listRecording) | **GET** /v1/Recordings |  |


<a id="deleteRecording"></a>
# **deleteRecording**
> deleteRecording(sid)



Delete a Recording resource identified by a Recording SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingApi apiInstance = new VideoV1RecordingApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Recording resource to delete.
    try {
      apiInstance.deleteRecording(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingApi#deleteRecording");
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
| **sid** | **String**| The SID of the Recording resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchRecording"></a>
# **fetchRecording**
> VideoV1Recording fetchRecording(sid)



Returns a single Recording resource identified by a Recording SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingApi apiInstance = new VideoV1RecordingApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Recording resource to fetch.
    try {
      VideoV1Recording result = apiInstance.fetchRecording(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingApi#fetchRecording");
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
| **sid** | **String**| The SID of the Recording resource to fetch. | |

### Return type

[**VideoV1Recording**](VideoV1Recording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRecording"></a>
# **listRecording**
> ListRecordingResponse listRecording(status, sourceSid, groupingSid, dateCreatedAfter, dateCreatedBefore, mediaType, pageSize, page, pageToken)



List of all Track recordings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingApi apiInstance = new VideoV1RecordingApi(defaultClient);
    RecordingEnumStatus status = RecordingEnumStatus.fromValue("processing"); // RecordingEnumStatus | Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
    String sourceSid = "sourceSid_example"; // String | Read only the recordings that have this `source_sid`.
    List<String> groupingSid = Arrays.asList(); // List<String> | Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
    OffsetDateTime dateCreatedAfter = OffsetDateTime.now(); // OffsetDateTime | Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
    OffsetDateTime dateCreatedBefore = OffsetDateTime.now(); // OffsetDateTime | Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
    RecordingEnumType mediaType = RecordingEnumType.fromValue("audio"); // RecordingEnumType | Read only recordings that have this media type. Can be either `audio` or `video`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRecordingResponse result = apiInstance.listRecording(status, sourceSid, groupingSid, dateCreatedAfter, dateCreatedBefore, mediaType, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingApi#listRecording");
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
| **status** | **RecordingEnumStatus**| Read only the recordings that have this status. Can be: &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;deleted&#x60;. | [optional] [enum: processing, completed, deleted, failed] |
| **sourceSid** | **String**| Read only the recordings that have this &#x60;source_sid&#x60;. | [optional] |
| **groupingSid** | [**List&lt;String&gt;**](String.md)| Read only recordings with this &#x60;grouping_sid&#x60;, which may include a &#x60;participant_sid&#x60; and/or a &#x60;room_sid&#x60;. | [optional] |
| **dateCreatedAfter** | **OffsetDateTime**| Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone. | [optional] |
| **dateCreatedBefore** | **OffsetDateTime**| Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as &#x60;YYYY-MM-DDThh:mm:ss+|-hh:mm&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;. | [optional] |
| **mediaType** | **RecordingEnumType**| Read only recordings that have this media type. Can be either &#x60;audio&#x60; or &#x60;video&#x60;. | [optional] [enum: audio, video, data] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRecordingResponse**](ListRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

