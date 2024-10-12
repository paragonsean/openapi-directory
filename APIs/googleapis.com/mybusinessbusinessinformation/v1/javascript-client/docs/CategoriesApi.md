# MyBusinessBusinessInformationApi.CategoriesApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessbusinessinformationCategoriesBatchGet**](CategoriesApi.md#mybusinessbusinessinformationCategoriesBatchGet) | **GET** /v1/categories:batchGet | 
[**mybusinessbusinessinformationCategoriesList**](CategoriesApi.md#mybusinessbusinessinformationCategoriesList) | **GET** /v1/categories | 



## mybusinessbusinessinformationCategoriesBatchGet

> BatchGetCategoriesResponse mybusinessbusinessinformationCategoriesBatchGet(opts)



Returns a list of business categories for the provided language and GConcept ids.

### Example

```javascript
import MyBusinessBusinessInformationApi from 'my_business_business_information_api';

let apiInstance = new MyBusinessBusinessInformationApi.CategoriesApi();
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
  'languageCode': "languageCode_example", // String | Required. The BCP 47 code of language that the category names should be returned in.
  'names': ["null"], // [String] | Required. At least one name must be set. The GConcept ids the localized category names should be returned for. To return details for more than one category, repeat this parameter in the request.
  'regionCode': "regionCode_example", // String | Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language.
  'view': "view_example" // String | Required. Specifies which parts to the Category resource should be returned in the response.
};
apiInstance.mybusinessbusinessinformationCategoriesBatchGet(opts, (error, data, response) => {
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
 **languageCode** | **String**| Required. The BCP 47 code of language that the category names should be returned in. | [optional] 
 **names** | [**[String]**](String.md)| Required. At least one name must be set. The GConcept ids the localized category names should be returned for. To return details for more than one category, repeat this parameter in the request. | [optional] 
 **regionCode** | **String**| Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language. | [optional] 
 **view** | **String**| Required. Specifies which parts to the Category resource should be returned in the response. | [optional] 

### Return type

[**BatchGetCategoriesResponse**](BatchGetCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mybusinessbusinessinformationCategoriesList

> ListCategoriesResponse mybusinessbusinessinformationCategoriesList(opts)



Returns a list of business categories. Search will match the category name but not the category ID. Search only matches the front of a category name (that is, &#39;food&#39; may return &#39;Food Court&#39; but not &#39;Fast Food Restaurant&#39;).

### Example

```javascript
import MyBusinessBusinessInformationApi from 'my_business_business_information_api';

let apiInstance = new MyBusinessBusinessInformationApi.CategoriesApi();
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
  'filter': "filter_example", // String | Optional. Filter string from user. The only field that supported is `displayName`. Eg: `filter=displayName=foo`.
  'languageCode': "languageCode_example", // String | Required. The BCP 47 code of language.
  'pageSize': 56, // Number | Optional. How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100.
  'pageToken': "pageToken_example", // String | Optional. If specified, the next page of categories will be fetched.
  'regionCode': "regionCode_example", // String | Required. The ISO 3166-1 alpha-2 country code.
  'view': "view_example" // String | Required. Specifies which parts to the Category resource should be returned in the response.
};
apiInstance.mybusinessbusinessinformationCategoriesList(opts, (error, data, response) => {
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
 **filter** | **String**| Optional. Filter string from user. The only field that supported is &#x60;displayName&#x60;. Eg: &#x60;filter&#x3D;displayName&#x3D;foo&#x60;. | [optional] 
 **languageCode** | **String**| Required. The BCP 47 code of language. | [optional] 
 **pageSize** | **Number**| Optional. How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100. | [optional] 
 **pageToken** | **String**| Optional. If specified, the next page of categories will be fetched. | [optional] 
 **regionCode** | **String**| Required. The ISO 3166-1 alpha-2 country code. | [optional] 
 **view** | **String**| Required. Specifies which parts to the Category resource should be returned in the response. | [optional] 

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

