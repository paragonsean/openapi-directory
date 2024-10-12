# Channel4Api.MetadataresourcesApi

All URIs are relative to *http://channel4.com/pmlsd*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brandEPGAtomFeed**](MetadataresourcesApi.md#brandEPGAtomFeed) | **GET** /{brand-web-safe-title}/epg.atom | Brand EPG Atom Feed
[**call4oDFeed**](MetadataresourcesApi.md#call4oDFeed) | **GET** /{brand-web-safe-title}/4od.atom | 4oD Feed
[**clipDetailAtomFeed**](MetadataresourcesApi.md#clipDetailAtomFeed) | **GET** /{brand-web-safe-title}/videos/{clip-asset-id}.atom | Clip Detail Atom Feed
[**clipsLandingFeedBrandSeriesAndEpisodeLevels**](MetadataresourcesApi.md#clipsLandingFeedBrandSeriesAndEpisodeLevels) | **GET** /{brand-web-safe-title}/videos/all.atom | Clips Landing Feed Brand Series and Episode Levels
[**clipsLandingFeedBrandSeriesAndEpisodeLevels2**](MetadataresourcesApi.md#clipsLandingFeedBrandSeriesAndEpisodeLevels2) | **GET** /{brand-web-safe-title}/videos/series-{series_number}.atom | Clips Landing Feed Brand Series and Episode Levels(2)
[**clipsLandingFeedBrandSeriesAndEpisodeLevels3**](MetadataresourcesApi.md#clipsLandingFeedBrandSeriesAndEpisodeLevels3) | **GET** /{brand-web-safe-title}/videos/series-{series_number}/episode-{episode_number}.atom | Clips Landing Feed Brand Series and Episode Levels(3)
[**comingSoonFeed**](MetadataresourcesApi.md#comingSoonFeed) | **GET** /coming-soon.atom | Coming Soon feed
[**comingSoonFeed2**](MetadataresourcesApi.md#comingSoonFeed2) | **GET** /coming-soon/{category}.atom | Coming Soon feed(2)
[**episodeGuideFeedEpisodeDetail**](MetadataresourcesApi.md#episodeGuideFeedEpisodeDetail) | **GET** /{brand-web-safe-title}/episode-guide/series-{series_number}/episode-{episode_number}.atom | Episode Guide Feed Episode Detail
[**episodeGuideFeedSeriesDetail**](MetadataresourcesApi.md#episodeGuideFeedSeriesDetail) | **GET** /{brand-web-safe-title}/episode-guide/series-{series_number}.atom | Episode Guide Feed Series Detail
[**episodeGuideFeedSeriesLanding**](MetadataresourcesApi.md#episodeGuideFeedSeriesLanding) | **GET** /{brand-web-safe-title}/episode-guide.atom | Episode Guide Feed Series Landing
[**hubFeed**](MetadataresourcesApi.md#hubFeed) | **GET** /{brand-web-safe-title}.atom | Hub Feed
[**programmeFeed**](MetadataresourcesApi.md#programmeFeed) | **GET** /programme/{programme-id}.atom | Programme Feed



## brandEPGAtomFeed

> Atom brandEPGAtomFeed(brandWebSafeTitle, opts)

Brand EPG Atom Feed

This feed contains metadata about upcoming electronic programme guide (EPG)    information for a brand. The entry details upcoming transmission slots for    this brand.    http://api.channel4.com/pmlsd/brand-web-safe-title/epg.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-simpsons/epg.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of the programme for which you seek EPG information
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.brandEPGAtomFeed(brandWebSafeTitle, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| Title of the programme for which you seek EPG information | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## call4oDFeed

> Atom call4oDFeed(brandWebSafeTitle, opts)

4oD Feed

A feed containing all available on-demand long-form content for a specified    brand. The entries for the 4oD feed contain references to each long-form    asset for a brand, ordered by series number and episode number.    http://api.channel4.com/pmlsd/[brand-web-safe-title]/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek on-demand content
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.call4oDFeed(brandWebSafeTitle, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| The title of the programme for which you seek on-demand content | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## clipDetailAtomFeed

> Atom clipDetailAtomFeed(brandWebSafeTitle, clipAssetId, opts)

Clip Detail Atom Feed

A feed containing metadata about a single short-form video (clip).    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/clip-asset-id.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/videos/TCGS_CLIP_0000001015.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of the brand for which you seek a clip
let clipAssetId = "clipAssetId_example"; // String | Asset id for this clip
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.clipDetailAtomFeed(brandWebSafeTitle, clipAssetId, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| Title of the brand for which you seek a clip | 
 **clipAssetId** | **String**| Asset id for this clip | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## clipsLandingFeedBrandSeriesAndEpisodeLevels

> Atom clipsLandingFeedBrandSeriesAndEpisodeLevels(brandWebSafeTitle, opts)

Clips Landing Feed Brand Series and Episode Levels

A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/all.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of brand to which clips belong
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.clipsLandingFeedBrandSeriesAndEpisodeLevels(brandWebSafeTitle, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| Title of brand to which clips belong | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## clipsLandingFeedBrandSeriesAndEpisodeLevels2

> Atom clipsLandingFeedBrandSeriesAndEpisodeLevels2(brandWebSafeTitle, seriesNumber, opts)

Clips Landing Feed Brand Series and Episode Levels(2)

A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/series-series_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of brand to which clips belong
let seriesNumber = "seriesNumber_example"; // String | Unique identifier of series to which clips belong
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.clipsLandingFeedBrandSeriesAndEpisodeLevels2(brandWebSafeTitle, seriesNumber, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| Title of brand to which clips belong | 
 **seriesNumber** | **String**| Unique identifier of series to which clips belong | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## clipsLandingFeedBrandSeriesAndEpisodeLevels3

> Atom clipsLandingFeedBrandSeriesAndEpisodeLevels3(brandWebSafeTitle, seriesNumber, episodeNumber, opts)

Clips Landing Feed Brand Series and Episode Levels(3)

A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/series-series_number/episode-episode_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of brand to which clips belong
let seriesNumber = "seriesNumber_example"; // String | Unique identifier of series to which clips belong
let episodeNumber = "episodeNumber_example"; // String | Unique identifier of episode to which clips belong
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.clipsLandingFeedBrandSeriesAndEpisodeLevels3(brandWebSafeTitle, seriesNumber, episodeNumber, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| Title of brand to which clips belong | 
 **seriesNumber** | **String**| Unique identifier of series to which clips belong | 
 **episodeNumber** | **String**| Unique identifier of episode to which clips belong | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## comingSoonFeed

> Atom comingSoonFeed(opts)

Coming Soon feed

Coming Soon feed display a list of episodes coming soon to linear TV so that    I can promote new Channel 4 content.    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.comingSoonFeed(opts, (error, data, response) => {
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
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## comingSoonFeed2

> Atom comingSoonFeed2(category, opts)

Coming Soon feed(2)

Coming Soon feed display a list of episodes coming soon to linear TV so that    I can promote new Channel 4 content.    http://api.channel4.com/pmlsd/coming-soon/[category].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let category = "category_example"; // String | The category websafe_title to filter the coming soon programmes on TV.
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.comingSoonFeed2(category, opts, (error, data, response) => {
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
 **category** | **String**| The category websafe_title to filter the coming soon programmes on TV. | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## episodeGuideFeedEpisodeDetail

> Atom episodeGuideFeedEpisodeDetail(brandWebSafeTitle, seriesNumber, episodeNumber, opts)

Episode Guide Feed Episode Detail

A feed containing metadata about a specified episode. (This feed does not    contain any entries and only contains a feed element regarding this    episode.)    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide/series-series_number/episode-episode_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/episode-guide/series-1/episode-1.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of the brand to which the episode belongs
let seriesNumber = "seriesNumber_example"; // String | Unique enumerated identifier of the series within its brand to which the episode belongs
let episodeNumber = "episodeNumber_example"; // String | Unique enumerated identifier of the episode within its series
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.episodeGuideFeedEpisodeDetail(brandWebSafeTitle, seriesNumber, episodeNumber, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| Title of the brand to which the episode belongs | 
 **seriesNumber** | **String**| Unique enumerated identifier of the series within its brand to which the episode belongs | 
 **episodeNumber** | **String**| Unique enumerated identifier of the episode within its series | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## episodeGuideFeedSeriesDetail

> Atom episodeGuideFeedSeriesDetail(brandWebSafeTitle, seriesNumber, opts)

Episode Guide Feed Series Detail

A feed containing metadata about all the episodes for a specific series. The    entries in this feed contain references to each of the episodes (where    metadata has been published), with some convenient links.    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide/series-series_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/chelmsford-123/episode-guide/series-1.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek series-related information
let seriesNumber = "seriesNumber_example"; // String | Unique enumerated identifier of the series within its brand
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.episodeGuideFeedSeriesDetail(brandWebSafeTitle, seriesNumber, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| The title of the programme for which you seek series-related information | 
 **seriesNumber** | **String**| Unique enumerated identifier of the series within its brand | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## episodeGuideFeedSeriesLanding

> Atom episodeGuideFeedSeriesLanding(brandWebSafeTitle, opts)

Episode Guide Feed Series Landing

A feed containing metadata about all series for a specified brand. The    entries in this feed contain references to each of the series (where    metadata has been published), with some convenient links.    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/father-ted/episode-guide.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek episode-guide information
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.episodeGuideFeedSeriesLanding(brandWebSafeTitle, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| The title of the programme for which you seek episode-guide information | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## hubFeed

> Atom hubFeed(brandWebSafeTitle, opts)

Hub Feed

The basis for all brand information    http://api.channel4.com/pmlsd/brand-web-safe-title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek associated data
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.hubFeed(brandWebSafeTitle, opts, (error, data, response) => {
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
 **brandWebSafeTitle** | **String**| The title of the programme for which you seek associated data | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## programmeFeed

> Atom programmeFeed(programmeId, opts)

Programme Feed

A feed containing all long-form content currently or previously available    for a specified Programme Id. The entries for the Programme feed contain    references to long-form assets for each platform.    http://api.channel4.com/pmlsd/programme/[programme-id].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/programme/33881-001/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example

```javascript
import Channel4Api from 'channel_4_api';
let defaultClient = Channel4Api.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new Channel4Api.MetadataresourcesApi();
let programmeId = "programmeId_example"; // String | The websafe programme identifier for the episode for which you seek on-demand content
let opts = {
  'platform': "platform_example" // String | The platform to use for the query. Alias 'client'.
};
apiInstance.programmeFeed(programmeId, opts, (error, data, response) => {
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
 **programmeId** | **String**| The websafe programme identifier for the episode for which you seek on-demand content | 
 **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] 

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml

