# SwaggerApiRestForPatrowlEngines.PatrowlEngineApi

All URIs are relative to *http://patrowl.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cleanScanPage**](PatrowlEngineApi.md#cleanScanPage) | **GET** /clean/{scanId} | Clean scan
[**cleanScansPage**](PatrowlEngineApi.md#cleanScansPage) | **GET** /clean | Clean all scans
[**getDefaultPage**](PatrowlEngineApi.md#getDefaultPage) | **GET** / | Index page
[**getFindingPage**](PatrowlEngineApi.md#getFindingPage) | **GET** /getfindings/{scanId} | Get findings on finished scans
[**getInfoPage**](PatrowlEngineApi.md#getInfoPage) | **GET** /info | Engine info page
[**getLivenessPage**](PatrowlEngineApi.md#getLivenessPage) | **GET** /liveness | Liveness page
[**getReadinessPage**](PatrowlEngineApi.md#getReadinessPage) | **GET** /readiness | Readiness page
[**getTestPage**](PatrowlEngineApi.md#getTestPage) | **GET** /test | Test page
[**reloadConfigurationPage**](PatrowlEngineApi.md#reloadConfigurationPage) | **GET** /reloadconfig | Configuration reloading page
[**startScanPage**](PatrowlEngineApi.md#startScanPage) | **POST** /startscan | Start a new scan
[**statusScanPage**](PatrowlEngineApi.md#statusScanPage) | **GET** /status/{scanId} | Status of a scan
[**statusScansPage**](PatrowlEngineApi.md#statusScansPage) | **GET** /status | Status on all scans
[**stopScanPage**](PatrowlEngineApi.md#stopScanPage) | **GET** /stop/{scanId} | Stop a scan
[**stopScansPage**](PatrowlEngineApi.md#stopScansPage) | **GET** /stopscans | Stop all scans



## cleanScanPage

> ApiResponse cleanScanPage(scanId)

Clean scan

Clean scan identified by id.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
let scanId = 56; // Number | Numeric ID of the scan to clean
apiInstance.cleanScanPage(scanId, (error, data, response) => {
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
 **scanId** | **Number**| Numeric ID of the scan to clean | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cleanScansPage

> ApiResponse cleanScansPage()

Clean all scans

Clean all current scans.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.cleanScansPage((error, data, response) => {
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

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDefaultPage

> ApiResponse getDefaultPage()

Index page

Return index page

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.getDefaultPage((error, data, response) => {
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

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFindingPage

> [FindingsInner] getFindingPage(scanId)

Get findings on finished scans

Get findings on finished scans.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
let scanId = 56; // Number | Numeric ID of the scan to get findings
apiInstance.getFindingPage(scanId, (error, data, response) => {
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
 **scanId** | **Number**| Numeric ID of the scan to get findings | 

### Return type

[**[FindingsInner]**](FindingsInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInfoPage

> ApiResponse getInfoPage()

Engine info page

Return information on engine.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.getInfoPage((error, data, response) => {
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

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLivenessPage

> getLivenessPage()

Liveness page

Return liveness page

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.getLivenessPage((error, data, response) => {
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


## getReadinessPage

> getReadinessPage()

Readiness page

Return liveness page

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.getReadinessPage((error, data, response) => {
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


## getTestPage

> getTestPage()

Test page

Return test page

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.getTestPage((error, data, response) => {
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


## reloadConfigurationPage

> ApiResponse reloadConfigurationPage()

Configuration reloading page

Reload the configuration file.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.reloadConfigurationPage((error, data, response) => {
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

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startScanPage

> ApiResponse startScanPage(scanDefinition)

Start a new scan

Start a new scan.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
let scanDefinition = new SwaggerApiRestForPatrowlEngines.ScanDefinition(); // ScanDefinition | 
apiInstance.startScanPage(scanDefinition, (error, data, response) => {
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
 **scanDefinition** | [**ScanDefinition**](ScanDefinition.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## statusScanPage

> ApiResponse statusScanPage(scanId)

Status of a scan

Status of a scan identified by id.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
let scanId = 56; // Number | Numeric ID of the scan to get status
apiInstance.statusScanPage(scanId, (error, data, response) => {
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
 **scanId** | **Number**| Numeric ID of the scan to get status | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## statusScansPage

> ApiResponse statusScansPage()

Status on all scans

Status all current scans.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.statusScansPage((error, data, response) => {
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

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopScanPage

> ApiResponse stopScanPage(scanId)

Stop a scan

Stop a scan identified by id.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
let scanId = 56; // Number | Numeric ID of the scan to stop
apiInstance.stopScanPage(scanId, (error, data, response) => {
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
 **scanId** | **Number**| Numeric ID of the scan to stop | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopScansPage

> ApiResponse stopScansPage()

Stop all scans

Stop all current scans.

### Example

```javascript
import SwaggerApiRestForPatrowlEngines from 'swagger_api_rest_for_patrowl_engines';

let apiInstance = new SwaggerApiRestForPatrowlEngines.PatrowlEngineApi();
apiInstance.stopScansPage((error, data, response) => {
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

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

