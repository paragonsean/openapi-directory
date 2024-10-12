# InsightsV1ParticipantApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchVideoParticipantSummary**](InsightsV1ParticipantApi.md#fetchVideoParticipantSummary) | **GET** /v1/Video/Rooms/{RoomSid}/Participants/{ParticipantSid} |  |
| [**listVideoParticipantSummary**](InsightsV1ParticipantApi.md#listVideoParticipantSummary) | **GET** /v1/Video/Rooms/{RoomSid}/Participants |  |


<a id="fetchVideoParticipantSummary"></a>
# **fetchVideoParticipantSummary**
> InsightsV1VideoRoomSummaryVideoParticipantSummary fetchVideoParticipantSummary(roomSid, participantSid)



Get Video Log Analyzer data for a Room Participant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1ParticipantApi apiInstance = new InsightsV1ParticipantApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource.
    String participantSid = "participantSid_example"; // String | The SID of the Participant resource.
    try {
      InsightsV1VideoRoomSummaryVideoParticipantSummary result = apiInstance.fetchVideoParticipantSummary(roomSid, participantSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1ParticipantApi#fetchVideoParticipantSummary");
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
| **roomSid** | **String**| The SID of the Room resource. | |
| **participantSid** | **String**| The SID of the Participant resource. | |

### Return type

[**InsightsV1VideoRoomSummaryVideoParticipantSummary**](InsightsV1VideoRoomSummaryVideoParticipantSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listVideoParticipantSummary"></a>
# **listVideoParticipantSummary**
> ListVideoParticipantSummaryResponse listVideoParticipantSummary(roomSid, pageSize, page, pageToken)



Get a list of room participants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1ParticipantApi apiInstance = new InsightsV1ParticipantApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListVideoParticipantSummaryResponse result = apiInstance.listVideoParticipantSummary(roomSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1ParticipantApi#listVideoParticipantSummary");
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
| **roomSid** | **String**| The SID of the Room resource. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListVideoParticipantSummaryResponse**](ListVideoParticipantSummaryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

