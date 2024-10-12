# BillingManagementClient.TransfersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfersCancel**](TransfersApi.md#transfersCancel) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/transfers/{transferName} | 
[**transfersGet**](TransfersApi.md#transfersGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/transfers/{transferName} | 
[**transfersInitiate**](TransfersApi.md#transfersInitiate) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/initiateTransfer | 
[**transfersList**](TransfersApi.md#transfersList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/transfers | 



## transfersCancel

> TransferDetails transfersCancel(billingAccountName, invoiceSectionName, transferName)



Cancels the transfer for given transfer Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransfersApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let transferName = "transferName_example"; // String | Transfer Name.
apiInstance.transfersCancel(billingAccountName, invoiceSectionName, transferName, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **transferName** | **String**| Transfer Name. | 

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transfersGet

> TransferDetails transfersGet(billingAccountName, invoiceSectionName, transferName)



Gets the transfer details for given transfer Id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransfersApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let transferName = "transferName_example"; // String | Transfer Name.
apiInstance.transfersGet(billingAccountName, invoiceSectionName, transferName, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **transferName** | **String**| Transfer Name. | 

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transfersInitiate

> TransferDetails transfersInitiate(billingAccountName, invoiceSectionName, body)



Initiates the request to transfer the legacy subscriptions or RIs.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransfersApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let body = new BillingManagementClient.InitiateTransferRequest(); // InitiateTransferRequest | Initiate transfer parameters.
apiInstance.transfersInitiate(billingAccountName, invoiceSectionName, body, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **body** | [**InitiateTransferRequest**](InitiateTransferRequest.md)| Initiate transfer parameters. | 

### Return type

[**TransferDetails**](TransferDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transfersList

> TransferDetailsListResult transfersList(billingAccountName, invoiceSectionName)



Lists all transfer&#39;s details initiated from given invoice section.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransfersApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.transfersList(billingAccountName, invoiceSectionName, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 

### Return type

[**TransferDetailsListResult**](TransferDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

