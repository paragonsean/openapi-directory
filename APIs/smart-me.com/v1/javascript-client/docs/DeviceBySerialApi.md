# SmartMe.DeviceBySerialApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deviceBySerialGet**](DeviceBySerialApi.md#deviceBySerialGet) | **GET** /api/DeviceBySerial | Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.



## deviceBySerialGet

> Device deviceBySerialGet(serial)

Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.

Gets a Device by it&#39;s Serial Number. The Serial is the part before the \&quot;-\&quot;.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DeviceBySerialApi();
let serial = 789; // Number | The Serial Number of the device
apiInstance.deviceBySerialGet(serial, (error, data, response) => {
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
 **serial** | **Number**| The Serial Number of the device | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

