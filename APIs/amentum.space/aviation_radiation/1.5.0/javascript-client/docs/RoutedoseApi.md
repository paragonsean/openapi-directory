# AviationRadiationApi.RoutedoseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiIcaroEndpointsICAROAmbientDose**](RoutedoseApi.md#appApiIcaroEndpointsICAROAmbientDose) | **GET** /route/ambient_dose | Calculate the ambient equivalent dose along a great circle flight route. 
[**appApiIcaroEndpointsICAROEffectiveDose**](RoutedoseApi.md#appApiIcaroEndpointsICAROEffectiveDose) | **GET** /route/effective_dose | Calculate the total effective dose along a great circle flight route. 



## appApiIcaroEndpointsICAROAmbientDose

> AppApiIcaroEndpointsICAROAmbientDose200Response appApiIcaroEndpointsICAROAmbientDose(origin, destination, year, month, day, opts)

Calculate the ambient equivalent dose along a great circle flight route. 

The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  &lt;br&gt; &lt;br&gt; Use this endpoint if you are comparing model predictions to measurements. &lt;br&gt; &lt;br&gt; This API can run in two modes: &lt;br&gt; &lt;br&gt; Either specify &lt;br&gt; &lt;b&gt;altitude&lt;/b&gt;, &lt;b&gt;duration&lt;/b&gt;&lt;br&gt; for constant altitude calculations; &lt;br&gt; &lt;br&gt; Or specify &lt;br&gt; &lt;b&gt;initial_altitude&lt;/b&gt;, &lt;b&gt;cruising_altitudes&lt;/b&gt;, &lt;b&gt;climb_times&lt;/b&gt;, &lt;b&gt;cruising_times&lt;/b&gt;, &lt;b&gt;descent_time&lt;/b&gt;, &lt;b&gt;final_altitude&lt;/b&gt;&lt;br&gt; to calculate dose accounting for a step climb. &lt;br&gt; &lt;br&gt; Note: the airport codes or coordinates (depending on which was specified), and the date in DD/MM/YYYY format, are echoed in the json response as strings. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.RoutedoseApi();
let origin = "YSSY"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport.
let destination = "33.94250107,-118.4079971"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport.
let year = 2019; // Number | Year in YYYY.
let month = 5; // Number | Month in MM.
let day = 21; // Number | Day in DD.
let opts = {
  'altitude': 10.1, // Number | Altitude (in km). The minimum is 0 m, the maximum is 20 km.
  'duration': 5, // Number | The flight duration in hours. The minimum is 0, the maximum is 20 hrs.
  'initialAltitude': 0, // Number | Initial altitude (in km). The minimum is 0 m, the maximum is 20 km.
  'cruisingAltitudes': [null], // [Number] | Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km.
  'climbTimes': [null], // [Number] | Climb times for each cruising altitude (hours).
  'cruisingTimes': [null], // [Number] | Cruising times at each cruising altitude (hours).
  'descentTime': 0.5, // Number | Descent time from last cruising altitude to final altitude (hours).
  'finalAltitude': 0 // Number | Final altitude (in km).
};
apiInstance.appApiIcaroEndpointsICAROAmbientDose(origin, destination, year, month, day, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport. | 
 **destination** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport. | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] 
 **duration** | **Number**| The flight duration in hours. The minimum is 0, the maximum is 20 hrs. | [optional] 
 **initialAltitude** | **Number**| Initial altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] 
 **cruisingAltitudes** | [**[Number]**](Number.md)| Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km. | [optional] 
 **climbTimes** | [**[Number]**](Number.md)| Climb times for each cruising altitude (hours). | [optional] 
 **cruisingTimes** | [**[Number]**](Number.md)| Cruising times at each cruising altitude (hours). | [optional] 
 **descentTime** | **Number**| Descent time from last cruising altitude to final altitude (hours). | [optional] 
 **finalAltitude** | **Number**| Final altitude (in km). | [optional] 

