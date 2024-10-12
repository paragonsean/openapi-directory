# RudderApi.CVEApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkCVE**](CVEApi.md#checkCVE) | **POST** /cve/check | Trigger a CVE check
[**getAllCve**](CVEApi.md#getAllCve) | **GET** /cve | Get all CVE details
[**getCVECheckConfiguration**](CVEApi.md#getCVECheckConfiguration) | **GET** /cve/check/config | Get CVE check config
[**getCVEList**](CVEApi.md#getCVEList) | **POST** /cve/list | Get a list of CVE details
[**getCve**](CVEApi.md#getCve) | **GET** /cve/{cveId} | Get a CVE details
[**getLastCVECheck**](CVEApi.md#getLastCVECheck) | **GET** /cve/check/last | Get last CVE check result
[**readCVEfromFS**](CVEApi.md#readCVEfromFS) | **POST** /cve/update/fs | Update CVE database from file system
[**updateCVE**](CVEApi.md#updateCVE) | **POST** /cve/update | Update CVE database from remote source
[**updateCVECheckConfiguration**](CVEApi.md#updateCVECheckConfiguration) | **POST** /cve/check/config | Update cve check config



## checkCVE

> CheckCVE200Response checkCVE()

Trigger a CVE check

Trigger a CVE check

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
apiInstance.checkCVE((error, data, response) => {
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

[**CheckCVE200Response**](CheckCVE200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllCve

> GetAllCve200Response getAllCve()

Get all CVE details

Get all CVE details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
apiInstance.getAllCve((error, data, response) => {
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

[**GetAllCve200Response**](GetAllCve200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCVECheckConfiguration

> GetCVECheckConfiguration200Response getCVECheckConfiguration()

Get CVE check config

Get CVE check config

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
apiInstance.getCVECheckConfiguration((error, data, response) => {
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

[**GetCVECheckConfiguration200Response**](GetCVECheckConfiguration200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCVEList

> GetCVEList200Response getCVEList(opts)

Get a list of CVE details

Get CVE details, from a list passed as parameter

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
let opts = {
  'getCVEListRequest': new RudderApi.GetCVEListRequest() // GetCVEListRequest | 
};
apiInstance.getCVEList(opts, (error, data, response) => {
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
 **getCVEListRequest** | [**GetCVEListRequest**](GetCVEListRequest.md)|  | [optional] 

### Return type

[**GetCVEList200Response**](GetCVEList200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCve

> GetCve200Response getCve(cveId)

Get a CVE details

Get a CVE details

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
let cveId = "cveId_example"; // String | Id of the CVE
apiInstance.getCve(cveId, (error, data, response) => {
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
 **cveId** | **String**| Id of the CVE | 

### Return type

[**GetCve200Response**](GetCve200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLastCVECheck

> GetLastCVECheck200Response getLastCVECheck(opts)

Get last CVE check result

Get last CVE check result

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
let opts = {
  'groupId': "groupId_example", // String | Id of node groups you want to get from last CVE check
  'nodeId': "nodeId_example", // String | Id of nodes you want to get from last CVE check
  'cveId': "cveId_example", // String | Id of CVE you want to get from last CVE check
  '_package': "_package_example", // String | Name of packages you want to get from last CVE check
  'severity': "severity_example" // String | Severity of the CVE you want to get from last CVE check
};
apiInstance.getLastCVECheck(opts, (error, data, response) => {
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
 **groupId** | **String**| Id of node groups you want to get from last CVE check | [optional] 
 **nodeId** | **String**| Id of nodes you want to get from last CVE check | [optional] 
 **cveId** | **String**| Id of CVE you want to get from last CVE check | [optional] 
 **_package** | **String**| Name of packages you want to get from last CVE check | [optional] 
 **severity** | **String**| Severity of the CVE you want to get from last CVE check | [optional] 

### Return type

[**GetLastCVECheck200Response**](GetLastCVECheck200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readCVEfromFS

> ReadCVEfromFS200Response readCVEfromFS()

Update CVE database from file system

Update CVE database from file system

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
apiInstance.readCVEfromFS((error, data, response) => {
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

[**ReadCVEfromFS200Response**](ReadCVEfromFS200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCVE

> UpdateCVE200Response updateCVE(opts)

Update CVE database from remote source

Update CVE database from remote source

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
let opts = {
  'updateCVERequest': new RudderApi.UpdateCVERequest() // UpdateCVERequest | 
};
apiInstance.updateCVE(opts, (error, data, response) => {
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
 **updateCVERequest** | [**UpdateCVERequest**](UpdateCVERequest.md)|  | [optional] 

### Return type

[**UpdateCVE200Response**](UpdateCVE200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCVECheckConfiguration

> UpdateCVECheckConfiguration200Response updateCVECheckConfiguration(opts)

Update cve check config

Update cve check config

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.CVEApi();
let opts = {
  'updateCVECheckConfigurationRequest': new RudderApi.UpdateCVECheckConfigurationRequest() // UpdateCVECheckConfigurationRequest | 
};
apiInstance.updateCVECheckConfiguration(opts, (error, data, response) => {
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
 **updateCVECheckConfigurationRequest** | [**UpdateCVECheckConfigurationRequest**](UpdateCVECheckConfigurationRequest.md)|  | [optional] 

### Return type

[**UpdateCVECheckConfiguration200Response**](UpdateCVECheckConfiguration200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

