# PeelTuneInApi.HashtagApi

All URIs are relative to *http://hashtag.peel-ci.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRelatedHashtags**](HashtagApi.md#getRelatedHashtags) | **GET** /hashtag/related | Gets related hashtags for a show.
[**getTrendingShows**](HashtagApi.md#getTrendingShows) | **GET** /hashtag/trendingShows | Gets trending shows.
[**getTuneinLinks**](HashtagApi.md#getTuneinLinks) | **GET** /hashtag/tuneinlinks | Gets tunein URLs (links) from either a tweet, hashtags, @mentions, or show ID.



## getRelatedHashtags

> getRelatedHashtags(showID, opts)

Gets related hashtags for a show.

Returns any official hashtag and any hashtags which were learned within the most recent time window for the show.

### Example

```javascript
import PeelTuneInApi from 'peel_tune_in_api';

let apiInstance = new PeelTuneInApi.HashtagApi();
let showID = "showID_example"; // String | Unique ID for a show
let opts = {
  'timeWindow': "timeWindow_example" // String | Time window in seconds (default is 2 hours)
};
apiInstance.getRelatedHashtags(showID, opts, (error, data, response) => {
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
 **showID** | **String**| Unique ID for a show | 
 **timeWindow** | **String**| Time window in seconds (default is 2 hours) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTrendingShows

> getTrendingShows(opts)

Gets trending shows.

### Example

```javascript
import PeelTuneInApi from 'peel_tune_in_api';

let apiInstance = new PeelTuneInApi.HashtagApi();
let opts = {
  'limit': "limit_example", // String | Number of trending shows (default is 20)
  'timeWindow': "timeWindow_example" // String | Time window in seconds (default is 2 hours)
};
apiInstance.getTrendingShows(opts, (error, data, response) => {
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
 **limit** | **String**| Number of trending shows (default is 20) | [optional] 
 **timeWindow** | **String**| Time window in seconds (default is 2 hours) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getTuneinLinks

> getTuneinLinks(opts)

Gets tunein URLs (links) from either a tweet, hashtags, @mentions, or show ID.

Either use &lt;b&gt;tweet&lt;/b&gt;, &lt;b&gt;hashtags&lt;/b&gt;, or &lt;b&gt;showID&lt;/b&gt; as the parameter. The tunein URLs that match best are returned in order of best match.&lt;br/&gt;&lt;br/&gt;A &lt;b&gt;tweet&lt;/b&gt; in this context is shorthand for text from a social networking conversation, e.g., it could be from Facebook, Twitter, LinkedIn, etc., and be greater than 140 characters.

### Example

```javascript
import PeelTuneInApi from 'peel_tune_in_api';

let apiInstance = new PeelTuneInApi.HashtagApi();
let opts = {
  'tweet': "tweet_example", // String | Text from a social networking conversation
  'hashtags': "hashtags_example", // String | Comma separated list of hashtags and @mentions
  'showID': "showID_example" // String | Unique ID for a show
};
apiInstance.getTuneinLinks(opts, (error, data, response) => {
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
 **tweet** | **String**| Text from a social networking conversation | [optional] 
 **hashtags** | **String**| Comma separated list of hashtags and @mentions | [optional] 
 **showID** | **String**| Unique ID for a show | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

