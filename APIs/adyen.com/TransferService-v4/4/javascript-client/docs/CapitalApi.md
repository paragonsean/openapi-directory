# TransfersApi.CapitalApi

All URIs are relative to *https://balanceplatform-api-test.adyen.com/btl/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGrants**](CapitalApi.md#getGrants) | **GET** /grants | Get a capital account
[**getGrantsId**](CapitalApi.md#getGrantsId) | **GET** /grants/{id} | Get grant reference details
[**postGrants**](CapitalApi.md#postGrants) | **POST** /grants | Request a grant payout



## getGrants

> CapitalGrants getGrants(opts)

Get a capital account

Returns a list of grants with status and outstanding balances.

### Example

```javascript
import TransfersApi from 'transfers_api';
let defaultClient = TransfersApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: clientKey
let clientKey = defaultClient.authentications['clientKey'];
clientKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientKey.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new TransfersApi.CapitalApi();
let opts = {
  'counterpartyAccountHolderId': "counterpartyAccountHolderId_example" // String | The counterparty account holder id.
};
apiInstance.getGrants(opts, (error, data, response) => {
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
 **counterpartyAccountHolderId** | **String**| The counterparty account holder id. | [optional] 

### Return type

[**CapitalGrants**](CapitalGrants.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGrantsId

> CapitalGrant getGrantsId(id)

Get grant reference details

Returns the details of a capital account specified in the path.

### Example

```javascript
import TransfersApi from 'transfers_api';
let defaultClient = TransfersApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: clientKey
let clientKey = defaultClient.authentications['clientKey'];
clientKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientKey.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new TransfersApi.CapitalApi();
let id = "id_example"; // String | The unique identifier of the grant.
apiInstance.getGrantsId(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the grant. | 

### Return type

[**CapitalGrant**](CapitalGrant.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postGrants

> CapitalGrant postGrants(opts)

Request a grant payout

Requests the payout of the selected grant offer.

### Example

```javascript
import TransfersApi from 'transfers_api';
let defaultClient = TransfersApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: clientKey
let clientKey = defaultClient.authentications['clientKey'];
clientKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientKey.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new TransfersApi.CapitalApi();
let opts = {
  'capitalGrantInfo': new TransfersApi.CapitalGrantInfo() // CapitalGrantInfo | 
};
apiInstance.postGrants(opts, (error, data, response) => {
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
 **capitalGrantInfo** | [**CapitalGrantInfo**](CapitalGrantInfo.md)|  | [optional] 

### Return type

[**CapitalGrant**](CapitalGrant.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [clientKey](../README.md#clientKey), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

