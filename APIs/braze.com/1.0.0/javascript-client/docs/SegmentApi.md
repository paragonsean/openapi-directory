# BrazeEndpoints.SegmentApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**segmentAnalytics_0**](SegmentApi.md#segmentAnalytics_0) | **GET** /segments/data_series | Segment Analytics
[**segmentDetails_0**](SegmentApi.md#segmentDetails_0) | **GET** /segments/details | Segment Details
[**segmentList_0**](SegmentApi.md#segmentList_0) | **GET** /segments/list | Segment List



## segmentAnalytics_0

> segmentAnalytics_0(opts)

Segment Analytics

This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;size\&quot; : (int) size of the segment on that date         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.SegmentApi();
let opts = {
  'segmentId': "{{segment_identifier}}", // String | (Required) String  Segment API identifier.
  'length': "14", // String | (Required) Integer  Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive.
  'endingAt': "2018-06-27T23:59:59-5:00" // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request.
};
apiInstance.segmentAnalytics_0(opts, (error, data, response) => {
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
 **segmentId** | **String**| (Required) String  Segment API identifier. | [optional] 
 **length** | **String**| (Required) Integer  Max number of days before &#x60;ending_at&#x60; to include in the returned series - must be between 1 and 100 inclusive. | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## segmentDetails_0

> segmentDetails_0(opts)

Segment Details

This endpoint allows you to retrieve relevant information on the segment, which can be identified by the &#x60;segment_id&#x60;.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {       \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,       \&quot;created_at\&quot; : (string) date created as ISO 8601 date,       \&quot;updated_at\&quot; : (string) date last updated as ISO 8601 date,       \&quot;name\&quot; : (string) segment name,       \&quot;description\&quot; : (string) human-readable description of filters,       \&quot;text_description\&quot; : (string) segment description,        \&quot;tags\&quot; : (array) tag names associated with the segment } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.SegmentApi();
let opts = {
  'segmentId': "{{segment_identifier}}" // String | (Required) String  Segment API identifier
};
apiInstance.segmentDetails_0(opts, (error, data, response) => {
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
 **segmentId** | **String**| (Required) String  Segment API identifier | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## segmentList_0

> segmentList_0(opts)

Segment List

This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;segments\&quot; : [         {             \&quot;id\&quot; : (string) Segment API Identifier,             \&quot;name\&quot; : (string) segment name,             \&quot;analytics_tracking_enabled\&quot; : (boolean) whether the segment has analytics tracking enabled,             \&quot;tags\&quot; : (array) tag names associated with the segment         },         ...     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.SegmentApi();
let opts = {
  'page': "1", // String | (Optional) Integer  The page of segments to return, defaults to 0 (returns the first set of up to 100)
  'sortDirection': "desc" // String | (Optional) String  Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest.
};
apiInstance.segmentList_0(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of segments to return, defaults to 0 (returns the first set of up to 100) | [optional] 
 **sortDirection** | **String**| (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If &#x60;sort_direction&#x60; is not included, the default order is oldest to newest. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

