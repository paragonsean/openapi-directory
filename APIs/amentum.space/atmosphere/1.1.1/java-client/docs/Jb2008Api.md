# Jb2008Api

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiEndpointsJB2008SampleAtmosphere**](Jb2008Api.md#appApiEndpointsJB2008SampleAtmosphere) | **GET** /jb2008 | Compute atmospheric density and temperatures  |


<a id="appApiEndpointsJB2008SampleAtmosphere"></a>
# **appApiEndpointsJB2008SampleAtmosphere**
> AppApiEndpointsJB2008SampleAtmosphere200Response appApiEndpointsJB2008SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc)

Compute atmospheric density and temperatures 

under given conditions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Jb2008Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    Jb2008Api apiInstance = new Jb2008Api(defaultClient);
    Integer year = 2020; // Integer | Year in YYYY format
    Integer month = 5; // Integer | Month in MM format
    Integer day = 23; // Integer | Day in DD format
    BigDecimal altitude = new BigDecimal("300"); // BigDecimal | Altitude in (km)
    BigDecimal geodeticLatitude = new BigDecimal("42"); // BigDecimal | GeodeticLatitude (deg) -90 to 90 deg
    BigDecimal geodeticLongitude = new BigDecimal("42"); // BigDecimal | GeodeticLongitude (deg) 0 to 360 deg
    BigDecimal utc = new BigDecimal("2"); // BigDecimal | Coordinated Universal Time (hrs)
    try {
      AppApiEndpointsJB2008SampleAtmosphere200Response result = apiInstance.appApiEndpointsJB2008SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Jb2008Api#appApiEndpointsJB2008SampleAtmosphere");
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

### Return type

[**AppApiEndpointsJB2008SampleAtmosphere200Response**](AppApiEndpointsJB2008SampleAtmosphere200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful atmospheric density calculation |  -  |

