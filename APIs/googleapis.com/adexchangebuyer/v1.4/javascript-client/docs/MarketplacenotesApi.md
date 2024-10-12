# AdExchangeBuyerApi.MarketplacenotesApi

All URIs are relative to *https://www.googleapis.com/adexchangebuyer/v1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adexchangebuyerMarketplacenotesInsert**](MarketplacenotesApi.md#adexchangebuyerMarketplacenotesInsert) | **POST** /proposals/{proposalId}/notes/insert | 
[**adexchangebuyerMarketplacenotesList**](MarketplacenotesApi.md#adexchangebuyerMarketplacenotesList) | **GET** /proposals/{proposalId}/notes | 



## adexchangebuyerMarketplacenotesInsert

> AddOrderNotesResponse adexchangebuyerMarketplacenotesInsert(proposalId, opts)



Add notes to the proposal

### Example

```javascript
import AdExchangeBuyerApi from 'ad_exchange_buyer_api';
let defaultClient = AdExchangeBuyerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdExchangeBuyerApi.MarketplacenotesApi();
let proposalId = "proposalId_example"; // String | The proposalId to add notes for.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'addOrderNotesRequest': new AdExchangeBuyerApi.AddOrderNotesRequest() // AddOrderNotesRequest | 
};
apiInstance.adexchangebuyerMarketplacenotesInsert(proposalId, opts, (error, data, response) => {
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
 **proposalId** | **String**| The proposalId to add notes for. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **addOrderNotesRequest** | [**AddOrderNotesRequest**](AddOrderNotesRequest.md)|  | [optional] 

### Return type

[**AddOrderNotesResponse**](AddOrderNotesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## adexchangebuyerMarketplacenotesList

> GetOrderNotesResponse adexchangebuyerMarketplacenotesList(proposalId, opts)



Get all the notes associated with a proposal

### Example

```javascript
import AdExchangeBuyerApi from 'ad_exchange_buyer_api';
let defaultClient = AdExchangeBuyerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdExchangeBuyerApi.MarketplacenotesApi();
let proposalId = "proposalId_example"; // String | The proposalId to get notes for. To search across all proposals specify order_id = '-' as part of the URL.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'pqlQuery': "pqlQuery_example" // String | Query string to retrieve specific notes. To search the text contents of notes, please use syntax like \"WHERE note.note = \"foo\" or \"WHERE note.note LIKE \"%bar%\"
};
apiInstance.adexchangebuyerMarketplacenotesList(proposalId, opts, (error, data, response) => {
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
 **proposalId** | **String**| The proposalId to get notes for. To search across all proposals specify order_id &#x3D; &#39;-&#39; as part of the URL. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **pqlQuery** | **String**| Query string to retrieve specific notes. To search the text contents of notes, please use syntax like \&quot;WHERE note.note &#x3D; \&quot;foo\&quot; or \&quot;WHERE note.note LIKE \&quot;%bar%\&quot; | [optional] 

### Return type

[**GetOrderNotesResponse**](GetOrderNotesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

