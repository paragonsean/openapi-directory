# TimeSeriesInsightsClient.QueryApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryExecute**](QueryApi.md#queryExecute) | **POST** /timeseries/query | 
[**queryGetAvailability**](QueryApi.md#queryGetAvailability) | **GET** /availability | 
[**queryGetEventSchema**](QueryApi.md#queryGetEventSchema) | **POST** /eventSchema | 



## queryExecute

> QueryResultPage queryExecute(apiVersion, parameters, opts)



Executes Time Series Query in pages of results - Get Events, Get Series or Aggregate Series.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.QueryApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.QueryRequest(); // QueryRequest | Time series query request body.
let opts = {
  'storeType': "storeType_example", // String | For the environments with warm store enabled, the query can be executed either on the 'WarmStore' or 'ColdStore'. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
  'xMsContinuation': "xMsContinuation_example", // String | Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.queryExecute(apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**QueryRequest**](QueryRequest.md)| Time series query request body. | 
 **storeType** | **String**| For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store. | [optional] 
 **xMsContinuation** | **String**| Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results. | [optional] 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**QueryResultPage**](QueryResultPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryGetAvailability

> AvailabilityResponse queryGetAvailability(apiVersion, opts)



Returns the time range and distribution of event count over the event timestamp ($ts). This API can be used to provide landing experience of navigating to the environment.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.QueryApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let opts = {
  'storeType': "storeType_example", // String | For the environments with warm store enabled, the query can be executed either on the 'WarmStore' or 'ColdStore'. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.queryGetAvailability(apiVersion, opts, (error, data, response) => {
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
 **storeType** | **String**| For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store. | [optional] 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**AvailabilityResponse**](AvailabilityResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryGetEventSchema

> EventSchema queryGetEventSchema(apiVersion, parameters, opts)



Returns environment event schema for a given search span. Event schema is a set of property definitions. Event schema may not be contain all persisted properties when there are too many properties.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.QueryApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.GetEventSchemaRequest(); // GetEventSchemaRequest | Parameters to get event schema.
let opts = {
  'storeType': "storeType_example", // String | For the environments with warm store enabled, the query can be executed either on the 'WarmStore' or 'ColdStore'. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.queryGetEventSchema(apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**GetEventSchemaRequest**](GetEventSchemaRequest.md)| Parameters to get event schema. | 
 **storeType** | **String**| For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store. | [optional] 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**EventSchema**](EventSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

