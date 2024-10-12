# OpenTargetsPlatformRestApi.UtilsApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDataMetrics_0**](UtilsApi.md#getDataMetrics_0) | **GET** /platform/public/utils/metrics | Get metrics about the current data release
[**getDataStats_0**](UtilsApi.md#getDataStats_0) | **GET** /platform/public/utils/stats | Get statistics about the current data release
[**getPing_0**](UtilsApi.md#getPing_0) | **GET** /platform/public/utils/ping | Ping service
[**getTherapeuticAreas_0**](UtilsApi.md#getTherapeuticAreas_0) | **GET** /platform/public/utils/therapeuticareas | Get the list of therapeutic areas about the current data release
[**getVersion_0**](UtilsApi.md#getVersion_0) | **GET** /platform/public/utils/version | Get API version



## getDataMetrics_0

> getDataMetrics_0()

Get metrics about the current data release

Returns the metrics about associations and evidences, divided by datasource, genes and so on. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.UtilsApi();
apiInstance.getDataMetrics_0((error, data, response) => {
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


## getDataStats_0

> getDataStats_0()

Get statistics about the current data release

Returns the number of associations and evidences, divided by datasource. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.UtilsApi();
apiInstance.getDataStats_0((error, data, response) => {
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


## getPing_0

> getPing_0()

Ping service

Check if the API is up 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.UtilsApi();
apiInstance.getPing_0((error, data, response) => {
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


## getTherapeuticAreas_0

> getTherapeuticAreas_0()

Get the list of therapeutic areas about the current data release

Returns the list of therapeutic areas for the current data release 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.UtilsApi();
apiInstance.getTherapeuticAreas_0((error, data, response) => {
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


## getVersion_0

> getVersion_0()

Get API version

Returns current API version. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.UtilsApi();
apiInstance.getVersion_0((error, data, response) => {
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

