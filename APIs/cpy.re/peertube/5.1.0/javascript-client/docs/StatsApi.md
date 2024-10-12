# PeerTube.StatsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1MetricsPlaybackPost**](StatsApi.md#apiV1MetricsPlaybackPost) | **POST** /api/v1/metrics/playback | Create playback metrics
[**getInstanceStats**](StatsApi.md#getInstanceStats) | **GET** /api/v1/server/stats | Get instance stats



## apiV1MetricsPlaybackPost

> apiV1MetricsPlaybackPost(opts)

Create playback metrics

These metrics are exposed by OpenTelemetry metrics exporter if enabled.

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.StatsApi();
let opts = {
  'playbackMetricCreate': new PeerTube.PlaybackMetricCreate() // PlaybackMetricCreate | 
};
apiInstance.apiV1MetricsPlaybackPost(opts, (error, data, response) => {
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
 **playbackMetricCreate** | [**PlaybackMetricCreate**](PlaybackMetricCreate.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getInstanceStats

> ServerStats getInstanceStats()

Get instance stats

Get instance public statistics. This endpoint is cached.

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.StatsApi();
apiInstance.getInstanceStats((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerStats**](ServerStats.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

