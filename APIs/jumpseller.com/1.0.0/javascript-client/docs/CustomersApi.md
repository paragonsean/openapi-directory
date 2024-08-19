# JumpsellerApi.CustomersApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customersCountJsonGet**](CustomersApi.md#customersCountJsonGet) | **GET** /customers/count.json | Count all Customers.
[**customersEmailEmailJsonGet**](CustomersApi.md#customersEmailEmailJsonGet) | **GET** /customers/email/{email}.json | Retrieve a single Customer by email.
[**customersIdJsonDelete**](CustomersApi.md#customersIdJsonDelete) | **DELETE** /customers/{id}.json | Delete an existing Customer.
[**customersIdJsonGet**](CustomersApi.md#customersIdJsonGet) | **GET** /customers/{id}.json | Retrieve a single Customer by id.
[**customersIdJsonPut**](CustomersApi.md#customersIdJsonPut) | **PUT** /customers/{id}.json | Update a new Customer.
[**customersJsonGet**](CustomersApi.md#customersJsonGet) | **GET** /customers.json | Retrieve all Customers.
[**customersJsonPost**](CustomersApi.md#customersJsonPost) | **POST** /customers.json | Create a new Customer.



## customersCountJsonGet

> Count customersCountJsonGet(login, authtoken)

Count all Customers.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.customersCountJsonGet(login, authtoken, (error, data, response) => {
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

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersEmailEmailJsonGet

> Customer customersEmailEmailJsonGet(login, authtoken, email)

Retrieve a single Customer by email.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let email = "email_example"; // String | Email of the Customer
apiInstance.customersEmailEmailJsonGet(login, authtoken, email, (error, data, response) => {
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
 **email** | **String**| Email of the Customer | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersIdJsonDelete

> String customersIdJsonDelete(login, authtoken, id)

Delete an existing Customer.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
apiInstance.customersIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersIdJsonGet

> Customer customersIdJsonGet(login, authtoken, id)

Retrieve a single Customer by id.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
apiInstance.customersIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersIdJsonPut

> Customer customersIdJsonPut(login, authtoken, id, customerWithPasswordNoID)

Update a new Customer.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
let customerWithPasswordNoID = new JumpsellerApi.CustomerWithPasswordNoID(); // CustomerWithPasswordNoID | Customer parameters.
apiInstance.customersIdJsonPut(login, authtoken, id, customerWithPasswordNoID, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 
 **customerWithPasswordNoID** | [**CustomerWithPasswordNoID**](CustomerWithPasswordNoID.md)| Customer parameters. | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customersJsonGet

> [Customer] customersJsonGet(login, authtoken, opts)

Retrieve all Customers.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.customersJsonGet(login, authtoken, opts, (error, data, response) => {
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

[**[Customer]**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersJsonPost

> Customer customersJsonPost(login, authtoken, customerWithPasswordNoID)

Create a new Customer.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let customerWithPasswordNoID = new JumpsellerApi.CustomerWithPasswordNoID(); // CustomerWithPasswordNoID | Customer parameters.
apiInstance.customersJsonPost(login, authtoken, customerWithPasswordNoID, (error, data, response) => {
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
 **customerWithPasswordNoID** | [**CustomerWithPasswordNoID**](CustomerWithPasswordNoID.md)| Customer parameters. | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

