# YouTubeDataApiV3.MembersApi

All URIs are relative to *https://youtube.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtubeMembersList**](MembersApi.md#youtubeMembersList) | **GET** /youtube/v3/members | 



## youtubeMembersList

> MemberListResponse youtubeMembersList(part, opts)



Retrieves a list of members that match the request criteria for a channel.

### Example

```javascript
import YouTubeDataApiV3 from 'you_tube_data_api_v3';
let defaultClient = YouTubeDataApiV3.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeDataApiV3.MembersApi();
let part = ["null"]; // [String] | The *part* parameter specifies the member resource parts that the API response will include. Set the parameter value to snippet.
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
  'filterByMemberChannelId': "filterByMemberChannelId_example", // String | Comma separated list of channel IDs. Only data about members that are part of this list will be included in the response.
  'hasAccessToLevel': "hasAccessToLevel_example", // String | Filter members in the results set to the ones that have access to a level.
  'maxResults': 56, // Number | The *maxResults* parameter specifies the maximum number of items that should be returned in the result set.
  'mode': "mode_example", // String | Parameter that specifies which channel members to return.
  'pageToken': "pageToken_example" // String | The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved.
};
apiInstance.youtubeMembersList(part, opts, (error, data, response) => {
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
 **part** | [**[String]**](String.md)| The *part* parameter specifies the member resource parts that the API response will include. Set the parameter value to snippet. | 
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
 **filterByMemberChannelId** | **String**| Comma separated list of channel IDs. Only data about members that are part of this list will be included in the response. | [optional] 
 **hasAccessToLevel** | **String**| Filter members in the results set to the ones that have access to a level. | [optional] 
 **maxResults** | **Number**| The *maxResults* parameter specifies the maximum number of items that should be returned in the result set. | [optional] 
 **mode** | **String**| Parameter that specifies which channel members to return. | [optional] 
 **pageToken** | **String**| The *pageToken* parameter identifies a specific page in the result set that should be returned. In an API response, the nextPageToken and prevPageToken properties identify other pages that could be retrieved. | [optional] 

### Return type

[**MemberListResponse**](MemberListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

