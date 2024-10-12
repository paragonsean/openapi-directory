# VideoV1RoomApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRoom**](VideoV1RoomApi.md#createRoom) | **POST** /v1/Rooms |  |
| [**fetchRoom**](VideoV1RoomApi.md#fetchRoom) | **GET** /v1/Rooms/{Sid} |  |
| [**listRoom**](VideoV1RoomApi.md#listRoom) | **GET** /v1/Rooms |  |
| [**updateRoom**](VideoV1RoomApi.md#updateRoom) | **POST** /v1/Rooms/{Sid} |  |


<a id="createRoom"></a>
# **createRoom**
> VideoV1Room createRoom(audioOnly, emptyRoomTimeout, enableTurn, largeRoom, maxParticipantDuration, maxParticipants, mediaRegion, recordParticipantsOnConnect, recordingRules, statusCallback, statusCallbackMethod, type, uniqueName, unusedRoomTimeout, videoCodecs)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomApi apiInstance = new VideoV1RoomApi(defaultClient);
    Boolean audioOnly = true; // Boolean | When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
    Integer emptyRoomTimeout = 56; // Integer | Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
    Boolean enableTurn = true; // Boolean | Deprecated, now always considered to be true.
    Boolean largeRoom = true; // Boolean | When set to true, indicated that this is the large room.
    Integer maxParticipantDuration = 56; // Integer | The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
    Integer maxParticipants = 56; // Integer | The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants.
    String mediaRegion = "mediaRegion_example"; // String | The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers). ***This feature is not available in `peer-to-peer` rooms.***
    Boolean recordParticipantsOnConnect = true; // Boolean | Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
    Object recordingRules = null; // Object | A collection of Recording Rules that describe how to include or exclude matching tracks for recording
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be `POST` or `GET`.
    RoomEnumRoomType type = RoomEnumRoomType.fromValue("go"); // RoomEnumRoomType | 
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
    Integer unusedRoomTimeout = 56; // Integer | Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
    List<RoomEnumVideoCodec> videoCodecs = Arrays.asList(); // List<RoomEnumVideoCodec> | An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
    try {
      VideoV1Room result = apiInstance.createRoom(audioOnly, emptyRoomTimeout, enableTurn, largeRoom, maxParticipantDuration, maxParticipants, mediaRegion, recordParticipantsOnConnect, recordingRules, statusCallback, statusCallbackMethod, type, uniqueName, unusedRoomTimeout, videoCodecs);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomApi#createRoom");
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
| **audioOnly** | **Boolean**| When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only. | [optional] |
| **emptyRoomTimeout** | **Integer**| Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions). | [optional] |
| **enableTurn** | **Boolean**| Deprecated, now always considered to be true. | [optional] |
| **largeRoom** | **Boolean**| When set to true, indicated that this is the large room. | [optional] |
| **maxParticipantDuration** | **Integer**| The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours). | [optional] |
| **maxParticipants** | **Integer**| The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants. | [optional] |
| **mediaRegion** | **String**| The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers). ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.*** | [optional] |
| **recordParticipantsOnConnect** | **Boolean**| Whether to start recording when Participants connect. ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.*** | [optional] |
| **recordingRules** | [**Object**](Object.md)| A collection of Recording Rules that describe how to include or exclude matching tracks for recording | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be &#x60;POST&#x60; or &#x60;GET&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **type** | **RoomEnumRoomType**|  | [optional] [enum: go, peer-to-peer, group, group-small] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used as a &#x60;room_sid&#x60; in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for &#x60;in-progress&#x60; rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is &#x60;in-progress&#x60;. | [optional] |
| **unusedRoomTimeout** | **Integer**| Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions). | [optional] |
| **videoCodecs** | [**List&lt;RoomEnumVideoCodec&gt;**](RoomEnumVideoCodec.md)| An array of the video codecs that are supported when publishing a track in the room.  Can be: &#x60;VP8&#x60; and &#x60;H264&#x60;.  ***This feature is not available in &#x60;peer-to-peer&#x60; rooms*** | [optional] |

### Return type

[**VideoV1Room**](VideoV1Room.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchRoom"></a>
# **fetchRoom**
> VideoV1Room fetchRoom(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomApi apiInstance = new VideoV1RoomApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Room resource to fetch.
    try {
      VideoV1Room result = apiInstance.fetchRoom(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomApi#fetchRoom");
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
| **sid** | **String**| The SID of the Room resource to fetch. | |

### Return type

[**VideoV1Room**](VideoV1Room.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRoom"></a>
# **listRoom**
> ListRoomResponse listRoom(status, uniqueName, dateCreatedAfter, dateCreatedBefore, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomApi apiInstance = new VideoV1RoomApi(defaultClient);
    RoomEnumRoomStatus status = RoomEnumRoomStatus.fromValue("in-progress"); // RoomEnumRoomStatus | Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
    String uniqueName = "uniqueName_example"; // String | Read only rooms with the this `unique_name`.
    OffsetDateTime dateCreatedAfter = OffsetDateTime.now(); // OffsetDateTime | Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
    OffsetDateTime dateCreatedBefore = OffsetDateTime.now(); // OffsetDateTime | Read only rooms that started before this date, given as `YYYY-MM-DD`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRoomResponse result = apiInstance.listRoom(status, uniqueName, dateCreatedAfter, dateCreatedBefore, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomApi#listRoom");
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
| **status** | **RoomEnumRoomStatus**| Read only the rooms with this status. Can be: &#x60;in-progress&#x60; (default) or &#x60;completed&#x60; | [optional] [enum: in-progress, completed, failed] |
| **uniqueName** | **String**| Read only rooms with the this &#x60;unique_name&#x60;. | [optional] |
| **dateCreatedAfter** | **OffsetDateTime**| Read only rooms that started on or after this date, given as &#x60;YYYY-MM-DD&#x60;. | [optional] |
| **dateCreatedBefore** | **OffsetDateTime**| Read only rooms that started before this date, given as &#x60;YYYY-MM-DD&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRoomResponse**](ListRoomResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRoom"></a>
# **updateRoom**
> VideoV1Room updateRoom(sid, status)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RoomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RoomApi apiInstance = new VideoV1RoomApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Room resource to update.
    RoomEnumRoomStatus status = RoomEnumRoomStatus.fromValue("in-progress"); // RoomEnumRoomStatus | 
    try {
      VideoV1Room result = apiInstance.updateRoom(sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RoomApi#updateRoom");
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
| **sid** | **String**| The SID of the Room resource to update. | |
| **status** | **RoomEnumRoomStatus**|  | [enum: in-progress, completed, failed] |

### Return type

[**VideoV1Room**](VideoV1Room.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

