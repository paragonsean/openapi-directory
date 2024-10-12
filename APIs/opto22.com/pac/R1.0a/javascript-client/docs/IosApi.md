# PacControlRestApi.IosApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readAnalogInputEu_0**](IosApi.md#readAnalogInputEu_0) | **GET** /device/strategy/ios/analogInputs/{ioName}/eu | 
[**readAnalogInputs_0**](IosApi.md#readAnalogInputs_0) | **GET** /device/strategy/ios/analogInputs | 
[**readAnalogOutputEu_0**](IosApi.md#readAnalogOutputEu_0) | **GET** /device/strategy/ios/analogOutputs/{ioName}/eu | 
[**readAnalogOutputs_0**](IosApi.md#readAnalogOutputs_0) | **GET** /device/strategy/ios/analogOutputs | 
[**readDigitalInputState_0**](IosApi.md#readDigitalInputState_0) | **GET** /device/strategy/ios/digitalInputs/{ioName}/state | 
[**readDigitalInputs_0**](IosApi.md#readDigitalInputs_0) | **GET** /device/strategy/ios/digitalInputs | 
[**readDigitalOutputState_0**](IosApi.md#readDigitalOutputState_0) | **GET** /device/strategy/ios/digitalOutputs/{ioName}/state | 
[**readDigitalOutputs_0**](IosApi.md#readDigitalOutputs_0) | **GET** /device/strategy/ios/digitalOutputs | 
[**writeAnalogOutputEu_0**](IosApi.md#writeAnalogOutputEu_0) | **POST** /device/strategy/ios/analogOutputs/{ioName}/eu | 
[**writeDigitalOutputState_0**](IosApi.md#writeDigitalOutputState_0) | **POST** /device/strategy/ios/digitalOutputs/{ioName}/state | 



## readAnalogInputEu_0

> FloatValueObject readAnalogInputEu_0(ioName)



Reads the value in engineering units (EU) of the specified analog input

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
let ioName = "ioName_example"; // String | Name of the analog input point to read
apiInstance.readAnalogInputEu_0(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of the analog input point to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readAnalogInputs_0

> [FloatVar] readAnalogInputs_0()



Returns the name and engineering units (EU) for all analog input points in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
apiInstance.readAnalogInputs_0((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readAnalogOutputEu_0

> FloatValueObject readAnalogOutputEu_0(ioName)



Reads the value in engineering units (EU) of the specified analog output

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
let ioName = "ioName_example"; // String | Name of analog output point to read
apiInstance.readAnalogOutputEu_0(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of analog output point to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readAnalogOutputs_0

> [FloatVar] readAnalogOutputs_0()



Returns the name and engineering units (EU) for all analog output points in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
apiInstance.readAnalogOutputs_0((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalInputState_0

> DigitalPointStateObject readDigitalInputState_0(ioName)



Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
let ioName = "ioName_example"; // String | Name of the digital input point to read
apiInstance.readDigitalInputState_0(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of the digital input point to read | 

### Return type

[**DigitalPointStateObject**](DigitalPointStateObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalInputs_0

> [DigitalPointStateVar] readDigitalInputs_0()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
apiInstance.readDigitalInputs_0((error, data, response) => {
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

[**[DigitalPointStateVar]**](DigitalPointStateVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalOutputState_0

> DigitalPointStateObject readDigitalOutputState_0(ioName)



Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
let ioName = "ioName_example"; // String | Name of the digit output point to read
apiInstance.readDigitalOutputState_0(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of the digit output point to read | 

### Return type

[**DigitalPointStateObject**](DigitalPointStateObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalOutputs_0

> [DigitalPointStateVar] readDigitalOutputs_0()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
apiInstance.readDigitalOutputs_0((error, data, response) => {
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

[**[DigitalPointStateVar]**](DigitalPointStateVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## writeAnalogOutputEu_0

> writeAnalogOutputEu_0(ioName, body)



Sets the value of the specified analog output point

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
let ioName = "ioName_example"; // String | Name of the analog output point to write
let body = new PacControlRestApi.FloatValueObject(); // FloatValueObject | Value to write
apiInstance.writeAnalogOutputEu_0(ioName, body, (error, data, response) => {
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
 **ioName** | **String**| Name of the analog output point to write | 
 **body** | [**FloatValueObject**](FloatValueObject.md)| Value to write | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeDigitalOutputState_0

> writeDigitalOutputState_0(ioName, body)



Sets the value of the specified digital output point

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.IosApi();
let ioName = "ioName_example"; // String | Name of the digital output point to write
let body = new PacControlRestApi.DigitalPointStateObject(); // DigitalPointStateObject | Value to write
apiInstance.writeDigitalOutputState_0(ioName, body, (error, data, response) => {
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
 **ioName** | **String**| Name of the digital output point to write | 
 **body** | [**DigitalPointStateObject**](DigitalPointStateObject.md)| Value to write | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

