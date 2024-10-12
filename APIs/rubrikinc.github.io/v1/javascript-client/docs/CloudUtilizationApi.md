# RubrikRestApi.CloudUtilizationApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doCloudOutForecast**](CloudUtilizationApi.md#doCloudOutForecast) | **POST** /cloud_utilization/cloud_out_forecast | Forecast of the cloud utilization for CloudOut



## doCloudOutForecast

> CloudOutForecastSummary doCloudOutForecast(cloudOutForecastRequest)

Forecast of the cloud utilization for CloudOut

Forecast of the cloud storage and compute utilization on cloud archival location according to the SLA Domain parameters.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CloudUtilizationApi();
let cloudOutForecastRequest = new RubrikRestApi.CloudOutForecastRequest(); // CloudOutForecastRequest | Object that contains the CloudOut forecast request.
apiInstance.doCloudOutForecast(cloudOutForecastRequest, (error, data, response) => {
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
 **cloudOutForecastRequest** | [**CloudOutForecastRequest**](CloudOutForecastRequest.md)| Object that contains the CloudOut forecast request. | 

### Return type

[**CloudOutForecastSummary**](CloudOutForecastSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

