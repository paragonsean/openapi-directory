# JumpsellerApi.ProductImagesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdImagesCountJsonGet**](ProductImagesApi.md#productsIdImagesCountJsonGet) | **GET** /products/{id}/images/count.json | Count all Product Images.
[**productsIdImagesImageIdJsonDelete**](ProductImagesApi.md#productsIdImagesImageIdJsonDelete) | **DELETE** /products/{id}/images/{image_id}.json | Delete a Product Image.
[**productsIdImagesImageIdJsonGet**](ProductImagesApi.md#productsIdImagesImageIdJsonGet) | **GET** /products/{id}/images/{image_id}.json | Retrieve a single Product Image.
[**productsIdImagesJsonGet**](ProductImagesApi.md#productsIdImagesJsonGet) | **GET** /products/{id}/images.json | Retrieve all Product Images.
[**productsIdImagesJsonPost**](ProductImagesApi.md#productsIdImagesJsonPost) | **POST** /products/{id}/images.json | Create a new Product Image.



## productsIdImagesCountJsonGet

> Count productsIdImagesCountJsonGet(login, authtoken, id)

Count all Product Images.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductImagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdImagesCountJsonGet(login, authtoken, id, (error, data, response) => {
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

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdImagesImageIdJsonDelete

> String productsIdImagesImageIdJsonDelete(login, authtoken, id, imageId)

Delete a Product Image.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductImagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let imageId = 56; // Number | Id of the Product Image
apiInstance.productsIdImagesImageIdJsonDelete(login, authtoken, id, imageId, (error, data, response) => {
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
 **imageId** | **Number**| Id of the Product Image | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdImagesImageIdJsonGet

> Image productsIdImagesImageIdJsonGet(login, authtoken, id, imageId)

Retrieve a single Product Image.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductImagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let imageId = 56; // Number | Id of the Product Image
apiInstance.productsIdImagesImageIdJsonGet(login, authtoken, id, imageId, (error, data, response) => {
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
 **imageId** | **Number**| Id of the Product Image | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdImagesJsonGet

> [Image] productsIdImagesJsonGet(login, authtoken, id)

Retrieve all Product Images.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductImagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdImagesJsonGet(login, authtoken, id, (error, data, response) => {
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

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdImagesJsonPost

> Image productsIdImagesJsonPost(login, authtoken, id, imageEdit)

Create a new Product Image.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductImagesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let imageEdit = new JumpsellerApi.ImageEdit(); // ImageEdit | Product Image parameters.
apiInstance.productsIdImagesJsonPost(login, authtoken, id, imageEdit, (error, data, response) => {
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
 **imageEdit** | [**ImageEdit**](ImageEdit.md)| Product Image parameters. | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

