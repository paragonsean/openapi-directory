# ConsumptionManagementClient.ReservationTransactionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationTransactionsList**](ReservationTransactionsApi.md#reservationTransactionsList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/reservationTransactions | 



## reservationTransactionsList

> ReservationTransactionsListResult reservationTransactionsList(apiVersion, billingAccountId, opts)



List of transactions for reserved instances on billing account scope

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationTransactionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let opts = {
  'filter': "filter_example" // String | Filter reservation transactions by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
};
apiInstance.reservationTransactionsList(apiVersion, billingAccountId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **filter** | **String**| Filter reservation transactions by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | [optional] 

### Return type

[**ReservationTransactionsListResult**](ReservationTransactionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

