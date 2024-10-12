# Labs64NetLicensingResTfulApiTestCenter.TransactionApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTransaction**](TransactionApi.md#createTransaction) | **POST** /transaction | Create Transaction
[**getTransaction**](TransactionApi.md#getTransaction) | **GET** /transaction/{transactionNumber} | Get Transaction 
[**listTransactions**](TransactionApi.md#listTransactions) | **GET** /transaction | List Transactions
[**updateTransaction**](TransactionApi.md#updateTransaction) | **POST** /transaction/{transactionNumber} | Update Transaction



## createTransaction

> Netlicensing createTransaction(active, source, status, opts)

Create Transaction

Creates a new Transaction

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TransactionApi();
let active = true; // Boolean | Always 'true' for Transactions
let source = "source_example"; // String | AUTO Transaction for internal use only
let status = "status_example"; // String | 
let opts = {
  'dateClosed': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'licenseeNumber': "licenseeNumber_example", // String | 
  'number': "number_example", // String | Unique number (across all Products of a Vendor) that identifies the Transaction
  'paymentMethod': "paymentMethod_example" // String | 
};
apiInstance.createTransaction(active, source, status, opts, (error, data, response) => {
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
 **active** | **Boolean**| Always &#39;true&#39; for Transactions | 
 **source** | **String**| AUTO Transaction for internal use only | 
 **status** | **String**|  | 
 **dateClosed** | **Date**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **licenseeNumber** | **String**|  | [optional] 
 **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | [optional] 
 **paymentMethod** | **String**|  | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## getTransaction

> Netlicensing getTransaction(transactionNumber)

Get Transaction 

Return a Transaction by &#39;transactionNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TransactionApi();
let transactionNumber = "transactionNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Transaction
apiInstance.getTransaction(transactionNumber, (error, data, response) => {
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
 **transactionNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listTransactions

> [Netlicensing] listTransactions()

List Transactions

Return a list of all Transactions for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TransactionApi();
apiInstance.listTransactions((error, data, response) => {
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

[**[Netlicensing]**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateTransaction

> Netlicensing updateTransaction(transactionNumber, opts)

Update Transaction

Sets the provided properties to a Transaction. Return an updated Transaction

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.TransactionApi();
let transactionNumber = "transactionNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Transaction
let opts = {
  'active': true, // Boolean | Always 'true' for Transactions
  'dateClosed': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'number': "number_example", // String | Unique number (across all Products of a Vendor) that identifies the Transaction
  'paymentMethod': "paymentMethod_example", // String | 
  'source': "source_example", // String | AUTO Transaction for internal use only
  'status': "status_example" // String | 
};
apiInstance.updateTransaction(transactionNumber, opts, (error, data, response) => {
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
 **transactionNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | 
 **active** | **Boolean**| Always &#39;true&#39; for Transactions | [optional] 
 **dateClosed** | **Date**|  | [optional] 
 **dateCreated** | **Date**|  | [optional] 
 **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Transaction | [optional] 
 **paymentMethod** | **String**|  | [optional] 
 **source** | **String**| AUTO Transaction for internal use only | [optional] 
 **status** | **String**|  | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

