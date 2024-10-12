# SmartMe.PicoChargingApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**picoChargingGet**](PicoChargingApi.md#picoChargingGet) | **GET** /api/pico/charging/{id} | Gets the active charging data of a pico station



## picoChargingGet

> PicoChargingData picoChargingGet(id)

Gets the active charging data of a pico station

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoChargingApi();
let id = "id_example"; // String | 
apiInstance.picoChargingGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**PicoChargingData**](PicoChargingData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

