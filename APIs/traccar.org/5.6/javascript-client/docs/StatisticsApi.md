# Traccar.StatisticsApi

All URIs are relative to *https://demo.traccar.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statisticsGet**](StatisticsApi.md#statisticsGet) | **GET** /statistics | Fetch server Statistics



## statisticsGet

> [Statistics] statisticsGet(from, to)

Fetch server Statistics

### Example

```javascript
import Traccar from 'traccar';
let defaultClient = Traccar.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Traccar.StatisticsApi();
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
apiInstance.statisticsGet(from, to, (error, data, response) => {
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
 **from** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 
 **to** | **Date**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | 

### Return type

[**[Statistics]**](Statistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

