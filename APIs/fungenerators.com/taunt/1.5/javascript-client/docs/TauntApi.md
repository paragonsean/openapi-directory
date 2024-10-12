# TauntAsAService.TauntApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tauntCategoriesGet**](TauntApi.md#tauntCategoriesGet) | **GET** /taunt/categories | 
[**tauntGenerateGet**](TauntApi.md#tauntGenerateGet) | **GET** /taunt/generate | 



## tauntCategoriesGet

> tauntCategoriesGet(opts)



Get available taunt generation categories.

### Example

```javascript
import TauntAsAService from 'taunt_as_a_service';
let defaultClient = TauntAsAService.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new TauntAsAService.TauntApi();
let opts = {
  'start': 56, // Number | start
  'limit': 56 // Number | limit
};
apiInstance.tauntCategoriesGet(opts, (error, data, response) => {
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


## tauntGenerateGet

> tauntGenerateGet(category, opts)



Generated taunts in the given category

### Example

```javascript
import TauntAsAService from 'taunt_as_a_service';
let defaultClient = TauntAsAService.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new TauntAsAService.TauntApi();
let category = "category_example"; // String | Category to generator taunt from
let opts = {
  'limit': 56 // Number | Limit. Controls number of taunts generated. Max of 5-10 based on the plan
};
apiInstance.tauntGenerateGet(category, opts, (error, data, response) => {
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
 **category** | **String**| Category to generator taunt from | 
 **limit** | **Number**| Limit. Controls number of taunts generated. Max of 5-10 based on the plan | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

