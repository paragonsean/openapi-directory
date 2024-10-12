# ForemApiV1.PodcastEpisodesApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPodcastEpisodes**](PodcastEpisodesApi.md#getPodcastEpisodes) | **GET** /api/podcast_episodes | Podcast Episodes



## getPodcastEpisodes

> [PodcastEpisodeIndex] getPodcastEpisodes(opts)

Podcast Episodes

This endpoint allows the client to retrieve a list of podcast episodes.         \&quot;Podcast episodes\&quot; are episodes belonging to podcasts.         It will only return active (reachable) podcast episodes that belong to published podcasts available on the platform, ordered by descending publication date.         It supports pagination, each page will contain 30 articles by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.PodcastEpisodesApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30, // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
  'username': "codenewbie" // String | Using this parameter will retrieve episodes belonging to a specific podcast.
};
apiInstance.getPodcastEpisodes(opts, (error, data, response) => {
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
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]
 **username** | **String**| Using this parameter will retrieve episodes belonging to a specific podcast. | [optional] 

### Return type

[**[PodcastEpisodeIndex]**](PodcastEpisodeIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

