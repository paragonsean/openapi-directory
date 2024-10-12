# Nrlmsise00Api

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiEndpointsNRLMSISE00SampleAtmosphere**](Nrlmsise00Api.md#appApiEndpointsNRLMSISE00SampleAtmosphere) | **GET** /nrlmsise00 | Compute atmospheric composition, density, and temperatures  |


<a id="appApiEndpointsNRLMSISE00SampleAtmosphere"></a>
# **appApiEndpointsNRLMSISE00SampleAtmosphere**
> AppApiEndpointsNRLMSISE00SampleAtmosphere200Response appApiEndpointsNRLMSISE00SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc, f107a, f107, ap)

Compute atmospheric composition, density, and temperatures 

at specified conditions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Nrlmsise00Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    Nrlmsise00Api apiInstance = new Nrlmsise00Api(defaultClient);
    Integer year = 2020; // Integer | Year in YYYY format
    Integer month = 5; // Integer | Month in MM format
    Integer day = 23; // Integer | Day in DD format
    BigDecimal altitude = new BigDecimal("300"); // BigDecimal | Altitude in (km)
    BigDecimal geodeticLatitude = new BigDecimal("42"); // BigDecimal | GeodeticLatitude (deg) -90 to 90 deg
    BigDecimal geodeticLongitude = new BigDecimal("42"); // BigDecimal | GeodeticLongitude (deg) 0 to 360 deg
    BigDecimal utc = new BigDecimal("2"); // BigDecimal | Coordinated Universal Time (hrs)
    BigDecimal f107a = new BigDecimal("120"); // BigDecimal | (Optional) 81 day average of F10.7 flux (SFU) centered on the specified day. F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically. 
    BigDecimal f107 = new BigDecimal("120"); // BigDecimal | (Optional) Daily F10.7 cm radio flux for previous day (SFU). F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically. 
    BigDecimal ap = new BigDecimal("30"); // BigDecimal | (Optional) The Ap-index provides a daily average level for geomagnetic activity F107, F107A, AP effects can be neglected below 80 km. If unspecified, the average of values in the 24 hours preceding the date-time  are automatically calculated from data provided by GFZ German Research Centre  for Geosciences. 
    try {
      AppApiEndpointsNRLMSISE00SampleAtmosphere200Response result = apiInstance.appApiEndpointsNRLMSISE00SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc, f107a, f107, ap);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Nrlmsise00Api#appApiEndpointsNRLMSISE00SampleAtmosphere");
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
| **year** | **Integer**| Year in YYYY format | |
| **month** | **Integer**| Month in MM format | |
| **day** | **Integer**| Day in DD format | |
| **altitude** | **BigDecimal**| Altitude in (km) | |
| **geodeticLatitude** | **BigDecimal**| GeodeticLatitude (deg) -90 to 90 deg | |
| **geodeticLongitude** | **BigDecimal**| GeodeticLongitude (deg) 0 to 360 deg | |
| **utc** | **BigDecimal**| Coordinated Universal Time (hrs) | |
| **f107a** | **BigDecimal**| (Optional) 81 day average of F10.7 flux (SFU) centered on the specified day. F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically.  | [optional] |
| **f107** | **BigDecimal**| (Optional) Daily F10.7 cm radio flux for previous day (SFU). F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically.  | [optional] |
| **ap** | **BigDecimal**| (Optional) The Ap-index provides a daily average level for geomagnetic activity F107, F107A, AP effects can be neglected below 80 km. If unspecified, the average of values in the 24 hours preceding the date-time  are automatically calculated from data provided by GFZ German Research Centre  for Geosciences.  | [optional] |

### Return type

[**AppApiEndpointsNRLMSISE00SampleAtmosphere200Response**](AppApiEndpointsNRLMSISE00SampleAtmosphere200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful atmospheric density calculation |  -  |

