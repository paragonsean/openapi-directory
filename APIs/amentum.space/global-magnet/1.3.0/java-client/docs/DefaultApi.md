# DefaultApi

All URIs are relative to */wmm*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiWmmEndpointsWMMMagneticField**](DefaultApi.md#appApiWmmEndpointsWMMMagneticField) | **GET** /magnetic_field | Calculate magnetic declination, inclination, total field intensity, and grid variation  |


<a id="appApiWmmEndpointsWMMMagneticField"></a>
# **appApiWmmEndpointsWMMMagneticField**
> AppApiWmmEndpointsWMMMagneticField200Response appApiWmmEndpointsWMMMagneticField(altitude, latitude, longitude, year)

Calculate magnetic declination, inclination, total field intensity, and grid variation 

at specified conditions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/wmm");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal altitude = new BigDecimal("10"); // BigDecimal | Geodetic Altitude 0 km to 600 km.
    BigDecimal latitude = new BigDecimal("80"); // BigDecimal | Geodetic Latitude. -90 deg (S) to 90 deg (N).
    BigDecimal longitude = new BigDecimal("100"); // BigDecimal | Geodetic Longitude. -180 deg (W) to 180 deg (E).
    BigDecimal year = new BigDecimal("2020.5"); // BigDecimal | Year as a decimal in the range 2015-2025 (2017.5 would be half way through 2017).
    try {
      AppApiWmmEndpointsWMMMagneticField200Response result = apiInstance.appApiWmmEndpointsWMMMagneticField(altitude, latitude, longitude, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#appApiWmmEndpointsWMMMagneticField");
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
| **altitude** | **BigDecimal**| Geodetic Altitude 0 km to 600 km. | |
| **latitude** | **BigDecimal**| Geodetic Latitude. -90 deg (S) to 90 deg (N). | |
| **longitude** | **BigDecimal**| Geodetic Longitude. -180 deg (W) to 180 deg (E). | |
| **year** | **BigDecimal**| Year as a decimal in the range 2015-2025 (2017.5 would be half way through 2017). | |

### Return type

[**AppApiWmmEndpointsWMMMagneticField200Response**](AppApiWmmEndpointsWMMMagneticField200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful magnetic field intensity calculation |  -  |

