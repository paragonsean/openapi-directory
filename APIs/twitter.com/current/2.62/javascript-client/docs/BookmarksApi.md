# TwitterApiV2.BookmarksApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUsersIdBookmarks**](BookmarksApi.md#getUsersIdBookmarks) | **GET** /2/users/{id}/bookmarks | Bookmarks by User
[**postUsersIdBookmarks**](BookmarksApi.md#postUsersIdBookmarks) | **POST** /2/users/{id}/bookmarks | Add Tweet to Bookmarks
[**usersIdBookmarksDelete**](BookmarksApi.md#usersIdBookmarksDelete) | **DELETE** /2/users/{id}/bookmarks/{tweet_id} | Remove a bookmarked Tweet



## getUsersIdBookmarks

> Get2UsersIdBookmarksResponse getUsersIdBookmarks(id, opts)

Bookmarks by User

Returns Tweet objects that have been bookmarked by the requesting User

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.BookmarksApi();
let id = "id_example"; // String | The ID of the authenticated source User for whom to return results.
let opts = {
  'maxResults': 56, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get the next 'page' of results.
  'tweetFields': ["null"], // [String] | A comma separated list of Tweet fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'pollFields': ["null"], // [String] | A comma separated list of Poll fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'placeFields': ["null"] // [String] | A comma separated list of Place fields to display.
};
apiInstance.getUsersIdBookmarks(id, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User for whom to return results. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] 
 **paginationToken** | **String**| This parameter is used to get the next &#39;page&#39; of results. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **pollFields** | [**[String]**](String.md)| A comma separated list of Poll fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **placeFields** | [**[String]**](String.md)| A comma separated list of Place fields to display. | [optional] 

### Return type

[**Get2UsersIdBookmarksResponse**](Get2UsersIdBookmarksResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## postUsersIdBookmarks

> BookmarkMutationResponse postUsersIdBookmarks(id, bookmarkAddRequest)

Add Tweet to Bookmarks

Adds a Tweet (ID in the body) to the requesting User&#39;s (in the path) bookmarks

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.BookmarksApi();
let id = "id_example"; // String | The ID of the authenticated source User for whom to add bookmarks.
let bookmarkAddRequest = new TwitterApiV2.BookmarkAddRequest(); // BookmarkAddRequest | 
apiInstance.postUsersIdBookmarks(id, bookmarkAddRequest, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User for whom to add bookmarks. | 
 **bookmarkAddRequest** | [**BookmarkAddRequest**](BookmarkAddRequest.md)|  | 

### Return type

[**BookmarkMutationResponse**](BookmarkMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## usersIdBookmarksDelete

> BookmarkMutationResponse usersIdBookmarksDelete(id, tweetId)

Remove a bookmarked Tweet

Removes a Tweet from the requesting User&#39;s bookmarked Tweets.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.BookmarksApi();
let id = "id_example"; // String | The ID of the authenticated source User whose bookmark is to be removed.
let tweetId = "tweetId_example"; // String | The ID of the Tweet that the source User is removing from bookmarks.
apiInstance.usersIdBookmarksDelete(id, tweetId, (error, data, response) => {
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
 **id** | **String**| The ID of the authenticated source User whose bookmark is to be removed. | 
 **tweetId** | **String**| The ID of the Tweet that the source User is removing from bookmarks. | 

### Return type

[**BookmarkMutationResponse**](BookmarkMutationResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

