# MuxApi.VideoViewsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVideoView**](VideoViewsApi.md#getVideoView) | **GET** /data/v1/video-views/{VIDEO_VIEW_ID} | Get a Video View
[**listVideoViews**](VideoViewsApi.md#listVideoViews) | **GET** /data/v1/video-views | List Video Views



## getVideoView

> VideoViewResponse getVideoView(VIDEO_VIEW_ID)

Get a Video View

Returns the details of a video view.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.VideoViewsApi();
let VIDEO_VIEW_ID = "abcd1234"; // String | ID of the Video View
apiInstance.getVideoView(VIDEO_VIEW_ID, (error, data, response) => {
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
 **VIDEO_VIEW_ID** | **String**| ID of the Video View | 

### Return type

[**VideoViewResponse**](VideoViewResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVideoViews

> ListVideoViewsResponse listVideoViews(opts)

List Video Views

Returns a list of video views which match the filters and have a &#x60;view_end&#x60; within the specified timeframe.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.VideoViewsApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'viewerId': "viewerId_example", // String | Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux.
  'errorId': 56, // Number | Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error.
  'orderDirection': "orderDirection_example", // String | Sort order.
  'filters': ["null"], // [String] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
  'timeframe': ["null"] // [String] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days` 
};
apiInstance.listVideoViews(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **viewerId** | **String**| Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux. | [optional] 
 **errorId** | **Number**| Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error. | [optional] 
 **orderDirection** | **String**| Sort order. | [optional] 
 **filters** | [**[String]**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **timeframe** | [**[String]**](String.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListVideoViewsResponse**](ListVideoViewsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

