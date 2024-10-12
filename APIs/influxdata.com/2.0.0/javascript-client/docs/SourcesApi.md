# InfluxOssApiService.SourcesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSourcesID**](SourcesApi.md#deleteSourcesID) | **DELETE** /sources/{sourceID} | Delete a source
[**getSources**](SourcesApi.md#getSources) | **GET** /sources | List all sources
[**getSourcesID**](SourcesApi.md#getSourcesID) | **GET** /sources/{sourceID} | Retrieve a source
[**getSourcesIDBuckets**](SourcesApi.md#getSourcesIDBuckets) | **GET** /sources/{sourceID}/buckets | Get buckets in a source
[**getSourcesIDHealth**](SourcesApi.md#getSourcesIDHealth) | **GET** /sources/{sourceID}/health | Get the health of a source
[**patchSourcesID**](SourcesApi.md#patchSourcesID) | **PATCH** /sources/{sourceID} | Update a Source
[**postSources**](SourcesApi.md#postSources) | **POST** /sources | Create a source



## deleteSourcesID

> deleteSourcesID(sourceID, opts)

Delete a source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let sourceID = "sourceID_example"; // String | The source ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteSourcesID(sourceID, opts, (error, data, response) => {
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
 **sourceID** | **String**| The source ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSources

> Sources getSources(opts)

List all sources

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'org': "org_example" // String | The name of the organization.
};
apiInstance.getSources(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **org** | **String**| The name of the organization. | [optional] 

### Return type

[**Sources**](Sources.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourcesID

> Source getSourcesID(sourceID, opts)

Retrieve a source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let sourceID = "sourceID_example"; // String | The source ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getSourcesID(sourceID, opts, (error, data, response) => {
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
 **sourceID** | **String**| The source ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourcesIDBuckets

> Buckets getSourcesIDBuckets(sourceID, opts)

Get buckets in a source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let sourceID = "sourceID_example"; // String | The source ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'org': "org_example" // String | The name of the organization.
};
apiInstance.getSourcesIDBuckets(sourceID, opts, (error, data, response) => {
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
 **sourceID** | **String**| The source ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **org** | **String**| The name of the organization. | [optional] 

### Return type

[**Buckets**](Buckets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSourcesIDHealth

> HealthCheck getSourcesIDHealth(sourceID, opts)

Get the health of a source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let sourceID = "sourceID_example"; // String | The source ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getSourcesIDHealth(sourceID, opts, (error, data, response) => {
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
 **sourceID** | **String**| The source ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**HealthCheck**](HealthCheck.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSourcesID

> Source patchSourcesID(sourceID, source, opts)

Update a Source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let sourceID = "sourceID_example"; // String | The source ID.
let source = new InfluxOssApiService.Source(); // Source | Source update
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchSourcesID(sourceID, source, opts, (error, data, response) => {
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
 **sourceID** | **String**| The source ID. | 
 **source** | [**Source**](Source.md)| Source update | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSources

> Source postSources(source, opts)

Create a source

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.SourcesApi();
let source = new InfluxOssApiService.Source(); // Source | Source to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postSources(source, opts, (error, data, response) => {
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
 **source** | [**Source**](Source.md)| Source to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

