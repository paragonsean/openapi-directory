# BrowshotApi.BrowserApi

All URIs are relative to *https://api.browshot.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBrowserInfo**](BrowserApi.md#getBrowserInfo) | **GET** /browser/info | Get information about a browser
[**getBrowsersInfo**](BrowserApi.md#getBrowsersInfo) | **GET** /browser/list | Get all browsers



## getBrowserInfo

> Browser getBrowserInfo(id)

Get information about a browser

Get information about a browser.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.BrowserApi();
let id = 56; // Number | browser ID
apiInstance.getBrowserInfo(id, (error, data, response) => {
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
 **id** | **Number**| browser ID | 

### Return type

[**Browser**](Browser.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBrowsersInfo

> BrowserList getBrowsersInfo()

Get all browsers

Get all browsers.

### Example

```javascript
import BrowshotApi from 'browshot_api';
let defaultClient = BrowshotApi.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';

let apiInstance = new BrowshotApi.BrowserApi();
apiInstance.getBrowsersInfo((error, data, response) => {
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

[**BrowserList**](BrowserList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

