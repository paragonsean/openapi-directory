# MediaV1MediaRecordingApi

All URIs are relative to *https://media.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMediaRecording**](MediaV1MediaRecordingApi.md#deleteMediaRecording) | **DELETE** /v1/MediaRecordings/{Sid} |  |
| [**fetchMediaRecording**](MediaV1MediaRecordingApi.md#fetchMediaRecording) | **GET** /v1/MediaRecordings/{Sid} |  |
| [**listMediaRecording**](MediaV1MediaRecordingApi.md#listMediaRecording) | **GET** /v1/MediaRecordings |  |


<a id="deleteMediaRecording"></a>
# **deleteMediaRecording**
> deleteMediaRecording(sid)



Deletes a MediaRecording resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaRecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaRecordingApi apiInstance = new MediaV1MediaRecordingApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the MediaRecording resource to delete.
    try {
      apiInstance.deleteMediaRecording(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaRecordingApi#deleteMediaRecording");
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
| **sid** | **String**| The SID of the MediaRecording resource to delete. | |

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

<a id="fetchMediaRecording"></a>
# **fetchMediaRecording**
> MediaV1MediaRecording fetchMediaRecording(sid)



Returns a single MediaRecording resource identified by a SID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaRecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaRecordingApi apiInstance = new MediaV1MediaRecordingApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the MediaRecording resource to fetch.
    try {
      MediaV1MediaRecording result = apiInstance.fetchMediaRecording(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaRecordingApi#fetchMediaRecording");
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
| **sid** | **String**| The SID of the MediaRecording resource to fetch. | |

### Return type

[**MediaV1MediaRecording**](MediaV1MediaRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMediaRecording"></a>
# **listMediaRecording**
> ListMediaRecordingResponse listMediaRecording(order, status, processorSid, sourceSid, pageSize, page, pageToken)



Returns a list of MediaRecordings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaV1MediaRecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://media.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MediaV1MediaRecordingApi apiInstance = new MediaV1MediaRecordingApi(defaultClient);
    MediaRecordingEnumOrder order = MediaRecordingEnumOrder.fromValue("asc"); // MediaRecordingEnumOrder | The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
    MediaRecordingEnumStatus status = MediaRecordingEnumStatus.fromValue("processing"); // MediaRecordingEnumStatus | Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
    String processorSid = "processorSid_example"; // String | SID of a MediaProcessor to filter by.
    String sourceSid = "sourceSid_example"; // String | SID of a MediaRecording source to filter by.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMediaRecordingResponse result = apiInstance.listMediaRecording(order, status, processorSid, sourceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaV1MediaRecordingApi#listMediaRecording");
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
| **order** | **MediaRecordingEnumOrder**| The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default. | [optional] [enum: asc, desc] |
| **status** | **MediaRecordingEnumStatus**| Status to filter by, with possible values &#x60;processing&#x60;, &#x60;completed&#x60;, &#x60;deleted&#x60;, or &#x60;failed&#x60;. | [optional] [enum: processing, completed, deleted, failed] |
| **processorSid** | **String**| SID of a MediaProcessor to filter by. | [optional] |
| **sourceSid** | **String**| SID of a MediaRecording source to filter by. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMediaRecordingResponse**](ListMediaRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

