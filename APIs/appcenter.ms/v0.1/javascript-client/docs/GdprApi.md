# AppCenterClient.GdprApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataSubjectRightCancelDeleteRequest**](GdprApi.md#dataSubjectRightCancelDeleteRequest) | **POST** /v0.1/user/dsr/delete/{token}/cancel | 
[**dataSubjectRightCancelExportRequest**](GdprApi.md#dataSubjectRightCancelExportRequest) | **POST** /v0.1/user/dsr/export/{token}/cancel | 
[**dataSubjectRightDeleteRequest**](GdprApi.md#dataSubjectRightDeleteRequest) | **POST** /v0.1/user/dsr/delete | 
[**dataSubjectRightDeleteStatusRequest**](GdprApi.md#dataSubjectRightDeleteStatusRequest) | **GET** /v0.1/user/dsr/delete/{token} | 
[**dataSubjectRightExportRequest**](GdprApi.md#dataSubjectRightExportRequest) | **POST** /v0.1/user/dsr/export | 
[**dataSubjectRightExportStatusRequest**](GdprApi.md#dataSubjectRightExportStatusRequest) | **GET** /v0.1/user/dsr/export/{token} | 



## dataSubjectRightCancelDeleteRequest

> DataSubjectRightDeleteRequest202Response dataSubjectRightCancelDeleteRequest(token, opts)



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.GdprApi();
let token = "token_example"; // String | Unique request ID (GUID)
let opts = {
  'dataSubjectRightCancelDeleteRequestRequest': new AppCenterClient.DataSubjectRightCancelDeleteRequestRequest() // DataSubjectRightCancelDeleteRequestRequest | 
};
apiInstance.dataSubjectRightCancelDeleteRequest(token, opts, (error, data, response) => {
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
 **token** | **String**| Unique request ID (GUID) | 
 **dataSubjectRightCancelDeleteRequestRequest** | [**DataSubjectRightCancelDeleteRequestRequest**](DataSubjectRightCancelDeleteRequestRequest.md)|  | [optional] 

### Return type

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataSubjectRightCancelExportRequest

> DataSubjectRightDeleteRequest202Response dataSubjectRightCancelExportRequest(token)



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.GdprApi();
let token = "token_example"; // String | Unique request ID (GUID)
apiInstance.dataSubjectRightCancelExportRequest(token, (error, data, response) => {
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
 **token** | **String**| Unique request ID (GUID) | 

### Return type

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSubjectRightDeleteRequest

> DataSubjectRightDeleteRequest202Response dataSubjectRightDeleteRequest()



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.GdprApi();
apiInstance.dataSubjectRightDeleteRequest((error, data, response) => {
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

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSubjectRightDeleteStatusRequest

> DataSubjectRightDeleteStatusRequest200Response dataSubjectRightDeleteStatusRequest(token, email)



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.GdprApi();
let token = "token_example"; // String | Unique request ID (GUID)
let email = "email_example"; // String | Email used for delete with x-authz-bypass headers
apiInstance.dataSubjectRightDeleteStatusRequest(token, email, (error, data, response) => {
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
 **token** | **String**| Unique request ID (GUID) | 
 **email** | **String**| Email used for delete with x-authz-bypass headers | 

### Return type

[**DataSubjectRightDeleteStatusRequest200Response**](DataSubjectRightDeleteStatusRequest200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSubjectRightExportRequest

> DataSubjectRightDeleteRequest202Response dataSubjectRightExportRequest()



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.GdprApi();
apiInstance.dataSubjectRightExportRequest((error, data, response) => {
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

[**DataSubjectRightDeleteRequest202Response**](DataSubjectRightDeleteRequest202Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataSubjectRightExportStatusRequest

> DataSubjectRightDeleteStatusRequest200Response dataSubjectRightExportStatusRequest(token)



### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.GdprApi();
let token = "token_example"; // String | Unique request ID (GUID)
apiInstance.dataSubjectRightExportStatusRequest(token, (error, data, response) => {
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
 **token** | **String**| Unique request ID (GUID) | 

### Return type

[**DataSubjectRightDeleteStatusRequest200Response**](DataSubjectRightDeleteStatusRequest200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

