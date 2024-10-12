# YouTubeAnalyticsApi.GroupItemsApi

All URIs are relative to *https://youtubeanalytics.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtubeAnalyticsGroupItemsDelete**](GroupItemsApi.md#youtubeAnalyticsGroupItemsDelete) | **DELETE** /v2/groupItems | 
[**youtubeAnalyticsGroupItemsInsert**](GroupItemsApi.md#youtubeAnalyticsGroupItemsInsert) | **POST** /v2/groupItems | 
[**youtubeAnalyticsGroupItemsList**](GroupItemsApi.md#youtubeAnalyticsGroupItemsList) | **GET** /v2/groupItems | 



## youtubeAnalyticsGroupItemsDelete

> EmptyResponse youtubeAnalyticsGroupItemsDelete(opts)



Removes an item from a group.

### Example

```javascript
import YouTubeAnalyticsApi from 'you_tube_analytics_api';
let defaultClient = YouTubeAnalyticsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeAnalyticsApi.GroupItemsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'id': "id_example", // String | The `id` parameter specifies the YouTube group item ID of the group item that is being deleted.
  'onBehalfOfContentOwner': "onBehalfOfContentOwner_example" // String | This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The `onBehalfOfContentOwner` parameter indicates that the request's authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
};
apiInstance.youtubeAnalyticsGroupItemsDelete(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **id** | **String**| The &#x60;id&#x60; parameter specifies the YouTube group item ID of the group item that is being deleted. | [optional] 
 **onBehalfOfContentOwner** | **String**| This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner. | [optional] 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## youtubeAnalyticsGroupItemsInsert

> GroupItem youtubeAnalyticsGroupItemsInsert(opts)



Creates a group item.

### Example

```javascript
import YouTubeAnalyticsApi from 'you_tube_analytics_api';
let defaultClient = YouTubeAnalyticsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeAnalyticsApi.GroupItemsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'onBehalfOfContentOwner': "onBehalfOfContentOwner_example", // String | This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The `onBehalfOfContentOwner` parameter indicates that the request's authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
  'groupItem': new YouTubeAnalyticsApi.GroupItem() // GroupItem | 
};
apiInstance.youtubeAnalyticsGroupItemsInsert(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **onBehalfOfContentOwner** | **String**| This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner. | [optional] 
 **groupItem** | [**GroupItem**](GroupItem.md)|  | [optional] 

### Return type

[**GroupItem**](GroupItem.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## youtubeAnalyticsGroupItemsList

> ListGroupItemsResponse youtubeAnalyticsGroupItemsList(opts)



Returns a collection of group items that match the API request parameters.

### Example

```javascript
import YouTubeAnalyticsApi from 'you_tube_analytics_api';
let defaultClient = YouTubeAnalyticsApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeAnalyticsApi.GroupItemsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'groupId': "groupId_example", // String | The `groupId` parameter specifies the unique ID of the group for which you want to retrieve group items.
  'onBehalfOfContentOwner': "onBehalfOfContentOwner_example" // String | This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The `onBehalfOfContentOwner` parameter indicates that the request's authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner.
};
apiInstance.youtubeAnalyticsGroupItemsList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **groupId** | **String**| The &#x60;groupId&#x60; parameter specifies the unique ID of the group for which you want to retrieve group items. | [optional] 
 **onBehalfOfContentOwner** | **String**| This parameter can only be used in a properly authorized request. **Note:** This parameter is intended exclusively for YouTube content partners that own and manage many different YouTube channels. The &#x60;onBehalfOfContentOwner&#x60; parameter indicates that the request&#39;s authorization credentials identify a YouTube user who is acting on behalf of the content owner specified in the parameter value. It allows content owners to authenticate once and get access to all their video and channel data, without having to provide authentication credentials for each individual channel. The account that the user authenticates with must be linked to the specified YouTube content owner. | [optional] 

### Return type

[**ListGroupItemsResponse**](ListGroupItemsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

