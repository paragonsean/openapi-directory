# JellyfinApi.ChannelsApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllChannelFeatures**](ChannelsApi.md#getAllChannelFeatures) | **GET** /Channels/Features | Get all channel features.
[**getChannelFeatures**](ChannelsApi.md#getChannelFeatures) | **GET** /Channels/{channelId}/Features | Get channel features.
[**getChannelItems**](ChannelsApi.md#getChannelItems) | **GET** /Channels/{channelId}/Items | Get channel items.
[**getChannels**](ChannelsApi.md#getChannels) | **GET** /Channels | Gets available channels.
[**getLatestChannelItems**](ChannelsApi.md#getLatestChannelItems) | **GET** /Channels/Items/Latest | Gets latest channel items.



## getAllChannelFeatures

> [ChannelFeatures] getAllChannelFeatures()

Get all channel features.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ChannelsApi();
apiInstance.getAllChannelFeatures((error, data, response) => {
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

[**[ChannelFeatures]**](ChannelFeatures.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getChannelFeatures

> ChannelFeatures getChannelFeatures(channelId)

Get channel features.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ChannelsApi();
let channelId = "channelId_example"; // String | Channel id.
apiInstance.getChannelFeatures(channelId, (error, data, response) => {
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
 **channelId** | **String**| Channel id. | 

### Return type

[**ChannelFeatures**](ChannelFeatures.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getChannelItems

> BaseItemDtoQueryResult getChannelItems(channelId, opts)

Get channel items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ChannelsApi();
let channelId = "channelId_example"; // String | Channel Id.
let opts = {
  'folderId': "folderId_example", // String | Optional. Folder Id.
  'userId': "userId_example", // String | Optional. User Id.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'sortOrder': "sortOrder_example", // String | Optional. Sort Order - Ascending,Descending.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply.
  'sortBy': "sortBy_example", // String | Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
  'fields': [new JellyfinApi.ItemFields()] // [ItemFields] | Optional. Specify additional fields of information to return in the output.
};
apiInstance.getChannelItems(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| Channel Id. | 
 **folderId** | **String**| Optional. Folder Id. | [optional] 
 **userId** | **String**| Optional. User Id. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **sortOrder** | **String**| Optional. Sort Order - Ascending,Descending. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **sortBy** | **String**| Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getChannels

> BaseItemDtoQueryResult getChannels(opts)

Gets available channels.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ChannelsApi();
let opts = {
  'userId': "userId_example", // String | User Id to filter by. Use System.Guid.Empty to not filter by user.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'supportsLatestItems': true, // Boolean | Optional. Filter by channels that support getting latest items.
  'supportsMediaDeletion': true, // Boolean | Optional. Filter by channels that support media deletion.
  'isFavorite': true // Boolean | Optional. Filter by channels that are favorite.
};
apiInstance.getChannels(opts, (error, data, response) => {
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
 **userId** | **String**| User Id to filter by. Use System.Guid.Empty to not filter by user. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **supportsLatestItems** | **Boolean**| Optional. Filter by channels that support getting latest items. | [optional] 
 **supportsMediaDeletion** | **Boolean**| Optional. Filter by channels that support media deletion. | [optional] 
 **isFavorite** | **Boolean**| Optional. Filter by channels that are favorite. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLatestChannelItems

> BaseItemDtoQueryResult getLatestChannelItems(opts)

Gets latest channel items.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ChannelsApi();
let opts = {
  'userId': "userId_example", // String | Optional. User Id.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'filters': [new JellyfinApi.ItemFilter()], // [ItemFilter] | Optional. Specify additional filters to apply.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'channelIds': ["null"] // [String] | Optional. Specify one or more channel id's, comma delimited.
};
apiInstance.getLatestChannelItems(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. User Id. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **filters** | [**[ItemFilter]**](ItemFilter.md)| Optional. Specify additional filters to apply. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **channelIds** | [**[String]**](String.md)| Optional. Specify one or more channel id&#39;s, comma delimited. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

