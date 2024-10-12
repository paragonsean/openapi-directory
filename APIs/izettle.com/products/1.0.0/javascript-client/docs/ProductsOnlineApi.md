# ProductLibraryApi.ProductsOnlineApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProductSlug**](ProductsOnlineApi.md#createProductSlug) | **POST** /organizations/{organizationUuid}/products/online/slug | Create a product identifier



## createProductSlug

> SlugResponse createProductSlug(organizationUuid, createSlugRequest)

Create a product identifier

Creates a unique slug (identifier) for a product. The slug is used to create a product URL

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsOnlineApi();
let organizationUuid = "organizationUuid_example"; // String | 
let createSlugRequest = new ProductLibraryApi.CreateSlugRequest(); // CreateSlugRequest | 
apiInstance.createProductSlug(organizationUuid, createSlugRequest, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **createSlugRequest** | [**CreateSlugRequest**](CreateSlugRequest.md)|  | 

### Return type

[**SlugResponse**](SlugResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

