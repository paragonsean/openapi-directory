# RebillyRestApi.PaymentTokensApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getToken**](PaymentTokensApi.md#getToken) | **GET** /tokens/{token} | Retrieve a token
[**getTokenCollection**](PaymentTokensApi.md#getTokenCollection) | **GET** /tokens | Retrieve a list of tokens
[**postDigitalWalletValidation**](PaymentTokensApi.md#postDigitalWalletValidation) | **POST** /digital-wallets/validation | Validate a digital wallet session
[**postToken**](PaymentTokensApi.md#postToken) | **POST** /tokens | Create a payment token



## getToken

> CompositeToken getToken(token, opts)

Retrieve a token

Retrieve a token with specified identifier string. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: PublishableApiKey
let PublishableApiKey = defaultClient.authentications['PublishableApiKey'];
PublishableApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//PublishableApiKey.apiKeyPrefix = 'Token';

let apiInstance = new RebillyRestApi.PaymentTokensApi();
let token = "token_example"; // String | The token identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.getToken(token, opts, (error, data, response) => {
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
 **token** | **String**| The token identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**CompositeToken**](CompositeToken.md)

### Authorization

[PublishableApiKey](../README.md#PublishableApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTokenCollection

> [CompositeToken] getTokenCollection(opts)

Retrieve a list of tokens

Retrieve a list of tokens. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.PaymentTokensApi();
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'limit': 56, // Number | The collection items limit.
  'offset': 56 // Number | The collection items offset.
};
apiInstance.getTokenCollection(opts, (error, data, response) => {
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
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **limit** | **Number**| The collection items limit. | [optional] 
 **offset** | **Number**| The collection items offset. | [optional] 

### Return type

[**[CompositeToken]**](CompositeToken.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDigitalWalletValidation

> DigitalWalletValidation postDigitalWalletValidation(digitalWalletValidation)

Validate a digital wallet session

[FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is the recommended way to use when validating a digital wallet session. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: PublishableApiKey
let PublishableApiKey = defaultClient.authentications['PublishableApiKey'];
PublishableApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//PublishableApiKey.apiKeyPrefix = 'Token';

let apiInstance = new RebillyRestApi.PaymentTokensApi();
let digitalWalletValidation = new RebillyRestApi.DigitalWalletValidation(); // DigitalWalletValidation | Digital wallet validation request.
apiInstance.postDigitalWalletValidation(digitalWalletValidation, (error, data, response) => {
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
 **digitalWalletValidation** | [**DigitalWalletValidation**](DigitalWalletValidation.md)| Digital wallet validation request. | 

### Return type

[**DigitalWalletValidation**](DigitalWalletValidation.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT), [PublishableApiKey](../README.md#PublishableApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postToken

> CompositeToken postToken(compositeToken, opts)

Create a payment token

[FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is the recommended way to create a payment token because it minimizes PCI DSS compliance.  Once a payment token is created, it can only be used once.  A payment token expires upon first use or within 30 minutes of the token creation (whichever comes first). 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: PublishableApiKey
let PublishableApiKey = defaultClient.authentications['PublishableApiKey'];
PublishableApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//PublishableApiKey.apiKeyPrefix = 'Token';

let apiInstance = new RebillyRestApi.PaymentTokensApi();
let compositeToken = new RebillyRestApi.CompositeToken(); // CompositeToken | PaymentToken resource.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.postToken(compositeToken, opts, (error, data, response) => {
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
 **compositeToken** | [**CompositeToken**](CompositeToken.md)| PaymentToken resource. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**CompositeToken**](CompositeToken.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT), [PublishableApiKey](../README.md#PublishableApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

