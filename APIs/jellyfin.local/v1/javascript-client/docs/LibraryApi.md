# JellyfinApi.LibraryApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteItem**](LibraryApi.md#deleteItem) | **DELETE** /Items/{itemId} | Deletes an item from the library and filesystem.
[**deleteItems**](LibraryApi.md#deleteItems) | **DELETE** /Items | Deletes items from the library and filesystem.
[**getAncestors**](LibraryApi.md#getAncestors) | **GET** /Items/{itemId}/Ancestors | Gets all parents of an item.
[**getCriticReviews**](LibraryApi.md#getCriticReviews) | **GET** /Items/{itemId}/CriticReviews | Gets critic review for an item.
[**getDownload**](LibraryApi.md#getDownload) | **GET** /Items/{itemId}/Download | Downloads item media.
[**getFile**](LibraryApi.md#getFile) | **GET** /Items/{itemId}/File | Get the original file of an item.
[**getItemCounts**](LibraryApi.md#getItemCounts) | **GET** /Items/Counts | Get item counts.
[**getLibraryOptionsInfo**](LibraryApi.md#getLibraryOptionsInfo) | **GET** /Libraries/AvailableOptions | Gets the library options info.
[**getMediaFolders**](LibraryApi.md#getMediaFolders) | **GET** /Library/MediaFolders | Gets all user media folders.
[**getPhysicalPaths**](LibraryApi.md#getPhysicalPaths) | **GET** /Library/PhysicalPaths | Gets a list of physical paths from virtual folders.
[**getSimilarAlbums**](LibraryApi.md#getSimilarAlbums) | **GET** /Albums/{itemId}/Similar | Gets similar items.
[**getSimilarArtists**](LibraryApi.md#getSimilarArtists) | **GET** /Artists/{itemId}/Similar | Gets similar items.
[**getSimilarItems**](LibraryApi.md#getSimilarItems) | **GET** /Items/{itemId}/Similar | Gets similar items.
[**getSimilarMovies**](LibraryApi.md#getSimilarMovies) | **GET** /Movies/{itemId}/Similar | Gets similar items.
[**getSimilarShows**](LibraryApi.md#getSimilarShows) | **GET** /Shows/{itemId}/Similar | Gets similar items.
[**getSimilarTrailers**](LibraryApi.md#getSimilarTrailers) | **GET** /Trailers/{itemId}/Similar | Gets similar items.
[**getThemeMedia**](LibraryApi.md#getThemeMedia) | **GET** /Items/{itemId}/ThemeMedia | Get theme songs and videos for an item.
[**getThemeSongs**](LibraryApi.md#getThemeSongs) | **GET** /Items/{itemId}/ThemeSongs | Get theme songs for an item.
[**getThemeVideos**](LibraryApi.md#getThemeVideos) | **GET** /Items/{itemId}/ThemeVideos | Get theme videos for an item.
[**postAddedMovies**](LibraryApi.md#postAddedMovies) | **POST** /Library/Movies/Added | Reports that new movies have been added by an external source.
[**postAddedSeries**](LibraryApi.md#postAddedSeries) | **POST** /Library/Series/Added | Reports that new episodes of a series have been added by an external source.
[**postUpdatedMedia**](LibraryApi.md#postUpdatedMedia) | **POST** /Library/Media/Updated | Reports that new movies have been added by an external source.
[**postUpdatedMovies**](LibraryApi.md#postUpdatedMovies) | **POST** /Library/Movies/Updated | Reports that new movies have been added by an external source.
[**postUpdatedSeries**](LibraryApi.md#postUpdatedSeries) | **POST** /Library/Series/Updated | Reports that new episodes of a series have been added by an external source.
[**refreshLibrary**](LibraryApi.md#refreshLibrary) | **GET** /Library/Refresh | Starts a library scan.



## deleteItem

> deleteItem(itemId)

Deletes an item from the library and filesystem.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
apiInstance.deleteItem(itemId, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## deleteItems

> deleteItems(opts)

Deletes items from the library and filesystem.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'ids': ["null"] // [String] | The item ids.
};
apiInstance.deleteItems(opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| The item ids. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getAncestors

> [BaseItemDto] getAncestors(itemId, opts)

Gets all parents of an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user id, and attach user data.
};
apiInstance.getAncestors(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 

### Return type

[**[BaseItemDto]**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getCriticReviews

> BaseItemDtoQueryResult getCriticReviews(itemId)

Gets critic review for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | 
apiInstance.getCriticReviews(itemId, (error, data, response) => {
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
 **itemId** | **String**|  | 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getDownload

> File getDownload(itemId)

Downloads item media.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
apiInstance.getDownload(itemId, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*, video/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getFile

> File getFile(itemId)

Get the original file of an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
apiInstance.getFile(itemId, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*, video/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getItemCounts

> ItemCounts getItemCounts(opts)

Get item counts.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'userId': "userId_example", // String | Optional. Get counts from a specific user's library.
  'isFavorite': true // Boolean | Optional. Get counts of favorite items.
};
apiInstance.getItemCounts(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. Get counts from a specific user&#39;s library. | [optional] 
 **isFavorite** | **Boolean**| Optional. Get counts of favorite items. | [optional] 

### Return type

[**ItemCounts**](ItemCounts.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLibraryOptionsInfo

> LibraryOptionsResultDto getLibraryOptionsInfo(opts)

Gets the library options info.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'libraryContentType': "libraryContentType_example", // String | Library content type.
  'isNewLibrary': true // Boolean | Whether this is a new library.
};
apiInstance.getLibraryOptionsInfo(opts, (error, data, response) => {
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
 **libraryContentType** | **String**| Library content type. | [optional] 
 **isNewLibrary** | **Boolean**| Whether this is a new library. | [optional] 

### Return type

[**LibraryOptionsResultDto**](LibraryOptionsResultDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMediaFolders

> BaseItemDtoQueryResult getMediaFolders(opts)

Gets all user media folders.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'isHidden': true // Boolean | Optional. Filter by folders that are marked hidden, or not.
};
apiInstance.getMediaFolders(opts, (error, data, response) => {
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
 **isHidden** | **Boolean**| Optional. Filter by folders that are marked hidden, or not. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPhysicalPaths

> [String] getPhysicalPaths()

Gets a list of physical paths from virtual folders.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
apiInstance.getPhysicalPaths((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSimilarAlbums

> BaseItemDtoQueryResult getSimilarAlbums(itemId, opts)

Gets similar items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'excludeArtistIds': ["null"], // [String] | Exclude artist ids.
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
};
apiInstance.getSimilarAlbums(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **excludeArtistIds** | [**[String]**](String.md)| Exclude artist ids. | [optional] 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSimilarArtists

> BaseItemDtoQueryResult getSimilarArtists(itemId, opts)

Gets similar items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'excludeArtistIds': ["null"], // [String] | Exclude artist ids.
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
};
apiInstance.getSimilarArtists(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **excludeArtistIds** | [**[String]**](String.md)| Exclude artist ids. | [optional] 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSimilarItems

> BaseItemDtoQueryResult getSimilarItems(itemId, opts)

Gets similar items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'excludeArtistIds': ["null"], // [String] | Exclude artist ids.
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
};
apiInstance.getSimilarItems(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **excludeArtistIds** | [**[String]**](String.md)| Exclude artist ids. | [optional] 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSimilarMovies

> BaseItemDtoQueryResult getSimilarMovies(itemId, opts)

Gets similar items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'excludeArtistIds': ["null"], // [String] | Exclude artist ids.
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
};
apiInstance.getSimilarMovies(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **excludeArtistIds** | [**[String]**](String.md)| Exclude artist ids. | [optional] 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSimilarShows

> BaseItemDtoQueryResult getSimilarShows(itemId, opts)

Gets similar items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'excludeArtistIds': ["null"], // [String] | Exclude artist ids.
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
};
apiInstance.getSimilarShows(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **excludeArtistIds** | [**[String]**](String.md)| Exclude artist ids. | [optional] 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSimilarTrailers

> BaseItemDtoQueryResult getSimilarTrailers(itemId, opts)

Gets similar items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'excludeArtistIds': ["null"], // [String] | Exclude artist ids.
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
};
apiInstance.getSimilarTrailers(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **excludeArtistIds** | [**[String]**](String.md)| Exclude artist ids. | [optional] 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getThemeMedia

> AllThemeMediaResult getThemeMedia(itemId, opts)

Get theme songs and videos for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'inheritFromParent': false // Boolean | Optional. Determines whether or not parent items should be searched for theme media.
};
apiInstance.getThemeMedia(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **inheritFromParent** | **Boolean**| Optional. Determines whether or not parent items should be searched for theme media. | [optional] [default to false]

### Return type

[**AllThemeMediaResult**](AllThemeMediaResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getThemeSongs

> ThemeMediaResult getThemeSongs(itemId, opts)

Get theme songs for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'inheritFromParent': false // Boolean | Optional. Determines whether or not parent items should be searched for theme media.
};
apiInstance.getThemeSongs(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **inheritFromParent** | **Boolean**| Optional. Determines whether or not parent items should be searched for theme media. | [optional] [default to false]

### Return type

[**ThemeMediaResult**](ThemeMediaResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getThemeVideos

> ThemeMediaResult getThemeVideos(itemId, opts)

Get theme videos for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'inheritFromParent': false // Boolean | Optional. Determines whether or not parent items should be searched for theme media.
};
apiInstance.getThemeVideos(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **inheritFromParent** | **Boolean**| Optional. Determines whether or not parent items should be searched for theme media. | [optional] [default to false]

### Return type

[**ThemeMediaResult**](ThemeMediaResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## postAddedMovies

> postAddedMovies(opts)

Reports that new movies have been added by an external source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'tmdbId': "tmdbId_example", // String | The tmdbId.
  'imdbId': "imdbId_example" // String | The imdbId.
};
apiInstance.postAddedMovies(opts, (error, data, response) => {
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
 **tmdbId** | **String**| The tmdbId. | [optional] 
 **imdbId** | **String**| The imdbId. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postAddedSeries

> postAddedSeries(opts)

Reports that new episodes of a series have been added by an external source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'tvdbId': "tvdbId_example" // String | The tvdbId.
};
apiInstance.postAddedSeries(opts, (error, data, response) => {
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
 **tvdbId** | **String**| The tvdbId. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUpdatedMedia

> postUpdatedMedia(mediaUpdateInfoDto)

Reports that new movies have been added by an external source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let mediaUpdateInfoDto = [new JellyfinApi.MediaUpdateInfoDto()]; // [MediaUpdateInfoDto] | A list of updated media paths.
apiInstance.postUpdatedMedia(mediaUpdateInfoDto, (error, data, response) => {
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
 **mediaUpdateInfoDto** | [**[MediaUpdateInfoDto]**](MediaUpdateInfoDto.md)| A list of updated media paths. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## postUpdatedMovies

> postUpdatedMovies(opts)

Reports that new movies have been added by an external source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'tmdbId': "tmdbId_example", // String | The tmdbId.
  'imdbId': "imdbId_example" // String | The imdbId.
};
apiInstance.postUpdatedMovies(opts, (error, data, response) => {
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
 **tmdbId** | **String**| The tmdbId. | [optional] 
 **imdbId** | **String**| The imdbId. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUpdatedSeries

> postUpdatedSeries(opts)

Reports that new episodes of a series have been added by an external source.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
let opts = {
  'tvdbId': "tvdbId_example" // String | The tvdbId.
};
apiInstance.postUpdatedSeries(opts, (error, data, response) => {
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
 **tvdbId** | **String**| The tvdbId. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## refreshLibrary

> refreshLibrary()

Starts a library scan.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LibraryApi();
apiInstance.refreshLibrary((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

