# ConsumptionManagementClient.PricesheetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingProfilePricesheetDownload**](PricesheetsApi.md#billingProfilePricesheetDownload) | **POST** /providers/Microsoft.Consumption/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/pricesheet/default/download | 
[**invoicePricesheetDownload**](PricesheetsApi.md#invoicePricesheetDownload) | **POST** /providers/Microsoft.Consumption/billingAccounts/{billingAccountId}/invoices/{invoiceName}/pricesheet/default/download | 



## billingProfilePricesheetDownload

> PricesheetDownloadResponse billingProfilePricesheetDownload(apiVersion, billingAccountId, billingProfileId)



Get pricesheet data for invoice id (invoiceName).

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.PricesheetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountId = "billingAccountId_example"; // String | Azure Billing Account Id.
let billingProfileId = "billingProfileId_example"; // String | Azure Billing Profile Id.
apiInstance.billingProfilePricesheetDownload(apiVersion, billingAccountId, billingProfileId, (error, data, response) => {
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
 **billingAccountId** | **String**| Azure Billing Account Id. | 
 **billingProfileId** | **String**| Azure Billing Profile Id. | 

### Return type

[**PricesheetDownloadResponse**](PricesheetDownloadResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicePricesheetDownload

> PricesheetDownloadResponse invoicePricesheetDownload(apiVersion, billingAccountId, invoiceName)



Get pricesheet data for invoice id (invoiceName).

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.PricesheetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountId = "billingAccountId_example"; // String | Azure Billing Account Id.
let invoiceName = "invoiceName_example"; // String | The name of an invoice resource.
apiInstance.invoicePricesheetDownload(apiVersion, billingAccountId, invoiceName, (error, data, response) => {
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
 **billingAccountId** | **String**| Azure Billing Account Id. | 
 **invoiceName** | **String**| The name of an invoice resource. | 

### Return type

[**PricesheetDownloadResponse**](PricesheetDownloadResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

