# TimeSeriesInsightsClient.TimeSeriesTypesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeSeriesTypesExecuteBatch**](TimeSeriesTypesApi.md#timeSeriesTypesExecuteBatch) | **POST** /timeseries/types/$batch | 
[**timeSeriesTypesGet**](TimeSeriesTypesApi.md#timeSeriesTypesGet) | **GET** /timeseries/types | 



## timeSeriesTypesExecuteBatch

> TypesBatchResponse timeSeriesTypesExecuteBatch(apiVersion, parameters, opts)



Executes a batch get, create, update, delete operation on multiple time series types.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.TimeSeriesTypesApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.TypesBatchRequest(); // TypesBatchRequest | Time series types batch request body.
let opts = {
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.timeSeriesTypesExecuteBatch(apiVersion, parameters, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;. | [default to &#39;2018-11-01-preview&#39;]
 **parameters** | [**TypesBatchRequest**](TypesBatchRequest.md)| Time series types batch request body. | 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**TypesBatchResponse**](TypesBatchResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeSeriesTypesGet

> GetTypesPage timeSeriesTypesGet(apiVersion, opts)



Gets time series types in pages.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.TimeSeriesTypesApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let opts = {
  'xMsContinuation': "xMsContinuation_example", // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.timeSeriesTypesGet(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;. | [default to &#39;2018-11-01-preview&#39;]
 **xMsContinuation** | **String**| Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results. | [optional] 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**GetTypesPage**](GetTypesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

