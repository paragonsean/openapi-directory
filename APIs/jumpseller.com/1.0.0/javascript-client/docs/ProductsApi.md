# JumpsellerApi.ProductsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsAfterIdJsonGet**](ProductsApi.md#productsAfterIdJsonGet) | **GET** /products/after/{id}.json | Retrieves Products after the given id.
[**productsCategoryCategoryIdCountJsonGet**](ProductsApi.md#productsCategoryCategoryIdCountJsonGet) | **GET** /products/category/{category_id}/count.json | Count Products filtered by category.
[**productsCategoryCategoryIdJsonGet**](ProductsApi.md#productsCategoryCategoryIdJsonGet) | **GET** /products/category/{category_id}.json | Retrieve Products filtered by category.
[**productsCountJsonGet**](ProductsApi.md#productsCountJsonGet) | **GET** /products/count.json | Count all Products.
[**productsIdJsonDelete**](ProductsApi.md#productsIdJsonDelete) | **DELETE** /products/{id}.json | Delete an existing Product.
[**productsIdJsonGet**](ProductsApi.md#productsIdJsonGet) | **GET** /products/{id}.json | Retrieve a single Product.
[**productsIdJsonPut**](ProductsApi.md#productsIdJsonPut) | **PUT** /products/{id}.json | Modify an existing Product.
[**productsJsonGet**](ProductsApi.md#productsJsonGet) | **GET** /products.json | Retrieve all Products.
[**productsJsonPost**](ProductsApi.md#productsJsonPost) | **POST** /products.json | Create a new Product.
[**productsSearchJsonGet**](ProductsApi.md#productsSearchJsonGet) | **GET** /products/search.json | Retrieve a Product List from a query.
[**productsStatusStatusCountJsonGet**](ProductsApi.md#productsStatusStatusCountJsonGet) | **GET** /products/status/{status}/count.json | Count Products filtered by status.
[**productsStatusStatusJsonGet**](ProductsApi.md#productsStatusStatusJsonGet) | **GET** /products/status/{status}.json | Retrieve Products filtered by status.



## productsAfterIdJsonGet

> [Product] productsAfterIdJsonGet(login, authtoken, id, opts)

Retrieves Products after the given id.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsAfterIdJsonGet(login, authtoken, id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the Product | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsCategoryCategoryIdCountJsonGet

> Count productsCategoryCategoryIdCountJsonGet(login, authtoken, categoryId, opts)

Count Products filtered by category.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let categoryId = 56; // Number | Category ID of the Product used as filter
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsCategoryCategoryIdCountJsonGet(login, authtoken, categoryId, opts, (error, data, response) => {
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
 **categoryId** | **Number**| Category ID of the Product used as filter | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsCategoryCategoryIdJsonGet

> [Product] productsCategoryCategoryIdJsonGet(login, authtoken, categoryId, opts)

Retrieve Products filtered by category.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let categoryId = 56; // Number | Category ID of the Product used as filter
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsCategoryCategoryIdJsonGet(login, authtoken, categoryId, opts, (error, data, response) => {
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
 **categoryId** | **Number**| Category ID of the Product used as filter | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsCountJsonGet

> Count productsCountJsonGet(login, authtoken)

Count all Products.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.productsCountJsonGet(login, authtoken, (error, data, response) => {
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


## productsIdJsonDelete

> String productsIdJsonDelete(login, authtoken, id)

Delete an existing Product.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
apiInstance.productsIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Product | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdJsonGet

> Product productsIdJsonGet(login, authtoken, id, opts)

Retrieve a single Product.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsIdJsonGet(login, authtoken, id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Product | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdJsonPut

> Product productsIdJsonPut(login, authtoken, id, productEdit, opts)

Modify an existing Product.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let productEdit = new JumpsellerApi.ProductEdit(); // ProductEdit | Product parameters to change
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsIdJsonPut(login, authtoken, id, productEdit, opts, (error, data, response) => {
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
 **id** | **Number**| Id of the Product | 
 **productEdit** | [**ProductEdit**](ProductEdit.md)| Product parameters to change | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsJsonGet

> [Product] productsJsonGet(login, authtoken, opts)

Retrieve all Products.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1, // Number | List page
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsJsonGet(login, authtoken, opts, (error, data, response) => {
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
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsJsonPost

> Product productsJsonPost(login, authtoken, productEdit, opts)

Create a new Product.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let productEdit = new JumpsellerApi.ProductEdit(); // ProductEdit | Product parameters.
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsJsonPost(login, authtoken, productEdit, opts, (error, data, response) => {
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
 **productEdit** | [**ProductEdit**](ProductEdit.md)| Product parameters. | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsSearchJsonGet

> [Product] productsSearchJsonGet(login, authtoken, query, opts)

Retrieve a Product List from a query.

Endpoint example:   &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/products/search.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX&amp;query&#x3D;test&amp;fields&#x3D;name,description  &#x60;&#x60;&#x60;

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let query = "query_example"; // String | Text to query for the Product
let opts = {
  'locale': "locale_example", // String | Locale code of the translation
  'fields': "fields_example" // String | Comma separated values of the fields to query for the Product
};
apiInstance.productsSearchJsonGet(login, authtoken, query, opts, (error, data, response) => {
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
 **query** | **String**| Text to query for the Product | 
 **locale** | **String**| Locale code of the translation | [optional] 
 **fields** | **String**| Comma separated values of the fields to query for the Product | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsStatusStatusCountJsonGet

> Count productsStatusStatusCountJsonGet(login, authtoken, status, opts)

Count Products filtered by status.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let status = "status_example"; // String | Status of the Product used as filter
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsStatusStatusCountJsonGet(login, authtoken, status, opts, (error, data, response) => {
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
 **status** | **String**| Status of the Product used as filter | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsStatusStatusJsonGet

> [Product] productsStatusStatusJsonGet(login, authtoken, status, opts)

Retrieve Products filtered by status.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let status = "status_example"; // String | Status of the Product used as filter
let opts = {
  'locale': "locale_example" // String | Locale code of the translation
};
apiInstance.productsStatusStatusJsonGet(login, authtoken, status, opts, (error, data, response) => {
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
 **status** | **String**| Status of the Product used as filter | 
 **locale** | **String**| Locale code of the translation | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

