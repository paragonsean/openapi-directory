# AviationRadiationApi.Cari7Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiCari7EndpointsCARI7AmbientDose**](Cari7Api.md#appApiCari7EndpointsCARI7AmbientDose) | **GET** /cari7/ambient_dose | The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 
[**appApiCari7EndpointsCARI7EffectiveDose**](Cari7Api.md#appApiCari7EndpointsCARI7EffectiveDose) | **GET** /cari7/effective_dose | The effective dose rate calculated for a single particle type, or accumulated over all particle types. 



## appApiCari7EndpointsCARI7AmbientDose

> AppApiCari7EndpointsCARI7AmbientDose200Response appApiCari7EndpointsCARI7AmbientDose(altitude, latitude, longitude, year, month, day, utc, particle)

The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 

The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  Use this endpoint if you are comparing model predictions to measurements. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.Cari7Api();
let altitude = 11; // Number | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
let latitude = 30; // Number | Latitude. -90 (S) to 90 (N).
let longitude = 30; // Number | Longitude. -180 (W) to 180 (E).
let year = 2019; // Number | Year in YYYY.
let month = 12; // Number | Month in MM.
let day = 1; // Number | Day in DD.
let utc = 3; // Number | Hour in 24 hour time.
let particle = "total"; // String | The particle type as a string. Specifying 'total' returns the dose for all particle types. 
apiInstance.appApiCari7EndpointsCARI7AmbientDose(altitude, latitude, longitude, year, month, day, utc, particle, (error, data, response) => {
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
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | 
 **latitude** | **Number**| Latitude. -90 (S) to 90 (N). | 
 **longitude** | **Number**| Longitude. -180 (W) to 180 (E). | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **utc** | **Number**| Hour in 24 hour time. | 
 **particle** | **String**| The particle type as a string. Specifying &#39;total&#39; returns the dose for all particle types.  | 

### Return type

[**AppApiCari7EndpointsCARI7AmbientDose200Response**](AppApiCari7EndpointsCARI7AmbientDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiCari7EndpointsCARI7EffectiveDose

> AppApiCari7EndpointsCARI7EffectiveDose200Response appApiCari7EndpointsCARI7EffectiveDose(altitude, latitude, longitude, year, month, day, utc, particle)

The effective dose rate calculated for a single particle type, or accumulated over all particle types. 

Effective Dose is a radiation protection quantity defined by the International Commission on  Radiological Protection (ICRP) and represents the stochastic health  risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. Use this endpoint if you need to estimate radiation exposures of personnel. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.Cari7Api();
let altitude = 11; // Number | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
let latitude = 30; // Number | Latitude. -90 (S) to 90 (N).
let longitude = 30; // Number | Longitude. -180 (W) to 180 (E).
let year = 2019; // Number | Year in YYYY.
let month = 12; // Number | Month in MM.
let day = 1; // Number | Day in DD.
let utc = 3; // Number | Hour in 24 hour time.
let particle = "total"; // String | The particle type as a string. Specifying 'total' returns the dose for all particle types. 
apiInstance.appApiCari7EndpointsCARI7EffectiveDose(altitude, latitude, longitude, year, month, day, utc, particle, (error, data, response) => {
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
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | 
 **latitude** | **Number**| Latitude. -90 (S) to 90 (N). | 
 **longitude** | **Number**| Longitude. -180 (W) to 180 (E). | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **utc** | **Number**| Hour in 24 hour time. | 
 **particle** | **String**| The particle type as a string. Specifying &#39;total&#39; returns the dose for all particle types.  | 

### Return type

[**AppApiCari7EndpointsCARI7EffectiveDose200Response**](AppApiCari7EndpointsCARI7EffectiveDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

