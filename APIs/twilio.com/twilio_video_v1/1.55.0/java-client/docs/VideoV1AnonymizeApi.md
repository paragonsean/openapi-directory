# VideoV1AnonymizeApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateRoomParticipantAnonymize**](VideoV1AnonymizeApi.md#updateRoomParticipantAnonymize) | **POST** /v1/Rooms/{RoomSid}/Participants/{Sid}/Anonymize |  |


<a id="updateRoomParticipantAnonymize"></a>
# **updateRoomParticipantAnonymize**
> VideoV1RoomRoomParticipantRoomParticipantAnonymize updateRoomParticipantAnonymize(roomSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1AnonymizeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1AnonymizeApi apiInstance = new VideoV1AnonymizeApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the room with the participant to update.
    String sid = "sid_example"; // String | The SID of the RoomParticipant resource to update.
    try {
      VideoV1RoomRoomParticipantRoomParticipantAnonymize result = apiInstance.updateRoomParticipantAnonymize(roomSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1AnonymizeApi#updateRoomParticipantAnonymize");
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

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantAnonymize**](VideoV1RoomRoomParticipantRoomParticipantAnonymize.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

