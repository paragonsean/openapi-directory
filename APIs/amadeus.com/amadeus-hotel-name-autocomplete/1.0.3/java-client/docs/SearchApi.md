# SearchApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gethotels**](SearchApi.md#gethotels) | **GET** /reference-data/locations/hotel | Returns a list of hotels matching a given keyword. |


<a id="gethotels"></a>
# **gethotels**
> Success gethotels(keyword, subType, countryCode, lang, max)

Returns a list of hotels matching a given keyword.

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
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String keyword = "PARI"; // String | Location query keyword
    List<String> subType = Arrays.asList(); // List<String> | Category of search - To enter several values, repeat the query parameter   Use HOTEL_LEISURE to target aggregators or HOTEL_GDS to target directly the chains
    String countryCode = "FR"; // String | The country in which you search the subType. Country Code in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format
    String lang = "EN"; // String | The language in which you want the results in following [ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1).   If the language entered is not available then the results will be shown in the default language, English.
    Integer max = 20; // Integer | The number of results requested from 1 to 20
    try {
      Success result = apiInstance.gethotels(keyword, subType, countryCode, lang, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#gethotels");
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
| **keyword** | **String**| Location query keyword | |
| **subType** | [**List&lt;String&gt;**](String.md)| Category of search - To enter several values, repeat the query parameter   Use HOTEL_LEISURE to target aggregators or HOTEL_GDS to target directly the chains | [enum: HOTEL_LEISURE, HOTEL_GDS] |
| **countryCode** | **String**| The country in which you search the subType. Country Code in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format | [optional] |
| **lang** | **String**| The language in which you want the results in following [ISO 639-1](https://fr.wikipedia.org/wiki/Liste_des_codes_ISO_639-1).   If the language entered is not available then the results will be shown in the default language, English. | [optional] [default to EN] |
| **max** | **Integer**| The number of results requested from 1 to 20 | [optional] [default to 20] |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Search Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | NOT FOUND  1797    | INVALID FORMAT 572     | INVALID LENGTH 32171   | MANDATORY DATA MISSING         |  -  |
| **500** | Unexpected Error |  -  |

