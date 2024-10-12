# ContentApiForShopping.SettlementtransactionsApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentSettlementtransactionsList**](SettlementtransactionsApi.md#contentSettlementtransactionsList) | **GET** /{merchantId}/settlementreports/{settlementId}/transactions | 



## contentSettlementtransactionsList

> SettlementtransactionsListResponse contentSettlementtransactionsList(merchantId, settlementId, opts)



Retrieves a list of transactions for the settlement.

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

let apiInstance = new ContentApiForShopping.SettlementtransactionsApi();
let merchantId = "merchantId_example"; // String | The Merchant Center account to list transactions for.
let settlementId = "settlementId_example"; // String | The Google-provided ID of the settlement.
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
  'maxResults': 56, // Number | The maximum number of transactions to return in the response, used for paging. The default value is 200 transactions per page, and the maximum allowed value is 5000 transactions per page.
  'pageToken': "pageToken_example", // String | The token returned by the previous request.
  'transactionIds': ["null"] // [String] | The list of transactions to return. If not set, all transactions will be returned.
};
apiInstance.contentSettlementtransactionsList(merchantId, settlementId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The Merchant Center account to list transactions for. | 
 **settlementId** | **String**| The Google-provided ID of the settlement. | 
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
 **maxResults** | **Number**| The maximum number of transactions to return in the response, used for paging. The default value is 200 transactions per page, and the maximum allowed value is 5000 transactions per page. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 
 **transactionIds** | [**[String]**](String.md)| The list of transactions to return. If not set, all transactions will be returned. | [optional] 

### Return type

[**SettlementtransactionsListResponse**](SettlementtransactionsListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

