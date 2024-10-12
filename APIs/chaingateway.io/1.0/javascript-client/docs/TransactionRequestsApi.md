# ChaingatewayIo.TransactionRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clearAddress**](TransactionRequestsApi.md#clearAddress) | **POST** /clearAddress | clearAddress
[**sendEthereum**](TransactionRequestsApi.md#sendEthereum) | **POST** /sendEthereum | sendEthereum
[**sendToken**](TransactionRequestsApi.md#sendToken) | **POST** /sendToken | sendToken



## clearAddress

> ClearAddress clearAddress(authorization, clearAddressRequest)

clearAddress

Sends all available ethereum funds of an address to a specified receiver address.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.TransactionRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let clearAddressRequest = {"ethereumaddress":"0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8","newaddress":"0xef4943d727e34280a2efa0b3352dfd61f508ee48","password":"padN39QkRA2hJ"}; // ClearAddressRequest | 
apiInstance.clearAddress(authorization, clearAddressRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **clearAddressRequest** | [**ClearAddressRequest**](ClearAddressRequest.md)|  | 

### Return type

[**ClearAddress**](ClearAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEthereum

> SendEthereum sendEthereum(authorization, sendEthereumRequest)

sendEthereum

Sends ethereum from an address controlled by the account to a specified receiver address.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.TransactionRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let sendEthereumRequest = {"amount":0.01,"from":"0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8","password":"padN39QkRA2hJ","to":"0xef4943d727e34280a2efa0b3352dfd61f508ee48"}; // SendEthereumRequest | 
apiInstance.sendEthereum(authorization, sendEthereumRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **sendEthereumRequest** | [**SendEthereumRequest**](SendEthereumRequest.md)|  | 

### Return type

[**SendEthereum**](SendEthereum.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendToken

> SendToken sendToken(authorization, sendTokenRequest)

sendToken

Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.TransactionRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let sendTokenRequest = {"amount":5,"contractaddress":"0xdac17f958d2ee523a2206206994597c13d831ec7","from":"0x3a32c4c31fe8d2a89976af5d284a94a040b44aa8","identifier":"CN562","password":"padN39QkRA2hJ","to":"0xef4943d727e34280a2efa0b3352dfd61f508ee48"}; // SendTokenRequest | 
apiInstance.sendToken(authorization, sendTokenRequest, (error, data, response) => {
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
 **authorization** | **String**| API Key | 
 **sendTokenRequest** | [**SendTokenRequest**](SendTokenRequest.md)|  | 

### Return type

[**SendToken**](SendToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

