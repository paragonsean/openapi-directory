# BeezUpMerchantApi.CatalogsImportationProcessApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**importationCancel**](CatalogsImportationProcessApi.md#importationCancel) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/cancel | Cancel importation
[**importationCommit**](CatalogsImportationProcessApi.md#importationCommit) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/commit | Commit Importation
[**importationCommitColumns**](CatalogsImportationProcessApi.md#importationCommitColumns) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/commitColumns | Commit columns
[**importationConfigureRemainingCatalogColumns**](CatalogsImportationProcessApi.md#importationConfigureRemainingCatalogColumns) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/configureRemainingCatalogColumns | Configure remaining catalog columns
[**importationGetImportationMonitoring**](CatalogsImportationProcessApi.md#importationGetImportationMonitoring) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId} | Get the importation status
[**importationGetProductsReport**](CatalogsImportationProcessApi.md#importationGetProductsReport) | **POST** /v2/user/catalogs/{storeId}/importations/{executionId}/products/list | Importation Get Products Report
[**importationGetReport**](CatalogsImportationProcessApi.md#importationGetReport) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/report | Importation Get Report
[**importationGetReportings**](CatalogsImportationProcessApi.md#importationGetReportings) | **GET** /v2/user/catalogs/{storeId}/importations | Get the latest catalog importation reporting
[**importationGetReportingsAllStores**](CatalogsImportationProcessApi.md#importationGetReportingsAllStores) | **GET** /v2/user/catalogs/importations | Get the latest catalog importation reporting for all your stores
[**importationStartManualUpdate**](CatalogsImportationProcessApi.md#importationStartManualUpdate) | **POST** /v2/user/catalogs/{storeId}/importations/start | Start Manual Import
[**importationTechnicalProgression**](CatalogsImportationProcessApi.md#importationTechnicalProgression) | **GET** /v2/user/catalogs/{storeId}/importations/{executionId}/technicalProgression | Get technical progression



## importationCancel

> importationCancel(storeId, executionId)

Cancel importation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationCancel(storeId, executionId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationCommit

> importationCommit(storeId, executionId)

Commit Importation

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationCommit(storeId, executionId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationCommitColumns

> importationCommitColumns(storeId, executionId)

Commit columns

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationCommitColumns(storeId, executionId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationConfigureRemainingCatalogColumns

> importationConfigureRemainingCatalogColumns(storeId, executionId)

Configure remaining catalog columns

This operation should be used after you have mapped the required BeezUP Columns

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationConfigureRemainingCatalogColumns(storeId, executionId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetImportationMonitoring

> ImportationMonitoring importationGetImportationMonitoring(storeId, executionId)

Get the importation status

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationGetImportationMonitoring(storeId, executionId, (error, data, response) => {
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

[**ImportationMonitoring**](ImportationMonitoring.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetProductsReport

> GetImportationProductsReportResponse importationGetProductsReport(storeId, executionId, getImportationProductsReportRequest)

Importation Get Products Report

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
let getImportationProductsReportRequest = new BeezUpMerchantApi.GetImportationProductsReportRequest(); // GetImportationProductsReportRequest | 
apiInstance.importationGetProductsReport(storeId, executionId, getImportationProductsReportRequest, (error, data, response) => {
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
 **getImportationProductsReportRequest** | [**GetImportationProductsReportRequest**](GetImportationProductsReportRequest.md)|  | 

### Return type

[**GetImportationProductsReportResponse**](GetImportationProductsReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importationGetReport

> GetImportationReportResponse importationGetReport(storeId, executionId)

Importation Get Report

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationGetReport(storeId, executionId, (error, data, response) => {
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

[**GetImportationReportResponse**](GetImportationReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetReportings

> ImportationsResponse importationGetReportings(storeId)

Get the latest catalog importation reporting

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
apiInstance.importationGetReportings(storeId, (error, data, response) => {
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

[**ImportationsResponse**](ImportationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationGetReportingsAllStores

> {String: ImportationsResponse} importationGetReportingsAllStores()

Get the latest catalog importation reporting for all your stores

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
apiInstance.importationGetReportingsAllStores((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**{String: ImportationsResponse}**](ImportationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importationStartManualUpdate

> LinksImportationGetImportationMonitoringLink importationStartManualUpdate(storeId, startManualImportRequest)

Start Manual Import

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let startManualImportRequest = new BeezUpMerchantApi.StartManualImportRequest(); // StartManualImportRequest | 
apiInstance.importationStartManualUpdate(storeId, startManualImportRequest, (error, data, response) => {
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
 **startManualImportRequest** | [**StartManualImportRequest**](StartManualImportRequest.md)|  | 

### Return type

[**LinksImportationGetImportationMonitoringLink**](LinksImportationGetImportationMonitoringLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importationTechnicalProgression

> ImportationTechnicalProgression importationTechnicalProgression(storeId, executionId)

Get technical progression

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsImportationProcessApi();
let storeId = "storeId_example"; // String | Your store identifier
let executionId = "executionId_example"; // String | The execution identifier of you catalog importation
apiInstance.importationTechnicalProgression(storeId, executionId, (error, data, response) => {
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

[**ImportationTechnicalProgression**](ImportationTechnicalProgression.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

