# SmartMe.PicoChargingHistoryApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**picoChargingHistoryGet**](PicoChargingHistoryApi.md#picoChargingHistoryGet) | **GET** /api/pico/history/{id} | Gets the last charging history for a pico station



## picoChargingHistoryGet

> [PicoChargingHistoryData] picoChargingHistoryGet(id)

Gets the last charging history for a pico station

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.PicoChargingHistoryApi();
let id = "id_example"; // String | 
apiInstance.picoChargingHistoryGet(id, (error, data, response) => {
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

[**[PicoChargingHistoryData]**](PicoChargingHistoryData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

