# AtmosphereApi.Nrlmsise00Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiEndpointsNRLMSISE00SampleAtmosphere**](Nrlmsise00Api.md#appApiEndpointsNRLMSISE00SampleAtmosphere) | **GET** /nrlmsise00 | Compute atmospheric composition, density, and temperatures 



## appApiEndpointsNRLMSISE00SampleAtmosphere

> AppApiEndpointsNRLMSISE00SampleAtmosphere200Response appApiEndpointsNRLMSISE00SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc, opts)

Compute atmospheric composition, density, and temperatures 

at specified conditions. 

### Example

```javascript
import AtmosphereApi from 'atmosphere_api';

let apiInstance = new AtmosphereApi.Nrlmsise00Api();
let year = 2020; // Number | Year in YYYY format
let month = 5; // Number | Month in MM format
let day = 23; // Number | Day in DD format
let altitude = 300; // Number | Altitude in (km)
let geodeticLatitude = 42; // Number | GeodeticLatitude (deg) -90 to 90 deg
let geodeticLongitude = 42; // Number | GeodeticLongitude (deg) 0 to 360 deg
let utc = 2; // Number | Coordinated Universal Time (hrs)
let opts = {
  'f107a': 120, // Number | (Optional) 81 day average of F10.7 flux (SFU) centered on the specified day. F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically. 
  'f107': 120, // Number | (Optional) Daily F10.7 cm radio flux for previous day (SFU). F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically. 
  'ap': 30 // Number | (Optional) The Ap-index provides a daily average level for geomagnetic activity F107, F107A, AP effects can be neglected below 80 km. If unspecified, the average of values in the 24 hours preceding the date-time  are automatically calculated from data provided by GFZ German Research Centre  for Geosciences. 
};
apiInstance.appApiEndpointsNRLMSISE00SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc, opts, (error, data, response) => {
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
 **year** | **Number**| Year in YYYY format | 
 **month** | **Number**| Month in MM format | 
 **day** | **Number**| Day in DD format | 
 **altitude** | **Number**| Altitude in (km) | 
 **geodeticLatitude** | **Number**| GeodeticLatitude (deg) -90 to 90 deg | 
 **geodeticLongitude** | **Number**| GeodeticLongitude (deg) 0 to 360 deg | 
 **utc** | **Number**| Coordinated Universal Time (hrs) | 
 **f107a** | **Number**| (Optional) 81 day average of F10.7 flux (SFU) centered on the specified day. F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically.  | [optional] 
 **f107** | **Number**| (Optional) Daily F10.7 cm radio flux for previous day (SFU). F107 and F107A values correspond to the 10.7 cm radio flux at the actual distance of Earth from Sun rather than radio flux at 1 AU. F107, F107A, AP effects can be neglected below 80 km. If unspecified, values provided by the US National Oceanic and  Atmospheric Administration are retrieved automatically.  | [optional] 
 **ap** | **Number**| (Optional) The Ap-index provides a daily average level for geomagnetic activity F107, F107A, AP effects can be neglected below 80 km. If unspecified, the average of values in the 24 hours preceding the date-time  are automatically calculated from data provided by GFZ German Research Centre  for Geosciences.  | [optional] 

### Return type

[**AppApiEndpointsNRLMSISE00SampleAtmosphere200Response**](AppApiEndpointsNRLMSISE00SampleAtmosphere200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

