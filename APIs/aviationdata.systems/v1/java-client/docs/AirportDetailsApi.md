# AirportDetailsApi

All URIs are relative to *https://api.aviationdata.systems*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airportDetailsAirportNameSearch**](AirportDetailsApi.md#airportDetailsAirportNameSearch) | **GET** /v1/airport/name/{airport_name} | Search for airport by name |


<a id="airportDetailsAirportNameSearch"></a>
# **airportDetailsAirportNameSearch**
> AirportsAPIControllersAirportDetailsControllerResponse airportDetailsAirportNameSearch(airportName)

Search for airport by name

Required parameters: airport_name, api_mode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirportDetailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.aviationdata.systems");

    AirportDetailsApi apiInstance = new AirportDetailsApi(defaultClient);
    String airportName = "airportName_example"; // String | Required: The airports name
    try {
      AirportsAPIControllersAirportDetailsControllerResponse result = apiInstance.airportDetailsAirportNameSearch(airportName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirportDetailsApi#airportDetailsAirportNameSearch");
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

### Return type

[**AirportsAPIControllersAirportDetailsControllerResponse**](AirportsAPIControllersAirportDetailsControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

