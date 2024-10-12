# Api20100401RecordingApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCallRecording**](Api20100401RecordingApi.md#createCallRecording) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json |  |
| [**deleteCallRecording**](Api20100401RecordingApi.md#deleteCallRecording) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json |  |
| [**deleteConferenceRecording**](Api20100401RecordingApi.md#deleteConferenceRecording) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json |  |
| [**deleteRecording**](Api20100401RecordingApi.md#deleteRecording) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json |  |
| [**fetchCallRecording**](Api20100401RecordingApi.md#fetchCallRecording) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json |  |
| [**fetchConferenceRecording**](Api20100401RecordingApi.md#fetchConferenceRecording) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json |  |
| [**fetchRecording**](Api20100401RecordingApi.md#fetchRecording) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json |  |
| [**listCallRecording**](Api20100401RecordingApi.md#listCallRecording) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json |  |
| [**listConferenceRecording**](Api20100401RecordingApi.md#listConferenceRecording) | **GET** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json |  |
| [**listRecording**](Api20100401RecordingApi.md#listRecording) | **GET** /2010-04-01/Accounts/{AccountSid}/Recordings.json |  |
| [**updateCallRecording**](Api20100401RecordingApi.md#updateCallRecording) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json |  |
| [**updateConferenceRecording**](Api20100401RecordingApi.md#updateConferenceRecording) | **POST** /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json |  |


<a id="createCallRecording"></a>
# **createCallRecording**
> ApiV2010AccountCallCallRecording createCallRecording(accountSid, callSid, recordingChannels, recordingStatusCallback, recordingStatusCallbackEvent, recordingStatusCallbackMethod, recordingTrack, trim)



Create a recording for the call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) to associate the resource with.
    String recordingChannels = "recordingChannels_example"; // String | The number of channels used in the recording. Can be: `mono` or `dual` and the default is `mono`. `mono` records all parties of the call into one channel. `dual` records each party of a 2-party call into separate channels.
    URI recordingStatusCallback = new URI(); // URI | The URL we should call using the `recording_status_callback_method` on each recording event specified in  `recording_status_callback_event`. For more information, see [RecordingStatusCallback parameters](https://www.twilio.com/docs/voice/api/recording#recordingstatuscallback).
    List<String> recordingStatusCallbackEvent = Arrays.asList(); // List<String> | The recording status events on which we should call the `recording_status_callback` URL. Can be: `in-progress`, `completed` and `absent` and the default is `completed`. Separate multiple event values with a space.
    String recordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `recording_status_callback`. Can be: `GET` or `POST` and the default is `POST`.
    String recordingTrack = "recordingTrack_example"; // String | The audio track to record for the call. Can be: `inbound`, `outbound` or `both`. The default is `both`. `inbound` records the audio that is received by Twilio. `outbound` records the audio that is generated from Twilio. `both` records the audio that is received and generated by Twilio.
    String trim = "trim_example"; // String | Whether to trim any leading and trailing silence in the recording. Can be: `trim-silence` or `do-not-trim` and the default is `do-not-trim`. `trim-silence` trims the silence from the beginning and end of the recording and `do-not-trim` does not.
    try {
      ApiV2010AccountCallCallRecording result = apiInstance.createCallRecording(accountSid, callSid, recordingChannels, recordingStatusCallback, recordingStatusCallbackEvent, recordingStatusCallbackMethod, recordingTrack, trim);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#createCallRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) to associate the resource with. | |
| **recordingChannels** | **String**| The number of channels used in the recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. &#x60;mono&#x60; records all parties of the call into one channel. &#x60;dual&#x60; records each party of a 2-party call into separate channels. | [optional] |
| **recordingStatusCallback** | **URI**| The URL we should call using the &#x60;recording_status_callback_method&#x60; on each recording event specified in  &#x60;recording_status_callback_event&#x60;. For more information, see [RecordingStatusCallback parameters](https://www.twilio.com/docs/voice/api/recording#recordingstatuscallback). | [optional] |
| **recordingStatusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The recording status events on which we should call the &#x60;recording_status_callback&#x60; URL. Can be: &#x60;in-progress&#x60;, &#x60;completed&#x60; and &#x60;absent&#x60; and the default is &#x60;completed&#x60;. Separate multiple event values with a space. | [optional] |
| **recordingStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **recordingTrack** | **String**| The audio track to record for the call. Can be: &#x60;inbound&#x60;, &#x60;outbound&#x60; or &#x60;both&#x60;. The default is &#x60;both&#x60;. &#x60;inbound&#x60; records the audio that is received by Twilio. &#x60;outbound&#x60; records the audio that is generated from Twilio. &#x60;both&#x60; records the audio that is received and generated by Twilio. | [optional] |
| **trim** | **String**| Whether to trim any leading and trailing silence in the recording. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and the default is &#x60;do-not-trim&#x60;. &#x60;trim-silence&#x60; trims the silence from the beginning and end of the recording and &#x60;do-not-trim&#x60; does not. | [optional] |

### Return type

[**ApiV2010AccountCallCallRecording**](ApiV2010AccountCallCallRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteCallRecording"></a>
# **deleteCallRecording**
> deleteCallRecording(accountSid, callSid, sid)



Delete a recording from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording resource to delete.
    try {
      apiInstance.deleteCallRecording(accountSid, callSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#deleteCallRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording resource to delete. | |

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

<a id="deleteConferenceRecording"></a>
# **deleteConferenceRecording**
> deleteConferenceRecording(accountSid, conferenceSid, sid)



Delete a recording from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to delete.
    String conferenceSid = "conferenceSid_example"; // String | The Conference SID that identifies the conference associated with the recording to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Conference Recording resource to delete.
    try {
      apiInstance.deleteConferenceRecording(accountSid, conferenceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#deleteConferenceRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to delete. | |
| **conferenceSid** | **String**| The Conference SID that identifies the conference associated with the recording to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Conference Recording resource to delete. | |

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

<a id="deleteRecording"></a>
# **deleteRecording**
> deleteRecording(accountSid, sid)



Delete a recording from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording resource to delete.
    try {
      apiInstance.deleteRecording(accountSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#deleteRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording resource to delete. | |

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

<a id="fetchCallRecording"></a>
# **fetchCallRecording**
> ApiV2010AccountCallCallRecording fetchCallRecording(accountSid, callSid, sid)



Fetch an instance of a recording for a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording resource to fetch.
    try {
      ApiV2010AccountCallCallRecording result = apiInstance.fetchCallRecording(accountSid, callSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#fetchCallRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording resource to fetch. | |

### Return type

[**ApiV2010AccountCallCallRecording**](ApiV2010AccountCallCallRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchConferenceRecording"></a>
# **fetchConferenceRecording**
> ApiV2010AccountConferenceConferenceRecording fetchConferenceRecording(accountSid, conferenceSid, sid)



Fetch an instance of a recording for a call

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to fetch.
    String conferenceSid = "conferenceSid_example"; // String | The Conference SID that identifies the conference associated with the recording to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch.
    try {
      ApiV2010AccountConferenceConferenceRecording result = apiInstance.fetchConferenceRecording(accountSid, conferenceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#fetchConferenceRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to fetch. | |
| **conferenceSid** | **String**| The Conference SID that identifies the conference associated with the recording to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Conference Recording resource to fetch. | |

### Return type

[**ApiV2010AccountConferenceConferenceRecording**](ApiV2010AccountConferenceConferenceRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchRecording"></a>
# **fetchRecording**
> ApiV2010AccountRecording fetchRecording(accountSid, sid, includeSoftDeleted)



Fetch an instance of a recording

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording resource to fetch.
    Boolean includeSoftDeleted = true; // Boolean | A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.
    try {
      ApiV2010AccountRecording result = apiInstance.fetchRecording(accountSid, sid, includeSoftDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#fetchRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording resource to fetch. | |
| **includeSoftDeleted** | **Boolean**| A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days. | [optional] |

### Return type

[**ApiV2010AccountRecording**](ApiV2010AccountRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listCallRecording"></a>
# **listCallRecording**
> ListCallRecordingResponse listCallRecording(accountSid, callSid, dateCreated, dateCreatedLessThan, dateCreatedGreaterThan, pageSize, page, pageToken)



Retrieve a list of recordings belonging to the call used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.
    LocalDate dateCreated = LocalDate.now(); // LocalDate | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
    LocalDate dateCreatedLessThan = LocalDate.now(); // LocalDate | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
    LocalDate dateCreatedGreaterThan = LocalDate.now(); // LocalDate | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListCallRecordingResponse result = apiInstance.listCallRecording(accountSid, callSid, dateCreated, dateCreatedLessThan, dateCreatedGreaterThan, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#listCallRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read. | |
| **dateCreated** | **LocalDate**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional] |
| **dateCreatedLessThan** | **LocalDate**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional] |
| **dateCreatedGreaterThan** | **LocalDate**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListCallRecordingResponse**](ListCallRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listConferenceRecording"></a>
# **listConferenceRecording**
> ListConferenceRecordingResponse listConferenceRecording(accountSid, conferenceSid, dateCreated, dateCreatedLessThan, dateCreatedGreaterThan, pageSize, page, pageToken)



Retrieve a list of recordings belonging to the call used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to read.
    String conferenceSid = "conferenceSid_example"; // String | The Conference SID that identifies the conference associated with the recording to read.
    LocalDate dateCreated = LocalDate.now(); // LocalDate | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
    LocalDate dateCreatedLessThan = LocalDate.now(); // LocalDate | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
    LocalDate dateCreatedGreaterThan = LocalDate.now(); // LocalDate | The `date_created` value, specified as `YYYY-MM-DD`, of the resources to read. You can also specify inequality: `DateCreated<=YYYY-MM-DD` will return recordings generated at or before midnight on a given date, and `DateCreated>=YYYY-MM-DD` returns recordings generated at or after midnight on a date.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListConferenceRecordingResponse result = apiInstance.listConferenceRecording(accountSid, conferenceSid, dateCreated, dateCreatedLessThan, dateCreatedGreaterThan, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#listConferenceRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resources to read. | |
| **conferenceSid** | **String**| The Conference SID that identifies the conference associated with the recording to read. | |
| **dateCreated** | **LocalDate**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional] |
| **dateCreatedLessThan** | **LocalDate**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional] |
| **dateCreatedGreaterThan** | **LocalDate**| The &#x60;date_created&#x60; value, specified as &#x60;YYYY-MM-DD&#x60;, of the resources to read. You can also specify inequality: &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60; will return recordings generated at or before midnight on a given date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; returns recordings generated at or after midnight on a date. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListConferenceRecordingResponse**](ListConferenceRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRecording"></a>
# **listRecording**
> ListRecordingResponse listRecording(accountSid, dateCreated, dateCreatedLessThan, dateCreatedGreaterThan, callSid, conferenceSid, includeSoftDeleted, pageSize, page, pageToken)



Retrieve a list of recordings belonging to the account used to make the request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
    OffsetDateTime dateCreatedLessThan = OffsetDateTime.now(); // OffsetDateTime | Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
    OffsetDateTime dateCreatedGreaterThan = OffsetDateTime.now(); // OffsetDateTime | Only include recordings that were created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read recordings that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read recordings that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read recordings that were created on or after midnight of this date.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read.
    String conferenceSid = "conferenceSid_example"; // String | The Conference SID that identifies the conference associated with the recording to read.
    Boolean includeSoftDeleted = true; // Boolean | A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListRecordingResponse result = apiInstance.listRecording(accountSid, dateCreated, dateCreatedLessThan, dateCreatedGreaterThan, callSid, conferenceSid, includeSoftDeleted, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#listRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resources to read. | |
| **dateCreated** | **OffsetDateTime**| Only include recordings that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read recordings that were created on this date. You can also specify an inequality, such as &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60;, to read recordings that were created on or before midnight of this date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; to read recordings that were created on or after midnight of this date. | [optional] |
| **dateCreatedLessThan** | **OffsetDateTime**| Only include recordings that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read recordings that were created on this date. You can also specify an inequality, such as &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60;, to read recordings that were created on or before midnight of this date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; to read recordings that were created on or after midnight of this date. | [optional] |
| **dateCreatedGreaterThan** | **OffsetDateTime**| Only include recordings that were created on this date. Specify a date as &#x60;YYYY-MM-DD&#x60; in GMT, for example: &#x60;2009-07-06&#x60;, to read recordings that were created on this date. You can also specify an inequality, such as &#x60;DateCreated&lt;&#x3D;YYYY-MM-DD&#x60;, to read recordings that were created on or before midnight of this date, and &#x60;DateCreated&gt;&#x3D;YYYY-MM-DD&#x60; to read recordings that were created on or after midnight of this date. | [optional] |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resources to read. | [optional] |
| **conferenceSid** | **String**| The Conference SID that identifies the conference associated with the recording to read. | [optional] |
| **includeSoftDeleted** | **Boolean**| A boolean parameter indicating whether to retrieve soft deleted recordings or not. Recordings metadata are kept after deletion for a retention period of 40 days. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListRecordingResponse**](ListRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCallRecording"></a>
# **updateCallRecording**
> ApiV2010AccountCallCallRecording updateCallRecording(accountSid, callSid, sid, status, pauseBehavior)



Changes the status of the recording to paused, stopped, or in-progress. Note: Pass &#x60;Twilio.CURRENT&#x60; instead of recording sid to reference current active recording.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to update.
    String callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Recording resource to update.
    CallRecordingEnumStatus status = CallRecordingEnumStatus.fromValue("in-progress"); // CallRecordingEnumStatus | 
    String pauseBehavior = "pauseBehavior_example"; // String | Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.
    try {
      ApiV2010AccountCallCallRecording result = apiInstance.updateCallRecording(accountSid, callSid, sid, status, pauseBehavior);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#updateCallRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource to update. | |
| **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Recording resource to update. | |
| **status** | **CallRecordingEnumStatus**|  | [enum: in-progress, paused, stopped, processing, completed, absent] |
| **pauseBehavior** | **String**| Whether to record during a pause. Can be: &#x60;skip&#x60; or &#x60;silence&#x60; and the default is &#x60;silence&#x60;. &#x60;skip&#x60; does not record during the pause period, while &#x60;silence&#x60; will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting &#x60;status&#x60; is set to &#x60;paused&#x60;. | [optional] |

### Return type

[**ApiV2010AccountCallCallRecording**](ApiV2010AccountCallCallRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateConferenceRecording"></a>
# **updateConferenceRecording**
> ApiV2010AccountConferenceConferenceRecording updateConferenceRecording(accountSid, conferenceSid, sid, status, pauseBehavior)



Changes the status of the recording to paused, stopped, or in-progress. Note: To use &#x60;Twilio.CURRENT&#x60;, pass it as recording sid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401RecordingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401RecordingApi apiInstance = new Api20100401RecordingApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to update.
    String conferenceSid = "conferenceSid_example"; // String | The Conference SID that identifies the conference associated with the recording to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use `Twilio.CURRENT` to reference the current active recording.
    ConferenceRecordingEnumStatus status = ConferenceRecordingEnumStatus.fromValue("in-progress"); // ConferenceRecordingEnumStatus | 
    String pauseBehavior = "pauseBehavior_example"; // String | Whether to record during a pause. Can be: `skip` or `silence` and the default is `silence`. `skip` does not record during the pause period, while `silence` will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting `status` is set to `paused`.
    try {
      ApiV2010AccountConferenceConferenceRecording result = apiInstance.updateConferenceRecording(accountSid, conferenceSid, sid, status, pauseBehavior);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401RecordingApi#updateConferenceRecording");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Conference Recording resource to update. | |
| **conferenceSid** | **String**| The Conference SID that identifies the conference associated with the recording to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Conference Recording resource to update. Use &#x60;Twilio.CURRENT&#x60; to reference the current active recording. | |
| **status** | **ConferenceRecordingEnumStatus**|  | [enum: in-progress, paused, stopped, processing, completed, absent] |
| **pauseBehavior** | **String**| Whether to record during a pause. Can be: &#x60;skip&#x60; or &#x60;silence&#x60; and the default is &#x60;silence&#x60;. &#x60;skip&#x60; does not record during the pause period, while &#x60;silence&#x60; will replace the actual audio of the call with silence during the pause period. This parameter only applies when setting &#x60;status&#x60; is set to &#x60;paused&#x60;. | [optional] |

### Return type

[**ApiV2010AccountConferenceConferenceRecording**](ApiV2010AccountConferenceConferenceRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

