# AviationRadiationApi.ParmaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiParmaEndpointsPARMAAmbientDose**](ParmaApi.md#appApiParmaEndpointsPARMAAmbientDose) | **GET** /parma/ambient_dose | The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 
[**appApiParmaEndpointsPARMADifferentialIntensity**](ParmaApi.md#appApiParmaEndpointsPARMADifferentialIntensity) | **GET** /parma/differential_intensity | The energy differential intensity of a particle at a given zenith angle.
[**appApiParmaEndpointsPARMAEffectiveDose**](ParmaApi.md#appApiParmaEndpointsPARMAEffectiveDose) | **GET** /parma/effective_dose | The effective dose rate calculated for a single particle type, or accumulated over all particle types. 



## appApiParmaEndpointsPARMAAmbientDose

> AppApiParmaEndpointsPARMAAmbientDose200Response appApiParmaEndpointsPARMAAmbientDose(latitude, longitude, year, month, day, particle, opts)

The ambient dose equivalent rate calculated for a single particle type, or accumulated over all particle types. 

The ambient dose equivalent, H*(10), is an operational quantity that simulates the  human body by measuring the dose equivalent at a depth of 10 mm within a tissue  equivalent sphere of 300 mm diameter. It is a measurable quantity that is  used to calibrate area monitors (radiation detectors) for mixed radiation fields.  Use this endpoint if you are comparing model predictions to measurements. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.ParmaApi();
let latitude = 30; // Number | Latitude. -90 (S) to 90 (N).
let longitude = 30; // Number | Longitude. -180 (W) to 180 (E).
let year = 2019; // Number | Year in YYYY.
let month = 12; // Number | Month in MM.
let day = 1; // Number | Day in DD.
let particle = "proton"; // String | The particle type as a string. Specifying 'total', only used for the dose calculation, returns the dose for all particle types. 
let opts = {
  'altitude': 11, // Number | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
  'atmosphericDepth': 0.92 // Number | Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
};
apiInstance.appApiParmaEndpointsPARMAAmbientDose(latitude, longitude, year, month, day, particle, opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude. -90 (S) to 90 (N). | 
 **longitude** | **Number**| Longitude. -180 (W) to 180 (E). | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **particle** | **String**| The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types.  | 
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | [optional] 
 **atmosphericDepth** | **Number**| Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both.  | [optional] 

### Return type

[**AppApiParmaEndpointsPARMAAmbientDose200Response**](AppApiParmaEndpointsPARMAAmbientDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiParmaEndpointsPARMADifferentialIntensity

> AppApiParmaEndpointsPARMADifferentialIntensity200Response appApiParmaEndpointsPARMADifferentialIntensity(latitude, longitude, year, month, day, particle, angle, opts)

The energy differential intensity of a particle at a given zenith angle.

The differential intensity of a particle is a directional quantity that describes the number of particles per unit area, per unit solid angle, per unit energy, and per unit time. The API leverages the functionality of PARMA to calculate differential intensity distributions with energies in units of MeV and Intensity in units of /cm2/sr/MeV/s. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.ParmaApi();
let latitude = 30; // Number | Latitude. -90 (S) to 90 (N).
let longitude = 30; // Number | Longitude. -180 (W) to 180 (E).
let year = 2019; // Number | Year in YYYY.
let month = 12; // Number | Month in MM.
let day = 1; // Number | Day in DD.
let particle = "proton"; // String | The particle type as a string. Specifying 'total', only used for the dose calculation, returns the dose for all particle types. 
let angle = 1; // Number | Direction cosine. 1.0 is in the downward direction.
let opts = {
  'altitude': 11, // Number | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
  'atmosphericDepth': 0.92 // Number | Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
};
apiInstance.appApiParmaEndpointsPARMADifferentialIntensity(latitude, longitude, year, month, day, particle, angle, opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude. -90 (S) to 90 (N). | 
 **longitude** | **Number**| Longitude. -180 (W) to 180 (E). | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **particle** | **String**| The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types.  | 
 **angle** | **Number**| Direction cosine. 1.0 is in the downward direction. | 
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | [optional] 
 **atmosphericDepth** | **Number**| Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both.  | [optional] 

### Return type

[**AppApiParmaEndpointsPARMADifferentialIntensity200Response**](AppApiParmaEndpointsPARMADifferentialIntensity200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiParmaEndpointsPARMAEffectiveDose

> AppApiParmaEndpointsPARMAEffectiveDose200Response appApiParmaEndpointsPARMAEffectiveDose(latitude, longitude, year, month, day, particle, opts)

The effective dose rate calculated for a single particle type, or accumulated over all particle types. 

Effective dose is a radiation protection quantity defined by the International Commission on Radiological Protection (ICRP) and represents the stochastic health risk to the human body at low levels of radiation. It accounts for the different sensitivities of organs to ionising radiation, as well as the different effectiveness of various types of radiation. Use this endpoint if you need to estimate radiation exposures of personnel. 

### Example

```javascript
import AviationRadiationApi from 'aviation_radiation_api';

let apiInstance = new AviationRadiationApi.ParmaApi();
let latitude = 30; // Number | Latitude. -90 (S) to 90 (N).
let longitude = 30; // Number | Longitude. -180 (W) to 180 (E).
let year = 2019; // Number | Year in YYYY.
let month = 12; // Number | Month in MM.
let day = 1; // Number | Day in DD.
let particle = "proton"; // String | The particle type as a string. Specifying 'total', only used for the dose calculation, returns the dose for all particle types. 
let opts = {
  'altitude': 11, // Number | Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere).
  'atmosphericDepth': 0.92 // Number | Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both. 
};
apiInstance.appApiParmaEndpointsPARMAEffectiveDose(latitude, longitude, year, month, day, particle, opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude. -90 (S) to 90 (N). | 
 **longitude** | **Number**| Longitude. -180 (W) to 180 (E). | 
 **year** | **Number**| Year in YYYY. | 
 **month** | **Number**| Month in MM. | 
 **day** | **Number**| Day in DD. | 
 **particle** | **String**| The particle type as a string. Specifying &#39;total&#39;, only used for the dose calculation, returns the dose for all particle types.  | 
 **altitude** | **Number**| Altitude (in km). The minimum is 0 m, the maximum is 47 km (the upper limit of the stratosphere). | [optional] 
 **atmosphericDepth** | **Number**| Atmospheric depth from the top of the atmosphere (in units of g/cm2). The minimum is 0.913 g/cm2, the maximum is 1032.66 g/cm2. WARNING: you can specify either altitude OR atmospheric depth, not both.  | [optional] 

### Return type

[**AppApiParmaEndpointsPARMAEffectiveDose200Response**](AppApiParmaEndpointsPARMAEffectiveDose200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

