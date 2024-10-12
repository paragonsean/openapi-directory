# TraktApi.UsersApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addHiddenItems**](UsersApi.md#addHiddenItems) | **POST** /users/hidden/{section} | Add hidden items
[**addItemsToPersonalList**](UsersApi.md#addItemsToPersonalList) | **POST** /users/{id}/lists/{list_id}/items | Add items to personal list
[**approveFollowRequest**](UsersApi.md#approveFollowRequest) | **POST** /users/requests/{id} | Approve follow request
[**createPersonalList**](UsersApi.md#createPersonalList) | **POST** /users/{id}/lists | Create personal list
[**deleteAUsersPersonalList**](UsersApi.md#deleteAUsersPersonalList) | **DELETE** /users/{id}/lists/{list_id} | Delete a user&#39;s personal list
[**denyFollowRequest**](UsersApi.md#denyFollowRequest) | **DELETE** /users/requests/{id} | Deny follow request
[**followThisUser**](UsersApi.md#followThisUser) | **POST** /users/{id}/follow | Follow this user
[**getAUsersPersonalLists**](UsersApi.md#getAUsersPersonalLists) | **GET** /users/{id}/lists | Get a user&#39;s personal lists
[**getAllListsAUserCanCollaborateOn**](UsersApi.md#getAllListsAUserCanCollaborateOn) | **GET** /users/{id}/lists/collaborations | Get all lists a user can collaborate on
[**getComments**](UsersApi.md#getComments) | **GET** /users/{id}/comments/{comment_type}/{type} | Get comments
[**getFollowRequests**](UsersApi.md#getFollowRequests) | **GET** /users/requests | Get follow requests
[**getFollowers**](UsersApi.md#getFollowers) | **GET** /users/{id}/followers | Get followers
[**getFollowing**](UsersApi.md#getFollowing) | **GET** /users/{id}/following | Get following
[**getFriends**](UsersApi.md#getFriends) | **GET** /users/{id}/friends | Get friends
[**getHiddenItems**](UsersApi.md#getHiddenItems) | **GET** /users/hidden/{section} | Get hidden items
[**getItemsOnAPersonalList**](UsersApi.md#getItemsOnAPersonalList) | **GET** /users/{id}/lists/{list_id}/items/{type} | Get items on a personal list
[**getLikes**](UsersApi.md#getLikes) | **GET** /users/{id}/likes/{type} | Get likes
[**getPendingFollowingRequests**](UsersApi.md#getPendingFollowingRequests) | **GET** /users/requests/following | Get pending following requests
[**getPersonalList**](UsersApi.md#getPersonalList) | **GET** /users/{id}/lists/{list_id} | Get personal list
[**getSavedFilters**](UsersApi.md#getSavedFilters) | **GET** /users/saved_filters/{section} | Get saved filters
[**getStats**](UsersApi.md#getStats) | **GET** /users/{id}/stats | Get stats
[**getUserProfile**](UsersApi.md#getUserProfile) | **GET** /users/{id} | Get user profile
[**getWatching**](UsersApi.md#getWatching) | **GET** /users/{id}/watching | Get watching
[**likeAList**](UsersApi.md#likeAList) | **POST** /users/{id}/lists/{list_id}/like | Like a list
[**removeHiddenItems**](UsersApi.md#removeHiddenItems) | **POST** /users/hidden/{section}/remove | Remove hidden items
[**removeItemsFromPersonalList**](UsersApi.md#removeItemsFromPersonalList) | **POST** /users/{id}/lists/{list_id}/items/remove | Remove items from personal list
[**removeLikeOnAList**](UsersApi.md#removeLikeOnAList) | **DELETE** /users/{id}/lists/{list_id}/like | Remove like on a list
[**reorderAUsersLists**](UsersApi.md#reorderAUsersLists) | **POST** /users/{id}/lists/reorder | Reorder a user&#39;s lists
[**reorderItemsOnAList**](UsersApi.md#reorderItemsOnAList) | **POST** /users/{id}/lists/{list_id}/items/reorder | Reorder items on a list
[**retrieveSettings**](UsersApi.md#retrieveSettings) | **GET** /users/settings | Retrieve settings
[**unfollowThisUser**](UsersApi.md#unfollowThisUser) | **DELETE** /users/{id}/follow | Unfollow this user
[**updatePersonalList**](UsersApi.md#updatePersonalList) | **PUT** /users/{id}/lists/{list_id} | Update personal list
[**usersIdCollectionTypeGet**](UsersApi.md#usersIdCollectionTypeGet) | **GET** /users/{id}/collection/{type} | Get collection
[**usersIdHistoryTypeItemIdGet**](UsersApi.md#usersIdHistoryTypeItemIdGet) | **GET** /users/{id}/history/{type}/{item_id} | Get watched history
[**usersIdListsListIdCommentsSortGet**](UsersApi.md#usersIdListsListIdCommentsSortGet) | **GET** /users/{id}/lists/{list_id}/comments/{sort} | Get all list comments
[**usersIdListsListIdLikesGet**](UsersApi.md#usersIdListsListIdLikesGet) | **GET** /users/{id}/lists/{list_id}/likes | Get all users who liked a list
[**usersIdRatingsTypeRatingGet**](UsersApi.md#usersIdRatingsTypeRatingGet) | **GET** /users/{id}/ratings/{type}/{rating} | Get ratings
[**usersIdRecommendationsTypeSortGet**](UsersApi.md#usersIdRecommendationsTypeSortGet) | **GET** /users/{id}/recommendations/{type}/{sort} | Get personal recommendations
[**usersIdWatchedTypeGet**](UsersApi.md#usersIdWatchedTypeGet) | **GET** /users/{id}/watched/{type} | Get watched
[**usersIdWatchlistTypeSortGet**](UsersApi.md#usersIdWatchlistTypeSortGet) | **GET** /users/{id}/watchlist/{type}/{sort} | Get watchlist



## addHiddenItems

> addHiddenItems(section, opts)

Add hidden items

#### &amp;#128274; OAuth Required  Hide items for a specific section. Here&#39;s what type of items can hidden for each section.  #### Hideable Media Objects  | Section | Objects | |---|---|---| | &#x60;calendar&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;progress_watched&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;progress_collected&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;recommendations&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;comments&#x60; | &#x60;user&#x60; |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;users&#x60; | array | Array of &#x60;user&#x60; objects. |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let section = "calendar"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'addHiddenItemsRequest': new TraktApi.AddHiddenItemsRequest() // AddHiddenItemsRequest | 
};
apiInstance.addHiddenItems(section, opts, (error, data, response) => {
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
 **section** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **addHiddenItemsRequest** | [**AddHiddenItemsRequest**](AddHiddenItemsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addItemsToPersonalList

> addItemsToPersonalList(id, listId, opts)

Add items to personal list

#### &amp;#128274; OAuth Required &amp;#128513; Emojis 🔥 VIP Enhanced  Add one or more items to a personal list. Items can be movies, shows, seasons, episodes, or people.  #### Notes  Each list item can optionally accept a &#x60;notes&#x60; *(255 maximum characters)* field with custom text. The user must be a [**Trakt VIP**](https://trakt.tv/vip) to send &#x60;notes&#x60;.  #### Limits  If the user&#39;s list item limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;people&#x60; | array | Array of &#x60;person&#x60; objects. |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'addItemsToPersonalListRequest': new TraktApi.AddItemsToPersonalListRequest() // AddItemsToPersonalListRequest | 
};
apiInstance.addItemsToPersonalList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **addItemsToPersonalListRequest** | [**AddItemsToPersonalListRequest**](AddItemsToPersonalListRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## approveFollowRequest

> approveFollowRequest(id, opts)

Approve follow request

#### &amp;#128274; OAuth Required  Approve a follower using the &#x60;id&#x60; of the request. If the &#x60;id&#x60; is not found, was already approved, or was already denied, a &#x60;404&#x60; error will be returned.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "123"; // String | ID of the follower request.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.approveFollowRequest(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the follower request. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPersonalList

> createPersonalList(id, opts)

Create personal list

#### &amp;#128274; OAuth Required 🔥 VIP Enhanced  Create a new personal list. The &#x60;name&#x60; is the only required field, but the other info is recommended to ask for.  #### Limits  If the user&#39;s list limit is exceeded, a &#x60;420&#x60; HTTP error code is returned. Use the [**_/users/settings**](/reference/users/settings) method to get all limits for a user account. In most cases, upgrading to [**Trakt VIP**](https://trakt.tv/vip) will increase the limits.  #### Privacy  Lists will be &#x60;private&#x60; by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | &#x60;private&#x60; | Only you can see the list. | | &#x60;link&#x60; | Anyone with the &#x60;share_link&#x60; can see the list. | | &#x60;friends&#x60; | Only your friends can see the list. | | &#x60;public&#x60; | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Default | Value | |---|---|---|---| | &#x60;name&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string |  | Name of the list. | | &#x60;description&#x60; | string |  | Description for this list. | | &#x60;privacy&#x60; | string | &#x60;private&#x60; | &#x60;private&#x60;, &#x60;link&#x60;, &#x60;friends&#x60;, &#x60;public&#x60; | | &#x60;display_numbers&#x60; | boolean | &#x60;false&#x60; | Should each item be numbered? | | &#x60;allow_comments&#x60; | boolean | &#x60;true&#x60; | Are comments allowed? | | &#x60;sort_by&#x60; | string | &#x60;rank&#x60; | &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, &#x60;collected&#x60; | | &#x60;sort_how&#x60; | string | &#x60;asc&#x60; | &#x60;asc&#x60;, &#x60;desc&#x60; |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'createPersonalListRequest': new TraktApi.CreatePersonalListRequest() // CreatePersonalListRequest | 
};
apiInstance.createPersonalList(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **createPersonalListRequest** | [**CreatePersonalListRequest**](CreatePersonalListRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAUsersPersonalList

> deleteAUsersPersonalList(id, listId, opts)

Delete a user&#39;s personal list

#### &amp;#128274; OAuth Required  Remove a personal list and all items it contains.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "id_example"; // String | Automatically added
let listId = "listId_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.deleteAUsersPersonalList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **listId** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## denyFollowRequest

> denyFollowRequest(id, opts)

Deny follow request

#### &amp;#128274; OAuth Required  Deny a follower using the &#x60;id&#x60; of the request. If the &#x60;id&#x60; is not found, was already approved, or was already denied, a &#x60;404&#x60; error will be returned.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.denyFollowRequest(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## followThisUser

> followThisUser(id, opts)

Follow this user

#### &amp;#128274; OAuth Required  If the user has a private profile, the follow request will require approval (&#x60;approved_at&#x60; will be null). If a user is public, they will be followed immediately (&#x60;approved_at&#x60; will have a date).  **Note:** If this user is already being followed, a &#x60;409&#x60; HTTP status code will returned.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.followThisUser(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAUsersPersonalLists

> getAUsersPersonalLists(id, opts)

Get a user&#39;s personal lists

#### &amp;#128275; OAuth Optional &amp;#128513; Emojis  Returns all personal lists for a user. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items a specific list contains.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAUsersPersonalLists(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllListsAUserCanCollaborateOn

> getAllListsAUserCanCollaborateOn(id, opts)

Get all lists a user can collaborate on

#### &amp;#128275; OAuth Optional  Returns all lists a user can collaborate on. This gives full access to add, remove, and re-order list items. It essentially works just like a list owned by the user, just make sure to use the correct list owner &#x60;user&#x60; when building the API URLs.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllListsAUserCanCollaborateOn(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComments

> getComments(id, commentType, type, opts)

Get comments

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#10024; Extended Info  Returns the most recently written comments for the user. You can optionally filter by the &#x60;comment_type&#x60; and media &#x60;type&#x60; to limit what gets returned.  By default, only top level comments are returned. Set &#x60;?include_replies&#x3D;true&#x60; to return replies in addition to top level comments. Set &#x60;?include_replies&#x3D;only&#x60; to return only replies and no top level comments.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let commentType = "all"; // String | 
let type = "all"; // String | 
let opts = {
  'includeReplies': "false", // String | include comment replies
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getComments(id, commentType, type, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **commentType** | **String**|  | 
 **type** | **String**|  | 
 **includeReplies** | **String**| include comment replies | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFollowRequests

> getFollowRequests(opts)

Get follow requests

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  List a user&#39;s pending follow requests so they can either approve or deny them.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getFollowRequests(opts, (error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFollowers

> getFollowers(id, opts)

Get followers

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all followers including when the relationship began.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getFollowers(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFollowing

> getFollowing(id, opts)

Get following

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all user&#39;s they follow including when the relationship began.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getFollowing(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFriends

> getFriends(id, opts)

Get friends

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all friends for a user including when the relationship began. Friendship is a 2 way relationship where each user follows the other.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getFriends(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHiddenItems

> getHiddenItems(section, opts)

Get hidden items

#### &amp;#128274; OAuth Required &amp;#128196; Pagination &amp;#10024; Extended Info  Get hidden items for a section. This will return an array of standard media objects. You can optionally limit the &#x60;type&#x60; of results to return.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let section = "calendar"; // String | 
let opts = {
  'type': "type_example", // String | Narrow down by element type.
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getHiddenItems(section, opts, (error, data, response) => {
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
 **section** | **String**|  | 
 **type** | **String**| Narrow down by element type. | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemsOnAPersonalList

> getItemsOnAPersonalList(id, listId, type, opts)

Get items on a personal list

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Get all items on a personal list. Items can be a &#x60;movie&#x60;, &#x60;show&#x60;, &#x60;season&#x60;, &#x60;episode&#x60;, or &#x60;person&#x60;. You can optionally specify the &#x60;type&#x60; parameter with a single value or comma delimited string for multiple item types.  #### Notes  Each list item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  All list items are sorted by ascending &#x60;rank&#x60;. We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which can be used to custom sort the list _**in your app**_ based on the user&#39;s preference. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, and &#x60;collected&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let type = "movies"; // String | Filter for a specific item type
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getItemsOnAPersonalList(id, listId, type, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
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


## getLikes

> getLikes(id, type, opts)

Get likes

#### &amp;#128274; OAuth Optional &amp;#128196; Pagination  Get items a user likes. This will return an array of standard media objects. You can optionally limit the &#x60;type&#x60; of results to return.  #### Comment Media Objects  If you add &#x60;?extended&#x3D;comments&#x60; to the URL, it will return media objects for each comment like.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "type_example"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getLikes(id, type, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPendingFollowingRequests

> getPendingFollowingRequests(opts)

Get pending following requests

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  List a user&#39;s pending following requests that they&#39;re waiting for the other user&#39;s to approve.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getPendingFollowingRequests(opts, (error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalList

> getPersonalList(id, listId, opts)

Get personal list

#### &amp;#128275; OAuth Optional &amp;#128513; Emojis  Returns a single personal list. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get the actual items this list contains.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getPersonalList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSavedFilters

> getSavedFilters(section, opts)

Get saved filters

#### &amp;#128274; OAuth Required &amp;#128196; Pagination 🔥 VIP Only  Get all saved filters a user has created. The &#x60;path&#x60; and &#x60;query&#x60; can be used to construct an API path to retrieve the saved data. Think of this like a dynamically updated list.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let section = "movies"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getSavedFilters(section, opts, (error, data, response) => {
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
 **section** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStats

> getStats(id, opts)

Get stats

#### &amp;#128275; OAuth Optional  Returns stats about the movies, shows, and episodes a user has watched, collected, and rated.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getStats(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserProfile

> getUserProfile(id, opts)

Get user profile

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Get a user&#39;s profile information. If the user is private, info will only be returned if you send OAuth and are either that user or an approved follower. Adding &#x60;?extended&#x3D;vip&#x60; will return some additional VIP related fields so you can display the user&#39;s Trakt VIP status and year count.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getUserProfile(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWatching

> getWatching(id, opts)

Get watching

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns a movie or episode if the user is currently watching something.  If they are not, it returns no data and a &#x60;204&#x60; HTTP status code.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getWatching(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## likeAList

> likeAList(id, listId, opts)

Like a list

#### &amp;#128274; OAuth Required  Votes help determine popular lists. Only one like is allowed per list per user.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.likeAList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeHiddenItems

> removeHiddenItems(section, opts)

Remove hidden items

#### &amp;#128274; OAuth Required  Unhide items for a specific section. Here&#39;s what type of items can unhidden for each section.  #### Unhideable Media Objects  | Section | Objects | |---|---|---| | &#x60;calendar&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;progress_watched&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;progress_collected&#x60; | &#x60;show&#x60;, &#x60;season&#x60; | | &#x60;recommendations&#x60; | &#x60;movie&#x60;, &#x60;show&#x60; | | &#x60;comments&#x60; | &#x60;user&#x60; |  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;users&#x60; | array | Array of &#x60;user&#x60; objects. |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let section = "calendar"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'addHiddenItemsRequest': new TraktApi.AddHiddenItemsRequest() // AddHiddenItemsRequest | 
};
apiInstance.removeHiddenItems(section, opts, (error, data, response) => {
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
 **section** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **addHiddenItemsRequest** | [**AddHiddenItemsRequest**](AddHiddenItemsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeItemsFromPersonalList

> removeItemsFromPersonalList(id, listId, opts)

Remove items from personal list

#### &amp;#128274; OAuth Required  Remove one or more items from a personal list.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;movies&#x60; | array | Array of &#x60;movie&#x60; objects. (see examples &amp;#8594;) | | &#x60;shows&#x60; | array | Array of &#x60;show&#x60; objects. | | &#x60;seasons&#x60; | array | Array of &#x60;season&#x60; objects. | | &#x60;episodes&#x60; | array | Array of &#x60;episode&#x60; objects. | | &#x60;people&#x60; | array | Array of &#x60;person&#x60; objects. |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'removeItemsFromPersonalListRequest': new TraktApi.RemoveItemsFromPersonalListRequest() // RemoveItemsFromPersonalListRequest | 
};
apiInstance.removeItemsFromPersonalList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **removeItemsFromPersonalListRequest** | [**RemoveItemsFromPersonalListRequest**](RemoveItemsFromPersonalListRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeLikeOnAList

> removeLikeOnAList(id, listId, opts)

Remove like on a list

#### &amp;#128274; OAuth Required  Remove a like on a list.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "id_example"; // String | Automatically added
let listId = "listId_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.removeLikeOnAList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **listId** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reorderAUsersLists

> reorderAUsersLists(id, opts)

Reorder a user&#39;s lists

#### &amp;#128274; OAuth Required  Reorder all lists by sending the updated &#x60;rank&#x60; of list ids. Use the [**_/users/:id/lists**](#reference/users/lists) method to get all list ids.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'reorderAUserSListsRequest': new TraktApi.ReorderAUserSListsRequest() // ReorderAUserSListsRequest | 
};
apiInstance.reorderAUsersLists(id, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **reorderAUserSListsRequest** | [**ReorderAUserSListsRequest**](ReorderAUserSListsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reorderItemsOnAList

> reorderItemsOnAList(id, listId, opts)

Reorder items on a list

#### &amp;#128274; OAuth Required  Reorder all items on a list by sending the updated &#x60;rank&#x60; of list item ids. Use the [**_/users/:id/lists/:list_id/items**](#reference/users/list-items) method to get all list item ids.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'reorderPersonallyRecommendedItemsRequest': new TraktApi.ReorderPersonallyRecommendedItemsRequest() // ReorderPersonallyRecommendedItemsRequest | 
};
apiInstance.reorderItemsOnAList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **reorderPersonallyRecommendedItemsRequest** | [**ReorderPersonallyRecommendedItemsRequest**](ReorderPersonallyRecommendedItemsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveSettings

> retrieveSettings(opts)

Retrieve settings

#### &amp;#128274; OAuth Required  Get the user&#39;s settings so you can align your app&#39;s experience with what they&#39;re used to on the trakt website. A globally unique &#x60;uuid&#x60; is also returned, which can be used to identify the user locally in your app if needed. However, the &#x60;uuid&#x60; can&#39;t be used to retrieve data from the Trakt API.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.retrieveSettings(opts, (error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unfollowThisUser

> unfollowThisUser(id, opts)

Unfollow this user

#### &amp;#128274; OAuth Required  Unfollow someone you already follow.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.unfollowThisUser(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updatePersonalList

> updatePersonalList(id, listId, opts)

Update personal list

#### &amp;#128274; OAuth Required  Update a personal list by sending 1 or more parameters. If you update the list name, the original slug will still be retained so existing references to this list won&#39;t break.  #### Privacy  Lists will be &#x60;private&#x60; by default. Here is what each value means.  | Value | Privacy impact... | |---|---| | &#x60;private&#x60; | Only you can see the list. | | &#x60;link&#x60; | Anyone with the &#x60;share_link&#x60; can see the list. | | &#x60;friends&#x60; | Only your friends can see the list. | | &#x60;public&#x60; | Anyone can see the list. |  #### JSON POST Data  | Key | Type | Value | |---|---|---|---| | &#x60;name&#x60; | string | Name of the list. | | &#x60;description&#x60; | string | Description for this list. | | &#x60;privacy&#x60; | string | &#x60;private&#x60;, &#x60;link&#x60;, &#x60;friends&#x60;, &#x60;public&#x60; | | &#x60;display_numbers&#x60; | boolean | Should each item be numbered? | | &#x60;allow_comments&#x60; | boolean | Are comments allowed? | | &#x60;sort_by&#x60; | string | &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, &#x60;votes&#x60;, &#x60;my_rating&#x60;, &#x60;random&#x60;, &#x60;watched&#x60;, &#x60;collected&#x60; | | &#x60;sort_how&#x60; | string | &#x60;asc&#x60;, &#x60;desc&#x60; |

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "id_example"; // String | Automatically added
let listId = "listId_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]", // String | e.g. [client_id]
  'updatePersonalListRequest': new TraktApi.UpdatePersonalListRequest() // UpdatePersonalListRequest | 
};
apiInstance.updatePersonalList(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **listId** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 
 **updatePersonalListRequest** | [**UpdatePersonalListRequest**](UpdatePersonalListRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdCollectionTypeGet

> usersIdCollectionTypeGet(id, type, opts)

Get collection

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Get all collected items in a user&#39;s collection. A collected item indicates availability to watch digitally or on physical media.  Each &#x60;movie&#x60; object contains &#x60;collected_at&#x60; and &#x60;updated_at&#x60; timestamps. Since users can set custom dates when they collected movies, it is possible for &#x60;collected_at&#x60; to be in the past. We also include &#x60;updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movie if you see a newer timestamp.  Each &#x60;show&#x60; object contains &#x60;last_collected_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they collected episodes, it is possible for &#x60;last_collected_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the show if you see a newer timestamp.  If you add &#x60;?extended&#x3D;metadata&#x60; to the URL, it will return the additional &#x60;media_type&#x60;, &#x60;resolution&#x60;, &#x60;hdr&#x60;, &#x60;audio&#x60;, &#x60;audio_channels&#x60; and &#39;3d&#39; metadata. It will use &#x60;null&#x60; if the metadata isn&#39;t set for an item.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "movies"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdCollectionTypeGet(id, type, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdHistoryTypeItemIdGet

> usersIdHistoryTypeItemIdGet(id, type, itemId, opts)

Get watched history

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#10024; Extended Info  Returns movies and episodes that a user has watched, sorted by most recent. You can optionally limit the &#x60;type&#x60; to &#x60;movies&#x60; or &#x60;episodes&#x60;. The &#x60;id&#x60; _(64-bit integer)_ in each history item uniquely identifies the event and can be used to remove individual events by using the [**_/sync/history/remove**](#reference/sync/remove-from-history/get-watched-history) method. The &#x60;action&#x60; will be set to &#x60;scrobble&#x60;, &#x60;checkin&#x60;, or &#x60;watch&#x60;.  Specify a &#x60;type&#x60; and trakt &#x60;item_id&#x60; to limit the history for just that item. If the &#x60;item_id&#x60; is valid, but there is no history, an empty array will be returned.  | Example URL | Returns watches for... | |---|---| | &#x60;/history/movies/12601&#x60; | TRON: Legacy | | &#x60;/history/shows/1388&#x60; | All episodes of Breaking Bad | | &#x60;/history/seasons/3950&#x60; | All episodes of Breaking Bad: Season 1 | | &#x60;/history/episodes/73482&#x60; | Only episode 1 for Breaking Bad: Season 1 |

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "movies"; // String | 
let itemId = 123; // Number | Trakt ID for a specific item.
let opts = {
  'startAt': "2016-06-01T00:00:00.000Z", // String | Starting date.
  'endAt': "2016-07-01T23:59:59.000Z", // String | Ending date.
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdHistoryTypeItemIdGet(id, type, itemId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**|  | 
 **itemId** | **Number**| Trakt ID for a specific item. | 
 **startAt** | **String**| Starting date. | [optional] 
 **endAt** | **String**| Ending date. | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdListsListIdCommentsSortGet

> usersIdListsListIdCommentsSortGet(id, listId, sort, opts)

Get all list comments

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a list. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, and most &#x60;replies&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let sort = "newest"; // String | how to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdListsListIdCommentsSortGet(id, listId, sort, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
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


## usersIdListsListIdLikesGet

> usersIdListsListIdLikesGet(id, listId, opts)

Get all users who liked a list

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination  Returns all users who liked a list.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let listId = "star-wars-in-machete-order"; // String | Trakt ID or Trakt slug
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdListsListIdLikesGet(id, listId, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **listId** | **String**| Trakt ID or Trakt slug | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdRatingsTypeRatingGet

> usersIdRatingsTypeRatingGet(id, type, rating, opts)

Get ratings

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info  Get a user&#39;s ratings filtered by &#x60;type&#x60;. You can optionally filter for a specific &#x60;rating&#x60; between 1 and 10. Send a comma separated string for &#x60;rating&#x60; if you need multiple ratings.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "movies"; // String | 
let rating = 9; // Number | Filter for a specific rating.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdRatingsTypeRatingGet(id, type, rating, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**|  | 
 **rating** | **Number**| Filter for a specific rating. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdRecommendationsTypeSortGet

> usersIdRecommendationsTypeSortGet(id, type, sort, opts)

Get personal recommendations

#### &amp;#128274; OAuth Required &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns the top 50 items a user personally recommendeds to others. These recommendations are used to enchance Trakt&#39;s social recommendation algorithm. Apps should encourage user&#39;s to build their personal recommendations so the algorithm keeps getting better.  #### Notes  Each recommendation contains a &#x60;notes&#x60; field explaining why the user recommended the item.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "movies"; // String | Filter for a specific item type
let sort = "rank"; // String | How to sort (only if type is also sent)
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdRecommendationsTypeSortGet(id, type, sort, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**| Filter for a specific item type | 
 **sort** | **String**| How to sort (only if type is also sent) | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdWatchedTypeGet

> usersIdWatchedTypeGet(id, type, opts)

Get watched

#### &amp;#128275; OAuth Optional &amp;#10024; Extended Info  Returns all movies or shows a user has watched sorted by most plays.  If &#x60;type&#x60; is set to _shows_ and you add &#x60;?extended&#x3D;noseasons&#x60; to the URL, it won&#39;t return season or episode info.  Each &#x60;movie&#x60; and &#x60;show&#x60; object contains &#x60;last_watched_at&#x60; and &#x60;last_updated_at&#x60; timestamps. Since users can set custom dates when they watched movies and episodes, it is possible for &#x60;last_watched_at&#x60; to be in the past. We also include &#x60;last_updated_at&#x60; to help sync Trakt data with your app. Cache this timestamp locally and only re-process the movies and shows if you see a newer timestamp.  Each &#x60;show&#x60; object contains a &#x60;reset_at&#x60; timestamp. If not &#x60;null&#x60;, this is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "movies"; // String | 
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdWatchedTypeGet(id, type, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**|  | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdWatchlistTypeSortGet

> usersIdWatchlistTypeSortGet(id, type, sort, opts)

Get watchlist

#### &amp;#128275; OAuth Optional &amp;#128196; Pagination Optional &amp;#10024; Extended Info &amp;#128513; Emojis  Returns all items in a user&#39;s watchlist filtered by type.  #### Notes  Each watchlist item contains a &#x60;notes&#x60; field with text entered by the user.  #### Sorting Headers  By default, all list items are sorted by &#x60;rank&#x60; &#x60;asc&#x60;. We send &#x60;X-Applied-Sort-By&#x60; and &#x60;X-Applied-Sort-How&#x60; headers to indicate how the results are actually being sorted.  We also send &#x60;X-Sort-By&#x60; and &#x60;X-Sort-How&#x60; headers which indicate the user&#39;s sort preference. Use these to to custom sort the watchlist _**in your app**_ for more advanced sort abilities we can&#39;t do in the API. Values for &#x60;X-Sort-By&#x60; include &#x60;rank&#x60;, &#x60;added&#x60;, &#x60;title&#x60;, &#x60;released&#x60;, &#x60;runtime&#x60;, &#x60;popularity&#x60;, &#x60;percentage&#x60;, and &#x60;votes&#x60;. Values for &#x60;X-Sort-How&#x60; include &#x60;asc&#x60; and &#x60;desc&#x60;.  #### Auto Removal  When an item is watched, it will be automatically removed from the watchlist. For shows and seasons, watching 1 episode will remove the entire show or season.  _**The watchlist should not be used as a list of what the user is actively watching.**_  Use a combination of the [**_/sync/watched**](/reference/sync/get-watched) and [**_/shows/:id/progress**](/reference/shows/watched-progress) methods to get what the user is actively watching.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.UsersApi();
let id = "sean"; // String | User slug
let type = "movies"; // String | Filter for a specific item type
let sort = "rank"; // String | How to sort (only if type is also sent)
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.usersIdWatchlistTypeSortGet(id, type, sort, opts, (error, data, response) => {
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
 **id** | **String**| User slug | 
 **type** | **String**| Filter for a specific item type | 
 **sort** | **String**| How to sort (only if type is also sent) | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

