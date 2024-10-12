# IntelligenceV2TranscriptApi

All URIs are relative to *https://intelligence.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTranscript**](IntelligenceV2TranscriptApi.md#createTranscript) | **POST** /v2/Transcripts |  |
| [**deleteTranscript**](IntelligenceV2TranscriptApi.md#deleteTranscript) | **DELETE** /v2/Transcripts/{Sid} |  |
| [**fetchTranscript**](IntelligenceV2TranscriptApi.md#fetchTranscript) | **GET** /v2/Transcripts/{Sid} |  |
| [**listTranscript**](IntelligenceV2TranscriptApi.md#listTranscript) | **GET** /v2/Transcripts |  |


<a id="createTranscript"></a>
# **createTranscript**
> IntelligenceV2Transcript createTranscript(channel, serviceSid, customerKey, mediaStartTime)



Create a new Transcript for the service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2TranscriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2TranscriptApi apiInstance = new IntelligenceV2TranscriptApi(defaultClient);
    Object channel = null; // Object | JSON object describing Media Channel including Source and Participants
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    String customerKey = "customerKey_example"; // String | Used to store client provided metadata. Maximum of 64 double-byte UTF8 characters.
    OffsetDateTime mediaStartTime = OffsetDateTime.now(); // OffsetDateTime | The date that this Transcript's media was started, given in ISO 8601 format.
    try {
      IntelligenceV2Transcript result = apiInstance.createTranscript(channel, serviceSid, customerKey, mediaStartTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2TranscriptApi#createTranscript");
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
| **channel** | [**Object**](Object.md)| JSON object describing Media Channel including Source and Participants | |
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **customerKey** | **String**| Used to store client provided metadata. Maximum of 64 double-byte UTF8 characters. | [optional] |
| **mediaStartTime** | **OffsetDateTime**| The date that this Transcript&#39;s media was started, given in ISO 8601 format. | [optional] |

### Return type

[**IntelligenceV2Transcript**](IntelligenceV2Transcript.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

<a id="deleteTranscript"></a>
# **deleteTranscript**
> deleteTranscript(sid)



Delete a specific Transcript.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2TranscriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2TranscriptApi apiInstance = new IntelligenceV2TranscriptApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Transcript.
    try {
      apiInstance.deleteTranscript(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2TranscriptApi#deleteTranscript");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Transcript. | |

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

<a id="fetchTranscript"></a>
# **fetchTranscript**
> IntelligenceV2Transcript fetchTranscript(sid)



Fetch a specific Transcript.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2TranscriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2TranscriptApi apiInstance = new IntelligenceV2TranscriptApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Transcript.
    try {
      IntelligenceV2Transcript result = apiInstance.fetchTranscript(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2TranscriptApi#fetchTranscript");
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
| **sid** | **String**| A 34 character string that uniquely identifies this Transcript. | |

### Return type

[**IntelligenceV2Transcript**](IntelligenceV2Transcript.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTranscript"></a>
# **listTranscript**
> ListTranscriptResponse listTranscript(serviceSid, beforeStartTime, afterStartTime, beforeDateCreated, afterDateCreated, status, languageCode, sourceSid, pageSize, page, pageToken)



Retrieve a list of Transcripts for a given service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2TranscriptApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2TranscriptApi apiInstance = new IntelligenceV2TranscriptApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    String beforeStartTime = "beforeStartTime_example"; // String | Filter by before StartTime.
    String afterStartTime = "afterStartTime_example"; // String | Filter by after StartTime.
    String beforeDateCreated = "beforeDateCreated_example"; // String | Filter by before DateCreated.
    String afterDateCreated = "afterDateCreated_example"; // String | Filter by after DateCreated.
    String status = "status_example"; // String | Filter by status.
    String languageCode = "languageCode_example"; // String | Filter by Language Code.
    String sourceSid = "sourceSid_example"; // String | Filter by SourceSid.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTranscriptResponse result = apiInstance.listTranscript(serviceSid, beforeStartTime, afterStartTime, beforeDateCreated, afterDateCreated, status, languageCode, sourceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2TranscriptApi#listTranscript");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | [optional] |
| **beforeStartTime** | **String**| Filter by before StartTime. | [optional] |
| **afterStartTime** | **String**| Filter by after StartTime. | [optional] |
| **beforeDateCreated** | **String**| Filter by before DateCreated. | [optional] |
| **afterDateCreated** | **String**| Filter by after DateCreated. | [optional] |
| **status** | **String**| Filter by status. | [optional] |
| **languageCode** | **String**| Filter by Language Code. | [optional] |
| **sourceSid** | **String**| Filter by SourceSid. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTranscriptResponse**](ListTranscriptResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

