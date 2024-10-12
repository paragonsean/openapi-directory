# ProductLibraryApi.ImportApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLatestImportStatus**](ImportApi.md#getLatestImportStatus) | **GET** /organizations/{organizationUuid}/import/status | Get status for latest import
[**getStatusByUuid**](ImportApi.md#getStatusByUuid) | **GET** /organizations/{organizationUuid}/import/status/{importUuid} | Get status for an import
[**importLibraryV2**](ImportApi.md#importLibraryV2) | **POST** /organizations/{organizationUuid}/import/v2 | Import library items



## getLatestImportStatus

> ImportResponse getLatestImportStatus(organizationUuid)

Get status for latest import

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ImportApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.getLatestImportStatus(organizationUuid, (error, data, response) => {
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

[**ImportResponse**](ImportResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatusByUuid

> ImportResponse getStatusByUuid(organizationUuid, importUuid)

Get status for an import

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ImportApi();
let organizationUuid = "organizationUuid_example"; // String | 
let importUuid = "importUuid_example"; // String | 
apiInstance.getStatusByUuid(organizationUuid, importUuid, (error, data, response) => {
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
 **importUuid** | **String**|  | 

### Return type

[**ImportResponse**](ImportResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importLibraryV2

> ImportResponse importLibraryV2(organizationUuid, bulkImportRequest)

Import library items

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ImportApi();
let organizationUuid = "organizationUuid_example"; // String | 
let bulkImportRequest = new ProductLibraryApi.BulkImportRequest(); // BulkImportRequest | 
apiInstance.importLibraryV2(organizationUuid, bulkImportRequest, (error, data, response) => {
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
 **bulkImportRequest** | [**BulkImportRequest**](BulkImportRequest.md)|  | 

### Return type

[**ImportResponse**](ImportResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

