# SevenIoApi.LookupApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lookup**](LookupApi.md#lookup) | **POST** /lookup | 
[**lookupCnam**](LookupApi.md#lookupCnam) | **POST** /lookup/cnam | 
[**lookupFormat**](LookupApi.md#lookupFormat) | **POST** /lookup/format | 
[**lookupHlr**](LookupApi.md#lookupHlr) | **POST** /lookup/hlr | 
[**lookupMnp**](LookupApi.md#lookupMnp) | **POST** /lookup/mnp | 



## lookup

> lookup(type, number, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.LookupApi();
let type = "type_example"; // String | Allowed values are \"cnam\", \"format\", \"hlr\" and \"mnp\".
let number = ["null"]; // [String] | The phone number to look up.
let opts = {
  'json': "json_example" // String | Determines whether the response shall be returned in JSON format. Does not work with type \"format\".
};
apiInstance.lookup(type, number, opts, (error, data, response) => {
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
 **type** | **String**| Allowed values are \&quot;cnam\&quot;, \&quot;format\&quot;, \&quot;hlr\&quot; and \&quot;mnp\&quot;. | 
 **number** | [**[String]**](String.md)| The phone number to look up. | 
 **json** | **String**| Determines whether the response shall be returned in JSON format. Does not work with type \&quot;format\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lookupCnam

> lookupCnam(number)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.LookupApi();
let number = ["null"]; // [String] | The phone number to look up.
apiInstance.lookupCnam(number, (error, data, response) => {
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
 **number** | [**[String]**](String.md)| The phone number to look up. | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lookupFormat

> lookupFormat(number)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.LookupApi();
let number = ["null"]; // [String] | The phone number to look up.
apiInstance.lookupFormat(number, (error, data, response) => {
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
 **number** | [**[String]**](String.md)| The phone number to look up. | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lookupHlr

> lookupHlr(number)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.LookupApi();
let number = ["null"]; // [String] | The phone number to look up.
apiInstance.lookupHlr(number, (error, data, response) => {
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
 **number** | [**[String]**](String.md)| The phone number to look up. | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lookupMnp

> lookupMnp(number, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.LookupApi();
let number = ["null"]; // [String] | The phone number to look up.
let opts = {
  'json': "json_example" // String | Determines whether the response shall be returned in JSON format.
};
apiInstance.lookupMnp(number, opts, (error, data, response) => {
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
 **number** | [**[String]**](String.md)| The phone number to look up. | 
 **json** | **String**| Determines whether the response shall be returned in JSON format. | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

