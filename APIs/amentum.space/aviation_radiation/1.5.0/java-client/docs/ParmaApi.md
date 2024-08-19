# ParmaApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiParmaEndpointsPARMAAmbientDose**](ParmaApi.md#appApiParmaEndpointsPARMAAmbientDose) | **GET** /parma/ambient_dose | The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types.  |
| [**appApiParmaEndpointsPARMADifferentialIntensity**](ParmaApi.md#appApiParmaEndpointsPARMADifferentialIntensity) | **GET** /parma/differential_intensity | The energy differential intensity of a particle at a given zenith angle. |
| [**appApiParmaEndpointsPARMAEffectiveDose**](ParmaApi.md#appApiParmaEndpointsPARMAEffectiveDose) | **GET** /parma/effective_dose | The effective dose rate calculated for a single particle type, or accumulated over all particle types.  |


<a id="appApiParmaEndpointsPARMAAmbientDose"></a>
# **appApiParmaEndpointsPARMAAmbientDose**
> AppApiParmaEndpointsPARMAAmbientDose200Response appApiParmaEndpointsPARMAAmbientDose(latitude, longitude, year, month, day, particle, altitude, atmosphericDepth)

The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 

The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  Use this endpoint if you are comparing model predictions to measurements. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParmaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ParmaApi apiInstance = new ParmaApi(defaultClient);
    BigDecimal latitude = new BigDecimal("30"); // BigDecimal | Latitude. -90 (S) to 90 (N).
    BigDecimal longitude = new BigDecimal("30"); // BigDecimal | Longitude. -180 (W) to 180 (E).
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 12; // Integer | Month in MM.
    Integer day = 1; // Integer | Day in DD.
    String particle = "total"; // String | The particle type as a string. Specifying 'total', only used for the dose calculation, returns the dose for all particle types. 
    BigDecimal altitude = new BigDecimal("11"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    BigDecimal atmosphericDepth = new BigDecimal("0.92"); // BigDecimal | Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
    try {
      AppApiParmaEndpointsPARMAAmbientDose200Response result = apiInstance.appApiParmaEndpointsPARMAAmbientDose(latitude, longitude, year, month, day, particle, altitude, atmosphericDepth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParmaApi#appApiParmaEndpointsPARMAAmbientDose");
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
| **latitude** | **BigDecimal**| Latitude. -90 (S) to 90 (N). | |
| **longitude** | **BigDecimal**| Longitude. -180 (W) to 180 (E). | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **particle** | **String**| The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types.  | [enum: total, e-, e+, mu+, mu-, gamma, neutron, proton, alpha] |
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | [optional] |
| **atmosphericDepth** | **BigDecimal**| Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both.  | [optional] |

### Return type

[**AppApiParmaEndpointsPARMAAmbientDose200Response**](AppApiParmaEndpointsPARMAAmbientDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful dose read operation |  -  |

<a id="appApiParmaEndpointsPARMADifferentialIntensity"></a>
# **appApiParmaEndpointsPARMADifferentialIntensity**
> AppApiParmaEndpointsPARMADifferentialIntensity200Response appApiParmaEndpointsPARMADifferentialIntensity(latitude, longitude, year, month, day, particle, angle, altitude, atmosphericDepth)

The energy differential intensity of a particle at a given zenith angle.

The differential intensity of a particle is a directional quantity that describes the number of particles per unit area, per unit solid angle, per unit energy, and per unit time. The API leverages the functionality of PARMA to calculate differential intensity distributions with energies in units of MeV and Intensity in units of /cm2/sr/MeV/s. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParmaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ParmaApi apiInstance = new ParmaApi(defaultClient);
    BigDecimal latitude = new BigDecimal("30"); // BigDecimal | Latitude. -90 (S) to 90 (N).
    BigDecimal longitude = new BigDecimal("30"); // BigDecimal | Longitude. -180 (W) to 180 (E).
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 12; // Integer | Month in MM.
    Integer day = 1; // Integer | Day in DD.
    String particle = "total"; // String | The particle type as a string. Specifying 'total', only used for the dose calculation, returns the dose for all particle types. 
    BigDecimal angle = new BigDecimal("1"); // BigDecimal | Direction cosine. 1.0 is in the downward direction.
    BigDecimal altitude = new BigDecimal("11"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    BigDecimal atmosphericDepth = new BigDecimal("0.92"); // BigDecimal | Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
    try {
      AppApiParmaEndpointsPARMADifferentialIntensity200Response result = apiInstance.appApiParmaEndpointsPARMADifferentialIntensity(latitude, longitude, year, month, day, particle, angle, altitude, atmosphericDepth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParmaApi#appApiParmaEndpointsPARMADifferentialIntensity");
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
| **latitude** | **BigDecimal**| Latitude. -90 (S) to 90 (N). | |
| **longitude** | **BigDecimal**| Longitude. -180 (W) to 180 (E). | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **particle** | **String**| The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types.  | [enum: total, e-, e+, mu+, mu-, gamma, neutron, proton, alpha] |
| **angle** | **BigDecimal**| Direction cosine. 1.0 is in the downward direction. | |
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | [optional] |
| **atmosphericDepth** | **BigDecimal**| Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both.  | [optional] |

### Return type

[**AppApiParmaEndpointsPARMADifferentialIntensity200Response**](AppApiParmaEndpointsPARMADifferentialIntensity200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful read of intensity operation |  -  |

<a id="appApiParmaEndpointsPARMAEffectiveDose"></a>
# **appApiParmaEndpointsPARMAEffectiveDose**
> AppApiParmaEndpointsPARMAEffectiveDose200Response appApiParmaEndpointsPARMAEffectiveDose(latitude, longitude, year, month, day, particle, altitude, atmosphericDepth)

The effective dose rate calculated for a single particle type, or accumulated over all particle types. 

Effective dose is a radiation protection quantity defined by the International Commission on Radiological Protection (ICRP) and represents the stochastic health risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. Use this endpoint if you need to estimate radiation exposures of personnel. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParmaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ParmaApi apiInstance = new ParmaApi(defaultClient);
    BigDecimal latitude = new BigDecimal("30"); // BigDecimal | Latitude. -90 (S) to 90 (N).
    BigDecimal longitude = new BigDecimal("30"); // BigDecimal | Longitude. -180 (W) to 180 (E).
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 12; // Integer | Month in MM.
    Integer day = 1; // Integer | Day in DD.
    String particle = "total"; // String | The particle type as a string. Specifying 'total', only used for the dose calculation, returns the dose for all particle types. 
    BigDecimal altitude = new BigDecimal("11"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
    BigDecimal atmosphericDepth = new BigDecimal("0.92"); // BigDecimal | Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
    try {
      AppApiParmaEndpointsPARMAEffectiveDose200Response result = apiInstance.appApiParmaEndpointsPARMAEffectiveDose(latitude, longitude, year, month, day, particle, altitude, atmosphericDepth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParmaApi#appApiParmaEndpointsPARMAEffectiveDose");
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
| **latitude** | **BigDecimal**| Latitude. -90 (S) to 90 (N). | |
| **longitude** | **BigDecimal**| Longitude. -180 (W) to 180 (E). | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **particle** | **String**| The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types.  | [enum: total, e-, e+, mu+, mu-, gamma, neutron, proton, alpha] |
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | [optional] |
| **atmosphericDepth** | **BigDecimal**| Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both.  | [optional] |

### Return type

[**AppApiParmaEndpointsPARMAEffectiveDose200Response**](AppApiParmaEndpointsPARMAEffectiveDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful dose read operation |  -  |

