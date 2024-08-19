# TrashNothing.PostsApi

All URIs are relative to *https://trashnothing.com/api/v1.3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllPosts**](PostsApi.md#getAllPosts) | **GET** /posts/all | List all posts
[**getAllPostsChanges**](PostsApi.md#getAllPostsChanges) | **GET** /posts/all/changes | List all post changes
[**getPost**](PostsApi.md#getPost) | **GET** /posts/{post_id} | Retrieve a post
[**getPostAndRelatedData**](PostsApi.md#getPostAndRelatedData) | **GET** /posts/{post_id}/display | Retrieve post display data
[**getPosts**](PostsApi.md#getPosts) | **GET** /posts | List posts
[**getPostsByIds**](PostsApi.md#getPostsByIds) | **GET** /posts/multiple | Retrieve multiple posts
[**searchPosts**](PostsApi.md#searchPosts) | **GET** /posts/search | Search posts



## getAllPosts

> GetAllPosts200Response getAllPosts(types, dateMin, dateMax, opts)

List all posts

This endpoint provides an easy way to get a feed of all the publicly published posts on trash nothing. It provides access to all publicly published offer and wanted posts from the last 30 days. The posts are sorted by date (newest first). &lt;br /&gt;&lt;br /&gt; There are fewer options for filtering, sorting and searching posts with this endpoint but there is no 1,000 post limit and posts that are crossposted to multiple groups are not merged together in the response.  In most cases, crossposted posts are easy to detect because they have the same user_id, title and content. 

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let types = "types_example"; // String | A comma separated list of the post types to return.  The available post types are: offer, wanted 
let dateMin = new Date("2013-10-20T19:20:30+01:00"); // Date | Only posts newer than or equal to this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_max. And the date and time must be within the last 30 days. And the date and time must be rounded to the nearest second. 
let dateMax = new Date("2013-10-20T19:20:30+01:00"); // Date | Only posts older than this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_min. And the date and time must be rounded to the nearest second. 
let opts = {
  'perPage': 20, // Number | The number of posts to return per page (must be >= 1 and <= 50).
  'page': 1, // Number | The page of posts to return.
  'devicePixelRatio': 1 // Number | Client device pixel ratio used to determine thumbnail size (default 1.0).
};
apiInstance.getAllPosts(types, dateMin, dateMax, opts, (error, data, response) => {
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
 **types** | **String**| A comma separated list of the post types to return.  The available post types are: offer, wanted  | 
 **dateMin** | **Date**| Only posts newer than or equal to this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_max. And the date and time must be within the last 30 days. And the date and time must be rounded to the nearest second.  | 
 **dateMax** | **Date**| Only posts older than this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_min. And the date and time must be rounded to the nearest second.  | 
 **perPage** | **Number**| The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 50). | [optional] [default to 20]
 **page** | **Number**| The page of posts to return. | [optional] [default to 1]
 **devicePixelRatio** | **Number**| Client device pixel ratio used to determine thumbnail size (default 1.0). | [optional] [default to 1]

### Return type

[**GetAllPosts200Response**](GetAllPosts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPostsChanges

> GetAllPostsChanges200Response getAllPostsChanges(dateMin, dateMax, opts)

List all post changes

This endpoint provides an easy way to get a feed of all the changes that have been made to publicly published posts on trash nothing.  Similar to the /posts/all endpoint, only data from the last 30 days is available and the changes are sorted by date (newest first).  Every change includes the date of the change, the post_id of the post that was changed and the type of change. &lt;br /&gt;&lt;br /&gt; The different types of changes that are returned are listed below. &lt;br /&gt;&lt;br /&gt; - deleted&lt;br /&gt; - undeleted&lt;br /&gt; - satisfied&lt;br /&gt; - promised&lt;br /&gt; - unpromised&lt;br /&gt; - withdrawn&lt;br /&gt; - edited&lt;br /&gt; &lt;br /&gt; For edited changes, clients can use the retrieve post API endpoint to get the edits that have been made to the post. 

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let dateMin = new Date("2013-10-20T19:20:30+01:00"); // Date | Only changes newer than or equal to this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_max. And the date and time must be within the last 30 days. And the date and time must be rounded to the nearest second. 
let dateMax = new Date("2013-10-20T19:20:30+01:00"); // Date | Only changes older than this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_min. And the date and time must be rounded to the nearest second. 
let opts = {
  'perPage': 20, // Number | The number of changes to return per page (must be >= 1 and <= 50).
  'page': 1 // Number | The page of changes to return.
};
apiInstance.getAllPostsChanges(dateMin, dateMax, opts, (error, data, response) => {
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
 **dateMin** | **Date**| Only changes newer than or equal to this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_max. And the date and time must be within the last 30 days. And the date and time must be rounded to the nearest second.  | 
 **dateMax** | **Date**| Only changes older than this UTC date and time will be returned. The UTC date and time used must be within a day or less of date_min. And the date and time must be rounded to the nearest second.  | 
 **perPage** | **Number**| The number of changes to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 50). | [optional] [default to 20]
 **page** | **Number**| The page of changes to return. | [optional] [default to 1]

### Return type

[**GetAllPostsChanges200Response**](GetAllPostsChanges200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPost

> Post getPost(postId)

Retrieve a post

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let postId = "postId_example"; // String | The ID of the post to retrieve.
apiInstance.getPost(postId, (error, data, response) => {
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
 **postId** | **String**| The ID of the post to retrieve. | 

### Return type

[**Post**](Post.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPostAndRelatedData

> GetPostAndRelatedData200Response getPostAndRelatedData(postId)

Retrieve post display data

Retrieve a post and other data related to the post that is useful for displaying the post such as data about the user who posted the post and the groups the post was posted on. 

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let postId = "postId_example"; // String | The ID of the post to retrieve.
apiInstance.getPostAndRelatedData(postId, (error, data, response) => {
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
 **postId** | **String**| The ID of the post to retrieve. | 

### Return type

[**GetPostAndRelatedData200Response**](GetPostAndRelatedData200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPosts

> GetPosts200Response getPosts(types, sources, opts)

List posts

NOTE: When paging through the posts returned by this endpoint, there will be at most 1,000 posts that can be returned (eg. 50 pages worth of posts with the default per_page value of 20).  In areas where there are more than 1,000 posts, clients can use more specific query parameters to adjust which posts are returned. NOTE: Passing the latitude, longitude and radius parameters filters all posts by their location and so these parameters will temporarily override the current users&#39; location preferences. When latitude, longitude and radius are not specified, public posts will be filtered by the current users&#39; location preferences. 

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let types = "types_example"; // String | A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
let sources = "sources_example"; // String | A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or the current users' location if latitude, longitude and radius aren't passed). <br /><br /> NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
let opts = {
  'sortBy': "'date'", // String | How to sort the posts that are returned.  One of: date, active, distance <br /><br /> Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first. 
  'groupIds': "'The group IDs of every group the current user is a member of.'", // String | A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the 'groups' source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). <br /><br /> NOTE: For requests using an api key instead of oauth, this field is required if the 'groups' source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). <br /><br/> *To determine which group IDs were used and which were discarded, use the group_ids field in the response. 
  'perPage': 20, // Number | The number of posts to return per page (must be >= 1 and <= 100).
  'page': 1, // Number | The page of posts to return.
  'devicePixelRatio': 1, // Number | Client device pixel ratio used to determine thumbnail size (default 1.0).
  'latitude': 3.4, // Number | The latitude of a point around which to return posts. 
  'longitude': 3.4, // Number | The longitude of a point around which to return posts. 
  'radius': 3.4, // Number | The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned. 
  'dateMin': new Date("2013-10-20T19:20:30+01:00"), // Date | Only posts newer than or equal to this UTC date and time will be returned.  If unset, defaults to the current date and time minus 90 days. 
  'dateMax': new Date("2013-10-20T19:20:30+01:00"), // Date | Only posts older than this UTC date and time will be returned.  If unset, defaults to the current date and time.
  'outcomes': "''", // String | A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn <br /><br /> There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to 'all', all posts will be returned no matter what outcome the posts have. If set to 'not-promised', only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
  'userState': "''", // String | If user_state is set, only posts matching the state specified will be returned.  Only one state may be passed and it must be one of the following: viewed, replied, bookmarked <br><br> NOTE: This option will only work with oauth requests. 
  'includeReposts': 1 // Number | If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
};
apiInstance.getPosts(types, sources, opts, (error, data, response) => {
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
 **types** | **String**| A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin  | 
 **sources** | **String**| A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or the current users&#39; location if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required.  | 
 **sortBy** | **String**| How to sort the posts that are returned.  One of: date, active, distance &lt;br /&gt;&lt;br /&gt; Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first.  | [optional] [default to &#39;date&#39;]
 **groupIds** | **String**| A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the &#39;groups&#39; source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, this field is required if the &#39;groups&#39; source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). &lt;br /&gt;&lt;br/&gt; *To determine which group IDs were used and which were discarded, use the group_ids field in the response.  | [optional] [default to &#39;The group IDs of every group the current user is a member of.&#39;]
 **perPage** | **Number**| The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100). | [optional] [default to 20]
 **page** | **Number**| The page of posts to return. | [optional] [default to 1]
 **devicePixelRatio** | **Number**| Client device pixel ratio used to determine thumbnail size (default 1.0). | [optional] [default to 1]
 **latitude** | **Number**| The latitude of a point around which to return posts.  | [optional] 
 **longitude** | **Number**| The longitude of a point around which to return posts.  | [optional] 
 **radius** | **Number**| The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned.  | [optional] 
 **dateMin** | **Date**| Only posts newer than or equal to this UTC date and time will be returned.  If unset, defaults to the current date and time minus 90 days.  | [optional] 
 **dateMax** | **Date**| Only posts older than this UTC date and time will be returned.  If unset, defaults to the current date and time. | [optional] 
 **outcomes** | **String**| A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned.  | [optional] [default to &#39;&#39;]
 **userState** | **String**| If user_state is set, only posts matching the state specified will be returned.  Only one state may be passed and it must be one of the following: viewed, replied, bookmarked &lt;br&gt;&lt;br&gt; NOTE: This option will only work with oauth requests.  | [optional] [default to &#39;&#39;]
 **includeReposts** | **Number**| If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified.  | [optional] [default to 1]

### Return type

[**GetPosts200Response**](GetPosts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPostsByIds

> GetPostsByIds200Response getPostsByIds(postIds)

Retrieve multiple posts

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let postIds = "postIds_example"; // String | A comma separated list of the post IDs. If more than 10 post IDs are passed, only the first 10 posts will be returned. 
apiInstance.getPostsByIds(postIds, (error, data, response) => {
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
 **postIds** | **String**| A comma separated list of the post IDs. If more than 10 post IDs are passed, only the first 10 posts will be returned.  | 

### Return type

[**GetPostsByIds200Response**](GetPostsByIds200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchPosts

> SearchPosts200Response searchPosts(search, types, sources, opts)

Search posts

Searching posts takes the same arguments as listing posts except for the addition of the search and sort_by parameters. NOTE: When paging through the posts returned by this endpoint, there will be at most 1,000 posts that can be returned (eg. 50 pages worth of posts with the default per_page value of 20).  In areas where there are more than 1,000 posts, clients can use more specific query parameters to adjust which posts are returned. 

### Example

```javascript
import TrashNothing from 'trash_nothing';
let defaultClient = TrashNothing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TrashNothing.PostsApi();
let search = "search_example"; // String | The search query used to find posts.
let types = "types_example"; // String | A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin 
let sources = "sources_example"; // String | A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or the current users' location if latitude, longitude and radius aren't passed). <br /><br /> NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required. 
let opts = {
  'sortBy': "'relevance'", // String | How to sort the posts that are returned.  One of: relevance, date, active, distance <br /><br /> Relevance sorting will sort the posts that best match the search query first. Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first. 
  'groupIds': "'The group IDs of every group the current user is a member of.'", // String | A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the 'groups' source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). <br /><br /> NOTE: For requests using an api key instead of oauth, this field is required if the 'groups' source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). <br /><br/> *To determine which group IDs were used and which were discarded, use the group_ids field in the response. 
  'perPage': 20, // Number | The number of posts to return per page (must be >= 1 and <= 100).
  'page': 1, // Number | The page of posts to return.
  'devicePixelRatio': 1, // Number | Client device pixel ratio used to determine thumbnail size (default 1.0).
  'latitude': 3.4, // Number | The latitude of a point around which to return posts. 
  'longitude': 3.4, // Number | The longitude of a point around which to return posts. 
  'radius': 3.4, // Number | The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned. 
  'dateMin': new Date("2013-10-20T19:20:30+01:00"), // Date | Only posts newer than or equal to this UTC date and time will be returned.  If unset, defaults to the current date and time minus 90 days. 
  'dateMax': new Date("2013-10-20T19:20:30+01:00"), // Date | Only posts older than this UTC date and time will be returned.  If unset, defaults to the current date and time.
  'outcomes': "''", // String | A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn <br /><br /> There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to 'all', all posts will be returned no matter what outcome the posts have. If set to 'not-promised', only posts that are not satisfied ant not withdrawn and not expired and not promised are returned. 
  'userState': "''", // String | If user_state is set, only posts matching the state specified will be returned.  Only one state may be passed and it must be one of the following: viewed, replied, bookmarked <br><br> NOTE: This option will only work with oauth requests. 
  'includeReposts': 1 // Number | If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified. 
};
apiInstance.searchPosts(search, types, sources, opts, (error, data, response) => {
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
 **search** | **String**| The search query used to find posts. | 
 **types** | **String**| A comma separated list of the post types to return.  The available post types are: offer, taken, wanted, received, admin  | 
 **sources** | **String**| A comma separated list of the post sources to retrieve posts from. The available sources are: groups, trashnothing, open_archive_groups. The trashnothing source is for public posts that are posted on trash nothing but are not associated with any group. The open_archive_groups source provides a way to easily request posts from groups that have open_archives set to true without having to pass a group_ids parameter.  When passed, it will automatically return posts from open archive groups that are within the area specified by the latitude, longitude and radius parameters (or the current users&#39; location if latitude, longitude and radius aren&#39;t passed). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, passing the trashnothing source or the open_archive_groups source makes the latitude, longitude and radius parameters required.  | 
 **sortBy** | **String**| How to sort the posts that are returned.  One of: relevance, date, active, distance &lt;br /&gt;&lt;br /&gt; Relevance sorting will sort the posts that best match the search query first. Date sorting will sort posts from newest to oldest. Active sorting will sort active posts before satisfied, withdrawn and expired posts and then sort by date. Distance sorting will sort the closest posts first.  | [optional] [default to &#39;relevance&#39;]
 **groupIds** | **String**| A comma separated list of the group IDs to retrieve posts from. This parameter is only used if the &#39;groups&#39; source is passed in the sources parameter and only groups that the current user is a member of or that are open archives groups will be used (the group IDs of other groups will be silently discarded*). &lt;br /&gt;&lt;br /&gt; NOTE: For requests using an api key instead of oauth, this field is required if the &#39;groups&#39; source is passed. In addition, only posts from groups that have open_archives set to true will be used (the group IDS of other groups will be silently discarded*). &lt;br /&gt;&lt;br/&gt; *To determine which group IDs were used and which were discarded, use the group_ids field in the response.  | [optional] [default to &#39;The group IDs of every group the current user is a member of.&#39;]
 **perPage** | **Number**| The number of posts to return per page (must be &gt;&#x3D; 1 and &lt;&#x3D; 100). | [optional] [default to 20]
 **page** | **Number**| The page of posts to return. | [optional] [default to 1]
 **devicePixelRatio** | **Number**| Client device pixel ratio used to determine thumbnail size (default 1.0). | [optional] [default to 1]
 **latitude** | **Number**| The latitude of a point around which to return posts.  | [optional] 
 **longitude** | **Number**| The longitude of a point around which to return posts.  | [optional] 
 **radius** | **Number**| The radius in meters of a circle centered at the point defined by the latitude and longitude parameters. When latitude, longitude and radius are passed, only posts within the circle defined by these parameters will be returned.  | [optional] 
 **dateMin** | **Date**| Only posts newer than or equal to this UTC date and time will be returned.  If unset, defaults to the current date and time minus 90 days.  | [optional] 
 **dateMax** | **Date**| Only posts older than this UTC date and time will be returned.  If unset, defaults to the current date and time. | [optional] 
 **outcomes** | **String**| A comma separated list of the post outcomes to return.  The available post outcomes are: satisfied, withdrawn &lt;br /&gt;&lt;br /&gt; There are also a couple special values that can be passed.  If set to an empty string (the default), only posts that are not satisfied and not withdrawn and not expired are returned. If set to &#39;all&#39;, all posts will be returned no matter what outcome the posts have. If set to &#39;not-promised&#39;, only posts that are not satisfied ant not withdrawn and not expired and not promised are returned.  | [optional] [default to &#39;&#39;]
 **userState** | **String**| If user_state is set, only posts matching the state specified will be returned.  Only one state may be passed and it must be one of the following: viewed, replied, bookmarked &lt;br&gt;&lt;br&gt; NOTE: This option will only work with oauth requests.  | [optional] [default to &#39;&#39;]
 **includeReposts** | **Number**| If set to 1 (the default), posts that are reposts will be included. If set to 0, reposts will be excluded. See the repost_count field of post objects for details about how reposts are identified.  | [optional] [default to 1]

### Return type

[**SearchPosts200Response**](SearchPosts200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

