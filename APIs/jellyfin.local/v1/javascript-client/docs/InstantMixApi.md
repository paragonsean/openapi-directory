# JellyfinApi.InstantMixApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInstantMixFromAlbum**](InstantMixApi.md#getInstantMixFromAlbum) | **GET** /Albums/{id}/InstantMix | Creates an instant playlist based on a given song.
[**getInstantMixFromArtists**](InstantMixApi.md#getInstantMixFromArtists) | **GET** /Artists/{id}/InstantMix | Creates an instant playlist based on a given song.
[**getInstantMixFromItem**](InstantMixApi.md#getInstantMixFromItem) | **GET** /Items/{id}/InstantMix | Creates an instant playlist based on a given song.
[**getInstantMixFromMusicGenre**](InstantMixApi.md#getInstantMixFromMusicGenre) | **GET** /MusicGenres/{name}/InstantMix | Creates an instant playlist based on a given song.
[**getInstantMixFromMusicGenres**](InstantMixApi.md#getInstantMixFromMusicGenres) | **GET** /MusicGenres/{id}/InstantMix | Creates an instant playlist based on a given song.
[**getInstantMixFromPlaylist**](InstantMixApi.md#getInstantMixFromPlaylist) | **GET** /Playlists/{id}/InstantMix | Creates an instant playlist based on a given song.
[**getInstantMixFromSong**](InstantMixApi.md#getInstantMixFromSong) | **GET** /Songs/{id}/InstantMix | Creates an instant playlist based on a given song.



## getInstantMixFromAlbum

> BaseItemDtoQueryResult getInstantMixFromAlbum(id, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let id = "id_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromAlbum(id, opts, (error, data, response) => {
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
 **id** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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


## getInstantMixFromArtists

> BaseItemDtoQueryResult getInstantMixFromArtists(id, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let id = "id_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromArtists(id, opts, (error, data, response) => {
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
 **id** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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


## getInstantMixFromItem

> BaseItemDtoQueryResult getInstantMixFromItem(id, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let id = "id_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromItem(id, opts, (error, data, response) => {
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
 **id** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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


## getInstantMixFromMusicGenre

> BaseItemDtoQueryResult getInstantMixFromMusicGenre(name, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let name = "name_example"; // String | The genre name.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromMusicGenre(name, opts, (error, data, response) => {
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
 **name** | **String**| The genre name. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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


## getInstantMixFromMusicGenres

> BaseItemDtoQueryResult getInstantMixFromMusicGenres(id, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let id = "id_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromMusicGenres(id, opts, (error, data, response) => {
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
 **id** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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


## getInstantMixFromPlaylist

> BaseItemDtoQueryResult getInstantMixFromPlaylist(id, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let id = "id_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromPlaylist(id, opts, (error, data, response) => {
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
 **id** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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


## getInstantMixFromSong

> BaseItemDtoQueryResult getInstantMixFromSong(id, opts)

Creates an instant playlist based on a given song.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.InstantMixApi();
let id = "id_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()] // [ImageType] | Optional. The image types to include in the output.
};
apiInstance.getInstantMixFromSong(id, opts, (error, data, response) => {
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
 **id** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
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

