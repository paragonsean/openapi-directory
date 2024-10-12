# SmartMe.CustomDeviceApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCustomDeviceIdGet**](CustomDeviceApi.md#apiCustomDeviceIdGet) | **GET** /api/CustomDevice/{id} | Gets a Custom Device by it&#39;s ID
[**customDeviceGet**](CustomDeviceApi.md#customDeviceGet) | **GET** /api/CustomDevice | Gets all Custom Devices
[**customDevicePost**](CustomDeviceApi.md#customDevicePost) | **POST** /api/CustomDevice | Creates or updates a Custom Device or updates it&#39;s values.



## apiCustomDeviceIdGet

> CustomDeviceToPost apiCustomDeviceIdGet(id)

Gets a Custom Device by it&#39;s ID

Gets a Device by it&#39;s ID

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.CustomDeviceApi();
let id = "id_example"; // String | The ID of the device
apiInstance.apiCustomDeviceIdGet(id, (error, data, response) => {
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

[**CustomDeviceToPost**](CustomDeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customDeviceGet

> [CustomDeviceToPost] customDeviceGet()

Gets all Custom Devices

Gets all Devices

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.CustomDeviceApi();
apiInstance.customDeviceGet((error, data, response) => {
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

[**[CustomDeviceToPost]**](CustomDeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customDevicePost

> CustomDeviceToPost customDevicePost(customDeviceToPost)

Creates or updates a Custom Device or updates it&#39;s values.

Creates or updates a Custom Device or updates it&#39;s values.              A Custom Device can be any device that like to add some measurement values to the smart-me Cloud.              Only use a custom device for all non meters.              For a new device leave the ID empty. To create a device you have to set the DeviceEnergyType.              To update values, add the ID of the device and the values you like to set.  (See the Data Type Model for more Information)

### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.CustomDeviceApi();
let customDeviceToPost = new SmartMe.CustomDeviceToPost(); // CustomDeviceToPost | Device object with all the data
apiInstance.customDevicePost(customDeviceToPost, (error, data, response) => {
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
 **customDeviceToPost** | [**CustomDeviceToPost**](CustomDeviceToPost.md)| Device object with all the data | 

### Return type

[**CustomDeviceToPost**](CustomDeviceToPost.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

