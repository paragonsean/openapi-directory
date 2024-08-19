# AggregatorsApiService.APIV2Api

All URIs are relative to *https://api.zeno.fm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPodcast**](APIV2Api.md#createPodcast) | **POST** /api/v2/podcasts/create | 
[**createPodcastEpisode**](APIV2Api.md#createPodcastEpisode) | **POST** /api/v2/podcasts/{podcastKey}/episodes/create | 
[**deletePodcast**](APIV2Api.md#deletePodcast) | **DELETE** /api/v2/podcasts/{podcastKey} | 
[**deletePodcast1**](APIV2Api.md#deletePodcast1) | **DELETE** /api/v2/podcasts/{podcastKey}/episodes/{episodeKey} | 
[**getPartnerAggregatorStations**](APIV2Api.md#getPartnerAggregatorStations) | **GET** /api/v2/stations/list | 
[**getPodcast**](APIV2Api.md#getPodcast) | **GET** /api/v2/podcasts/{podcastKey} | 
[**getPodcastCategories**](APIV2Api.md#getPodcastCategories) | **GET** /api/v2/podcasts/categories | 
[**getPodcastCountries**](APIV2Api.md#getPodcastCountries) | **GET** /api/v2/podcasts/countries | 
[**getPodcastEpisode**](APIV2Api.md#getPodcastEpisode) | **GET** /api/v2/podcasts/{podcastKey}/episodes/{episodeKey} | 
[**getPodcastEpisodes**](APIV2Api.md#getPodcastEpisodes) | **GET** /api/v2/podcasts/{podcastKey}/episodes | 
[**getPodcastLanguages**](APIV2Api.md#getPodcastLanguages) | **GET** /api/v2/podcasts/languages | 
[**getStationCountries**](APIV2Api.md#getStationCountries) | **GET** /api/v2/stations/countries | 
[**getStationGenres**](APIV2Api.md#getStationGenres) | **GET** /api/v2/stations/genres | 
[**getStationLanguages**](APIV2Api.md#getStationLanguages) | **GET** /api/v2/stations/languages | 
[**searchPodcasts**](APIV2Api.md#searchPodcasts) | **POST** /api/v2/podcasts/search | 
[**searchStations**](APIV2Api.md#searchStations) | **POST** /api/v2/stations/search | 
[**updatePodcast**](APIV2Api.md#updatePodcast) | **PUT** /api/v2/podcasts/{podcastKey} | 
[**updatePodcastEpisode**](APIV2Api.md#updatePodcastEpisode) | **PUT** /api/v2/podcasts/{podcastKey}/episodes/{episodeKey} | 



## createPodcast

> Podcast createPodcast(fileLogo, podcast)



Create podcast

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let fileLogo = "/path/to/file"; // File | 
let podcast = new AggregatorsApiService.Podcast(); // Podcast | 
apiInstance.createPodcast(fileLogo, podcast, (error, data, response) => {
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
 **fileLogo** | **File**|  | 
 **podcast** | [**Podcast**](Podcast.md)|  | 

### Return type

[**Podcast**](Podcast.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## createPodcastEpisode

> PodcastEpisode createPodcastEpisode(podcastKey, episode, fileLogo, fileMedia)



Create podcast episode

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
let episode = new AggregatorsApiService.PodcastEpisode(); // PodcastEpisode | 
let fileLogo = "/path/to/file"; // File | 
let fileMedia = "/path/to/file"; // File | 
apiInstance.createPodcastEpisode(podcastKey, episode, fileLogo, fileMedia, (error, data, response) => {
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
 **podcastKey** | **String**|  | 
 **episode** | [**PodcastEpisode**](PodcastEpisode.md)|  | 
 **fileLogo** | **File**|  | 
 **fileMedia** | **File**|  | 

### Return type

[**PodcastEpisode**](PodcastEpisode.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## deletePodcast

> deletePodcast(podcastKey)



Delete podcast

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
apiInstance.deletePodcast(podcastKey, (error, data, response) => {
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
 **podcastKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePodcast1

> deletePodcast1(podcastKey, episodeKey)



Delete podcast episode

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
let episodeKey = "episodeKey_example"; // String | 
apiInstance.deletePodcast1(podcastKey, episodeKey, (error, data, response) => {
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
 **podcastKey** | **String**|  | 
 **episodeKey** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPartnerAggregatorStations

> StationList getPartnerAggregatorStations(opts)



List stations

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let opts = {
  'page': "'1'", // String | 
  'hitsPerPage': "'10'" // String | 
};
apiInstance.getPartnerAggregatorStations(opts, (error, data, response) => {
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
 **page** | **String**|  | [optional] [default to &#39;1&#39;]
 **hitsPerPage** | **String**|  | [optional] [default to &#39;10&#39;]

### Return type

[**StationList**](StationList.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPodcast

> Podcast getPodcast(podcastKey)



Get podcast

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
apiInstance.getPodcast(podcastKey, (error, data, response) => {
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
 **podcastKey** | **String**|  | 

### Return type

[**Podcast**](Podcast.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPodcastCategories

> [PodcastCategory] getPodcastCategories()



Get the list of Categories that can be used to filter podcasts in the search podcasts request

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
apiInstance.getPodcastCategories((error, data, response) => {
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

[**[PodcastCategory]**](PodcastCategory.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPodcastCountries

> [Country] getPodcastCountries()



Get the list of Countries that can be used to filter podcasts in the search podcasts request

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
apiInstance.getPodcastCountries((error, data, response) => {
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

[**[Country]**](Country.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPodcastEpisode

> PodcastEpisode getPodcastEpisode(podcastKey, episodeKey)



Get podcast episode

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
let episodeKey = "episodeKey_example"; // String | 
apiInstance.getPodcastEpisode(podcastKey, episodeKey, (error, data, response) => {
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
 **podcastKey** | **String**|  | 
 **episodeKey** | **String**|  | 

### Return type

[**PodcastEpisode**](PodcastEpisode.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPodcastEpisodes

> PodcastEpisodeList getPodcastEpisodes(podcastKey, opts)



Get podcast episodes

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
let opts = {
  'limit': "'10'", // String | 
  'offset': "'0'" // String | 
};
apiInstance.getPodcastEpisodes(podcastKey, opts, (error, data, response) => {
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
 **podcastKey** | **String**|  | 
 **limit** | **String**|  | [optional] [default to &#39;10&#39;]
 **offset** | **String**|  | [optional] [default to &#39;0&#39;]

### Return type

[**PodcastEpisodeList**](PodcastEpisodeList.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPodcastLanguages

> [Language] getPodcastLanguages()



Get the list of Languages that can be used to filter podcasts in the search podcasts request

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
apiInstance.getPodcastLanguages((error, data, response) => {
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

[**[Language]**](Language.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStationCountries

> [Country] getStationCountries()



Get the list of Countries that can be used to filter stations in the search stations request

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
apiInstance.getStationCountries((error, data, response) => {
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

[**[Country]**](Country.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStationGenres

> [StationGenre] getStationGenres()



Get the list of Genres that can be used to filter stations in the search stations request

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
apiInstance.getStationGenres((error, data, response) => {
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

[**[StationGenre]**](StationGenre.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStationLanguages

> [Language] getStationLanguages()



Get the list of Languages that can be used to filter stations in the search stations request

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
apiInstance.getStationLanguages((error, data, response) => {
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

[**[Language]**](Language.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## searchPodcasts

> PodcastSearchResults searchPodcasts(podcastSearchParams)



Search podcasts

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastSearchParams = new AggregatorsApiService.PodcastSearchParams(); // PodcastSearchParams | 
apiInstance.searchPodcasts(podcastSearchParams, (error, data, response) => {
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
 **podcastSearchParams** | [**PodcastSearchParams**](PodcastSearchParams.md)|  | 

### Return type

[**PodcastSearchResults**](PodcastSearchResults.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## searchStations

> StationSearchResults searchStations(stationSearchParams)



Search stations

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let stationSearchParams = new AggregatorsApiService.StationSearchParams(); // StationSearchParams | 
apiInstance.searchStations(stationSearchParams, (error, data, response) => {
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
 **stationSearchParams** | [**StationSearchParams**](StationSearchParams.md)|  | 

### Return type

[**StationSearchResults**](StationSearchResults.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## updatePodcast

> Podcast updatePodcast(podcastKey, podcast, opts)



Update podcast

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
let podcast = new AggregatorsApiService.Podcast(); // Podcast | 
let opts = {
  'fileLogo': "/path/to/file" // File | 
};
apiInstance.updatePodcast(podcastKey, podcast, opts, (error, data, response) => {
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
 **podcastKey** | **String**|  | 
 **podcast** | [**Podcast**](Podcast.md)|  | 
 **fileLogo** | **File**|  | [optional] 

### Return type

[**Podcast**](Podcast.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## updatePodcastEpisode

> PodcastEpisode updatePodcastEpisode(podcastKey, episodeKey, episode, opts)



Update podcast episode

### Example

```javascript
import AggregatorsApiService from 'aggregators_api_service';
let defaultClient = AggregatorsApiService.ApiClient.instance;
// Configure API key authorization: API_Key
let API_Key = defaultClient.authentications['API_Key'];
API_Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key.apiKeyPrefix = 'Token';

let apiInstance = new AggregatorsApiService.APIV2Api();
let podcastKey = "podcastKey_example"; // String | 
let episodeKey = "episodeKey_example"; // String | 
let episode = new AggregatorsApiService.PodcastEpisode(); // PodcastEpisode | 
let opts = {
  'fileLogo': "/path/to/file" // File | 
};
apiInstance.updatePodcastEpisode(podcastKey, episodeKey, episode, opts, (error, data, response) => {
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
 **podcastKey** | **String**|  | 
 **episodeKey** | **String**|  | 
 **episode** | [**PodcastEpisode**](PodcastEpisode.md)|  | 
 **fileLogo** | **File**|  | [optional] 

### Return type

[**PodcastEpisode**](PodcastEpisode.md)

### Authorization

[API_Key](../README.md#API_Key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*

