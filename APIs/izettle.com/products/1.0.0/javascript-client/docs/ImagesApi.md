# ProductLibraryApi.ImagesApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllImageUrls**](ImagesApi.md#getAllImageUrls) | **GET** /organizations/{organizationUuid}/images | Retrieve all library item images



## getAllImageUrls

> LibraryImagesResponse getAllImageUrls(organizationUuid)

Retrieve all library item images

Retrieves all library items images used by the organization, sorted by updated date

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ImagesApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.getAllImageUrls(organizationUuid, (error, data, response) => {
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

### Return type

[**LibraryImagesResponse**](LibraryImagesResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

