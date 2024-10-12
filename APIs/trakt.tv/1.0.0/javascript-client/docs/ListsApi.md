# TraktApi.ListsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllListComments**](ListsApi.md#getAllListComments) | **GET** /lists/{id}/comments/{sort} | Get all list comments
[**getAllUsersWhoLikedAList**](ListsApi.md#getAllUsersWhoLikedAList) | **GET** /lists/{id}/likes | Get all users who liked a list
[**getItemsOnAList**](ListsApi.md#getItemsOnAList) | **GET** /lists/{id}/items/{type} | Get items on a list
[**getList**](ListsApi.md#getList) | **GET** /lists/{id} | Get list
[**getPopularLists**](ListsApi.md#getPopularLists) | **GET** /lists/popular | Get popular lists
[**getTrendingLists**](ListsApi.md#getTrendingLists) | **GET** /lists/trending | Get trending lists



## getAllListComments

> getAllListComments(id, sort, opts)

Get all list comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a list. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, and most &#x60;replies&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ListsApi();
let id = 55; // Number | Trakt ID
let sort = "newest"; // String | how to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllListComments(id, sort, opts, (error, data, response) => {
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
 **id** | **Number**| Trakt ID | 
 **sort** | **String**| how to sort | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllUsersWhoLikedAList

> getAllUsersWhoLikedAList(id, opts)

Get all users who liked a list

#### &amp;#128196; Pagination  Returns all users who liked a list.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ListsApi();
let id = "55"; // String | Trakt ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllUsersWhoLikedAList(id, opts, (error, data, response) => {
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
 **id** | **String**| Trakt ID | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemsOnAList

> getItemsOnAList(id, type, opts)

Get items on a list

#### &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Get all items on a personal list. Items can be a &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;person&#x60;. You can optionally specify the &#x60;type&#x60; parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending &#x60;rank&#x60;. We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which can be used to custom sort the list _**in your app**_ based on the user&#39;s preference. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, and &#x60;collected&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ListsApi();
let id = "55"; // String | Trakt ID
let type = "movies"; // String | Filter for a specific item type
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getItemsOnAList(id, type, opts, (error, data, response) => {
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
 **id** | **String**| Trakt ID | 
 **type** | **String**| Filter for a specific item type | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getList

> getList(id, opts)

Get list

#### &amp;#128513; Emojis  Returns a single list. Use the [**_/lists/:id/items**](#reference/lists/list-items) method to get the actual items this list contains.  **Note:** You must use an integer &#x60;id&#x60;, and only public lists will return data.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ListsApi();
let id = 55; // Number | Trakt ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getList(id, opts, (error, data, response) => {
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
 **id** | **Number**| Trakt ID | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPopularLists

> getPopularLists(opts)

Get popular lists

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns the most popular lists. Popularity is calculated using total number of likes and comments.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ListsApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getPopularLists(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrendingLists

> getTrendingLists(opts)

Get trending lists

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists with the most likes and comments over the last 7 days.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ListsApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTrendingLists(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

