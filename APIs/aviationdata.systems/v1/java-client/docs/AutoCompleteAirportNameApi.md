# AutoCompleteAirportNameApi

All URIs are relative to *https://api.aviationdata.systems*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoCompleteAirportNameAirportNameSearch**](AutoCompleteAirportNameApi.md#autoCompleteAirportNameAirportNameSearch) | **GET** /v1/airport/autocomplete/{airport_name} | Autocomplete airport names. Returns a maximum of 10 airport names. |


<a id="autoCompleteAirportNameAirportNameSearch"></a>
# **autoCompleteAirportNameAirportNameSearch**
> AirportsAPIControllersAutoCompleteAirportNameControllerResponse autoCompleteAirportNameAirportNameSearch(airportName, airportServiceType, optionalCountryCode)

Autocomplete airport names. Returns a maximum of 10 airport names.

Required parameters: airport_name, airport_service_type. Optional parameter: country code (ISO 3166-1).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutoCompleteAirportNameApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.aviationdata.systems");

    AutoCompleteAirportNameApi apiInstance = new AutoCompleteAirportNameApi(defaultClient);
    String airportName = "airportName_example"; // String | Required: The airports name
    String airportServiceType = "All"; // String | Required: Needs to be: All, Scheduled or NonScheduled
    String optionalCountryCode = "optionalCountryCode_example"; // String | Optional: Country code (ISO 3166-1). This can be found via /countries
    try {
      AirportsAPIControllersAutoCompleteAirportNameControllerResponse result = apiInstance.autoCompleteAirportNameAirportNameSearch(airportName, airportServiceType, optionalCountryCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutoCompleteAirportNameApi#autoCompleteAirportNameAirportNameSearch");
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
| **airportName** | **String**| Required: The airports name | |
| **airportServiceType** | **String**| Required: Needs to be: All, Scheduled or NonScheduled | [enum: All, Scheduled, NonScheduled] |
| **optionalCountryCode** | **String**| Optional: Country code (ISO 3166-1). This can be found via /countries | [optional] |

### Return type

[**AirportsAPIControllersAutoCompleteAirportNameControllerResponse**](AirportsAPIControllersAutoCompleteAirportNameControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

