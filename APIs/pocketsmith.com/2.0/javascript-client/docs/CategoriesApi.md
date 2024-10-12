# PocketSmith.CategoriesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesIdDelete**](CategoriesApi.md#categoriesIdDelete) | **DELETE** /categories/{id} | Delete category
[**categoriesIdGet**](CategoriesApi.md#categoriesIdGet) | **GET** /categories/{id} | Get category
[**categoriesIdPut**](CategoriesApi.md#categoriesIdPut) | **PUT** /categories/{id} | Update category
[**usersIdCategoriesGet**](CategoriesApi.md#usersIdCategoriesGet) | **GET** /users/{id}/categories | List categories in user
[**usersIdCategoriesPost**](CategoriesApi.md#usersIdCategoriesPost) | **POST** /users/{id}/categories | Create category in user



## categoriesIdDelete

> categoriesIdDelete(id)

Delete category

Deletes a particular category by its ID. This will delete all budgets within the category, and uncategorize all transactions assigned to the category.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoriesApi();
let id = 42; // Number | The unique identifier of the category.
apiInstance.categoriesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| The unique identifier of the category. | 

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdGet

> Category categoriesIdGet(id)

Get category

Gets a particular category by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoriesApi();
let id = 42; // Number | The unique identifier of the category.
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
 **id** | **Number**| The unique identifier of the category. | 

### Return type

[**Category**](Category.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdPut

> Category categoriesIdPut(id, opts)

Update category

Updates a category by its ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoriesApi();
let id = 42; // Number | The unique identifier of the category.
let opts = {
  'categoriesIdPutRequest': new PocketSmith.CategoriesIdPutRequest() // CategoriesIdPutRequest | 
};
apiInstance.categoriesIdPut(id, opts, (error, data, response) => {
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
 **categoriesIdPutRequest** | [**CategoriesIdPutRequest**](CategoriesIdPutRequest.md)|  | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersIdCategoriesGet

> [Category] usersIdCategoriesGet(id)

List categories in user

Lists all categories belonging to a user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoriesApi();
let id = 42; // Number | The unique identifier of the user.
apiInstance.usersIdCategoriesGet(id, (error, data, response) => {
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

[**[Category]**](Category.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersIdCategoriesPost

> Category usersIdCategoriesPost(id, opts)

Create category in user

Creates a category belonging to the user by their ID.

### Example

```javascript
import PocketSmith from 'pocket_smith';
let defaultClient = PocketSmith.ApiClient.instance;
// Configure API key authorization: developerKey
let developerKey = defaultClient.authentications['developerKey'];
developerKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developerKey.apiKeyPrefix = 'Token';

let apiInstance = new PocketSmith.CategoriesApi();
let id = 42; // Number | The unique identifier of the user.
let opts = {
  'usersIdCategoriesPostRequest': new PocketSmith.UsersIdCategoriesPostRequest() // UsersIdCategoriesPostRequest | 
};
apiInstance.usersIdCategoriesPost(id, opts, (error, data, response) => {
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
 **usersIdCategoriesPostRequest** | [**UsersIdCategoriesPostRequest**](UsersIdCategoriesPostRequest.md)|  | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

