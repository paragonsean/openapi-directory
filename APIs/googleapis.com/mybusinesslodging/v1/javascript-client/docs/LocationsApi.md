# MyBusinessLodgingApi.LocationsApi

All URIs are relative to *https://mybusinesslodging.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinesslodgingLocationsGetLodging**](LocationsApi.md#mybusinesslodgingLocationsGetLodging) | **GET** /v1/{name} | 
[**mybusinesslodgingLocationsLodgingGetGoogleUpdated**](LocationsApi.md#mybusinesslodgingLocationsLodgingGetGoogleUpdated) | **GET** /v1/{name}:getGoogleUpdated | 
[**mybusinesslodgingLocationsUpdateLodging**](LocationsApi.md#mybusinesslodgingLocationsUpdateLodging) | **PATCH** /v1/{name} | 



## mybusinesslodgingLocationsGetLodging

> Lodging mybusinesslodgingLocationsGetLodging(name, opts)



Returns the Lodging of a specific location.

### Example

```javascript
import MyBusinessLodgingApi from 'my_business_lodging_api';

let apiInstance = new MyBusinessLodgingApi.LocationsApi();
let name = "name_example"; // String | Required. Google identifier for this location in the form: `locations/{location_id}/lodging`
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
  'readMask': "readMask_example" // String | Required. The specific fields to return. Use \"*\" to include all fields. Repeated field items cannot be individually specified.
};
apiInstance.mybusinesslodgingLocationsGetLodging(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Google identifier for this location in the form: &#x60;locations/{location_id}/lodging&#x60; | 
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
 **readMask** | **String**| Required. The specific fields to return. Use \&quot;*\&quot; to include all fields. Repeated field items cannot be individually specified. | [optional] 

### Return type

[**Lodging**](Lodging.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinesslodgingLocationsLodgingGetGoogleUpdated

> GetGoogleUpdatedLodgingResponse mybusinesslodgingLocationsLodgingGetGoogleUpdated(name, opts)



Returns the Google updated Lodging of a specific location.

### Example

```javascript
import MyBusinessLodgingApi from 'my_business_lodging_api';

let apiInstance = new MyBusinessLodgingApi.LocationsApi();
let name = "name_example"; // String | Required. Google identifier for this location in the form: `locations/{location_id}/lodging`
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
  'readMask': "readMask_example" // String | Required. The specific fields to return. Use \"*\" to include all fields. Repeated field items cannot be individually specified.
};
apiInstance.mybusinesslodgingLocationsLodgingGetGoogleUpdated(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Google identifier for this location in the form: &#x60;locations/{location_id}/lodging&#x60; | 
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
 **readMask** | **String**| Required. The specific fields to return. Use \&quot;*\&quot; to include all fields. Repeated field items cannot be individually specified. | [optional] 

### Return type

[**GetGoogleUpdatedLodgingResponse**](GetGoogleUpdatedLodgingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinesslodgingLocationsUpdateLodging

> Lodging mybusinesslodgingLocationsUpdateLodging(name, opts)



Updates the Lodging of a specific location.

### Example

```javascript
import MyBusinessLodgingApi from 'my_business_lodging_api';

let apiInstance = new MyBusinessLodgingApi.LocationsApi();
let name = "name_example"; // String | Required. Google identifier for this location in the form: `locations/{location_id}/lodging`
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
  'updateMask': "updateMask_example", // String | Required. The specific fields to update. Use \"*\" to update all fields, which may include unsetting empty fields in the request. Repeated field items cannot be individually updated.
  'lodging': new MyBusinessLodgingApi.Lodging() // Lodging | 
};
apiInstance.mybusinesslodgingLocationsUpdateLodging(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Google identifier for this location in the form: &#x60;locations/{location_id}/lodging&#x60; | 
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
 **updateMask** | **String**| Required. The specific fields to update. Use \&quot;*\&quot; to update all fields, which may include unsetting empty fields in the request. Repeated field items cannot be individually updated. | [optional] 
 **lodging** | [**Lodging**](Lodging.md)|  | [optional] 

### Return type

[**Lodging**](Lodging.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

