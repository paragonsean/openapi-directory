# AppStoreConnectApi.IdfaDeclarationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idfaDeclarationsCreateInstance**](IdfaDeclarationsApi.md#idfaDeclarationsCreateInstance) | **POST** /v1/idfaDeclarations | 
[**idfaDeclarationsDeleteInstance**](IdfaDeclarationsApi.md#idfaDeclarationsDeleteInstance) | **DELETE** /v1/idfaDeclarations/{id} | 
[**idfaDeclarationsUpdateInstance**](IdfaDeclarationsApi.md#idfaDeclarationsUpdateInstance) | **PATCH** /v1/idfaDeclarations/{id} | 



## idfaDeclarationsCreateInstance

> IdfaDeclarationResponse idfaDeclarationsCreateInstance(idfaDeclarationCreateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.IdfaDeclarationsApi();
let idfaDeclarationCreateRequest = new AppStoreConnectApi.IdfaDeclarationCreateRequest(); // IdfaDeclarationCreateRequest | IdfaDeclaration representation
apiInstance.idfaDeclarationsCreateInstance(idfaDeclarationCreateRequest, (error, data, response) => {
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
 **idfaDeclarationCreateRequest** | [**IdfaDeclarationCreateRequest**](IdfaDeclarationCreateRequest.md)| IdfaDeclaration representation | 

### Return type

[**IdfaDeclarationResponse**](IdfaDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## idfaDeclarationsDeleteInstance

> idfaDeclarationsDeleteInstance(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.IdfaDeclarationsApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.idfaDeclarationsDeleteInstance(id, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idfaDeclarationsUpdateInstance

> IdfaDeclarationResponse idfaDeclarationsUpdateInstance(id, idfaDeclarationUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.IdfaDeclarationsApi();
let id = "id_example"; // String | the id of the requested resource
let idfaDeclarationUpdateRequest = new AppStoreConnectApi.IdfaDeclarationUpdateRequest(); // IdfaDeclarationUpdateRequest | IdfaDeclaration representation
apiInstance.idfaDeclarationsUpdateInstance(id, idfaDeclarationUpdateRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **idfaDeclarationUpdateRequest** | [**IdfaDeclarationUpdateRequest**](IdfaDeclarationUpdateRequest.md)| IdfaDeclaration representation | 

### Return type

[**IdfaDeclarationResponse**](IdfaDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

