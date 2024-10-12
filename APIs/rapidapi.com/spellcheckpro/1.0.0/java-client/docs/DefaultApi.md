# DefaultApi

All URIs are relative to *https://spellcheckpro.p.rapidapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkSpellingRussian**](DefaultApi.md#checkSpellingRussian) | **POST** /check_spelling | Check Spelling (Russian) |


<a id="checkSpellingRussian"></a>
# **checkSpellingRussian**
> checkSpellingRussian(xRapidAPIKey, checkSpellingRussianRequest)

Check Spelling (Russian)

Check Spelling (Russian)

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
    defaultClient.setBasePath("https://spellcheckpro.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xRapidAPIKey = ""; // String | 
    CheckSpellingRussianRequest checkSpellingRussianRequest = new CheckSpellingRussianRequest(); // CheckSpellingRussianRequest | 
    try {
      apiInstance.checkSpellingRussian(xRapidAPIKey, checkSpellingRussianRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#checkSpellingRussian");
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
| **xRapidAPIKey** | **String**|  | [optional] |
| **checkSpellingRussianRequest** | [**CheckSpellingRussianRequest**](CheckSpellingRussianRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

