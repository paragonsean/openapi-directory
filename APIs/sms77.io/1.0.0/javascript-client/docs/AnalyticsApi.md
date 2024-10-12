# SevenIoApi.AnalyticsApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics**](AnalyticsApi.md#analytics) | **GET** /analytics | 



## analytics

> Analytics200Response analytics(opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.AnalyticsApi();
let opts = {
  'start': "start_example", // String | Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set.
  'end': "end_example", // String | End date of the statistics in the format YYYY-MM-DD. By default, the current day.
  'label': "label_example", // String | Shows only data of a specific label.
  'subaccounts': "subaccounts_example", // String | Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts.
  'groupBy': "groupBy_example" // String | Defines the grouping of the data.
};
apiInstance.analytics(opts, (error, data, response) => {
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
 **start** | **String**| Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set. | [optional] 
 **end** | **String**| End date of the statistics in the format YYYY-MM-DD. By default, the current day. | [optional] 
 **label** | **String**| Shows only data of a specific label. | [optional] 
 **subaccounts** | **String**| Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts. | [optional] 
 **groupBy** | **String**| Defines the grouping of the data. | [optional] 

### Return type

[**Analytics200Response**](Analytics200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

