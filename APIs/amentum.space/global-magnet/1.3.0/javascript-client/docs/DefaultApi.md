# GeomagApi.DefaultApi

All URIs are relative to */wmm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiWmmEndpointsWMMMagneticField**](DefaultApi.md#appApiWmmEndpointsWMMMagneticField) | **GET** /magnetic_field | Calculate magnetic declination, inclination, total field intensity, and grid variation 



## appApiWmmEndpointsWMMMagneticField

> AppApiWmmEndpointsWMMMagneticField200Response appApiWmmEndpointsWMMMagneticField(altitude, latitude, longitude, year)

Calculate magnetic declination, inclination, total field intensity, and grid variation 

at specified conditions. 

### Example

```javascript
import GeomagApi from 'geomag_api';

let apiInstance = new GeomagApi.DefaultApi();
let altitude = 10; // Number | Geodetic Altitude 0 km to 600 km.
let latitude = 80; // Number | Geodetic Latitude. -90 deg (S) to 90 deg (N).
let longitude = 100; // Number | Geodetic Longitude. -180 deg (W) to 180 deg (E).
let year = 2020.5; // Number | Year as a decimal in the range 2015-2025 (2017.5 would be half way through 2017).
apiInstance.appApiWmmEndpointsWMMMagneticField(altitude, latitude, longitude, year, (error, data, response) => {
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
 **altitude** | **Number**| Geodetic Altitude 0 km to 600 km. | 
 **latitude** | **Number**| Geodetic Latitude. -90 deg (S) to 90 deg (N). | 
 **longitude** | **Number**| Geodetic Longitude. -180 deg (W) to 180 deg (E). | 
 **year** | **Number**| Year as a decimal in the range 2015-2025 (2017.5 would be half way through 2017). | 

### Return type

[**AppApiWmmEndpointsWMMMagneticField200Response**](AppApiWmmEndpointsWMMMagneticField200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

