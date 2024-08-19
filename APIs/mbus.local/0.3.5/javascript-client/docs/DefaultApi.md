# MBusHttpdApi.DefaultApi

All URIs are relative to *http://mbus.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](DefaultApi.md#get) | **POST** /mbus/get/{device}/{baudrate}/{address} | 
[**getMulti**](DefaultApi.md#getMulti) | **POST** /mbus/getMulti/{device}/{baudrate}/{address}/{maxframes} | 
[**hat**](DefaultApi.md#hat) | **GET** /mbus/hat | 
[**hatOff**](DefaultApi.md#hatOff) | **POST** /mbus/hat/off | 
[**hatOn**](DefaultApi.md#hatOn) | **POST** /mbus/hat/on | 
[**mbusApi**](DefaultApi.md#mbusApi) | **GET** /mbus/api | 
[**scan**](DefaultApi.md#scan) | **POST** /mbus/scan/{device}/{baudrate} | 



## get

> String get(device, baudrate, address)



Gets data from the slave identified by {address}

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
let device = "ttyAMA0"; // String | The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
let baudrate = new MBusHttpdApi.Baudrate(); // Baudrate | Baudrate to communicate with M-Bus devices
let address = "48"; // String | The slave device to get data from
apiInstance.get(device, baudrate, address, (error, data, response) => {
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
 **device** | **String**| The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning | 
 **baudrate** | [**Baudrate**](.md)| Baudrate to communicate with M-Bus devices | 
 **address** | **String**| The slave device to get data from | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, text/plain


## getMulti

> String getMulti(device, baudrate, address, maxframes)



Gets data from the slave identified by {address}, and supports multiple responses from the slave

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
let device = "ttyAMA0"; // String | The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
let baudrate = new MBusHttpdApi.Baudrate(); // Baudrate | Baudrate to communicate with M-Bus devices
let address = "48"; // String | The slave device to get data from
let maxframes = 16; // Number | The slave device to get data from
apiInstance.getMulti(device, baudrate, address, maxframes, (error, data, response) => {
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
 **device** | **String**| The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning | 
 **baudrate** | [**Baudrate**](.md)| Baudrate to communicate with M-Bus devices | 
 **address** | **String**| The slave device to get data from | 
 **maxframes** | **Number**| The slave device to get data from | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, text/plain


## hat

> Hat hat()



Gets Raspberry Pi Hat information

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
apiInstance.hat((error, data, response) => {
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

[**Hat**](Hat.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## hatOff

> hatOff()



Turns off power to the M-Bus

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
apiInstance.hatOff((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## hatOn

> hatOn()



Turns on power to the M-Bus

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
apiInstance.hatOn((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## mbusApi

> String mbusApi()



Returns this API specification

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
apiInstance.mbusApi((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/x-yaml, text/plain


## scan

> String scan(device, baudrate)



Scan the specified device for slaves

### Example

```javascript
import MBusHttpdApi from 'm_bus_httpd_api';

let apiInstance = new MBusHttpdApi.DefaultApi();
let device = "ttyAMA0"; // String | The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
let baudrate = new MBusHttpdApi.Baudrate(); // Baudrate | Baudrate to communicate with M-Bus devices
apiInstance.scan(device, baudrate, (error, data, response) => {
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
 **device** | **String**| The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning | 
 **baudrate** | [**Baudrate**](.md)| Baudrate to communicate with M-Bus devices | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

