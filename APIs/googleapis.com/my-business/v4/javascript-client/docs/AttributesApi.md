# GoogleMyBusinessApi.AttributesApi

All URIs are relative to *https://mybusiness.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessAttributesList**](AttributesApi.md#mybusinessAttributesList) | **GET** /v4/attributes | 



## mybusinessAttributesList

> ListAttributeMetadataResponse mybusinessAttributesList(opts)



Returns the list of available attributes that would be available for a location with the given primary category and country.

### Example

```javascript
import GoogleMyBusinessApi from 'google_my_business_api';

let apiInstance = new GoogleMyBusinessApi.AttributesApi();
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
  'categoryId': "categoryId_example", // String | The primary category stable ID to find available attributes.
  'country': "country_example", // String | The ISO 3166-1 alpha-2 country code to find available attributes.
  'languageCode': "languageCode_example", // String | The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English.
  'name': "name_example", // String | Resource name of the location to look up available attributes.
  'pageSize': 56, // Number | How many attributes to include per page. Default is 200, minimum is 1.
  'pageToken': "pageToken_example" // String | If specified, the next page of attribute metadata is retrieved. The `pageToken` is returned when a call to `attributes.list` returns more results than can fit into the requested page size.
};
apiInstance.mybusinessAttributesList(opts, (error, data, response) => {
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
 **categoryId** | **String**| The primary category stable ID to find available attributes. | [optional] 
 **country** | **String**| The ISO 3166-1 alpha-2 country code to find available attributes. | [optional] 
 **languageCode** | **String**| The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English. | [optional] 
 **name** | **String**| Resource name of the location to look up available attributes. | [optional] 
 **pageSize** | **Number**| How many attributes to include per page. Default is 200, minimum is 1. | [optional] 
 **pageToken** | **String**| If specified, the next page of attribute metadata is retrieved. The &#x60;pageToken&#x60; is returned when a call to &#x60;attributes.list&#x60; returns more results than can fit into the requested page size. | [optional] 

### Return type

[**ListAttributeMetadataResponse**](ListAttributeMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

