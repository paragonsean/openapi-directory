# EanSearchOrgApi.DefaultApi

All URIs are relative to *https://api.ean-search.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcodeImage**](DefaultApi.md#barcodeImage) | **GET** /barcode-image | Generate a PNG barcode image
[**barcodeLookup**](DefaultApi.md#barcodeLookup) | **GET** /barcode-lookup | Look up an EAN
[**barcodePrefixSearch**](DefaultApi.md#barcodePrefixSearch) | **GET** /barcode-prefix-search | Query the database for all barcodes with the same beginning
[**categorySearch**](DefaultApi.md#categorySearch) | **GET** /category-search | Search for products form a certain category
[**issuingCountry**](DefaultApi.md#issuingCountry) | **GET** /issuing-country | Search for a issuing country of a barcode
[**productSearch**](DefaultApi.md#productSearch) | **GET** /product-search | Search by product name
[**verifyChecksum**](DefaultApi.md#verifyChecksum) | **GET** /verify-checksum | Verify the checksum of an EAN code



## barcodeImage

> [Barcode] barcodeImage(op, ean, opts)

Generate a PNG barcode image

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let ean = 56; // Number | EAN code to search for
let opts = {
  'width': 102, // Number | 
  'height': 50, // Number | 
  'format': "format_example" // String | output format
};
apiInstance.barcodeImage(op, ean, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **ean** | **Number**| EAN code to search for | 
 **width** | **Number**|  | [optional] [default to 102]
 **height** | **Number**|  | [optional] [default to 50]
 **format** | **String**| output format | [optional] 

### Return type

[**[Barcode]**](Barcode.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## barcodeLookup

> [Product] barcodeLookup(op, ean, opts)

Look up an EAN

Search by EAN code

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let ean = 56; // Number | EAN code to search for
let opts = {
  'language': 1, // Number | preferred language for the product name
  'format': "format_example" // String | output format
};
apiInstance.barcodeLookup(op, ean, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **ean** | **Number**| EAN code to search for | 
 **language** | **Number**| preferred language for the product name | [optional] [default to 1]
 **format** | **String**| output format | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## barcodePrefixSearch

> [Product] barcodePrefixSearch(op, prefix, opts)

Query the database for all barcodes with the same beginning

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let prefix = "prefix_example"; // String | barcode prefix to search for, at least 4 digits
let opts = {
  'language': 1, // Number | preferred language for the product name
  'page': 0, // Number | result page
  'format': "format_example" // String | output format
};
apiInstance.barcodePrefixSearch(op, prefix, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **prefix** | **String**| barcode prefix to search for, at least 4 digits | 
 **language** | **Number**| preferred language for the product name | [optional] [default to 1]
 **page** | **Number**| result page | [optional] [default to 0]
 **format** | **String**| output format | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## categorySearch

> [Product] categorySearch(op, category, opts)

Search for products form a certain category

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let category = 56; // Number | category number
let opts = {
  'name': "name_example", // String | name or keyords to search for
  'language': 99, // Number | preferred language for the product name (default any language)
  'page': 0, // Number | result page
  'format': "format_example" // String | output format
};
apiInstance.categorySearch(op, category, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **category** | **Number**| category number | 
 **name** | **String**| name or keyords to search for | [optional] 
 **language** | **Number**| preferred language for the product name (default any language) | [optional] [default to 99]
 **page** | **Number**| result page | [optional] [default to 0]
 **format** | **String**| output format | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## issuingCountry

> [IssuingCountry] issuingCountry(op, ean, opts)

Search for a issuing country of a barcode

Search for a issuing country of a barcode. In contrast to barcode-lookup, this will always give a result, even if we don&#39;t know the product name.

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let ean = 56; // Number | EAN code to search for
let opts = {
  'format': "format_example" // String | output format
};
apiInstance.issuingCountry(op, ean, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **ean** | **Number**| EAN code to search for | 
 **format** | **String**| output format | [optional] 

### Return type

[**[IssuingCountry]**](IssuingCountry.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## productSearch

> [Product] productSearch(op, name, opts)

Search by product name

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let name = "name_example"; // String | name or keyords to search for
let opts = {
  'language': 99, // Number | preferred language for the product name (default any language)
  'page': 0, // Number | result page
  'format': "format_example" // String | output format
};
apiInstance.productSearch(op, name, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **name** | **String**| name or keyords to search for | 
 **language** | **Number**| preferred language for the product name (default any language) | [optional] [default to 99]
 **page** | **Number**| result page | [optional] [default to 0]
 **format** | **String**| output format | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## verifyChecksum

> [VerifyChecksum] verifyChecksum(op, ean, opts)

Verify the checksum of an EAN code

### Example

```javascript
import EanSearchOrgApi from 'ean_search_org_api';
let defaultClient = EanSearchOrgApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new EanSearchOrgApi.DefaultApi();
let op = "op_example"; // String | API operation
let ean = 56; // Number | EAN code to search for
let opts = {
  'format': "format_example" // String | output format
};
apiInstance.verifyChecksum(op, ean, opts, (error, data, response) => {
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
 **op** | **String**| API operation | 
 **ean** | **Number**| EAN code to search for | 
 **format** | **String**| output format | [optional] 

### Return type

[**[VerifyChecksum]**](VerifyChecksum.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

