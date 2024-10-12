# SvixApi.ApplicationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplicationApiV1AppPost**](ApplicationApi.md#createApplicationApiV1AppPost) | **POST** /api/v1/app/ | Create Application
[**deleteApplicationApiV1AppAppIdDelete**](ApplicationApi.md#deleteApplicationApiV1AppAppIdDelete) | **DELETE** /api/v1/app/{app_id}/ | Delete Application
[**getApplicationApiV1AppAppIdGet**](ApplicationApi.md#getApplicationApiV1AppAppIdGet) | **GET** /api/v1/app/{app_id}/ | Get Application
[**listApplicationsApiV1AppGet**](ApplicationApi.md#listApplicationsApiV1AppGet) | **GET** /api/v1/app/ | List Applications
[**updateApplicationApiV1AppAppIdPut**](ApplicationApi.md#updateApplicationApiV1AppAppIdPut) | **PUT** /api/v1/app/{app_id}/ | Update Application



## createApplicationApiV1AppPost

> ApplicationOut createApplicationApiV1AppPost(applicationIn, opts)

Create Application

Create a new application.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.ApplicationApi();
let applicationIn = new SvixApi.ApplicationIn(); // ApplicationIn | 
let opts = {
  'getIfExists': false, // Boolean | Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.createApplicationApiV1AppPost(applicationIn, opts, (error, data, response) => {
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
 **applicationIn** | [**ApplicationIn**](ApplicationIn.md)|  | 
 **getIfExists** | **Boolean**| Get an existing application, or create a new one if doesn&#39;t exist. It&#39;s two separate functions in the libs. | [optional] [default to false]
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ApplicationOut**](ApplicationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplicationApiV1AppAppIdDelete

> deleteApplicationApiV1AppAppIdDelete(appId, opts)

Delete Application

Delete an application.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.ApplicationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.deleteApplicationApiV1AppAppIdDelete(appId, opts, (error, data, response) => {
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
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationApiV1AppAppIdGet

> ApplicationOut getApplicationApiV1AppAppIdGet(appId, opts)

Get Application

Get an application.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.ApplicationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getApplicationApiV1AppAppIdGet(appId, opts, (error, data, response) => {
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
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ApplicationOut**](ApplicationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplicationsApiV1AppGet

> ListResponseApplicationOut listApplicationsApiV1AppGet(opts)

List Applications

List of all the organization&#39;s applications.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.ApplicationApi();
let opts = {
  'iterator': "app_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'order': new SvixApi.Ordering(), // Ordering | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listApplicationsApiV1AppGet(opts, (error, data, response) => {
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
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **order** | [**Ordering**](.md)|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseApplicationOut**](ListResponseApplicationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApplicationApiV1AppAppIdPut

> ApplicationOut updateApplicationApiV1AppAppIdPut(appId, applicationIn, opts)

Update Application

Update an application.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.ApplicationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let applicationIn = new SvixApi.ApplicationIn(); // ApplicationIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.updateApplicationApiV1AppAppIdPut(appId, applicationIn, opts, (error, data, response) => {
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
 **appId** | **String**|  | 
 **applicationIn** | [**ApplicationIn**](ApplicationIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ApplicationOut**](ApplicationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

