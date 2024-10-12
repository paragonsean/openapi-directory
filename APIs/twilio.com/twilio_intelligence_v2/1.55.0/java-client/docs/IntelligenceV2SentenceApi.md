# IntelligenceV2SentenceApi

All URIs are relative to *https://intelligence.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSentence**](IntelligenceV2SentenceApi.md#listSentence) | **GET** /v2/Transcripts/{TranscriptSid}/Sentences |  |


<a id="listSentence"></a>
# **listSentence**
> ListSentenceResponse listSentence(transcriptSid, redacted, pageSize, page, pageToken)



Get all Transcript Sentences by TranscriptSid

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2SentenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2SentenceApi apiInstance = new IntelligenceV2SentenceApi(defaultClient);
    String transcriptSid = "transcriptSid_example"; // String | The unique SID identifier of the Transcript.
    Boolean redacted = true; // Boolean | Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSentenceResponse result = apiInstance.listSentence(transcriptSid, redacted, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2SentenceApi#listSentence");
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
| **transcriptSid** | **String**| The unique SID identifier of the Transcript. | |
| **redacted** | **Boolean**| Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is &#x60;true&#x60; to access redacted sentences. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSentenceResponse**](ListSentenceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

