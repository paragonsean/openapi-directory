# TransportForLondonUnifiedApi.ModeApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modeArrivals**](ModeApi.md#modeArrivals) | **GET** /Mode/{mode}/Arrivals | Gets the next arrival predictions for all stops of a given mode
[**modeGetActiveServiceTypes**](ModeApi.md#modeGetActiveServiceTypes) | **GET** /Mode/ActiveServiceTypes | Returns the service type active for a mode.              Currently only supports tube



## modeArrivals

> [TflApiPresentationEntitiesPrediction] modeArrivals(mode, opts)

Gets the next arrival predictions for all stops of a given mode

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.ModeApi();
let mode = "mode_example"; // String | A mode name e.g. tube, dlr
let opts = {
  'count': 56 // Number | A number of arrivals to return for each stop, -1 to return all available.
};
apiInstance.modeArrivals(mode, opts, (error, data, response) => {
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
 **mode** | **String**| A mode name e.g. tube, dlr | 
 **count** | **Number**| A number of arrivals to return for each stop, -1 to return all available. | [optional] 

### Return type

[**[TflApiPresentationEntitiesPrediction]**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## modeGetActiveServiceTypes

> [TflApiPresentationEntitiesActiveServiceType] modeGetActiveServiceTypes()

Returns the service type active for a mode.              Currently only supports tube

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.ModeApi();
apiInstance.modeGetActiveServiceTypes((error, data, response) => {
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

[**[TflApiPresentationEntitiesActiveServiceType]**](TflApiPresentationEntitiesActiveServiceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

