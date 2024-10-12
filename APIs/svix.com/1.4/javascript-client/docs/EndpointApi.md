# SvixApi.EndpointApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEndpointApiV1AppAppIdEndpointPost**](EndpointApi.md#createEndpointApiV1AppAppIdEndpointPost) | **POST** /api/v1/app/{app_id}/endpoint/ | Create Endpoint
[**deleteEndpointApiV1AppAppIdEndpointEndpointIdDelete**](EndpointApi.md#deleteEndpointApiV1AppAppIdEndpointEndpointIdDelete) | **DELETE** /api/v1/app/{app_id}/endpoint/{endpoint_id}/ | Delete Endpoint
[**getEndpointApiV1AppAppIdEndpointEndpointIdGet**](EndpointApi.md#getEndpointApiV1AppAppIdEndpointEndpointIdGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/ | Get Endpoint
[**getEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersGet**](EndpointApi.md#getEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/headers/ | Get Endpoint Headers
[**getEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretGet**](EndpointApi.md#getEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/secret/ | Get Endpoint Secret
[**getEndpointStatsApiV1AppAppIdEndpointEndpointIdStatsGet**](EndpointApi.md#getEndpointStatsApiV1AppAppIdEndpointEndpointIdStatsGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/stats/ | Get Endpoint Stats
[**getEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationGet**](EndpointApi.md#getEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/transformation/ | Get Endpoint Transformation
[**listEndpointsApiV1AppAppIdEndpointGet**](EndpointApi.md#listEndpointsApiV1AppAppIdEndpointGet) | **GET** /api/v1/app/{app_id}/endpoint/ | List Endpoints
[**patchEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPatch**](EndpointApi.md#patchEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPatch) | **PATCH** /api/v1/app/{app_id}/endpoint/{endpoint_id}/headers/ | Patch Endpoint Headers
[**recoverFailedWebhooksApiV1AppAppIdEndpointEndpointIdRecoverPost**](EndpointApi.md#recoverFailedWebhooksApiV1AppAppIdEndpointEndpointIdRecoverPost) | **POST** /api/v1/app/{app_id}/endpoint/{endpoint_id}/recover/ | Recover Failed Webhooks
[**replayMissingWebhooksApiV1AppAppIdEndpointEndpointIdReplayMissingPost**](EndpointApi.md#replayMissingWebhooksApiV1AppAppIdEndpointEndpointIdReplayMissingPost) | **POST** /api/v1/app/{app_id}/endpoint/{endpoint_id}/replay-missing/ | Replay Missing Webhooks
[**rotateEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretRotatePost**](EndpointApi.md#rotateEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretRotatePost) | **POST** /api/v1/app/{app_id}/endpoint/{endpoint_id}/secret/rotate/ | Rotate Endpoint Secret
[**sendEventTypeExampleMessageApiV1AppAppIdEndpointEndpointIdSendExamplePost**](EndpointApi.md#sendEventTypeExampleMessageApiV1AppAppIdEndpointEndpointIdSendExamplePost) | **POST** /api/v1/app/{app_id}/endpoint/{endpoint_id}/send-example/ | Send Event Type Example Message
[**setEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationPatch**](EndpointApi.md#setEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationPatch) | **PATCH** /api/v1/app/{app_id}/endpoint/{endpoint_id}/transformation/ | Set Endpoint Transformation
[**updateEndpointApiV1AppAppIdEndpointEndpointIdPut**](EndpointApi.md#updateEndpointApiV1AppAppIdEndpointEndpointIdPut) | **PUT** /api/v1/app/{app_id}/endpoint/{endpoint_id}/ | Update Endpoint
[**updateEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPut**](EndpointApi.md#updateEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPut) | **PUT** /api/v1/app/{app_id}/endpoint/{endpoint_id}/headers/ | Update Endpoint Headers



## createEndpointApiV1AppAppIdEndpointPost

> EndpointOut createEndpointApiV1AppAppIdEndpointPost(appId, endpointIn, opts)

Create Endpoint

Create a new endpoint for the application.  When &#x60;secret&#x60; is &#x60;null&#x60; the secret is automatically generated (recommended)

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointIn = new SvixApi.EndpointIn(); // EndpointIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.createEndpointApiV1AppAppIdEndpointPost(appId, endpointIn, opts, (error, data, response) => {
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
 **endpointIn** | [**EndpointIn**](EndpointIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointOut**](EndpointOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEndpointApiV1AppAppIdEndpointEndpointIdDelete

> deleteEndpointApiV1AppAppIdEndpointEndpointIdDelete(endpointId, appId, opts)

Delete Endpoint

Delete an endpoint.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.deleteEndpointApiV1AppAppIdEndpointEndpointIdDelete(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEndpointApiV1AppAppIdEndpointEndpointIdGet

> EndpointOut getEndpointApiV1AppAppIdEndpointEndpointIdGet(endpointId, appId, opts)

Get Endpoint

Get an application.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getEndpointApiV1AppAppIdEndpointEndpointIdGet(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointOut**](EndpointOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersGet

> EndpointHeadersOut getEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersGet(endpointId, appId, opts)

Get Endpoint Headers

Get the additional headers to be sent with the webhook

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersGet(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointHeadersOut**](EndpointHeadersOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretGet

> EndpointSecretOut getEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretGet(endpointId, appId, opts)

Get Endpoint Secret

Get the endpoint&#39;s signing secret.  This is used to verify the authenticity of the webhook. For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretGet(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointSecretOut**](EndpointSecretOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEndpointStatsApiV1AppAppIdEndpointEndpointIdStatsGet

> EndpointStats getEndpointStatsApiV1AppAppIdEndpointEndpointIdStatsGet(endpointId, appId, opts)

Get Endpoint Stats

Get basic statistics for the endpoint.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'until': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getEndpointStatsApiV1AppAppIdEndpointEndpointIdStatsGet(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **since** | **Date**|  | [optional] 
 **until** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointStats**](EndpointStats.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationGet

> EndpointTransformationOut getEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationGet(endpointId, appId, opts)

Get Endpoint Transformation

Get the transformation code associated with this endpoint

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationGet(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointTransformationOut**](EndpointTransformationOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEndpointsApiV1AppAppIdEndpointGet

> ListResponseEndpointOut listEndpointsApiV1AppAppIdEndpointGet(appId, opts)

List Endpoints

List the application&#39;s endpoints.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'order': new SvixApi.Ordering(), // Ordering | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listEndpointsApiV1AppAppIdEndpointGet(appId, opts, (error, data, response) => {
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
 **order** | [**Ordering**](.md)|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseEndpointOut**](ListResponseEndpointOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPatch

> patchEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPatch(appId, endpointId, endpointHeadersPatchIn, opts)

Patch Endpoint Headers

Partially set the additional headers to be sent with the webhook

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointHeadersPatchIn = new SvixApi.EndpointHeadersPatchIn(); // EndpointHeadersPatchIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.patchEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPatch(appId, endpointId, endpointHeadersPatchIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **endpointHeadersPatchIn** | [**EndpointHeadersPatchIn**](EndpointHeadersPatchIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## recoverFailedWebhooksApiV1AppAppIdEndpointEndpointIdRecoverPost

> RecoverOut recoverFailedWebhooksApiV1AppAppIdEndpointEndpointIdRecoverPost(appId, endpointId, recoverIn, opts)

Recover Failed Webhooks

Resend all failed messages since a given time.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let recoverIn = new SvixApi.RecoverIn(); // RecoverIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.recoverFailedWebhooksApiV1AppAppIdEndpointEndpointIdRecoverPost(appId, endpointId, recoverIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **recoverIn** | [**RecoverIn**](RecoverIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**RecoverOut**](RecoverOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replayMissingWebhooksApiV1AppAppIdEndpointEndpointIdReplayMissingPost

> ReplayOut replayMissingWebhooksApiV1AppAppIdEndpointEndpointIdReplayMissingPost(appId, endpointId, replayIn, opts)

Replay Missing Webhooks

Replays messages to the endpoint. Only messages that were created after &#x60;since&#x60; will be sent. Messages that were previously sent to the endpoint are not resent.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let replayIn = new SvixApi.ReplayIn(); // ReplayIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.replayMissingWebhooksApiV1AppAppIdEndpointEndpointIdReplayMissingPost(appId, endpointId, replayIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **replayIn** | [**ReplayIn**](ReplayIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ReplayOut**](ReplayOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rotateEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretRotatePost

> rotateEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretRotatePost(endpointId, appId, endpointSecretRotateIn, opts)

Rotate Endpoint Secret

Rotates the endpoint&#39;s signing secret.  The previous secret will be valid for the next 24 hours.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointSecretRotateIn = new SvixApi.EndpointSecretRotateIn(); // EndpointSecretRotateIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.rotateEndpointSecretApiV1AppAppIdEndpointEndpointIdSecretRotatePost(endpointId, appId, endpointSecretRotateIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **endpointSecretRotateIn** | [**EndpointSecretRotateIn**](EndpointSecretRotateIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEventTypeExampleMessageApiV1AppAppIdEndpointEndpointIdSendExamplePost

> MessageOut sendEventTypeExampleMessageApiV1AppAppIdEndpointEndpointIdSendExamplePost(appId, endpointId, eventExampleIn, opts)

Send Event Type Example Message

Send an example message for event

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let eventExampleIn = new SvixApi.EventExampleIn(); // EventExampleIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.sendEventTypeExampleMessageApiV1AppAppIdEndpointEndpointIdSendExamplePost(appId, endpointId, eventExampleIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **eventExampleIn** | [**EventExampleIn**](EventExampleIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationPatch

> setEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationPatch(appId, endpointId, endpointTransformationIn, opts)

Set Endpoint Transformation

Set or unset the transformation code associated with this endpoint

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointTransformationIn = new SvixApi.EndpointTransformationIn(); // EndpointTransformationIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.setEndpointTransformationApiV1AppAppIdEndpointEndpointIdTransformationPatch(appId, endpointId, endpointTransformationIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **endpointTransformationIn** | [**EndpointTransformationIn**](EndpointTransformationIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEndpointApiV1AppAppIdEndpointEndpointIdPut

> EndpointOut updateEndpointApiV1AppAppIdEndpointEndpointIdPut(endpointId, appId, endpointUpdate, opts)

Update Endpoint

Update an endpoint.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointUpdate = new SvixApi.EndpointUpdate(); // EndpointUpdate | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.updateEndpointApiV1AppAppIdEndpointEndpointIdPut(endpointId, appId, endpointUpdate, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **endpointUpdate** | [**EndpointUpdate**](EndpointUpdate.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**EndpointOut**](EndpointOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPut

> updateEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPut(appId, endpointId, endpointHeadersIn, opts)

Update Endpoint Headers

Set the additional headers to be sent with the webhook

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.EndpointApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointHeadersIn = new SvixApi.EndpointHeadersIn(); // EndpointHeadersIn | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.updateEndpointHeadersApiV1AppAppIdEndpointEndpointIdHeadersPut(appId, endpointId, endpointHeadersIn, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **endpointHeadersIn** | [**EndpointHeadersIn**](EndpointHeadersIn.md)|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

