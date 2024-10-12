# LgtmApiSpecification.SystemApi

All URIs are relative to *https://lgtm.com/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHealth**](SystemApi.md#getHealth) | **GET** /system/health | Get a summary of the application&#39;s health
[**getMetric**](SystemApi.md#getMetric) | **GET** /system/metrics/{metric-id} | Get the computed values of the specified metric
[**getMetrics**](SystemApi.md#getMetrics) | **GET** /system/metrics | Get the identifiers and descriptions of the usage metrics



## getHealth

> Health getHealth()

Get a summary of the application&#39;s health

Return an indication of whether the application is working as expected (up) or needs  attention (down).  \\&gt; The &#x60;description&#x60; and &#x60;details&#x60; fields are reported only if the request includes an access token for a user account that has administration rights for this LGTM server. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.SystemApi();
apiInstance.getHealth((error, data, response) => {
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

[**Health**](Health.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetric

> Metric getMetric(metricId)

Get the computed values of the specified metric

LGTM administrators can download usage data using this endpoint. The response includes up to 1000 values for the specified metric and reports the date-time that each value was calculated. There is normally one value per day. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.SystemApi();
let metricId = "metricId_example"; // String | The identifier of the metric.
apiInstance.getMetric(metricId, (error, data, response) => {
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
 **metricId** | **String**| The identifier of the metric. | 

### Return type

[**Metric**](Metric.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMetrics

> MetricsList getMetrics()

Get the identifiers and descriptions of the usage metrics

LGTM administrators can use this endpoint to list the usage metrics that are available to download. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.SystemApi();
apiInstance.getMetrics((error, data, response) => {
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

[**MetricsList**](MetricsList.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

