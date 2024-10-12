# DisplayVideo360Api.TargetingTypesApi

All URIs are relative to *https://displayvideo.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**displayvideoTargetingTypesTargetingOptionsGet**](TargetingTypesApi.md#displayvideoTargetingTypesTargetingOptionsGet) | **GET** /v2/targetingTypes/{targetingType}/targetingOptions/{targetingOptionId} | 
[**displayvideoTargetingTypesTargetingOptionsList**](TargetingTypesApi.md#displayvideoTargetingTypesTargetingOptionsList) | **GET** /v2/targetingTypes/{targetingType}/targetingOptions | 
[**displayvideoTargetingTypesTargetingOptionsSearch**](TargetingTypesApi.md#displayvideoTargetingTypesTargetingOptionsSearch) | **POST** /v2/targetingTypes/{targetingType}/targetingOptions:search | 



## displayvideoTargetingTypesTargetingOptionsGet

> TargetingOption displayvideoTargetingTypesTargetingOptionsGet(targetingType, targetingOptionId, opts)



Gets a single targeting option.

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

let apiInstance = new DisplayVideo360Api.TargetingTypesApi();
let targetingType = "targetingType_example"; // String | Required. The type of targeting option to retrieve. Accepted values are: * `TARGETING_TYPE_APP_CATEGORY` * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_VIDEO_PLAYER_SIZE` * `TARGETING_TYPE_USER_REWARDED_CONTENT` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_CONTENT_INSTREAM_POSITION` * `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION` * `TARGETING_TYPE_DEVICE_TYPE` * `TARGETING_TYPE_BROWSER` * `TARGETING_TYPE_HOUSEHOLD_INCOME` * `TARGETING_TYPE_ON_SCREEN_POSITION` * `TARGETING_TYPE_CARRIER_AND_ISP` * `TARGETING_TYPE_OPERATING_SYSTEM` * `TARGETING_TYPE_DEVICE_MAKE_MODEL` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_CATEGORY` * `TARGETING_TYPE_VIEWABILITY` * `TARGETING_TYPE_AUTHORIZED_SELLER_STATUS` * `TARGETING_TYPE_LANGUAGE` * `TARGETING_TYPE_GEO_REGION` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_EXCHANGE` * `TARGETING_TYPE_SUB_EXCHANGE` * `TARGETING_TYPE_NATIVE_CONTENT_POSITION` * `TARGETING_TYPE_OMID`
let targetingOptionId = "targetingOptionId_example"; // String | Required. The ID of the of targeting option to retrieve.
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
  'advertiserId': "advertiserId_example" // String | Required. The Advertiser this request is being made in the context of.
};
apiInstance.displayvideoTargetingTypesTargetingOptionsGet(targetingType, targetingOptionId, opts, (error, data, response) => {
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
 **targetingType** | **String**| Required. The type of targeting option to retrieve. Accepted values are: * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; | 
 **targetingOptionId** | **String**| Required. The ID of the of targeting option to retrieve. | 
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
 **advertiserId** | **String**| Required. The Advertiser this request is being made in the context of. | [optional] 

### Return type

[**TargetingOption**](TargetingOption.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoTargetingTypesTargetingOptionsList

> ListTargetingOptionsResponse displayvideoTargetingTypesTargetingOptionsList(targetingType, opts)



Lists targeting options of a given type.

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

let apiInstance = new DisplayVideo360Api.TargetingTypesApi();
let targetingType = "targetingType_example"; // String | Required. The type of targeting option to be listed. Accepted values are: * `TARGETING_TYPE_APP_CATEGORY` * `TARGETING_TYPE_AGE_RANGE` * `TARGETING_TYPE_GENDER` * `TARGETING_TYPE_VIDEO_PLAYER_SIZE` * `TARGETING_TYPE_USER_REWARDED_CONTENT` * `TARGETING_TYPE_PARENTAL_STATUS` * `TARGETING_TYPE_CONTENT_INSTREAM_POSITION` * `TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION` * `TARGETING_TYPE_DEVICE_TYPE` * `TARGETING_TYPE_BROWSER` * `TARGETING_TYPE_HOUSEHOLD_INCOME` * `TARGETING_TYPE_ON_SCREEN_POSITION` * `TARGETING_TYPE_CARRIER_AND_ISP` * `TARGETING_TYPE_OPERATING_SYSTEM` * `TARGETING_TYPE_DEVICE_MAKE_MODEL` * `TARGETING_TYPE_ENVIRONMENT` * `TARGETING_TYPE_CATEGORY` * `TARGETING_TYPE_VIEWABILITY` * `TARGETING_TYPE_AUTHORIZED_SELLER_STATUS` * `TARGETING_TYPE_LANGUAGE` * `TARGETING_TYPE_GEO_REGION` * `TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION` * `TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION` * `TARGETING_TYPE_EXCHANGE` * `TARGETING_TYPE_SUB_EXCHANGE` * `TARGETING_TYPE_NATIVE_CONTENT_POSITION` * `TARGETING_TYPE_OMID`
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
  'advertiserId': "advertiserId_example", // String | Required. The Advertiser this request is being made in the context of.
  'filter': "filter_example", // String | Allows filtering by targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `OR` logical operators. * A restriction has the form of `{field} {operator} {value}`. * All fields must use the `EQUALS (=)` operator. Supported fields: * `carrierAndIspDetails.type` * `geoRegionDetails.geoRegionType` * `targetingOptionId` Examples: * All `GEO REGION` targeting options that belong to sub type `GEO_REGION_TYPE_COUNTRY` or `GEO_REGION_TYPE_STATE`: `geoRegionDetails.geoRegionType=\"GEO_REGION_TYPE_COUNTRY\" OR geoRegionDetails.geoRegionType=\"GEO_REGION_TYPE_STATE\"` * All `CARRIER AND ISP` targeting options that belong to sub type `CARRIER_AND_ISP_TYPE_CARRIER`: `carrierAndIspDetails.type=\"CARRIER_AND_ISP_TYPE_CARRIER\"` The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
  'orderBy': "orderBy_example", // String | Field by which to sort the list. Acceptable values are: * `targetingOptionId` (default) The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. Example: `targetingOptionId desc`.
  'pageSize': 56, // Number | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
  'pageToken': "pageToken_example" // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListTargetingOptions` method. If not specified, the first page of results will be returned.
};
apiInstance.displayvideoTargetingTypesTargetingOptionsList(targetingType, opts, (error, data, response) => {
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
 **targetingType** | **String**| Required. The type of targeting option to be listed. Accepted values are: * &#x60;TARGETING_TYPE_APP_CATEGORY&#x60; * &#x60;TARGETING_TYPE_AGE_RANGE&#x60; * &#x60;TARGETING_TYPE_GENDER&#x60; * &#x60;TARGETING_TYPE_VIDEO_PLAYER_SIZE&#x60; * &#x60;TARGETING_TYPE_USER_REWARDED_CONTENT&#x60; * &#x60;TARGETING_TYPE_PARENTAL_STATUS&#x60; * &#x60;TARGETING_TYPE_CONTENT_INSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION&#x60; * &#x60;TARGETING_TYPE_DEVICE_TYPE&#x60; * &#x60;TARGETING_TYPE_BROWSER&#x60; * &#x60;TARGETING_TYPE_HOUSEHOLD_INCOME&#x60; * &#x60;TARGETING_TYPE_ON_SCREEN_POSITION&#x60; * &#x60;TARGETING_TYPE_CARRIER_AND_ISP&#x60; * &#x60;TARGETING_TYPE_OPERATING_SYSTEM&#x60; * &#x60;TARGETING_TYPE_DEVICE_MAKE_MODEL&#x60; * &#x60;TARGETING_TYPE_ENVIRONMENT&#x60; * &#x60;TARGETING_TYPE_CATEGORY&#x60; * &#x60;TARGETING_TYPE_VIEWABILITY&#x60; * &#x60;TARGETING_TYPE_AUTHORIZED_SELLER_STATUS&#x60; * &#x60;TARGETING_TYPE_LANGUAGE&#x60; * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION&#x60; * &#x60;TARGETING_TYPE_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_SUB_EXCHANGE&#x60; * &#x60;TARGETING_TYPE_NATIVE_CONTENT_POSITION&#x60; * &#x60;TARGETING_TYPE_OMID&#x60; | 
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
 **advertiserId** | **String**| Required. The Advertiser this request is being made in the context of. | [optional] 
 **filter** | **String**| Allows filtering by targeting option fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;OR&#x60; logical operators. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * All fields must use the &#x60;EQUALS (&#x3D;)&#x60; operator. Supported fields: * &#x60;carrierAndIspDetails.type&#x60; * &#x60;geoRegionDetails.geoRegionType&#x60; * &#x60;targetingOptionId&#x60; Examples: * All &#x60;GEO REGION&#x60; targeting options that belong to sub type &#x60;GEO_REGION_TYPE_COUNTRY&#x60; or &#x60;GEO_REGION_TYPE_STATE&#x60;: &#x60;geoRegionDetails.geoRegionType&#x3D;\&quot;GEO_REGION_TYPE_COUNTRY\&quot; OR geoRegionDetails.geoRegionType&#x3D;\&quot;GEO_REGION_TYPE_STATE\&quot;&#x60; * All &#x60;CARRIER AND ISP&#x60; targeting options that belong to sub type &#x60;CARRIER_AND_ISP_TYPE_CARRIER&#x60;: &#x60;carrierAndIspDetails.type&#x3D;\&quot;CARRIER_AND_ISP_TYPE_CARRIER\&quot;&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] 
 **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;targetingOptionId&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;targetingOptionId desc&#x60;. | [optional] 
 **pageSize** | **Number**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] 
 **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListTargetingOptions&#x60; method. If not specified, the first page of results will be returned. | [optional] 

### Return type

[**ListTargetingOptionsResponse**](ListTargetingOptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoTargetingTypesTargetingOptionsSearch

> SearchTargetingOptionsResponse displayvideoTargetingTypesTargetingOptionsSearch(targetingType, opts)



Searches for targeting options of a given type based on the given search terms.

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

let apiInstance = new DisplayVideo360Api.TargetingTypesApi();
let targetingType = "targetingType_example"; // String | Required. The type of targeting options to retrieve. Accepted values are: * `TARGETING_TYPE_GEO_REGION` * `TARGETING_TYPE_POI` * `TARGETING_TYPE_BUSINESS_CHAIN`
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
  'searchTargetingOptionsRequest': new DisplayVideo360Api.SearchTargetingOptionsRequest() // SearchTargetingOptionsRequest | 
};
apiInstance.displayvideoTargetingTypesTargetingOptionsSearch(targetingType, opts, (error, data, response) => {
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
 **targetingType** | **String**| Required. The type of targeting options to retrieve. Accepted values are: * &#x60;TARGETING_TYPE_GEO_REGION&#x60; * &#x60;TARGETING_TYPE_POI&#x60; * &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60; | 
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
 **searchTargetingOptionsRequest** | [**SearchTargetingOptionsRequest**](SearchTargetingOptionsRequest.md)|  | [optional] 

### Return type

[**SearchTargetingOptionsResponse**](SearchTargetingOptionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

