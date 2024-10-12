# IoEIoTApiToCreateEndUserApplications.ActionApi

All URIs are relative to *https://ioe2api.ijenko.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deviceRun**](ActionApi.md#deviceRun) | **POST** /devices/{deviceId}/run/{action} | Run actions
[**functionalityRun**](ActionApi.md#functionalityRun) | **POST** /functionalities/{functionalityId}/run/{action} | Run an action
[**placeRun**](ActionApi.md#placeRun) | **POST** /places/{placeId}/run/{action} | Run actions



## deviceRun

> [ActionResult] deviceRun(deviceId, action, functionalities, _arguments)

Run actions

Run an *Action* on zero, one or multiple Functionalities selected with tags. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ActionApi();
let deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
let action = "action_example"; // String | Identifier of an *Action* inside a *Functionality*.
let functionalities = "functionalities_example"; // String | Functionality selector: Functionality tags or functionality class (optionally, '@' followed by a endpoint in decimal) or '*' for all. Multiple values are separated by '|' and are interpreted as « OR ». 
let _arguments = [null]; // [Object] | 
apiInstance.deviceRun(deviceId, action, functionalities, _arguments, (error, data, response) => {
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
 **deviceId** | **String**| Unique identifier of a *Device*. | 
 **action** | **String**| Identifier of an *Action* inside a *Functionality*. | 
 **functionalities** | **String**| Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ».  | 
 **_arguments** | [**[Object]**](Object.md)|  | 

### Return type

[**[ActionResult]**](ActionResult.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionalityRun

> ActionResult functionalityRun(functionalityId, action, _arguments)

Run an action

Run an action on the Functionality. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ActionApi();
let functionalityId = "functionalityId_example"; // String | Unique identifier of a *Functionality*.
let action = "action_example"; // String | Identifier of an *Action* inside a *Functionality*.
let _arguments = [null]; // [Object] | 
apiInstance.functionalityRun(functionalityId, action, _arguments, (error, data, response) => {
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
 **functionalityId** | **String**| Unique identifier of a *Functionality*. | 
 **action** | **String**| Identifier of an *Action* inside a *Functionality*. | 
 **_arguments** | [**[Object]**](Object.md)|  | 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## placeRun

> [ActionResult] placeRun(placeId, action, devices, functionalities, _arguments)

Run actions

Run an *Action* on zero, one or multiple *Functionalities* selected with tags.  *Device* and *Functionality* selection are combined with « AND ».  If no functionality is matched by the device/functionality selection, an empty array is returned. 

### Example

```javascript
import IoEIoTApiToCreateEndUserApplications from 'io_e_io_t_api_to_create_end_user_applications';
let defaultClient = IoEIoTApiToCreateEndUserApplications.ApiClient.instance;
// Configure API key authorization: Token in query
let Token in query = defaultClient.authentications['Token in query'];
Token in query.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in query.apiKeyPrefix = 'Token';
// Configure API key authorization: Token in Access-Token header
let Token in Access-Token header = defaultClient.authentications['Token in Access-Token header'];
Token in Access-Token header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token in Access-Token header.apiKeyPrefix = 'Token';

let apiInstance = new IoEIoTApiToCreateEndUserApplications.ActionApi();
let placeId = "placeId_example"; // String | Unique identifier of a *Place*.
let action = "action_example"; // String | Identifier of an *Action* inside a *Functionality*.
let devices = "devices_example"; // String | Devices selector. Device tags or device classes or device ids or '*' for any. Multiple values are separated by '|' and interpreted as « OR ».
let functionalities = "functionalities_example"; // String | Functionality selector: Functionality tags or functionality class (optionally, '@' followed by a endpoint in decimal) or '*' for all. Multiple values are separated by '|' and are interpreted as « OR ». 
let _arguments = [null]; // [Object] | 
apiInstance.placeRun(placeId, action, devices, functionalities, _arguments, (error, data, response) => {
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
 **placeId** | **String**| Unique identifier of a *Place*. | 
 **action** | **String**| Identifier of an *Action* inside a *Functionality*. | 
 **devices** | **String**| Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ». | 
 **functionalities** | **String**| Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ».  | 
 **_arguments** | [**[Object]**](Object.md)|  | 

### Return type

[**[ActionResult]**](ActionResult.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

