# VideoV1PublishedTrackApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRoomParticipantPublishedTrack**](VideoV1PublishedTrackApi.md#fetchRoomParticipantPublishedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks/{Sid} |  |
| [**listRoomParticipantPublishedTrack**](VideoV1PublishedTrackApi.md#listRoomParticipantPublishedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks |  |


<a id="fetchRoomParticipantPublishedTrack"></a>
# **fetchRoomParticipantPublishedTrack**
> VideoV1RoomRoomParticipantRoomParticipantPublishedTrack fetchRoomParticipantPublishedTrack(roomSid, participantSid, sid)



Returns a single Track resource represented by TrackName or SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1PublishedTrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1PublishedTrackApi apiInstance = new VideoV1PublishedTrackApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource where the Track resource to fetch is published.
    String participantSid = "participantSid_example"; // String | The SID of the Participant resource with the published track to fetch.
    String sid = "sid_example"; // String | The SID of the RoomParticipantPublishedTrack resource to fetch.
    try {
      VideoV1RoomRoomParticipantRoomParticipantPublishedTrack result = apiInstance.fetchRoomParticipantPublishedTrack(roomSid, participantSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1PublishedTrackApi#fetchRoomParticipantPublishedTrack");
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
| **roomSid** | **String**| The SID of the Room resource where the Track resource to fetch is published. | |
| **participantSid** | **String**| The SID of the Participant resource with the published track to fetch. | |
| **sid** | **String**| The SID of the RoomParticipantPublishedTrack resource to fetch. | |

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantPublishedTrack**](VideoV1RoomRoomParticipantRoomParticipantPublishedTrack.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRoomParticipantPublishedTrack"></a>
# **listRoomParticipantPublishedTrack**
> ListRoomParticipantPublishedTrackResponse listRoomParticipantPublishedTrack(roomSid, participantSid, pageSize, page, pageToken)



Returns a list of tracks associated with a given Participant. Only &#x60;currently&#x60; Published Tracks are in the list resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1PublishedTrackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1PublishedTrackApi apiInstance = new VideoV1PublishedTrackApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource where the Track resources to read are published.
    String participantSid = "participantSid_example"; // String | The SID of the Participant resource with the published tracks to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRoomParticipantPublishedTrackResponse result = apiInstance.listRoomParticipantPublishedTrack(roomSid, participantSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1PublishedTrackApi#listRoomParticipantPublishedTrack");
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
| **roomSid** | **String**| The SID of the Room resource where the Track resources to read are published. | |
| **participantSid** | **String**| The SID of the Participant resource with the published tracks to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRoomParticipantPublishedTrackResponse**](ListRoomParticipantPublishedTrackResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

