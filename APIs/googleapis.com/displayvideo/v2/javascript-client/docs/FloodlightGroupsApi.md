# DisplayVideo360Api.FloodlightGroupsApi

All URIs are relative to *https://displayvideo.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**displayvideoFloodlightGroupsFloodlightActivitiesGet**](FloodlightGroupsApi.md#displayvideoFloodlightGroupsFloodlightActivitiesGet) | **GET** /v2/floodlightGroups/{floodlightGroupId}/floodlightActivities/{floodlightActivityId} | 
[**displayvideoFloodlightGroupsFloodlightActivitiesList**](FloodlightGroupsApi.md#displayvideoFloodlightGroupsFloodlightActivitiesList) | **GET** /v2/floodlightGroups/{floodlightGroupId}/floodlightActivities | 
[**displayvideoFloodlightGroupsGet**](FloodlightGroupsApi.md#displayvideoFloodlightGroupsGet) | **GET** /v2/floodlightGroups/{floodlightGroupId} | 



## displayvideoFloodlightGroupsFloodlightActivitiesGet

> FloodlightActivity displayvideoFloodlightGroupsFloodlightActivitiesGet(floodlightGroupId, floodlightActivityId, opts)



Gets a Floodlight activity.

### Example

```javascript
import DisplayVideo360Api from 'display__video_360_api';
let defaultClient = DisplayVideo360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DisplayVideo360Api.FloodlightGroupsApi();
let floodlightGroupId = "floodlightGroupId_example"; // String | Required. The ID of the parent Floodlight group to which the requested Floodlight activity belongs.
let floodlightActivityId = "floodlightActivityId_example"; // String | Required. The ID of the Floodlight activity to fetch.
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
  'partnerId': "partnerId_example" // String | Required. The ID of the partner through which the Floodlight activity is being accessed.
};
apiInstance.displayvideoFloodlightGroupsFloodlightActivitiesGet(floodlightGroupId, floodlightActivityId, opts, (error, data, response) => {
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
 **floodlightGroupId** | **String**| Required. The ID of the parent Floodlight group to which the requested Floodlight activity belongs. | 
 **floodlightActivityId** | **String**| Required. The ID of the Floodlight activity to fetch. | 
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
 **partnerId** | **String**| Required. The ID of the partner through which the Floodlight activity is being accessed. | [optional] 

### Return type

[**FloodlightActivity**](FloodlightActivity.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoFloodlightGroupsFloodlightActivitiesList

> ListFloodlightActivitiesResponse displayvideoFloodlightGroupsFloodlightActivitiesList(floodlightGroupId, opts)



Lists Floodlight activities in a Floodlight group.

### Example

```javascript
import DisplayVideo360Api from 'display__video_360_api';
let defaultClient = DisplayVideo360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DisplayVideo360Api.FloodlightGroupsApi();
let floodlightGroupId = "floodlightGroupId_example"; // String | Required. The ID of the parent Floodlight group to which the requested Floodlight activities belong.
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
  'orderBy': "orderBy_example", // String | Optional. Field by which to sort the list. Acceptable values are: * `displayName` (default) * `floodlightActivityId` The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. Example: `displayName desc`.
  'pageSize': 56, // Number | Optional. Requested page size. Must be between `1` and `100`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
  'pageToken': "pageToken_example", // String | Optional. A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListFloodlightActivities` method. If not specified, the first page of results will be returned.
  'partnerId': "partnerId_example" // String | Required. The ID of the partner through which the Floodlight activities are being accessed.
};
apiInstance.displayvideoFloodlightGroupsFloodlightActivitiesList(floodlightGroupId, opts, (error, data, response) => {
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
 **floodlightGroupId** | **String**| Required. The ID of the parent Floodlight group to which the requested Floodlight activities belong. | 
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
 **orderBy** | **String**| Optional. Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;floodlightActivityId&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;. | [optional] 
 **pageSize** | **Number**| Optional. Requested page size. Must be between &#x60;1&#x60; and &#x60;100&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] 
 **pageToken** | **String**| Optional. A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListFloodlightActivities&#x60; method. If not specified, the first page of results will be returned. | [optional] 
 **partnerId** | **String**| Required. The ID of the partner through which the Floodlight activities are being accessed. | [optional] 

### Return type

[**ListFloodlightActivitiesResponse**](ListFloodlightActivitiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoFloodlightGroupsGet

> FloodlightGroup displayvideoFloodlightGroupsGet(floodlightGroupId, opts)



Gets a Floodlight group.

### Example

```javascript
import DisplayVideo360Api from 'display__video_360_api';
let defaultClient = DisplayVideo360Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DisplayVideo360Api.FloodlightGroupsApi();
let floodlightGroupId = "floodlightGroupId_example"; // String | Required. The ID of the Floodlight group to fetch.
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
  'partnerId': "partnerId_example" // String | Required. The partner context by which the Floodlight group is being accessed.
};
apiInstance.displayvideoFloodlightGroupsGet(floodlightGroupId, opts, (error, data, response) => {
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
 **floodlightGroupId** | **String**| Required. The ID of the Floodlight group to fetch. | 
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
 **partnerId** | **String**| Required. The partner context by which the Floodlight group is being accessed. | [optional] 

### Return type

[**FloodlightGroup**](FloodlightGroup.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

