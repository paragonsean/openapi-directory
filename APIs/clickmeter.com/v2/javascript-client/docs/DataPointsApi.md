# ClickMeterApi.DataPointsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataPointsBatchDelete**](DataPointsApi.md#dataPointsBatchDelete) | **DELETE** /datapoints/batch | Delete multiple datapoints
[**dataPointsBatchPost**](DataPointsApi.md#dataPointsBatchPost) | **POST** /datapoints/batch | Update multiple datapoints
[**dataPointsBatchPut**](DataPointsApi.md#dataPointsBatchPut) | **PUT** /datapoints/batch | Create multiple datapoints
[**dataPointsCount**](DataPointsApi.md#dataPointsCount) | **GET** /datapoints/count | Count the datapoints associated to the user
[**dataPointsDelete**](DataPointsApi.md#dataPointsDelete) | **DELETE** /datapoints/{id} | Delete a datapoint
[**dataPointsGet**](DataPointsApi.md#dataPointsGet) | **GET** /datapoints | List of all the datapoints associated to the user
[**dataPointsGetHits**](DataPointsApi.md#dataPointsGetHits) | **GET** /datapoints/{id}/hits | Retrieve the list of events related to this datapoint.
[**dataPointsGetStatisticsAggregatedSingle**](DataPointsApi.md#dataPointsGetStatisticsAggregatedSingle) | **GET** /datapoints/aggregated | Retrieve statistics about this customer for a timeframe by groups
[**dataPointsGetStatisticsAllList**](DataPointsApi.md#dataPointsGetStatisticsAllList) | **GET** /datapoints/aggregated/list | Retrieve statistics about all datapoints of this customer for a timeframe grouped by some temporal entity (day/week/month)
[**dataPointsGetStatisticsList**](DataPointsApi.md#dataPointsGetStatisticsList) | **GET** /datapoints/{id}/aggregated/list | Retrieve statistics about this datapoint for a timeframe grouped by some temporal entity (day/week/month)
[**dataPointsGetStatisticsSingle**](DataPointsApi.md#dataPointsGetStatisticsSingle) | **GET** /datapoints/{id}/aggregated | Retrieve statistics about this datapoint for a timeframe
[**dataPointsPatchFavourite**](DataPointsApi.md#dataPointsPatchFavourite) | **PUT** /datapoints/{id}/favourite | Fast switch the \&quot;favourite\&quot; field of a datapoint
[**dataPointsPatchNotes**](DataPointsApi.md#dataPointsPatchNotes) | **PUT** /datapoints/{id}/notes | Fast patch the \&quot;notes\&quot; field of a datapoint
[**dataPointsPost**](DataPointsApi.md#dataPointsPost) | **POST** /datapoints/{id} | Update a datapoint
[**dataPointsPut**](DataPointsApi.md#dataPointsPut) | **POST** /datapoints | Create a datapoint
[**datapointsIdGet**](DataPointsApi.md#datapointsIdGet) | **GET** /datapoints/{id} | Get a datapoint



## dataPointsBatchDelete

> ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 dataPointsBatchDelete(apiCoreRequestsDeleteBatch)

Delete multiple datapoints

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let apiCoreRequestsDeleteBatch = new ClickMeterApi.ApiCoreRequestsDeleteBatch(); // ApiCoreRequestsDeleteBatch | A json containing the datapoints to delete.
apiInstance.dataPointsBatchDelete(apiCoreRequestsDeleteBatch, (error, data, response) => {
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
 **apiCoreRequestsDeleteBatch** | [**ApiCoreRequestsDeleteBatch**](ApiCoreRequestsDeleteBatch.md)| A json containing the datapoints to delete. | 

### Return type

[**ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64**](ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json


## dataPointsBatchPost

> ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 dataPointsBatchPost(apiCoreRequestsDatapointsBatch)

Update multiple datapoints

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let apiCoreRequestsDatapointsBatch = new ClickMeterApi.ApiCoreRequestsDatapointsBatch(); // ApiCoreRequestsDatapointsBatch | A json containing the datapoints to update.
apiInstance.dataPointsBatchPost(apiCoreRequestsDatapointsBatch, (error, data, response) => {
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
 **apiCoreRequestsDatapointsBatch** | [**ApiCoreRequestsDatapointsBatch**](ApiCoreRequestsDatapointsBatch.md)| A json containing the datapoints to update. | 

### Return type

[**ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64**](ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json


## dataPointsBatchPut

> ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64 dataPointsBatchPut(apiCoreRequestsDatapointsBatch)

Create multiple datapoints

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let apiCoreRequestsDatapointsBatch = new ClickMeterApi.ApiCoreRequestsDatapointsBatch(); // ApiCoreRequestsDatapointsBatch | A json containing the datapoints to create.
apiInstance.dataPointsBatchPut(apiCoreRequestsDatapointsBatch, (error, data, response) => {
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
 **apiCoreRequestsDatapointsBatch** | [**ApiCoreRequestsDatapointsBatch**](ApiCoreRequestsDatapointsBatch.md)| A json containing the datapoints to create. | 

### Return type

[**ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64**](ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json


## dataPointsCount

> ApiCoreResponsesCountResponce dataPointsCount(opts)

Count the datapoints associated to the user

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let opts = {
  'type': "type_example", // String | Type of the datapoint (\"tp\"/\"tl\")
  'status': "status_example", // String | Status of the datapoint
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'onlyFavorites': true, // Boolean | Filter fields by favourite status
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.dataPointsCount(opts, (error, data, response) => {
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
 **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] 
 **status** | **String**| Status of the datapoint | [optional] 
 **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## dataPointsDelete

> ApiCoreResponsesEntityUriSystemInt64 dataPointsDelete(id)

Delete a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | The id of the datapoint
apiInstance.dataPointsDelete(id, (error, data, response) => {
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
 **id** | **Number**| The id of the datapoint | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## dataPointsGet

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 dataPointsGet(opts)

List of all the datapoints associated to the user

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20, // Number | Maximum elements to retrieve. Default to 20 if not specified.
  'type': "type_example", // String | Type of the datapoint (\"tp\"/\"tl\")
  'status': "status_example", // String | Status of the datapoint
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'onlyFavorites': true, // Boolean | Filter fields by favourite status
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.dataPointsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Where to start when retrieving elements. Default is 0 if not specified. | [optional] [default to 0]
 **limit** | **Number**| Maximum elements to retrieve. Default to 20 if not specified. | [optional] [default to 20]
 **type** | **String**| Type of the datapoint (\&quot;tp\&quot;/\&quot;tl\&quot;) | [optional] 
 **status** | **String**| Status of the datapoint | [optional] 
 **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **onlyFavorites** | **Boolean**| Filter fields by favourite status | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## dataPointsGetHits

> ApiCoreDtoClickStreamHitListPage dataPointsGetHits(id, timeframe, opts)

Retrieve the list of events related to this datapoint.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | Id of the datapoint
let timeframe = "timeframe_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'limit': 56, // Number | Limit results to this number
  'offset': "offset_example", // String | Offset where to start from (it's the lastKey field in the response object)
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'filter': "filter_example" // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
};
apiInstance.dataPointsGetHits(id, timeframe, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the datapoint | 
 **timeframe** | **String**| Timeframe of the request. See list at $timeframeList | 
 **limit** | **Number**| Limit results to this number | [optional] 
 **offset** | **String**| Offset where to start from (it&#39;s the lastKey field in the response object) | [optional] 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **filter** | **String**| Filter event type (\&quot;spiders\&quot;/\&quot;uniques\&quot;/\&quot;nonuniques\&quot;/\&quot;conversions\&quot;) | [optional] 

### Return type

[**ApiCoreDtoClickStreamHitListPage**](ApiCoreDtoClickStreamHitListPage.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## dataPointsGetStatisticsAggregatedSingle

> ApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsAggregatedSingle(timeFrame, opts)

Retrieve statistics about this customer for a timeframe by groups

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'type': "type_example", // String | Type of datapoint (\"tl\"/\"tp\")
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'hourly': true, // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
  'status': "status_example", // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true // Boolean | Is the datapoint is marked as favourite
};
apiInstance.dataPointsGetStatisticsAggregatedSingle(timeFrame, opts, (error, data, response) => {
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
 **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] 
 **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] 
 **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **favourite** | **Boolean**| Is the datapoint is marked as favourite | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedResult**](ApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## dataPointsGetStatisticsAllList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsAllList(type, timeFrame, opts)

Retrieve statistics about all datapoints of this customer for a timeframe grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let type = "type_example"; // String | Type of datapoint (\"tl\"/\"tp\")
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true, // Boolean | Is the datapoint is marked as favourite
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.dataPointsGetStatisticsAllList(type, timeFrame, opts, (error, data, response) => {
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
 **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | 
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] 
 **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **favourite** | **Boolean**| Is the datapoint is marked as favourite | [optional] 
 **groupBy** | **String**| The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;. | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult**](ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## dataPointsGetStatisticsList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsList(id, timeFrame, opts)

Retrieve statistics about this datapoint for a timeframe grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | Id of the datapoint
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.dataPointsGetStatisticsList(id, timeFrame, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the datapoint | 
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


## dataPointsGetStatisticsSingle

> ApiCoreDtoAggregatedAggregatedResult dataPointsGetStatisticsSingle(id, timeFrame, opts)

Retrieve statistics about this datapoint for a timeframe

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | Id of the datapoint
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'hourly': true // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
};
apiInstance.dataPointsGetStatisticsSingle(id, timeFrame, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the datapoint | 
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedResult**](ApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## dataPointsPatchFavourite

> ApiCoreResponsesEntityUriSystemInt64 dataPointsPatchFavourite(id)

Fast switch the \&quot;favourite\&quot; field of a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | Id of the datapoint
apiInstance.dataPointsPatchFavourite(id, (error, data, response) => {
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
 **id** | **Number**| Id of the datapoint | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## dataPointsPatchNotes

> ApiCoreResponsesEntityUriSystemInt64 dataPointsPatchNotes(id, apiCoreRequestsGenericTextPatch)

Fast patch the \&quot;notes\&quot; field of a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | Id of the datapoint
let apiCoreRequestsGenericTextPatch = new ClickMeterApi.ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | Patch requests
apiInstance.dataPointsPatchNotes(id, apiCoreRequestsGenericTextPatch, (error, data, response) => {
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
 **id** | **Number**| Id of the datapoint | 
 **apiCoreRequestsGenericTextPatch** | [**ApiCoreRequestsGenericTextPatch**](ApiCoreRequestsGenericTextPatch.md)| Patch requests | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## dataPointsPost

> ApiCoreResponsesEntityUriSystemInt64 dataPointsPost(id, apiCoreDtoDatapointsDatapoint)

Update a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | The id of the datapoint
let apiCoreDtoDatapointsDatapoint = new ClickMeterApi.ApiCoreDtoDatapointsDatapoint(); // ApiCoreDtoDatapointsDatapoint | The body of the datapoint
apiInstance.dataPointsPost(id, apiCoreDtoDatapointsDatapoint, (error, data, response) => {
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
 **id** | **Number**| The id of the datapoint | 
 **apiCoreDtoDatapointsDatapoint** | [**ApiCoreDtoDatapointsDatapoint**](ApiCoreDtoDatapointsDatapoint.md)| The body of the datapoint | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## dataPointsPut

> ApiCoreResponsesEntityUriSystemInt64 dataPointsPut(apiCoreDtoDatapointsDatapoint)

Create a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let apiCoreDtoDatapointsDatapoint = new ClickMeterApi.ApiCoreDtoDatapointsDatapoint(); // ApiCoreDtoDatapointsDatapoint | The body of the datapoint
apiInstance.dataPointsPut(apiCoreDtoDatapointsDatapoint, (error, data, response) => {
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
 **apiCoreDtoDatapointsDatapoint** | [**ApiCoreDtoDatapointsDatapoint**](ApiCoreDtoDatapointsDatapoint.md)| The body of the datapoint | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## datapointsIdGet

> ApiCoreDtoDatapointsDatapoint datapointsIdGet(id)

Get a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.DataPointsApi();
let id = 789; // Number | The id of the datapoint
apiInstance.datapointsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The id of the datapoint | 

### Return type

[**ApiCoreDtoDatapointsDatapoint**](ApiCoreDtoDatapointsDatapoint.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

