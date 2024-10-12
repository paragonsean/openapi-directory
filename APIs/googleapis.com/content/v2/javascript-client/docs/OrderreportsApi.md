# ContentApiForShopping.OrderreportsApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentOrderreportsListdisbursements**](OrderreportsApi.md#contentOrderreportsListdisbursements) | **GET** /{merchantId}/orderreports/disbursements | 
[**contentOrderreportsListtransactions**](OrderreportsApi.md#contentOrderreportsListtransactions) | **GET** /{merchantId}/orderreports/disbursements/{disbursementId}/transactions | 



## contentOrderreportsListdisbursements

> OrderreportsListDisbursementsResponse contentOrderreportsListdisbursements(merchantId, opts)



Retrieves a report for disbursements from your Merchant Center account.

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

let apiInstance = new ContentApiForShopping.OrderreportsApi();
let merchantId = "merchantId_example"; // String | The ID of the account that manages the order. This cannot be a multi-client account.
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
  'disbursementEndDate': "disbursementEndDate_example", // String | The last date which disbursements occurred. In ISO 8601 format. Default: current date.
  'disbursementStartDate': "disbursementStartDate_example", // String | The first date which disbursements occurred. In ISO 8601 format.
  'maxResults': 56, // Number | The maximum number of disbursements to return in the response, used for paging.
  'pageToken': "pageToken_example" // String | The token returned by the previous request.
};
apiInstance.contentOrderreportsListdisbursements(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The ID of the account that manages the order. This cannot be a multi-client account. | 
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
 **disbursementEndDate** | **String**| The last date which disbursements occurred. In ISO 8601 format. Default: current date. | [optional] 
 **disbursementStartDate** | **String**| The first date which disbursements occurred. In ISO 8601 format. | [optional] 
 **maxResults** | **Number**| The maximum number of disbursements to return in the response, used for paging. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 

### Return type

[**OrderreportsListDisbursementsResponse**](OrderreportsListDisbursementsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentOrderreportsListtransactions

> OrderreportsListTransactionsResponse contentOrderreportsListtransactions(merchantId, disbursementId, opts)



Retrieves a list of transactions for a disbursement from your Merchant Center account.

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

let apiInstance = new ContentApiForShopping.OrderreportsApi();
let merchantId = "merchantId_example"; // String | The ID of the account that manages the order. This cannot be a multi-client account.
let disbursementId = "disbursementId_example"; // String | The Google-provided ID of the disbursement (found in Wallet).
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
  'maxResults': 56, // Number | The maximum number of disbursements to return in the response, used for paging.
  'pageToken': "pageToken_example", // String | The token returned by the previous request.
  'transactionEndDate': "transactionEndDate_example", // String | The last date in which transaction occurred. In ISO 8601 format. Default: current date.
  'transactionStartDate': "transactionStartDate_example" // String | The first date in which transaction occurred. In ISO 8601 format.
};
apiInstance.contentOrderreportsListtransactions(merchantId, disbursementId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The ID of the account that manages the order. This cannot be a multi-client account. | 
 **disbursementId** | **String**| The Google-provided ID of the disbursement (found in Wallet). | 
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
 **maxResults** | **Number**| The maximum number of disbursements to return in the response, used for paging. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 
 **transactionEndDate** | **String**| The last date in which transaction occurred. In ISO 8601 format. Default: current date. | [optional] 
 **transactionStartDate** | **String**| The first date in which transaction occurred. In ISO 8601 format. | [optional] 

### Return type

[**OrderreportsListTransactionsResponse**](OrderreportsListTransactionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

