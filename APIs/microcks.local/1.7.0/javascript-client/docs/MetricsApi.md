# MicrocksApiV17.MetricsApi

All URIs are relative to *http://microcks.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAggregatedInvocationsStats**](MetricsApi.md#getAggregatedInvocationsStats) | **GET** /metrics/invocations/global | Get aggregated invocation statistics for a day
[**getConformanceMetricsAggregation**](MetricsApi.md#getConformanceMetricsAggregation) | **GET** /metrics/conformance/aggregate | Get aggregation of conformance metrics
[**getInvocationStatsByService**](MetricsApi.md#getInvocationStatsByService) | **GET** /metrics/invocations/{serviceName}/{serviceVersion} | Get invocation statistics for Service
[**getLatestAggregatedInvocationsStats**](MetricsApi.md#getLatestAggregatedInvocationsStats) | **GET** /metrics/invocations/global/latest | Get aggregated invocations statistics for latest days
[**getLatestTestResults**](MetricsApi.md#getLatestTestResults) | **GET** /metrics/tests/latest | Get latest tests results
[**getServiceTestConformanceMetric**](MetricsApi.md#getServiceTestConformanceMetric) | **GET** /metrics/conformance/service/{serviceId} | Get conformance metrics for a Service
[**getTopIvnocationsStatsByDay**](MetricsApi.md#getTopIvnocationsStatsByDay) | **GET** /metrics/invocations/top | Get top invocation statistics for a day



## getAggregatedInvocationsStats

> DailyInvocationStatistic getAggregatedInvocationsStats(opts)

Get aggregated invocation statistics for a day

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
let opts = {
  'day': "day_example" // String | The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
};
apiInstance.getAggregatedInvocationsStats(opts, (error, data, response) => {
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
 **day** | **String**| The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided. | [optional] 

### Return type

[**DailyInvocationStatistic**](DailyInvocationStatistic.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConformanceMetricsAggregation

> [WeightedMetricValue] getConformanceMetricsAggregation()

Get aggregation of conformance metrics

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
apiInstance.getConformanceMetricsAggregation((error, data, response) => {
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

[**[WeightedMetricValue]**](WeightedMetricValue.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvocationStatsByService

> DailyInvocationStatistic getInvocationStatsByService(serviceName, serviceVersion, opts)

Get invocation statistics for Service

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
let serviceName = "serviceName_example"; // String | Name of service to get statistics for
let serviceVersion = "serviceVersion_example"; // String | Version of service to get statistics for
let opts = {
  'day': "day_example" // String | The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
};
apiInstance.getInvocationStatsByService(serviceName, serviceVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| Name of service to get statistics for | 
 **serviceVersion** | **String**| Version of service to get statistics for | 
 **day** | **String**| The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided. | [optional] 

### Return type

[**DailyInvocationStatistic**](DailyInvocationStatistic.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLatestAggregatedInvocationsStats

> {String: Number} getLatestAggregatedInvocationsStats(opts)

Get aggregated invocations statistics for latest days

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
let opts = {
  'limit': 56 // Number | Number of days to get back in time. Default is 20.
};
apiInstance.getLatestAggregatedInvocationsStats(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of days to get back in time. Default is 20. | [optional] 

### Return type

**{String: Number}**

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLatestTestResults

> [TestResultSummary] getLatestTestResults(opts)

Get latest tests results

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
let opts = {
  'limit': 56 // Number | Number of days to consider for test results to return. Default is 7 (one week)
};
apiInstance.getLatestTestResults(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of days to consider for test results to return. Default is 7 (one week) | [optional] 

### Return type

[**[TestResultSummary]**](TestResultSummary.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceTestConformanceMetric

> TestConformanceMetric getServiceTestConformanceMetric(serviceId)

Get conformance metrics for a Service

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
let serviceId = "serviceId_example"; // String | Unique Services identifier this metrics are related to
apiInstance.getServiceTestConformanceMetric(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Unique Services identifier this metrics are related to | 

### Return type

[**TestConformanceMetric**](TestConformanceMetric.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTopIvnocationsStatsByDay

> [DailyInvocationStatistic] getTopIvnocationsStatsByDay(opts)

Get top invocation statistics for a day

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.MetricsApi();
let opts = {
  'day': "day_example", // String | The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided.
  'limit': 56 // Number | The number of top invoked mocks to return
};
apiInstance.getTopIvnocationsStatsByDay(opts, (error, data, response) => {
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
 **day** | **String**| The day to get statistics for (formatted with yyyyMMdd pattern). Default to today if not provided. | [optional] 
 **limit** | **Number**| The number of top invoked mocks to return | [optional] 

### Return type

[**[DailyInvocationStatistic]**](DailyInvocationStatistic.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

