# ContentApiForShopping.MerchantsupportApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentMerchantsupportRenderaccountissues**](MerchantsupportApi.md#contentMerchantsupportRenderaccountissues) | **POST** /{merchantId}/merchantsupport/renderaccountissues | 
[**contentMerchantsupportRenderproductissues**](MerchantsupportApi.md#contentMerchantsupportRenderproductissues) | **POST** /{merchantId}/merchantsupport/renderproductissues/{productId} | 



## contentMerchantsupportRenderaccountissues

> RenderAccountIssuesResponse contentMerchantsupportRenderaccountissues(merchantId, opts)



Provide a list of merchant&#39;s issues with a support content and available actions. This content and actions are meant to be rendered and shown in third-party applications.

### Example

```javascript
import ContentApiForShopping from 'content_api_for_shopping';
let defaultClient = ContentApiForShopping.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentApiForShopping.MerchantsupportApi();
let merchantId = "merchantId_example"; // String | Required. The ID of the account to fetch issues for.
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
  'languageCode': "languageCode_example", // String | Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language `en-US`.
  'timeZone': "timeZone_example", // String | Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example 'America/Los_Angeles'. If not set, results will use as a default UTC.
  'renderAccountIssuesRequestPayload': new ContentApiForShopping.RenderAccountIssuesRequestPayload() // RenderAccountIssuesRequestPayload | 
};
apiInstance.contentMerchantsupportRenderaccountissues(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| Required. The ID of the account to fetch issues for. | 
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
 **languageCode** | **String**| Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language &#x60;en-US&#x60;. | [optional] 
 **timeZone** | **String**| Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example &#39;America/Los_Angeles&#39;. If not set, results will use as a default UTC. | [optional] 
 **renderAccountIssuesRequestPayload** | [**RenderAccountIssuesRequestPayload**](RenderAccountIssuesRequestPayload.md)|  | [optional] 

### Return type

[**RenderAccountIssuesResponse**](RenderAccountIssuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contentMerchantsupportRenderproductissues

> RenderProductIssuesResponse contentMerchantsupportRenderproductissues(merchantId, productId, opts)



Provide a list of issues for merchant&#39;s product with a support content and available actions. This content and actions are meant to be rendered and shown in third-party applications.

### Example

```javascript
import ContentApiForShopping from 'content_api_for_shopping';
let defaultClient = ContentApiForShopping.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentApiForShopping.MerchantsupportApi();
let merchantId = "merchantId_example"; // String | Required. The ID of the account that contains the product.
let productId = "productId_example"; // String | Required. The [REST_ID](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.id) of the product to fetch issues for.
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
  'languageCode': "languageCode_example", // String | Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language `en-US`.
  'timeZone': "timeZone_example", // String | Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example 'America/Los_Angeles'. If not set, results will use as a default UTC.
  'renderProductIssuesRequestPayload': new ContentApiForShopping.RenderProductIssuesRequestPayload() // RenderProductIssuesRequestPayload | 
};
apiInstance.contentMerchantsupportRenderproductissues(merchantId, productId, opts, (error, data, response) => {
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
 **merchantId** | **String**| Required. The ID of the account that contains the product. | 
 **productId** | **String**| Required. The [REST_ID](https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.id) of the product to fetch issues for. | 
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
 **languageCode** | **String**| Optional. The [IETF BCP-47](https://tools.ietf.org/html/bcp47) language code used to localize support content. If not set, the result will be in default language &#x60;en-US&#x60;. | [optional] 
 **timeZone** | **String**| Optional. The [IANA](https://www.iana.org/time-zones) timezone used to localize times in support content. For example &#39;America/Los_Angeles&#39;. If not set, results will use as a default UTC. | [optional] 
 **renderProductIssuesRequestPayload** | [**RenderProductIssuesRequestPayload**](RenderProductIssuesRequestPayload.md)|  | [optional] 

### Return type

[**RenderProductIssuesResponse**](RenderProductIssuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

