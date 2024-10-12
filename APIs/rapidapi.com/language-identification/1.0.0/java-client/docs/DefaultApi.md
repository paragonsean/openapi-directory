# DefaultApi

All URIs are relative to *https://language-identification-prediction.p.rapidapi.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recognizeLanguagePost**](DefaultApi.md#recognizeLanguagePost) | **POST** /recognize-language/ | Recognize Language |


<a id="recognizeLanguagePost"></a>
# **recognizeLanguagePost**
> recognizeLanguagePost(xRapidAPIHost, xRapidAPIKey, text)

Recognize Language

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://language-identification-prediction.p.rapidapi.com/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xRapidAPIHost = "language-identification-prediction.p.rapidapi.com"; // String | 
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | 
    String text = "text_example"; // String | text
    try {
      apiInstance.recognizeLanguagePost(xRapidAPIHost, xRapidAPIKey, text);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizeLanguagePost");
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
| **xRapidAPIHost** | **String**|  | [default to language-identification-prediction.p.rapidapi.com] |
| **xRapidAPIKey** | **String**|  | |
| **text** | **String**| text | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

