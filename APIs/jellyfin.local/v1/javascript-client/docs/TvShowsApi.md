# JellyfinApi.TvShowsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEpisodes**](TvShowsApi.md#getEpisodes) | **GET** /Shows/{seriesId}/Episodes | Gets episodes for a tv season.
[**getNextUp**](TvShowsApi.md#getNextUp) | **GET** /Shows/NextUp | Gets a list of next up episodes.
[**getSeasons**](TvShowsApi.md#getSeasons) | **GET** /Shows/{seriesId}/Seasons | Gets seasons for a tv series.
[**getUpcomingEpisodes**](TvShowsApi.md#getUpcomingEpisodes) | **GET** /Shows/Upcoming | Gets a list of upcoming episodes.



## getEpisodes

> BaseItemDtoQueryResult getEpisodes(seriesId, opts)

Gets episodes for a tv season.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.TvShowsApi();
let seriesId = "seriesId_example"; // String | The series id.
let opts = {
  'userId': "userId_example", // String | The user id.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
  'season': 56, // Number | Optional filter by season number.
  'seasonId': "seasonId_example", // String | Optional. Filter by season id.
  'isMissing': true, // Boolean | Optional. Filter by items that are missing episodes or not.
  'adjacentTo': "adjacentTo_example", // String | Optional. Return items that are siblings of a supplied item.
  'startItemId': "startItemId_example", // String | Optional. Skip through the list until a given item is found.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'enableImages': true, // Boolean | Optional, include image information in output.
  'imageTypeLimit': 56, // Number | Optional, the max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'sortBy': "sortBy_example" // String | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
};
apiInstance.getEpisodes(seriesId, opts, (error, data, response) => {
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
 **seriesId** | **String**| The series id. | 
 **userId** | **String**| The user id. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 
 **season** | **Number**| Optional filter by season number. | [optional] 
 **seasonId** | **String**| Optional. Filter by season id. | [optional] 
 **isMissing** | **Boolean**| Optional. Filter by items that are missing episodes or not. | [optional] 
 **adjacentTo** | **String**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **startItemId** | **String**| Optional. Skip through the list until a given item is found. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **enableImages** | **Boolean**| Optional, include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional, the max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **sortBy** | **String**| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getNextUp

> BaseItemDtoQueryResult getNextUp(opts)

Gets a list of next up episodes.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.TvShowsApi();
let opts = {
  'userId': "userId_example", // String | The user id of the user to get the next up episodes for.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'seriesId': "seriesId_example", // String | Optional. Filter by series id.
  'parentId': "parentId_example", // String | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
  'enableImges': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'enableTotalRecordCount': true // Boolean | Whether to enable the total records count. Defaults to true.
};
apiInstance.getNextUp(opts, (error, data, response) => {
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
 **userId** | **String**| The user id of the user to get the next up episodes for. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **seriesId** | **String**| Optional. Filter by series id. | [optional] 
 **parentId** | **String**| Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **enableImges** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Whether to enable the total records count. Defaults to true. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSeasons

> BaseItemDtoQueryResult getSeasons(seriesId, opts)

Gets seasons for a tv series.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.TvShowsApi();
let seriesId = "seriesId_example"; // String | The series id.
let opts = {
  'userId': "userId_example", // String | The user id.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
  'isSpecialSeason': true, // Boolean | Optional. Filter by special season.
  'isMissing': true, // Boolean | Optional. Filter by items that are missing episodes or not.
  'adjacentTo': "adjacentTo_example", // String | Optional. Return items that are siblings of a supplied item.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'enableUserData': true // Boolean | Optional. Include user data.
};
apiInstance.getSeasons(seriesId, opts, (error, data, response) => {
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
 **seriesId** | **String**| The series id. | 
 **userId** | **String**| The user id. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls. | [optional] 
 **isSpecialSeason** | **Boolean**| Optional. Filter by special season. | [optional] 
 **isMissing** | **Boolean**| Optional. Filter by items that are missing episodes or not. | [optional] 
 **adjacentTo** | **String**| Optional. Return items that are siblings of a supplied item. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getUpcomingEpisodes

> BaseItemDtoQueryResult getUpcomingEpisodes(opts)

Gets a list of upcoming episodes.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.TvShowsApi();
let opts = {
  'userId': "userId_example", // String | The user id of the user to get the upcoming episodes for.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'parentId': "parentId_example", // String | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
  'enableImges': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'enableUserData': true // Boolean | Optional. Include user data.
};
apiInstance.getUpcomingEpisodes(opts, (error, data, response) => {
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
 **userId** | **String**| The user id of the user to get the upcoming episodes for. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **parentId** | **String**| Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **enableImges** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

