# JellyfinApi.ImageApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteItemImage**](ImageApi.md#deleteItemImage) | **DELETE** /Items/{itemId}/Images/{imageType} | Delete an item&#39;s image.
[**deleteItemImageByIndex**](ImageApi.md#deleteItemImageByIndex) | **DELETE** /Items/{itemId}/Images/{imageType}/{imageIndex} | Delete an item&#39;s image.
[**deleteUserImage**](ImageApi.md#deleteUserImage) | **DELETE** /Users/{userId}/Images/{imageType} | Delete the user&#39;s image.
[**deleteUserImageByIndex**](ImageApi.md#deleteUserImageByIndex) | **DELETE** /Users/{userId}/Images/{imageType}/{index} | Delete the user&#39;s image.
[**getArtistImage**](ImageApi.md#getArtistImage) | **GET** /Artists/{name}/Images/{imageType}/{imageIndex} | Get artist image by name.
[**getGenreImage**](ImageApi.md#getGenreImage) | **GET** /Genres/{name}/Images/{imageType} | Get genre image by name.
[**getGenreImageByIndex**](ImageApi.md#getGenreImageByIndex) | **GET** /Genres/{name}/Images/{imageType}/{imageIndex} | Get genre image by name.
[**getItemImage**](ImageApi.md#getItemImage) | **GET** /Items/{itemId}/Images/{imageType} | Gets the item&#39;s image.
[**getItemImage2**](ImageApi.md#getItemImage2) | **GET** /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount} | Gets the item&#39;s image.
[**getItemImageByIndex**](ImageApi.md#getItemImageByIndex) | **GET** /Items/{itemId}/Images/{imageType}/{imageIndex} | Gets the item&#39;s image.
[**getItemImageInfos**](ImageApi.md#getItemImageInfos) | **GET** /Items/{itemId}/Images | Get item image infos.
[**getMusicGenreImage**](ImageApi.md#getMusicGenreImage) | **GET** /MusicGenres/{name}/Images/{imageType} | Get music genre image by name.
[**getMusicGenreImageByIndex**](ImageApi.md#getMusicGenreImageByIndex) | **GET** /MusicGenres/{name}/Images/{imageType}/{imageIndex} | Get music genre image by name.
[**getPersonImage**](ImageApi.md#getPersonImage) | **GET** /Persons/{name}/Images/{imageType} | Get person image by name.
[**getPersonImageByIndex**](ImageApi.md#getPersonImageByIndex) | **GET** /Persons/{name}/Images/{imageType}/{imageIndex} | Get person image by name.
[**getStudioImage**](ImageApi.md#getStudioImage) | **GET** /Studios/{name}/Images/{imageType} | Get studio image by name.
[**getStudioImageByIndex**](ImageApi.md#getStudioImageByIndex) | **GET** /Studios/{name}/Images/{imageType}/{imageIndex} | Get studio image by name.
[**getUserImage**](ImageApi.md#getUserImage) | **GET** /Users/{userId}/Images/{imageType} | Get user profile image.
[**getUserImageByIndex**](ImageApi.md#getUserImageByIndex) | **GET** /Users/{userId}/Images/{imageType}/{imageIndex} | Get user profile image.
[**headArtistImage**](ImageApi.md#headArtistImage) | **HEAD** /Artists/{name}/Images/{imageType}/{imageIndex} | Get artist image by name.
[**headGenreImage**](ImageApi.md#headGenreImage) | **HEAD** /Genres/{name}/Images/{imageType} | Get genre image by name.
[**headGenreImageByIndex**](ImageApi.md#headGenreImageByIndex) | **HEAD** /Genres/{name}/Images/{imageType}/{imageIndex} | Get genre image by name.
[**headItemImage**](ImageApi.md#headItemImage) | **HEAD** /Items/{itemId}/Images/{imageType} | Gets the item&#39;s image.
[**headItemImage2**](ImageApi.md#headItemImage2) | **HEAD** /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount} | Gets the item&#39;s image.
[**headItemImageByIndex**](ImageApi.md#headItemImageByIndex) | **HEAD** /Items/{itemId}/Images/{imageType}/{imageIndex} | Gets the item&#39;s image.
[**headMusicGenreImage**](ImageApi.md#headMusicGenreImage) | **HEAD** /MusicGenres/{name}/Images/{imageType} | Get music genre image by name.
[**headMusicGenreImageByIndex**](ImageApi.md#headMusicGenreImageByIndex) | **HEAD** /MusicGenres/{name}/Images/{imageType}/{imageIndex} | Get music genre image by name.
[**headPersonImage**](ImageApi.md#headPersonImage) | **HEAD** /Persons/{name}/Images/{imageType} | Get person image by name.
[**headPersonImageByIndex**](ImageApi.md#headPersonImageByIndex) | **HEAD** /Persons/{name}/Images/{imageType}/{imageIndex} | Get person image by name.
[**headStudioImage**](ImageApi.md#headStudioImage) | **HEAD** /Studios/{name}/Images/{imageType} | Get studio image by name.
[**headStudioImageByIndex**](ImageApi.md#headStudioImageByIndex) | **HEAD** /Studios/{name}/Images/{imageType}/{imageIndex} | Get studio image by name.
[**headUserImage**](ImageApi.md#headUserImage) | **HEAD** /Users/{userId}/Images/{imageType} | Get user profile image.
[**headUserImageByIndex**](ImageApi.md#headUserImageByIndex) | **HEAD** /Users/{userId}/Images/{imageType}/{imageIndex} | Get user profile image.
[**postUserImage**](ImageApi.md#postUserImage) | **POST** /Users/{userId}/Images/{imageType} | Sets the user image.
[**postUserImageByIndex**](ImageApi.md#postUserImageByIndex) | **POST** /Users/{userId}/Images/{imageType}/{index} | Sets the user image.
[**setItemImage**](ImageApi.md#setItemImage) | **POST** /Items/{itemId}/Images/{imageType} | Set item image.
[**setItemImageByIndex**](ImageApi.md#setItemImageByIndex) | **POST** /Items/{itemId}/Images/{imageType}/{imageIndex} | Set item image.
[**updateItemImageIndex**](ImageApi.md#updateItemImageIndex) | **POST** /Items/{itemId}/Images/{imageType}/{imageIndex}/Index | Updates the index for an item image.



## deleteItemImage

> deleteItemImage(itemId, imageType, opts)

Delete an item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'imageIndex': 56 // Number | The image index.
};
apiInstance.deleteItemImage(itemId, imageType, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| The image index. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## deleteItemImageByIndex

> deleteItemImageByIndex(itemId, imageType, imageIndex)

Delete an item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | The image index.
apiInstance.deleteItemImageByIndex(itemId, imageType, imageIndex, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| The image index. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## deleteUserImage

> deleteUserImage(userId, imageType, opts)

Delete the user&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User Id.
let imageType = new JellyfinApi.ImageType(); // ImageType | (Unused) Image type.
let opts = {
  'index': 56 // Number | (Unused) Image index.
};
apiInstance.deleteUserImage(userId, imageType, opts, (error, data, response) => {
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
 **userId** | **String**| User Id. | 
 **imageType** | [**ImageType**](.md)| (Unused) Image type. | 
 **index** | **Number**| (Unused) Image index. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## deleteUserImageByIndex

> deleteUserImageByIndex(userId, imageType, index)

Delete the user&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User Id.
let imageType = new JellyfinApi.ImageType(); // ImageType | (Unused) Image type.
let index = 56; // Number | (Unused) Image index.
apiInstance.deleteUserImageByIndex(userId, imageType, index, (error, data, response) => {
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
 **userId** | **String**| User Id. | 
 **imageType** | [**ImageType**](.md)| (Unused) Image type. | 
 **index** | **Number**| (Unused) Image index. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getArtistImage

> File getArtistImage(name, imageType, imageIndex, opts)

Get artist image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Artist name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getArtistImage(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Artist name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getGenreImage

> File getGenreImage(name, imageType, opts)

Get genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.getGenreImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getGenreImageByIndex

> File getGenreImageByIndex(name, imageType, imageIndex, opts)

Get genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getGenreImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItemImage

> File getItemImage(itemId, imageType, opts)

Gets the item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.getItemImage(itemId, imageType, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **format** | [**ImageFormat**](.md)| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItemImage2

> File getItemImage2(itemId, imageType, maxWidth, maxHeight, tag, format, percentPlayed, unplayedCount, imageIndex, opts)

Gets the item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let maxWidth = 56; // Number | The maximum image width to return.
let maxHeight = 56; // Number | The maximum image height to return.
let tag = "tag_example"; // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
let format = new JellyfinApi.ImageFormat(); // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
let percentPlayed = 3.4; // Number | Optional. Percent to render for the percent played overlay.
let unplayedCount = 56; // Number | Optional. Unplayed count overlay to render.
let imageIndex = 56; // Number | Image index.
let opts = {
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getItemImage2(itemId, imageType, maxWidth, maxHeight, tag, format, percentPlayed, unplayedCount, imageIndex, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **maxWidth** | **Number**| The maximum image width to return. | 
 **maxHeight** | **Number**| The maximum image height to return. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | 
 **imageIndex** | **Number**| Image index. | 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItemImageByIndex

> File getItemImageByIndex(itemId, imageType, imageIndex, opts)

Gets the item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getItemImageByIndex(itemId, imageType, imageIndex, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **format** | [**ImageFormat**](.md)| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItemImageInfos

> [ImageInfo] getItemImageInfos(itemId)

Get item image infos.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
apiInstance.getItemImageInfos(itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**[ImageInfo]**](ImageInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMusicGenreImage

> File getMusicGenreImage(name, imageType, opts)

Get music genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Music genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.getMusicGenreImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Music genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMusicGenreImageByIndex

> File getMusicGenreImageByIndex(name, imageType, imageIndex, opts)

Get music genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Music genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getMusicGenreImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Music genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPersonImage

> File getPersonImage(name, imageType, opts)

Get person image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Person name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.getPersonImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Person name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPersonImageByIndex

> File getPersonImageByIndex(name, imageType, imageIndex, opts)

Get person image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Person name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getPersonImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Person name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getStudioImage

> File getStudioImage(name, imageType, opts)

Get studio image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Studio name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.getStudioImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Studio name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getStudioImageByIndex

> File getStudioImageByIndex(name, imageType, imageIndex, opts)

Get studio image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Studio name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getStudioImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Studio name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getUserImage

> File getUserImage(userId, imageType, opts)

Get user profile image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.getUserImage(userId, imageType, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getUserImageByIndex

> File getUserImageByIndex(userId, imageType, imageIndex, opts)

Get user profile image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.getUserImageByIndex(userId, imageType, imageIndex, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headArtistImage

> File headArtistImage(name, imageType, imageIndex, opts)

Get artist image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Artist name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headArtistImage(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Artist name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headGenreImage

> File headGenreImage(name, imageType, opts)

Get genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.headGenreImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headGenreImageByIndex

> File headGenreImageByIndex(name, imageType, imageIndex, opts)

Get genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headGenreImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headItemImage

> File headItemImage(itemId, imageType, opts)

Gets the item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.headItemImage(itemId, imageType, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **format** | [**ImageFormat**](.md)| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headItemImage2

> File headItemImage2(itemId, imageType, maxWidth, maxHeight, tag, format, percentPlayed, unplayedCount, imageIndex, opts)

Gets the item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let maxWidth = 56; // Number | The maximum image width to return.
let maxHeight = 56; // Number | The maximum image height to return.
let tag = "tag_example"; // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
let format = new JellyfinApi.ImageFormat(); // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
let percentPlayed = 3.4; // Number | Optional. Percent to render for the percent played overlay.
let unplayedCount = 56; // Number | Optional. Unplayed count overlay to render.
let imageIndex = 56; // Number | Image index.
let opts = {
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headItemImage2(itemId, imageType, maxWidth, maxHeight, tag, format, percentPlayed, unplayedCount, imageIndex, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **maxWidth** | **Number**| The maximum image width to return. | 
 **maxHeight** | **Number**| The maximum image height to return. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | 
 **imageIndex** | **Number**| Image index. | 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headItemImageByIndex

> File headItemImageByIndex(itemId, imageType, imageIndex, opts)

Gets the item&#39;s image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headItemImageByIndex(itemId, imageType, imageIndex, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **format** | [**ImageFormat**](.md)| Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headMusicGenreImage

> File headMusicGenreImage(name, imageType, opts)

Get music genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Music genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.headMusicGenreImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Music genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headMusicGenreImageByIndex

> File headMusicGenreImageByIndex(name, imageType, imageIndex, opts)

Get music genre image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Music genre name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headMusicGenreImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Music genre name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headPersonImage

> File headPersonImage(name, imageType, opts)

Get person image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Person name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.headPersonImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Person name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headPersonImageByIndex

> File headPersonImageByIndex(name, imageType, imageIndex, opts)

Get person image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Person name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headPersonImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Person name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headStudioImage

> File headStudioImage(name, imageType, opts)

Get studio image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Studio name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.headStudioImage(name, imageType, opts, (error, data, response) => {
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
 **name** | **String**| Studio name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headStudioImageByIndex

> File headStudioImageByIndex(name, imageType, imageIndex, opts)

Get studio image by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let name = "name_example"; // String | Studio name.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headStudioImageByIndex(name, imageType, imageIndex, opts, (error, data, response) => {
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
 **name** | **String**| Studio name. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headUserImage

> File headUserImage(userId, imageType, opts)

Get user profile image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example", // String | Optional. Apply a foreground layer on top of the image.
  'imageIndex': 56 // Number | Image index.
};
apiInstance.headUserImage(userId, imageType, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 
 **imageIndex** | **Number**| Image index. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## headUserImageByIndex

> File headUserImageByIndex(userId, imageType, imageIndex, opts)

Get user profile image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Image index.
let opts = {
  'tag': "tag_example", // String | Optional. Supply the cache tag from the item object to receive strong caching headers.
  'format': new JellyfinApi.ImageFormat(), // ImageFormat | Determines the output format of the image - original,gif,jpg,png.
  'maxWidth': 56, // Number | The maximum image width to return.
  'maxHeight': 56, // Number | The maximum image height to return.
  'percentPlayed': 3.4, // Number | Optional. Percent to render for the percent played overlay.
  'unplayedCount': 56, // Number | Optional. Unplayed count overlay to render.
  'width': 56, // Number | The fixed image width to return.
  'height': 56, // Number | The fixed image height to return.
  'quality': 56, // Number | Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
  'cropWhitespace': true, // Boolean | Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
  'addPlayedIndicator': true, // Boolean | Optional. Add a played indicator.
  'blur': 56, // Number | Optional. Blur image.
  'backgroundColor': "backgroundColor_example", // String | Optional. Apply a background color for transparent images.
  'foregroundLayer': "foregroundLayer_example" // String | Optional. Apply a foreground layer on top of the image.
};
apiInstance.headUserImageByIndex(userId, imageType, imageIndex, opts, (error, data, response) => {
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
 **userId** | **String**| User id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Image index. | 
 **tag** | **String**| Optional. Supply the cache tag from the item object to receive strong caching headers. | [optional] 
 **format** | [**ImageFormat**](.md)| Determines the output format of the image - original,gif,jpg,png. | [optional] 
 **maxWidth** | **Number**| The maximum image width to return. | [optional] 
 **maxHeight** | **Number**| The maximum image height to return. | [optional] 
 **percentPlayed** | **Number**| Optional. Percent to render for the percent played overlay. | [optional] 
 **unplayedCount** | **Number**| Optional. Unplayed count overlay to render. | [optional] 
 **width** | **Number**| The fixed image width to return. | [optional] 
 **height** | **Number**| The fixed image height to return. | [optional] 
 **quality** | **Number**| Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases. | [optional] 
 **cropWhitespace** | **Boolean**| Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art. | [optional] 
 **addPlayedIndicator** | **Boolean**| Optional. Add a played indicator. | [optional] 
 **blur** | **Number**| Optional. Blur image. | [optional] 
 **backgroundColor** | **String**| Optional. Apply a background color for transparent images. | [optional] 
 **foregroundLayer** | **String**| Optional. Apply a foreground layer on top of the image. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## postUserImage

> postUserImage(userId, imageType, opts)

Sets the user image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User Id.
let imageType = new JellyfinApi.ImageType(); // ImageType | (Unused) Image type.
let opts = {
  'index': 56 // Number | (Unused) Image index.
};
apiInstance.postUserImage(userId, imageType, opts, (error, data, response) => {
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
 **userId** | **String**| User Id. | 
 **imageType** | [**ImageType**](.md)| (Unused) Image type. | 
 **index** | **Number**| (Unused) Image index. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## postUserImageByIndex

> postUserImageByIndex(userId, imageType, index)

Sets the user image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let userId = "userId_example"; // String | User Id.
let imageType = new JellyfinApi.ImageType(); // ImageType | (Unused) Image type.
let index = 56; // Number | (Unused) Image index.
apiInstance.postUserImageByIndex(userId, imageType, index, (error, data, response) => {
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
 **userId** | **String**| User Id. | 
 **imageType** | [**ImageType**](.md)| (Unused) Image type. | 
 **index** | **Number**| (Unused) Image index. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## setItemImage

> setItemImage(itemId, imageType)

Set item image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
apiInstance.setItemImage(itemId, imageType, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## setItemImageByIndex

> setItemImageByIndex(itemId, imageType, imageIndex)

Set item image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | (Unused) Image index.
apiInstance.setItemImageByIndex(itemId, imageType, imageIndex, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| (Unused) Image index. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updateItemImageIndex

> updateItemImageIndex(itemId, imageType, imageIndex, opts)

Updates the index for an item image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageApi();
let itemId = "itemId_example"; // String | Item id.
let imageType = new JellyfinApi.ImageType(); // ImageType | Image type.
let imageIndex = 56; // Number | Old image index.
let opts = {
  'newIndex': 56 // Number | New image index.
};
apiInstance.updateItemImageIndex(itemId, imageType, imageIndex, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **imageType** | [**ImageType**](.md)| Image type. | 
 **imageIndex** | **Number**| Old image index. | 
 **newIndex** | **Number**| New image index. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