### Return type

[**AppApiIcaroEndpointsICAROAmbientDose200Response**](AppApiIcaroEndpointsICAROAmbientDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiIcaroEndpointsICAROEffectiveDose

> AppApiIcaroEndpointsICAROEffectiveDose200Response appApiIcaroEndpointsICAROEffectiveDose(origin, destination, year, month, day, opts)

Calculate the total effective dose along a great circle flight route. 

Effective Dose is a radiation protection quantity defined by the International Commission on  Radiological Protection (ICRP) and represents the stochastic health  risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. &lt;br&gt; &lt;br&gt; Use this endpoint if you need to estimate radiation exposures of personnel. &lt;br&gt; &lt;br&gt; This API can run in two modes: &lt;br&gt; &lt;br&gt; Either specify &lt;br&gt; &lt;b&gt;altitude&lt;/b&gt;, &lt;b&gt;duration&lt;/b&gt;&lt;br&gt; for constant altitude calculations; &lt;br&gt; &lt;br&gt; Or specify &lt;br&gt; &lt;b&gt;initial_altitude&lt;/b&gt;, &lt;b&gt;cruising_altitudes&lt;/b&gt;, &lt;b&gt;climb_times&lt;/b&gt;, &lt;b&gt;cruising_times&lt;/b&gt;, &lt;b&gt;descent_time&lt;/b&gt;, &lt;b&gt;final_altitude&lt;/b&gt;&lt;br&gt; to calculate dose accounting for a step climb. &lt;br&gt; &lt;br&gt; Note: the airport codes or coordinates (depending on which was specified), and the date in DD/MM/YYYY format, are echoed in the json response as strings. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.RoutedoseApi();
let origin = "YSSY"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport.
let destination = "33.94250107,-118.4079971"; // String | The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport.
let year = 2019; // Number | Year in YYYY.
let month = 5; // Number | Month in MM.
let day = 21; // Number | Day in DD.
let opts = {
  'altitude': 10.1, // Number | Altitude (in km). The minimum is 0 m, the maximum is 20 km.
  'duration': 5, // Number | The flight duration in hours. The minimum is 0, the maximum is 20 hrs.
  'initialAltitude': 0, // Number | Initial altitude (in km). The minimum is 0 m, the maximum is 20 km.
  'cruisingAltitudes': [null], // [Number] | Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km.
  'climbTimes': [null], // [Number] | Climb times for each cruising altitude (hours).
  'cruisingTimes': [null], // [Number] | Cruising times at each cruising altitude (hours).
  'descentTime': 0.5, // Number | Descent time from last cruising altitude to final altitude (hours).
  'finalAltitude': 0 // Number | Final altitude (in km).
};
apiInstance.appApiIcaroEndpointsICAROEffectiveDose(origin, destination, year, month, day, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the origin airport. | 
 **destination** | **String**| The ICAO code or IATA code or latitude,longitude pair (in decimal degrees) of the destination airport. | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] 
 **duration** | **Number**| The flight duration in hours. The minimum is 0, the maximum is 20 hrs. | [optional] 
 **initialAltitude** | **Number**| Initial altitude (in km). The minimum is 0 m, the maximum is 20 km. | [optional] 
 **cruisingAltitudes** | [**[Number]**](Number.md)| Cruising altitudes (in km). The minimum is 0 m, the maximum is 20 km. | [optional] 
 **climbTimes** | [**[Number]**](Number.md)| Climb times for each cruising altitude (hours). | [optional] 
 **cruisingTimes** | [**[Number]**](Number.md)| Cruising times at each cruising altitude (hours). | [optional] 
 **descentTime** | **Number**| Descent time from last cruising altitude to final altitude (hours). | [optional] 
 **finalAltitude** | **Number**| Final altitude (in km). | [optional] 

### Return type

[**AppApiIcaroEndpointsICAROEffectiveDose200Response**](AppApiIcaroEndpointsICAROEffectiveDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

