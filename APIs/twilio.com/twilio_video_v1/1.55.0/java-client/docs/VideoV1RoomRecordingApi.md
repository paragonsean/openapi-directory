# VideoV1RoomRecordingApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRoomRecording**](VideoV1RoomRecordingApi.md#deleteRoomRecording) | **DELETE** /v1/Rooms/{RoomSid}/Recordings/{Sid} |  |
| [**fetchRoomRecording**](VideoV1RoomRecordingApi.md#fetchRoomRecording) | **GET** /v1/Rooms/{RoomSid}/Recordings/{Sid} |  |
| [**listRoomRecording**](VideoV1RoomRecordingApi.md#listRoomRecording) | **GET** /v1/Rooms/{RoomSid}/Recordings |  |


<a id="deleteRoomRecording"></a>
# **deleteRoomRecording**
> deleteRoomRecording(roomSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomRecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomRecordingApi apiInstance = new VideoV1RoomRecordingApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the room with the RoomRecording resource to delete.
    String sid = "sid_example"; // String | The SID of the RoomRecording resource to delete.
    try {
      apiInstance.deleteRoomRecording(roomSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomRecordingApi#deleteRoomRecording");
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
| **roomSid** | **String**| The SID of the room with the RoomRecording resource to delete. | |
| **sid** | **String**| The SID of the RoomRecording resource to delete. | |

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

<a id="fetchRoomRecording"></a>
# **fetchRoomRecording**
> VideoV1RoomRoomRecording fetchRoomRecording(roomSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomRecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomRecordingApi apiInstance = new VideoV1RoomRecordingApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource with the recording to fetch.
    String sid = "sid_example"; // String | The SID of the RoomRecording resource to fetch.
    try {
      VideoV1RoomRoomRecording result = apiInstance.fetchRoomRecording(roomSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomRecordingApi#fetchRoomRecording");
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
| **roomSid** | **String**| The SID of the Room resource with the recording to fetch. | |
| **sid** | **String**| The SID of the RoomRecording resource to fetch. | |

### Return type

[**VideoV1RoomRoomRecording**](VideoV1RoomRoomRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRoomRecording"></a>
# **listRoomRecording**
> ListRoomRecordingResponse listRoomRecording(roomSid, status, sourceSid, dateCreatedAfter, dateCreatedBefore, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomRecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomRecordingApi apiInstance = new VideoV1RoomRecordingApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the room with the RoomRecording resources to read.
    RoomRecordingEnumStatus status = RoomRecordingEnumStatus.fromValue("processing"); // RoomRecordingEnumStatus | Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
    String sourceSid = "sourceSid_example"; // String | Read only the recordings that have this `source_sid`.
    OffsetDateTime dateCreatedAfter = OffsetDateTime.now(); // OffsetDateTime | Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
    OffsetDateTime dateCreatedBefore = OffsetDateTime.now(); // OffsetDateTime | Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRoomRecordingResponse result = apiInstance.listRoomRecording(roomSid, status, sourceSid, dateCreatedAfter, dateCreatedBefore, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomRecordingApi#listRoomRecording");
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
| **roomSid** | **String**| The SID of the room with the RoomRecording resources to read. | |
| **status** | **RoomRecordingEnumStatus**| Read only the recordings with this status. Can be: &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;deleted&#x60;. | [optional] [enum: processing, completed, deleted, failed] |
| **sourceSid** | **String**| Read only the recordings that have this &#x60;source_sid&#x60;. | [optional] |
| **dateCreatedAfter** | **OffsetDateTime**| Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone. | [optional] |
| **dateCreatedBefore** | **OffsetDateTime**| Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRoomRecordingResponse**](ListRoomRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

