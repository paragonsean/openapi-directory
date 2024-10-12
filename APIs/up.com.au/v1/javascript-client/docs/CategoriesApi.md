# UpApi.CategoriesApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | List categories
[**categoriesIdGet**](CategoriesApi.md#categoriesIdGet) | **GET** /categories/{id} | Retrieve category
[**transactionsTransactionIdRelationshipsCategoryPatch**](CategoriesApi.md#transactionsTransactionIdRelationshipsCategoryPatch) | **PATCH** /transactions/{transactionId}/relationships/category | Categorize transaction



## categoriesGet

> ListCategoriesResponse categoriesGet(opts)

List categories

Retrieve a list of all categories and their ancestry. The returned list is not paginated. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.CategoriesApi();
let opts = {
  'filterParent': "good-life" // String | The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a `404` response. 
};
apiInstance.categoriesGet(opts, (error, data, response) => {
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
 **filterParent** | **String**| The unique identifier of a parent category for which to return only its children. Providing an invalid category identifier results in a &#x60;404&#x60; response.  | [optional] 

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdGet

> GetCategoryResponse categoriesIdGet(id)

Retrieve category

Retrieve a specific category by providing its unique identifier. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.CategoriesApi();
let id = "restaurants-and-cafes"; // String | The unique identifier for the category. 
apiInstance.categoriesIdGet(id, (error, data, response) => {
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
 **id** | **String**| The unique identifier for the category.  | 

### Return type

[**GetCategoryResponse**](GetCategoryResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsTransactionIdRelationshipsCategoryPatch

> transactionsTransactionIdRelationshipsCategoryPatch(transactionId, opts)

Categorize transaction

Updates the category associated with a transaction. Only transactions for which &#x60;isCategorizable&#x60; is set to true support this operation. The &#x60;id&#x60; is taken from the list exposed on &#x60;/categories&#x60; and cannot be one of the top-level (parent) categories. To de-categorize a transaction, set the entire &#x60;data&#x60; key to &#x60;null&#x60;. An HTTP &#x60;204&#x60; is returned on success. The associated category, along with its request URL is also exposed via the &#x60;category&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.CategoriesApi();
let transactionId = "a572c7c3-b637-433c-a4ce-c0be5dcb0a5a"; // String | The unique identifier for the transaction. 
let opts = {
  'updateTransactionCategoryRequest': new UpApi.UpdateTransactionCategoryRequest() // UpdateTransactionCategoryRequest | 
};
apiInstance.transactionsTransactionIdRelationshipsCategoryPatch(transactionId, opts, (error, data, response) => {
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
 **transactionId** | **String**| The unique identifier for the transaction.  | 
 **updateTransactionCategoryRequest** | [**UpdateTransactionCategoryRequest**](UpdateTransactionCategoryRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

