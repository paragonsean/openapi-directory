# NordigenAccountInformationServicesApi.PremiumApi

All URIs are relative to *https://ob.nordigen.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveAccountTransactionsV2**](PremiumApi.md#retrieveAccountTransactionsV2) | **GET** /api/v2/accounts/premium/{id}/transactions/ | 



## retrieveAccountTransactionsV2

> {String: Object} retrieveAccountTransactionsV2(id, opts)



Access account premium transactions.

### Example

```javascript
import NordigenAccountInformationServicesApi from 'nordigen_account_information_services_api';
let defaultClient = NordigenAccountInformationServicesApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwtAuth
let jwtAuth = defaultClient.authentications['jwtAuth'];
jwtAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new NordigenAccountInformationServicesApi.PremiumApi();
let id = "id_example"; // String | 
let opts = {
  'country': "AT", // String | ISO 3166 two-character country code
  'dateFrom': new Date("2023-01-21"), // Date | 
  'dateTo': new Date("2023-04-21") // Date | 
};
apiInstance.retrieveAccountTransactionsV2(id, opts, (error, data, response) => {
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
 **country** | **String**| ISO 3166 two-character country code | [optional] 
 **dateFrom** | **Date**|  | [optional] 
 **dateTo** | **Date**|  | [optional] 

### Return type

**{String: Object}**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

