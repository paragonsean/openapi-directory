# JellyfinApi.YearsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getYear**](YearsApi.md#getYear) | **GET** /Years/{year} | Gets a year.
[**getYears**](YearsApi.md#getYears) | **GET** /Years | Get years.



## getYear

> BaseItemDto getYear(year, opts)

Gets a year.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.YearsApi();
let year = 56; // Number | The year.
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user id, and attach user data.
};
apiInstance.getYear(year, opts, (error, data, response) => {
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
 **year** | **Number**| The year. | 
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getYears

> BaseItemDtoQueryResult getYears(opts)

Get years.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.YearsApi();
let opts = {
  'startIndex': 56, // Number | Skips over a given number of items within the results. Use for paging.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'sortOrder': "sortOrder_example", // String | Sort Order - Ascending,Descending.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'excludeItemTypes': ["null"], // [String] | Optional. If specified, results will be excluded based on item type. This allows multiple, comma delimited.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be included based on item type. This allows multiple, comma delimited.
  'mediaTypes': ["null"], // [String] | Optional. Filter by MediaType. Allows multiple, comma delimited.
  'sortBy': "sortBy_example", // String | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'userId': "userId_example", // String | User Id.
  'recursive': true, // Boolean | Search recursively.
  'enableImages': true // Boolean | Optional. Include image information in output.
};
apiInstance.getYears(opts, (error, data, response) => {
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
 **startIndex** | **Number**| Skips over a given number of items within the results. Use for paging. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **sortOrder** | **String**| Sort Order - Ascending,Descending. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be excluded based on item type. This allows multiple, comma delimited. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be included based on item type. This allows multiple, comma delimited. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional. Filter by MediaType. Allows multiple, comma delimited. | [optional] 
 **sortBy** | **String**| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **userId** | **String**| User Id. | [optional] 
 **recursive** | **Boolean**| Search recursively. | [optional] [default to true]
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

