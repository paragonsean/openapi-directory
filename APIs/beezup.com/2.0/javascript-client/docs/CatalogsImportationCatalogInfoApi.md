# BeezUpMerchantApi.CatalogsImportationCatalogInfoApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**importationConfigureCatalogColumn**](CatalogsImportationCatalogInfoApi.md#importationConfigureCatalogColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId} | Configure catalog column
[**importationDeleteCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationDeleteCustomColumn) | **DELETE** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId} | Delete Custom Column
[**importationGetCustomColumnExpression**](CatalogsImportationCatalogInfoApi.md#importationGetCustomColumnExpression) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId}/expression | Get the encrypted custom column expression in this importation
[**importationGetCustomColumns**](CatalogsImportationCatalogInfoApi.md#importationGetCustomColumns) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns | Get custom columns currently place in this importation
[**importationGetDetectedCatalogColumns**](CatalogsImportationCatalogInfoApi.md#importationGetDetectedCatalogColumns) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns | Get detected catalog columns during this importation.
[**importationGetProductSample**](CatalogsImportationCatalogInfoApi.md#importationGetProductSample) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/productSamples/{productSampleIndex} | Get the product sample related to this importation with all columns (catalog and custom)
[**importationGetProductSampleCustomColumnValue**](CatalogsImportationCatalogInfoApi.md#importationGetProductSampleCustomColumnValue) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/productSamples/{productSampleIndex}/customColumns/{columnId} | Get product sample custom column value related to this importation.
[**importationIgnoreColumn**](CatalogsImportationCatalogInfoApi.md#importationIgnoreColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/ignore | Ignore Column
[**importationMapCatalogColumn**](CatalogsImportationCatalogInfoApi.md#importationMapCatalogColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/map | Map catalog column to a BeezUP column
[**importationMapCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationMapCustomColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId}/map | Map custom column to a BeezUP column
[**importationReattendColumn**](CatalogsImportationCatalogInfoApi.md#importationReattendColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/reattend | Reattend Column
[**importationSaveCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationSaveCustomColumn) | **PUT** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId} | Create or replace a custom column
[**importationUnmapCatalogColumn**](CatalogsImportationCatalogInfoApi.md#importationUnmapCatalogColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/catalogColumns/{columnId}/unmap | Unmap catalog column
[**importationUnmapCustomColumn**](CatalogsImportationCatalogInfoApi.md#importationUnmapCustomColumn) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/customColumns/{columnId}/unmap | Unmap custom column



## importationConfigureCatalogColumn

> importationConfigureCatalogColumn(storeId, executionId, columnId, configureCatalogColumnCatalogRequest)

Configure catalog column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
let configureCatalogColumnCatalogRequest = new BeezUpMerchantApi.ConfigureCatalogColumnCatalogRequest(); // ConfigureCatalogColumnCatalogRequest | 
apiInstance.importationConfigureCatalogColumn(storeId, executionId, columnId, configureCatalogColumnCatalogRequest, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 
 **configureCatalogColumnCatalogRequest** | [**ConfigureCatalogColumnCatalogRequest**](ConfigureCatalogColumnCatalogRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importationDeleteCustomColumn

> importationDeleteCustomColumn(storeId, executionId, columnId)

Delete Custom Column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.importationDeleteCustomColumn(storeId, executionId, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetCustomColumnExpression

> String importationGetCustomColumnExpression(storeId, executionId, columnId)

Get the encrypted custom column expression in this importation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.importationGetCustomColumnExpression(storeId, executionId, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetCustomColumns

> ImportationCustomColumnList importationGetCustomColumns(storeId, executionId)

Get custom columns currently place in this importation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationGetCustomColumns(storeId, executionId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 

### Return type

[**ImportationCustomColumnList**](ImportationCustomColumnList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetDetectedCatalogColumns

> DetectedCatalogColumnList importationGetDetectedCatalogColumns(storeId, executionId)

Get detected catalog columns during this importation.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationGetDetectedCatalogColumns(storeId, executionId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 

### Return type

[**DetectedCatalogColumnList**](DetectedCatalogColumnList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetProductSample

> ProductSample importationGetProductSample(storeId, executionId, productSampleIndex)

Get the product sample related to this importation with all columns (catalog and custom)

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let productSampleIndex = 56; // Number | Index of the product sample. Starting from 0 to 99.
apiInstance.importationGetProductSample(storeId, executionId, productSampleIndex, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **productSampleIndex** | **Number**| Index of the product sample. Starting from 0 to 99. | 

### Return type

[**ProductSample**](ProductSample.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetProductSampleCustomColumnValue

> String importationGetProductSampleCustomColumnValue(storeId, executionId, productSampleIndex, columnId)

Get product sample custom column value related to this importation.

/!\\ Use this operation only when you just changed the custom column expression and you want to get a precise the property value. Otherwise use the operation Importation_GetProductSample which will give you all property values

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let productSampleIndex = 56; // Number | Index of the product sample. Starting from 0 to 99.
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.importationGetProductSampleCustomColumnValue(storeId, executionId, productSampleIndex, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **productSampleIndex** | **Number**| Index of the product sample. Starting from 0 to 99. | 
 **columnId** | **String**| The custom column identifier | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationIgnoreColumn

> importationIgnoreColumn(storeId, executionId, columnId)

Ignore Column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.importationIgnoreColumn(storeId, executionId, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationMapCatalogColumn

> importationMapCatalogColumn(storeId, executionId, columnId, mapBeezUPColumnRequest)

Map catalog column to a BeezUP column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The catalog column identifier
let mapBeezUPColumnRequest = new BeezUpMerchantApi.MapBeezUPColumnRequest(); // MapBeezUPColumnRequest | 
apiInstance.importationMapCatalogColumn(storeId, executionId, columnId, mapBeezUPColumnRequest, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The catalog column identifier | 
 **mapBeezUPColumnRequest** | [**MapBeezUPColumnRequest**](MapBeezUPColumnRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importationMapCustomColumn

> importationMapCustomColumn(storeId, executionId, columnId, mapBeezUPColumnRequest)

Map custom column to a BeezUP column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
let mapBeezUPColumnRequest = new BeezUpMerchantApi.MapBeezUPColumnRequest(); // MapBeezUPColumnRequest | 
apiInstance.importationMapCustomColumn(storeId, executionId, columnId, mapBeezUPColumnRequest, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 
 **mapBeezUPColumnRequest** | [**MapBeezUPColumnRequest**](MapBeezUPColumnRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importationReattendColumn

> importationReattendColumn(storeId, executionId, columnId)

Reattend Column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.importationReattendColumn(storeId, executionId, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationSaveCustomColumn

> importationSaveCustomColumn(storeId, executionId, columnId, changeCustomColumnRequest)

Create or replace a custom column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
let changeCustomColumnRequest = new BeezUpMerchantApi.ChangeCustomColumnRequest(); // ChangeCustomColumnRequest | 
apiInstance.importationSaveCustomColumn(storeId, executionId, columnId, changeCustomColumnRequest, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 
 **changeCustomColumnRequest** | [**ChangeCustomColumnRequest**](ChangeCustomColumnRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importationUnmapCatalogColumn

> importationUnmapCatalogColumn(storeId, executionId, columnId)

Unmap catalog column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The catalog column identifier
apiInstance.importationUnmapCatalogColumn(storeId, executionId, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The catalog column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationUnmapCustomColumn

> importationUnmapCustomColumn(storeId, executionId, columnId)

Unmap custom column

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationCatalogInfoApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let columnId = "columnId_example"; // String | The custom column identifier
apiInstance.importationUnmapCustomColumn(storeId, executionId, columnId, (error, data, response) => {
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
 **executionId** | **String**| The execution identifier of you catalog importation | 
 **columnId** | **String**| The custom column identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

