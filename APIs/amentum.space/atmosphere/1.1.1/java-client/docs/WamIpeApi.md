# WamIpeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiWfsEndpointsWFSGetValues**](WamIpeApi.md#appApiWfsEndpointsWFSGetValues) | **GET** /wam-ipe | Forecast winds, ion and molecular densities, and temperatures in the atmosphere  |


<a id="appApiWfsEndpointsWFSGetValues"></a>
# **appApiWfsEndpointsWFSGetValues**
> AppApiWfsEndpointsWFSGetValues200Response appApiWfsEndpointsWFSGetValues(latitude, longitude, altitude, year, month, day, hour, minute)

Forecast winds, ion and molecular densities, and temperatures in the atmosphere 

at a given position and time on 42-48 hour forecast horizon (10 minute resolution). NOTE: latitudes outside the interval (-90,90) are clipped to the endpoints; longitudes outside (0,360) are wrapped.    

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WamIpeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WamIpeApi apiInstance = new WamIpeApi(defaultClient);
    BigDecimal latitude = new BigDecimal("42"); // BigDecimal | Latitude (deg) -90 to 90 deg
    BigDecimal longitude = new BigDecimal("42"); // BigDecimal | Longitude (deg) 0 to 360 deg or -180 to 180 deg
    BigDecimal altitude = new BigDecimal("300"); // BigDecimal | Altitude in (km)
    Integer year = 2020; // Integer | Year in YYYY format
    Integer month = 5; // Integer | Month in MM format
    Integer day = 23; // Integer | Day in DD format
    Integer hour = 15; // Integer | UTC Hour of the day in 24 hour format
    Integer minute = 10; // Integer | Minute of the given hour
    try {
      AppApiWfsEndpointsWFSGetValues200Response result = apiInstance.appApiWfsEndpointsWFSGetValues(latitude, longitude, altitude, year, month, day, hour, minute);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WamIpeApi#appApiWfsEndpointsWFSGetValues");
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
| **latitude** | **BigDecimal**| Latitude (deg) -90 to 90 deg | |
| **longitude** | **BigDecimal**| Longitude (deg) 0 to 360 deg or -180 to 180 deg | |
| **altitude** | **BigDecimal**| Altitude in (km) | |
| **year** | **Integer**| Year in YYYY format | |
| **month** | **Integer**| Month in MM format | |
| **day** | **Integer**| Day in DD format | |
| **hour** | **Integer**| UTC Hour of the day in 24 hour format | |
| **minute** | **Integer**| Minute of the given hour | |

### Return type

[**AppApiWfsEndpointsWFSGetValues200Response**](AppApiWfsEndpointsWFSGetValues200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful wam-ipe calculation |  -  |

