# MuxApi.MonitoringApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMonitoringBreakdown**](MonitoringApi.md#getMonitoringBreakdown) | **GET** /data/v1/monitoring/metrics/{MONITORING_METRIC_ID}/breakdown | Get Monitoring Breakdown
[**getMonitoringBreakdownTimeseries**](MonitoringApi.md#getMonitoringBreakdownTimeseries) | **GET** /data/v1/monitoring/metrics/{MONITORING_METRIC_ID}/breakdown-timeseries | Get Monitoring Breakdown Timeseries
[**getMonitoringHistogramTimeseries**](MonitoringApi.md#getMonitoringHistogramTimeseries) | **GET** /data/v1/monitoring/metrics/{MONITORING_HISTOGRAM_METRIC_ID}/histogram-timeseries | Get Monitoring Histogram Timeseries
[**getMonitoringTimeseries**](MonitoringApi.md#getMonitoringTimeseries) | **GET** /data/v1/monitoring/metrics/{MONITORING_METRIC_ID}/timeseries | Get Monitoring Timeseries
[**listMonitoringDimensions**](MonitoringApi.md#listMonitoringDimensions) | **GET** /data/v1/monitoring/dimensions | List Monitoring Dimensions
[**listMonitoringMetrics**](MonitoringApi.md#listMonitoringMetrics) | **GET** /data/v1/monitoring/metrics | List Monitoring Metrics



## getMonitoringBreakdown

> GetMonitoringBreakdownResponse getMonitoringBreakdown(MONITORING_METRIC_ID, opts)

Get Monitoring Breakdown

Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.MonitoringApi();
let MONITORING_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Monitoring Metric
let opts = {
  'dimension': "dimension_example", // String | Dimension the specified value belongs to
  'timestamp': 56, // Number | Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'orderBy': "orderBy_example", // String | Value to order the results by
  'orderDirection': "orderDirection_example" // String | Sort order.
};
apiInstance.getMonitoringBreakdown(MONITORING_METRIC_ID, opts, (error, data, response) => {
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
 **MONITORING_METRIC_ID** | **String**| ID of the Monitoring Metric | 
 **dimension** | **String**| Dimension the specified value belongs to | [optional] 
 **timestamp** | **Number**| Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. | [optional] 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **orderBy** | **String**| Value to order the results by | [optional] 
 **orderDirection** | **String**| Sort order. | [optional] 

### Return type

[**GetMonitoringBreakdownResponse**](GetMonitoringBreakdownResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringBreakdownTimeseries

> GetMonitoringBreakdownTimeseriesResponse getMonitoringBreakdownTimeseries(MONITORING_METRIC_ID, opts)

Get Monitoring Breakdown Timeseries

Gets timeseries of breakdown information for a specific dimension and metric. Each datapoint in the response represents 5 seconds worth of data.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.MonitoringApi();
let MONITORING_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Monitoring Metric
let opts = {
  'dimension': "dimension_example", // String | Dimension the specified value belongs to
  'timeframe': ["null"], // [String] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  The default for this is the last 60 seconds of available data. Timeframes larger than 10 minutes are not allowed, and must be within the last 24 hours. 
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'limit': 10, // Number | Number of items to include in each timestamp's `value` list.  The default is 10, and the maximum is 100. 
  'orderBy': "orderBy_example", // String | Value to order the results by
  'orderDirection': "orderDirection_example" // String | Sort order.
};
apiInstance.getMonitoringBreakdownTimeseries(MONITORING_METRIC_ID, opts, (error, data, response) => {
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
 **MONITORING_METRIC_ID** | **String**| ID of the Monitoring Metric | 
 **dimension** | **String**| Dimension the specified value belongs to | [optional] 
 **timeframe** | [**[String]**](String.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  The default for this is the last 60 seconds of available data. Timeframes larger than 10 minutes are not allowed, and must be within the last 24 hours.  | [optional] 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **limit** | **Number**| Number of items to include in each timestamp&#39;s &#x60;value&#x60; list.  The default is 10, and the maximum is 100.  | [optional] [default to 10]
 **orderBy** | **String**| Value to order the results by | [optional] 
 **orderDirection** | **String**| Sort order. | [optional] 

### Return type

[**GetMonitoringBreakdownTimeseriesResponse**](GetMonitoringBreakdownTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringHistogramTimeseries

> GetMonitoringHistogramTimeseriesResponse getMonitoringHistogramTimeseries(MONITORING_HISTOGRAM_METRIC_ID, opts)

Get Monitoring Histogram Timeseries

Gets histogram timeseries information for a specific metric.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.MonitoringApi();
let MONITORING_HISTOGRAM_METRIC_ID = "video-startup-time"; // String | ID of the Monitoring Histogram Metric
let opts = {
  'filters': ["null"] // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
};
apiInstance.getMonitoringHistogramTimeseries(MONITORING_HISTOGRAM_METRIC_ID, opts, (error, data, response) => {
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
 **MONITORING_HISTOGRAM_METRIC_ID** | **String**| ID of the Monitoring Histogram Metric | 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 

### Return type

[**GetMonitoringHistogramTimeseriesResponse**](GetMonitoringHistogramTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMonitoringTimeseries

> GetMonitoringTimeseriesResponse getMonitoringTimeseries(MONITORING_METRIC_ID, opts)

Get Monitoring Timeseries

Gets Time series information for a specific metric along with the number of concurrent viewers.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.MonitoringApi();
let MONITORING_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Monitoring Metric
let opts = {
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'timestamp': 56 // Number | Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago.
};
apiInstance.getMonitoringTimeseries(MONITORING_METRIC_ID, opts, (error, data, response) => {
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
 **MONITORING_METRIC_ID** | **String**| ID of the Monitoring Metric | 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timestamp** | **Number**| Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. | [optional] 

### Return type

[**GetMonitoringTimeseriesResponse**](GetMonitoringTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMonitoringDimensions

> ListMonitoringDimensionsResponse listMonitoringDimensions()

List Monitoring Dimensions

Lists available monitoring dimensions.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.MonitoringApi();
apiInstance.listMonitoringDimensions((error, data, response) => {
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

[**ListMonitoringDimensionsResponse**](ListMonitoringDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMonitoringMetrics

> ListMonitoringMetricsResponse listMonitoringMetrics()

List Monitoring Metrics

Lists available monitoring metrics.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.MonitoringApi();
apiInstance.listMonitoringMetrics((error, data, response) => {
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

[**ListMonitoringMetricsResponse**](ListMonitoringMetricsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

