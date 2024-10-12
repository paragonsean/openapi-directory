# ListenApiPodcastSearchDirectoryAndInsightsApi.InsightsAPIApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPodcastAudience**](InsightsAPIApi.md#getPodcastAudience) | **GET** /podcasts/{id}/audience | Fetch audience demographics for a podcast
[**getPodcastsByDomainName**](InsightsAPIApi.md#getPodcastsByDomainName) | **GET** /podcasts/domains/{domain_name} | Fetch podcasts by a publisher&#39;s domain name



## getPodcastAudience

> PodcastAudienceResponse getPodcastAudience(xListenAPIKey, id)

Fetch audience demographics for a podcast

Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.InsightsAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "25212ac3c53240a880dd5032e547047b"; // String | Podcast id.
apiInstance.getPodcastAudience(xListenAPIKey, id, (error, data, response) => {
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
 **id** | **String**| Podcast id. | 

### Return type

[**PodcastAudienceResponse**](PodcastAudienceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcastsByDomainName

> PodcastDomainResponse getPodcastsByDomainName(xListenAPIKey, domainName, opts)

Fetch podcasts by a publisher&#39;s domain name

Fetch podcasts by a publisher&#39;s domain name, e.g., nytimes.com, wondery.com, npr.org... Each request will return up to 10 podcasts. You can use the &#x60;page&#x60; parameter to paginate. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.InsightsAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let domainName = "nytimes.com"; // String | A publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...
let opts = {
  'page': 1 // Number | Page number of the podcasts from this domain name
};
apiInstance.getPodcastsByDomainName(xListenAPIKey, domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| A publisher&#39;s domain name, e.g., nytimes.com, wondery.com, npr.org... | 
 **page** | **Number**| Page number of the podcasts from this domain name | [optional] [default to 1]

### Return type

[**PodcastDomainResponse**](PodcastDomainResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

