# BackgroundRemovalApi.FetchAccountInfoApi

All URIs are relative to *https://api.remove.bg/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountGet**](FetchAccountInfoApi.md#accountGet) | **GET** /account | Fetch credit balance and free API calls.



## accountGet

> AccountGet200Response accountGet()

Fetch credit balance and free API calls.

Get the current credit balance and number of free API calls.  Notes:  * Balance changes may be delayed by several seconds. To locally keep track of your credit balance, you should therefore only call this endpoint initially (or e.g. when the user manually triggers a refresh), then use the &#x60;X-Credits-Charged&#x60; response header returned with each image processing response to adjust the local balance.  * The \&quot;*sizes*\&quot; field is always \&quot;all\&quot;, is deprecated and will soon be removed. 

### Example

```javascript
import BackgroundRemovalApi from 'background_removal_api';
let defaultClient = BackgroundRemovalApi.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new BackgroundRemovalApi.FetchAccountInfoApi();
apiInstance.accountGet((error, data, response) => {
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

[**AccountGet200Response**](AccountGet200Response.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

