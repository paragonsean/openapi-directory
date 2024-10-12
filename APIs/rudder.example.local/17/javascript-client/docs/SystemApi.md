# RudderApi.SystemApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createArchive**](SystemApi.md#createArchive) | **POST** /system/archives/{archiveKind} | Create an archive
[**getHealthcheckResult**](SystemApi.md#getHealthcheckResult) | **GET** /system/healthcheck | Get healthcheck
[**getStatus**](SystemApi.md#getStatus) | **GET** /system/status | Get server status
[**getSystemInfo**](SystemApi.md#getSystemInfo) | **GET** /system/info | Get server information
[**getZipArchive**](SystemApi.md#getZipArchive) | **GET** /system/archives/{archiveKind}/zip/{commitId} | Get an archive as a ZIP
[**listArchives**](SystemApi.md#listArchives) | **GET** /system/archives/{archiveKind} | List archives
[**purgeSoftware**](SystemApi.md#purgeSoftware) | **POST** /system/maintenance/purgeSoftware | Trigger batch for cleaning unreferenced software
[**regeneratePolicies**](SystemApi.md#regeneratePolicies) | **POST** /system/regenerate/policies | Trigger a new policy generation
[**reloadAll**](SystemApi.md#reloadAll) | **POST** /system/reload | Reload both techniques and dynamic groups
[**reloadGroups**](SystemApi.md#reloadGroups) | **POST** /system/reload/groups | Reload dynamic groups
[**reloadTechniques**](SystemApi.md#reloadTechniques) | **POST** /system/reload/techniques | Reload techniques
[**restoreArchive**](SystemApi.md#restoreArchive) | **POST** /system/archives/{archiveKind}/restore/{archiveRestoreKind} | Restore an archive
[**updatePolicies**](SystemApi.md#updatePolicies) | **POST** /system/update/policies | Trigger update of policies



## createArchive

> CreateArchive200Response createArchive(archiveKind)

Create an archive

Create new archive of the given kind

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
let archiveKind = "full"; // String | Type of archive to make
apiInstance.createArchive(archiveKind, (error, data, response) => {
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
 **archiveKind** | **String**| Type of archive to make | 

### Return type

[**CreateArchive200Response**](CreateArchive200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHealthcheckResult

> GetHealthcheckResult200Response getHealthcheckResult()

Get healthcheck

Run and get the result of all checks

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.getHealthcheckResult((error, data, response) => {
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

[**GetHealthcheckResult200Response**](GetHealthcheckResult200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatus

> GetStatus200Response getStatus()

Get server status

Get information about current server status

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.getStatus((error, data, response) => {
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

[**GetStatus200Response**](GetStatus200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSystemInfo

> GetSystemInfo200Response getSystemInfo()

Get server information

Get information about the server version

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.getSystemInfo((error, data, response) => {
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

[**GetSystemInfo200Response**](GetSystemInfo200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getZipArchive

> File getZipArchive(archiveKind, commitId)

Get an archive as a ZIP

Get an archive of the given kind as a zip

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
let archiveKind = "full"; // String | Type of archive to make
let commitId = "commitId_example"; // String | commit ID of the archive to get as a ZIP file
apiInstance.getZipArchive(archiveKind, commitId, (error, data, response) => {
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
 **archiveKind** | **String**| Type of archive to make | 
 **commitId** | **String**| commit ID of the archive to get as a ZIP file | 

### Return type

**File**

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## listArchives

> ListArchives200Response listArchives(archiveKind)

List archives

List configuration archives

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
let archiveKind = "full"; // String | Type of archive to make
apiInstance.listArchives(archiveKind, (error, data, response) => {
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
 **archiveKind** | **String**| Type of archive to make | 

### Return type

[**ListArchives200Response**](ListArchives200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purgeSoftware

> PurgeSoftware200Response purgeSoftware()

Trigger batch for cleaning unreferenced software

Start the software cleaning batch asynchronously.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.purgeSoftware((error, data, response) => {
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

[**PurgeSoftware200Response**](PurgeSoftware200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regeneratePolicies

> RegeneratePolicies200Response regeneratePolicies()

Trigger a new policy generation

Trigger a full policy generation

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.regeneratePolicies((error, data, response) => {
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

[**RegeneratePolicies200Response**](RegeneratePolicies200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadAll

> ReloadAll200Response reloadAll()

Reload both techniques and dynamic groups

Reload both techniques and dynamic groups

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.reloadAll((error, data, response) => {
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

[**ReloadAll200Response**](ReloadAll200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadGroups

> ReloadGroups200Response reloadGroups()

Reload dynamic groups

Reload dynamic groups

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.reloadGroups((error, data, response) => {
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

[**ReloadGroups200Response**](ReloadGroups200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reloadTechniques

> ReloadTechniques200Response reloadTechniques()

Reload techniques

Reload techniques from local technique library

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.reloadTechniques((error, data, response) => {
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

[**ReloadTechniques200Response**](ReloadTechniques200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restoreArchive

> RestoreArchive200Response restoreArchive(archiveKind, archiveRestoreKind)

Restore an archive

Restore an archive of the given kind for the given moment

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
let archiveKind = "full"; // String | Type of archive to make
let archiveRestoreKind = "latestCommit"; // String | 
apiInstance.restoreArchive(archiveKind, archiveRestoreKind, (error, data, response) => {
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
 **archiveKind** | **String**| Type of archive to make | 
 **archiveRestoreKind** | **String**|  | 

### Return type

[**RestoreArchive200Response**](RestoreArchive200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePolicies

> UpdatePolicies200Response updatePolicies()

Trigger update of policies

Update configuration policies if needed

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.SystemApi();
apiInstance.updatePolicies((error, data, response) => {
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

[**UpdatePolicies200Response**](UpdatePolicies200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

