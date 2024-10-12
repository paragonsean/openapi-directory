# ListenApiPodcastSearchDirectoryAndInsightsApi.PodcasterAPIApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePodcastById**](PodcasterAPIApi.md#deletePodcastById) | **DELETE** /podcasts/{id} | Request to delete a podcast
[**submitPodcast**](PodcasterAPIApi.md#submitPodcast) | **POST** /podcasts/submit | Submit a podcast to Listen Notes database



## deletePodcastById

> DeletePodcastResponse deletePodcastById(xListenAPIKey, id, opts)

Request to delete a podcast

Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the \&quot;status\&quot; field in the response will be \&quot;deleted\&quot;. Otherwise, the status field will be \&quot;in review\&quot;. If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcasterAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "4d3fe717742d4963a85562e9f84d8c79"; // String | Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...
let opts = {
  'reason': "the podcaster wants to delete it" // String | The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put \"testing\" here to indicate that you are testing this endpoint, so we will not actually delete the podcast.
};
apiInstance.deletePodcastById(xListenAPIKey, id, opts, (error, data, response) => {
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
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **id** | **String**| Podcast id. You can get podcast id from using other endpoints, e.g., &#x60;GET /search&#x60;, &#x60;GET /best_podcasts&#x60;... | 
 **reason** | **String**| The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put \&quot;testing\&quot; here to indicate that you are testing this endpoint, so we will not actually delete the podcast. | [optional] 

### Return type

[**DeletePodcastResponse**](DeletePodcastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## submitPodcast

> SubmitPodcastResponse submitPodcast(xListenAPIKey, rss, opts)

Submit a podcast to Listen Notes database

Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn&#39;t exist in the database, \&quot;status\&quot; in the response will be \&quot;in review\&quot;, and we&#39;ll review it within 12 hours. If the podcast exists, \&quot;status\&quot; in the response will be \&quot;found\&quot;. If this submission is rejected, \&quot;status\&quot; in the response will be \&quot;rejected\&quot;. You can use &#x60;POST /podcasts&#x60; to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the \&quot;email\&quot; parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcasterAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let rss = "rss_example"; // String | A valid podcast rss url.
let opts = {
  'email': "email_example" // String | A valid email address. If **email** is specified, then we'll notify this email address once the podcast is accepted.
};
apiInstance.submitPodcast(xListenAPIKey, rss, opts, (error, data, response) => {
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
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **rss** | **String**| A valid podcast rss url. | 
 **email** | **String**| A valid email address. If **email** is specified, then we&#39;ll notify this email address once the podcast is accepted. | [optional] 

### Return type

[**SubmitPodcastResponse**](SubmitPodcastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

