# PiratesApi.GenerationApi

All URIs are relative to *http://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pirateGenerateInsultGet**](GenerationApi.md#pirateGenerateInsultGet) | **GET** /pirate/generate/insult | 
[**pirateGenerateLoremIpsumGet**](GenerationApi.md#pirateGenerateLoremIpsumGet) | **GET** /pirate/generate/lorem-ipsum | 
[**pirateGenerateNameGet**](GenerationApi.md#pirateGenerateNameGet) | **GET** /pirate/generate/name | 



## pirateGenerateInsultGet

> pirateGenerateInsultGet(opts)



Generate random pirate insults.

### Example

```javascript
import PiratesApi from 'pirates_api';
let defaultClient = PiratesApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new PiratesApi.GenerationApi();
let opts = {
  'limit': 56 // Number | No of insults to generate
};
apiInstance.pirateGenerateInsultGet(opts, (error, data, response) => {
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
 **limit** | **Number**| No of insults to generate | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pirateGenerateLoremIpsumGet

> pirateGenerateLoremIpsumGet(opts)



Generate pirate lorem ipsum.

### Example

```javascript
import PiratesApi from 'pirates_api';
let defaultClient = PiratesApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new PiratesApi.GenerationApi();
let opts = {
  'type': "type_example", // String | Type of element to generate `paragraphs/sentences/words`.
  'limit': 56 // Number | No of elements to generate
};
apiInstance.pirateGenerateLoremIpsumGet(opts, (error, data, response) => {
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
 **type** | **String**| Type of element to generate &#x60;paragraphs/sentences/words&#x60;. | [optional] 
 **limit** | **Number**| No of elements to generate | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pirateGenerateNameGet

> pirateGenerateNameGet(opts)



Generate random pirate names.

### Example

```javascript
import PiratesApi from 'pirates_api';
let defaultClient = PiratesApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new PiratesApi.GenerationApi();
let opts = {
  'variation': "variation_example", // String | Variation to generate `male/female`.
  'limit': 56 // Number | No of names to generate
};
apiInstance.pirateGenerateNameGet(opts, (error, data, response) => {
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
 **variation** | **String**| Variation to generate &#x60;male/female&#x60;. | [optional] 
 **limit** | **Number**| No of names to generate | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

