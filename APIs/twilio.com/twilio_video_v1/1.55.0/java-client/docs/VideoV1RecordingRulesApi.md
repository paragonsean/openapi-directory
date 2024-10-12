# VideoV1RecordingRulesApi

All URIs are relative to *https://video.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRoomRecordingRule**](VideoV1RecordingRulesApi.md#fetchRoomRecordingRule) | **GET** /v1/Rooms/{RoomSid}/RecordingRules |  |
| [**updateRoomRecordingRule**](VideoV1RecordingRulesApi.md#updateRoomRecordingRule) | **POST** /v1/Rooms/{RoomSid}/RecordingRules |  |


<a id="fetchRoomRecordingRule"></a>
# **fetchRoomRecordingRule**
> VideoV1RoomRoomRecordingRule fetchRoomRecordingRule(roomSid)



Returns a list of Recording Rules for the Room.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingRulesApi apiInstance = new VideoV1RecordingRulesApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource where the recording rules to fetch apply.
    try {
      VideoV1RoomRoomRecordingRule result = apiInstance.fetchRoomRecordingRule(roomSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingRulesApi#fetchRoomRecordingRule");
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
| **roomSid** | **String**| The SID of the Room resource where the recording rules to fetch apply. | |

### Return type

[**VideoV1RoomRoomRecordingRule**](VideoV1RoomRoomRecordingRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRoomRecordingRule"></a>
# **updateRoomRecordingRule**
> VideoV1RoomRoomRecordingRule updateRoomRecordingRule(roomSid, rules)



Update the Recording Rules for the Room

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoV1RecordingRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://video.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VideoV1RecordingRulesApi apiInstance = new VideoV1RecordingRulesApi(defaultClient);
    String roomSid = "roomSid_example"; // String | The SID of the Room resource where the recording rules to update apply.
    Object rules = null; // Object | A JSON-encoded array of recording rules.
    try {
      VideoV1RoomRoomRecordingRule result = apiInstance.updateRoomRecordingRule(roomSid, rules);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoV1RecordingRulesApi#updateRoomRecordingRule");
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
| **roomSid** | **String**| The SID of the Room resource where the recording rules to update apply. | |
| **rules** | [**Object**](Object.md)| A JSON-encoded array of recording rules. | [optional] |

### Return type

[**VideoV1RoomRoomRecordingRule**](VideoV1RoomRoomRecordingRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

