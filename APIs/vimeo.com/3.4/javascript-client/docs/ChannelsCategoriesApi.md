# Vimeo.ChannelsCategoriesApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addChannelCategories**](ChannelsCategoriesApi.md#addChannelCategories) | **PUT** /channels/{channel_id}/categories | Add a list of categories to a channel
[**categorizeChannel**](ChannelsCategoriesApi.md#categorizeChannel) | **PUT** /channels/{channel_id}/categories/{category} | Categorize a channel
[**deleteChannelCategory**](ChannelsCategoriesApi.md#deleteChannelCategory) | **DELETE** /channels/{channel_id}/categories/{category} | Remove a category from a channel
[**getChannelCategories**](ChannelsCategoriesApi.md#getChannelCategories) | **GET** /channels/{channel_id}/categories | Get all the categories in a channel



## addChannelCategories

> addChannelCategories(channelId, addChannelCategoriesRequest)

Add a list of categories to a channel

This method adds multiple categories to the specified channel.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsCategoriesApi();
let channelId = 927; // Number | The ID of the channel.
let addChannelCategoriesRequest = new Vimeo.AddChannelCategoriesRequest(); // AddChannelCategoriesRequest | 
apiInstance.addChannelCategories(channelId, addChannelCategoriesRequest, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **addChannelCategoriesRequest** | [**AddChannelCategoriesRequest**](AddChannelCategoriesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## categorizeChannel

> categorizeChannel(category, channelId)

Categorize a channel

This method adds a channel to a category.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsCategoriesApi();
let category = "animation"; // String | The name of the category.
let channelId = 927; // Number | The ID of the channel.
apiInstance.categorizeChannel(category, channelId, (error, data, response) => {
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
 **category** | **String**| The name of the category. | 
 **channelId** | **Number**| The ID of the channel. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.category+json


## deleteChannelCategory

> deleteChannelCategory(category, channelId)

Remove a category from a channel

This method removes a single category from the specified channel.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsCategoriesApi();
let category = "animation"; // String | The name of the category.
let channelId = 927; // Number | The ID of the channel.
apiInstance.deleteChannelCategory(category, channelId, (error, data, response) => {
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
 **category** | **String**| The name of the category. | 
 **channelId** | **Number**| The ID of the channel. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.category+json


## getChannelCategories

> [Category] getChannelCategories(channelId)

Get all the categories in a channel

This method gets all the categories in the specified channel.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.ChannelsCategoriesApi();
let channelId = 927; // Number | The ID of the channel.
apiInstance.getChannelCategories(channelId, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 

### Return type

[**[Category]**](Category.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.category+json

