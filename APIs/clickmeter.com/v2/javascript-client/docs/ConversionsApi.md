# ClickMeterApi.ConversionsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversionsConversionIdDatapointsBatchPatchPut**](ConversionsApi.md#conversionsConversionIdDatapointsBatchPatchPut) | **PUT** /conversions/{conversionId}/datapoints/batch/patch | Modify the association between a conversion and multiple datapoints
[**conversionsConversionIdGet**](ConversionsApi.md#conversionsConversionIdGet) | **GET** /conversions/{conversionId} | Retrieve conversion specified by id
[**conversionsCount**](ConversionsApi.md#conversionsCount) | **GET** /conversions/count | Retrieve a count of conversions
[**conversionsDelete**](ConversionsApi.md#conversionsDelete) | **DELETE** /conversions/{conversionId} | Delete conversion specified by id
[**conversionsGet**](ConversionsApi.md#conversionsGet) | **GET** /conversions | Retrieve a list of conversions
[**conversionsGetDatapoints**](ConversionsApi.md#conversionsGetDatapoints) | **GET** /conversions/{conversionId}/datapoints | Retrieve a list of datapoints connected to this conversion
[**conversionsGetDatapointsCount**](ConversionsApi.md#conversionsGetDatapointsCount) | **GET** /conversions/{conversionId}/datapoints/count | Retrieve a count of datapoints connected to this conversion
[**conversionsGetHits**](ConversionsApi.md#conversionsGetHits) | **GET** /conversions/{conversionId}/hits | Retrieve the list of events related to this conversion.
[**conversionsGetStatisticsAllList**](ConversionsApi.md#conversionsGetStatisticsAllList) | **GET** /conversions/aggregated/list | Retrieve statistics about this customer for a timeframe related to a subset of conversions grouped by some temporal entity (day/week/month)
[**conversionsGetStatisticsList**](ConversionsApi.md#conversionsGetStatisticsList) | **GET** /conversions/{conversionId}/aggregated/list | Retrieve statistics about this conversion for a timeframe grouped by some temporal entity (day/week/month)
[**conversionsGetStatisticsSingle**](ConversionsApi.md#conversionsGetStatisticsSingle) | **GET** /conversions/{conversionId}/aggregated | Retrieve statistics about this conversion for a timeframe
[**conversionsPatch**](ConversionsApi.md#conversionsPatch) | **PUT** /conversions/{conversionId}/datapoints/patch | Modify the association between a conversion and a datapoint
[**conversionsPatchNotes**](ConversionsApi.md#conversionsPatchNotes) | **PUT** /conversions/{conversionId}/notes | Fast patch the \&quot;notes\&quot; field of a conversion
[**conversionsPost**](ConversionsApi.md#conversionsPost) | **POST** /conversions/{conversionId} | Update conversion specified by id
[**conversionsPut**](ConversionsApi.md#conversionsPut) | **POST** /conversions | Create a conversion



## conversionsConversionIdDatapointsBatchPatchPut

> ApiCoreResponsesEntityUriSystemInt64 conversionsConversionIdDatapointsBatchPatchPut(conversionId, apiCoreRequestsPatchBodyBatch)

Modify the association between a conversion and multiple datapoints

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let apiCoreRequestsPatchBodyBatch = new ClickMeterApi.ApiCoreRequestsPatchBodyBatch(); // ApiCoreRequestsPatchBodyBatch | Patch requests
apiInstance.conversionsConversionIdDatapointsBatchPatchPut(conversionId, apiCoreRequestsPatchBodyBatch, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **apiCoreRequestsPatchBodyBatch** | [**ApiCoreRequestsPatchBodyBatch**](ApiCoreRequestsPatchBodyBatch.md)| Patch requests | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsConversionIdGet

> ApiCoreDtoConversionsConversion conversionsConversionIdGet(conversionId)

Retrieve conversion specified by id

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
apiInstance.conversionsConversionIdGet(conversionId, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 

### Return type

[**ApiCoreDtoConversionsConversion**](ApiCoreDtoConversionsConversion.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsCount

> ApiCoreResponsesCountResponce conversionsCount(opts)

Retrieve a count of conversions

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let opts = {
  'status': "status_example", // String | Status of conversion (\"deleted\"/\"active\")
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude conversions created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude conversions created after this date (YYYYMMDD)
};
apiInstance.conversionsCount(opts, (error, data, response) => {
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
 **status** | **String**| Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude conversions created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude conversions created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsDelete

> ApiCoreResponsesEntityUriSystemInt64 conversionsDelete(conversionId)

Delete conversion specified by id

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
apiInstance.conversionsDelete(conversionId, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsGet

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 conversionsGet(opts)

Retrieve a list of conversions

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let opts = {
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'status': "status_example", // String | Status of conversion (\"deleted\"/\"active\")
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude conversions created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude conversions created after this date (YYYYMMDD)
};
apiInstance.conversionsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **status** | **String**| Status of conversion (\&quot;deleted\&quot;/\&quot;active\&quot;) | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude conversions created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude conversions created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## conversionsGetDatapoints

> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 conversionsGetDatapoints(conversionId, opts)

Retrieve a list of datapoints connected to this conversion

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let opts = {
  'offset': 56, // Number | Offset where to start from
  'limit': 56, // Number | Limit results to this number
  'type': "type_example", // String | Type of datapoint (\"tl\"/\"tp\")
  'status': "status_example", // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
  'tags': "tags_example", // String | Filter by this tag name
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.conversionsGetDatapoints(conversionId, opts, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **offset** | **Number**| Offset where to start from | [optional] 
 **limit** | **Number**| Limit results to this number | [optional] 
 **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] 
 **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] 
 **tags** | **String**| Filter by this tag name | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## conversionsGetDatapointsCount

> ApiCoreResponsesCountResponce conversionsGetDatapointsCount(conversionId, opts)

Retrieve a count of datapoints connected to this conversion

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let opts = {
  'type': "type_example", // String | Type of datapoint (\"tl\"/\"tp\")
  'status': "status_example", // String | Status of datapoint (\"deleted\"/\"active\"/\"paused\"/\"spam\")
  'tags': "tags_example", // String | Filter by this tag name
  'textSearch': "textSearch_example", // String | Filter fields by this pattern
  'createdAfter': "createdAfter_example", // String | Exclude datapoints created before this date (YYYYMMDD)
  'createdBefore': "createdBefore_example" // String | Exclude datapoints created after this date (YYYYMMDD)
};
apiInstance.conversionsGetDatapointsCount(conversionId, opts, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **type** | **String**| Type of datapoint (\&quot;tl\&quot;/\&quot;tp\&quot;) | [optional] 
 **status** | **String**| Status of datapoint (\&quot;deleted\&quot;/\&quot;active\&quot;/\&quot;paused\&quot;/\&quot;spam\&quot;) | [optional] 
 **tags** | **String**| Filter by this tag name | [optional] 
 **textSearch** | **String**| Filter fields by this pattern | [optional] 
 **createdAfter** | **String**| Exclude datapoints created before this date (YYYYMMDD) | [optional] 
 **createdBefore** | **String**| Exclude datapoints created after this date (YYYYMMDD) | [optional] 

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsGetHits

> ApiCoreDtoClickStreamHitListPage conversionsGetHits(conversionId, timeframe, opts)

Retrieve the list of events related to this conversion.

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let timeframe = "timeframe_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'limit': 56, // Number | Limit results to this number
  'offset': "offset_example", // String | Offset where to start from (it's the lastKey field in the response object)
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'filter': "filter_example" // String | Filter event type (\"spiders\"/\"uniques\"/\"nonuniques\"/\"conversions\")
};
apiInstance.conversionsGetHits(conversionId, timeframe, opts, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
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


## conversionsGetStatisticsAllList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult conversionsGetStatisticsAllList(timeFrame, opts)

Retrieve statistics about this customer for a timeframe related to a subset of conversions grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'status': "status_example", // String | Status of conversion (\"deleted\"/\"active\")
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.conversionsGetStatisticsAllList(timeFrame, opts, (error, data, response) => {
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
 **groupBy** | **String**| The temporal entity you want to group by (\&quot;week\&quot;/\&quot;month\&quot;). If unspecified is \&quot;day\&quot;. | [optional] 

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult**](ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## conversionsGetStatisticsList

> ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult conversionsGetStatisticsList(conversionId, timeFrame, opts)

Retrieve statistics about this conversion for a timeframe grouped by some temporal entity (day/week/month)

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'groupBy': "groupBy_example" // String | The temporal entity you want to group by (\"week\"/\"month\"). If unspecified is \"day\".
};
apiInstance.conversionsGetStatisticsList(conversionId, timeFrame, opts, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
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


## conversionsGetStatisticsSingle

> ApiCoreDtoAggregatedAggregatedResult conversionsGetStatisticsSingle(conversionId, timeFrame, opts)

Retrieve statistics about this conversion for a timeframe

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let timeFrame = "timeFrame_example"; // String | Timeframe of the request. See list at $timeframeList
let opts = {
  'fromDay': "fromDay_example", // String | If using a \"custom\" timeFrame you can specify the starting day (YYYYMMDD)
  'toDay': "toDay_example", // String | If using a \"custom\" timeFrame you can specify the ending day (YYYYMMDD)
  'tag': "tag_example", // String | Filter by this tag name
  'favourite': true, // Boolean | Is the datapoint marked as favourite
  'hourly': true // Boolean | If using \"yesterday\" or \"today\" timeframe you can ask for the hourly detail
};
apiInstance.conversionsGetStatisticsSingle(conversionId, timeFrame, opts, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **timeFrame** | **String**| Timeframe of the request. See list at $timeframeList | 
 **fromDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the starting day (YYYYMMDD) | [optional] 
 **toDay** | **String**| If using a \&quot;custom\&quot; timeFrame you can specify the ending day (YYYYMMDD) | [optional] 
 **tag** | **String**| Filter by this tag name | [optional] 
 **favourite** | **Boolean**| Is the datapoint marked as favourite | [optional] 
 **hourly** | **Boolean**| If using \&quot;yesterday\&quot; or \&quot;today\&quot; timeframe you can ask for the hourly detail | [optional] 

### Return type

[**ApiCoreDtoAggregatedAggregatedResult**](ApiCoreDtoAggregatedAggregatedResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## conversionsPatch

> ApiCoreResponsesEntityUriSystemInt64 conversionsPatch(conversionId, apiCoreRequestsConversionPatchBody)

Modify the association between a conversion and a datapoint

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let apiCoreRequestsConversionPatchBody = new ClickMeterApi.ApiCoreRequestsConversionPatchBody(); // ApiCoreRequestsConversionPatchBody | Patch request
apiInstance.conversionsPatch(conversionId, apiCoreRequestsConversionPatchBody, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **apiCoreRequestsConversionPatchBody** | [**ApiCoreRequestsConversionPatchBody**](ApiCoreRequestsConversionPatchBody.md)| Patch request | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsPatchNotes

> ApiCoreResponsesEntityUriSystemInt64 conversionsPatchNotes(conversionId, apiCoreRequestsGenericTextPatch)

Fast patch the \&quot;notes\&quot; field of a conversion

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let apiCoreRequestsGenericTextPatch = new ClickMeterApi.ApiCoreRequestsGenericTextPatch(); // ApiCoreRequestsGenericTextPatch | Patch requests
apiInstance.conversionsPatchNotes(conversionId, apiCoreRequestsGenericTextPatch, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **apiCoreRequestsGenericTextPatch** | [**ApiCoreRequestsGenericTextPatch**](ApiCoreRequestsGenericTextPatch.md)| Patch requests | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsPost

> ApiCoreResponsesEntityUriSystemInt64 conversionsPost(conversionId, apiCoreDtoConversionsConversion)

Update conversion specified by id

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let conversionId = 789; // Number | Id of the conversion
let apiCoreDtoConversionsConversion = new ClickMeterApi.ApiCoreDtoConversionsConversion(); // ApiCoreDtoConversionsConversion | Updated body of the conversion
apiInstance.conversionsPost(conversionId, apiCoreDtoConversionsConversion, (error, data, response) => {
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
 **conversionId** | **Number**| Id of the conversion | 
 **apiCoreDtoConversionsConversion** | [**ApiCoreDtoConversionsConversion**](ApiCoreDtoConversionsConversion.md)| Updated body of the conversion | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## conversionsPut

> ApiCoreResponsesEntityUriSystemInt64 conversionsPut(apiCoreDtoConversionsConversion)

Create a conversion

### Example

```javascript
import ClickMeterApi from 'click_meter_api';
let defaultClient = ClickMeterApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClickMeterApi.ConversionsApi();
let apiCoreDtoConversionsConversion = new ClickMeterApi.ApiCoreDtoConversionsConversion(); // ApiCoreDtoConversionsConversion | The body of the conversion
apiInstance.conversionsPut(apiCoreDtoConversionsConversion, (error, data, response) => {
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
 **apiCoreDtoConversionsConversion** | [**ApiCoreDtoConversionsConversion**](ApiCoreDtoConversionsConversion.md)| The body of the conversion | 

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

