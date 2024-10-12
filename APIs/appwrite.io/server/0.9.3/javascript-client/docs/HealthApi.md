# Appwrite.HealthApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthGet**](HealthApi.md#healthGet) | **GET** /health | Get HTTP
[**healthGetAntiVirus**](HealthApi.md#healthGetAntiVirus) | **GET** /health/anti-virus | Get Anti virus
[**healthGetCache**](HealthApi.md#healthGetCache) | **GET** /health/cache | Get Cache
[**healthGetDB**](HealthApi.md#healthGetDB) | **GET** /health/db | Get DB
[**healthGetQueueCertificates**](HealthApi.md#healthGetQueueCertificates) | **GET** /health/queue/certificates | Get Certificate Queue
[**healthGetQueueFunctions**](HealthApi.md#healthGetQueueFunctions) | **GET** /health/queue/functions | Get Functions Queue
[**healthGetQueueLogs**](HealthApi.md#healthGetQueueLogs) | **GET** /health/queue/logs | Get Logs Queue
[**healthGetQueueTasks**](HealthApi.md#healthGetQueueTasks) | **GET** /health/queue/tasks | Get Tasks Queue
[**healthGetQueueUsage**](HealthApi.md#healthGetQueueUsage) | **GET** /health/queue/usage | Get Usage Queue
[**healthGetQueueWebhooks**](HealthApi.md#healthGetQueueWebhooks) | **GET** /health/queue/webhooks | Get Webhooks Queue
[**healthGetStorageLocal**](HealthApi.md#healthGetStorageLocal) | **GET** /health/storage/local | Get Local Storage
[**healthGetTime**](HealthApi.md#healthGetTime) | **GET** /health/time | Get Time



## healthGet

> healthGet()

Get HTTP

Check the Appwrite HTTP server is up and responsive.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGet((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetAntiVirus

> healthGetAntiVirus()

Get Anti virus

Check the Appwrite Anti Virus server is up and connection is successful.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetAntiVirus((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetCache

> healthGetCache()

Get Cache

Check the Appwrite in-memory cache server is up and connection is successful.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetCache((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetDB

> healthGetDB()

Get DB

Check the Appwrite database server is up and connection is successful.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetDB((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetQueueCertificates

> healthGetQueueCertificates()

Get Certificate Queue

Get the number of certificates that are waiting to be issued against [Letsencrypt](https://letsencrypt.org/) in the Appwrite internal queue server.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetQueueCertificates((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetQueueFunctions

> healthGetQueueFunctions()

Get Functions Queue



### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetQueueFunctions((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetQueueLogs

> healthGetQueueLogs()

Get Logs Queue

Get the number of logs that are waiting to be processed in the Appwrite internal queue server.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetQueueLogs((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetQueueTasks

> healthGetQueueTasks()

Get Tasks Queue

Get the number of tasks that are waiting to be processed in the Appwrite internal queue server.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetQueueTasks((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetQueueUsage

> healthGetQueueUsage()

Get Usage Queue

Get the number of usage stats that are waiting to be processed in the Appwrite internal queue server.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetQueueUsage((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetQueueWebhooks

> healthGetQueueWebhooks()

Get Webhooks Queue

Get the number of webhooks that are waiting to be processed in the Appwrite internal queue server.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetQueueWebhooks((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetStorageLocal

> healthGetStorageLocal()

Get Local Storage

Check the Appwrite local storage device is up and connection is successful.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetStorageLocal((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## healthGetTime

> healthGetTime()

Get Time

Check the Appwrite server time is synced with Google remote NTP server. We use this technology to smoothly handle leap seconds with no disruptive events. The [Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol) (NTP) is used by hundreds of millions of computers and devices to synchronize their clocks over the Internet. If your computer sets its own clock, it likely uses NTP.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.HealthApi();
apiInstance.healthGetTime((error, data, response) => {
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

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

