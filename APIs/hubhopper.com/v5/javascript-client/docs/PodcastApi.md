# HubhopperPartnerIntegrationApiSProduction.PodcastApi

All URIs are relative to *https://apis.hubhopper.com/partner*

Method | HTTP request | Description
------------- | ------------- | -------------
[**podcastsGet**](PodcastApi.md#podcastsGet) | **GET** /podcasts | 
[**podcastsPodcastIdEpisodesGet**](PodcastApi.md#podcastsPodcastIdEpisodesGet) | **GET** /podcasts/{podcastId}/episodes | 
[**podcastsPodcastIdGet**](PodcastApi.md#podcastsPodcastIdGet) | **GET** /podcasts/{podcastId} | 



## podcastsGet

> PodcastList podcastsGet(opts)



Get the list of all podcasts.

### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.PodcastApi();
let opts = {
  'page': "page_example", // String | Provide the page number to fetch.
  'pageSize': "pageSize_example", // String | Provide the size of the page to fetch.
  'order': "order_example", // String | Order the items by 'newest' | 'random'
  'filters': "filters_example" // String | Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
};
apiInstance.podcastsGet(opts, (error, data, response) => {
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
 **page** | **String**| Provide the page number to fetch. | [optional] 
 **pageSize** | **String**| Provide the size of the page to fetch. | [optional] 
 **order** | **String**| Order the items by &#39;newest&#39; | &#39;random&#39; | [optional] 
 **filters** | **String**| Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); | [optional] 

### Return type

[**PodcastList**](PodcastList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## podcastsPodcastIdEpisodesGet

> PodcastEpisodeList podcastsPodcastIdEpisodesGet(podcastId, opts)



Get a list of all episodes under a podcast.

### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.PodcastApi();
let podcastId = "podcastId_example"; // String | Unique qualifier for a podcast.
let opts = {
  'page': "page_example", // String | Provide the page number to fetch.
  'pageSize': "pageSize_example", // String | Provide the size of the page to fetch.
  'order': "order_example", // String | Order the items by 'newest' | 'random'
  'filters': "filters_example" // String | Takes filters like 'lang' in a url encoded json.  Example: 1)Single -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson)); 2)Multiple -> &nbsp;&nbsp;&nbsp;&nbsp; var filterJson = {\"lang\":[\"en\",\"hi\"]}; &nbsp;&nbsp;&nbsp;&nbsp; var url = baseUrl+'?'+filters=enocdeURI(JSON.stringify(filterJson));
};
apiInstance.podcastsPodcastIdEpisodesGet(podcastId, opts, (error, data, response) => {
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
 **podcastId** | **String**| Unique qualifier for a podcast. | 
 **page** | **String**| Provide the page number to fetch. | [optional] 
 **pageSize** | **String**| Provide the size of the page to fetch. | [optional] 
 **order** | **String**| Order the items by &#39;newest&#39; | &#39;random&#39; | [optional] 
 **filters** | **String**| Takes filters like &#39;lang&#39; in a url encoded json.  Example: 1)Single -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); 2)Multiple -&gt; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var filterJson &#x3D; {\&quot;lang\&quot;:[\&quot;en\&quot;,\&quot;hi\&quot;]}; &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp; var url &#x3D; baseUrl+&#39;?&#39;+filters&#x3D;enocdeURI(JSON.stringify(filterJson)); | [optional] 

### Return type

[**PodcastEpisodeList**](PodcastEpisodeList.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## podcastsPodcastIdGet

> SinglePodcast podcastsPodcastIdGet(podcastId)



Get a single Podcast.

### Example

```javascript
import HubhopperPartnerIntegrationApiSProduction from 'hubhopper_partner_integration_api_s_production';
let defaultClient = HubhopperPartnerIntegrationApiSProduction.ApiClient.instance;
// Configure API key authorization: partner_id
let partner_id = defaultClient.authentications['partner_id'];
partner_id.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//partner_id.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new HubhopperPartnerIntegrationApiSProduction.PodcastApi();
let podcastId = "podcastId_example"; // String | Unique qualifier for a podcast.
apiInstance.podcastsPodcastIdGet(podcastId, (error, data, response) => {
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
 **podcastId** | **String**| Unique qualifier for a podcast. | 

### Return type

[**SinglePodcast**](SinglePodcast.md)

### Authorization

[partner_id](../README.md#partner_id), [api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

