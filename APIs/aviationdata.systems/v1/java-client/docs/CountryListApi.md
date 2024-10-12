# CountryListApi

All URIs are relative to *https://api.aviationdata.systems*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countryListCountryAirportList**](CountryListApi.md#countryListCountryAirportList) | **GET** /v1/country_list | Country list. Returns a list of countries where airport data is available |


<a id="countryListCountryAirportList"></a>
# **countryListCountryAirportList**
> AirportsAPIControllersCountryListControllerCountryListResponse countryListCountryAirportList()

Country list. Returns a list of countries where airport data is available

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryListApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.aviationdata.systems");

    CountryListApi apiInstance = new CountryListApi(defaultClient);
    try {
      AirportsAPIControllersCountryListControllerCountryListResponse result = apiInstance.countryListCountryAirportList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryListApi#countryListCountryAirportList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AirportsAPIControllersCountryListControllerCountryListResponse**](AirportsAPIControllersCountryListControllerCountryListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

