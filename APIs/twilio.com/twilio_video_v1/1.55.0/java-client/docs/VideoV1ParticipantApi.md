# VideoV1ParticipantApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRoomParticipant**](VideoV1ParticipantApi.md#fetchRoomParticipant) | **GET** /v1/Rooms/{RoomSid}/Participants/{Sid} |  |
| [**listRoomParticipant**](VideoV1ParticipantApi.md#listRoomParticipant) | **GET** /v1/Rooms/{RoomSid}/Participants |  |
| [**updateRoomParticipant**](VideoV1ParticipantApi.md#updateRoomParticipant) | **POST** /v1/Rooms/{RoomSid}/Participants/{Sid} |  |


<a id="fetchRoomParticipant"></a>
# **fetchRoomParticipant**
> VideoV1RoomRoomParticipant fetchRoomParticipant(roomSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1ParticipantApi apiInstance = new VideoV1ParticipantApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the room with the Participant resource to fetch.
    String sid = "sid_example"; // String | The SID of the RoomParticipant resource to fetch.
    try {
      VideoV1RoomRoomParticipant result = apiInstance.fetchRoomParticipant(roomSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1ParticipantApi#fetchRoomParticipant");
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
| **roomSid** | **String**| The SID of the room with the Participant resource to fetch. | |
| **sid** | **String**| The SID of the RoomParticipant resource to fetch. | |

### Return type

[**VideoV1RoomRoomParticipant**](VideoV1RoomRoomParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRoomParticipant"></a>
# **listRoomParticipant**
> ListRoomParticipantResponse listRoomParticipant(roomSid, status, identity, dateCreatedAfter, dateCreatedBefore, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1ParticipantApi apiInstance = new VideoV1ParticipantApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the room with the Participant resources to read.
    RoomParticipantEnumStatus status = RoomParticipantEnumStatus.fromValue("connected"); // RoomParticipantEnumStatus | Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
    String identity = "identity_example"; // String | Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
    OffsetDateTime dateCreatedAfter = OffsetDateTime.now(); // OffsetDateTime | Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    OffsetDateTime dateCreatedBefore = OffsetDateTime.now(); // OffsetDateTime | Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRoomParticipantResponse result = apiInstance.listRoomParticipant(roomSid, status, identity, dateCreatedAfter, dateCreatedBefore, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1ParticipantApi#listRoomParticipant");
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
| **roomSid** | **String**| The SID of the room with the Participant resources to read. | |
| **status** | **RoomParticipantEnumStatus**| Read only the participants with this status. Can be: &#x60;connected&#x60; or &#x60;disconnected&#x60;. For &#x60;in-progress&#x60; Rooms the default Status is &#x60;connected&#x60;, for &#x60;completed&#x60; Rooms only &#x60;disconnected&#x60; Participants are returned. | [optional] [enum: connected, disconnected] |
| **identity** | **String**| Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) &#x60;identity&#x60; value. | [optional] |
| **dateCreatedAfter** | **OffsetDateTime**| Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. | [optional] |
| **dateCreatedBefore** | **OffsetDateTime**| Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRoomParticipantResponse**](ListRoomParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRoomParticipant"></a>
# **updateRoomParticipant**
> VideoV1RoomRoomParticipant updateRoomParticipant(roomSid, sid, status)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1ParticipantApi apiInstance = new VideoV1ParticipantApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the room with the participant to update.
    String sid = "sid_example"; // String | The SID of the RoomParticipant resource to update.
    RoomParticipantEnumStatus status = RoomParticipantEnumStatus.fromValue("connected"); // RoomParticipantEnumStatus | 
    try {
      VideoV1RoomRoomParticipant result = apiInstance.updateRoomParticipant(roomSid, sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1ParticipantApi#updateRoomParticipant");
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
| **roomSid** | **String**| The SID of the room with the participant to update. | |
| **sid** | **String**| The SID of the RoomParticipant resource to update. | |
| **status** | **RoomParticipantEnumStatus**|  | [optional] [enum: connected, disconnected] |

### Return type

[**VideoV1RoomRoomParticipant**](VideoV1RoomRoomParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

