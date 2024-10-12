# ListenApiPodcastSearchDirectoryAndInsightsApi.DefaultApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**podcastDeletedPost**](DefaultApi.md#podcastDeletedPost) | **POST** /podcastDeleted | 
[**podcastsSubmitAcceptedPost**](DefaultApi.md#podcastsSubmitAcceptedPost) | **POST** /podcastsSubmitAccepted | 
[**podcastsSubmitRejectedPost**](DefaultApi.md#podcastsSubmitRejectedPost) | **POST** /podcastsSubmitRejected | 



## podcastDeletedPost

> podcastDeletedPost(opts)



### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DefaultApi();
let opts = {
  'podcastMinimumRss': new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastMinimumRss() // PodcastMinimumRss | Triggered by your request to DELETE /podcasts/{id}, if the podcast is actually deleted.
};
apiInstance.podcastDeletedPost(opts, (error, data, response) => {
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
 **podcastMinimumRss** | [**PodcastMinimumRss**](PodcastMinimumRss.md)| Triggered by your request to DELETE /podcasts/{id}, if the podcast is actually deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## podcastsSubmitAcceptedPost

> podcastsSubmitAcceptedPost(opts)



### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DefaultApi();
let opts = {
  'podcastMinimumRss': new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastMinimumRss() // PodcastMinimumRss | Triggered by your request to POST /podcasts/submit, if the podcast submission is accepted.
};
apiInstance.podcastsSubmitAcceptedPost(opts, (error, data, response) => {
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
 **podcastMinimumRss** | [**PodcastMinimumRss**](PodcastMinimumRss.md)| Triggered by your request to POST /podcasts/submit, if the podcast submission is accepted. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## podcastsSubmitRejectedPost

> podcastsSubmitRejectedPost(opts)



### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DefaultApi();
let opts = {
  'UNKNOWN_BASE_TYPE': new ListenApiPodcastSearchDirectoryAndInsightsApi.UNKNOWN_BASE_TYPE() // UNKNOWN_BASE_TYPE | Triggered by your request to POST /podcasts/submit, if the podcast submission is rejected.
};
apiInstance.podcastsSubmitRejectedPost(opts, (error, data, response) => {
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
 **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Triggered by your request to POST /podcasts/submit, if the podcast submission is rejected. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

