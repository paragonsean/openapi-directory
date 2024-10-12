# DisplayVideo360Api.CustomBiddingAlgorithmsApi

All URIs are relative to *https://displayvideo.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**displayvideoCustomBiddingAlgorithmsCreate**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsCreate) | **POST** /v1/customBiddingAlgorithms | 
[**displayvideoCustomBiddingAlgorithmsGet**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsGet) | **GET** /v1/customBiddingAlgorithms/{customBiddingAlgorithmId} | 
[**displayvideoCustomBiddingAlgorithmsList**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsList) | **GET** /v1/customBiddingAlgorithms | 
[**displayvideoCustomBiddingAlgorithmsPatch**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsPatch) | **PATCH** /v1/customBiddingAlgorithms/{customBiddingAlgorithmId} | 
[**displayvideoCustomBiddingAlgorithmsScriptsCreate**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsScriptsCreate) | **POST** /v1/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts | 
[**displayvideoCustomBiddingAlgorithmsScriptsGet**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsScriptsGet) | **GET** /v1/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts/{customBiddingScriptId} | 
[**displayvideoCustomBiddingAlgorithmsScriptsList**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsScriptsList) | **GET** /v1/customBiddingAlgorithms/{customBiddingAlgorithmId}/scripts | 
[**displayvideoCustomBiddingAlgorithmsUploadScript**](CustomBiddingAlgorithmsApi.md#displayvideoCustomBiddingAlgorithmsUploadScript) | **GET** /v1/customBiddingAlgorithms/{customBiddingAlgorithmId}:uploadScript | 



## displayvideoCustomBiddingAlgorithmsCreate

> CustomBiddingAlgorithm displayvideoCustomBiddingAlgorithmsCreate(opts)



Creates a new custom bidding algorithm. Returns the newly created custom bidding algorithm if successful.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
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
  'customBiddingAlgorithm': new DisplayVideo360Api.CustomBiddingAlgorithm() // CustomBiddingAlgorithm | 
};
apiInstance.displayvideoCustomBiddingAlgorithmsCreate(opts, (error, data, response) => {
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
 **customBiddingAlgorithm** | [**CustomBiddingAlgorithm**](CustomBiddingAlgorithm.md)|  | [optional] 

### Return type

[**CustomBiddingAlgorithm**](CustomBiddingAlgorithm.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsGet

> CustomBiddingAlgorithm displayvideoCustomBiddingAlgorithmsGet(customBiddingAlgorithmId, opts)



Gets a custom bidding algorithm.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
let customBiddingAlgorithmId = "customBiddingAlgorithmId_example"; // String | Required. The ID of the custom bidding algorithm to fetch.
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
  'advertiserId': "advertiserId_example", // String | The ID of the DV360 partner that has access to the custom bidding algorithm.
  'partnerId': "partnerId_example" // String | The ID of the DV360 partner that has access to the custom bidding algorithm.
};
apiInstance.displayvideoCustomBiddingAlgorithmsGet(customBiddingAlgorithmId, opts, (error, data, response) => {
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
 **customBiddingAlgorithmId** | **String**| Required. The ID of the custom bidding algorithm to fetch. | 
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
 **advertiserId** | **String**| The ID of the DV360 partner that has access to the custom bidding algorithm. | [optional] 
 **partnerId** | **String**| The ID of the DV360 partner that has access to the custom bidding algorithm. | [optional] 

### Return type

[**CustomBiddingAlgorithm**](CustomBiddingAlgorithm.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsList

> ListCustomBiddingAlgorithmsResponse displayvideoCustomBiddingAlgorithmsList(opts)



Lists custom bidding algorithms that are accessible to the current user and can be used in bidding stratgies. The order is defined by the order_by parameter.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
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
  'advertiserId': "advertiserId_example", // String | The ID of the DV360 advertiser that has access to the custom bidding algorithm.
  'filter': "filter_example", // String | Allows filtering by custom bidding algorithm fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND`. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * The `customBiddingAlgorithmType` field must use the `EQUALS (=)` operator. * The `displayName` field must use the `HAS (:)` operator. Supported fields: * `customBiddingAlgorithmType` * `displayName` Examples: * All custom bidding algorithms for which the display name contains \"politics\": `displayName:\"politics\"`. * All custom bidding algorithms for which the type is \"SCRIPT_BASED\": `customBiddingAlgorithmType=SCRIPT_BASED` The length of this field should be no more than 500 characters. Reference our [filter `LIST` requests](/display-video/api/guides/how-tos/filters) guide for more information.
  'orderBy': "orderBy_example", // String | Field by which to sort the list. Acceptable values are: * `displayName` (default) The default sorting order is ascending. To specify descending order for a field, a suffix \"desc\" should be added to the field name. Example: `displayName desc`.
  'pageSize': 56, // Number | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
  'pageToken': "pageToken_example", // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListCustomBiddingAlgorithms` method. If not specified, the first page of results will be returned.
  'partnerId': "partnerId_example" // String | The ID of the DV360 partner that has access to the custom bidding algorithm.
};
apiInstance.displayvideoCustomBiddingAlgorithmsList(opts, (error, data, response) => {
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
 **advertiserId** | **String**| The ID of the DV360 advertiser that has access to the custom bidding algorithm. | [optional] 
 **filter** | **String**| Allows filtering by custom bidding algorithm fields. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60;. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * The &#x60;customBiddingAlgorithmType&#x60; field must use the &#x60;EQUALS (&#x3D;)&#x60; operator. * The &#x60;displayName&#x60; field must use the &#x60;HAS (:)&#x60; operator. Supported fields: * &#x60;customBiddingAlgorithmType&#x60; * &#x60;displayName&#x60; Examples: * All custom bidding algorithms for which the display name contains \&quot;politics\&quot;: &#x60;displayName:\&quot;politics\&quot;&#x60;. * All custom bidding algorithms for which the type is \&quot;SCRIPT_BASED\&quot;: &#x60;customBiddingAlgorithmType&#x3D;SCRIPT_BASED&#x60; The length of this field should be no more than 500 characters. Reference our [filter &#x60;LIST&#x60; requests](/display-video/api/guides/how-tos/filters) guide for more information. | [optional] 
 **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;. | [optional] 
 **pageSize** | **Number**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] 
 **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCustomBiddingAlgorithms&#x60; method. If not specified, the first page of results will be returned. | [optional] 
 **partnerId** | **String**| The ID of the DV360 partner that has access to the custom bidding algorithm. | [optional] 

### Return type

[**ListCustomBiddingAlgorithmsResponse**](ListCustomBiddingAlgorithmsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsPatch

> CustomBiddingAlgorithm displayvideoCustomBiddingAlgorithmsPatch(customBiddingAlgorithmId, opts)



Updates an existing custom bidding algorithm. Returns the updated custom bidding algorithm if successful.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
let customBiddingAlgorithmId = "customBiddingAlgorithmId_example"; // String | Output only. The unique ID of the custom bidding algorithm. Assigned by the system.
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
  'updateMask': "updateMask_example", // String | Required. The mask to control which fields to update.
  'customBiddingAlgorithm': new DisplayVideo360Api.CustomBiddingAlgorithm() // CustomBiddingAlgorithm | 
};
apiInstance.displayvideoCustomBiddingAlgorithmsPatch(customBiddingAlgorithmId, opts, (error, data, response) => {
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
 **customBiddingAlgorithmId** | **String**| Output only. The unique ID of the custom bidding algorithm. Assigned by the system. | 
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
 **updateMask** | **String**| Required. The mask to control which fields to update. | [optional] 
 **customBiddingAlgorithm** | [**CustomBiddingAlgorithm**](CustomBiddingAlgorithm.md)|  | [optional] 

### Return type

[**CustomBiddingAlgorithm**](CustomBiddingAlgorithm.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsScriptsCreate

> CustomBiddingScript displayvideoCustomBiddingAlgorithmsScriptsCreate(customBiddingAlgorithmId, opts)



Creates a new custom bidding script. Returns the newly created script if successful.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
let customBiddingAlgorithmId = "customBiddingAlgorithmId_example"; // String | Required. The ID of the custom bidding algorithm that owns the script.
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
  'advertiserId': "advertiserId_example", // String | The ID of the advertiser that owns the parent custom bidding algorithm.
  'partnerId': "partnerId_example", // String | The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
  'customBiddingScript': new DisplayVideo360Api.CustomBiddingScript() // CustomBiddingScript | 
};
apiInstance.displayvideoCustomBiddingAlgorithmsScriptsCreate(customBiddingAlgorithmId, opts, (error, data, response) => {
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
 **customBiddingAlgorithmId** | **String**| Required. The ID of the custom bidding algorithm that owns the script. | 
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
 **advertiserId** | **String**| The ID of the advertiser that owns the parent custom bidding algorithm. | [optional] 
 **partnerId** | **String**| The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script. | [optional] 
 **customBiddingScript** | [**CustomBiddingScript**](CustomBiddingScript.md)|  | [optional] 

### Return type

[**CustomBiddingScript**](CustomBiddingScript.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsScriptsGet

> CustomBiddingScript displayvideoCustomBiddingAlgorithmsScriptsGet(customBiddingAlgorithmId, customBiddingScriptId, opts)



Gets a custom bidding script.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
let customBiddingAlgorithmId = "customBiddingAlgorithmId_example"; // String | Required. The ID of the custom bidding algorithm owns the script.
let customBiddingScriptId = "customBiddingScriptId_example"; // String | Required. The ID of the custom bidding script to fetch.
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
  'advertiserId': "advertiserId_example", // String | The ID of the advertiser that owns the parent custom bidding algorithm.
  'partnerId': "partnerId_example" // String | The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
};
apiInstance.displayvideoCustomBiddingAlgorithmsScriptsGet(customBiddingAlgorithmId, customBiddingScriptId, opts, (error, data, response) => {
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
 **customBiddingAlgorithmId** | **String**| Required. The ID of the custom bidding algorithm owns the script. | 
 **customBiddingScriptId** | **String**| Required. The ID of the custom bidding script to fetch. | 
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
 **advertiserId** | **String**| The ID of the advertiser that owns the parent custom bidding algorithm. | [optional] 
 **partnerId** | **String**| The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script. | [optional] 

### Return type

[**CustomBiddingScript**](CustomBiddingScript.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsScriptsList

> ListCustomBiddingScriptsResponse displayvideoCustomBiddingAlgorithmsScriptsList(customBiddingAlgorithmId, opts)



Lists custom bidding scripts that belong to the given algorithm. The order is defined by the order_by parameter.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
let customBiddingAlgorithmId = "customBiddingAlgorithmId_example"; // String | Required. The ID of the custom bidding algorithm owns the script.
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
  'advertiserId': "advertiserId_example", // String | The ID of the advertiser that owns the parent custom bidding algorithm.
  'orderBy': "orderBy_example", // String | Field by which to sort the list. Acceptable values are: * `createTime desc` (default) The default sorting order is descending. To specify ascending order for a field, the suffix \"desc\" should be removed. Example: `createTime`.
  'pageSize': 56, // Number | Requested page size. Must be between `1` and `200`. If unspecified will default to `100`. Returns error code `INVALID_ARGUMENT` if an invalid value is specified.
  'pageToken': "pageToken_example", // String | A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to `ListCustomBiddingScripts` method. If not specified, the first page of results will be returned.
  'partnerId': "partnerId_example" // String | The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
};
apiInstance.displayvideoCustomBiddingAlgorithmsScriptsList(customBiddingAlgorithmId, opts, (error, data, response) => {
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
 **customBiddingAlgorithmId** | **String**| Required. The ID of the custom bidding algorithm owns the script. | 
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
 **advertiserId** | **String**| The ID of the advertiser that owns the parent custom bidding algorithm. | [optional] 
 **orderBy** | **String**| Field by which to sort the list. Acceptable values are: * &#x60;createTime desc&#x60; (default) The default sorting order is descending. To specify ascending order for a field, the suffix \&quot;desc\&quot; should be removed. Example: &#x60;createTime&#x60;. | [optional] 
 **pageSize** | **Number**| Requested page size. Must be between &#x60;1&#x60; and &#x60;200&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified. | [optional] 
 **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListCustomBiddingScripts&#x60; method. If not specified, the first page of results will be returned. | [optional] 
 **partnerId** | **String**| The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script. | [optional] 

### Return type

[**ListCustomBiddingScriptsResponse**](ListCustomBiddingScriptsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## displayvideoCustomBiddingAlgorithmsUploadScript

> CustomBiddingScriptRef displayvideoCustomBiddingAlgorithmsUploadScript(customBiddingAlgorithmId, opts)



Creates a custom bidding script reference object for a script file. The resulting reference object provides a resource path to which the script file should be uploaded. This reference object should be included in when creating a new custom bidding script object.

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

let apiInstance = new DisplayVideo360Api.CustomBiddingAlgorithmsApi();
let customBiddingAlgorithmId = "customBiddingAlgorithmId_example"; // String | Required. The ID of the custom bidding algorithm owns the script.
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
  'advertiserId': "advertiserId_example", // String | The ID of the advertiser that owns the parent custom bidding algorithm.
  'partnerId': "partnerId_example" // String | The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script.
};
apiInstance.displayvideoCustomBiddingAlgorithmsUploadScript(customBiddingAlgorithmId, opts, (error, data, response) => {
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
 **customBiddingAlgorithmId** | **String**| Required. The ID of the custom bidding algorithm owns the script. | 
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
 **advertiserId** | **String**| The ID of the advertiser that owns the parent custom bidding algorithm. | [optional] 
 **partnerId** | **String**| The ID of the partner that owns the parent custom bidding algorithm. Only this partner will have write access to this custom bidding script. | [optional] 

### Return type

[**CustomBiddingScriptRef**](CustomBiddingScriptRef.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

