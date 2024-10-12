# SmartMe.FastSendDeviceValuesApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fastSendDeviceValuesGet**](FastSendDeviceValuesApi.md#fastSendDeviceValuesGet) | **GET** /api/FastSendDeviceValues/{id} | Force a device to send the data every second (if supported). This for about 30s.              Don&#39;t use this call to force a device to send the data every second for a longer time.



## fastSendDeviceValuesGet

> fastSendDeviceValuesGet(id)

Force a device to send the data every second (if supported). This for about 30s.              Don&#39;t use this call to force a device to send the data every second for a longer time.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.FastSendDeviceValuesApi();
let id = "id_example"; // String | 
apiInstance.fastSendDeviceValuesGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

