# Bng2latlong.DefaultApi

All URIs are relative to *https://api.getthedata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bng2latlongEastingNorthingGet**](DefaultApi.md#bng2latlongEastingNorthingGet) | **GET** /bng2latlong/{easting}/{northing} | Returns latitude and longitude for the given easting and northing.



## bng2latlongEastingNorthingGet

> Bng2latlongEastingNorthingGet200Response bng2latlongEastingNorthingGet(easting, northing)

Returns latitude and longitude for the given easting and northing.

Takes an OSGB36 easting and northing (British National Grid) and returns the geographically equivalent WGS84 latitude and longitude. #### A successful request returns the following fields: * status - this will be &#x60;ok&#x60; * easting - the easting provided in the request * northing - the northing provided in the request * latitude - the latitude of the converted coordinates * longitude - the longitude of the converted coordinates #### An unsuccessful request returns the following fields: * status - this will be &#x60;error&#x60; * error - an error message 

### Example

```javascript
import Bng2latlong from 'bng2latlong';

let apiInstance = new Bng2latlong.DefaultApi();
let easting = 326897; // Number | An OSGB36 (British National Grid) easting.
let northing = 673919; // Number | An OSGB36 (British National Grid) northing.
apiInstance.bng2latlongEastingNorthingGet(easting, northing, (error, data, response) => {
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
 **easting** | **Number**| An OSGB36 (British National Grid) easting. | 
 **northing** | **Number**| An OSGB36 (British National Grid) northing. | 

### Return type

[**Bng2latlongEastingNorthingGet200Response**](Bng2latlongEastingNorthingGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

