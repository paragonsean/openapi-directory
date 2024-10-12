# GoogleMyBusinessApi.CategoriesApi

All URIs are relative to *https://mybusiness.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessCategoriesBatchGet**](CategoriesApi.md#mybusinessCategoriesBatchGet) | **GET** /v4/categories:batchGet | 
[**mybusinessCategoriesList**](CategoriesApi.md#mybusinessCategoriesList) | **GET** /v4/categories | 



## mybusinessCategoriesBatchGet

> BatchGetBusinessCategoriesResponse mybusinessCategoriesBatchGet(opts)



Returns a list of business categories for the provided language and GConcept ids.

### Example

```javascript
import GoogleMyBusinessApi from 'google_my_business_api';

let apiInstance = new GoogleMyBusinessApi.CategoriesApi();
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
  'categoryIds': ["null"], // [String] | Required. At least one name must be set. The GConcept ids the localized category names should be returned for.
  'languageCode': "languageCode_example", // String | Required. The BCP 47 code of language that the category names should be returned in.
  'regionCode': "regionCode_example", // String | Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language.
  'view': "view_example" // String | Required. Specifies which parts to the Category resource should be returned in the response.
};
apiInstance.mybusinessCategoriesBatchGet(opts, (error, data, response) => {
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
 **categoryIds** | [**[String]**](String.md)| Required. At least one name must be set. The GConcept ids the localized category names should be returned for. | [optional] 
 **languageCode** | **String**| Required. The BCP 47 code of language that the category names should be returned in. | [optional] 
 **regionCode** | **String**| Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language. | [optional] 
 **view** | **String**| Required. Specifies which parts to the Category resource should be returned in the response. | [optional] 

### Return type

[**BatchGetBusinessCategoriesResponse**](BatchGetBusinessCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessCategoriesList

> ListBusinessCategoriesResponse mybusinessCategoriesList(opts)



Returns a list of business categories. Search will match the category name but not the category ID. *Note:* Search only matches the front of a category name (that is, &#39;food&#39; may return &#39;Food Court&#39; but not &#39;Fast Food Restaurant&#39;).

### Example

```javascript
import GoogleMyBusinessApi from 'google_my_business_api';

let apiInstance = new GoogleMyBusinessApi.CategoriesApi();
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
  'languageCode': "languageCode_example", // String | The BCP 47 code of language. If the language is not available, it will default to English.
  'pageSize': 56, // Number | How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100.
  'pageToken': "pageToken_example", // String | If specified, the next page of categories will be fetched.
  'regionCode': "regionCode_example", // String | The ISO 3166-1 alpha-2 country code.
  'searchTerm': "searchTerm_example", // String | Optional filter string from user.
  'view': "view_example" // String | Optional. Specifies which parts to the Category resource should be returned in the response.
};
apiInstance.mybusinessCategoriesList(opts, (error, data, response) => {
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
 **languageCode** | **String**| The BCP 47 code of language. If the language is not available, it will default to English. | [optional] 
 **pageSize** | **Number**| How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100. | [optional] 
 **pageToken** | **String**| If specified, the next page of categories will be fetched. | [optional] 
 **regionCode** | **String**| The ISO 3166-1 alpha-2 country code. | [optional] 
 **searchTerm** | **String**| Optional filter string from user. | [optional] 
 **view** | **String**| Optional. Specifies which parts to the Category resource should be returned in the response. | [optional] 

### Return type

[**ListBusinessCategoriesResponse**](ListBusinessCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

