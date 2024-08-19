# MuxApi.RealTimeApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRealtimeBreakdown**](RealTimeApi.md#getRealtimeBreakdown) | **GET** /data/v1/realtime/metrics/{REALTIME_METRIC_ID}/breakdown | Get Real-Time Breakdown
[**getRealtimeHistogramTimeseries**](RealTimeApi.md#getRealtimeHistogramTimeseries) | **GET** /data/v1/realtime/metrics/{REALTIME_HISTOGRAM_METRIC_ID}/histogram-timeseries | Get Real-Time Histogram Timeseries
[**getRealtimeTimeseries**](RealTimeApi.md#getRealtimeTimeseries) | **GET** /data/v1/realtime/metrics/{REALTIME_METRIC_ID}/timeseries | Get Real-Time Timeseries
[**listRealtimeDimensions**](RealTimeApi.md#listRealtimeDimensions) | **GET** /data/v1/realtime/dimensions | List Real-Time Dimensions
[**listRealtimeMetrics**](RealTimeApi.md#listRealtimeMetrics) | **GET** /data/v1/realtime/metrics | List Real-Time Metrics



## getRealtimeBreakdown

> GetRealTimeBreakdownResponse getRealtimeBreakdown(REALTIME_METRIC_ID, opts)

Get Real-Time Breakdown

Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score. This API is now deprecated, please use the &#x60;Get Monitoring Breakdown&#x60; API.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.RealTimeApi();
let REALTIME_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Realtime Metric
let opts = {
  'dimension': "dimension_example", // String | Dimension the specified value belongs to
  'timestamp': 56, // Number | Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'orderBy': "orderBy_example", // String | Value to order the results by
  'orderDirection': "orderDirection_example" // String | Sort order.
};
apiInstance.getRealtimeBreakdown(REALTIME_METRIC_ID, opts, (error, data, response) => {
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
 **REALTIME_METRIC_ID** | **String**| ID of the Realtime Metric | 
 **dimension** | **String**| Dimension the specified value belongs to | [optional] 
 **timestamp** | **Number**| Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. | [optional] 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **orderBy** | **String**| Value to order the results by | [optional] 
 **orderDirection** | **String**| Sort order. | [optional] 

### Return type

[**GetRealTimeBreakdownResponse**](GetRealTimeBreakdownResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRealtimeHistogramTimeseries

> GetRealTimeHistogramTimeseriesResponse getRealtimeHistogramTimeseries(REALTIME_HISTOGRAM_METRIC_ID, opts)

Get Real-Time Histogram Timeseries

Gets histogram timeseries information for a specific metric. This API is now deprecated, please use the &#x60;Get Monitoring Histogram Timeseries&#x60; API.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.RealTimeApi();
let REALTIME_HISTOGRAM_METRIC_ID = "video-startup-time"; // String | ID of the Realtime Histogram Metric
let opts = {
  'filters': ["null"] // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
};
apiInstance.getRealtimeHistogramTimeseries(REALTIME_HISTOGRAM_METRIC_ID, opts, (error, data, response) => {
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
 **REALTIME_HISTOGRAM_METRIC_ID** | **String**| ID of the Realtime Histogram Metric | 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 

### Return type

[**GetRealTimeHistogramTimeseriesResponse**](GetRealTimeHistogramTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRealtimeTimeseries

> GetRealTimeTimeseriesResponse getRealtimeTimeseries(REALTIME_METRIC_ID, opts)

Get Real-Time Timeseries

Gets Time series information for a specific metric along with the number of concurrent viewers. This API is now deprecated, please use the &#x60;Get Monitoring Timeseries&#x60; API.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.RealTimeApi();
let REALTIME_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Realtime Metric
let opts = {
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'timestamp': 56 // Number | Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago.
};
apiInstance.getRealtimeTimeseries(REALTIME_METRIC_ID, opts, (error, data, response) => {
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
 **REALTIME_METRIC_ID** | **String**| ID of the Realtime Metric | 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timestamp** | **Number**| Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. | [optional] 

### Return type

[**GetRealTimeTimeseriesResponse**](GetRealTimeTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRealtimeDimensions

> ListRealTimeDimensionsResponse listRealtimeDimensions()

List Real-Time Dimensions

Lists available real-time dimensions. This API is now deprecated, please use the &#x60;List Monitoring Dimensions&#x60; API.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.RealTimeApi();
apiInstance.listRealtimeDimensions((error, data, response) => {
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

[**ListRealTimeDimensionsResponse**](ListRealTimeDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRealtimeMetrics

> ListRealTimeMetricsResponse listRealtimeMetrics()

List Real-Time Metrics

Lists available real-time metrics. This API is now deprecated, please use the &#x60;List Monitoring Metrics&#x60; API.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.RealTimeApi();
apiInstance.listRealtimeMetrics((error, data, response) => {
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

[**ListRealTimeMetricsResponse**](ListRealTimeMetricsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

