# JellyfinApi.MusicGenresApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMusicGenre**](MusicGenresApi.md#getMusicGenre) | **GET** /MusicGenres/{genreName} | Gets a music genre, by name.
[**getMusicGenres**](MusicGenresApi.md#getMusicGenres) | **GET** /MusicGenres | Gets all music genres from a given item, folder, or the entire library.



## getMusicGenre

> BaseItemDto getMusicGenre(genreName, opts)

Gets a music genre, by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MusicGenresApi();
let genreName = "genreName_example"; // String | The genre name.
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user id, and attach user data.
};
apiInstance.getMusicGenre(genreName, opts, (error, data, response) => {
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
 **genreName** | **String**| The genre name. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMusicGenres

> BaseItemDtoQueryResult getMusicGenres(opts)

Gets all music genres from a given item, folder, or the entire library.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MusicGenresApi();
let opts = {
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'searchTerm': "searchTerm_example", // String | The search term.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered in based on item type. This allows multiple, comma delimited.
  'isFavorite': true, // Boolean | Optional filter by items that are marked as favorite, or not.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'userId': "userId_example", // String | User id.
  'nameStartsWithOrGreater': "nameStartsWithOrGreater_example", // String | Optional filter by items whose name is sorted equally or greater than a given input string.
  'nameStartsWith': "nameStartsWith_example", // String | Optional filter by items whose name is sorted equally than a given input string.
  'nameLessThan': "nameLessThan_example", // String | Optional filter by items whose name is equally or lesser than a given input string.
  'enableImages': true, // Boolean | Optional, include image information in output.
  'enableTotalRecordCount': true // Boolean | Optional. Include total record count.
};
apiInstance.getMusicGenres(opts, (error, data, response) => {
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
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **searchTerm** | **String**| The search term. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered in based on item type. This allows multiple, comma delimited. | [optional] 
 **isFavorite** | **Boolean**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **userId** | **String**| User id. | [optional] 
 **nameStartsWithOrGreater** | **String**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **nameStartsWith** | **String**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **nameLessThan** | **String**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] [default to true]
 **enableTotalRecordCount** | **Boolean**| Optional. Include total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

