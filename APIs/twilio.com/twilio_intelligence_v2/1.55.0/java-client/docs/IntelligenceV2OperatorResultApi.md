# IntelligenceV2OperatorResultApi

All URIs are relative to *https://intelligence.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchOperatorResult**](IntelligenceV2OperatorResultApi.md#fetchOperatorResult) | **GET** /v2/Transcripts/{TranscriptSid}/OperatorResults/{OperatorSid} |  |
| [**listOperatorResult**](IntelligenceV2OperatorResultApi.md#listOperatorResult) | **GET** /v2/Transcripts/{TranscriptSid}/OperatorResults |  |


<a id="fetchOperatorResult"></a>
# **fetchOperatorResult**
> IntelligenceV2TranscriptOperatorResult fetchOperatorResult(transcriptSid, operatorSid, redacted)



Fetch a specific Operator Result for the given Transcript.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2OperatorResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2OperatorResultApi apiInstance = new IntelligenceV2OperatorResultApi(defaultClient);
    String transcriptSid = "transcriptSid_example"; // String | A 34 character string that uniquely identifies this Transcript.
    String operatorSid = "operatorSid_example"; // String | A 34 character string that identifies this Language Understanding operator sid.
    Boolean redacted = true; // Boolean | Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
    try {
      IntelligenceV2TranscriptOperatorResult result = apiInstance.fetchOperatorResult(transcriptSid, operatorSid, redacted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2OperatorResultApi#fetchOperatorResult");
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
| **transcriptSid** | **String**| A 34 character string that uniquely identifies this Transcript. | |
| **operatorSid** | **String**| A 34 character string that identifies this Language Understanding operator sid. | |
| **redacted** | **Boolean**| Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True. | [optional] |

### Return type

[**IntelligenceV2TranscriptOperatorResult**](IntelligenceV2TranscriptOperatorResult.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listOperatorResult"></a>
# **listOperatorResult**
> ListOperatorResultResponse listOperatorResult(transcriptSid, redacted, pageSize, page, pageToken)



Retrieve a list of Operator Results for the given Transcript.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2OperatorResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2OperatorResultApi apiInstance = new IntelligenceV2OperatorResultApi(defaultClient);
    String transcriptSid = "transcriptSid_example"; // String | A 34 character string that uniquely identifies this Transcript.
    Boolean redacted = true; // Boolean | Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListOperatorResultResponse result = apiInstance.listOperatorResult(transcriptSid, redacted, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2OperatorResultApi#listOperatorResult");
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
| **transcriptSid** | **String**| A 34 character string that uniquely identifies this Transcript. | |
| **redacted** | **Boolean**| Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListOperatorResultResponse**](ListOperatorResultResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

