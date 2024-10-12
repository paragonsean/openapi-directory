# PeerTube.VideoStatsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1VideosIdStatsOverallGet**](VideoStatsApi.md#apiV1VideosIdStatsOverallGet) | **GET** /api/v1/videos/{id}/stats/overall | Get overall stats of a video
[**apiV1VideosIdStatsRetentionGet**](VideoStatsApi.md#apiV1VideosIdStatsRetentionGet) | **GET** /api/v1/videos/{id}/stats/retention | Get retention stats of a video
[**apiV1VideosIdStatsTimeseriesMetricGet**](VideoStatsApi.md#apiV1VideosIdStatsTimeseriesMetricGet) | **GET** /api/v1/videos/{id}/stats/timeseries/{metric} | Get timeserie stats of a video



## apiV1VideosIdStatsOverallGet

> VideoStatsOverall apiV1VideosIdStatsOverallGet(id, opts)

Get overall stats of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoStatsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter stats by start date
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | Filter stats by end date
};
apiInstance.apiV1VideosIdStatsOverallGet(id, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **startDate** | **Date**| Filter stats by start date | [optional] 
 **endDate** | **Date**| Filter stats by end date | [optional] 

### Return type

[**VideoStatsOverall**](VideoStatsOverall.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideosIdStatsRetentionGet

> VideoStatsRetention apiV1VideosIdStatsRetentionGet(id)

Get retention stats of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoStatsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.apiV1VideosIdStatsRetentionGet(id, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**VideoStatsRetention**](VideoStatsRetention.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VideosIdStatsTimeseriesMetricGet

> VideoStatsTimeserie apiV1VideosIdStatsTimeseriesMetricGet(id, metric, opts)

Get timeserie stats of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoStatsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let metric = "metric_example"; // String | The metric to get
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter stats by start date
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | Filter stats by end date
};
apiInstance.apiV1VideosIdStatsTimeseriesMetricGet(id, metric, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **metric** | **String**| The metric to get | 
 **startDate** | **Date**| Filter stats by start date | [optional] 
 **endDate** | **Date**| Filter stats by end date | [optional] 

### Return type

[**VideoStatsTimeserie**](VideoStatsTimeserie.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

