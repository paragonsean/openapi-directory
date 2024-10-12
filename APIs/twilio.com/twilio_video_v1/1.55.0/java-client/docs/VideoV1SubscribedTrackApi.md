# VideoV1SubscribedTrackApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRoomParticipantSubscribedTrack**](VideoV1SubscribedTrackApi.md#fetchRoomParticipantSubscribedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribedTracks/{Sid} |  |
| [**listRoomParticipantSubscribedTrack**](VideoV1SubscribedTrackApi.md#listRoomParticipantSubscribedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribedTracks |  |


<a id="fetchRoomParticipantSubscribedTrack"></a>
# **fetchRoomParticipantSubscribedTrack**
> VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack fetchRoomParticipantSubscribedTrack(roomSid, participantSid, sid)



Returns a single Track resource represented by &#x60;track_sid&#x60;.  Note: This is one resource with the Video API that requires a SID, be Track Name on the subscriber side is not guaranteed to be unique.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1SubscribedTrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1SubscribedTrackApi apiInstance = new VideoV1SubscribedTrackApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room where the Track resource to fetch is subscribed.
    String participantSid = "participantSid_example"; // String | The SID of the participant that subscribes to the Track resource to fetch.
    String sid = "sid_example"; // String | The SID of the RoomParticipantSubscribedTrack resource to fetch.
    try {
      VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack result = apiInstance.fetchRoomParticipantSubscribedTrack(roomSid, participantSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1SubscribedTrackApi#fetchRoomParticipantSubscribedTrack");
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
| **roomSid** | **String**| The SID of the Room where the Track resource to fetch is subscribed. | |
| **participantSid** | **String**| The SID of the participant that subscribes to the Track resource to fetch. | |
| **sid** | **String**| The SID of the RoomParticipantSubscribedTrack resource to fetch. | |

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack**](VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRoomParticipantSubscribedTrack"></a>
# **listRoomParticipantSubscribedTrack**
> ListRoomParticipantSubscribedTrackResponse listRoomParticipantSubscribedTrack(roomSid, participantSid, pageSize, page, pageToken)



Returns a list of tracks that are subscribed for the participant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1SubscribedTrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1SubscribedTrackApi apiInstance = new VideoV1SubscribedTrackApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource with the Track resources to read.
    String participantSid = "participantSid_example"; // String | The SID of the participant that subscribes to the Track resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRoomParticipantSubscribedTrackResponse result = apiInstance.listRoomParticipantSubscribedTrack(roomSid, participantSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1SubscribedTrackApi#listRoomParticipantSubscribedTrack");
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
| **roomSid** | **String**| The SID of the Room resource with the Track resources to read. | |
| **participantSid** | **String**| The SID of the participant that subscribes to the Track resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRoomParticipantSubscribedTrackResponse**](ListRoomParticipantSubscribedTrackResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

