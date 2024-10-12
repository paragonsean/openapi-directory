# BillingManagementClient.PriceSheetApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**priceSheetDownload**](PriceSheetApi.md#priceSheetDownload) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoices/{invoiceName}/pricesheet/default/download | 



## priceSheetDownload

> DownloadUrl priceSheetDownload(apiVersion, billingAccountName, invoiceName)



Download price sheet for an invoice.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.PriceSheetApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Azure Billing Account ID.
let invoiceName = "invoiceName_example"; // String | The name of an invoice resource.
apiInstance.priceSheetDownload(apiVersion, billingAccountName, invoiceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **billingAccountName** | **String**| Azure Billing Account ID. | 
 **invoiceName** | **String**| The name of an invoice resource. | 

### Return type

[**DownloadUrl**](DownloadUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

