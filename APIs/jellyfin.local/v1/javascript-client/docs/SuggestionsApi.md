# JellyfinApi.SuggestionsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSuggestions**](SuggestionsApi.md#getSuggestions) | **GET** /Users/{userId}/Suggestions | Gets suggestions.



## getSuggestions

> BaseItemDtoQueryResult getSuggestions(userId, opts)

Gets suggestions.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.SuggestionsApi();
let userId = "userId_example"; // String | The user id.
let opts = {
  'mediaType': ["null"], // [String] | The media types.
  'type': ["null"], // [String] | The type.
  'startIndex': 56, // Number | Optional. The start index.
  'limit': 56, // Number | Optional. The limit.
  'enableTotalRecordCount': false // Boolean | Whether to enable the total record count.
};
apiInstance.getSuggestions(userId, opts, (error, data, response) => {
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
 **userId** | **String**| The user id. | 
 **mediaType** | [**[String]**](String.md)| The media types. | [optional] 
 **type** | [**[String]**](String.md)| The type. | [optional] 
 **startIndex** | **Number**| Optional. The start index. | [optional] 
 **limit** | **Number**| Optional. The limit. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Whether to enable the total record count. | [optional] [default to false]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

