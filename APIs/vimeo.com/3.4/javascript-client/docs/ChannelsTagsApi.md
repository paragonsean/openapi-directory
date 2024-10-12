# Vimeo.ChannelsTagsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addChannelTag**](ChannelsTagsApi.md#addChannelTag) | **PUT** /channels/{channel_id}/tags/{word} | Add a specific tag to a channel
[**addTagsToChannel**](ChannelsTagsApi.md#addTagsToChannel) | **PUT** /channels/{channel_id}/tags | Add a list of tags to a channel
[**checkIfChannelHasTag**](ChannelsTagsApi.md#checkIfChannelHasTag) | **GET** /channels/{channel_id}/tags/{word} | Check if a tag has been added to a channel
[**deleteTagFromChannel**](ChannelsTagsApi.md#deleteTagFromChannel) | **DELETE** /channels/{channel_id}/tags/{word} | Remove a tag from a channel
[**getChannelTags**](ChannelsTagsApi.md#getChannelTags) | **GET** /channels/{channel_id}/tags | Get all the tags that have been added to a channel



## addChannelTag

> addChannelTag(channelId, word)

Add a specific tag to a channel

This method adds a single tag to the specified channel.

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

let apiInstance = new Vimeo.ChannelsTagsApi();
let channelId = 927; // Number | The ID of the channel.
let word = "awesome"; // String | The word to use as the tag.
apiInstance.addChannelTag(channelId, word, (error, data, response) => {
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
 **word** | **String**| The word to use as the tag. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.tag+json


## addTagsToChannel

> [Tag] addTagsToChannel(channelId, addTagsToChannelRequest)

Add a list of tags to a channel

This method adds multiple tags to the specified channel.

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

let apiInstance = new Vimeo.ChannelsTagsApi();
let channelId = 927; // Number | The ID of the channel.
let addTagsToChannelRequest = new Vimeo.AddTagsToChannelRequest(); // AddTagsToChannelRequest | 
apiInstance.addTagsToChannel(channelId, addTagsToChannelRequest, (error, data, response) => {
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
 **addTagsToChannelRequest** | [**AddTagsToChannelRequest**](AddTagsToChannelRequest.md)|  | 

### Return type

[**[Tag]**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.tag+json
- **Accept**: application/vnd.vimeo.tag+json


## checkIfChannelHasTag

> checkIfChannelHasTag(channelId, word)

Check if a tag has been added to a channel

This method determines whether a specific tag has been added to the channel in question.

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

let apiInstance = new Vimeo.ChannelsTagsApi();
let channelId = 927; // Number | The ID of the channel.
let word = "awesome"; // String | The word to use as the tag.
apiInstance.checkIfChannelHasTag(channelId, word, (error, data, response) => {
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
 **word** | **String**| The word to use as the tag. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.tag+json


## deleteTagFromChannel

> deleteTagFromChannel(channelId, word)

Remove a tag from a channel

This method removes a single tag from the specified channel.

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

let apiInstance = new Vimeo.ChannelsTagsApi();
let channelId = 927; // Number | The ID of the channel.
let word = "awesome"; // String | The word to use as the tag.
apiInstance.deleteTagFromChannel(channelId, word, (error, data, response) => {
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
 **word** | **String**| The word to use as the tag. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.tag+json


## getChannelTags

> [Tag] getChannelTags(channelId)

Get all the tags that have been added to a channel

This method gets all the tags that have been added to the specified channel.

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

let apiInstance = new Vimeo.ChannelsTagsApi();
let channelId = 927; // Number | The ID of the channel.
apiInstance.getChannelTags(channelId, (error, data, response) => {
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

[**[Tag]**](Tag.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.tag+json

