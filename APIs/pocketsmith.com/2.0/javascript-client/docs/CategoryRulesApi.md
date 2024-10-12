# PocketSmith.CategoryRulesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesIdCategoryRulesPost**](CategoryRulesApi.md#categoriesIdCategoryRulesPost) | **POST** /categories/{id}/category_rules | Create category rule in category
[**usersIdCategoryRulesGet**](CategoryRulesApi.md#usersIdCategoryRulesGet) | **GET** /users/{id}/category_rules | List category rules in user



## categoriesIdCategoryRulesPost

> CategoryRule categoriesIdCategoryRulesPost(id, opts)

Create category rule in category

Creates a rule to allocate a category to transactions.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoryRulesApi();
let id = 42; // Number | The unique identifier of the category.
let opts = {
  'categoriesIdCategoryRulesPostRequest': new PocketSmith.CategoriesIdCategoryRulesPostRequest() // CategoriesIdCategoryRulesPostRequest | 
};
apiInstance.categoriesIdCategoryRulesPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the category. | 
 **categoriesIdCategoryRulesPostRequest** | [**CategoriesIdCategoryRulesPostRequest**](CategoriesIdCategoryRulesPostRequest.md)|  | [optional] 

### Return type

[**CategoryRule**](CategoryRule.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdCategoryRulesGet

> [CategoryRule] usersIdCategoryRulesGet(id)

List category rules in user

Lists all category rules belonging to a user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoryRulesApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdCategoryRulesGet(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the user. | 

### Return type

[**[CategoryRule]**](CategoryRule.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

