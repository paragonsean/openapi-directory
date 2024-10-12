# BeezUpMerchantApi.CatalogsCatalogApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogChangeCatalogColumnUserName**](CatalogsCatalogApi.md#catalogChangeCatalogColumnUserName) | **POST** /v2/user/catalogs/{storeId}/catalogColumns/{columnId}/rename | Change Catalog Column User Name
[**catalogChangeCustomColumnExpression**](CatalogsCatalogApi.md#catalogChangeCustomColumnExpression) | **PUT** /v2/user/catalogs/{storeId}/customColumns/{columnId}/expression | Change custom column expression
[**catalogChangeCustomColumnUserName**](CatalogsCatalogApi.md#catalogChangeCustomColumnUserName) | **POST** /v2/user/catalogs/{storeId}/customColumns/{columnId}/rename | Change Custom Column User Name
[**catalogComputeExpression**](CatalogsCatalogApi.md#catalogComputeExpression) | **POST** /v2/user/catalogs/{storeId}/customColumns/computeExpression | Compute the expression for this catalog.
[**catalogDeleteCustomColumn**](CatalogsCatalogApi.md#catalogDeleteCustomColumn) | **DELETE** /v2/user/catalogs/{storeId}/customColumns/{columnId} | Delete custom column
[**catalogGetCatalogColumns**](CatalogsCatalogApi.md#catalogGetCatalogColumns) | **GET** /v2/user/catalogs/{storeId}/catalogColumns | Get catalog column list
[**catalogGetCategories**](CatalogsCatalogApi.md#catalogGetCategories) | **GET** /v2/user/catalogs/{storeId}/categories | Get category list
[**catalogGetCustomColumnExpression**](CatalogsCatalogApi.md#catalogGetCustomColumnExpression) | **GET** /v2/user/catalogs/{storeId}/customColumns/{columnId}/expression | Get the encrypted custom column expression
[**catalogGetCustomColumns**](CatalogsCatalogApi.md#catalogGetCustomColumns) | **GET** /v2/user/catalogs/{storeId}/customColumns | Get custom column list
[**catalogGetProductByProductId**](CatalogsCatalogApi.md#catalogGetProductByProductId) | **GET** /v2/user/catalogs/{storeId}/products/{productId} | Get product by ProductId
[**catalogGetProductBySku**](CatalogsCatalogApi.md#catalogGetProductBySku) | **GET** /v2/user/catalogs/{storeId}/products | Get product by Sku
[**catalogGetProducts**](CatalogsCatalogApi.md#catalogGetProducts) | **POST** /v2/user/catalogs/{storeId}/products/list | Get product list
[**catalogGetRandomProducts**](CatalogsCatalogApi.md#catalogGetRandomProducts) | **GET** /v2/user/catalogs/{storeId}/products/random | Get random product list
[**catalogSaveCustomColumn**](CatalogsCatalogApi.md#catalogSaveCustomColumn) | **PUT** /v2/user/catalogs/{storeId}/customColumns/{columnId} | Create or replace a custom column
[**catalogStoreIndex**](CatalogsCatalogApi.md#catalogStoreIndex) | **GET** /v2/user/catalogs/{storeId} | Get the index of the catalog API for this store
[**importationGetManualUpdateLastInputConfig**](CatalogsCatalogApi.md#importationGetManualUpdateLastInputConfig) | **GET** /v2/user/catalogs/{storeId}/inputConfiguration | Get the last input configuration



## catalogChangeCatalogColumnUserName

> catalogChangeCatalogColumnUserName(storeId, columnId, changeUserColumnNameRequest)

Change Catalog Column User Name

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let columnId = "columnId_example"; // String | The catalog column identifier
let changeUserColumnNameRequest = new BeezUpMerchantApi.ChangeUserColumnNameRequest(); // ChangeUserColumnNameRequest | 
apiInstance.catalogChangeCatalogColumnUserName(storeId, columnId, changeUserColumnNameRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeId** | **String**| Your store identifier | 
 **columnId** | **String**| The catalog column identifier | 
 **changeUserColumnNameRequest** | [**ChangeUserColumnNameRequest**](ChangeUserColumnNameRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogChangeCustomColumnExpression

> catalogChangeCustomColumnExpression(storeId, columnId, changeCustomColumnExpressionRequest)

Change custom column expression

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let columnId = "columnId_example"; // String | The custom column identifier
let changeCustomColumnExpressionRequest = new BeezUpMerchantApi.ChangeCustomColumnExpressionRequest(); // ChangeCustomColumnExpressionRequest | 
apiInstance.catalogChangeCustomColumnExpression(storeId, columnId, changeCustomColumnExpressionRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeId** | **String**| Your store identifier | 
 **columnId** | **String**| The custom column identifier | 
 **changeCustomColumnExpressionRequest** | [**ChangeCustomColumnExpressionRequest**](ChangeCustomColumnExpressionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogChangeCustomColumnUserName

> catalogChangeCustomColumnUserName(storeId, columnId, changeUserColumnNameRequest)

Change Custom Column User Name

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let columnId = "columnId_example"; // String | The custom column identifier
let changeUserColumnNameRequest = new BeezUpMerchantApi.ChangeUserColumnNameRequest(); // ChangeUserColumnNameRequest | 
apiInstance.catalogChangeCustomColumnUserName(storeId, columnId, changeUserColumnNameRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeId** | **String**| Your store identifier | 
 **columnId** | **String**| The custom column identifier | 
 **changeUserColumnNameRequest** | [**ChangeUserColumnNameRequest**](ChangeUserColumnNameRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogComputeExpression

> String catalogComputeExpression(storeId, computeExpressionRequest)

Compute the expression for this catalog.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let computeExpressionRequest = new BeezUpMerchantApi.ComputeExpressionRequest(); // ComputeExpressionRequest | 
apiInstance.catalogComputeExpression(storeId, computeExpressionRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **computeExpressionRequest** | [**ComputeExpressionRequest**](ComputeExpressionRequest.md)|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogDeleteCustomColumn

> catalogDeleteCustomColumn(storeId, columnId)

Delete custom column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.catalogDeleteCustomColumn(storeId, columnId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeId** | **String**| Your store identifier | 
 **columnId** | **String**| The custom column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetCatalogColumns

> CatalogColumnList catalogGetCatalogColumns(storeId)

Get catalog column list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.catalogGetCatalogColumns(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**CatalogColumnList**](CatalogColumnList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetCategories

> CategoryList catalogGetCategories(storeId, acceptEncoding)

Get category list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let acceptEncoding = ["null"]; // [String] | Indicates that the client accepts that the response will be compressed to reduce traffic size.
apiInstance.catalogGetCategories(storeId, acceptEncoding, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **acceptEncoding** | [**[String]**](String.md)| Indicates that the client accepts that the response will be compressed to reduce traffic size. | 

### Return type

[**CategoryList**](CategoryList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetCustomColumnExpression

> String catalogGetCustomColumnExpression(storeId, columnId)

Get the encrypted custom column expression

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.catalogGetCustomColumnExpression(storeId, columnId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **columnId** | **String**| The custom column identifier | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetCustomColumns

> CustomColumnList catalogGetCustomColumns(storeId)

Get custom column list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.catalogGetCustomColumns(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**CustomColumnList**](CustomColumnList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetProductByProductId

> Product catalogGetProductByProductId(storeId, productId)

Get product by ProductId

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let productId = "productId_example"; // String | The product identifier you want to get
apiInstance.catalogGetProductByProductId(storeId, productId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **productId** | **String**| The product identifier you want to get | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetProductBySku

> Product catalogGetProductBySku(storeId, sku)

Get product by Sku

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let sku = "sku_example"; // String | The product sku you want to get
apiInstance.catalogGetProductBySku(storeId, sku, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **sku** | **String**| The product sku you want to get | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogGetProducts

> ProductList catalogGetProducts(storeId, getProductsRequest)

Get product list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let getProductsRequest = new BeezUpMerchantApi.GetProductsRequest(); // GetProductsRequest | 
apiInstance.catalogGetProducts(storeId, getProductsRequest, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 
 **getProductsRequest** | [**GetProductsRequest**](GetProductsRequest.md)|  | 

### Return type

[**ProductList**](ProductList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogGetRandomProducts

> RandomProductList catalogGetRandomProducts(storeId)

Get random product list

We will return 10 products randomly selected with all product values

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.catalogGetRandomProducts(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**RandomProductList**](RandomProductList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogSaveCustomColumn

> catalogSaveCustomColumn(storeId, columnId, createCustomColumnRequest)

Create or replace a custom column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
let columnId = "columnId_example"; // String | The custom column identifier
let createCustomColumnRequest = new BeezUpMerchantApi.CreateCustomColumnRequest(); // CreateCustomColumnRequest | 
apiInstance.catalogSaveCustomColumn(storeId, columnId, createCustomColumnRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeId** | **String**| Your store identifier | 
 **columnId** | **String**| The custom column identifier | 
 **createCustomColumnRequest** | [**CreateCustomColumnRequest**](CreateCustomColumnRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogStoreIndex

> CatalogStoreIndex catalogStoreIndex(storeId)

Get the index of the catalog API for this store

The operation will give you all the operations you will be able to do on this store for this API.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.catalogStoreIndex(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**CatalogStoreIndex**](CatalogStoreIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetManualUpdateLastInputConfig

> LastManualImportInputConfiguration importationGetManualUpdateLastInputConfig(storeId)

Get the last input configuration

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsCatalogApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.importationGetManualUpdateLastInputConfig(storeId, (error, data, response) => {
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
 **storeId** | **String**| Your store identifier | 

### Return type

[**LastManualImportInputConfiguration**](LastManualImportInputConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

