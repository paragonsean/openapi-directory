# CountryAirportListApi

All URIs are relative to *https://api.aviationdata.systems*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countryAirportListCountryAirportList**](CountryAirportListApi.md#countryAirportListCountryAirportList) | **GET** /v1/country/code/{country_code} | Country airports. Returns a list of airports for a country code(ISO 3166-1 alpha-2 code) |


<a id="countryAirportListCountryAirportList"></a>
# **countryAirportListCountryAirportList**
> AirportsAPIControllersCountryAirportListControllerAirportListResponse countryAirportListCountryAirportList(countryCode, airportServiceType)

Country airports. Returns a list of airports for a country code(ISO 3166-1 alpha-2 code)

Required parameters: country code (ISO 3166-1), airport_service_type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryAirportListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.aviationdata.systems");

    CountryAirportListApi apiInstance = new CountryAirportListApi(defaultClient);
    String countryCode = "countryCode_example"; // String | Country code (ISO 3166-1). This can be found via /countries
    String airportServiceType = "All"; // String | Required: Needs to be: All, Scheduled or NonScheduled
    try {
      AirportsAPIControllersCountryAirportListControllerAirportListResponse result = apiInstance.countryAirportListCountryAirportList(countryCode, airportServiceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryAirportListApi#countryAirportListCountryAirportList");
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
| **countryCode** | **String**| Country code (ISO 3166-1). This can be found via /countries | |
| **airportServiceType** | **String**| Required: Needs to be: All, Scheduled or NonScheduled | [enum: All, Scheduled, NonScheduled] |

### Return type

[**AirportsAPIControllersCountryAirportListControllerAirportListResponse**](AirportsAPIControllersCountryAirportListControllerAirportListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

