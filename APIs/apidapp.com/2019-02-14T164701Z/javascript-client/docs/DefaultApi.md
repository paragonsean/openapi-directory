# ApiDapp.DefaultApi

All URIs are relative to *https://ethereum.apidapp.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountIdGet**](DefaultApi.md#accountIdGet) | **GET** /account/{id} | 
[**accountIdOptions**](DefaultApi.md#accountIdOptions) | **OPTIONS** /account/{id} | 
[**accountOptions**](DefaultApi.md#accountOptions) | **OPTIONS** /account | 
[**accountPost**](DefaultApi.md#accountPost) | **POST** /account | 
[**blockGet**](DefaultApi.md#blockGet) | **GET** /block | 
[**blockIdGet**](DefaultApi.md#blockIdGet) | **GET** /block/{id} | 
[**blockIdOptions**](DefaultApi.md#blockIdOptions) | **OPTIONS** /block/{id} | 
[**blockIdTransactionGet**](DefaultApi.md#blockIdTransactionGet) | **GET** /block/{id}/transaction | 
[**blockIdTransactionIndexGet**](DefaultApi.md#blockIdTransactionIndexGet) | **GET** /block/{id}/transaction/{index} | 
[**blockIdTransactionIndexOptions**](DefaultApi.md#blockIdTransactionIndexOptions) | **OPTIONS** /block/{id}/transaction/{index} | 
[**blockIdTransactionOptions**](DefaultApi.md#blockIdTransactionOptions) | **OPTIONS** /block/{id}/transaction | 
[**blockOptions**](DefaultApi.md#blockOptions) | **OPTIONS** /block | 
[**blockchainGet**](DefaultApi.md#blockchainGet) | **GET** /blockchain | 
[**blockchainIdGet**](DefaultApi.md#blockchainIdGet) | **GET** /blockchain/{id} | 
[**blockchainIdOptions**](DefaultApi.md#blockchainIdOptions) | **OPTIONS** /blockchain/{id} | 
[**blockchainOptions**](DefaultApi.md#blockchainOptions) | **OPTIONS** /blockchain | 
[**contractIdGet**](DefaultApi.md#contractIdGet) | **GET** /contract/{id} | 
[**contractIdOptions**](DefaultApi.md#contractIdOptions) | **OPTIONS** /contract/{id} | 
[**contractIdPost**](DefaultApi.md#contractIdPost) | **POST** /contract/{id} | 
[**contractOptions**](DefaultApi.md#contractOptions) | **OPTIONS** /contract | 
[**contractPost**](DefaultApi.md#contractPost) | **POST** /contract | 
[**echoOptions**](DefaultApi.md#echoOptions) | **OPTIONS** /echo | 
[**erc20AddressGet**](DefaultApi.md#erc20AddressGet) | **GET** /erc20/{address} | 
[**erc20AddressOptions**](DefaultApi.md#erc20AddressOptions) | **OPTIONS** /erc20/{address} | 
[**erc20AddressPost**](DefaultApi.md#erc20AddressPost) | **POST** /erc20/{address} | 
[**erc20Get**](DefaultApi.md#erc20Get) | **GET** /erc20 | 
[**erc20Options**](DefaultApi.md#erc20Options) | **OPTIONS** /erc20 | 
[**erc20Post**](DefaultApi.md#erc20Post) | **POST** /erc20 | 
[**keyGet**](DefaultApi.md#keyGet) | **GET** /key | 
[**keyKeyDelete**](DefaultApi.md#keyKeyDelete) | **DELETE** /key/{key} | 
[**keyKeyOptions**](DefaultApi.md#keyKeyOptions) | **OPTIONS** /key/{key} | 
[**keyOptions**](DefaultApi.md#keyOptions) | **OPTIONS** /key | 
[**keyPost**](DefaultApi.md#keyPost) | **POST** /key | 
[**rootOptions**](DefaultApi.md#rootOptions) | **OPTIONS** / | 
[**transactionHashGet**](DefaultApi.md#transactionHashGet) | **GET** /transaction/{hash} | 
[**transactionHashOptions**](DefaultApi.md#transactionHashOptions) | **OPTIONS** /transaction/{hash} | 
[**transactionHashReceiptGet**](DefaultApi.md#transactionHashReceiptGet) | **GET** /transaction/{hash}/receipt | 
[**transactionHashReceiptOptions**](DefaultApi.md#transactionHashReceiptOptions) | **OPTIONS** /transaction/{hash}/receipt | 
[**transactionOptions**](DefaultApi.md#transactionOptions) | **OPTIONS** /transaction | 
[**transactionPost**](DefaultApi.md#transactionPost) | **POST** /transaction | 
[**versionGet**](DefaultApi.md#versionGet) | **GET** /version | 
[**versionOptions**](DefaultApi.md#versionOptions) | **OPTIONS** /version | 
[**walletAccountGet**](DefaultApi.md#walletAccountGet) | **GET** /wallet/account | 
[**walletAccountIdContractPost**](DefaultApi.md#walletAccountIdContractPost) | **POST** /wallet/account/{id}/contract | 
[**walletAccountIdErc20Post**](DefaultApi.md#walletAccountIdErc20Post) | **POST** /wallet/account/{id}/erc20 | 
[**walletAccountIdGet**](DefaultApi.md#walletAccountIdGet) | **GET** /wallet/account/{id} | 
[**walletAccountIdOptions**](DefaultApi.md#walletAccountIdOptions) | **OPTIONS** /wallet/account/{id} | 
[**walletAccountIdPayOptions**](DefaultApi.md#walletAccountIdPayOptions) | **OPTIONS** /wallet/account/{id}/pay | 
[**walletAccountIdPayPost**](DefaultApi.md#walletAccountIdPayPost) | **POST** /wallet/account/{id}/pay | 
[**walletAccountOptions**](DefaultApi.md#walletAccountOptions) | **OPTIONS** /wallet/account | 
[**walletAccountPost**](DefaultApi.md#walletAccountPost) | **POST** /wallet/account | 
[**walletGet**](DefaultApi.md#walletGet) | **GET** /wallet | 
[**walletOptions**](DefaultApi.md#walletOptions) | **OPTIONS** /wallet | 
[**walletPost**](DefaultApi.md#walletPost) | **POST** /wallet | 



## accountIdGet

> Object accountIdGet(id)



Get account balance

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.accountIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountIdOptions

> Object accountIdOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.accountIdOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountOptions

> Object accountOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.accountOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountPost

> Object accountPost()



Create new account

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.accountPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockGet

> Object blockGet()



Access detailed block information

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.blockGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockIdGet

> Object blockIdGet(id)



Get information about particular block

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.blockIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockIdOptions

> Object blockIdOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.blockIdOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockIdTransactionGet

> Object blockIdTransactionGet(id)



Get transaction count within block

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.blockIdTransactionGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockIdTransactionIndexGet

> Object blockIdTransactionIndexGet(index, id)



Get information about particular transaction within block

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let index = "index_example"; // String | 
let id = "id_example"; // String | 
apiInstance.blockIdTransactionIndexGet(index, id, (error, data, response) => {
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
 **index** | **String**|  | 
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockIdTransactionIndexOptions

> Object blockIdTransactionIndexOptions(id, index)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
let index = "index_example"; // String | Automatically added
apiInstance.blockIdTransactionIndexOptions(id, index, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **index** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockIdTransactionOptions

> Object blockIdTransactionOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.blockIdTransactionOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockOptions

> Object blockOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.blockOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainGet

> Object blockchainGet()



Get a list of supported blockchains

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.blockchainGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainIdGet

> Object blockchainIdGet(id)



Get information about blockchain woth given id

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.blockchainIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainIdOptions

> Object blockchainIdOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.blockchainIdOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainOptions

> Object blockchainOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.blockchainOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contractIdGet

> Object contractIdGet(id)



Get contract balance

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.contractIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contractIdOptions

> Object contractIdOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.contractIdOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contractIdPost

> Object contractIdPost(id)



Call the contract

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.contractIdPost(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contractOptions

> Object contractOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.contractOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contractPost

> Object contractPost()



Create a new smart contract

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.contractPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## echoOptions

> Object echoOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.echoOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## erc20AddressGet

> Object erc20AddressGet(address)



Get information amout token balance in the account

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let address = "address_example"; // String | 
apiInstance.erc20AddressGet(address, (error, data, response) => {
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
 **address** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## erc20AddressOptions

> Object erc20AddressOptions(address)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let address = "address_example"; // String | Automatically added
apiInstance.erc20AddressOptions(address, (error, data, response) => {
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
 **address** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## erc20AddressPost

> Object erc20AddressPost(address)



Transfer tokens to another account

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let address = "address_example"; // String | 
apiInstance.erc20AddressPost(address, (error, data, response) => {
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
 **address** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## erc20Get

> Object erc20Get()



Get token information such as name, total amount in circulation, etc

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.erc20Get((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## erc20Options

> Object erc20Options()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.erc20Options((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## erc20Post

> Object erc20Post()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.erc20Post((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keyGet

> Object keyGet(opts)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let opts = {
  'token': "token_example" // String | 
};
apiInstance.keyGet(opts, (error, data, response) => {
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
 **token** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keyKeyDelete

> Object keyKeyDelete(key)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let key = "key_example"; // String | 
apiInstance.keyKeyDelete(key, (error, data, response) => {
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
 **key** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keyKeyOptions

> Object keyKeyOptions(key)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let key = "key_example"; // String | Automatically added
apiInstance.keyKeyOptions(key, (error, data, response) => {
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
 **key** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keyOptions

> Object keyOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.keyOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keyPost

> Object keyPost()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.keyPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rootOptions

> Object rootOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.rootOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionHashGet

> Object transactionHashGet(hash)



Get information about transaction by the transaction hash value

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let hash = "hash_example"; // String | 
apiInstance.transactionHashGet(hash, (error, data, response) => {
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
 **hash** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionHashOptions

> Object transactionHashOptions(hash)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let hash = "hash_example"; // String | Automatically added
apiInstance.transactionHashOptions(hash, (error, data, response) => {
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
 **hash** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionHashReceiptGet

> Object transactionHashReceiptGet(hash)



Get receipt detail information

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
let hash = "hash_example"; // String | 
apiInstance.transactionHashReceiptGet(hash, (error, data, response) => {
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
 **hash** | **String**|  | 

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionHashReceiptOptions

> Object transactionHashReceiptOptions(hash)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let hash = "hash_example"; // String | Automatically added
apiInstance.transactionHashReceiptOptions(hash, (error, data, response) => {
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
 **hash** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionOptions

> Object transactionOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.transactionOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionPost

> Object transactionPost()



Create a new transaction. Transfer Ether between accounts

### Example

```javascript
import ApiDapp from 'api_dapp';
let defaultClient = ApiDapp.ApiClient.instance;
// Configure API key authorization: Key2
let Key2 = defaultClient.authentications['Key2'];
Key2.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key2.apiKeyPrefix = 'Token';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.transactionPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[Key2](../README.md#Key2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionGet

> Object versionGet()



Get API version info

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.versionGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## versionOptions

> Object versionOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.versionOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountGet

> Object walletAccountGet()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.walletAccountGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountIdContractPost

> Object walletAccountIdContractPost(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.walletAccountIdContractPost(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountIdErc20Post

> Object walletAccountIdErc20Post(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.walletAccountIdErc20Post(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountIdGet

> Object walletAccountIdGet(id)



Get account balance

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.walletAccountIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountIdOptions

> Object walletAccountIdOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.walletAccountIdOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountIdPayOptions

> Object walletAccountIdPayOptions(id)



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | Automatically added
apiInstance.walletAccountIdPayOptions(id, (error, data, response) => {
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
 **id** | **String**| Automatically added | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountIdPayPost

> Object walletAccountIdPayPost(id)



Send payment from the account held within the wallet

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
let id = "id_example"; // String | 
apiInstance.walletAccountIdPayPost(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountOptions

> Object walletAccountOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.walletAccountOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletAccountPost

> Object walletAccountPost()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.walletAccountPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletGet

> Object walletGet()



Get current account balance

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.walletGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletOptions

> Object walletOptions()



### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.walletOptions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## walletPost

> Object walletPost()



Create personal wallet

### Example

```javascript
import ApiDapp from 'api_dapp';

let apiInstance = new ApiDapp.DefaultApi();
apiInstance.walletPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

