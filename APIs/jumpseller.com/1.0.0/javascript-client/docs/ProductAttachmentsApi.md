# JumpsellerApi.ProductAttachmentsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdAttachmentsAttachmentIdJsonDelete**](ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonDelete) | **DELETE** /products/{id}/attachments/{attachment_id}.json | Delete a Product Attachment.
[**productsIdAttachmentsAttachmentIdJsonGet**](ProductAttachmentsApi.md#productsIdAttachmentsAttachmentIdJsonGet) | **GET** /products/{id}/attachments/{attachment_id}.json | Retrieve a single Product Attachment.
[**productsIdAttachmentsCountJsonGet**](ProductAttachmentsApi.md#productsIdAttachmentsCountJsonGet) | **GET** /products/{id}/attachments/count.json | Count all Product Attachments.
[**productsIdAttachmentsJsonGet**](ProductAttachmentsApi.md#productsIdAttachmentsJsonGet) | **GET** /products/{id}/attachments.json | Retrieve all Product Attachments.
[**productsIdAttachmentsJsonPost**](ProductAttachmentsApi.md#productsIdAttachmentsJsonPost) | **POST** /products/{id}/attachments.json | Create a new Product Attachment.



## productsIdAttachmentsAttachmentIdJsonDelete

> String productsIdAttachmentsAttachmentIdJsonDelete(login, authtoken, id, attachmentId)

Delete a Product Attachment.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductAttachmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let attachmentId = 56; // Number | Id of the Product Attachment
apiInstance.productsIdAttachmentsAttachmentIdJsonDelete(login, authtoken, id, attachmentId, (error, data, response) => {
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
 **attachmentId** | **Number**| Id of the Product Attachment | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdAttachmentsAttachmentIdJsonGet

> Attachment productsIdAttachmentsAttachmentIdJsonGet(login, authtoken, id, attachmentId)

Retrieve a single Product Attachment.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductAttachmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let attachmentId = 56; // Number | Id of the Product Attachment
apiInstance.productsIdAttachmentsAttachmentIdJsonGet(login, authtoken, id, attachmentId, (error, data, response) => {
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
 **attachmentId** | **Number**| Id of the Product Attachment | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdAttachmentsCountJsonGet

> Count productsIdAttachmentsCountJsonGet(login, authtoken, id)

Count all Product Attachments.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductAttachmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdAttachmentsCountJsonGet(login, authtoken, id, (error, data, response) => {
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


## productsIdAttachmentsJsonGet

> [Attachment] productsIdAttachmentsJsonGet(login, authtoken, id)

Retrieve all Product Attachments.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductAttachmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdAttachmentsJsonGet(login, authtoken, id, (error, data, response) => {
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

[**[Attachment]**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdAttachmentsJsonPost

> Attachment productsIdAttachmentsJsonPost(login, authtoken, id, attachmentEdit)

Create a new Product Attachment.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductAttachmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let attachmentEdit = new JumpsellerApi.AttachmentEdit(); // AttachmentEdit | Product Attachment parameters.
apiInstance.productsIdAttachmentsJsonPost(login, authtoken, id, attachmentEdit, (error, data, response) => {
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
 **attachmentEdit** | [**AttachmentEdit**](AttachmentEdit.md)| Product Attachment parameters. | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

