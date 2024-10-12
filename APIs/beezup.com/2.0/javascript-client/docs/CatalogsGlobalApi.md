# BeezUpMerchantApi.CatalogsGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogGetBeezUPColumns**](CatalogsGlobalApi.md#catalogGetBeezUPColumns) | **GET** /v2/user/catalogs/beezupColumns | Get the BeezUP columns
[**catalogIndex**](CatalogsGlobalApi.md#catalogIndex) | **GET** /v2/user/catalogs/ | Get the index of the catalog API



## catalogGetBeezUPColumns

> [BeezUPColumnConfiguration] catalogGetBeezUPColumns()

Get the BeezUP columns

Get the BeezUP columns, this columns are used for mapping during the manual catalog importation process.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsGlobalApi();
apiInstance.catalogGetBeezUPColumns((error, data, response) => {
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

[**[BeezUPColumnConfiguration]**](BeezUPColumnConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## catalogIndex

> CatalogIndex catalogIndex()

Get the index of the catalog API

The operation will give you all the operations you will be able to do and all the LOV used in this API.

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CatalogsGlobalApi();
apiInstance.catalogIndex((error, data, response) => {
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

[**CatalogIndex**](CatalogIndex.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

