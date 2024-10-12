# BbcIPlayerBusinessLayer.EpisodesApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getClips**](EpisodesApi.md#getClips) | **GET** /clips/{pid} | Get Clips
[**getEpisodesByCategory**](EpisodesApi.md#getEpisodesByCategory) | **GET** /categories/{category}/episodes | List all the episodes for a category.
[**getEpisodesByGroup**](EpisodesApi.md#getEpisodesByGroup) | **GET** /groups/{pid}/episodes | Get episodes by group, brand or series
[**getEpisodesByParentPID**](EpisodesApi.md#getEpisodesByParentPID) | **GET** /programmes/{pid}/episodes | Child episodes for a given programme pid.
[**getOnwardJourney**](EpisodesApi.md#getOnwardJourney) | **GET** /episodes/{pid}/next | Get Onward Journey
[**getPostRolls**](EpisodesApi.md#getPostRolls) | **GET** /episodes/{pid}/postrolls | Get Follow-ups (post-rolls)
[**getProgrammeByPID**](EpisodesApi.md#getProgrammeByPID) | **GET** /episodes/{pid} | Episode for a given pid.
[**getProgrammeRecommendations**](EpisodesApi.md#getProgrammeRecommendations) | **GET** /episodes/{pid}/recommendations | Get programme recommendations
[**getProgrammesPopular**](EpisodesApi.md#getProgrammesPopular) | **GET** /groups/popular/episodes | Get programmes popular
[**getTrailersPreRolls**](EpisodesApi.md#getTrailersPreRolls) | **GET** /episodes/{pid}/prerolls | Get Trailers (pre-rolls)



## getClips

> Object getClips(pid, rights, availability)

Get Clips

Get Clips

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.getClips(pid, rights, availability, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodesByCategory

> Object getEpisodesByCategory(category, lang, rights, availability, page, perPage, opts)

List all the episodes for a category.

Get the list of all the episodes for a given category in TV &amp; iPlayer.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let category = "category_example"; // String | The category identifier to return results from.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
let opts = {
  'sort': "sort_example" // String | The sort order of the results.
};
apiInstance.getEpisodesByCategory(category, lang, rights, availability, page, perPage, opts, (error, data, response) => {
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
 **category** | **String**| The category identifier to return results from. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 
 **sort** | **String**| The sort order of the results. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodesByGroup

> Object getEpisodesByGroup(pid, rights, page, perPage, initialChildCount, sort, sortDirection, availability, opts)

Get episodes by group, brand or series

Get episodes by group, brand or series

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
let initialChildCount = 4; // Number | The depth to return child entities.
let sort = "sort_example"; // String | The sort order of the results.
let sortDirection = "sortDirection_example"; // String | Whether to sort ascending or descending
let availability = "'available'"; // String | Whether to return all, or available programmes
let opts = {
  'mixin': ["null"] // [String] | Request additional data in the output
};
apiInstance.getEpisodesByGroup(pid, rights, page, perPage, initialChildCount, sort, sortDirection, availability, opts, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 
 **initialChildCount** | **Number**| The depth to return child entities. | [default to 4]
 **sort** | **String**| The sort order of the results. | 
 **sortDirection** | **String**| Whether to sort ascending or descending | 
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodesByParentPID

> Object getEpisodesByParentPID(pid, rights, availability, initialChildCount)

Child episodes for a given programme pid.

Get the child episodes belonging to a given programme identifier.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let initialChildCount = 4; // Number | The depth to return child entities.
apiInstance.getEpisodesByParentPID(pid, rights, availability, initialChildCount, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **initialChildCount** | **Number**| The depth to return child entities. | [default to 4]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOnwardJourney

> Object getOnwardJourney(pid, rights, availability)

Get Onward Journey

Get Onward Journey (next programme)

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.getOnwardJourney(pid, rights, availability, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPostRolls

> Object getPostRolls(pid, rights, availability)

Get Follow-ups (post-rolls)

Get Follow-ups (post-rolls)

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.getPostRolls(pid, rights, availability, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammeByPID

> Object getProgrammeByPID(pid, rights, availability, opts)

Episode for a given pid.

Get the episode for a given episode identifier.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let opts = {
  'mixin': ["null"] // [String] | Request additional data in the output
};
apiInstance.getProgrammeByPID(pid, rights, availability, opts, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammeRecommendations

> Object getProgrammeRecommendations(pid, rights, availability, page, perPage)

Get programme recommendations

Get programme recommendations

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
apiInstance.getProgrammeRecommendations(pid, rights, availability, page, perPage, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammesPopular

> Object getProgrammesPopular(rights, page, perPage, initialChildCount, sort, sortDirection, availability, opts)

Get programmes popular

Get programmes popular

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let rights = "'web'"; // String | The rights group to limit results to.
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
let initialChildCount = 4; // Number | The depth to return child entities.
let sort = "sort_example"; // String | The sort order of the results.
let sortDirection = "sortDirection_example"; // String | Whether to sort ascending or descending
let availability = "'available'"; // String | Whether to return all, or available programmes
let opts = {
  'mixin': ["null"] // [String] | Request additional data in the output
};
apiInstance.getProgrammesPopular(rights, page, perPage, initialChildCount, sort, sortDirection, availability, opts, (error, data, response) => {
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
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 
 **initialChildCount** | **Number**| The depth to return child entities. | [default to 4]
 **sort** | **String**| The sort order of the results. | 
 **sortDirection** | **String**| Whether to sort ascending or descending | 
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]
 **mixin** | [**[String]**](String.md)| Request additional data in the output | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrailersPreRolls

> Object getTrailersPreRolls(pid, rights, availability)

Get Trailers (pre-rolls)

Get Trailers (pre-rolls)

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.EpisodesApi();
let pid = "pid_example"; // String | The programme identifier.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.getTrailersPreRolls(pid, rights, availability, (error, data, response) => {
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
 **pid** | **String**| The programme identifier. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

