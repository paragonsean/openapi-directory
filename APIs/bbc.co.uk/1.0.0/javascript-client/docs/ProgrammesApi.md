# RadioMusicServices.ProgrammesApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPopularEpisodesClips**](ProgrammesApi.md#getPopularEpisodesClips) | **GET** /radio/popular | Popular Episodes &amp; Clips
[**getRadioProgrammes**](ProgrammesApi.md#getRadioProgrammes) | **GET** /radio/programmes | Radio programmes
[**getRadioProgrammesByPid**](ProgrammesApi.md#getRadioProgrammesByPid) | **GET** /radio/programmes/{pid} | Available radio programme by Pid
[**getRecommendations**](ProgrammesApi.md#getRecommendations) | **GET** /my/programmes/recommendations | Recommended Programmes



## getPopularEpisodesClips

> PopularResponse getPopularEpisodesClips(xAPIKey, opts)

Popular Episodes &amp; Clips

Retrieve Popular Episodes &amp; Clips 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.ProgrammesApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'type': "type_example", // String | Programme type required. Accepts comma separated values
  'distinct': "distinct_example", // String | Filter by deduplication rule. E.g. 'tleo' returns programmes with distinct top level episode objects
  'network': "network_example", // String | Filter by network master brand ID (mid). Accepts comma separated values
  'networkUrlKey': "networkUrlKey_example", // String | Filter by network URL key. Accepts comma separated values
  'category': "category_example", // String | Filter by category. Accepts comma separated values
  'format': "format_example", // String | Filter by format. Accepts comma separated values
  'group': "group_example", // String | Filter by group. Accepts comma separated values
  'mediaType': "mediaType_example", // String | Filter by programme media type. Accepts comma separated values
  'container': "container_example", // String | Filter by container. Accepts any pid e.g. brand,series,episode
  'mediaSet': [null], // [Object] | Filter by media set name. Accepts comma separated combinations of the following: pc,mobile-download,android-download-high,apple-ios-download-high,mobile-cellular-main,mobile-phone-main,iptv-all
  'q': "q_example" // String | Search query String
};
apiInstance.getPopularEpisodesClips(xAPIKey, opts, (error, data, response) => {
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
 **type** | **String**| Programme type required. Accepts comma separated values | [optional] 
 **distinct** | **String**| Filter by deduplication rule. E.g. &#39;tleo&#39; returns programmes with distinct top level episode objects | [optional] 
 **network** | **String**| Filter by network master brand ID (mid). Accepts comma separated values | [optional] 
 **networkUrlKey** | **String**| Filter by network URL key. Accepts comma separated values | [optional] 
 **category** | **String**| Filter by category. Accepts comma separated values | [optional] 
 **format** | **String**| Filter by format. Accepts comma separated values | [optional] 
 **group** | **String**| Filter by group. Accepts comma separated values | [optional] 
 **mediaType** | **String**| Filter by programme media type. Accepts comma separated values | [optional] 
 **container** | **String**| Filter by container. Accepts any pid e.g. brand,series,episode | [optional] 
 **mediaSet** | [**[Object]**](Object.md)| Filter by media set name. Accepts comma separated combinations of the following: pc,mobile-download,android-download-high,apple-ios-download-high,mobile-cellular-main,mobile-phone-main,iptv-all | [optional] 
 **q** | **String**| Search query String | [optional] 

### Return type

[**PopularResponse**](PopularResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRadioProgrammes

> ProgrammesResponse getRadioProgrammes(xAPIKey, opts)

Radio programmes

Provides a paginated list of programmes by PID (brand, series, episode and clip). Accepts various filters and sorting methods.  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining results as an array of Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.ProgrammesApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'kind': "kind_example", // String | Filter by provided query. E.g. 'tleo' returns top level objects, ie. brands, orphaned series, and orphaned episodes
  'network': "network_example", // String | Filter by network master brand ID (mid). Accepts comma separated values
  'networkUrlKey': "networkUrlKey_example", // String | Filter by network URL key. Accepts comma separated values
  'category': "category_example", // String | Filter by category id. Accepts comma separated values. See /category endpoint below for the type of response provided
  'sort': "sort_example", // String | Sort by provided query. E.g. 'title' sorts in ascending order, and -title sorts in descending order
  'container': "container_example", // String | Filter by container. Accepts any brand or series pid
  'type': "type_example" // String | Filter by programme type. Accepts comma separated values
};
apiInstance.getRadioProgrammes(xAPIKey, opts, (error, data, response) => {
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
 **kind** | **String**| Filter by provided query. E.g. &#39;tleo&#39; returns top level objects, ie. brands, orphaned series, and orphaned episodes | [optional] 
 **network** | **String**| Filter by network master brand ID (mid). Accepts comma separated values | [optional] 
 **networkUrlKey** | **String**| Filter by network URL key. Accepts comma separated values | [optional] 
 **category** | **String**| Filter by category id. Accepts comma separated values. See /category endpoint below for the type of response provided | [optional] 
 **sort** | **String**| Sort by provided query. E.g. &#39;title&#39; sorts in ascending order, and -title sorts in descending order | [optional] 
 **container** | **String**| Filter by container. Accepts any brand or series pid | [optional] 
 **type** | **String**| Filter by programme type. Accepts comma separated values | [optional] 

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRadioProgrammesByPid

> ProgrammesResponse getRadioProgrammesByPid(xAPIKey, pid)

Available radio programme by Pid

Find programmes by PID (brand, series, episode and clip)  N.B.  Swagger schemas cannot currently handle multiple combinations of object in an array i.e. a mix of Episode and Clip Summaries so we are defining results as an array of Programme Summary here.  This will be resolved in V3 with full support for  anyOf https://www.openapis.org/blog/2017/01/24/a-new-year-a-new-specification 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.ProgrammesApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let pid = "pid_example"; // String | pid
apiInstance.getRadioProgrammesByPid(xAPIKey, pid, (error, data, response) => {
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

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecommendations

> ProgrammesResponse getRecommendations(authorization, xAPIKey, rights, opts)

Recommended Programmes

Recommended Programmes from the Audience Platforms&#39; Recomendations Service 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.ProgrammesApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let rights = "rights_example"; // String | Only return available results for the web/mobile.
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getRecommendations(authorization, xAPIKey, rights, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **rights** | **String**| Only return available results for the web/mobile. | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**ProgrammesResponse**](ProgrammesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

