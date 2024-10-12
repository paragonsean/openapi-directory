# NordigenAccountInformationServicesApi.AccountsApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveAccountBalancesV2**](AccountsApi.md#retrieveAccountBalancesV2) | **GET** /api/v2/accounts/{id}/balances/ | 
[**retrieveAccountDetailsV2**](AccountsApi.md#retrieveAccountDetailsV2) | **GET** /api/v2/accounts/{id}/details/ | 
[**retrieveAccountMetadata**](AccountsApi.md#retrieveAccountMetadata) | **GET** /api/v2/accounts/{id}/ | 
[**retrieveAccountTransactionsV22**](AccountsApi.md#retrieveAccountTransactionsV22) | **GET** /api/v2/accounts/{id}/transactions/ | 



## retrieveAccountBalancesV2

> {String: Object} retrieveAccountBalancesV2(id)



Access account balances.  Balances will be returned in Berlin Group PSD2 format.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AccountsApi();
let id = "id_example"; // String | 
apiInstance.retrieveAccountBalancesV2(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAccountDetailsV2

> {String: Object} retrieveAccountDetailsV2(id)



Access account details.  Account details will be returned in Berlin Group PSD2 format.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AccountsApi();
let id = "id_example"; // String | 
apiInstance.retrieveAccountDetailsV2(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAccountMetadata

> Account retrieveAccountMetadata(id)



Access account metadata.  Information about the account record, such as the processing status and IBAN.  Account status is recalculated based on the error count in the latest req.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AccountsApi();
let id = "id_example"; // String | 
apiInstance.retrieveAccountMetadata(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveAccountTransactionsV22

> {String: Object} retrieveAccountTransactionsV22(id, opts)



Access account transactions.  Transactions will be returned in Berlin Group PSD2 format.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.AccountsApi();
let id = "id_example"; // String | 
let opts = {
  'dateFrom': new Date("2023-01-21"), // Date | 
  'dateTo': new Date("2023-04-21") // Date | 
};
apiInstance.retrieveAccountTransactionsV22(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 

### Return type

**{String: Object}**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

