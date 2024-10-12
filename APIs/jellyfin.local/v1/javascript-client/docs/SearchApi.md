# JellyfinApi.SearchApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](SearchApi.md#get) | **GET** /Search/Hints | Gets the search hint result.



## get

> SearchHintResult get(searchTerm, opts)

Gets the search hint result.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SearchApi();
let searchTerm = "searchTerm_example"; // String | The search term to filter on.
let opts = {
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'userId': "userId_example", // String | Optional. Supply a user id to search within a user's library or omit to search all.
  'includeItemTypes': ["null"], // [String] | If specified, only results with the specified item types are returned. This allows multiple, comma delimeted.
  'excludeItemTypes': ["null"], // [String] | If specified, results with these item types are filtered out. This allows multiple, comma delimeted.
  'mediaTypes': ["null"], // [String] | If specified, only results with the specified media types are returned. This allows multiple, comma delimeted.
  'parentId': "parentId_example", // String | If specified, only children of the parent are returned.
  'isMovie': true, // Boolean | Optional filter for movies.
  'isSeries': true, // Boolean | Optional filter for series.
  'isNews': true, // Boolean | Optional filter for news.
  'isKids': true, // Boolean | Optional filter for kids.
  'isSports': true, // Boolean | Optional filter for sports.
  'includePeople': true, // Boolean | Optional filter whether to include people.
  'includeMedia': true, // Boolean | Optional filter whether to include media.
  'includeGenres': true, // Boolean | Optional filter whether to include genres.
  'includeStudios': true, // Boolean | Optional filter whether to include studios.
  'includeArtists': true // Boolean | Optional filter whether to include artists.
};
apiInstance.get(searchTerm, opts, (error, data, response) => {
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
 **searchTerm** | **String**| The search term to filter on. | 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **userId** | **String**| Optional. Supply a user id to search within a user&#39;s library or omit to search all. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| If specified, only results with the specified item types are returned. This allows multiple, comma delimeted. | [optional] 
 **excludeItemTypes** | [**[String]**](String.md)| If specified, results with these item types are filtered out. This allows multiple, comma delimeted. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| If specified, only results with the specified media types are returned. This allows multiple, comma delimeted. | [optional] 
 **parentId** | **String**| If specified, only children of the parent are returned. | [optional] 
 **isMovie** | **Boolean**| Optional filter for movies. | [optional] 
 **isSeries** | **Boolean**| Optional filter for series. | [optional] 
 **isNews** | **Boolean**| Optional filter for news. | [optional] 
 **isKids** | **Boolean**| Optional filter for kids. | [optional] 
 **isSports** | **Boolean**| Optional filter for sports. | [optional] 
 **includePeople** | **Boolean**| Optional filter whether to include people. | [optional] [default to true]
 **includeMedia** | **Boolean**| Optional filter whether to include media. | [optional] [default to true]
 **includeGenres** | **Boolean**| Optional filter whether to include genres. | [optional] [default to true]
 **includeStudios** | **Boolean**| Optional filter whether to include studios. | [optional] [default to true]
 **includeArtists** | **Boolean**| Optional filter whether to include artists. | [optional] [default to true]

### Return type

[**SearchHintResult**](SearchHintResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

