# RoutedoseApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiIcaroEndpointsICAROAmbientDose**](RoutedoseApi.md#appApiIcaroEndpointsICAROAmbientDose) | **GET** /route/ambient_dose | Calculate the ambient equivalent dose along a great circle flight route.  |
| [**appApiIcaroEndpointsICAROEffectiveDose**](RoutedoseApi.md#appApiIcaroEndpointsICAROEffectiveDose) | **GET** /route/effective_dose | Calculate the total effective dose along a great circle flight route.  |


<a id="appApiIcaroEndpointsICAROAmbientDose"></a>
# **appApiIcaroEndpointsICAROAmbientDose**
> AppApiIcaroEndpointsICAROAmbientDose200Response appApiIcaroEndpointsICAROAmbientDose(origin, destination, year, month, day, altitude, duration, initialAltitude, cruisingAltitudes, climbTimes, cruisingTimes, descentTime, finalAltitude)

Calculate the ambient equivalent dose along a great circle flight route. 

The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  &lt;br&gt; &lt;br&gt; Use this endpoint if you are comparing model predictions to measurements. &lt;br&gt; &lt;br&gt; This API can run in two modes: &lt;br&gt; &lt;br&gt; Either specify &lt;br&gt; &lt;b&gt;altitude&lt;/b&gt;, &lt;b&gt;duration&lt;/b&gt;&lt;br&gt; for constant altitude calculations; &lt;br&gt; &lt;br&gt; Or specify &lt;br&gt; &lt;b&gt;initial_altitude&lt;/b&gt;, &lt;b&gt;cruising_altitudes&lt;/b&gt;, &lt;b&gt;climb_times&lt;/b&gt;, &lt;b&gt;cruising_times&lt;/b&gt;, &lt;b&gt;descent_time&lt;/b&gt;, &lt;b&gt;final_altitude&lt;/b&gt;&lt;br&gt; to calculate dose accounting for a step climb. &lt;br&gt; &lt;br&gt; Note: the airport codes or coordinates (depending on which was specified), and the date in DD/MM/YYYY format, are echoed in the json response as strings. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutedoseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RoutedoseApi apiInstance = new RoutedoseApi(defaultClient);
    String origin = "YSSY"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport.
    String destination = "33.94250107,-118.4079971"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport.
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 5; // Integer | Month in MM.
    Integer day = 21; // Integer | Day in DD.
    BigDecimal altitude = new BigDecimal("10.1"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 20 km.
    BigDecimal duration = new BigDecimal("5"); // BigDecimal | The flight duration in hours. The minimum is 0, the maximum is 20 hrs.
    BigDecimal initialAltitude = new BigDecimal("0"); // BigDecimal | Initial altitude (in km). The minimum is 0 m, the maximum is 20 km.
    List<BigDecimal> cruisingAltitudes = Arrays.asList(); // List<BigDecimal> | Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km.
    List<BigDecimal> climbTimes = Arrays.asList(); // List<BigDecimal> | Climb times for each cruising altitude (hours).
    List<BigDecimal> cruisingTimes = Arrays.asList(); // List<BigDecimal> | Cruising times at each cruising altitude (hours).
    BigDecimal descentTime = new BigDecimal("0.5"); // BigDecimal | Descent time from last cruising altitude to final altitude (hours).
    BigDecimal finalAltitude = new BigDecimal("0"); // BigDecimal | Final altitude (in km).
    try {
      AppApiIcaroEndpointsICAROAmbientDose200Response result = apiInstance.appApiIcaroEndpointsICAROAmbientDose(origin, destination, year, month, day, altitude, duration, initialAltitude, cruisingAltitudes, climbTimes, cruisingTimes, descentTime, finalAltitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutedoseApi#appApiIcaroEndpointsICAROAmbientDose");
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
| **origin** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport. | |
| **destination** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport. | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] |
| **duration** | **BigDecimal**| The flight duration in hours. The minimum is 0, the maximum is 20 hrs. | [optional] |
| **initialAltitude** | **BigDecimal**| Initial altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] |
| **cruisingAltitudes** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km. | [optional] |
| **climbTimes** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Climb times for each cruising altitude (hours). | [optional] |
| **cruisingTimes** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Cruising times at each cruising altitude (hours). | [optional] |
| **descentTime** | **BigDecimal**| Descent time from last cruising altitude to final altitude (hours). | [optional] |
| **finalAltitude** | **BigDecimal**| Final altitude (in km). | [optional] |

### Return type

[**AppApiIcaroEndpointsICAROAmbientDose200Response**](AppApiIcaroEndpointsICAROAmbientDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful dose calculation |  -  |

<a id="appApiIcaroEndpointsICAROEffectiveDose"></a>
# **appApiIcaroEndpointsICAROEffectiveDose**
> AppApiIcaroEndpointsICAROEffectiveDose200Response appApiIcaroEndpointsICAROEffectiveDose(origin, destination, year, month, day, altitude, duration, initialAltitude, cruisingAltitudes, climbTimes, cruisingTimes, descentTime, finalAltitude)

Calculate the total effective dose along a great circle flight route. 

Effective Dose is a radiation protection quantity defined by the International Commission on  Radiological Protection (ICRP) and represents the stochastic health  risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. &lt;br&gt; &lt;br&gt; Use this endpoint if you need to estimate radiation exposures of personnel. &lt;br&gt; &lt;br&gt; This API can run in two modes: &lt;br&gt; &lt;br&gt; Either specify &lt;br&gt; &lt;b&gt;altitude&lt;/b&gt;, &lt;b&gt;duration&lt;/b&gt;&lt;br&gt; for constant altitude calculations; &lt;br&gt; &lt;br&gt; Or specify &lt;br&gt; &lt;b&gt;initial_altitude&lt;/b&gt;, &lt;b&gt;cruising_altitudes&lt;/b&gt;, &lt;b&gt;climb_times&lt;/b&gt;, &lt;b&gt;cruising_times&lt;/b&gt;, &lt;b&gt;descent_time&lt;/b&gt;, &lt;b&gt;final_altitude&lt;/b&gt;&lt;br&gt; to calculate dose accounting for a step climb. &lt;br&gt; &lt;br&gt; Note: the airport codes or coordinates (depending on which was specified), and the date in DD/MM/YYYY format, are echoed in the json response as strings. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutedoseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RoutedoseApi apiInstance = new RoutedoseApi(defaultClient);
    String origin = "YSSY"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport.
    String destination = "33.94250107,-118.4079971"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport.
    Integer year = 2019; // Integer | Year in YYYY.
    Integer month = 5; // Integer | Month in MM.
    Integer day = 21; // Integer | Day in DD.
    BigDecimal altitude = new BigDecimal("10.1"); // BigDecimal | Altitude (in km). The minimum is 0 m, the maximum is 20 km.
    BigDecimal duration = new BigDecimal("5"); // BigDecimal | The flight duration in hours. The minimum is 0, the maximum is 20 hrs.
    BigDecimal initialAltitude = new BigDecimal("0"); // BigDecimal | Initial altitude (in km). The minimum is 0 m, the maximum is 20 km.
    List<BigDecimal> cruisingAltitudes = Arrays.asList(); // List<BigDecimal> | Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km.
    List<BigDecimal> climbTimes = Arrays.asList(); // List<BigDecimal> | Climb times for each cruising altitude (hours).
    List<BigDecimal> cruisingTimes = Arrays.asList(); // List<BigDecimal> | Cruising times at each cruising altitude (hours).
    BigDecimal descentTime = new BigDecimal("0.5"); // BigDecimal | Descent time from last cruising altitude to final altitude (hours).
    BigDecimal finalAltitude = new BigDecimal("0"); // BigDecimal | Final altitude (in km).
    try {
      AppApiIcaroEndpointsICAROEffectiveDose200Response result = apiInstance.appApiIcaroEndpointsICAROEffectiveDose(origin, destination, year, month, day, altitude, duration, initialAltitude, cruisingAltitudes, climbTimes, cruisingTimes, descentTime, finalAltitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutedoseApi#appApiIcaroEndpointsICAROEffectiveDose");
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
| **origin** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport. | |
| **destination** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport. | |
| **year** | **Integer**| Year in YYYY. | |
| **month** | **Integer**| Month in MM. | |
| **day** | **Integer**| Day in DD. | |
| **altitude** | **BigDecimal**| Altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] |
| **duration** | **BigDecimal**| The flight duration in hours. The minimum is 0, the maximum is 20 hrs. | [optional] |
| **initialAltitude** | **BigDecimal**| Initial altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] |
| **cruisingAltitudes** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km. | [optional] |
| **climbTimes** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Climb times for each cruising altitude (hours). | [optional] |
| **cruisingTimes** | [**List&lt;BigDecimal&gt;**](BigDecimal.md)| Cruising times at each cruising altitude (hours). | [optional] |
| **descentTime** | **BigDecimal**| Descent time from last cruising altitude to final altitude (hours). | [optional] |
| **finalAltitude** | **BigDecimal**| Final altitude (in km). | [optional] |

### Return type

[**AppApiIcaroEndpointsICAROEffectiveDose200Response**](AppApiIcaroEndpointsICAROEffectiveDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful dose calculation |  -  |

