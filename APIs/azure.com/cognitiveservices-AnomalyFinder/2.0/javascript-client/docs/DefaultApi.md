# AnomalyFinderClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entireDetect**](DefaultApi.md#entireDetect) | **POST** /timeseries/entire/detect | Find anomalies for the entire series in batch.
[**lastDetect**](DefaultApi.md#lastDetect) | **POST** /timeseries/last/detect | Detect anomaly status of the latest point in time series.



## entireDetect

> EntireDetectResponse entireDetect(body)

Find anomalies for the entire series in batch.

The operation will generate a model using the entire series, each point will be detected with the same model. In this method, points before and after a certain point will be used to determine whether it&#39;s an anomaly. The entire detection can give user an overall status of the time series.

### Example

```javascript
import AnomalyFinderClient from 'anomaly_finder_client';
let defaultClient = AnomalyFinderClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AnomalyFinderClient.DefaultApi();
let body = new AnomalyFinderClient.Request(); // Request | Time series points and period if needed. Advanced model parameters can also be set in the request.
apiInstance.entireDetect(body, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| Time series points and period if needed. Advanced model parameters can also be set in the request. | 

### Return type

[**EntireDetectResponse**](EntireDetectResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## lastDetect

> LastDetectResponse lastDetect(body)

Detect anomaly status of the latest point in time series.

The operation will generate a model using points before the latest one, In this method, only history points are used for determine whether the target point is an anomaly. Latest point detecting matches the scenario of real-time monitoring of business metrics.

### Example

```javascript
import AnomalyFinderClient from 'anomaly_finder_client';
let defaultClient = AnomalyFinderClient.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AnomalyFinderClient.DefaultApi();
let body = new AnomalyFinderClient.Request(); // Request | Time series points and period if needed. Advanced model parameters can also be set in the request.
apiInstance.lastDetect(body, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| Time series points and period if needed. Advanced model parameters can also be set in the request. | 

### Return type

[**LastDetectResponse**](LastDetectResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

