# JumpsellerApi.CustomerCategoriesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCategoriesIdCustomersJsonDelete**](CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonDelete) | **DELETE** /customer_categories/{id}/customers.json | Delete Customers from an existing CustomerCategory.
[**customerCategoriesIdCustomersJsonGet**](CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonGet) | **GET** /customer_categories/{id}/customers.json | Retrieves the customers in a CustomerCategory.
[**customerCategoriesIdCustomersJsonPost**](CustomerCategoriesApi.md#customerCategoriesIdCustomersJsonPost) | **POST** /customer_categories/{id}/customers.json | Adds Customers to a CustomerCategory.
[**customerCategoriesIdJsonDelete**](CustomerCategoriesApi.md#customerCategoriesIdJsonDelete) | **DELETE** /customer_categories/{id}.json | Delete an existing CustomerCategory.
[**customerCategoriesIdJsonGet**](CustomerCategoriesApi.md#customerCategoriesIdJsonGet) | **GET** /customer_categories/{id}.json | Retrieve a single CustomerCategory.
[**customerCategoriesIdJsonPut**](CustomerCategoriesApi.md#customerCategoriesIdJsonPut) | **PUT** /customer_categories/{id}.json | Update a CustomerCategory.
[**customerCategoriesJsonGet**](CustomerCategoriesApi.md#customerCategoriesJsonGet) | **GET** /customer_categories.json | Retrieve all Customer Categories.
[**customerCategoriesJsonPost**](CustomerCategoriesApi.md#customerCategoriesJsonPost) | **POST** /customer_categories.json | Create a new CustomerCategory.



## customerCategoriesIdCustomersJsonDelete

> String customerCategoriesIdCustomersJsonDelete(login, authtoken, id, customersToCustomerCategory)

Delete Customers from an existing CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomerCategory
let customersToCustomerCategory = new JumpsellerApi.CustomersToCustomerCategory(); // CustomersToCustomerCategory | Customer parameters.
apiInstance.customerCategoriesIdCustomersJsonDelete(login, authtoken, id, customersToCustomerCategory, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomerCategory | 
 **customersToCustomerCategory** | [**CustomersToCustomerCategory**](CustomersToCustomerCategory.md)| Customer parameters. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCategoriesIdCustomersJsonGet

> [Customer] customerCategoriesIdCustomersJsonGet(login, authtoken, id)

Retrieves the customers in a CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomerCategory
apiInstance.customerCategoriesIdCustomersJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomerCategory | 

### Return type

[**[Customer]**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCategoriesIdCustomersJsonPost

> [Customer] customerCategoriesIdCustomersJsonPost(login, authtoken, id, customersToCustomerCategory)

Adds Customers to a CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomerCategory
let customersToCustomerCategory = new JumpsellerApi.CustomersToCustomerCategory(); // CustomersToCustomerCategory | Customer parameters.
apiInstance.customerCategoriesIdCustomersJsonPost(login, authtoken, id, customersToCustomerCategory, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomerCategory | 
 **customersToCustomerCategory** | [**CustomersToCustomerCategory**](CustomersToCustomerCategory.md)| Customer parameters. | 

### Return type

[**[Customer]**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCategoriesIdJsonDelete

> String customerCategoriesIdJsonDelete(login, authtoken, id)

Delete an existing CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomerCategory
apiInstance.customerCategoriesIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomerCategory | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCategoriesIdJsonGet

> CustomerCategory customerCategoriesIdJsonGet(login, authtoken, id)

Retrieve a single CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomerCategory
apiInstance.customerCategoriesIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomerCategory | 

### Return type

[**CustomerCategory**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCategoriesIdJsonPut

> CustomerCategory customerCategoriesIdJsonPut(login, authtoken, id, customerCategoryEdit)

Update a CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomerCategory
let customerCategoryEdit = new JumpsellerApi.CustomerCategoryEdit(); // CustomerCategoryEdit | CustomerCategory parameters.
apiInstance.customerCategoriesIdJsonPut(login, authtoken, id, customerCategoryEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomerCategory | 
 **customerCategoryEdit** | [**CustomerCategoryEdit**](CustomerCategoryEdit.md)| CustomerCategory parameters. | 

### Return type

[**CustomerCategory**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerCategoriesJsonGet

> [CustomerCategory] customerCategoriesJsonGet(login, authtoken, opts)

Retrieve all Customer Categories.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.customerCategoriesJsonGet(login, authtoken, opts, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **limit** | **Number**| List restriction | [optional] [default to 50]
 **page** | **Number**| List page | [optional] [default to 1]

### Return type

[**[CustomerCategory]**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCategoriesJsonPost

> CustomerCategory customerCategoriesJsonPost(login, authtoken, customerCategoryEdit)

Create a new CustomerCategory.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerCategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let customerCategoryEdit = new JumpsellerApi.CustomerCategoryEdit(); // CustomerCategoryEdit | CustomerCategory parameters.
apiInstance.customerCategoriesJsonPost(login, authtoken, customerCategoryEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **customerCategoryEdit** | [**CustomerCategoryEdit**](CustomerCategoryEdit.md)| CustomerCategory parameters. | 

### Return type

[**CustomerCategory**](CustomerCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

