# TimeSeriesInsightsClient.TimeSeriesInstancesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeSeriesInstancesExecuteBatch**](TimeSeriesInstancesApi.md#timeSeriesInstancesExecuteBatch) | **POST** /timeseries/instances/$batch | 
[**timeSeriesInstancesGet**](TimeSeriesInstancesApi.md#timeSeriesInstancesGet) | **GET** /timeseries/instances | 
[**timeSeriesInstancesSearch**](TimeSeriesInstancesApi.md#timeSeriesInstancesSearch) | **POST** /timeseries/instances/search | 
[**timeSeriesInstancesSuggest**](TimeSeriesInstancesApi.md#timeSeriesInstancesSuggest) | **POST** /timeseries/instances/suggest | 



## timeSeriesInstancesExecuteBatch

> InstancesBatchResponse timeSeriesInstancesExecuteBatch(apiVersion, parameters, opts)



Executes a batch get, create, update, delete operation on multiple time series instances.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.TimeSeriesInstancesApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.InstancesBatchRequest(); // InstancesBatchRequest | Time series instances suggest request body.
let opts = {
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.timeSeriesInstancesExecuteBatch(apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**InstancesBatchRequest**](InstancesBatchRequest.md)| Time series instances suggest request body. | 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**InstancesBatchResponse**](InstancesBatchResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeSeriesInstancesGet

> GetInstancesPage timeSeriesInstancesGet(apiVersion, opts)



Gets time series instances in pages.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.TimeSeriesInstancesApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let opts = {
  'xMsContinuation': "xMsContinuation_example", // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.timeSeriesInstancesGet(apiVersion, opts, (error, data, response) => {
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

[**GetInstancesPage**](GetInstancesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeSeriesInstancesSearch

> SearchInstancesResponsePage timeSeriesInstancesSearch(apiVersion, parameters, opts)



Partial list of hits on search for time series instances based on instance attributes.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.TimeSeriesInstancesApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.SearchInstancesRequest(); // SearchInstancesRequest | Time series instances search request body.
let opts = {
  'xMsContinuation': "xMsContinuation_example", // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.timeSeriesInstancesSearch(apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**SearchInstancesRequest**](SearchInstancesRequest.md)| Time series instances search request body. | 
 **xMsContinuation** | **String**| Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results. | [optional] 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**SearchInstancesResponsePage**](SearchInstancesResponsePage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeSeriesInstancesSuggest

> InstancesSuggestResponse timeSeriesInstancesSuggest(apiVersion, parameters, opts)



Suggests keywords based on time series instance attributes to be later used in Search Instances.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.TimeSeriesInstancesApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.InstancesSuggestRequest(); // InstancesSuggestRequest | Time series instances suggest request body.
let opts = {
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.timeSeriesInstancesSuggest(apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**InstancesSuggestRequest**](InstancesSuggestRequest.md)| Time series instances suggest request body. | 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**InstancesSuggestResponse**](InstancesSuggestResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

