# RebillyRestApi.PaymentCardsApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPaymentCard**](PaymentCardsApi.md#getPaymentCard) | **GET** /payment-cards/{id} | Retrieve a Payment Card
[**getPaymentCardCollection**](PaymentCardsApi.md#getPaymentCardCollection) | **GET** /payment-cards | Retrieve a list of Payment Cards
[**patchPaymentCard**](PaymentCardsApi.md#patchPaymentCard) | **PATCH** /payment-cards/{id} | Update a payment card&#39;s values
[**postPaymentCard**](PaymentCardsApi.md#postPaymentCard) | **POST** /payment-cards | Create a Payment Card
[**postPaymentCardDeactivation**](PaymentCardsApi.md#postPaymentCardDeactivation) | **POST** /payment-cards/{id}/deactivation | Deactivate a Payment Card
[**putPaymentCard**](PaymentCardsApi.md#putPaymentCard) | **PUT** /payment-cards/{id} | Create a payment card with predefined ID



## getPaymentCard

> PaymentCard getPaymentCard(id, opts)

Retrieve a Payment Card

Retrieve a Payment Card with specified identifier string. 

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

let apiInstance = new RebillyRestApi.PaymentCardsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.getPaymentCard(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**PaymentCard**](PaymentCard.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaymentCardCollection

> [PaymentCard] getPaymentCardCollection(opts)

Retrieve a list of Payment Cards

Retrieve a list of Payments Cards. 

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

let apiInstance = new RebillyRestApi.PaymentCardsApi();
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'limit': 56, // Number | The collection items limit.
  'offset': 56, // Number | The collection items offset.
  'filter': "filter_example", // String | The collection items filter requires a special format. Use \",\" for multiple allowed values.  Use \";\" for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format. 
  'sort': ["null"], // [String] | The collection items sort field and order (prefix with \"-\" for descending sort).
  'q': "q_example", // String | The partial search of the text fields.
  'expand': "expand_example" // String | Expand a response to get a full related object included inside of the `_embedded` path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info. 
};
apiInstance.getPaymentCardCollection(opts, (error, data, response) => {
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
 **filter** | **String**| The collection items filter requires a special format. Use \&quot;,\&quot; for multiple allowed values.  Use \&quot;;\&quot; for multiple fields. See the [filter guide](https://api-reference.rebilly.com/#section/Using-filter-with-collections) for more options and examples about this format.  | [optional] 
 **sort** | [**[String]**](String.md)| The collection items sort field and order (prefix with \&quot;-\&quot; for descending sort). | [optional] 
 **q** | **String**| The partial search of the text fields. | [optional] 
 **expand** | **String**| Expand a response to get a full related object included inside of the &#x60;_embedded&#x60; path in the response. It accepts a comma-separated list of objects to expand. See the [expand guide](https://api-reference.rebilly.com/#section/Expand-to-include-embedded-objects) for more info.  | [optional] 

### Return type

[**[PaymentCard]**](PaymentCard.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchPaymentCard

> PaymentCard patchPaymentCard(id, opts)

Update a payment card&#39;s values

Update any of the payment card&#39;s values except for the pan. 

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

let apiInstance = new RebillyRestApi.PaymentCardsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'paymentCardUpdatePlain': new RebillyRestApi.PaymentCardUpdatePlain() // PaymentCardUpdatePlain | Payment card.
};
apiInstance.patchPaymentCard(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **paymentCardUpdatePlain** | [**PaymentCardUpdatePlain**](PaymentCardUpdatePlain.md)| Payment card. | [optional] 

### Return type

[**PaymentCard**](PaymentCard.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentCard

> PaymentCard postPaymentCard(postPaymentCardRequest, opts)

Create a Payment Card

Create a Payment Card. 

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

let apiInstance = new RebillyRestApi.PaymentCardsApi();
let postPaymentCardRequest = new RebillyRestApi.PostPaymentCardRequest(); // PostPaymentCardRequest | PaymentCard resource.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.postPaymentCard(postPaymentCardRequest, opts, (error, data, response) => {
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
 **postPaymentCardRequest** | [**PostPaymentCardRequest**](PostPaymentCardRequest.md)| PaymentCard resource. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**PaymentCard**](PaymentCard.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPaymentCardDeactivation

> PaymentCard postPaymentCardDeactivation(id, opts)

Deactivate a Payment Card

Deactivate a Payment Card. 

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

let apiInstance = new RebillyRestApi.PaymentCardsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.postPaymentCardDeactivation(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**PaymentCard**](PaymentCard.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putPaymentCard

> PaymentCard putPaymentCard(id, opts)

Create a payment card with predefined ID

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

let apiInstance = new RebillyRestApi.PaymentCardsApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'postPaymentCardRequest': new RebillyRestApi.PostPaymentCardRequest() // PostPaymentCardRequest | Payment card.
};
apiInstance.putPaymentCard(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **postPaymentCardRequest** | [**PostPaymentCardRequest**](PostPaymentCardRequest.md)| Payment card. | [optional] 

### Return type

[**PaymentCard**](PaymentCard.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

