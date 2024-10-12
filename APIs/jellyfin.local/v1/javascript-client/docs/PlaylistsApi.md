# JellyfinApi.PlaylistsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addToPlaylist**](PlaylistsApi.md#addToPlaylist) | **POST** /Playlists/{playlistId}/Items | Adds items to a playlist.
[**createPlaylist**](PlaylistsApi.md#createPlaylist) | **POST** /Playlists | Creates a new playlist.
[**getPlaylistItems**](PlaylistsApi.md#getPlaylistItems) | **GET** /Playlists/{playlistId}/Items | Gets the original items of a playlist.
[**moveItem**](PlaylistsApi.md#moveItem) | **POST** /Playlists/{playlistId}/Items/{itemId}/Move/{newIndex} | Moves a playlist item.
[**removeFromPlaylist**](PlaylistsApi.md#removeFromPlaylist) | **DELETE** /Playlists/{playlistId}/Items | Removes items from a playlist.



## addToPlaylist

> addToPlaylist(playlistId, opts)

Adds items to a playlist.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaylistsApi();
let playlistId = "playlistId_example"; // String | The playlist id.
let opts = {
  'ids': ["null"], // [String] | Item id, comma delimited.
  'userId': "userId_example" // String | The userId.
};
apiInstance.addToPlaylist(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**| The playlist id. | 
 **ids** | [**[String]**](String.md)| Item id, comma delimited. | [optional] 
 **userId** | **String**| The userId. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createPlaylist

> PlaylistCreationResult createPlaylist(opts)

Creates a new playlist.

For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaylistsApi();
let opts = {
  'name': "name_example", // String | The playlist name.
  'ids': ["null"], // [String] | The item ids.
  'userId': "userId_example", // String | The user id.
  'mediaType': "mediaType_example", // String | The media type.
  'createPlaylistDto': new JellyfinApi.CreatePlaylistDto() // CreatePlaylistDto | The create playlist payload.
};
apiInstance.createPlaylist(opts, (error, data, response) => {
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
 **name** | **String**| The playlist name. | [optional] 
 **ids** | [**[String]**](String.md)| The item ids. | [optional] 
 **userId** | **String**| The user id. | [optional] 
 **mediaType** | **String**| The media type. | [optional] 
 **createPlaylistDto** | [**CreatePlaylistDto**](CreatePlaylistDto.md)| The create playlist payload. | [optional] 

### Return type

[**PlaylistCreationResult**](PlaylistCreationResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPlaylistItems

> BaseItemDtoQueryResult getPlaylistItems(playlistId, userId, opts)

Gets the original items of a playlist.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaylistsApi();
let playlistId = "playlistId_example"; // String | The playlist id.
let userId = "userId_example"; // String | User id.
let opts = {
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getPlaylistItems(playlistId, userId, opts, (error, data, response) => {
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
 **playlistId** | **String**| The playlist id. | 
 **userId** | **String**| User id. | 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## moveItem

> moveItem(playlistId, itemId, newIndex)

Moves a playlist item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaylistsApi();
let playlistId = "playlistId_example"; // String | The playlist id.
let itemId = "itemId_example"; // String | The item id.
let newIndex = 56; // Number | The new index.
apiInstance.moveItem(playlistId, itemId, newIndex, (error, data, response) => {
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
 **playlistId** | **String**| The playlist id. | 
 **itemId** | **String**| The item id. | 
 **newIndex** | **Number**| The new index. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeFromPlaylist

> removeFromPlaylist(playlistId, opts)

Removes items from a playlist.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.PlaylistsApi();
let playlistId = "playlistId_example"; // String | The playlist id.
let opts = {
  'entryIds': ["null"] // [String] | The item ids, comma delimited.
};
apiInstance.removeFromPlaylist(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**| The playlist id. | 
 **entryIds** | [**[String]**](String.md)| The item ids, comma delimited. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

