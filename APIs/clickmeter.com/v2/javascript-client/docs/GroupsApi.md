# ClickMeterApi.GroupsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsCount**](GroupsApi.md#groupsCount) | **GET** /groups/count | Count the groups associated to the user.
[**groupsDelete**](GroupsApi.md#groupsDelete) | **DELETE** /groups/{id} | Delete group specified by id
[**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups | List of all the groups associated to the user.
[**groupsGetDatapoints**](GroupsApi.md#groupsGetDatapoints) | **GET** /groups/{id}/datapoints | List of all the datapoints associated to the user in this group.
[**groupsGetDatapointsCount**](GroupsApi.md#groupsGetDatapointsCount) | **GET** /groups/{id}/datapoints/count | Count the datapoints associated to the user in this group.
[**groupsGetDatapointsSummary**](GroupsApi.md#groupsGetDatapointsSummary) | **GET** /groups/{id}/aggregated/summary | Retrieve statistics about a subset of datapoints for a timeframe with datapoints data
[**groupsGetHits**](GroupsApi.md#groupsGetHits) | **GET** /groups/{id}/hits | Retrieve the list of events related to this group.
[**groupsGetStatisticsAggregatedSingle**](GroupsApi.md#groupsGetStatisticsAggregatedSingle) | **GET** /groups/aggregated | Retrieve statistics about this customer for a timeframe by groups
[**groupsGetStatisticsAllList**](GroupsApi.md#groupsGetStatisticsAllList) | **GET** /groups/aggregated/list | Retrieve statistics about all groups of this customer for a timeframe grouped by some temporal entity (day/week/month)
[**groupsGetStatisticsList**](GroupsApi.md#groupsGetStatisticsList) | **GET** /groups/{id}/aggregated/list | Retrieve statistics about this group for a timeframe grouped by some temporal entity (day/week/month)
[**groupsGetStatisticsSingle**](GroupsApi.md#groupsGetStatisticsSingle) | **GET** /groups/{id}/aggregated | Retrieve statistics about this group for a timeframe
[**groupsIdGet**](GroupsApi.md#groupsIdGet) | **GET** /groups/{id} | Get a group
[**groupsPatchFavourite**](GroupsApi.md#groupsPatchFavourite) | **PUT** /groups/{id}/favourite | Fast switch the \&quot;favourite\&quot; field of a group
[**groupsPatchNotes**](GroupsApi.md#groupsPatchNotes) | **PUT** /groups/{id}/notes | Fast patch the \&quot;notes\&quot; field of a group
[**groupsPost**](GroupsApi.md#groupsPost) | **POST** /groups/{id} | Update a group
[**groupsPut**](GroupsApi.md#groupsPut) | **POST** /groups | Create a group
[**groupsPutDatapoint**](GroupsApi.md#groupsPutDatapoint) | **POST** /groups/{id}/datapoints | Create a datapoint in this group



## groupsCount

> ApiCoreResponsesCountResponce groupsCount(opts)

Count the groups associated to the user.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let opts = {
  'status': "status_example", // String | Status of the datapoint
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude groups created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example", // String | Exclude groups created after this date (YYYYMMDD)
  'write': true // Boolean | Write permission
};
apiInstance.groupsCount(opts, (error, data, response) => {
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
 **status** | **String**| Status of the datapoint | [optional] 
 **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] 
 **write** | **Boolean**| Write permission | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## groupsDelete

> ApiCoreResponsesEntityUriSystemInt64 groupsDelete(id)

Delete group specified by id

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
apiInstance.groupsDelete(id, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## groupsGet

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 groupsGet(opts)

List of all the groups associated to the user.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let opts = {
  'offset': 0, // Number | Where to start when retrieving elements. Default is 0 if not specified.
  'limit': 20, // Number | Maximum elements to retrieve. Default to 20 if not specified.
  'status': "status_example", // String | Status of the group
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude groups created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example", // String | Exclude groups created after this date (YYYYMMDD)
  'write': true // Boolean | Write permission
};
apiInstance.groupsGet(opts, (error, data, response) => {
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
 **status** | **String**| Status of the group | [optional] 
 **tags** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude groups created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude groups created after this date (YYYYMMDD) | [optional] 
 **write** | **Boolean**| Write permission | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGetDatapoints

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 groupsGetDatapoints(id, opts)

List of all the datapoints associated to the user in this group.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
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
apiInstance.groupsGetDatapoints(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
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


## groupsGetDatapointsCount

> ApiCoreResponsesCountResponce groupsGetDatapointsCount(id, opts)

Count the datapoints associated to the user in this group.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
let opts = {
  'type': "type_example", // String | Type of the datapoint (\"tp\"/\"tl\")
  'status': "status_example", // String | Status of the datapoint
  'tags': "tags_example", // String | A comma separated list of tags you want to filter with.
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'onlyFavorites': true, // Boolean | Filter fields by favourite status
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.groupsGetDatapointsCount(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
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


## groupsGetDatapointsSummary

> ApiCoreDtoAggregatedAggregatedSummaryResult groupsGetDatapointsSummary(id, timeFrame, opts)

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

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Filter by this group id
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'type': "type_example", // String | Type of datapoint (\"tl\"/\"tp\")
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true, // Boolean | Is the datapoint marked as favourite
  'sortBy': "sortBy_example", // String | Field to sort by
  'sortDirection': "sortDirection_example", // String | Direction of sort \"asc\" or \"desc\"
  'offset': 0, // Number | Offset where to start from
  'limit': 20, // Number | Limit results to this number
  'textSearch': "textSearch_example" // String | Filter fields by this pattern
};
apiInstance.groupsGetDatapointsSummary(id, timeFrame, opts, (error, data, response) => {
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
 **id** | **Number**| Filter by this group id | 
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] 
 **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **favourite** | **Boolean**| Is the datapoint marked as favourite | [optional] 
 **sortBy** | **String**| Field to sort by | [optional] 
 **sortDirection** | **String**| Direction of sort \&quot;asc\&quot; or \&quot;desc\&quot; | [optional] 
 **offset** | **Number**| Offset where to start from | [optional] [default to 0]
 **limit** | **Number**| Limit results to this number | [optional] [default to 20]
 **textSearch** | **String**| Filter fields by this pattern | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedSummaryResult**](ApiCoreDtoAggregatedAggregatedSummaryResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGetHits

> ApiCoreDtoClickStreamHitListPage groupsGetHits(id, timeframe, opts)

Retrieve the list of events related to this group.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
let timeframe = "timeframe_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'limit': 56, // Number | Limit results to this number
  'offset': "offset_example", // String | Offset where to start from (it's the lastKey field in the response object)
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'filter': "filter_example" // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
};
apiInstance.groupsGetHits(id, timeframe, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
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


## groupsGetStatisticsAggregatedSingle

> ApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsAggregatedSingle(timeFrame, opts)

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

let apiInstance = new ClickMeterApi.GroupsApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'hourly': true, // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
  'status': "status_example", // String | Status of group (\"deleted\"/\"active\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true // Boolean | Is the group is marked as favourite
};
apiInstance.groupsGetStatisticsAggregatedSingle(timeFrame, opts, (error, data, response) => {
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
 **status** | **String**| Status of group (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] 
 **tag** | **String**| A comma separated list of tags you want to filter with. | [optional] 
 **favourite** | **Boolean**| Is the group is marked as favourite | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedResult**](ApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGetStatisticsAllList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsAllList(timeFrame, opts)

Retrieve statistics about all groups of this customer for a timeframe grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of group (\"deleted\"/\"active\")
  'tag': "tag_example", // String | A comma separated list of tags you want to filter with.
  'favourite': true, // Boolean | Is the group is marked as favourite
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.groupsGetStatisticsAllList(timeFrame, opts, (error, data, response) => {
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
 **favourite** | **Boolean**| Is the group is marked as favourite | [optional] 
 **groupBy** | **String**| The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;. | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult**](ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsGetStatisticsList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsList(id, timeFrame, opts)

Retrieve statistics about this group for a timeframe grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.groupsGetStatisticsList(id, timeFrame, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
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


## groupsGetStatisticsSingle

> ApiCoreDtoAggregatedAggregatedResult groupsGetStatisticsSingle(id, timeFrame, opts)

Retrieve statistics about this group for a timeframe

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'hourly': true // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
};
apiInstance.groupsGetStatisticsSingle(id, timeFrame, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
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


## groupsIdGet

> ApiCoreDtoGroupsGroup groupsIdGet(id)

Get a group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | The id of the group
apiInstance.groupsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The id of the group | 

### Return type

[**ApiCoreDtoGroupsGroup**](ApiCoreDtoGroupsGroup.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## groupsPatchFavourite

> ApiCoreResponsesEntityUriSystemInt64 groupsPatchFavourite(id)

Fast switch the \&quot;favourite\&quot; field of a group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
apiInstance.groupsPatchFavourite(id, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## groupsPatchNotes

> ApiCoreResponsesEntityUriSystemInt64 groupsPatchNotes(id, apiCoreRequestsGenericTextPatch)

Fast patch the \&quot;notes\&quot; field of a group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | Id of the group
let apiCoreRequestsGenericTextPatch = new ClickMeterApi.ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | Patch requests
apiInstance.groupsPatchNotes(id, apiCoreRequestsGenericTextPatch, (error, data, response) => {
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
 **id** | **Number**| Id of the group | 
 **apiCoreRequestsGenericTextPatch** | [**ApiCoreRequestsGenericTextPatch**](ApiCoreRequestsGenericTextPatch.md)| Patch requests | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## groupsPost

> ApiCoreResponsesEntityUriSystemInt64 groupsPost(id, apiCoreDtoGroupsGroup)

Update a group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | The id of the group
let apiCoreDtoGroupsGroup = new ClickMeterApi.ApiCoreDtoGroupsGroup(); // ApiCoreDtoGroupsGroup | The body of the group
apiInstance.groupsPost(id, apiCoreDtoGroupsGroup, (error, data, response) => {
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
 **id** | **Number**| The id of the group | 
 **apiCoreDtoGroupsGroup** | [**ApiCoreDtoGroupsGroup**](ApiCoreDtoGroupsGroup.md)| The body of the group | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## groupsPut

> ApiCoreResponsesEntityUriSystemInt64 groupsPut(apiCoreDtoGroupsGroup)

Create a group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let apiCoreDtoGroupsGroup = new ClickMeterApi.ApiCoreDtoGroupsGroup(); // ApiCoreDtoGroupsGroup | The body of the group
apiInstance.groupsPut(apiCoreDtoGroupsGroup, (error, data, response) => {
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
 **apiCoreDtoGroupsGroup** | [**ApiCoreDtoGroupsGroup**](ApiCoreDtoGroupsGroup.md)| The body of the group | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## groupsPutDatapoint

> ApiCoreResponsesEntityUriSystemInt64 groupsPutDatapoint(id, apiCoreDtoDatapointsDatapoint)

Create a datapoint in this group

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.GroupsApi();
let id = 789; // Number | The id of the group
let apiCoreDtoDatapointsDatapoint = new ClickMeterApi.ApiCoreDtoDatapointsDatapoint(); // ApiCoreDtoDatapointsDatapoint | The body of the datapoint
apiInstance.groupsPutDatapoint(id, apiCoreDtoDatapointsDatapoint, (error, data, response) => {
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
 **id** | **Number**| The id of the group | 
 **apiCoreDtoDatapointsDatapoint** | [**ApiCoreDtoDatapointsDatapoint**](ApiCoreDtoDatapointsDatapoint.md)| The body of the datapoint | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml

