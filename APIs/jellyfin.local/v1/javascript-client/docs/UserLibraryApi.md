# JellyfinApi.UserLibraryApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserItemRating**](UserLibraryApi.md#deleteUserItemRating) | **DELETE** /Users/{userId}/Items/{itemId}/Rating | Deletes a user&#39;s saved personal rating for an item.
[**getIntros**](UserLibraryApi.md#getIntros) | **GET** /Users/{userId}/Items/{itemId}/Intros | Gets intros to play before the main media item plays.
[**getItem**](UserLibraryApi.md#getItem) | **GET** /Users/{userId}/Items/{itemId} | Gets an item from a user&#39;s library.
[**getLatestMedia**](UserLibraryApi.md#getLatestMedia) | **GET** /Users/{userId}/Items/Latest | Gets latest media.
[**getLocalTrailers**](UserLibraryApi.md#getLocalTrailers) | **GET** /Users/{userId}/Items/{itemId}/LocalTrailers | Gets local trailers for an item.
[**getRootFolder**](UserLibraryApi.md#getRootFolder) | **GET** /Users/{userId}/Items/Root | Gets the root folder from a user&#39;s library.
[**getSpecialFeatures**](UserLibraryApi.md#getSpecialFeatures) | **GET** /Users/{userId}/Items/{itemId}/SpecialFeatures | Gets special features for an item.
[**markFavoriteItem**](UserLibraryApi.md#markFavoriteItem) | **POST** /Users/{userId}/FavoriteItems/{itemId} | Marks an item as a favorite.
[**unmarkFavoriteItem**](UserLibraryApi.md#unmarkFavoriteItem) | **DELETE** /Users/{userId}/FavoriteItems/{itemId} | Unmarks item as a favorite.
[**updateUserItemRating**](UserLibraryApi.md#updateUserItemRating) | **POST** /Users/{userId}/Items/{itemId}/Rating | Updates a user&#39;s rating for an item.



## deleteUserItemRating

> UserItemDataDto deleteUserItemRating(userId, itemId)

Deletes a user&#39;s saved personal rating for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.deleteUserItemRating(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getIntros

> BaseItemDtoQueryResult getIntros(userId, itemId)

Gets intros to play before the main media item plays.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.getIntros(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItem

> BaseItemDto getItem(userId, itemId)

Gets an item from a user&#39;s library.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.getItem(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLatestMedia

> [BaseItemDto] getLatestMedia(userId, opts)

Gets latest media.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let opts = {
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'isPlayed': true, // Boolean | Filter by items that are played, or not.
  'enableImages': true, // Boolean | Optional. include image information in output.
  'imageTypeLimit': 56, // Number | Optional. the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'enableUserData': true, // Boolean | Optional. include user data.
  'limit': 20, // Number | Return item limit.
  'groupItems': true // Boolean | Whether or not to group items into a parent container.
};
apiInstance.getLatestMedia(userId, opts, (error, data, response) => {
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
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **isPlayed** | **Boolean**| Filter by items that are played, or not. | [optional] 
 **enableImages** | **Boolean**| Optional. include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. include user data. | [optional] 
 **limit** | **Number**| Return item limit. | [optional] [default to 20]
 **groupItems** | **Boolean**| Whether or not to group items into a parent container. | [optional] [default to true]

### Return type

[**[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLocalTrailers

> [BaseItemDto] getLocalTrailers(userId, itemId)

Gets local trailers for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.getLocalTrailers(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRootFolder

> BaseItemDto getRootFolder(userId)

Gets the root folder from a user&#39;s library.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
apiInstance.getRootFolder(userId, (error, data, response) => {
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

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSpecialFeatures

> [BaseItemDto] getSpecialFeatures(userId, itemId)

Gets special features for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.getSpecialFeatures(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## markFavoriteItem

> UserItemDataDto markFavoriteItem(userId, itemId)

Marks an item as a favorite.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.markFavoriteItem(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## unmarkFavoriteItem

> UserItemDataDto unmarkFavoriteItem(userId, itemId)

Unmarks item as a favorite.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
apiInstance.unmarkFavoriteItem(userId, itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updateUserItemRating

> UserItemDataDto updateUserItemRating(userId, itemId, opts)

Updates a user&#39;s rating for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.UserLibraryApi();
let userId = "userId_example"; // String | User id.
let itemId = "itemId_example"; // String | Item id.
let opts = {
  'likes': true // Boolean | Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Guid,System.Guid,System.Nullable{System.Boolean}) is likes.
};
apiInstance.updateUserItemRating(userId, itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **likes** | **Boolean**| Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Guid,System.Guid,System.Nullable{System.Boolean}) is likes. | [optional] 

### Return type

[**UserItemDataDto**](UserItemDataDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

