# NameGenerationApi.NamesApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nameCategoriesGet**](NamesApi.md#nameCategoriesGet) | **GET** /name/categories | 
[**nameGenerateGet**](NamesApi.md#nameGenerateGet) | **GET** /name/generate | 



## nameCategoriesGet

> nameCategoriesGet(opts)



Get available name generation categories.

### Example

```javascript
import NameGenerationApi from 'name_generation_api';
let defaultClient = NameGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NameGenerationApi.NamesApi();
let opts = {
  'start': 56, // Number | start
  'limit': 56 // Number | limit
};
apiInstance.nameCategoriesGet(opts, (error, data, response) => {
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
 **start** | **Number**| start | [optional] 
 **limit** | **Number**| limit | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nameGenerateGet

> nameGenerateGet(category, opts)



Generated names in the given category

### Example

```javascript
import NameGenerationApi from 'name_generation_api';
let defaultClient = NameGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new NameGenerationApi.NamesApi();
let category = "category_example"; // String | Category to generator names from
let opts = {
  'suggest': "suggest_example", // String | Suggestion string if supported by this category generator.
  'start': 56, // Number | start. Controls pagination. Relevant only if suggestion is supported
  'limit': 56, // Number | limit. Controls pagination limit. Relevant only if suggestion is supported
  'variation': "variation_example" // String | Variation if supported ( male/female/any )
};
apiInstance.nameGenerateGet(category, opts, (error, data, response) => {
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
 **category** | **String**| Category to generator names from | 
 **suggest** | **String**| Suggestion string if supported by this category generator. | [optional] 
 **start** | **Number**| start. Controls pagination. Relevant only if suggestion is supported | [optional] 
 **limit** | **Number**| limit. Controls pagination limit. Relevant only if suggestion is supported | [optional] 
 **variation** | **String**| Variation if supported ( male/female/any ) | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

