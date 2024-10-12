# SvixApi.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expireAllApiV1AuthAppAppIdExpireAllPost**](AuthenticationApi.md#expireAllApiV1AuthAppAppIdExpireAllPost) | **POST** /api/v1/auth/app/{app_id}/expire-all/ | Expire All
[**getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost**](AuthenticationApi.md#getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost) | **POST** /api/v1/auth/app-portal-access/{app_id}/ | Get Consumer App Portal Access
[**getDashboardAccessApiV1AuthDashboardAccessAppIdPost**](AuthenticationApi.md#getDashboardAccessApiV1AuthDashboardAccessAppIdPost) | **POST** /api/v1/auth/dashboard-access/{app_id}/ | Get Dashboard Access
[**logoutApiV1AuthLogoutPost**](AuthenticationApi.md#logoutApiV1AuthLogoutPost) | **POST** /api/v1/auth/logout/ | Logout



## expireAllApiV1AuthAppAppIdExpireAllPost

> expireAllApiV1AuthAppAppIdExpireAllPost(appId, applicationTokenExpireIn, opts)

Expire All

Expire all of the tokens associated with a specific Application

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.AuthenticationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let applicationTokenExpireIn = new SvixApi.ApplicationTokenExpireIn(); // ApplicationTokenExpireIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.expireAllApiV1AuthAppAppIdExpireAllPost(appId, applicationTokenExpireIn, opts, (error, data, response) => {
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
 **applicationTokenExpireIn** | [**ApplicationTokenExpireIn**](ApplicationTokenExpireIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost

> AppPortalAccessOut getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost(appId, appPortalAccessIn, opts)

Get Consumer App Portal Access

Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.AuthenticationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appPortalAccessIn = new SvixApi.AppPortalAccessIn(); // AppPortalAccessIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getAppPortalAccessApiV1AuthAppPortalAccessAppIdPost(appId, appPortalAccessIn, opts, (error, data, response) => {
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
 **appPortalAccessIn** | [**AppPortalAccessIn**](AppPortalAccessIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**AppPortalAccessOut**](AppPortalAccessOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDashboardAccessApiV1AuthDashboardAccessAppIdPost

> DashboardAccessOut getDashboardAccessApiV1AuthDashboardAccessAppIdPost(appId, opts)

Get Dashboard Access

DEPRECATED: Please use &#x60;app-portal-access&#x60; instead.  Use this function to get magic links (and authentication codes) for connecting your users to the Consumer Application Portal.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.AuthenticationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getDashboardAccessApiV1AuthDashboardAccessAppIdPost(appId, opts, (error, data, response) => {
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

[**DashboardAccessOut**](DashboardAccessOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logoutApiV1AuthLogoutPost

> logoutApiV1AuthLogoutPost(opts)

Logout

Logout an app token.  Trying to log out other tokens will fail.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.AuthenticationApi();
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.logoutApiV1AuthLogoutPost(opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

