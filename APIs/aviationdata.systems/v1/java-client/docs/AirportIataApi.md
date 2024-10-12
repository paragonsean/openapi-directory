# AirportIataApi

All URIs are relative to *https://api.aviationdata.systems*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airportIATAAirportIATASearch**](AirportIataApi.md#airportIATAAirportIATASearch) | **GET** /v1/airport/iata/{airport_iata} | Search for airport by IATA code |


<a id="airportIATAAirportIATASearch"></a>
# **airportIATAAirportIATASearch**
> AirportsAPIControllersAirportIATAControllerResponse airportIATAAirportIATASearch(airportIata)

Search for airport by IATA code

Required parameters: airport_iata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirportIataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.aviationdata.systems");

    AirportIataApi apiInstance = new AirportIataApi(defaultClient);
    String airportIata = "airportIata_example"; // String | Required: The airports IATA code
    try {
      AirportsAPIControllersAirportIATAControllerResponse result = apiInstance.airportIATAAirportIATASearch(airportIata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirportIataApi#airportIATAAirportIATASearch");
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
| **airportIata** | **String**| Required: The airports IATA code | |

### Return type

[**AirportsAPIControllersAirportIATAControllerResponse**](AirportsAPIControllersAirportIATAControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

