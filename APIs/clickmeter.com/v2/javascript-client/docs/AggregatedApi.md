# ClickMeterApi.AggregatedApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregatedGetConversionsSummary**](AggregatedApi.md#aggregatedGetConversionsSummary) | **GET** /aggregated/summary/conversions | Retrieve statistics about a subset of conversions for a timeframe with conversions data
[**aggregatedGetDatapointsSummary**](AggregatedApi.md#aggregatedGetDatapointsSummary) | **GET** /aggregated/summary/datapoints | Retrieve statistics about a subset of datapoints for a timeframe with datapoints data
[**aggregatedGetGroupsSummary**](AggregatedApi.md#aggregatedGetGroupsSummary) | **GET** /aggregated/summary/groups | Retrieve statistics about a subset of groups for a timeframe with groups data
[**aggregatedGetStatisticsList**](AggregatedApi.md#aggregatedGetStatisticsList) | **GET** /aggregated/list | Retrieve statistics about this customer for a timeframe grouped by some temporal entity (day/week/month)
[**aggregatedGetStatisticsSingle**](AggregatedApi.md#aggregatedGetStatisticsSingle) | **GET** /aggregated | Retrieve statistics about this customer for a timeframe



## aggregatedGetConversionsSummary

> ApiCoreDtoAggregatedAggregatedSummaryResult aggregatedGetConversionsSummary(timeFrame, opts)

Retrieve statistics about a subset of conversions for a timeframe with conversions data

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AggregatedApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of conversion (\"deleted\"/\"active\")
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'textSearch': "textSearch_example" // String | Filter fields by this pattern
};
apiInstance.aggregatedGetConversionsSummary(timeFrame, opts, (error, data, response) => {
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
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **status** | **String**| Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## aggregatedGetDatapointsSummary

> ApiCoreDtoAggregatedAggregatedSummaryResult aggregatedGetDatapointsSummary(timeFrame, type, opts)

Retrieve statistics about a subset of datapoints for a timeframe with datapoints data

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AggregatedApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let type = "type_example"; // String | Type of datapoint (\"tl\"/\"tp\")
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true, // Boolean | Is the datapoint marked as favourite
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'groupId': 789, // Number | Filter by this group id
  'textSearch': "textSearch_example" // String | Filter fields by this pattern
};
apiInstance.aggregatedGetDatapointsSummary(timeFrame, type, opts, (error, data, response) => {
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
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] 
 **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **favourite** | **Boolean**| Is the datapoint marked as favourite | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **groupId** | **Number**| Filter by this group id | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## aggregatedGetGroupsSummary

> ApiCoreDtoAggregatedAggregatedSummaryResult aggregatedGetGroupsSummary(timeFrame, opts)

Retrieve statistics about a subset of groups for a timeframe with groups data

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AggregatedApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of group (\"deleted\"/\"active\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true, // Boolean | Is the group marked as favourite
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'textSearch': "textSearch_example" // String | Filter fields by this pattern
};
apiInstance.aggregatedGetGroupsSummary(timeFrame, opts, (error, data, response) => {
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
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **status** | **String**| Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] 
 **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **favourite** | **Boolean**| Is the group marked as favourite | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## aggregatedGetStatisticsList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult aggregatedGetStatisticsList(timeFrame, opts)

Retrieve statistics about this customer for a timeframe grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AggregatedApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.aggregatedGetStatisticsList(timeFrame, opts, (error, data, response) => {
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
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **groupBy** | **String**| The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;. | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult**](ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## aggregatedGetStatisticsSingle

> ApiCoreDtoAggregatedAggregatedResult aggregatedGetStatisticsSingle(timeFrame, opts)

Retrieve statistics about this customer for a timeframe

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.AggregatedApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'hourly': true, // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
  'onlyFavorites': "onlyFavorites_example" // String | 
};
apiInstance.aggregatedGetStatisticsSingle(timeFrame, opts, (error, data, response) => {
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
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] 
 **onlyFavorites** | **String**|  | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedResult**](ApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

