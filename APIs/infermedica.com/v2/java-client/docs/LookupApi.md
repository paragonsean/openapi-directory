# LookupApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMatchingObservation**](LookupApi.md#getMatchingObservation) | **GET** /lookup | Find observation matching given phrase |


<a id="getMatchingObservation"></a>
# **getMatchingObservation**
> SearchResult getMatchingObservation(phrase, sex, ageValue, ageUnit)

Find observation matching given phrase

Returns a single observation matching given phrase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String phrase = "phrase_example"; // String | phrase to match
    String sex = "male"; // String | sex filter
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    try {
      SearchResult result = apiInstance.getMatchingObservation(phrase, sex, ageValue, ageUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#getMatchingObservation");
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
| **phrase** | **String**| phrase to match | |
| **sex** | **String**| sex filter | [optional] [enum: male, female] |
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Phrase missing or invalid sex specified |  -  |
| **404** | No observation matches given phrase |  -  |

