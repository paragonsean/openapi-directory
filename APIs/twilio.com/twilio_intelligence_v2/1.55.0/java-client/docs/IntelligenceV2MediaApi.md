# IntelligenceV2MediaApi

All URIs are relative to *https://intelligence.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchMedia**](IntelligenceV2MediaApi.md#fetchMedia) | **GET** /v2/Transcripts/{Sid}/Media |  |


<a id="fetchMedia"></a>
# **fetchMedia**
> IntelligenceV2TranscriptMedia fetchMedia(sid, redacted)



Get download URLs for media if possible

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntelligenceV2MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://intelligence.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IntelligenceV2MediaApi apiInstance = new IntelligenceV2MediaApi(defaultClient);
    String sid = "sid_example"; // String | The unique SID identifier of the Transcript.
    Boolean redacted = true; // Boolean | Grant access to PII Redacted/Unredacted Media. If redaction is enabled, the default is `true` to access redacted media.
    try {
      IntelligenceV2TranscriptMedia result = apiInstance.fetchMedia(sid, redacted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntelligenceV2MediaApi#fetchMedia");
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
| **sid** | **String**| The unique SID identifier of the Transcript. | |
| **redacted** | **Boolean**| Grant access to PII Redacted/Unredacted Media. If redaction is enabled, the default is &#x60;true&#x60; to access redacted media. | [optional] |

### Return type

[**IntelligenceV2TranscriptMedia**](IntelligenceV2TranscriptMedia.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

