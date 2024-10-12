# AdyenStoredValueApi.GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/StoredValue/v46*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postChangeStatus**](GeneralApi.md#postChangeStatus) | **POST** /changeStatus | Changes the status of the payment method.
[**postCheckBalance**](GeneralApi.md#postCheckBalance) | **POST** /checkBalance | Checks the balance.
[**postIssue**](GeneralApi.md#postIssue) | **POST** /issue | Issues a new card.
[**postLoad**](GeneralApi.md#postLoad) | **POST** /load | Loads the payment method.
[**postMergeBalance**](GeneralApi.md#postMergeBalance) | **POST** /mergeBalance | Merge the balance of two cards.
[**postVoidTransaction**](GeneralApi.md#postVoidTransaction) | **POST** /voidTransaction | Voids a transaction.



## postChangeStatus

> StoredValueStatusChangeResponse postChangeStatus(opts)

Changes the status of the payment method.

Changes the status of the provided payment method to the specified status.

### Example

```javascript
import AdyenStoredValueApi from 'adyen_stored_value_api';
let defaultClient = AdyenStoredValueApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenStoredValueApi.GeneralApi();
let opts = {
  'storedValueStatusChangeRequest': new AdyenStoredValueApi.StoredValueStatusChangeRequest() // StoredValueStatusChangeRequest | 
};
apiInstance.postChangeStatus(opts, (error, data, response) => {
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
 **storedValueStatusChangeRequest** | [**StoredValueStatusChangeRequest**](StoredValueStatusChangeRequest.md)|  | [optional] 

### Return type

[**StoredValueStatusChangeResponse**](StoredValueStatusChangeResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCheckBalance

> StoredValueBalanceCheckResponse postCheckBalance(opts)

Checks the balance.

Checks the balance of the provided payment method.

### Example

```javascript
import AdyenStoredValueApi from 'adyen_stored_value_api';
let defaultClient = AdyenStoredValueApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenStoredValueApi.GeneralApi();
let opts = {
  'storedValueBalanceCheckRequest': new AdyenStoredValueApi.StoredValueBalanceCheckRequest() // StoredValueBalanceCheckRequest | 
};
apiInstance.postCheckBalance(opts, (error, data, response) => {
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
 **storedValueBalanceCheckRequest** | [**StoredValueBalanceCheckRequest**](StoredValueBalanceCheckRequest.md)|  | [optional] 

### Return type

[**StoredValueBalanceCheckResponse**](StoredValueBalanceCheckResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postIssue

> StoredValueIssueResponse postIssue(opts)

Issues a new card.

Issues a new card of the given payment method.

### Example

```javascript
import AdyenStoredValueApi from 'adyen_stored_value_api';
let defaultClient = AdyenStoredValueApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenStoredValueApi.GeneralApi();
let opts = {
  'storedValueIssueRequest': new AdyenStoredValueApi.StoredValueIssueRequest() // StoredValueIssueRequest | 
};
apiInstance.postIssue(opts, (error, data, response) => {
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
 **storedValueIssueRequest** | [**StoredValueIssueRequest**](StoredValueIssueRequest.md)|  | [optional] 

### Return type

[**StoredValueIssueResponse**](StoredValueIssueResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postLoad

> StoredValueLoadResponse postLoad(opts)

Loads the payment method.

Loads the payment method with the specified funds.

### Example

```javascript
import AdyenStoredValueApi from 'adyen_stored_value_api';
let defaultClient = AdyenStoredValueApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenStoredValueApi.GeneralApi();
let opts = {
  'storedValueLoadRequest': new AdyenStoredValueApi.StoredValueLoadRequest() // StoredValueLoadRequest | 
};
apiInstance.postLoad(opts, (error, data, response) => {
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
 **storedValueLoadRequest** | [**StoredValueLoadRequest**](StoredValueLoadRequest.md)|  | [optional] 

### Return type

[**StoredValueLoadResponse**](StoredValueLoadResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postMergeBalance

> StoredValueBalanceMergeResponse postMergeBalance(opts)

Merge the balance of two cards.

Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

### Example

```javascript
import AdyenStoredValueApi from 'adyen_stored_value_api';
let defaultClient = AdyenStoredValueApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenStoredValueApi.GeneralApi();
let opts = {
  'storedValueBalanceMergeRequest': new AdyenStoredValueApi.StoredValueBalanceMergeRequest() // StoredValueBalanceMergeRequest | 
};
apiInstance.postMergeBalance(opts, (error, data, response) => {
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
 **storedValueBalanceMergeRequest** | [**StoredValueBalanceMergeRequest**](StoredValueBalanceMergeRequest.md)|  | [optional] 

### Return type

[**StoredValueBalanceMergeResponse**](StoredValueBalanceMergeResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postVoidTransaction

> StoredValueVoidResponse postVoidTransaction(opts)

Voids a transaction.

Voids the referenced stored value transaction.

### Example

```javascript
import AdyenStoredValueApi from 'adyen_stored_value_api';
let defaultClient = AdyenStoredValueApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenStoredValueApi.GeneralApi();
let opts = {
  'storedValueVoidRequest': new AdyenStoredValueApi.StoredValueVoidRequest() // StoredValueVoidRequest | 
};
apiInstance.postVoidTransaction(opts, (error, data, response) => {
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
 **storedValueVoidRequest** | [**StoredValueVoidRequest**](StoredValueVoidRequest.md)|  | [optional] 

### Return type

[**StoredValueVoidResponse**](StoredValueVoidResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

