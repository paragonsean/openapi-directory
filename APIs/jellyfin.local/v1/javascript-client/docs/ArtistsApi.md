# JellyfinApi.ArtistsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAlbumArtists**](ArtistsApi.md#getAlbumArtists) | **GET** /Artists/AlbumArtists | Gets all album artists from a given item, folder, or the entire library.
[**getArtistByName**](ArtistsApi.md#getArtistByName) | **GET** /Artists/{name} | Gets an artist by name.
[**getArtists**](ArtistsApi.md#getArtists) | **GET** /Artists | Gets all artists from a given item, folder, or the entire library.



## getAlbumArtists

> BaseItemDtoQueryResult getAlbumArtists(opts)

Gets all album artists from a given item, folder, or the entire library.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ArtistsApi();
let opts = {
  'minCommunityRating': 3.4, // Number | Optional filter by minimum community rating.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'searchTerm': "searchTerm_example", // String | Optional. Search term.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply.
  'isFavorite': true, // Boolean | Optional filter by items that are marked as favorite, or not.
  'mediaTypes': ["null"], // [String] | Optional filter by MediaType. Allows multiple, comma delimited.
  'genres': ["null"], // [String] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
  'genreIds': ["null"], // [String] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
  'officialRatings': ["null"], // [String] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
  'tags': ["null"], // [String] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
  'years': [null], // [Number] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
  'enableUserData': true, // Boolean | Optional, include user data.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'person': "person_example", // String | Optional. If specified, results will be filtered to include only those containing the specified person.
  'personIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified person ids.
  'personTypes': ["null"], // [String] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
  'studios': ["null"], // [String] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
  'studioIds': ["null"], // [String] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
  'userId': "userId_example", // String | User id.
  'nameStartsWithOrGreater': "nameStartsWithOrGreater_example", // String | Optional filter by items whose name is sorted equally or greater than a given input string.
  'nameStartsWith': "nameStartsWith_example", // String | Optional filter by items whose name is sorted equally than a given input string.
  'nameLessThan': "nameLessThan_example", // String | Optional filter by items whose name is equally or lesser than a given input string.
  'enableImages': true, // Boolean | Optional, include image information in output.
  'enableTotalRecordCount': true // Boolean | Total record count.
};
apiInstance.getAlbumArtists(opts, (error, data, response) => {
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
 **minCommunityRating** | **Number**| Optional filter by minimum community rating. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **searchTerm** | **String**| Optional. Search term. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **isFavorite** | **Boolean**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **genres** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. | [optional] 
 **genreIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. | [optional] 
 **officialRatings** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. | [optional] 
 **tags** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. | [optional] 
 **years** | [**[Number]**](Number.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. | [optional] 
 **enableUserData** | **Boolean**| Optional, include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **String**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **personIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified person ids. | [optional] 
 **personTypes** | [**[String]**](String.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. | [optional] 
 **studioIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. | [optional] 
 **userId** | **String**| User id. | [optional] 
 **nameStartsWithOrGreater** | **String**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **nameStartsWith** | **String**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **nameLessThan** | **String**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] [default to true]
 **enableTotalRecordCount** | **Boolean**| Total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getArtistByName

> BaseItemDto getArtistByName(name, opts)

Gets an artist by name.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ArtistsApi();
let name = "name_example"; // String | Studio name.
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user id, and attach user data.
};
apiInstance.getArtistByName(name, opts, (error, data, response) => {
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
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getArtists

> BaseItemDtoQueryResult getArtists(opts)

Gets all artists from a given item, folder, or the entire library.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ArtistsApi();
let opts = {
  'minCommunityRating': 3.4, // Number | Optional filter by minimum community rating.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'searchTerm': "searchTerm_example", // String | Optional. Search term.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply.
  'isFavorite': true, // Boolean | Optional filter by items that are marked as favorite, or not.
  'mediaTypes': ["null"], // [String] | Optional filter by MediaType. Allows multiple, comma delimited.
  'genres': ["null"], // [String] | Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
  'genreIds': ["null"], // [String] | Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
  'officialRatings': ["null"], // [String] | Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
  'tags': ["null"], // [String] | Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
  'years': [null], // [Number] | Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
  'enableUserData': true, // Boolean | Optional, include user data.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'person': "person_example", // String | Optional. If specified, results will be filtered to include only those containing the specified person.
  'personIds': ["null"], // [String] | Optional. If specified, results will be filtered to include only those containing the specified person ids.
  'personTypes': ["null"], // [String] | Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
  'studios': ["null"], // [String] | Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
  'studioIds': ["null"], // [String] | Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
  'userId': "userId_example", // String | User id.
  'nameStartsWithOrGreater': "nameStartsWithOrGreater_example", // String | Optional filter by items whose name is sorted equally or greater than a given input string.
  'nameStartsWith': "nameStartsWith_example", // String | Optional filter by items whose name is sorted equally than a given input string.
  'nameLessThan': "nameLessThan_example", // String | Optional filter by items whose name is equally or lesser than a given input string.
  'enableImages': true, // Boolean | Optional, include image information in output.
  'enableTotalRecordCount': true // Boolean | Total record count.
};
apiInstance.getArtists(opts, (error, data, response) => {
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
 **minCommunityRating** | **Number**| Optional filter by minimum community rating. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **searchTerm** | **String**| Optional. Search term. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **isFavorite** | **Boolean**| Optional filter by items that are marked as favorite, or not. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **genres** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited. | [optional] 
 **genreIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited. | [optional] 
 **officialRatings** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited. | [optional] 
 **tags** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited. | [optional] 
 **years** | [**[Number]**](Number.md)| Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited. | [optional] 
 **enableUserData** | **Boolean**| Optional, include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **person** | **String**| Optional. If specified, results will be filtered to include only those containing the specified person. | [optional] 
 **personIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered to include only those containing the specified person ids. | [optional] 
 **personTypes** | [**[String]**](String.md)| Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited. | [optional] 
 **studios** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited. | [optional] 
 **studioIds** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited. | [optional] 
 **userId** | **String**| User id. | [optional] 
 **nameStartsWithOrGreater** | **String**| Optional filter by items whose name is sorted equally or greater than a given input string. | [optional] 
 **nameStartsWith** | **String**| Optional filter by items whose name is sorted equally than a given input string. | [optional] 
 **nameLessThan** | **String**| Optional filter by items whose name is equally or lesser than a given input string. | [optional] 
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] [default to true]
 **enableTotalRecordCount** | **Boolean**| Total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

