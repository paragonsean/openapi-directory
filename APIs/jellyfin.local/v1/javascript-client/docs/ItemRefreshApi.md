# JellyfinApi.ItemRefreshApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post**](ItemRefreshApi.md#post) | **POST** /Items/{itemId}/Refresh | Refreshes metadata for an item.



## post

> post(itemId, opts)

Refreshes metadata for an item.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemRefreshApi();
let itemId = "itemId_example"; // String | Item id.
let opts = {
  'metadataRefreshMode': new JellyfinApi.MetadataRefreshMode(), // MetadataRefreshMode | (Optional) Specifies the metadata refresh mode.
  'imageRefreshMode': new JellyfinApi.MetadataRefreshMode(), // MetadataRefreshMode | (Optional) Specifies the image refresh mode.
  'replaceAllMetadata': false, // Boolean | (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.
  'replaceAllImages': false // Boolean | (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.
};
apiInstance.post(itemId, opts, (error, data, response) => {
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
 **metadataRefreshMode** | [**MetadataRefreshMode**](.md)| (Optional) Specifies the metadata refresh mode. | [optional] 
 **imageRefreshMode** | [**MetadataRefreshMode**](.md)| (Optional) Specifies the image refresh mode. | [optional] 
 **replaceAllMetadata** | **Boolean**| (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh. | [optional] [default to false]
 **replaceAllImages** | **Boolean**| (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

