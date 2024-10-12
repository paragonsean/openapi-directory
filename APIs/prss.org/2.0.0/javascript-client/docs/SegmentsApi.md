# ContentDepot.SegmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2SegmentsGet**](SegmentsApi.md#apiV2SegmentsGet) | **GET** /api/v2/segments | Returns the segments matching the query parameters.
[**apiV2SegmentsIdContentGet**](SegmentsApi.md#apiV2SegmentsIdContentGet) | **GET** /api/v2/segments/{id}/content | UNDER DEVELOPMENT - Returns the audio content segment matching the given ID.
[**apiV2SegmentsIdDelete**](SegmentsApi.md#apiV2SegmentsIdDelete) | **DELETE** /api/v2/segments/{id} | Deletes the segment with the given ID.
[**apiV2SegmentsIdGet**](SegmentsApi.md#apiV2SegmentsIdGet) | **GET** /api/v2/segments/{id} | Returns the segment matching the given ID.
[**apiV2SegmentsPost**](SegmentsApi.md#apiV2SegmentsPost) | **POST** /api/v2/segments | Creates a new segment.



## apiV2SegmentsGet

> [Segment] apiV2SegmentsGet(episodeId, opts)

Returns the segments matching the query parameters.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SegmentsApi();
let episodeId = 789; // Number | The ID of the episode that owns the segment.
let opts = {
  'segmentNumber': 56, // Number | 
  'pageStart': 0, // Number | The start page of the results to return. The first item is indexed at 0.
  'pageSize': 500, // Number | The number of items to return. Must be between 0 and 500, inclusive.
  'orderById': "orderById_example" // String | The sort order of the list of segments, based on segment ID. If unspecified, the segments are returned in random order. If using paging to iterate through the results, sort order should be specified.
};
apiInstance.apiV2SegmentsGet(episodeId, opts, (error, data, response) => {
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
 **episodeId** | **Number**| The ID of the episode that owns the segment. | 
 **segmentNumber** | **Number**|  | [optional] 
 **pageStart** | **Number**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0]
 **pageSize** | **Number**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500]
 **orderById** | **String**| The sort order of the list of segments, based on segment ID. If unspecified, the segments are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] 

### Return type

[**[Segment]**](Segment.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SegmentsIdContentGet

> File apiV2SegmentsIdContentGet(id)

UNDER DEVELOPMENT - Returns the audio content segment matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SegmentsApi();
let id = 789; // Number | 
apiInstance.apiV2SegmentsIdContentGet(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**File**

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## apiV2SegmentsIdDelete

> apiV2SegmentsIdDelete(id)

Deletes the segment with the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SegmentsApi();
let id = 789; // Number | 
apiInstance.apiV2SegmentsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SegmentsIdGet

> Segment apiV2SegmentsIdGet(id)

Returns the segment matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SegmentsApi();
let id = 789; // Number | 
apiInstance.apiV2SegmentsIdGet(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**Segment**](Segment.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SegmentsPost

> Segment apiV2SegmentsPost(cdDriveUri, episodeId, segmentNumber, opts)

Creates a new segment.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SegmentsApi();
let cdDriveUri = "cdDriveUri_example"; // String | The URI to the segment content in CD Drive. Format should be 'cddrive:id:{value}' or 'cddrive://{path}'.
let episodeId = 789; // Number | The ID of the episode that owns the segment.
let segmentNumber = 56; // Number | The segment number of the segment.
let opts = {
  'inCue': "inCue_example", // String | The incue for the segment. Defaults to the program segment incue.
  'outCue': "outCue_example" // String | The outcue for the segment. Defaults to the program segment outcue.
};
apiInstance.apiV2SegmentsPost(cdDriveUri, episodeId, segmentNumber, opts, (error, data, response) => {
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
 **cdDriveUri** | **String**| The URI to the segment content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;. | 
 **episodeId** | **Number**| The ID of the episode that owns the segment. | 
 **segmentNumber** | **Number**| The segment number of the segment. | 
 **inCue** | **String**| The incue for the segment. Defaults to the program segment incue. | [optional] 
 **outCue** | **String**| The outcue for the segment. Defaults to the program segment outcue. | [optional] 

### Return type

[**Segment**](Segment.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

