# TimeSeriesInsightsClient.ModelSettingsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modelSettingsGet**](ModelSettingsApi.md#modelSettingsGet) | **GET** /timeseries/modelSettings | 
[**modelSettingsUpdate**](ModelSettingsApi.md#modelSettingsUpdate) | **PATCH** /timeseries/modelSettings | 



## modelSettingsGet

> ModelSettingsResponse modelSettingsGet(apiVersion, opts)



Returns the model settings which includes model display name, Time Series ID properties and default type ID. Every pay-as-you-go environment has a model that is automatically created.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ModelSettingsApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let opts = {
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.modelSettingsGet(apiVersion, opts, (error, data, response) => {
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
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**ModelSettingsResponse**](ModelSettingsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## modelSettingsUpdate

> ModelSettingsResponse modelSettingsUpdate(apiVersion, parameters, opts)



Updates time series model settings - either the model name or default type ID.

### Example

```javascript
import TimeSeriesInsightsClient from 'time_series_insights_client';
let defaultClient = TimeSeriesInsightsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TimeSeriesInsightsClient.ModelSettingsApi();
let apiVersion = "'2018-11-01-preview'"; // String | Version of the API to be used with the client request. Currently supported version is \"2018-11-01-preview\".
let parameters = new TimeSeriesInsightsClient.UpdateModelSettingsRequest(); // UpdateModelSettingsRequest | Model settings update request body.
let opts = {
  'xMsClientRequestId': "xMsClientRequestId_example", // String | Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
  'xMsClientSessionId': "xMsClientSessionId_example" // String | Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
};
apiInstance.modelSettingsUpdate(apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**UpdateModelSettingsRequest**](UpdateModelSettingsRequest.md)| Model settings update request body. | 
 **xMsClientRequestId** | **String**| Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request. | [optional] 
 **xMsClientSessionId** | **String**| Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests. | [optional] 

### Return type

[**ModelSettingsResponse**](ModelSettingsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

