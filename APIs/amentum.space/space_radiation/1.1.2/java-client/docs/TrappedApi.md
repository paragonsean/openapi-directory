# TrappedApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiEndpointsTrappedRadiationCalculateFluxMean**](TrappedApi.md#appApiEndpointsTrappedRadiationCalculateFluxMean) | **GET** /trapped/flux_mean | Calculate mean particle flux  |
| [**appApiEndpointsTrappedRadiationCalculateFluxPercentile**](TrappedApi.md#appApiEndpointsTrappedRadiationCalculateFluxPercentile) | **GET** /trapped/flux_percentile | Calculate percentile particle flux  |


<a id="appApiEndpointsTrappedRadiationCalculateFluxMean"></a>
# **appApiEndpointsTrappedRadiationCalculateFluxMean**
> Flux appApiEndpointsTrappedRadiationCalculateFluxMean(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second)

Calculate mean particle flux 

at given coordinates and date-time. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrappedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TrappedApi apiInstance = new TrappedApi(defaultClient);
    String model = "AE9"; // String | <br>Which model to use: <br><br> - Energetic electrons (AE9) <br> - Energetic protons (AP9)  <br> - Space plasma model for electrons (SPME) <br> - for hydrogen (SPMH) <br> - for helium (SPMHE) <br> - for oxygen (SPMO)  
    String coordSys = "GDZ"; // String | <br>Coordinate system to use:  <br><br> - Geodetic/WGS84 (GDZ) <br> - Geocentric Cartesian (GEO) <br> - Geocentric Earth Inertial (GEI) <br> See \"Bhavnani, K. H., & Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\"  for coord system definitions. 
    String coordUnits = "KM"; // String | <br>Coordinate units to use: km (KM) or Earth Radii (RE) 
    BigDecimal coord1 = new BigDecimal("3216.6"); // BigDecimal | <br>First coordinate value to specify position. <br><br> Ordering for GEI, GEO coords:X, Y, Z<br> Ordering for GDZ coords: Alt, Lat, Long<br>  Valid ranges for latitude: -90, 90<br>  Valid ranges for longitude: 0, 360<br>  
    BigDecimal coord2 = new BigDecimal("35426"); // BigDecimal | <br>Second coordinate value.
    BigDecimal coord3 = new BigDecimal("603.4"); // BigDecimal | <br>Third coordinate value.
    Integer year = 2017; // Integer | <br>
    Integer month = 1; // Integer | <br>
    Integer day = 1; // Integer | <br>
    Integer hour = 0; // Integer | <br>
    Integer minute = 0; // Integer | <br>
    Integer second = 0; // Integer | <br>
    try {
      Flux result = apiInstance.appApiEndpointsTrappedRadiationCalculateFluxMean(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrappedApi#appApiEndpointsTrappedRadiationCalculateFluxMean");
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
| **model** | **String**| &lt;br&gt;Which model to use: &lt;br&gt;&lt;br&gt; - Energetic electrons (AE9) &lt;br&gt; - Energetic protons (AP9)  &lt;br&gt; - Space plasma model for electrons (SPME) &lt;br&gt; - for hydrogen (SPMH) &lt;br&gt; - for helium (SPMHE) &lt;br&gt; - for oxygen (SPMO)   | [enum: AE9, AP9, SPME, SPMH, SPMHE, SPMO] |
| **coordSys** | **String**| &lt;br&gt;Coordinate system to use:  &lt;br&gt;&lt;br&gt; - Geodetic/WGS84 (GDZ) &lt;br&gt; - Geocentric Cartesian (GEO) &lt;br&gt; - Geocentric Earth Inertial (GEI) &lt;br&gt; See \&quot;Bhavnani, K. H., &amp; Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\&quot;  for coord system definitions.  | [enum: GDZ, GEO, GEI] |
| **coordUnits** | **String**| &lt;br&gt;Coordinate units to use: km (KM) or Earth Radii (RE)  | [enum: KM, RE] |
| **coord1** | **BigDecimal**| &lt;br&gt;First coordinate value to specify position. &lt;br&gt;&lt;br&gt; Ordering for GEI, GEO coords:X, Y, Z&lt;br&gt; Ordering for GDZ coords: Alt, Lat, Long&lt;br&gt;  Valid ranges for latitude: -90, 90&lt;br&gt;  Valid ranges for longitude: 0, 360&lt;br&gt;   | |
| **coord2** | **BigDecimal**| &lt;br&gt;Second coordinate value. | |
| **coord3** | **BigDecimal**| &lt;br&gt;Third coordinate value. | |
| **year** | **Integer**| &lt;br&gt; | |
| **month** | **Integer**| &lt;br&gt; | |
| **day** | **Integer**| &lt;br&gt; | |
| **hour** | **Integer**| &lt;br&gt; | |
| **minute** | **Integer**| &lt;br&gt; | |
| **second** | **Integer**| &lt;br&gt; | |

### Return type

[**Flux**](Flux.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful flux calculation |  -  |

<a id="appApiEndpointsTrappedRadiationCalculateFluxPercentile"></a>
# **appApiEndpointsTrappedRadiationCalculateFluxPercentile**
> Flux appApiEndpointsTrappedRadiationCalculateFluxPercentile(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second, percentile)

Calculate percentile particle flux 

at given coordinates and date-time. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrappedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TrappedApi apiInstance = new TrappedApi(defaultClient);
    String model = "AE9"; // String | <br>Which model to use: <br><br> - Energetic electrons (AE9) <br> - Energetic protons (AP9)  <br> - Space plasma model for electrons (SPME) <br> - for hydrogen (SPMH) <br> - for helium (SPMHE) <br> - for oxygen (SPMO)  
    String coordSys = "GDZ"; // String | <br>Coordinate system to use:  <br><br> - Geodetic/WGS84 (GDZ) <br> - Geocentric Cartesian (GEO) <br> - Geocentric Earth Inertial (GEI) <br> See \"Bhavnani, K. H., & Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\"  for coord system definitions. 
    String coordUnits = "KM"; // String | <br>Coordinate units to use: km (KM) or Earth Radii (RE) 
    BigDecimal coord1 = new BigDecimal("3216.6"); // BigDecimal | <br>First coordinate value to specify position. <br><br> Ordering for GEI, GEO coords:X, Y, Z<br> Ordering for GDZ coords: Alt, Lat, Long<br>  Valid ranges for latitude: -90, 90<br>  Valid ranges for longitude: 0, 360<br>  
    BigDecimal coord2 = new BigDecimal("35426"); // BigDecimal | <br>Second coordinate value.
    BigDecimal coord3 = new BigDecimal("603.4"); // BigDecimal | <br>Third coordinate value.
    Integer year = 2017; // Integer | <br>
    Integer month = 1; // Integer | <br>
    Integer day = 1; // Integer | <br>
    Integer hour = 0; // Integer | <br>
    Integer minute = 0; // Integer | <br>
    Integer second = 0; // Integer | <br>
    Integer percentile = 50; // Integer | <br>Integer percentile at which to calc flux (50 is the median value). 
    try {
      Flux result = apiInstance.appApiEndpointsTrappedRadiationCalculateFluxPercentile(model, coordSys, coordUnits, coord1, coord2, coord3, year, month, day, hour, minute, second, percentile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrappedApi#appApiEndpointsTrappedRadiationCalculateFluxPercentile");
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
| **model** | **String**| &lt;br&gt;Which model to use: &lt;br&gt;&lt;br&gt; - Energetic electrons (AE9) &lt;br&gt; - Energetic protons (AP9)  &lt;br&gt; - Space plasma model for electrons (SPME) &lt;br&gt; - for hydrogen (SPMH) &lt;br&gt; - for helium (SPMHE) &lt;br&gt; - for oxygen (SPMO)   | [enum: AE9, AP9, SPME, SPMH, SPMHE, SPMO] |
| **coordSys** | **String**| &lt;br&gt;Coordinate system to use:  &lt;br&gt;&lt;br&gt; - Geodetic/WGS84 (GDZ) &lt;br&gt; - Geocentric Cartesian (GEO) &lt;br&gt; - Geocentric Earth Inertial (GEI) &lt;br&gt; See \&quot;Bhavnani, K. H., &amp; Vancour, R. P. (1991).  Coordinate systems for space and geophysical applications\&quot;  for coord system definitions.  | [enum: GDZ, GEO, GEI] |
| **coordUnits** | **String**| &lt;br&gt;Coordinate units to use: km (KM) or Earth Radii (RE)  | [enum: KM, RE] |
| **coord1** | **BigDecimal**| &lt;br&gt;First coordinate value to specify position. &lt;br&gt;&lt;br&gt; Ordering for GEI, GEO coords:X, Y, Z&lt;br&gt; Ordering for GDZ coords: Alt, Lat, Long&lt;br&gt;  Valid ranges for latitude: -90, 90&lt;br&gt;  Valid ranges for longitude: 0, 360&lt;br&gt;   | |
| **coord2** | **BigDecimal**| &lt;br&gt;Second coordinate value. | |
| **coord3** | **BigDecimal**| &lt;br&gt;Third coordinate value. | |
| **year** | **Integer**| &lt;br&gt; | |
| **month** | **Integer**| &lt;br&gt; | |
| **day** | **Integer**| &lt;br&gt; | |
| **hour** | **Integer**| &lt;br&gt; | |
| **minute** | **Integer**| &lt;br&gt; | |
| **second** | **Integer**| &lt;br&gt; | |
| **percentile** | **Integer**| &lt;br&gt;Integer percentile at which to calc flux (50 is the median value).  | |

### Return type

[**Flux**](Flux.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful flux calculation |  -  |

