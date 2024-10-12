# DisplayVideo360Api.CombinedAudiencesApi

All URIs are relative to *https://displayvideo.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**displayvideoCombinedAudiencesGet**](CombinedAudiencesApi.md#displayvideoCombinedAudiencesGet) | **GET** /v1/combinedAudiences/{combinedAudienceId} | 
[**displayvideoCombinedAudiencesList**](CombinedAudiencesApi.md#displayvideoCombinedAudiencesList) | **GET** /v1/combinedAudiences | 



## displayvideoCombinedAudiencesGet

> CombinedAudience displayvideoCombinedAudiencesGet(combinedAudienceId, opts)



Gets a combined audience.

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

let apiInstance = new DisplayVideo360Api.CombinedAudiencesApi();
let combinedAudienceId = "combinedAudienceId_example"; // String | Required. The ID of the combined audience to fetch.
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
  'advertiserId': "advertiserId_example", // String | The ID of the advertiser that has access to the fetched combined audience.
  'partnerId': "partnerId_example" // String | The ID of the partner that has access to the fetched combined audience.
};
apiInstance.displayvideoCombinedAudiencesGet(combinedAudienceId, opts, (error, data, response) => {
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
 **combinedAudienceId** | **String**| Required. The ID of the combined audience to fetch. | 
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
 **advertiserId** | **String**| The ID of the advertiser that has access to the fetched combined audience. | [optional] 
 **partnerId** | **String**| The ID of the partner that has access to the fetched combined audience. | [optional] 

### Return type

[**CombinedAudience**](CombinedAudience.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoCombinedAudiencesList

> ListCombinedAudiencesResponse displayvideoCombinedAudiencesList(opts)



Lists combined audiences. The order is defined by the order_by parameter.

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

let apiInstance = new DisplayVideo360Api.CombinedAudiencesApi();
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
  'advertiserId': "advertiserId_example", // String | The ID of the advertiser that has access to the fetched combined audiences.
  'filter': "filter_example", // String | Allows filtering by combined audience fields. Supported syntax: * Filter expressions for combined audiences can only contain at most one restriction. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `HAS (:)` operator. Supported fields: * `displayName` Examples: * All combined audiences for which the display name contains \"Google\": `displayName : \"Google\"`. The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
  'orderBy': "orderBy_example", // String | Field by which to sort the list. Acceptable values are: * `combinedAudienceId` (default) * `displayName` The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. Example: `displayName desc`.
  'pageSize': 56, // Number | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
  'pageToken': "pageToken_example", // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListCombinedAudiences` method. If not specified, the first page of results will be returned.
  'partnerId': "partnerId_example" // String | The ID of the partner that has access to the fetched combined audiences.
};
apiInstance.displayvideoCombinedAudiencesList(opts, (error, data, response) => {
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
 **advertiserId** | **String**| The ID of the advertiser that has access to the fetched combined audiences. | [optional] 
 **filter** | **String**| Allows filtering by combined audience fields. Supported syntax: * Filter expressions for combined audiences can only contain at most one restriction. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;displayName&#x60; Examples: * All combined audiences for which the display name contains \&quot;Google\&quot;: &#x60;displayName : \&quot;Google\&quot;&#x60;. The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] 
 **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;combinedAudienceId&#x60; (default) * &#x60;displayName&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;. | [optional] 
 **pageSize** | **Number**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] 
 **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCombinedAudiences&#x60; method. If not specified, the first page of results will be returned. | [optional] 
 **partnerId** | **String**| The ID of the partner that has access to the fetched combined audiences. | [optional] 

### Return type

[**ListCombinedAudiencesResponse**](ListCombinedAudiencesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

