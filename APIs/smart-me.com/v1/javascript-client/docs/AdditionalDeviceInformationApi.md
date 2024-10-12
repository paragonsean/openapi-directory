# SmartMe.AdditionalDeviceInformationApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**additionalDeviceInformationGet**](AdditionalDeviceInformationApi.md#additionalDeviceInformationGet) | **GET** /api/AdditionalDeviceInformation/{id} | Gets the additional information (e.g. Firmware Version) about a device.



## additionalDeviceInformationGet

> AdditionalDeviceInformation additionalDeviceInformationGet(id)

Gets the additional information (e.g. Firmware Version) about a device.

Gets the additional information (e.g. Firmware Version) about a device.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.AdditionalDeviceInformationApi();
let id = "id_example"; // String | The ID of the device
apiInstance.additionalDeviceInformationGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the device | 

### Return type

[**AdditionalDeviceInformation**](AdditionalDeviceInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

