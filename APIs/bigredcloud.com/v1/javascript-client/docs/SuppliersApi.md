# BigRedCloudApi.SuppliersApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppliersDelete**](SuppliersApi.md#suppliersDelete) | **DELETE** /v1/suppliers/{id} | Removes an existing Supplier.
[**suppliersGet**](SuppliersApi.md#suppliersGet) | **GET** /v1/suppliers | Returns a list of company&#39;s Suppliers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.
[**suppliersGetAccountTrans**](SuppliersApi.md#suppliersGetAccountTrans) | **GET** /v1/suppliers/{itemId}/accountTrans | Returns a list of Supplier&#39;s account transactions.
[**suppliersGetOpeningBalance**](SuppliersApi.md#suppliersGetOpeningBalance) | **GET** /v1/suppliers/{itemId}/openingBalance | Returns a Supplier&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.
[**suppliersGetOpeningBalanceList**](SuppliersApi.md#suppliersGetOpeningBalanceList) | **GET** /v1/suppliers/{itemId}/openingBalanceList | Returns a list of Supplier&#39;s opening balance transactions.
[**suppliersPost**](SuppliersApi.md#suppliersPost) | **POST** /v1/suppliers | Creates a new Supplier.
[**suppliersProcessBatch**](SuppliersApi.md#suppliersProcessBatch) | **PUT** /v1/suppliers/batch | Processes a batch of Suppliers.
[**suppliersPut**](SuppliersApi.md#suppliersPut) | **PUT** /v1/suppliers/{id} | Updates an existing Supplier.
[**v1SuppliersIdGet**](SuppliersApi.md#v1SuppliersIdGet) | **GET** /v1/suppliers/{id} | Returns information about a single Supplier. You may specify that Supplier&#39;s ledger balance should be calculated.



## suppliersDelete

> Object suppliersDelete(id, timestamp)

Removes an existing Supplier.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let id = 789; // Number | Id of Supplier to remove.
let timestamp = "timestamp_example"; // String | Timestamp of Supplier to remove. Should be encoded in Base64.
apiInstance.suppliersDelete(id, timestamp, (error, data, response) => {
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
 **id** | **Number**| Id of Supplier to remove. | 
 **timestamp** | **String**| Timestamp of Supplier to remove. Should be encoded in Base64. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suppliersGet

> PageResultSupplierQueryDto suppliersGet()

Returns a list of company&#39;s Suppliers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; and \&quot;code\&quot; fields.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
apiInstance.suppliersGet((error, data, response) => {
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

[**PageResultSupplierQueryDto**](PageResultSupplierQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suppliersGetAccountTrans

> [AccountTranDto] suppliersGetAccountTrans(itemId)

Returns a list of Supplier&#39;s account transactions.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let itemId = 789; // Number | Id of Supplier to return account transaction.
apiInstance.suppliersGetAccountTrans(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Supplier to return account transaction. | 

### Return type

[**[AccountTranDto]**](AccountTranDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suppliersGetOpeningBalance

> OwnerOpeningBalanceInPeriodsDto suppliersGetOpeningBalance(itemId)

Returns a Supplier&#39;s opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let itemId = 789; // Number | Id of Supplier to return opening balances.
apiInstance.suppliersGetOpeningBalance(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Supplier to return opening balances. | 

### Return type

[**OwnerOpeningBalanceInPeriodsDto**](OwnerOpeningBalanceInPeriodsDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suppliersGetOpeningBalanceList

> [OwnerOpeningBalanceDto] suppliersGetOpeningBalanceList(itemId)

Returns a list of Supplier&#39;s opening balance transactions.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let itemId = 789; // Number | Id of Supplier to return opening balances transaction.
apiInstance.suppliersGetOpeningBalanceList(itemId, (error, data, response) => {
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
 **itemId** | **Number**| Id of Supplier to return opening balances transaction. | 

### Return type

[**[OwnerOpeningBalanceDto]**](OwnerOpeningBalanceDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suppliersPost

> Object suppliersPost(supplierDto)

Creates a new Supplier.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let supplierDto = new BigRedCloudApi.SupplierDto(); // SupplierDto | Information of Supplier to create.
apiInstance.suppliersPost(supplierDto, (error, data, response) => {
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
 **supplierDto** | [**SupplierDto**](SupplierDto.md)| Information of Supplier to create. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suppliersProcessBatch

> Object suppliersProcessBatch(batchItemSupplierDto)

Processes a batch of Suppliers.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let batchItemSupplierDto = [new BigRedCloudApi.BatchItemSupplierDto()]; // [BatchItemSupplierDto] | Batch of Suppliers to process.
apiInstance.suppliersProcessBatch(batchItemSupplierDto, (error, data, response) => {
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
 **batchItemSupplierDto** | [**[BatchItemSupplierDto]**](BatchItemSupplierDto.md)| Batch of Suppliers to process. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## suppliersPut

> Object suppliersPut(id, supplierDto)

Updates an existing Supplier.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let id = 789; // Number | Id of Supplier to update.
let supplierDto = new BigRedCloudApi.SupplierDto(); // SupplierDto | Information of Supplier to update.
apiInstance.suppliersPut(id, supplierDto, (error, data, response) => {
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
 **id** | **Number**| Id of Supplier to update. | 
 **supplierDto** | [**SupplierDto**](SupplierDto.md)| Information of Supplier to update. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## v1SuppliersIdGet

> SupplierDto v1SuppliersIdGet(id, opts)

Returns information about a single Supplier. You may specify that Supplier&#39;s ledger balance should be calculated.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.SuppliersApi();
let id = 789; // Number | Id of Supplier to return.
let opts = {
  'needBalance': true // Boolean | If \"true\" then Supplier's ledger balance will be calculated; otherwise balance will be returned as 0.
};
apiInstance.v1SuppliersIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| Id of Supplier to return. | 
 **needBalance** | **Boolean**| If \&quot;true\&quot; then Supplier&#39;s ledger balance will be calculated; otherwise balance will be returned as 0. | [optional] 

### Return type

[**SupplierDto**](SupplierDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

