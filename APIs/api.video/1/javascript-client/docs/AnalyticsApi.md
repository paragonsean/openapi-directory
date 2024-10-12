# ApiVideo.AnalyticsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETAnalyticsLiveStreamsLiveStreamId**](AnalyticsApi.md#gETAnalyticsLiveStreamsLiveStreamId) | **GET** /analytics/live-streams/{liveStreamId} | List live stream player sessions
[**gETAnalyticsSessionsSessionIdEvents**](AnalyticsApi.md#gETAnalyticsSessionsSessionIdEvents) | **GET** /analytics/sessions/{sessionId}/events | List player session events
[**gETAnalyticsVideosVideoId**](AnalyticsApi.md#gETAnalyticsVideosVideoId) | **GET** /analytics/videos/{videoId} | List video player sessions



## gETAnalyticsLiveStreamsLiveStreamId

> RawStatisticsListLiveStreamAnalyticsResponse gETAnalyticsLiveStreamsLiveStreamId(liveStreamId, opts)

List live stream player sessions

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.AnalyticsApi();
let liveStreamId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the live stream you want to retrieve analytics for.
let opts = {
  'period': "2019-01-01", // String | Period must have one of the following formats:  - For a day : \"2018-01-01\", - For a week: \"2018-W01\",  - For a month: \"2018-01\" - For a year: \"2018\" For a range period:  -  Date range: \"2018-01-01/2018-01-15\" 
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.gETAnalyticsLiveStreamsLiveStreamId(liveStreamId, opts, (error, data, response) => {
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
 **liveStreamId** | **String**| The unique identifier for the live stream you want to retrieve analytics for. | 
 **period** | **String**| Period must have one of the following formats:  - For a day : \&quot;2018-01-01\&quot;, - For a week: \&quot;2018-W01\&quot;,  - For a month: \&quot;2018-01\&quot; - For a year: \&quot;2018\&quot; For a range period:  -  Date range: \&quot;2018-01-01/2018-01-15\&quot;  | [optional] 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**RawStatisticsListLiveStreamAnalyticsResponse**](RawStatisticsListLiveStreamAnalyticsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETAnalyticsSessionsSessionIdEvents

> RawStatisticsListPlayerSessionEventsResponse gETAnalyticsSessionsSessionIdEvents(sessionId, opts)

List player session events

Useful to track and measure video&#39;s engagement.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.AnalyticsApi();
let sessionId = "psEmFwGQUAXR2lFHj5nDOpy"; // String | A unique identifier you can use to reference and track a session with.
let opts = {
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.gETAnalyticsSessionsSessionIdEvents(sessionId, opts, (error, data, response) => {
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
 **sessionId** | **String**| A unique identifier you can use to reference and track a session with. | 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**RawStatisticsListPlayerSessionEventsResponse**](RawStatisticsListPlayerSessionEventsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETAnalyticsVideosVideoId

> RawStatisticsListSessionsResponse gETAnalyticsVideosVideoId(videoId, opts)

List video player sessions

Retrieve all available user sessions for a specific video. Tutorials that use the [analytics endpoint](https://api.video/blog/endpoints/analytics).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.AnalyticsApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to retrieve session information for.
let opts = {
  'period': "period_example", // String | Period must have one of the following formats:  - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018 For a range period:  -  Date range: 2018-01-01/2018-01-15 
  'metadata': ["null"], // [String] | Metadata and [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) filter. Send an array of key value pairs you want to filter sessios with.
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.gETAnalyticsVideosVideoId(videoId, opts, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to retrieve session information for. | 
 **period** | **String**| Period must have one of the following formats:  - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018 For a range period:  -  Date range: 2018-01-01/2018-01-15  | [optional] 
 **metadata** | [**[String]**](String.md)| Metadata and [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) filter. Send an array of key value pairs you want to filter sessios with. | [optional] 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**RawStatisticsListSessionsResponse**](RawStatisticsListSessionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

