# JellyfinApi.FilterApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQueryFilters**](FilterApi.md#getQueryFilters) | **GET** /Items/Filters2 | Gets query filters.
[**getQueryFiltersLegacy**](FilterApi.md#getQueryFiltersLegacy) | **GET** /Items/Filters | Gets legacy query filters.



## getQueryFilters

> QueryFilters getQueryFilters(opts)

Gets query filters.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.FilterApi();
let opts = {
  'userId': "userId_example", // String | Optional. User id.
  'parentId': "parentId_example", // String | Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'isAiring': true, // Boolean | Optional. Is item airing.
  'isMovie': true, // Boolean | Optional. Is item movie.
  'isSports': true, // Boolean | Optional. Is item sports.
  'isKids': true, // Boolean | Optional. Is item kids.
  'isNews': true, // Boolean | Optional. Is item news.
  'isSeries': true, // Boolean | Optional. Is item series.
  'recursive': true // Boolean | Optional. Search recursive.
};
apiInstance.getQueryFilters(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. User id. | [optional] 
 **parentId** | **String**| Optional. Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **isAiring** | **Boolean**| Optional. Is item airing. | [optional] 
 **isMovie** | **Boolean**| Optional. Is item movie. | [optional] 
 **isSports** | **Boolean**| Optional. Is item sports. | [optional] 
 **isKids** | **Boolean**| Optional. Is item kids. | [optional] 
 **isNews** | **Boolean**| Optional. Is item news. | [optional] 
 **isSeries** | **Boolean**| Optional. Is item series. | [optional] 
 **recursive** | **Boolean**| Optional. Search recursive. | [optional] 

### Return type

[**QueryFilters**](QueryFilters.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getQueryFiltersLegacy

> QueryFiltersLegacy getQueryFiltersLegacy(opts)

Gets legacy query filters.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.FilterApi();
let opts = {
  'userId': "userId_example", // String | Optional. User id.
  'parentId': "parentId_example", // String | Optional. Parent id.
  'includeItemTypes': ["null"], // [String] | Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
  'mediaTypes': ["null"] // [String] | Optional. Filter by MediaType. Allows multiple, comma delimited.
};
apiInstance.getQueryFiltersLegacy(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. User id. | [optional] 
 **parentId** | **String**| Optional. Parent id. | [optional] 
 **includeItemTypes** | [**[String]**](String.md)| Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited. | [optional] 
 **mediaTypes** | [**[String]**](String.md)| Optional. Filter by MediaType. Allows multiple, comma delimited. | [optional] 

### Return type

[**QueryFiltersLegacy**](QueryFiltersLegacy.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

