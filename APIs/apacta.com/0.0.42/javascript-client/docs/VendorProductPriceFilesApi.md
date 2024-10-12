# Apacta.VendorProductPriceFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendorProductPriceFilesGet**](VendorProductPriceFilesApi.md#vendorProductPriceFilesGet) | **GET** /vendor_product_price_files | Get a list of price files
[**vendorProductPriceFilesPost**](VendorProductPriceFilesApi.md#vendorProductPriceFilesPost) | **POST** /vendor_product_price_files | Upload a vendor price file
[**vendorProductPriceFilesVendorProductPriceFileIdGet**](VendorProductPriceFilesApi.md#vendorProductPriceFilesVendorProductPriceFileIdGet) | **GET** /vendor_product_price_files/{vendor_product_price_file_id} | Get a single price file



## vendorProductPriceFilesGet

> VendorProductPriceFilesGet200Response vendorProductPriceFilesGet(opts)

Get a list of price files

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.VendorProductPriceFilesApi();
let opts = {
  'fileName': "fileName_example", // String | 
  'vendorName': "vendorName_example", // String | 
  'vendorIds': ["null"], // [String] | 
  'status': "status_example" // String | 
};
apiInstance.vendorProductPriceFilesGet(opts, (error, data, response) => {
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
 **fileName** | **String**|  | [optional] 
 **vendorName** | **String**|  | [optional] 
 **vendorIds** | [**[String]**](String.md)|  | [optional] 
 **status** | **String**|  | [optional] 

### Return type

[**VendorProductPriceFilesGet200Response**](VendorProductPriceFilesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vendorProductPriceFilesPost

> CreateSuccessResponse vendorProductPriceFilesPost(companiesVendorId, file)

Upload a vendor price file

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.VendorProductPriceFilesApi();
let companiesVendorId = "companiesVendorId_example"; // String | 
let file = "/path/to/file"; // File | 
apiInstance.vendorProductPriceFilesPost(companiesVendorId, file, (error, data, response) => {
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
 **companiesVendorId** | **String**|  | 
 **file** | **File**|  | 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## vendorProductPriceFilesVendorProductPriceFileIdGet

> VendorProductPriceFilesVendorProductPriceFileIdGet200Response vendorProductPriceFilesVendorProductPriceFileIdGet(vendorProductPriceFileId)

Get a single price file

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.VendorProductPriceFilesApi();
let vendorProductPriceFileId = "vendorProductPriceFileId_example"; // String | Automatically added
apiInstance.vendorProductPriceFilesVendorProductPriceFileIdGet(vendorProductPriceFileId, (error, data, response) => {
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
 **vendorProductPriceFileId** | **String**| Automatically added | 

### Return type

[**VendorProductPriceFilesVendorProductPriceFileIdGet200Response**](VendorProductPriceFilesVendorProductPriceFileIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

