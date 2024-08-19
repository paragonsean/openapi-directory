# GravityApi.Egm2008Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appApiEgm2008EndpointsEGM2008CalculateAnomaly**](Egm2008Api.md#appApiEgm2008EndpointsEGM2008CalculateAnomaly) | **GET** /egm2008/gravity_anomaly | Calculate gravity anomaly values 
[**appApiEgm2008EndpointsEGM2008CalculateHeight**](Egm2008Api.md#appApiEgm2008EndpointsEGM2008CalculateHeight) | **GET** /egm2008/geoid_height | Calculate the geoid height 



## appApiEgm2008EndpointsEGM2008CalculateAnomaly

> Anomaly appApiEgm2008EndpointsEGM2008CalculateAnomaly(latitude, longitude)

Calculate gravity anomaly values 

for a given latitude / longitude. 

### Example

```javascript
import GravityApi from 'gravity_api';

let apiInstance = new GravityApi.Egm2008Api();
let latitude = -45; // Number | Geographic latitude (-90 to 90 deg).
let longitude = 45; // Number | Geographic longitude (-180 to 180 deg).
apiInstance.appApiEgm2008EndpointsEGM2008CalculateAnomaly(latitude, longitude, (error, data, response) => {
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
 **latitude** | **Number**| Geographic latitude (-90 to 90 deg). | 
 **longitude** | **Number**| Geographic longitude (-180 to 180 deg). | 

### Return type

[**Anomaly**](Anomaly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appApiEgm2008EndpointsEGM2008CalculateHeight

> Height appApiEgm2008EndpointsEGM2008CalculateHeight(latitude, longitude)

Calculate the geoid height 

for a given latitude / longitude.  

### Example

```javascript
import GravityApi from 'gravity_api';

let apiInstance = new GravityApi.Egm2008Api();
let latitude = -45; // Number | Geographic latitude (-90 to 90 deg).
let longitude = 45; // Number | Geographic longitude (-180 to 180 deg).
apiInstance.appApiEgm2008EndpointsEGM2008CalculateHeight(latitude, longitude, (error, data, response) => {
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
 **latitude** | **Number**| Geographic latitude (-90 to 90 deg). | 
 **longitude** | **Number**| Geographic longitude (-180 to 180 deg). | 

### Return type

[**Height**](Height.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

