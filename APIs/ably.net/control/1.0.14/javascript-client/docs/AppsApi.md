# ControlApiV1.AppsApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountIdAppsGet**](AppsApi.md#accountsAccountIdAppsGet) | **GET** /accounts/{account_id}/apps | Lists apps
[**accountsAccountIdAppsPost**](AppsApi.md#accountsAccountIdAppsPost) | **POST** /accounts/{account_id}/apps | Creates an app
[**appsIdDelete**](AppsApi.md#appsIdDelete) | **DELETE** /apps/{id} | Deletes an app
[**appsIdPatch**](AppsApi.md#appsIdPatch) | **PATCH** /apps/{id} | Updates an app
[**appsIdPkcs12Post**](AppsApi.md#appsIdPkcs12Post) | **POST** /apps/{id}/pkcs12 | Updates app&#39;s APNs info from a &#x60;.p12&#x60; file



## accountsAccountIdAppsGet

> [AppResponse] accountsAccountIdAppsGet(accountId)

Lists apps

List all applications for the specified account ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.AppsApi();
let accountId = "accountId_example"; // String | The account ID for which to retrieve the associated applications.
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
 **accountId** | **String**| The account ID for which to retrieve the associated applications. | 

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

Creates an application with the specified properties.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.AppsApi();
let accountId = "accountId_example"; // String | The account ID of the account in which to create the application.
let opts = {
  'appPost': new ControlApiV1.AppPost() // AppPost | 
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
 **accountId** | **String**| The account ID of the account in which to create the application. | 
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

Deletes the application with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.AppsApi();
let id = "id_example"; // String | The ID of the application to be deleted.
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
 **id** | **String**| The ID of the application to be deleted. | 

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

Updates the application with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.AppsApi();
let id = "id_example"; // String | The ID of application to be updated.
let opts = {
  'appPatch': new ControlApiV1.AppPatch() // AppPatch | 
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
 **id** | **String**| The ID of application to be updated. | 
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

Updates app&#39;s APNs info from a &#x60;.p12&#x60; file

Updates the application&#39;s Apple Push Notification service (APNs) information.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.AppsApi();
let id = "id_example"; // String | The application ID.
let p12File = "/path/to/file"; // File | The `.p12` file containing the app's APNs information.
let p12Pass = "p12Pass_example"; // String | The password for the corresponding `.p12` file.
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
 **id** | **String**| The application ID. | 
 **p12File** | **File**| The &#x60;.p12&#x60; file containing the app&#39;s APNs information. | 
 **p12Pass** | **String**| The password for the corresponding &#x60;.p12&#x60; file. | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

