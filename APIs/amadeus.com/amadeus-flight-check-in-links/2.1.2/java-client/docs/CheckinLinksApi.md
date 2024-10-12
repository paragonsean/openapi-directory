# CheckinLinksApi

All URIs are relative to *https://test.api.amadeus.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCheckinURLs**](CheckinLinksApi.md#getCheckinURLs) | **GET** /reference-data/urls/checkin-links | Lists Check-in URLs. |


<a id="getCheckinURLs"></a>
# **getCheckinURLs**
> Success getCheckinURLs(airlineCode, language)

Lists Check-in URLs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CheckinLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v2");

    CheckinLinksApi apiInstance = new CheckinLinksApi(defaultClient);
    String airlineCode = "BA"; // String | Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)  [ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes) 
    String language = "language_example"; // String | Check-in page language with one of the following patterns 'languageCode' (e.g. EN) or 'languageCode-IATAcountryCode' (e.g. en-GB).   Default value is **en-GB** (used when required language is not available or when no value is specified). 
    try {
      Success result = apiInstance.getCheckinURLs(airlineCode, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CheckinLinksApi#getCheckinURLs");
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
| **airlineCode** | **String**| Airline code following IATA or ICAO standard - e.g. 1X; AF or ESY  [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)  [ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes)  | |
| **language** | **String**| Check-in page language with one of the following patterns &#39;languageCode&#39; (e.g. EN) or &#39;languageCode-IATAcountryCode&#39; (e.g. en-GB).   Default value is **en-GB** (used when required language is not available or when no value is specified).  | [optional] |

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
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 572     | INVALID OPTION 32171     | MANDATORY DATA MISSING                              |  -  |
| **0** | Unexpected Error |  -  |

