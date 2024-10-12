# SmartMe.DevicesByEnergyApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devicesByEnergyGet**](DevicesByEnergyApi.md#devicesByEnergyGet) | **GET** /api/DevicesByEnergy | Gets all Devices for an Energy Type



## devicesByEnergyGet

> [Device] devicesByEnergyGet(meterEnergyType)

Gets all Devices for an Energy Type

Gets all Devices for an Energy Type

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.DevicesByEnergyApi();
let meterEnergyType = "meterEnergyType_example"; // String | 
apiInstance.devicesByEnergyGet(meterEnergyType, (error, data, response) => {
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
 **meterEnergyType** | **String**|  | 

### Return type

[**[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

