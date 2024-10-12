# RadioMusicServices.PodcastsApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPodcastByPid**](PodcastsApi.md#getPodcastByPid) | **GET** /podcasts/{pid} | Podcast
[**getPodcastEpisodes**](PodcastsApi.md#getPodcastEpisodes) | **GET** /podcasts/{pid}/episodes | Podcast Episodes
[**getPodcasts**](PodcastsApi.md#getPodcasts) | **GET** /podcasts | All Podcasts
[**getPodcastsFeatured**](PodcastsApi.md#getPodcastsFeatured) | **GET** /podcasts/featured | Featured Podcasts



## getPodcastByPid

> PodcastsResponse getPodcastByPid(xAPIKey, pid, opts)

Podcast

Retrieve data about the podcast with the supplied PID 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PodcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let pid = "pid_example"; // String | pid
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getPodcastByPid(xAPIKey, pid, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **pid** | **String**| pid | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PodcastsResponse**](PodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcastEpisodes

> PodcastEpisodesResponse getPodcastEpisodes(xAPIKey, pid, opts)

Podcast Episodes

Retrieve all episodes for a specific podcast 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PodcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let pid = "pid_example"; // String | pid
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getPodcastEpisodes(xAPIKey, pid, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **pid** | **String**| pid | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PodcastEpisodesResponse**](PodcastEpisodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcasts

> PodcastsResponse getPodcasts(xAPIKey, opts)

All Podcasts

Retrieve all Podcasts 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PodcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'sort': "sort_example", // String | Sort order for Podcasts results
  'network': "network_example", // String | Network Master Brand ID (mid)
  'networkUrlKey': "networkUrlKey_example", // String | Network URL key
  'category': "category_example", // String | Category ID
  'q': "q_example", // String | Search query String
  'coverage': "coverage_example" // String | Local, National or Regional Coverage
};
apiInstance.getPodcasts(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **sort** | **String**| Sort order for Podcasts results | [optional] 
 **network** | **String**| Network Master Brand ID (mid) | [optional] 
 **networkUrlKey** | **String**| Network URL key | [optional] 
 **category** | **String**| Category ID | [optional] 
 **q** | **String**| Search query String | [optional] 
 **coverage** | **String**| Local, National or Regional Coverage | [optional] 

### Return type

[**PodcastsResponse**](PodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcastsFeatured

> PodcastsFeaturedResponse getPodcastsFeatured(xAPIKey)

Featured Podcasts

Retrieve featured podcasts 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.PodcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
apiInstance.getPodcastsFeatured(xAPIKey, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 

### Return type

[**PodcastsFeaturedResponse**](PodcastsFeaturedResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

