# ApiDiscoveryService.ApisApi

All URIs are relative to *https://www.googleapis.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discoveryApisGetRest**](ApisApi.md#discoveryApisGetRest) | **GET** /apis/{api}/{version}/rest | 
[**discoveryApisList**](ApisApi.md#discoveryApisList) | **GET** /apis | 



## discoveryApisGetRest

> RestDescription discoveryApisGetRest(api, version, opts)



Retrieve the description of a particular version of an api.

### Example

```javascript
import ApiDiscoveryService from 'api_discovery_service';

let apiInstance = new ApiDiscoveryService.ApisApi();
let api = "api_example"; // String | The name of the API.
let version = "version_example"; // String | The version of the API.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example" // String | Deprecated. Please use quotaUser instead.
};
apiInstance.discoveryApisGetRest(api, version, opts, (error, data, response) => {
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
 **api** | **String**| The name of the API. | 
 **version** | **String**| The version of the API. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 

### Return type

[**RestDescription**](RestDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## discoveryApisList

> DirectoryList discoveryApisList(opts)



Retrieve the list of APIs supported at this endpoint.

### Example

```javascript
import ApiDiscoveryService from 'api_discovery_service';

let apiInstance = new ApiDiscoveryService.ApisApi();
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'name': "name_example", // String | Only include APIs with the given name.
  'preferred': true // Boolean | Return only the preferred version of an API.
};
apiInstance.discoveryApisList(opts, (error, data, response) => {
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
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **name** | **String**| Only include APIs with the given name. | [optional] 
 **preferred** | **Boolean**| Return only the preferred version of an API. | [optional] 

### Return type

[**DirectoryList**](DirectoryList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

