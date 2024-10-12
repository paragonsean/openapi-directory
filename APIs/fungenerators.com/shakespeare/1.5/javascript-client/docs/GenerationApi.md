# ShakespeareApi.GenerationApi

All URIs are relative to *http://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shakespeareGenerateInsultGet**](GenerationApi.md#shakespeareGenerateInsultGet) | **GET** /shakespeare/generate/insult | 
[**shakespeareGenerateLoremIpsumGet**](GenerationApi.md#shakespeareGenerateLoremIpsumGet) | **GET** /shakespeare/generate/lorem-ipsum | 
[**shakespeareGenerateNameGet**](GenerationApi.md#shakespeareGenerateNameGet) | **GET** /shakespeare/generate/name | 



## shakespeareGenerateInsultGet

> shakespeareGenerateInsultGet(opts)



Generate random Shakespeare style insults.

### Example

```javascript
import ShakespeareApi from 'shakespeare_api';
let defaultClient = ShakespeareApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new ShakespeareApi.GenerationApi();
let opts = {
  'limit': 56 // Number | No of insults to generate
};
apiInstance.shakespeareGenerateInsultGet(opts, (error, data, response) => {
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


## shakespeareGenerateLoremIpsumGet

> shakespeareGenerateLoremIpsumGet(opts)



Generate Shakespeare lorem ipsum.

### Example

```javascript
import ShakespeareApi from 'shakespeare_api';
let defaultClient = ShakespeareApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new ShakespeareApi.GenerationApi();
let opts = {
  'type': "type_example", // String | Type of element to generate `paragraphs/sentences/words`.
  'limit': 56 // Number | No of elements to generate
};
apiInstance.shakespeareGenerateLoremIpsumGet(opts, (error, data, response) => {
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


## shakespeareGenerateNameGet

> shakespeareGenerateNameGet(opts)



Generate random Shakespearen names.

### Example

```javascript
import ShakespeareApi from 'shakespeare_api';
let defaultClient = ShakespeareApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new ShakespeareApi.GenerationApi();
let opts = {
  'variation': "variation_example", // String | Variation to generate `male/female`.
  'limit': 56 // Number | No of names to generate
};
apiInstance.shakespeareGenerateNameGet(opts, (error, data, response) => {
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

