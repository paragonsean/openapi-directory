# SvixApi.IntegrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIntegrationApiV1AppAppIdIntegrationPost**](IntegrationApi.md#createIntegrationApiV1AppAppIdIntegrationPost) | **POST** /api/v1/app/{app_id}/integration/ | Create Integration
[**deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete**](IntegrationApi.md#deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete) | **DELETE** /api/v1/app/{app_id}/integration/{integ_id}/ | Delete Integration
[**getIntegrationApiV1AppAppIdIntegrationIntegIdGet**](IntegrationApi.md#getIntegrationApiV1AppAppIdIntegrationIntegIdGet) | **GET** /api/v1/app/{app_id}/integration/{integ_id}/ | Get Integration
[**getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet**](IntegrationApi.md#getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet) | **GET** /api/v1/app/{app_id}/integration/{integ_id}/key/ | Get Integration Key
[**listIntegrationsApiV1AppAppIdIntegrationGet**](IntegrationApi.md#listIntegrationsApiV1AppAppIdIntegrationGet) | **GET** /api/v1/app/{app_id}/integration/ | List Integrations
[**rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost**](IntegrationApi.md#rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost) | **POST** /api/v1/app/{app_id}/integration/{integ_id}/key/rotate/ | Rotate Integration Key
[**updateIntegrationApiV1AppAppIdIntegrationIntegIdPut**](IntegrationApi.md#updateIntegrationApiV1AppAppIdIntegrationIntegIdPut) | **PUT** /api/v1/app/{app_id}/integration/{integ_id}/ | Update Integration



## createIntegrationApiV1AppAppIdIntegrationPost

> IntegrationOut createIntegrationApiV1AppAppIdIntegrationPost(appId, integrationIn, opts)

Create Integration

Create an integration.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let integrationIn = new SvixApi.IntegrationIn(); // IntegrationIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.createIntegrationApiV1AppAppIdIntegrationPost(appId, integrationIn, opts, (error, data, response) => {
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
 **integrationIn** | [**IntegrationIn**](IntegrationIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**IntegrationOut**](IntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete

> deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete(integId, appId, opts)

Delete Integration

Delete an integration and revoke it&#39;s key.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.deleteIntegrationApiV1AppAppIdIntegrationIntegIdDelete(integId, appId, opts, (error, data, response) => {
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
 **integId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationApiV1AppAppIdIntegrationIntegIdGet

> IntegrationOut getIntegrationApiV1AppAppIdIntegrationIntegIdGet(integId, appId, opts)

Get Integration

Get an integration.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getIntegrationApiV1AppAppIdIntegrationIntegIdGet(integId, appId, opts, (error, data, response) => {
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
 **integId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**IntegrationOut**](IntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet

> IntegrationKeyOut getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet(integId, appId, opts)

Get Integration Key

Get an integration&#39;s key.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyGet(integId, appId, opts, (error, data, response) => {
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
 **integId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**IntegrationKeyOut**](IntegrationKeyOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIntegrationsApiV1AppAppIdIntegrationGet

> ListResponseIntegrationOut listIntegrationsApiV1AppAppIdIntegrationGet(appId, opts)

List Integrations

List the application&#39;s integrations.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listIntegrationsApiV1AppAppIdIntegrationGet(appId, opts, (error, data, response) => {
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
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseIntegrationOut**](ListResponseIntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost

> IntegrationKeyOut rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost(integId, appId, opts)

Rotate Integration Key

Rotate the integration&#39;s key. The previous key will be immediately revoked.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.rotateIntegrationKeyApiV1AppAppIdIntegrationIntegIdKeyRotatePost(integId, appId, opts, (error, data, response) => {
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
 **integId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**IntegrationKeyOut**](IntegrationKeyOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateIntegrationApiV1AppAppIdIntegrationIntegIdPut

> IntegrationOut updateIntegrationApiV1AppAppIdIntegrationIntegIdPut(integId, appId, integrationUpdate, opts)

Update Integration

Update an integration.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.IntegrationApi();
let integId = "integ_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let integrationUpdate = new SvixApi.IntegrationUpdate(); // IntegrationUpdate | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.updateIntegrationApiV1AppAppIdIntegrationIntegIdPut(integId, appId, integrationUpdate, opts, (error, data, response) => {
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
 **integId** | **String**|  | 
 **appId** | **String**|  | 
 **integrationUpdate** | [**IntegrationUpdate**](IntegrationUpdate.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**IntegrationOut**](IntegrationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

