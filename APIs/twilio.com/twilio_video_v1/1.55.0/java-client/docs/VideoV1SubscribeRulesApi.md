# VideoV1SubscribeRulesApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRoomParticipantSubscribeRule**](VideoV1SubscribeRulesApi.md#fetchRoomParticipantSubscribeRule) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules |  |
| [**updateRoomParticipantSubscribeRule**](VideoV1SubscribeRulesApi.md#updateRoomParticipantSubscribeRule) | **POST** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules |  |


<a id="fetchRoomParticipantSubscribeRule"></a>
# **fetchRoomParticipantSubscribeRule**
> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule fetchRoomParticipantSubscribeRule(roomSid, participantSid)



Returns a list of Subscribe Rules for the Participant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1SubscribeRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1SubscribeRulesApi apiInstance = new VideoV1SubscribeRulesApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource where the subscribe rules to fetch apply.
    String participantSid = "participantSid_example"; // String | The SID of the Participant resource with the subscribe rules to fetch.
    try {
      VideoV1RoomRoomParticipantRoomParticipantSubscribeRule result = apiInstance.fetchRoomParticipantSubscribeRule(roomSid, participantSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1SubscribeRulesApi#fetchRoomParticipantSubscribeRule");
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
| **roomSid** | **String**| The SID of the Room resource where the subscribe rules to fetch apply. | |
| **participantSid** | **String**| The SID of the Participant resource with the subscribe rules to fetch. | |

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantSubscribeRule**](VideoV1RoomRoomParticipantRoomParticipantSubscribeRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRoomParticipantSubscribeRule"></a>
# **updateRoomParticipantSubscribeRule**
> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule updateRoomParticipantSubscribeRule(roomSid, participantSid, rules)



Update the Subscribe Rules for the Participant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1SubscribeRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1SubscribeRulesApi apiInstance = new VideoV1SubscribeRulesApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource where the subscribe rules to update apply.
    String participantSid = "participantSid_example"; // String | The SID of the Participant resource to update the Subscribe Rules.
    Object rules = null; // Object | A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.
    try {
      VideoV1RoomRoomParticipantRoomParticipantSubscribeRule result = apiInstance.updateRoomParticipantSubscribeRule(roomSid, participantSid, rules);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1SubscribeRulesApi#updateRoomParticipantSubscribeRule");
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
| **roomSid** | **String**| The SID of the Room resource where the subscribe rules to update apply. | |
| **participantSid** | **String**| The SID of the Participant resource to update the Subscribe Rules. | |
| **rules** | [**Object**](Object.md)| A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information. | [optional] |

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantSubscribeRule**](VideoV1RoomRoomParticipantRoomParticipantSubscribeRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

