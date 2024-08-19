# Cari7Api

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiCari7EndpointsCARI7AmbientDose**](Cari7Api.md#appApiCari7EndpointsCARI7AmbientDose) | **GET** /cari7/ambient_dose | The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types.  |
| [**appApiCari7EndpointsCARI7EffectiveDose**](Cari7Api.md#appApiCari7EndpointsCARI7EffectiveDose) | **GET** /cari7/effective_dose | The effective dose rate calculated for a single particle type, or accumulated over all particle types.  |


<a id="appApiCari7EndpointsCARI7AmbientDose"></a>
# **appApiCari7EndpointsCARI7AmbientDose**
> AppApiCari7EndpointsCARI7AmbientDose200Response appApiCari7EndpointsCARI7AmbientDose(altitude, latitude, longitude, year, month, day, utc, particle)

The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 

The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  Use this endpoint if you are comparing model predictions to measurements. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Cari7Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    Cari7Api apiInstance = new Cari7Api(defaultClient);
    BigDecimal altitude = new BigDecimal("11"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    BigDecimal latitude = new BigDecimal("30"); // BigDecimal | Latitude. -90 (S) to 90 (N).
    BigDecimal longitude = new BigDecimal("30"); // BigDecimal | Longitude. -180 (W) to 180 (E).
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 12; // Integer | Month in MM.
    Integer day = 1; // Integer | Day in DD.
    Integer utc = 3; // Integer | Hour in 24 hour time.
    String particle = "total"; // String | The particle type as a string. Specifying 'total' returns the dose for all particle types. 
    try {
      AppApiCari7EndpointsCARI7AmbientDose200Response result = apiInstance.appApiCari7EndpointsCARI7AmbientDose(altitude, latitude, longitude, year, month, day, utc, particle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Cari7Api#appApiCari7EndpointsCARI7AmbientDose");
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
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | |
| **latitude** | **BigDecimal**| Latitude. -90 (S) to 90 (N). | |
| **longitude** | **BigDecimal**| Longitude. -180 (W) to 180 (E). | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **utc** | **Integer**| Hour in 24 hour time. | |
| **particle** | **String**| The particle type as a string. Specifying &#39;total&#39; returns the dose for all particle types.  | [enum: total, neutron, photon, e-, e+, mu-, mu+, proton, pi-, pi+, deuteron, triton, helion, alpha, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe] |

### Return type

[**AppApiCari7EndpointsCARI7AmbientDose200Response**](AppApiCari7EndpointsCARI7AmbientDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful dose calculation |  -  |

<a id="appApiCari7EndpointsCARI7EffectiveDose"></a>
# **appApiCari7EndpointsCARI7EffectiveDose**
> AppApiCari7EndpointsCARI7EffectiveDose200Response appApiCari7EndpointsCARI7EffectiveDose(altitude, latitude, longitude, year, month, day, utc, particle)

The effective dose rate calculated for a single particle type, or accumulated over all particle types. 

Effective Dose is a radiation protection quantity defined by the International Commission on  Radiological Protection (ICRP) and represents the stochastic health  risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. Use this endpoint if you need to estimate radiation exposures of personnel. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Cari7Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    Cari7Api apiInstance = new Cari7Api(defaultClient);
    BigDecimal altitude = new BigDecimal("11"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    BigDecimal latitude = new BigDecimal("30"); // BigDecimal | Latitude. -90 (S) to 90 (N).
    BigDecimal longitude = new BigDecimal("30"); // BigDecimal | Longitude. -180 (W) to 180 (E).
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 12; // Integer | Month in MM.
    Integer day = 1; // Integer | Day in DD.
    Integer utc = 3; // Integer | Hour in 24 hour time.
    String particle = "total"; // String | The particle type as a string. Specifying 'total' returns the dose for all particle types. 
    try {
      AppApiCari7EndpointsCARI7EffectiveDose200Response result = apiInstance.appApiCari7EndpointsCARI7EffectiveDose(altitude, latitude, longitude, year, month, day, utc, particle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Cari7Api#appApiCari7EndpointsCARI7EffectiveDose");
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
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | |
| **latitude** | **BigDecimal**| Latitude. -90 (S) to 90 (N). | |
| **longitude** | **BigDecimal**| Longitude. -180 (W) to 180 (E). | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **utc** | **Integer**| Hour in 24 hour time. | |
| **particle** | **String**| The particle type as a string. Specifying &#39;total&#39; returns the dose for all particle types.  | [enum: total, neutron, photon, e-, e+, mu-, mu+, proton, pi-, pi+, deuteron, triton, helion, alpha, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe] |

### Return type

[**AppApiCari7EndpointsCARI7EffectiveDose200Response**](AppApiCari7EndpointsCARI7EffectiveDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful dose calculation |  -  |

