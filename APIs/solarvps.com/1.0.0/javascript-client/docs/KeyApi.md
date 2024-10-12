# SolarVps.KeyApi

All URIs are relative to *http://api.ss.solarvps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyGenerateGet**](KeyApi.md#keyGenerateGet) | **GET** /key/generate | Generate API Key
[**keyGetGet**](KeyApi.md#keyGetGet) | **GET** /key/get | Get API Key



## keyGenerateGet

> keyGenerateGet(username, password)

Generate API Key

API Key is regenerated if it already exists

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.KeyApi();
let username = "username_example"; // String | Email address used to login to SolarSystem
let password = "password_example"; // String | Password used to login to SolarSystem
apiInstance.keyGenerateGet(username, password, (error, data, response) => {
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
 **username** | **String**| Email address used to login to SolarSystem | 
 **password** | **String**| Password used to login to SolarSystem | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## keyGetGet

> keyGetGet(username, password)

Get API Key

Gets the API Key for user

### Example

```javascript
import SolarVps from 'solar_vps';
let defaultClient = SolarVps.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new SolarVps.KeyApi();
let username = "username_example"; // String | Email address used to login to SolarSystem
let password = "password_example"; // String | Password used to login to SolarSystem
apiInstance.keyGetGet(username, password, (error, data, response) => {
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
 **username** | **String**| Email address used to login to SolarSystem | 
 **password** | **String**| Password used to login to SolarSystem | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

