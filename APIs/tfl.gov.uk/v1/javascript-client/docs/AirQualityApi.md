# TransportForLondonUnifiedApi.AirQualityApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**airQualityGet**](AirQualityApi.md#airQualityGet) | **GET** /AirQuality | Gets air quality data feed



## airQualityGet

> Object airQualityGet()

Gets air quality data feed

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.AirQualityApi();
apiInstance.airQualityGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

