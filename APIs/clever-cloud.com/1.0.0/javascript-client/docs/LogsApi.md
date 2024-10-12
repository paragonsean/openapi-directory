# CleverCloudApi.LogsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logsAppIdDrainsGet_0**](LogsApi.md#logsAppIdDrainsGet_0) | **GET** /logs/{appId}/drains | 
[**logsAppIdDrainsIdOrUrlDelete_0**](LogsApi.md#logsAppIdDrainsIdOrUrlDelete_0) | **DELETE** /logs/{appId}/drains/:idOrUrl | 
[**logsAppIdDrainsIdOrUrlGet_0**](LogsApi.md#logsAppIdDrainsIdOrUrlGet_0) | **GET** /logs/{appId}/drains/:idOrUrl | 
[**logsAppIdDrainsPost_0**](LogsApi.md#logsAppIdDrainsPost_0) | **POST** /logs/{appId}/drains | 
[**logsAppIdGet_0**](LogsApi.md#logsAppIdGet_0) | **GET** /logs/{appId} | 
[**logsAppIdSseGet_0**](LogsApi.md#logsAppIdSseGet_0) | **GET** /logs/{appId}/sse | 
[**logsDrainsDrainIdPut_0**](LogsApi.md#logsDrainsDrainIdPut_0) | **PUT** /logs/drains/{drainId} | 
[**logsDrainsGet_0**](LogsApi.md#logsDrainsGet_0) | **GET** /logs/drains | 
[**logsLogsChunkedAppIdGet_0**](LogsApi.md#logsLogsChunkedAppIdGet_0) | **GET** /logs/logs-chunked/{appId} | 
[**logsLogsSocketAppIdGet_0**](LogsApi.md#logsLogsSocketAppIdGet_0) | **GET** /logs/logs-socket/{appId} | 
[**v3LogsAppIdDrainsGet_0**](LogsApi.md#v3LogsAppIdDrainsGet_0) | **GET** /v3/logs/{appId}/drains | 
[**v3LogsAppIdDrainsIdOrUrlDelete_0**](LogsApi.md#v3LogsAppIdDrainsIdOrUrlDelete_0) | **DELETE** /v3/logs/{appId}/drains/:idOrUrl | 
[**v3LogsAppIdDrainsIdOrUrlGet_0**](LogsApi.md#v3LogsAppIdDrainsIdOrUrlGet_0) | **GET** /v3/logs/{appId}/drains/:idOrUrl | 
[**v3LogsAppIdDrainsPost_0**](LogsApi.md#v3LogsAppIdDrainsPost_0) | **POST** /v3/logs/{appId}/drains | 
[**v3LogsAppIdGet_0**](LogsApi.md#v3LogsAppIdGet_0) | **GET** /v3/logs/{appId} | 
[**v3LogsAppIdLogsChunkedGet_0**](LogsApi.md#v3LogsAppIdLogsChunkedGet_0) | **GET** /v3/logs/{appId}/logs-chunked | 
[**v3LogsAppIdLogsSocketGet_0**](LogsApi.md#v3LogsAppIdLogsSocketGet_0) | **GET** /v3/logs/{appId}/logs-socket | 



## logsAppIdDrainsGet_0

> logsAppIdDrainsGet_0(appId)



Fetch the logs drains for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdDrainsIdOrUrlDelete_0

> logsAppIdDrainsIdOrUrlDelete_0(appId)



Delete the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsIdOrUrlDelete_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdDrainsIdOrUrlGet_0

> logsAppIdDrainsIdOrUrlGet_0(appId)



Fetch the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsIdOrUrlGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdDrainsPost_0

> logsAppIdDrainsPost_0(appId)



Add a log drain for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdDrainsPost_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdGet_0

> logsAppIdGet_0(appId, opts)



Fetch the logs for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Application Id
let opts = {
  'limit': 56, // Number | Number of lines to return
  'order': "'desc'", // String | Logs order
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | Lowest bound for logs date, ISO 8601
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | Highest bounds for logs date, ISO 8601
  'filter': "filter_example", // String | A pattern to filter with
  'deploymentId': "deploymentId_example" // String | Only fetch logs emitted by this deployment
};
apiInstance.logsAppIdGet_0(appId, opts, (error, data, response) => {
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
 **appId** | **String**| Application Id | 
 **limit** | **Number**| Number of lines to return | [optional] 
 **order** | **String**| Logs order | [optional] [default to &#39;desc&#39;]
 **after** | **Date**| Lowest bound for logs date, ISO 8601 | [optional] 
 **before** | **Date**| Highest bounds for logs date, ISO 8601 | [optional] 
 **filter** | **String**| A pattern to filter with | [optional] 
 **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsAppIdSseGet_0

> logsAppIdSseGet_0(appId)



Retrieve logs as they come through a sse connection. To have authorization, you have to add &#x60;authorization&#x3D;oAuthAuthorizationString&#x60; as query param.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.logsAppIdSseGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsDrainsDrainIdPut_0

> logsDrainsDrainIdPut_0(drainId)



Fetch all the logs drains (ccadmin dedicated route)

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let drainId = "drainId_example"; // String | Automatically added
apiInstance.logsDrainsDrainIdPut_0(drainId, (error, data, response) => {
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
 **drainId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsDrainsGet_0

> logsDrainsGet_0()



Fetch all the logs drains (ccadmin dedicated route)

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
apiInstance.logsDrainsGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsLogsChunkedAppIdGet_0

> logsLogsChunkedAppIdGet_0(appId, opts)



Retrieve logs as they come through a chunked, never-ending response

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Application Id
let opts = {
  'download': true // Boolean | Tell the user-agent to download the body as a file
};
apiInstance.logsLogsChunkedAppIdGet_0(appId, opts, (error, data, response) => {
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
 **appId** | **String**| Application Id | 
 **download** | **Boolean**| Tell the user-agent to download the body as a file | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsLogsSocketAppIdGet_0

> logsLogsSocketAppIdGet_0(appId, opts)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Application Id
let opts = {
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only fetch logs newer than this (ISO-8601 formatted) date
  'filter': "filter_example", // String | A pattern to filter with
  'deploymentId': "deploymentId_example" // String | Only fetch logs emitted by this deployment
};
apiInstance.logsLogsSocketAppIdGet_0(appId, opts, (error, data, response) => {
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
 **appId** | **String**| Application Id | 
 **since** | **Date**| Only fetch logs newer than this (ISO-8601 formatted) date | [optional] 
 **filter** | **String**| A pattern to filter with | [optional] 
 **deploymentId** | **String**| Only fetch logs emitted by this deployment | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsGet_0

> v3LogsAppIdDrainsGet_0(appId)



Fetch the logs drains for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsIdOrUrlDelete_0

> v3LogsAppIdDrainsIdOrUrlDelete_0(appId)



Delete the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsIdOrUrlDelete_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsIdOrUrlGet_0

> v3LogsAppIdDrainsIdOrUrlGet_0(appId)



Fetch the logs drain by id or url for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsIdOrUrlGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdDrainsPost_0

> v3LogsAppIdDrainsPost_0(appId)



Add a log drain for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdDrainsPost_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdGet_0

> v3LogsAppIdGet_0(appId)



Fetch the logs for a given application

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdLogsChunkedGet_0

> v3LogsAppIdLogsChunkedGet_0(appId)



Retrieve logs as they come through a chunked, never-ending response

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdLogsChunkedGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v3LogsAppIdLogsSocketGet_0

> v3LogsAppIdLogsSocketGet_0(appId)



Retrieve logs as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.LogsApi();
let appId = "appId_example"; // String | Automatically added
apiInstance.v3LogsAppIdLogsSocketGet_0(appId, (error, data, response) => {
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
 **appId** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

