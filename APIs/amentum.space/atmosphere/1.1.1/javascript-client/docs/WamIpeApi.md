# AtmosphereApi.WamIpeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiWfsEndpointsWFSGetValues**](WamIpeApi.md#appApiWfsEndpointsWFSGetValues) | **GET** /wam-ipe | Forecast winds, ion and molecular densities, and temperatures in the atmosphere 



## appApiWfsEndpointsWFSGetValues

> AppApiWfsEndpointsWFSGetValues200Response appApiWfsEndpointsWFSGetValues(latitude, longitude, altitude, year, month, day, hour, minute)

Forecast winds, ion and molecular densities, and temperatures in the atmosphere 

at a given position and time on 42-48 hour forecast horizon (10 minute resolution). NOTE: latitudes outside the interval (-90,90) are clipped to the endpoints; longitudes outside (0,360) are wrapped.    

### Example

```javascript
import AtmosphereApi from 'atmosphere_api';

let apiInstance = new AtmosphereApi.WamIpeApi();
let latitude = 42; // Number | Latitude (deg) -90 to 90 deg
let longitude = 42; // Number | Longitude (deg) 0 to 360 deg or -180 to 180 deg
let altitude = 300; // Number | Altitude in (km)
let year = 2020; // Number | Year in YYYY format
let month = 5; // Number | Month in MM format
let day = 23; // Number | Day in DD format
let hour = 15; // Number | UTC Hour of the day in 24 hour format
let minute = 10; // Number | Minute of the given hour
apiInstance.appApiWfsEndpointsWFSGetValues(latitude, longitude, altitude, year, month, day, hour, minute, (error, data, response) => {
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
 **latitude** | **Number**| Latitude (deg) -90 to 90 deg | 
 **longitude** | **Number**| Longitude (deg) 0 to 360 deg or -180 to 180 deg | 
 **altitude** | **Number**| Altitude in (km) | 
 **year** | **Number**| Year in YYYY format | 
 **month** | **Number**| Month in MM format | 
 **day** | **Number**| Day in DD format | 
 **hour** | **Number**| UTC Hour of the day in 24 hour format | 
 **minute** | **Number**| Minute of the given hour | 

### Return type

[**AppApiWfsEndpointsWFSGetValues200Response**](AppApiWfsEndpointsWFSGetValues200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

