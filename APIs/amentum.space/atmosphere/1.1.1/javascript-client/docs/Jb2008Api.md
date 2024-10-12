# AtmosphereApi.Jb2008Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiEndpointsJB2008SampleAtmosphere**](Jb2008Api.md#appApiEndpointsJB2008SampleAtmosphere) | **GET** /jb2008 | Compute atmospheric density and temperatures 



## appApiEndpointsJB2008SampleAtmosphere

> AppApiEndpointsJB2008SampleAtmosphere200Response appApiEndpointsJB2008SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc)

Compute atmospheric density and temperatures 

under given conditions. 

### Example

```javascript
import AtmosphereApi from 'atmosphere_api';

let apiInstance = new AtmosphereApi.Jb2008Api();
let year = 2020; // Number | Year in YYYY format
let month = 5; // Number | Month in MM format
let day = 23; // Number | Day in DD format
let altitude = 300; // Number | Altitude in (km)
let geodeticLatitude = 42; // Number | GeodeticLatitude (deg) -90 to 90 deg
let geodeticLongitude = 42; // Number | GeodeticLongitude (deg) 0 to 360 deg
let utc = 2; // Number | Coordinated Universal Time (hrs)
apiInstance.appApiEndpointsJB2008SampleAtmosphere(year, month, day, altitude, geodeticLatitude, geodeticLongitude, utc, (error, data, response) => {
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

### Return type

[**AppApiEndpointsJB2008SampleAtmosphere200Response**](AppApiEndpointsJB2008SampleAtmosphere200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

