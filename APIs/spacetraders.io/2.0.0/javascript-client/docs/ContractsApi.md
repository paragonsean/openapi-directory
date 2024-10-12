# SpaceTradersApi.ContractsApi

All URIs are relative to *https://api.spacetraders.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptContract**](ContractsApi.md#acceptContract) | **POST** /my/contracts/{contractId}/accept | Accept Contract
[**deliverContract**](ContractsApi.md#deliverContract) | **POST** /my/contracts/{contractId}/deliver | Deliver Contract
[**fulfillContract**](ContractsApi.md#fulfillContract) | **POST** /my/contracts/{contractId}/fulfill | Fulfill Contract
[**getContract**](ContractsApi.md#getContract) | **GET** /my/contracts/{contractId} | Get Contract
[**getContracts**](ContractsApi.md#getContracts) | **GET** /my/contracts | List Contracts



## acceptContract

> AcceptContract200Response acceptContract(contractId)

Accept Contract

Accept a contract.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.ContractsApi();
let contractId = "contractId_example"; // String | 
apiInstance.acceptContract(contractId, (error, data, response) => {
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
 **contractId** | **String**|  | 

### Return type

[**AcceptContract200Response**](AcceptContract200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deliverContract

> DeliverContract200Response deliverContract(contractId, opts)

Deliver Contract

Deliver cargo on a given contract.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.ContractsApi();
let contractId = "contractId_example"; // String | The ID of the contract
let opts = {
  'deliverContractRequest': new SpaceTradersApi.DeliverContractRequest() // DeliverContractRequest | 
};
apiInstance.deliverContract(contractId, opts, (error, data, response) => {
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
 **contractId** | **String**| The ID of the contract | 
 **deliverContractRequest** | [**DeliverContractRequest**](DeliverContractRequest.md)|  | [optional] 

### Return type

[**DeliverContract200Response**](DeliverContract200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fulfillContract

> FulfillContract200Response fulfillContract(contractId)

Fulfill Contract

Fulfill a contract

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.ContractsApi();
let contractId = "contractId_example"; // String | The ID of the contract
apiInstance.fulfillContract(contractId, (error, data, response) => {
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
 **contractId** | **String**| The ID of the contract | 

### Return type

[**FulfillContract200Response**](FulfillContract200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContract

> GetContract200Response getContract(contractId)

Get Contract

Get the details of a contract by ID.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.ContractsApi();
let contractId = "contractId_example"; // String | The contract ID
apiInstance.getContract(contractId, (error, data, response) => {
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
 **contractId** | **String**| The contract ID | 

### Return type

[**GetContract200Response**](GetContract200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContracts

> GetContracts200Response getContracts(opts)

List Contracts

List all of your contracts.

### Example

```javascript
import SpaceTradersApi from 'space_traders_api';
let defaultClient = SpaceTradersApi.ApiClient.instance;
// Configure Bearer access token for authorization: AgentToken
let AgentToken = defaultClient.authentications['AgentToken'];
AgentToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpaceTradersApi.ContractsApi();
let opts = {
  'page': 56, // Number | What entry offset to request
  'limit': 56 // Number | How many entries to return per page
};
apiInstance.getContracts(opts, (error, data, response) => {
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
 **page** | **Number**| What entry offset to request | [optional] 
 **limit** | **Number**| How many entries to return per page | [optional] 

### Return type

[**GetContracts200Response**](GetContracts200Response.md)

### Authorization

[AgentToken](../README.md#AgentToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

