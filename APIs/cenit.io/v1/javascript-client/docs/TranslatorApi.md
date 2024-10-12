# CenitIoRestApiSpecification.TranslatorApi

All URIs are relative to *https://cenit.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupTranslatorGet**](TranslatorApi.md#setupTranslatorGet) | **GET** /setup/translator/ | Returns a list of translators
[**setupTranslatorIdDelete**](TranslatorApi.md#setupTranslatorIdDelete) | **DELETE** /setup/translator/{id} | Delete a translator
[**setupTranslatorIdGet**](TranslatorApi.md#setupTranslatorIdGet) | **GET** /setup/translator/{id} | Retrieve an existing translator
[**setupTranslatorPost**](TranslatorApi.md#setupTranslatorPost) | **POST** /setup/translator/ | Create or update a translator



## setupTranslatorGet

> [Translator] setupTranslatorGet()

Returns a list of translators

Returns a list of translators you&#39;ve previously created. The translators are returned in sorted order, with the most recent translator appearing first.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.TranslatorApi();
apiInstance.setupTranslatorGet((error, data, response) => {
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

[**[Translator]**](Translator.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupTranslatorIdDelete

> setupTranslatorIdDelete(id)

Delete a translator

Deletes the specified translator.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.TranslatorApi();
let id = "id_example"; // String | Translator ID.
apiInstance.setupTranslatorIdDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Translator ID. | 

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupTranslatorIdGet

> Translator setupTranslatorIdGet(id)

Retrieve an existing translator

Retrieves the details of an existing translator. You need only supply the unique translator identifier that was returned upon translator creation.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.TranslatorApi();
let id = "id_example"; // String | Translator ID.
apiInstance.setupTranslatorIdGet(id, (error, data, response) => {
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
 **id** | **String**| Translator ID. | 

### Return type

[**Translator**](Translator.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupTranslatorPost

> Translator setupTranslatorPost()

Create or update a translator

Creates or updates the specified translator. Any parameters not provided will be left unchanged.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.TranslatorApi();
apiInstance.setupTranslatorPost((error, data, response) => {
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

[**Translator**](Translator.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

