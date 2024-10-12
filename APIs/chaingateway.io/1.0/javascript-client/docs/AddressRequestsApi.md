# ChaingatewayIo.AddressRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAddress**](AddressRequestsApi.md#deleteAddress) | **POST** /deleteAddress | deleteAddress
[**exportAddress**](AddressRequestsApi.md#exportAddress) | **POST** /exportAddress | exportAddress
[**importAddress**](AddressRequestsApi.md#importAddress) | **POST** /importAddress | importAddress
[**listAddresses**](AddressRequestsApi.md#listAddresses) | **POST** /listAddresses | listAddresses
[**newAddress**](AddressRequestsApi.md#newAddress) | **POST** /newAddress | newAddress



## deleteAddress

> DeleteAddress deleteAddress(authorization, deleteAddressRequest)

deleteAddress

Deletes an existing ethereum address. Be careful when using this function.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.AddressRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let deleteAddressRequest = {"ethereumaddress":"0x71892689ed0d79d88ab6ea3783b571b8ece9bee3","password":"padN39QkRA2hJ"}; // DeleteAddressRequest | 
apiInstance.deleteAddress(authorization, deleteAddressRequest, (error, data, response) => {
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
 **deleteAddressRequest** | [**DeleteAddressRequest**](DeleteAddressRequest.md)|  | 

### Return type

[**DeleteAddress**](DeleteAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## exportAddress

> ExportAddress exportAddress(authorization, exportAddressRequest)

exportAddress

Returns all ethereum addresses created with an account.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.AddressRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let exportAddressRequest = {"ethaddress":"0x71892889ed4d79d88ab6ea3783b571b8ece9bef4","password":"padN39QkRA2hJ"}; // ExportAddressRequest | 
apiInstance.exportAddress(authorization, exportAddressRequest, (error, data, response) => {
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
 **exportAddressRequest** | [**ExportAddressRequest**](ExportAddressRequest.md)|  | 

### Return type

[**ExportAddress**](ExportAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importAddress

> ImportAddress importAddress(authorization, importAddressRequest)

importAddress

Returns all ethereum addresses created with an account.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.AddressRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let importAddressRequest = {"content":{"address":"71892889ed4d79d88ab6ea3783b571b8ece9bef4","crypto":{"cipher":"aes-128-ctr","cipherparams":{"iv":"76e6f2497b9f2a8e024fc752a5418a6d"},"ciphertext":"9d74262517b984f9b0560b8f23b5e3340f7be0f56b70cd91ff445dcaf5b1968f","kdf":"scrypt","kdfparams":{"dklen":32,"n":131072,"p":1,"r":8,"salt":"d11d996a7cc4bfad730d4c9b9057eff2c0fb3940b5bfc59db62ae218c14a54f4"},"mac":"dcc342bbbbb8eea97c89b47bafc23de568fc1a48e0bd21ae8d776a95c4704ac9"},"id":"85b790ff-408e-42b8-b123-bec9523964dc","version":3},"filename":"UTC--2020-09-19T10-42-26.196Z--71892889ed4d79d88ab6ea3783b571b8ece9bef4","password":"padN39QkRA2hJ"}; // ImportAddressRequest | 
apiInstance.importAddress(authorization, importAddressRequest, (error, data, response) => {
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
 **importAddressRequest** | [**ImportAddressRequest**](ImportAddressRequest.md)|  | 

### Return type

[**ImportAddress**](ImportAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAddresses

> ListAddresses listAddresses(contentType, authorization)

listAddresses

Returns all ethereum addresses created with an account.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.AddressRequestsApi();
let contentType = "application/json"; // String | 
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
apiInstance.listAddresses(contentType, authorization, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **authorization** | **String**| API Key | 

### Return type

[**ListAddresses**](ListAddresses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## newAddress

> NewAddress newAddress(authorization, newAddressRequest)

newAddress

Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can&#39;t restore access to an address if you lose it.

### Example

```javascript
import ChaingatewayIo from 'chaingateway_io';

let apiInstance = new ChaingatewayIo.AddressRequestsApi();
let authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
let newAddressRequest = {"password":"padN39QkRA2hJ"}; // NewAddressRequest | 
apiInstance.newAddress(authorization, newAddressRequest, (error, data, response) => {
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
 **newAddressRequest** | [**NewAddressRequest**](NewAddressRequest.md)|  | 

### Return type

[**NewAddress**](NewAddress.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

