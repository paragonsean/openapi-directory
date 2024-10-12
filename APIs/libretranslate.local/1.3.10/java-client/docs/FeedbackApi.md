# FeedbackApi

All URIs are relative to *http://libretranslate.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**suggestPost**](FeedbackApi.md#suggestPost) | **POST** /suggest | Submit a suggestion to improve a translation |


<a id="suggestPost"></a>
# **suggestPost**
> SuggestResponse suggestPost()

Submit a suggestion to improve a translation



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://libretranslate.local");

    FeedbackApi apiInstance = new FeedbackApi(defaultClient);
    try {
      SuggestResponse result = apiInstance.suggestPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeedbackApi#suggestPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SuggestResponse**](SuggestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not authorized |  -  |

