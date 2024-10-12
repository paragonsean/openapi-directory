# AgcoApi.AuthorizationCategoriesApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizationCategoriesAddUser**](AuthorizationCategoriesApi.md#authorizationCategoriesAddUser) | **POST** /api/v2/AuthorizationCategories/{id}/Users/{userID} | Add a category that a user can see.
[**authorizationCategoriesDelete**](AuthorizationCategoriesApi.md#authorizationCategoriesDelete) | **DELETE** /api/v2/AuthorizationCategories/{id} | Remove an authorization category.
[**authorizationCategoriesGet**](AuthorizationCategoriesApi.md#authorizationCategoriesGet) | **GET** /api/v2/AuthorizationCategories | Get authorization categories.
[**authorizationCategoriesGetUsers**](AuthorizationCategoriesApi.md#authorizationCategoriesGetUsers) | **GET** /api/v2/AuthorizationCategories/Users | Returns a report of access that users have to Authorization Categories.
[**authorizationCategoriesPost**](AuthorizationCategoriesApi.md#authorizationCategoriesPost) | **POST** /api/v2/AuthorizationCategories | Add an authorization category.
[**authorizationCategoriesPut**](AuthorizationCategoriesApi.md#authorizationCategoriesPut) | **PUT** /api/v2/AuthorizationCategories/{id} | Update an authorization category.
[**authorizationCategoriesRemoveUser**](AuthorizationCategoriesApi.md#authorizationCategoriesRemoveUser) | **DELETE** /api/v2/AuthorizationCategories/{id}/Users/{userID} | Deletes a category a user could see.



## authorizationCategoriesAddUser

> authorizationCategoriesAddUser(id, userID)

Add a category that a user can see.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let id = "id_example"; // String | 
let userID = 56; // Number | 
apiInstance.authorizationCategoriesAddUser(id, userID, (error, data, response) => {
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
 **id** | **String**|  | 
 **userID** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## authorizationCategoriesDelete

> authorizationCategoriesDelete(id)

Remove an authorization category.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let id = "id_example"; // String | The ID of the authorization category.
apiInstance.authorizationCategoriesDelete(id, (error, data, response) => {
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
 **id** | **String**| The ID of the authorization category. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## authorizationCategoriesGet

> APIIPagedResponseAuthorizationCodesSharedModelsCategory authorizationCategoriesGet(opts)

Get authorization categories.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'userID': 56, // Number | Optional. Filter by categories visible to the provided user with the provided userID.
  'definitionID': "definitionID_example" // String | Optional. Filter by categories containing a definition with the provided ID.
};
apiInstance.authorizationCategoriesGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **userID** | **Number**| Optional. Filter by categories visible to the provided user with the provided userID. | [optional] 
 **definitionID** | **String**| Optional. Filter by categories containing a definition with the provided ID. | [optional] 

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsCategory**](APIIPagedResponseAuthorizationCodesSharedModelsCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCategoriesGetUsers

> APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport authorizationCategoriesGetUsers(opts)

Returns a report of access that users have to Authorization Categories.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let opts = {
  'limit': 56, // Number | Optional. Defaults to 10.
  'offset': 56, // Number | Optional. Defaults to 0.
  'userIDs': "userIDs_example", // String | Optional. Includes only users with IDs on the provided comma-separated list.
  'categoryIDs': "categoryIDs_example", // String | Optional. Includes only users with categories with IDs on the provided comma-separated list.
  'includeCategories': true, // Boolean | If true, include full Authorization Category detail. Defaults to false.
  'includeUsers': true, // Boolean | If true, include full User detail. Defaults to false.
  'userSearch': "userSearch_example" // String | Optional. Includes only users with a Name, Username, or Email containing the provided value.
};
apiInstance.authorizationCategoriesGetUsers(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. Defaults to 10. | [optional] 
 **offset** | **Number**| Optional. Defaults to 0. | [optional] 
 **userIDs** | **String**| Optional. Includes only users with IDs on the provided comma-separated list. | [optional] 
 **categoryIDs** | **String**| Optional. Includes only users with categories with IDs on the provided comma-separated list. | [optional] 
 **includeCategories** | **Boolean**| If true, include full Authorization Category detail. Defaults to false. | [optional] 
 **includeUsers** | **Boolean**| If true, include full User detail. Defaults to false. | [optional] 
 **userSearch** | **String**| Optional. Includes only users with a Name, Username, or Email containing the provided value. | [optional] 

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport**](APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCategoriesPost

> String authorizationCategoriesPost(authorizationCodesSharedModelsCategory)

Add an authorization category.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let authorizationCodesSharedModelsCategory = new AgcoApi.AuthorizationCodesSharedModelsCategory(); // AuthorizationCodesSharedModelsCategory | An authorization category.
apiInstance.authorizationCategoriesPost(authorizationCodesSharedModelsCategory, (error, data, response) => {
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
 **authorizationCodesSharedModelsCategory** | [**AuthorizationCodesSharedModelsCategory**](AuthorizationCodesSharedModelsCategory.md)| An authorization category. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationCategoriesPut

> authorizationCategoriesPut(id, authorizationCodesSharedModelsCategory)

Update an authorization category.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let id = "id_example"; // String | 
let authorizationCodesSharedModelsCategory = new AgcoApi.AuthorizationCodesSharedModelsCategory(); // AuthorizationCodesSharedModelsCategory | An authorization category.
apiInstance.authorizationCategoriesPut(id, authorizationCodesSharedModelsCategory, (error, data, response) => {
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
 **id** | **String**|  | 
 **authorizationCodesSharedModelsCategory** | [**AuthorizationCodesSharedModelsCategory**](AuthorizationCodesSharedModelsCategory.md)| An authorization category. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## authorizationCategoriesRemoveUser

> authorizationCategoriesRemoveUser(id, userID)

Deletes a category a user could see.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationCategoriesApi();
let id = "id_example"; // String | 
let userID = 56; // Number | 
apiInstance.authorizationCategoriesRemoveUser(id, userID, (error, data, response) => {
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
 **id** | **String**|  | 
 **userID** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

