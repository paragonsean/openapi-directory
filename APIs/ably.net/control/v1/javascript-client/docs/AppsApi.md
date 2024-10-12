# ApiV1.AppsApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountIdAppsGet**](AppsApi.md#accountsAccountIdAppsGet) | **GET** /accounts/{account_id}/apps | Lists account apps
[**accountsAccountIdAppsPost**](AppsApi.md#accountsAccountIdAppsPost) | **POST** /accounts/{account_id}/apps | Creates an app
[**appsIdDelete**](AppsApi.md#appsIdDelete) | **DELETE** /apps/{id} | Deletes an app
[**appsIdPatch**](AppsApi.md#appsIdPatch) | **PATCH** /apps/{id} | Updates an app
[**appsIdPkcs12Post**](AppsApi.md#appsIdPkcs12Post) | **POST** /apps/{id}/pkcs12 | Updates app&#39;s APNS info from a .p12 file



## accountsAccountIdAppsGet

> [AppResponse] accountsAccountIdAppsGet(accountId)

Lists account apps

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.AppsApi();
let accountId = "accountId_example"; // String | 
apiInstance.accountsAccountIdAppsGet(accountId, (error, data, response) => {
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
 **accountId** | **String**|  | 

### Return type

[**[AppResponse]**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsAccountIdAppsPost

> AppResponse accountsAccountIdAppsPost(accountId, opts)

Creates an app

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.AppsApi();
let accountId = "accountId_example"; // String | 
let opts = {
  'appPost': new ApiV1.AppPost() // AppPost | 
};
apiInstance.accountsAccountIdAppsPost(accountId, opts, (error, data, response) => {
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
 **accountId** | **String**|  | 
 **appPost** | [**AppPost**](AppPost.md)|  | [optional] 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsIdDelete

> appsIdDelete(id)

Deletes an app

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.AppsApi();
let id = "id_example"; // String | 
apiInstance.appsIdDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsIdPatch

> AppResponse appsIdPatch(id, opts)

Updates an app

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.AppsApi();
let id = "id_example"; // String | 
let opts = {
  'appPatch': new ApiV1.AppPatch() // AppPatch | 
};
apiInstance.appsIdPatch(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **appPatch** | [**AppPatch**](AppPatch.md)|  | [optional] 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsIdPkcs12Post

> AppResponse appsIdPkcs12Post(id, p12File, p12Pass)

Updates app&#39;s APNS info from a .p12 file

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.AppsApi();
let id = "id_example"; // String | 
let p12File = "/path/to/file"; // File | 
let p12Pass = "p12Pass_example"; // String | 
apiInstance.appsIdPkcs12Post(id, p12File, p12Pass, (error, data, response) => {
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
 **id** | **String**|  | 
 **p12File** | **File**|  | 
 **p12Pass** | **String**|  | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

