# CorrentlyIo.DispatchGreenEnergyDistributionAPIApi

All URIs are relative to *https://api.corrently.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gsiDispatch_0**](DispatchGreenEnergyDistributionAPIApi.md#gsiDispatch_0) | **GET** /gsi/dispatch | Dispatch (Green Energy Distribution Schedule)



## gsiDispatch_0

> GsiDispatch200Response gsiDispatch_0(opts)

Dispatch (Green Energy Distribution Schedule)

Dispatch of green energy has two aspects to consider:   - Availability of gerneration facility (depends on weather and installed capacity)   - Demand of energy Using the green power index (GrünstromIndex) we have received a tool to automate distribution of energy in order to prevent redispatch situations. Doing this alows to opimize resource usage (tactical) and leverage data for investment planning (strategic). 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.DispatchGreenEnergyDistributionAPIApi();
let opts = {
  'zip': "zip_example", // String | Zipcode (Postleitzahl) of a city in Germany.
  'key': "key_example" // String | Any valid Stromkonto account (address).
};
apiInstance.gsiDispatch_0(opts, (error, data, response) => {
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
 **zip** | **String**| Zipcode (Postleitzahl) of a city in Germany. | [optional] 
 **key** | **String**| Any valid Stromkonto account (address). | [optional] 

### Return type

[**GsiDispatch200Response**](GsiDispatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

