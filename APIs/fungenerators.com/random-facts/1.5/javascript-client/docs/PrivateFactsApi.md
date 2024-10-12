# FactsApi.PrivateFactsApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factDelete**](PrivateFactsApi.md#factDelete) | **DELETE** /fact | 
[**factGet_0**](PrivateFactsApi.md#factGet_0) | **GET** /fact | 
[**factPut**](PrivateFactsApi.md#factPut) | **PUT** /fact | 



## factDelete

> factDelete(id)



Delete a Fact entry identified by the id.

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.PrivateFactsApi();
let id = "id_example"; // String | Fact ID
apiInstance.factDelete(id, (error, data, response) => {
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
 **id** | **String**| Fact ID | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factGet_0

> factGet_0(opts)



Get a Fact belonging to the id.

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.PrivateFactsApi();
let opts = {
  'id': "id_example" // String | ID of the fact to fetch
};
apiInstance.factGet_0(opts, (error, data, response) => {
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
 **id** | **String**| ID of the fact to fetch | [optional] 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## factPut

> factPut(fact, category, subcategory, tags)



Add a Fact entry to the database (private collection).

### Example

```javascript
import FactsApi from 'facts_api';
let defaultClient = FactsApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FactsApi.PrivateFactsApi();
let fact = "fact_example"; // String | Fact Text
let category = "category_example"; // String | Category of the fact
let subcategory = "subcategory_example"; // String | Sub Category of the fact
let tags = "tags_example"; // String | Tags
apiInstance.factPut(fact, category, subcategory, tags, (error, data, response) => {
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
 **fact** | **String**| Fact Text | 
 **category** | **String**| Category of the fact | 
 **subcategory** | **String**| Sub Category of the fact | 
 **tags** | **String**| Tags | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

