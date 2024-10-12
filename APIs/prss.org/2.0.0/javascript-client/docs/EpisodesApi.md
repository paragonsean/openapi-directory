# ContentDepot.EpisodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2EpisodesGet**](EpisodesApi.md#apiV2EpisodesGet) | **GET** /api/v2/episodes | Gets episodes matching the given criteria.
[**apiV2EpisodesIdGet**](EpisodesApi.md#apiV2EpisodesIdGet) | **GET** /api/v2/episodes/{id} | Returns the episode matching the given ID.



## apiV2EpisodesGet

> [Episode] apiV2EpisodesGet(programId, opts)

Gets episodes matching the given criteria.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.EpisodesApi();
let programId = 789; // Number | Matches on the ID of the program that owns the episode.
let opts = {
  'id': 789, // Number | Matches on the ID of the episode.
  'beginAirDateAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Matches on the begin air date of the episode (inclusive).
  'endAirDateBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Matches on the end air date of the episode (inclusive).
  'pageStart': 0, // Number | The start page of the results to return. The first item is indexed at 0.
  'pageSize': 500, // Number | The number of items to return. Must be between 0 and 500, inclusive.
  'orderById': "orderById_example" // String | The sort order of the list of episodes, based on episode ID. If unspecified, the episodes are returned in random order. If using paging to iterate through the results, sort order should be specified.
};
apiInstance.apiV2EpisodesGet(programId, opts, (error, data, response) => {
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
 **programId** | **Number**| Matches on the ID of the program that owns the episode. | 
 **id** | **Number**| Matches on the ID of the episode. | [optional] 
 **beginAirDateAfter** | **Date**| Matches on the begin air date of the episode (inclusive). | [optional] 
 **endAirDateBefore** | **Date**| Matches on the end air date of the episode (inclusive). | [optional] 
 **pageStart** | **Number**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0]
 **pageSize** | **Number**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500]
 **orderById** | **String**| The sort order of the list of episodes, based on episode ID. If unspecified, the episodes are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] 

### Return type

[**[Episode]**](Episode.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2EpisodesIdGet

> Episode apiV2EpisodesIdGet(id)

Returns the episode matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.EpisodesApi();
let id = 789; // Number | The ID of the episode to operate on.
apiInstance.apiV2EpisodesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the episode to operate on. | 

### Return type

[**Episode**](Episode.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

