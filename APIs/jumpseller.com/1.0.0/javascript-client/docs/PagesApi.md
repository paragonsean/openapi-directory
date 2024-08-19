# JumpsellerApi.PagesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pagesCountJsonGet**](PagesApi.md#pagesCountJsonGet) | **GET** /pages/count.json | Count all Pages.
[**pagesIdJsonDelete**](PagesApi.md#pagesIdJsonDelete) | **DELETE** /pages/{id}.json | Delete an existing Page.
[**pagesIdJsonGet**](PagesApi.md#pagesIdJsonGet) | **GET** /pages/{id}.json | Retrieve a single Page by id.
[**pagesIdJsonPut**](PagesApi.md#pagesIdJsonPut) | **PUT** /pages/{id}.json | Update a Page.
[**pagesJsonGet**](PagesApi.md#pagesJsonGet) | **GET** /pages.json | Retrieve all Pages.
[**pagesJsonPost**](PagesApi.md#pagesJsonPost) | **POST** /pages.json | Create a new Page.



## pagesCountJsonGet

> Count pagesCountJsonGet(login, authtoken)

Count all Pages.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.pagesCountJsonGet(login, authtoken, (error, data, response) => {
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


## pagesIdJsonDelete

> String pagesIdJsonDelete(login, authtoken, id)

Delete an existing Page.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Page
apiInstance.pagesIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Page | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pagesIdJsonGet

> Page pagesIdJsonGet(login, authtoken, id)

Retrieve a single Page by id.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Page
apiInstance.pagesIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Page | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pagesIdJsonPut

> Page pagesIdJsonPut(login, authtoken, id, pageModify)

Update a Page.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Page
let pageModify = new JumpsellerApi.PageModify(); // PageModify | Page parameters.
apiInstance.pagesIdJsonPut(login, authtoken, id, pageModify, (error, data, response) => {
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
 **id** | **Number**| Id of the Page | 
 **pageModify** | [**PageModify**](PageModify.md)| Page parameters. | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pagesJsonGet

> [Page] pagesJsonGet(login, authtoken, opts)

Retrieve all Pages.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.pagesJsonGet(login, authtoken, opts, (error, data, response) => {
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

[**[Page]**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pagesJsonPost

> Page pagesJsonPost(login, authtoken, pageModify)

Create a new Page.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let pageModify = new JumpsellerApi.PageModify(); // PageModify | Page parameters.
apiInstance.pagesJsonPost(login, authtoken, pageModify, (error, data, response) => {
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
 **pageModify** | [**PageModify**](PageModify.md)| Page parameters. | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

