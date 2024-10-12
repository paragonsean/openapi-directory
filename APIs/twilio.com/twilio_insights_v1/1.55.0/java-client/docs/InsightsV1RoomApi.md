# InsightsV1RoomApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchVideoRoomSummary**](InsightsV1RoomApi.md#fetchVideoRoomSummary) | **GET** /v1/Video/Rooms/{RoomSid} |  |
| [**listVideoRoomSummary**](InsightsV1RoomApi.md#listVideoRoomSummary) | **GET** /v1/Video/Rooms |  |


<a id="fetchVideoRoomSummary"></a>
# **fetchVideoRoomSummary**
> InsightsV1VideoRoomSummary fetchVideoRoomSummary(roomSid)



Get Video Log Analyzer data for a Room.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1RoomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1RoomApi apiInstance = new InsightsV1RoomApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource.
    try {
      InsightsV1VideoRoomSummary result = apiInstance.fetchVideoRoomSummary(roomSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1RoomApi#fetchVideoRoomSummary");
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

### Return type

[**InsightsV1VideoRoomSummary**](InsightsV1VideoRoomSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listVideoRoomSummary"></a>
# **listVideoRoomSummary**
> ListVideoRoomSummaryResponse listVideoRoomSummary(roomType, codec, roomName, createdAfter, createdBefore, pageSize, page, pageToken)



Get a list of Programmable Video Rooms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1RoomApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1RoomApi apiInstance = new InsightsV1RoomApi(defaultClient);
    List<VideoRoomSummaryEnumRoomType> roomType = Arrays.asList(); // List<VideoRoomSummaryEnumRoomType> | Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
    List<VideoRoomSummaryEnumCodec> codec = Arrays.asList(); // List<VideoRoomSummaryEnumCodec> | Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
    String roomName = "roomName_example"; // String | Room friendly name.
    OffsetDateTime createdAfter = OffsetDateTime.now(); // OffsetDateTime | Only read rooms that started on or after this ISO 8601 timestamp.
    OffsetDateTime createdBefore = OffsetDateTime.now(); // OffsetDateTime | Only read rooms that started before this ISO 8601 timestamp.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListVideoRoomSummaryResponse result = apiInstance.listVideoRoomSummary(roomType, codec, roomName, createdAfter, createdBefore, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1RoomApi#listVideoRoomSummary");
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
| **roomType** | [**List&lt;VideoRoomSummaryEnumRoomType&gt;**](VideoRoomSummaryEnumRoomType.md)| Type of room. Can be &#x60;go&#x60;, &#x60;peer_to_peer&#x60;, &#x60;group&#x60;, or &#x60;group_small&#x60;. | [optional] |
| **codec** | [**List&lt;VideoRoomSummaryEnumCodec&gt;**](VideoRoomSummaryEnumCodec.md)| Codecs used by participants in the room. Can be &#x60;VP8&#x60;, &#x60;H264&#x60;, or &#x60;VP9&#x60;. | [optional] |
| **roomName** | **String**| Room friendly name. | [optional] |
| **createdAfter** | **OffsetDateTime**| Only read rooms that started on or after this ISO 8601 timestamp. | [optional] |
| **createdBefore** | **OffsetDateTime**| Only read rooms that started before this ISO 8601 timestamp. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListVideoRoomSummaryResponse**](ListVideoRoomSummaryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

