# RubrikRestApi.EventSeriesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryEventSeriesByIdV1**](EventSeriesApi.md#queryEventSeriesByIdV1) | **GET** /event_series/{id} | Get all events and relevant information associated with an event series ID



## queryEventSeriesByIdV1

> EventSeriesSummaryV1 queryEventSeriesByIdV1(id)

Get all events and relevant information associated with an event series ID

Gets all events, event series, SLA Domain, and object information that is associated with a specified event series ID.

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

let apiInstance = new RubrikRestApi.EventSeriesApi();
let id = "id_example"; // String | The ID of the event series.
apiInstance.queryEventSeriesByIdV1(id, (error, data, response) => {
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
 **id** | **String**| The ID of the event series. | 

### Return type

[**EventSeriesSummaryV1**](EventSeriesSummaryV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

