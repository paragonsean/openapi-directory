# ContentproSimilarTextApi

All URIs are relative to *https://api.byautomata.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**contentproSimilarTextPost**](ContentproSimilarTextApi.md#contentproSimilarTextPost) | **POST** /contentpro-similar-text | The /contentpro-similar-text endpoint accepts and arbitrary piece of text and returns similar articles and blogs written by companies. |


<a id="contentproSimilarTextPost"></a>
# **contentproSimilarTextPost**
> ContentproSearchGet200Response contentproSimilarTextPost(contentproSimilarTextPostRequest)

The /contentpro-similar-text endpoint accepts and arbitrary piece of text and returns similar articles and blogs written by companies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentproSimilarTextApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.byautomata.io");

    ContentproSimilarTextApi apiInstance = new ContentproSimilarTextApi(defaultClient);
    ContentproSimilarTextPostRequest contentproSimilarTextPostRequest = new ContentproSimilarTextPostRequest(); // ContentproSimilarTextPostRequest | We'll provide information about related companies and articles based on the text you provide.
    try {
      ContentproSearchGet200Response result = apiInstance.contentproSimilarTextPost(contentproSimilarTextPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentproSimilarTextApi#contentproSimilarTextPost");
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
| **contentproSimilarTextPostRequest** | [**ContentproSimilarTextPostRequest**](ContentproSimilarTextPostRequest.md)| We&#39;ll provide information about related companies and articles based on the text you provide. | |

### Return type

[**ContentproSearchGet200Response**](ContentproSearchGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation |  -  |
| **400** | Your request was not valid. Please refer to the API documentation https://api-specs.byautomata.io. |  -  |
| **403** | Invalid API Key. Please refer to the API documentation https://api-specs.byautomata.io. |  -  |
| **501** | There was a server error. Please try again later or contact support@byautomata.io |  -  |

