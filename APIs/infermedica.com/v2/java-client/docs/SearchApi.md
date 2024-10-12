# SearchApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMatchingObservations**](SearchApi.md#getMatchingObservations) | **GET** /search | Find observations matching given phrase |


<a id="getMatchingObservations"></a>
# **getMatchingObservations**
> List&lt;SearchResult&gt; getMatchingObservations(phrase, sex, ageValue, ageUnit, maxResults, type)

Find observations matching given phrase

Returns list of observations matching the given phrase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String phrase = "phrase_example"; // String | phrase to match
    String sex = "male"; // String | sex filter
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    Integer maxResults = 8; // Integer | maximum number of results
    List<String> type = Arrays.asList(); // List<String> | type of results
    try {
      List<SearchResult> result = apiInstance.getMatchingObservations(phrase, sex, ageValue, ageUnit, maxResults, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getMatchingObservations");
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
| **maxResults** | **Integer**| maximum number of results | [optional] [default to 8] |
| **type** | [**List&lt;String&gt;**](String.md)| type of results | [optional] [enum: symptom, risk_factor, lab_test] |

### Return type

[**List&lt;SearchResult&gt;**](SearchResult.md)

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

