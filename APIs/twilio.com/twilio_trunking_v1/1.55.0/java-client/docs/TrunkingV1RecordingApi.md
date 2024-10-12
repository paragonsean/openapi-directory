# TrunkingV1RecordingApi

All URIs are relative to *https://trunking.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchRecording**](TrunkingV1RecordingApi.md#fetchRecording) | **GET** /v1/Trunks/{TrunkSid}/Recording |  |
| [**updateRecording**](TrunkingV1RecordingApi.md#updateRecording) | **POST** /v1/Trunks/{TrunkSid}/Recording |  |


<a id="fetchRecording"></a>
# **fetchRecording**
> TrunkingV1TrunkRecording fetchRecording(trunkSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1RecordingApi apiInstance = new TrunkingV1RecordingApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the recording settings.
    try {
      TrunkingV1TrunkRecording result = apiInstance.fetchRecording(trunkSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1RecordingApi#fetchRecording");
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
| **trunkSid** | **String**| The SID of the Trunk from which to fetch the recording settings. | |

### Return type

[**TrunkingV1TrunkRecording**](TrunkingV1TrunkRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateRecording"></a>
# **updateRecording**
> TrunkingV1TrunkRecording updateRecording(trunkSid, mode, trim)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1RecordingApi apiInstance = new TrunkingV1RecordingApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk that will have its recording settings updated.
    RecordingEnumRecordingMode mode = RecordingEnumRecordingMode.fromValue("do-not-record"); // RecordingEnumRecordingMode | 
    RecordingEnumRecordingTrim trim = RecordingEnumRecordingTrim.fromValue("trim-silence"); // RecordingEnumRecordingTrim | 
    try {
      TrunkingV1TrunkRecording result = apiInstance.updateRecording(trunkSid, mode, trim);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1RecordingApi#updateRecording");
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
| **trunkSid** | **String**| The SID of the Trunk that will have its recording settings updated. | |
| **mode** | **RecordingEnumRecordingMode**|  | [optional] [enum: do-not-record, record-from-ringing, record-from-answer, record-from-ringing-dual, record-from-answer-dual] |
| **trim** | **RecordingEnumRecordingTrim**|  | [optional] [enum: trim-silence, do-not-trim] |

### Return type

[**TrunkingV1TrunkRecording**](TrunkingV1TrunkRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

