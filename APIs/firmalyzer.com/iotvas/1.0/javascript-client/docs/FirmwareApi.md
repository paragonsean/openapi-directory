# IoTvasApi.FirmwareApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAccounts**](FirmwareApi.md#getAccounts) | **GET** /firmware/{firmware_hash}/accounts | Get default accounts and password hashes of a firmware
[**getConfigIssues**](FirmwareApi.md#getConfigIssues) | **GET** /firmware/{firmware_hash}/config-issues | Get default OS configuration issues of a device firmware
[**getExpiredCerts**](FirmwareApi.md#getExpiredCerts) | **GET** /firmware/{firmware_hash}/expired-certs | Get expired digital certificates embedded in a device firmware
[**getPrivateKeys**](FirmwareApi.md#getPrivateKeys) | **GET** /firmware/{firmware_hash}/private-keys | Get private crypto keys embedded in a device firmware
[**getRisk**](FirmwareApi.md#getRisk) | **GET** /firmware/{firmware_hash}/risk | Get iot device firmware risk analysis
[**getWeakCerts**](FirmwareApi.md#getWeakCerts) | **GET** /firmware/{firmware_hash}/weak-certs | Get certificates with weak fingerprinting algorithms that are mebedded in a device firmware
[**getWeakKeys**](FirmwareApi.md#getWeakKeys) | **GET** /firmware/{firmware_hash}/weak-keys | Get weak crypto keys with short length



## getAccounts

> [DefaultAccount] getAccounts(firmwareHash)

Get default accounts and password hashes of a firmware

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "af88b1aaac0b222df8539f3ae1479b5c8eaeae41f1776b5dd2fa805cb33a1175"; // String | SHA2 hash of device firmware
apiInstance.getAccounts(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**[DefaultAccount]**](DefaultAccount.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfigIssues

> [ConfigIssue] getConfigIssues(firmwareHash)

Get default OS configuration issues of a device firmware

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "aa96e4d41a4b0ceb3f1ae4d94f3cb445621b9501e3a9c69e6b9eb37c5888a03c"; // String | SHA2 hash of device firmware
apiInstance.getConfigIssues(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**[ConfigIssue]**](ConfigIssue.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExpiredCerts

> [ExpiredCert] getExpiredCerts(firmwareHash)

Get expired digital certificates embedded in a device firmware

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "ac7c090c34338ea6a3b335004755e24578e7e4eee739c5c33736f0822b64907e"; // String | SHA2 hash of device firmware
apiInstance.getExpiredCerts(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**[ExpiredCert]**](ExpiredCert.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrivateKeys

> [CryptoKey] getPrivateKeys(firmwareHash)

Get private crypto keys embedded in a device firmware

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "90e3e68e1c61850f20c50e551816d47d484d7feb46890f5bc0a0e0dab3e3ba0b"; // String | SHA2 hash of device firmware
apiInstance.getPrivateKeys(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**[CryptoKey]**](CryptoKey.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRisk

> FirmwareRisk getRisk(firmwareHash)

Get iot device firmware risk analysis

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "af88b1aaac0b222df8539f3ae1479b5c8eaeae41f1776b5dd2fa805cb33a1175"; // String | SHA2 hash of device firmware
apiInstance.getRisk(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**FirmwareRisk**](FirmwareRisk.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWeakCerts

> [WeakCert] getWeakCerts(firmwareHash)

Get certificates with weak fingerprinting algorithms that are mebedded in a device firmware

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "52841661d61e00649451cc471e9b56d169df8041926b1252bb3fd0710c27b12c"; // String | SHA2 hash of device firmware
apiInstance.getWeakCerts(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**[WeakCert]**](WeakCert.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWeakKeys

> [CryptoKey] getWeakKeys(firmwareHash)

Get weak crypto keys with short length

### Example

```javascript
import IoTvasApi from 'io_tvas_api';
let defaultClient = IoTvasApi.ApiClient.instance;
// Configure API key authorization: api-key-header
let api-key-header = defaultClient.authentications['api-key-header'];
api-key-header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key-header.apiKeyPrefix = 'Token';

let apiInstance = new IoTvasApi.FirmwareApi();
let firmwareHash = "852031776c09f8152c90496f2c3fac85b46a938d20612d7fc03eea8aab46f23e"; // String | SHA2 hash of device firmware
apiInstance.getWeakKeys(firmwareHash, (error, data, response) => {
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
 **firmwareHash** | **String**| SHA2 hash of device firmware | 

### Return type

[**[CryptoKey]**](CryptoKey.md)

### Authorization

[api-key-header](../README.md#api-key-header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

