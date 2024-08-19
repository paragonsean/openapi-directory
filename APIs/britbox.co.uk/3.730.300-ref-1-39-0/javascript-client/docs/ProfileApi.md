# RocketServices.ProfileApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookmarkItem**](ProfileApi.md#bookmarkItem) | **PUT** /account/profile/bookmarks/{itemId} | 
[**deleteItemBookmark**](ProfileApi.md#deleteItemBookmark) | **DELETE** /account/profile/bookmarks/{itemId} | 
[**deleteWatched**](ProfileApi.md#deleteWatched) | **DELETE** /account/profile/watched | 
[**getBookmarkList**](ProfileApi.md#getBookmarkList) | **GET** /account/profile/bookmarks/list | 
[**getBookmarks**](ProfileApi.md#getBookmarks) | **GET** /account/profile/bookmarks | 
[**getContinueWatchingList**](ProfileApi.md#getContinueWatchingList) | **GET** /account/profile/continue-watching/list | 
[**getItemBookmark**](ProfileApi.md#getItemBookmark) | **GET** /account/profile/bookmarks/{itemId} | 
[**getItemRating**](ProfileApi.md#getItemRating) | **GET** /account/profile/ratings/{itemId} | 
[**getItemWatchedStatus**](ProfileApi.md#getItemWatchedStatus) | **GET** /account/profile/watched/{itemId} | 
[**getNextPlaybackItem**](ProfileApi.md#getNextPlaybackItem) | **GET** /account/profile/items/{itemId}/next | 
[**getProfile**](ProfileApi.md#getProfile) | **GET** /account/profile | 
[**getRatings**](ProfileApi.md#getRatings) | **GET** /account/profile/ratings | 
[**getRatingsList**](ProfileApi.md#getRatingsList) | **GET** /account/profile/ratings/list | 
[**getWatched**](ProfileApi.md#getWatched) | **GET** /account/profile/watched | 
[**getWatchedList**](ProfileApi.md#getWatchedList) | **GET** /account/profile/watched/list | 
[**rateItem**](ProfileApi.md#rateItem) | **PUT** /account/profile/ratings/{itemId} | 
[**setItemWatchedStatus**](ProfileApi.md#setItemWatchedStatus) | **PUT** /account/profile/watched/{itemId} | 



## bookmarkItem

> Bookmark bookmarkItem(itemId, opts)



Bookmark an item under the active profile.  Creates one if it doesn&#39;t exist, overwrites one if it does. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The id of the item to bookmark.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.bookmarkItem(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The id of the item to bookmark. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**Bookmark**](Bookmark.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteItemBookmark

> deleteItemBookmark(itemId, opts)



Unbookmark an item under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The identifier of the bookmark to delete.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.deleteItemBookmark(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The identifier of the bookmark to delete. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWatched

> deleteWatched(opts)



Remove the watched status of items under the active profile. Passing in specific &#x60;itemId&#x60;s to the &#x60;item_ids&#x60; query parameter will cause only these items to be removed. **If this list is missing all watched items will be removed** 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'itemIds': ["null"], // [String] | List of `itemId`s to delete. Omit this parameter to delete all items 
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.deleteWatched(opts, (error, data, response) => {
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
 **itemIds** | [**[String]**](String.md)| List of &#x60;itemId&#x60;s to delete. Omit this parameter to delete all items  | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

null (empty response body)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBookmarkList

> ItemList getBookmarkList(opts)



Returns the list of bookmarked items under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'page': 56, // Number | The page of items to load. Starts from page 1.
  'pageSize': 56, // Number | The number of items to return in a page.
  'order': "'desc'", // String | The list sort order, either 'asc' or 'desc'.
  'itemType': "itemType_example", // String | The item type to filter by. Defaults to unspecified.
  'device': "'web_browser'", // String | The type of device the content is targeting.
  'sub': "sub_example", // String | The active subscription code.
  'segments': ["null"], // [String] | The list of segments to filter the response by.
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getBookmarkList(opts, (error, data, response) => {
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
 **page** | **Number**| The page of items to load. Starts from page 1. | [optional] 
 **pageSize** | **Number**| The number of items to return in a page. | [optional] 
 **order** | **String**| The list sort order, either &#39;asc&#39; or &#39;desc&#39;. | [optional] [default to &#39;desc&#39;]
 **itemType** | **String**| The item type to filter by. Defaults to unspecified. | [optional] 
 **device** | **String**| The type of device the content is targeting. | [optional] [default to &#39;web_browser&#39;]
 **sub** | **String**| The active subscription code. | [optional] 
 **segments** | [**[String]**](String.md)| The list of segments to filter the response by. | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItemList**](ItemList.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBookmarks

> {String: Date} getBookmarks(opts)



Get the map of bookmarked item ids (itemId &#x3D;&gt; creationDate) under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getBookmarks(opts, (error, data, response) => {
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
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

**{String: Date}**

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContinueWatchingList

> ItemList getContinueWatchingList(opts)



Returns a list of items which have been watched but not completed under the active profile.  Multiple episodes under the same show may be watched or in progress, however only a single item belonging to a particular show will be included in the returned list.  The next episode to continue watching for a particular show will be the most recent incompletely watched episode, or the next episode following the most recently completely watched episode. Based on the specified &#x60;show_item_type&#x60; type, either the next episode, the season of the next episode, or the show will be included in the list. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'showItemType': "'episode'", // String | The item type to be returned for continue watching items belonging to a show.  Multiple episodes under the same show may be watched or in progress, however only a single item belonging to a particular show will be included in the returned list.  The next episode to continue watching for a particular show will be the most recent incompletely watched episode, or the next episode following the most recently completely watched episode. Based on the specified `show_item_type` type, either the next episode, the season of the next episode, or the show will be included in the list.  If `episode` is specified, then only the next episode to continue watching for a show will be returned.  If `season` is specified, then only the season of the next episode will be returned.  If `show` is specified, then only the show of the next episode will be returned  The recommended value of this parameter should reflect the desitination the user will be sent to when they select this item in the list. So if a user will be sent to the show detail page then this should be `show` and you can use the `include` parameter to get metadata about the episode or season if needed 
  'include': ["null"], // [String] | Include one opr more ancestor/children for items belonging to a show. Extra items will be populated in the `listData` property of the list  If no value is specified no dependencies are included.  If `episode` is specified, then the next episode will be added for season/show items. Has no effect if `show_item_type` is set to `episode`.  If `season` is specified, then the season of the next episode will be added for episode/show items. Has no effect if `show_item_type` is set to `season`.  If `show` is specified, then the show of the next episode will be added for episode/season items. Has no effect if `show_item_type` is set to `show`. 
  'page': 1, // Number | The page of items to load. Starts from page 1.
  'pageSize': 12, // Number | The number of items to return in a page.
  'maxRating': "maxRating_example", // String | The maximum rating (inclusive) of an item returned, e.g. 'auoflc-pg'.
  'device': "'web_browser'", // String | The type of device the content is targeting.
  'sub': "sub_example", // String | The active subscription code.
  'segments': ["null"], // [String] | The list of segments to filter the response by.
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getContinueWatchingList(opts, (error, data, response) => {
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
 **showItemType** | **String**| The item type to be returned for continue watching items belonging to a show.  Multiple episodes under the same show may be watched or in progress, however only a single item belonging to a particular show will be included in the returned list.  The next episode to continue watching for a particular show will be the most recent incompletely watched episode, or the next episode following the most recently completely watched episode. Based on the specified &#x60;show_item_type&#x60; type, either the next episode, the season of the next episode, or the show will be included in the list.  If &#x60;episode&#x60; is specified, then only the next episode to continue watching for a show will be returned.  If &#x60;season&#x60; is specified, then only the season of the next episode will be returned.  If &#x60;show&#x60; is specified, then only the show of the next episode will be returned  The recommended value of this parameter should reflect the desitination the user will be sent to when they select this item in the list. So if a user will be sent to the show detail page then this should be &#x60;show&#x60; and you can use the &#x60;include&#x60; parameter to get metadata about the episode or season if needed  | [optional] [default to &#39;episode&#39;]
 **include** | [**[String]**](String.md)| Include one opr more ancestor/children for items belonging to a show. Extra items will be populated in the &#x60;listData&#x60; property of the list  If no value is specified no dependencies are included.  If &#x60;episode&#x60; is specified, then the next episode will be added for season/show items. Has no effect if &#x60;show_item_type&#x60; is set to &#x60;episode&#x60;.  If &#x60;season&#x60; is specified, then the season of the next episode will be added for episode/show items. Has no effect if &#x60;show_item_type&#x60; is set to &#x60;season&#x60;.  If &#x60;show&#x60; is specified, then the show of the next episode will be added for episode/season items. Has no effect if &#x60;show_item_type&#x60; is set to &#x60;show&#x60;.  | [optional] 
 **page** | **Number**| The page of items to load. Starts from page 1. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return in a page. | [optional] [default to 12]
 **maxRating** | **String**| The maximum rating (inclusive) of an item returned, e.g. &#39;auoflc-pg&#39;. | [optional] 
 **device** | **String**| The type of device the content is targeting. | [optional] [default to &#39;web_browser&#39;]
 **sub** | **String**| The active subscription code. | [optional] 
 **segments** | [**[String]**](String.md)| The list of segments to filter the response by. | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItemList**](ItemList.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemBookmark

> Bookmark getItemBookmark(itemId, opts)



Get the bookmark for an item under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The id of the item to get the bookmark for.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getItemBookmark(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The id of the item to get the bookmark for. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**Bookmark**](Bookmark.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemRating

> UserRating getItemRating(itemId, opts)



Get the rating info for an item under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The id of the item to get the rating info for.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getItemRating(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The id of the item to get the rating info for. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**UserRating**](UserRating.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getItemWatchedStatus

> Watched getItemWatchedStatus(itemId, opts)



Get the watched status info for an item under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The id of the item to get the watched status for.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getItemWatchedStatus(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The id of the item to get the watched status for. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**Watched**](Watched.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNextPlaybackItem

> NextPlaybackItem getNextPlaybackItem(itemId, opts)



Returns the next item to play given a source item id.  For an unwatched show it returns the first episode available to the account.  For a watched show it returns the last incompletely watched episode by the profile, or the episode that immediately follows the last completely watched episode  or nothing.  For an episode it always returns the immediately following episode, if available to the account, or nothing.  If the response does not contain a &#x60;next&#x60; property then no item was found. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The identifier of the source item to base the next to watch item off. 
let opts = {
  'maxRating': "maxRating_example", // String | The maximum rating (inclusive) of an item returned, e.g. 'auoflc-pg'.
  'expand': "expand_example", // String | If no value is specified no dependencies are expanded.  If 'parent' is specified then only the direct parent will be expanded. For example if an `Episode` then the `Season` would be included.  If 'ancestors' is specified then the full parent chain is expanded. For example if an `Episode` then both the `Season` and `Show` would be included. 
  'device': "'web_browser'", // String | The type of device the content is targeting.
  'sub': "sub_example", // String | The active subscription code.
  'segments': ["null"], // [String] | The list of segments to filter the response by.
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getNextPlaybackItem(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The identifier of the source item to base the next to watch item off.  | 
 **maxRating** | **String**| The maximum rating (inclusive) of an item returned, e.g. &#39;auoflc-pg&#39;. | [optional] 
 **expand** | **String**| If no value is specified no dependencies are expanded.  If &#39;parent&#39; is specified then only the direct parent will be expanded. For example if an &#x60;Episode&#x60; then the &#x60;Season&#x60; would be included.  If &#39;ancestors&#39; is specified then the full parent chain is expanded. For example if an &#x60;Episode&#x60; then both the &#x60;Season&#x60; and &#x60;Show&#x60; would be included.  | [optional] 
 **device** | **String**| The type of device the content is targeting. | [optional] [default to &#39;web_browser&#39;]
 **sub** | **String**| The active subscription code. | [optional] 
 **segments** | [**[String]**](String.md)| The list of segments to filter the response by. | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**NextPlaybackItem**](NextPlaybackItem.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfile

> ProfileDetail getProfile(opts)



Get the details of the active profile, including watched, bookmarked and rated items.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getProfile(opts, (error, data, response) => {
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
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ProfileDetail**](ProfileDetail.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRatings

> {String: Number} getRatings(opts)



Get the map of rated item ids (itemId &#x3D;&gt; rating out of 10) under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getRatings(opts, (error, data, response) => {
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
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

**{String: Number}**

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRatingsList

> ItemList getRatingsList(opts)



Returns the list of rated items under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'page': 1, // Number | The page of items to load. Starts from page 1.
  'pageSize': 12, // Number | The number of items to return in a page.
  'order': "'desc'", // String | The list sort order, either 'asc' or 'desc'.
  'orderBy': "'date-added'", // String | What to order by.  Ordering by `date-modified` equates to ordering by the last rated date. 
  'itemType': "itemType_example", // String | The item type to filter by. Defaults to unspecified.
  'device': "'web_browser'", // String | The type of device the content is targeting.
  'sub': "sub_example", // String | The active subscription code.
  'segments': ["null"], // [String] | The list of segments to filter the response by.
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getRatingsList(opts, (error, data, response) => {
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
 **page** | **Number**| The page of items to load. Starts from page 1. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return in a page. | [optional] [default to 12]
 **order** | **String**| The list sort order, either &#39;asc&#39; or &#39;desc&#39;. | [optional] [default to &#39;desc&#39;]
 **orderBy** | **String**| What to order by.  Ordering by &#x60;date-modified&#x60; equates to ordering by the last rated date.  | [optional] [default to &#39;date-added&#39;]
 **itemType** | **String**| The item type to filter by. Defaults to unspecified. | [optional] 
 **device** | **String**| The type of device the content is targeting. | [optional] [default to &#39;web_browser&#39;]
 **sub** | **String**| The active subscription code. | [optional] 
 **segments** | [**[String]**](String.md)| The list of segments to filter the response by. | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItemList**](ItemList.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWatched

> {String: Watched} getWatched(opts)



Get the map of watched item ids (itemId &#x3D;&gt; last playhead position) under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getWatched(opts, (error, data, response) => {
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
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**{String: Watched}**](Watched.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWatchedList

> ItemList getWatchedList(opts)



Returns the list of watched items under the active profile.

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let opts = {
  'page': 1, // Number | The page of items to load. Starts from page 1.
  'pageSize': 12, // Number | The number of items to return in a page.
  'completed': true, // Boolean | Filter by whether an item has been fully watched (completed) or not.  If `undefined` then both partially and fully watched items are returned. 
  'order': "'desc'", // String | The list sort order, either 'asc' or 'desc'.
  'orderBy': "'date-added'", // String | What to order by.  Ordering by `date-modified` equates to ordering by the last watched date. 
  'itemType': "itemType_example", // String | The item type to filter by. Defaults to unspecified.
  'device': "'web_browser'", // String | The type of device the content is targeting.
  'sub': "sub_example", // String | The active subscription code.
  'segments': ["null"], // [String] | The list of segments to filter the response by.
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.getWatchedList(opts, (error, data, response) => {
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
 **page** | **Number**| The page of items to load. Starts from page 1. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return in a page. | [optional] [default to 12]
 **completed** | **Boolean**| Filter by whether an item has been fully watched (completed) or not.  If &#x60;undefined&#x60; then both partially and fully watched items are returned.  | [optional] 
 **order** | **String**| The list sort order, either &#39;asc&#39; or &#39;desc&#39;. | [optional] [default to &#39;desc&#39;]
 **orderBy** | **String**| What to order by.  Ordering by &#x60;date-modified&#x60; equates to ordering by the last watched date.  | [optional] [default to &#39;date-added&#39;]
 **itemType** | **String**| The item type to filter by. Defaults to unspecified. | [optional] 
 **device** | **String**| The type of device the content is targeting. | [optional] [default to &#39;web_browser&#39;]
 **sub** | **String**| The active subscription code. | [optional] 
 **segments** | [**[String]**](String.md)| The list of segments to filter the response by. | [optional] 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**ItemList**](ItemList.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rateItem

> UserRating rateItem(itemId, rating, opts)



Rate an item under the active profile.  Creates one if it doesn&#39;t exist, overwrites one if it does. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The id of the item to rate.
let rating = 56; // Number | The item rating between 1 and 10 inclusive.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.rateItem(itemId, rating, opts, (error, data, response) => {
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
 **itemId** | **String**| The id of the item to rate. | 
 **rating** | **Number**| The item rating between 1 and 10 inclusive. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**UserRating**](UserRating.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setItemWatchedStatus

> Watched setItemWatchedStatus(itemId, position, opts)



Record the watched playhead position of a video under the active profile.  Can be used later to resume a video from where it was last watched.  Creates one if it doesn&#39;t exist, overwrites one if it does. 

### Example

```javascript
import RocketServices from 'rocket_services';
let defaultClient = RocketServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: profileAuth
let profileAuth = defaultClient.authentications['profileAuth'];
profileAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RocketServices.ProfileApi();
let itemId = "itemId_example"; // String | The id of the item being watched.
let position = 56; // Number | The playhead position to record.
let opts = {
  'ff': ["null"], // [String] | The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - `all` - Enable all flags. Useful for testing. _Don't use in production_. - `idp` - Dynamic item detail pages with schedulable rows. - `ldp` - Dynamic list detail pages with schedulable rows. - `hb` - Hubble formatted image urls. - `rpt` - Updated resume point threshold logic. - `cas` - \"Custom Asset Search\", inlcude `customAssets` in search results. - `lrl` - Do not pre-populate related list if more than `max_list_prefetch` down the page. - `cd` - Custom Destination support.  See the `feature-flags.md` for available flag details. 
  'lang': "lang_example" // String | Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to 'en', unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
};
apiInstance.setItemWatchedStatus(itemId, position, opts, (error, data, response) => {
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
 **itemId** | **String**| The id of the item being watched. | 
 **position** | **Number**| The playhead position to record. | 
 **ff** | [**[String]**](String.md)| The set of opt in feature flags which cause breaking changes to responses.  While Rocket APIs look to avoid breaking changes under the active major version, the formats of responses may need to evolve over this time.  These feature flags allow clients to select which response formats they expect and avoid breaking clients as these formats evolve under the current major version.  ### Flags  - &#x60;all&#x60; - Enable all flags. Useful for testing. _Don&#39;t use in production_. - &#x60;idp&#x60; - Dynamic item detail pages with schedulable rows. - &#x60;ldp&#x60; - Dynamic list detail pages with schedulable rows. - &#x60;hb&#x60; - Hubble formatted image urls. - &#x60;rpt&#x60; - Updated resume point threshold logic. - &#x60;cas&#x60; - \&quot;Custom Asset Search\&quot;, inlcude &#x60;customAssets&#x60; in search results. - &#x60;lrl&#x60; - Do not pre-populate related list if more than &#x60;max_list_prefetch&#x60; down the page. - &#x60;cd&#x60; - Custom Destination support.  See the &#x60;feature-flags.md&#x60; for available flag details.  | [optional] 
 **lang** | **String**| Language code for the preferred language to be returned in the response.  Parameter value is case-insensitive and should be   - a valid 2 letter language code without region such as en, de   - or with region such as en_us, en_au  If undefined then defaults to &#39;en&#39;, unless the server has been configured with a custom default.  See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  | [optional] 

### Return type

[**Watched**](Watched.md)

### Authorization

[profileAuth](../README.md#profileAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

