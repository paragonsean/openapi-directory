# RecommendedLocationsApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRecommendedLocation**](RecommendedLocationsApi.md#getRecommendedLocation) | **GET** /reference-data/recommended-locations | GET recommended destinations |


<a id="getRecommendedLocation"></a>
# **getRecommendedLocation**
> GetRecommendedLocation200Response getRecommendedLocation(cityCodes, travelerCountryCode, destinationCountryCodes)

GET recommended destinations



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendedLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    RecommendedLocationsApi apiInstance = new RecommendedLocationsApi(defaultClient);
    String cityCodes = "PAR"; // String | City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx)
    String travelerCountryCode = "FR"; // String | Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US)
    String destinationCountryCodes = "destinationCountryCodes_example"; // String | List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US)
    try {
      GetRecommendedLocation200Response result = apiInstance.getRecommendedLocation(cityCodes, travelerCountryCode, destinationCountryCodes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendedLocationsApi#getRecommendedLocation");
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
| **cityCodes** | **String**| City used by the algorythm to recommend new destination. Several cities can be specified using comma.  City codes follow [IATA standard](http://www.iata.org/publications/Pages/code-search.aspx) | |
| **travelerCountryCode** | **String**| Origin country of the traveler following [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) | [optional] [default to FR] |
| **destinationCountryCodes** | **String**| List of country the traveler want to visit, separated with comma.  Country codes follow [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code format (e.g. US) | [optional] |

### Return type

[**GetRecommendedLocation200Response**](GetRecommendedLocation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful reply |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION                             32171   | MANDATORY DATA MISSING  |  -  |
| **500** | Internal Server Error |  -  |

