# SmartMe.SmartMeDeviceConfigurationApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smartMeDeviceConfigurationGet**](SmartMeDeviceConfigurationApi.md#smartMeDeviceConfigurationGet) | **GET** /api/SmartMeDeviceConfiguration/{id} | Gets the configuration of a smart-me device.
[**smartMeDeviceConfigurationPost**](SmartMeDeviceConfigurationApi.md#smartMeDeviceConfigurationPost) | **POST** /api/SmartMeDeviceConfiguration | Sets the configuration of a smart-me device. The device needs to be online.



## smartMeDeviceConfigurationGet

> SmartMeDeviceConfigurationContainer smartMeDeviceConfigurationGet(id)

Gets the configuration of a smart-me device.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.SmartMeDeviceConfigurationApi();
let id = "id_example"; // String | 
apiInstance.smartMeDeviceConfigurationGet(id, (error, data, response) => {
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

[**SmartMeDeviceConfigurationContainer**](SmartMeDeviceConfigurationContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## smartMeDeviceConfigurationPost

> smartMeDeviceConfigurationPost(smartMeDeviceConfigurationContainer)

Sets the configuration of a smart-me device. The device needs to be online.

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.SmartMeDeviceConfigurationApi();
let smartMeDeviceConfigurationContainer = new SmartMe.SmartMeDeviceConfigurationContainer(); // SmartMeDeviceConfigurationContainer | 
apiInstance.smartMeDeviceConfigurationPost(smartMeDeviceConfigurationContainer, (error, data, response) => {
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
 **smartMeDeviceConfigurationContainer** | [**SmartMeDeviceConfigurationContainer**](SmartMeDeviceConfigurationContainer.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: Not defined

