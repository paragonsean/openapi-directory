# AirlinesApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getairlines**](AirlinesApi.md#getairlines) | **GET** /reference-data/airlines | Return airlines information. |


<a id="getairlines"></a>
# **getairlines**
> SuccessThings getairlines(airlineCodes)

Return airlines information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirlinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    AirlinesApi apiInstance = new AirlinesApi(defaultClient);
    String airlineCodes = "BA"; // String | Code of the airline following IATA standard([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)) or ICAO standard ([ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes))  Several airlines can be selected at once by sending a list separated by a coma (i.e. AF, SWA) 
    try {
      SuccessThings result = apiInstance.getairlines(airlineCodes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirlinesApi#getairlines");
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
| **airlineCodes** | **String**| Code of the airline following IATA standard([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)) or ICAO standard ([ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes))  Several airlines can be selected at once by sending a list separated by a coma (i.e. AF, SWA)  | [optional] |

### Return type

[**SuccessThings**](SuccessThings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------    572   | INVALID OPTION    |  -  |
| **0** | Unexpected Error |  -  |

