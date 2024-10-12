# DisputesApi.GeneralApi

All URIs are relative to *https://ca-test.adyen.com/ca/services/DisputeService/v30*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postAcceptDispute**](GeneralApi.md#postAcceptDispute) | **POST** /acceptDispute | Accept a dispute
[**postDefendDispute**](GeneralApi.md#postDefendDispute) | **POST** /defendDispute | Defend a dispute
[**postDeleteDisputeDefenseDocument**](GeneralApi.md#postDeleteDisputeDefenseDocument) | **POST** /deleteDisputeDefenseDocument | Delete a defense document
[**postRetrieveApplicableDefenseReasons**](GeneralApi.md#postRetrieveApplicableDefenseReasons) | **POST** /retrieveApplicableDefenseReasons | Get applicable defense reasons
[**postSupplyDefenseDocument**](GeneralApi.md#postSupplyDefenseDocument) | **POST** /supplyDefenseDocument | Supply a defense document



## postAcceptDispute

> AcceptDisputeResponse postAcceptDispute(opts)

Accept a dispute

Accepts a specific dispute.

### Example

```javascript
import DisputesApi from 'disputes_api';
let defaultClient = DisputesApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DisputesApi.GeneralApi();
let opts = {
  'acceptDisputeRequest': new DisputesApi.AcceptDisputeRequest() // AcceptDisputeRequest | 
};
apiInstance.postAcceptDispute(opts, (error, data, response) => {
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
 **acceptDisputeRequest** | [**AcceptDisputeRequest**](AcceptDisputeRequest.md)|  | [optional] 

### Return type

[**AcceptDisputeResponse**](AcceptDisputeResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDefendDispute

> DefendDisputeResponse postDefendDispute(opts)

Defend a dispute

Defends a specific dispute.

### Example

```javascript
import DisputesApi from 'disputes_api';
let defaultClient = DisputesApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DisputesApi.GeneralApi();
let opts = {
  'defendDisputeRequest': new DisputesApi.DefendDisputeRequest() // DefendDisputeRequest | 
};
apiInstance.postDefendDispute(opts, (error, data, response) => {
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
 **defendDisputeRequest** | [**DefendDisputeRequest**](DefendDisputeRequest.md)|  | [optional] 

### Return type

[**DefendDisputeResponse**](DefendDisputeResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDeleteDisputeDefenseDocument

> DeleteDefenseDocumentResponse postDeleteDisputeDefenseDocument(opts)

Delete a defense document

Deletes a specific dispute defense document that was supplied earlier.

### Example

```javascript
import DisputesApi from 'disputes_api';
let defaultClient = DisputesApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DisputesApi.GeneralApi();
let opts = {
  'deleteDefenseDocumentRequest': new DisputesApi.DeleteDefenseDocumentRequest() // DeleteDefenseDocumentRequest | 
};
apiInstance.postDeleteDisputeDefenseDocument(opts, (error, data, response) => {
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
 **deleteDefenseDocumentRequest** | [**DeleteDefenseDocumentRequest**](DeleteDefenseDocumentRequest.md)|  | [optional] 

### Return type

[**DeleteDefenseDocumentResponse**](DeleteDefenseDocumentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postRetrieveApplicableDefenseReasons

> DefenseReasonsResponse postRetrieveApplicableDefenseReasons(opts)

Get applicable defense reasons

Returns a list of all applicable defense reasons to defend a specific dispute.

### Example

```javascript
import DisputesApi from 'disputes_api';
let defaultClient = DisputesApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DisputesApi.GeneralApi();
let opts = {
  'defenseReasonsRequest': new DisputesApi.DefenseReasonsRequest() // DefenseReasonsRequest | 
};
apiInstance.postRetrieveApplicableDefenseReasons(opts, (error, data, response) => {
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
 **defenseReasonsRequest** | [**DefenseReasonsRequest**](DefenseReasonsRequest.md)|  | [optional] 

### Return type

[**DefenseReasonsResponse**](DefenseReasonsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSupplyDefenseDocument

> SupplyDefenseDocumentResponse postSupplyDefenseDocument(opts)

Supply a defense document

Supplies a specific dispute defense document.

### Example

```javascript
import DisputesApi from 'disputes_api';
let defaultClient = DisputesApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DisputesApi.GeneralApi();
let opts = {
  'supplyDefenseDocumentRequest': new DisputesApi.SupplyDefenseDocumentRequest() // SupplyDefenseDocumentRequest | 
};
apiInstance.postSupplyDefenseDocument(opts, (error, data, response) => {
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
 **supplyDefenseDocumentRequest** | [**SupplyDefenseDocumentRequest**](SupplyDefenseDocumentRequest.md)|  | [optional] 

### Return type

[**SupplyDefenseDocumentResponse**](SupplyDefenseDocumentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

