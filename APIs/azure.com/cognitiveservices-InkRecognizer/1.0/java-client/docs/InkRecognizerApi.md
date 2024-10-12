# InkRecognizerApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**inkRecognizerRecognize**](InkRecognizerApi.md#inkRecognizerRecognize) | **PUT** /recognize |  |


<a id="inkRecognizerRecognize"></a>
# **inkRecognizerRecognize**
> AnalysisResponse inkRecognizerRecognize(body, xMsClientRequestId)



Ink Recognition operation is used to perform ink layout and recognition of written words and shapes. It allows passing the ink strokes to the service to get the recognition results in the response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InkRecognizerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    InkRecognizerApi apiInstance = new InkRecognizerApi(defaultClient);
    AnalysisRequest body = new AnalysisRequest(); // AnalysisRequest | The collection of stroke objects to send for analysis
    String xMsClientRequestId = "xMsClientRequestId_example"; // String | The request id used to uniquely identify each request during troubleshooting. This is an optional parameter useful for correlating logs and other artifacts.
    try {
      AnalysisResponse result = apiInstance.inkRecognizerRecognize(body, xMsClientRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InkRecognizerApi#inkRecognizerRecognize");
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
| **body** | [**AnalysisRequest**](AnalysisRequest.md)| The collection of stroke objects to send for analysis | |
| **xMsClientRequestId** | **String**| The request id used to uniquely identify each request during troubleshooting. This is an optional parameter useful for correlating logs and other artifacts. | [optional] |

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The results were processed successfully. |  -  |
| **0** | unexpected error |  -  |

