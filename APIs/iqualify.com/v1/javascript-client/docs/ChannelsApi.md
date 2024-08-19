# IQualifyManagementApi.ChannelsApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet**](ChannelsApi.md#offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet) | **GET** /offerings/{offeringId}/analytics/channels/{channelId}/comments | Find comments
[**offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet**](ChannelsApi.md#offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet) | **GET** /offerings/{offeringId}/analytics/channels/{channelId}/posts | Find posts
[**offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet**](ChannelsApi.md#offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet) | **GET** /offerings/{offeringId}/analytics/channels/{channelId}/replies | Find replies
[**offeringsOfferingIdChannelsChannelIdLearnersDelete**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdLearnersDelete) | **DELETE** /offerings/{offeringId}/channels/{channelId}/learners | Remove learners from a group channel
[**offeringsOfferingIdChannelsChannelIdLearnersGet**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdLearnersGet) | **GET** /offerings/{offeringId}/channels/{channelId}/learners | Find learners in a group channel
[**offeringsOfferingIdChannelsChannelIdLearnersPost**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdLearnersPost) | **POST** /offerings/{offeringId}/channels/{channelId}/learners | Add learners to a group channel
[**offeringsOfferingIdChannelsChannelIdPatch**](ChannelsApi.md#offeringsOfferingIdChannelsChannelIdPatch) | **PATCH** /offerings/{offeringId}/channels/{channelId} | Update channel
[**offeringsOfferingIdChannelsGet**](ChannelsApi.md#offeringsOfferingIdChannelsGet) | **GET** /offerings/{offeringId}/channels | Find channels
[**offeringsOfferingIdChannelsPost**](ChannelsApi.md#offeringsOfferingIdChannelsPost) | **POST** /offerings/{offeringId}/channels | Add channel



## offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet

> [Comment] offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet(offeringId, channelId)

Find comments

Responds with a list of comments made in any posts in a specified channel, within an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
apiInstance.offeringsOfferingIdAnalyticsChannelsChannelIdCommentsGet(offeringId, channelId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet

> [HttpPost] offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet(offeringId, channelId)

Find posts

Responds with a list of posts made in a specified channel, within an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
apiInstance.offeringsOfferingIdAnalyticsChannelsChannelIdPostsGet(offeringId, channelId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 

### Return type

[**[HttpPost]**](HttpPost.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet

> [Comment] offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet(offeringId, channelId)

Find replies

Responds with a list of replies to comments in any posts in a specified channel, within an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
apiInstance.offeringsOfferingIdAnalyticsChannelsChannelIdRepliesGet(offeringId, channelId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 

### Return type

[**[Comment]**](Comment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdChannelsChannelIdLearnersDelete

> offeringsOfferingIdChannelsChannelIdLearnersDelete(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest)

Remove learners from a group channel

Removes a learner from the specified group channel.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
let offeringsOfferingIdChannelsChannelIdLearnersPostRequest = new IQualifyManagementApi.OfferingsOfferingIdChannelsChannelIdLearnersPostRequest(); // OfferingsOfferingIdChannelsChannelIdLearnersPostRequest | 
apiInstance.offeringsOfferingIdChannelsChannelIdLearnersDelete(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 
 **offeringsOfferingIdChannelsChannelIdLearnersPostRequest** | [**OfferingsOfferingIdChannelsChannelIdLearnersPostRequest**](OfferingsOfferingIdChannelsChannelIdLearnersPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdChannelsChannelIdLearnersGet

> ChannelResponse offeringsOfferingIdChannelsChannelIdLearnersGet(offeringId, channelId)

Find learners in a group channel

Finds all learners in a specified group channel.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
apiInstance.offeringsOfferingIdChannelsChannelIdLearnersGet(offeringId, channelId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdChannelsChannelIdLearnersPost

> offeringsOfferingIdChannelsChannelIdLearnersPost(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest)

Add learners to a group channel

Adds a learner to a specified group channel.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
let offeringsOfferingIdChannelsChannelIdLearnersPostRequest = new IQualifyManagementApi.OfferingsOfferingIdChannelsChannelIdLearnersPostRequest(); // OfferingsOfferingIdChannelsChannelIdLearnersPostRequest | 
apiInstance.offeringsOfferingIdChannelsChannelIdLearnersPost(offeringId, channelId, offeringsOfferingIdChannelsChannelIdLearnersPostRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 
 **offeringsOfferingIdChannelsChannelIdLearnersPostRequest** | [**OfferingsOfferingIdChannelsChannelIdLearnersPostRequest**](OfferingsOfferingIdChannelsChannelIdLearnersPostRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdChannelsChannelIdPatch

> ChannelResponse offeringsOfferingIdChannelsChannelIdPatch(offeringId, channelId, channel)

Update channel

Updates a channel in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelId = "channelId_example"; // String | channel's id
let channel = new IQualifyManagementApi.Channel(); // Channel | 
apiInstance.offeringsOfferingIdChannelsChannelIdPatch(offeringId, channelId, channel, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelId** | **String**| channel&#39;s id | 
 **channel** | [**Channel**](Channel.md)|  | 

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdChannelsGet

> [ChannelResponse] offeringsOfferingIdChannelsGet(offeringId)

Find channels

Responds with a list of channels in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdChannelsGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**[ChannelResponse]**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdChannelsPost

> ChannelResponse offeringsOfferingIdChannelsPost(offeringId, channelRequired)

Add channel

Adds new channel to the specified offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.ChannelsApi();
let offeringId = "offeringId_example"; // String | offering's id
let channelRequired = new IQualifyManagementApi.ChannelRequired(); // ChannelRequired | 
apiInstance.offeringsOfferingIdChannelsPost(offeringId, channelRequired, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **channelRequired** | [**ChannelRequired**](ChannelRequired.md)|  | 

### Return type

[**ChannelResponse**](ChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

