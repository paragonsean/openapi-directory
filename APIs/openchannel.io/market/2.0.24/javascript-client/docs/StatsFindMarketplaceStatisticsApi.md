# OpenChannelMarketApi.StatsFindMarketplaceStatisticsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statsIncrementFieldPost**](StatsFindMarketplaceStatisticsApi.md#statsIncrementFieldPost) | **POST** /stats/increment/{field} | Increments a statistics field
[**statsSeriesPeriodFieldsGet**](StatsFindMarketplaceStatisticsApi.md#statsSeriesPeriodFieldsGet) | **GET** /stats/series/{period}/{fields} | Return a timeseries for a particular field
[**statsTotalGet**](StatsFindMarketplaceStatisticsApi.md#statsTotalGet) | **GET** /stats/total | Returns the total number of events for a particular field.



## statsIncrementFieldPost

> statsIncrementFieldPost(field, appId, opts)

Increments a statistics field

increment a statistics field

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.StatsFindMarketplaceStatisticsApi();
let field = "field_example"; // String | The field to be incremented
let appId = "appId_example"; // String | The id of the app associated with this statistic value
let opts = {
  'userId': "userId_example", // String | The id of the user that is performing the action
  'value': 56, // Number | The increment amount. Default is 1 if no value is provided.
  'date': 789 // Number | The date (in millis) for when this increment occurred. The default is the current date if no value is provided.
};
apiInstance.statsIncrementFieldPost(field, appId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **String**| The field to be incremented | 
 **appId** | **String**| The id of the app associated with this statistic value | 
 **userId** | **String**| The id of the user that is performing the action | [optional] 
 **value** | **Number**| The increment amount. Default is 1 if no value is provided. | [optional] 
 **date** | **Number**| The date (in millis) for when this increment occurred. The default is the current date if no value is provided. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## statsSeriesPeriodFieldsGet

> [[Object]] statsSeriesPeriodFieldsGet(period, fields, opts)

Return a timeseries for a particular field

Return a timeseries nested array containing date and value. Example: [[1406520000000,2],[1406606400000,34],[1406692800000,245],...]

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.StatsFindMarketplaceStatisticsApi();
let period = "period_example"; // String | The period for the series (day or month)
let fields = "fields_example"; // String | The field to be graphed. This also be a comma separated list of fields and the result will be a single timeseries containing the sum of all fields.
let opts = {
  'start': 789, // Number | The start date for this series (in millis)
  'end': 789, // Number | The end date for this series (in millis)
  'query': "query_example" // String | A query document. Example: {'developerId': '112'} matches all the apps that have the developer with id 112
};
apiInstance.statsSeriesPeriodFieldsGet(period, fields, opts, (error, data, response) => {
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
 **period** | **String**| The period for the series (day or month) | 
 **fields** | **String**| The field to be graphed. This also be a comma separated list of fields and the result will be a single timeseries containing the sum of all fields. | 
 **start** | **Number**| The start date for this series (in millis) | [optional] 
 **end** | **Number**| The end date for this series (in millis) | [optional] 
 **query** | **String**| A query document. Example: {&#39;developerId&#39;: &#39;112&#39;} matches all the apps that have the developer with id 112 | [optional] 

### Return type

**[[Object]]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## statsTotalGet

> Total statsTotalGet(fields, opts)

Returns the total number of events for a particular field.

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.StatsFindMarketplaceStatisticsApi();
let fields = "fields_example"; // String | A comma seperated list of all the fields to be returned in the total (available by default: dislikes, likes, reviews, totalSales, developerSales, marketplaceSales, downloads, ownerships, views)
let opts = {
  'query': "query_example", // String | A query document. Example: {'developerId': '112'} matches all the apps that have the developer with id 112
  'start': 789, // Number | The start date for this total (in millis)
  'end': 789 // Number | The end date for this total (in millis)
};
apiInstance.statsTotalGet(fields, opts, (error, data, response) => {
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
 **fields** | **String**| A comma seperated list of all the fields to be returned in the total (available by default: dislikes, likes, reviews, totalSales, developerSales, marketplaceSales, downloads, ownerships, views) | 
 **query** | **String**| A query document. Example: {&#39;developerId&#39;: &#39;112&#39;} matches all the apps that have the developer with id 112 | [optional] 
 **start** | **Number**| The start date for this total (in millis) | [optional] 
 **end** | **Number**| The end date for this total (in millis) | [optional] 

### Return type

[**Total**](Total.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

