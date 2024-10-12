# SmartMe.DevicesBySubTypeApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesBySubTypeGet**](DevicesBySubTypeApi.md#devicesBySubTypeGet) | **GET** /api/DevicesBySubType | Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)



## devicesBySubTypeGet

> [Device] devicesBySubTypeGet(meterSubType)

Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)

Gets all Devices by it&#39;s Sub Type (e.g. E-Charging Station)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DevicesBySubTypeApi();
let meterSubType = "meterSubType_example"; // String | 
apiInstance.devicesBySubTypeGet(meterSubType, (error, data, response) => {
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
 **meterSubType** | **String**|  | 

### Return type

[**[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

