# BillingManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingSubscriptionsTransfer**](DefaultApi.md#billingSubscriptionsTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName}/transfer | 
[**billingSubscriptionsValidateTransfer**](DefaultApi.md#billingSubscriptionsValidateTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName}/validateTransferEligibility | 
[**productsValidateTransfer**](DefaultApi.md#productsValidateTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName}/validateTransferEligibility | 



## billingSubscriptionsTransfer

> TransferBillingSubscriptionResult billingSubscriptionsTransfer(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, parameters)



Transfers the subscription from one invoice section to another within a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.DefaultApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let parameters = new BillingManagementClient.TransferBillingSubscriptionRequestProperties(); // TransferBillingSubscriptionRequestProperties | Request parameters supplied to the Transfer Billing Subscription operation.
apiInstance.billingSubscriptionsTransfer(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, parameters, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **parameters** | [**TransferBillingSubscriptionRequestProperties**](TransferBillingSubscriptionRequestProperties.md)| Request parameters supplied to the Transfer Billing Subscription operation. | 

### Return type

[**TransferBillingSubscriptionResult**](TransferBillingSubscriptionResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingSubscriptionsValidateTransfer

> ValidateSubscriptionTransferEligibilityResult billingSubscriptionsValidateTransfer(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, parameters)



Validates the transfer of billing subscriptions across invoice sections.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.DefaultApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let parameters = new BillingManagementClient.TransferBillingSubscriptionRequestProperties(); // TransferBillingSubscriptionRequestProperties | Parameters supplied to the Transfer Billing Subscription operation.
apiInstance.billingSubscriptionsValidateTransfer(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, parameters, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **parameters** | [**TransferBillingSubscriptionRequestProperties**](TransferBillingSubscriptionRequestProperties.md)| Parameters supplied to the Transfer Billing Subscription operation. | 

### Return type

[**ValidateSubscriptionTransferEligibilityResult**](ValidateSubscriptionTransferEligibilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsValidateTransfer

> ValidateProductTransferEligibilityResult productsValidateTransfer(billingAccountName, billingProfileName, invoiceSectionName, productName, parameters)



Validates the transfer of products across invoice sections.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.DefaultApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let productName = "productName_example"; // String | Invoice Id.
let parameters = new BillingManagementClient.TransferProductRequestProperties(); // TransferProductRequestProperties | Parameters supplied to the Transfer Products operation.
apiInstance.productsValidateTransfer(billingAccountName, billingProfileName, invoiceSectionName, productName, parameters, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **productName** | **String**| Invoice Id. | 
 **parameters** | [**TransferProductRequestProperties**](TransferProductRequestProperties.md)| Parameters supplied to the Transfer Products operation. | 

### Return type

[**ValidateProductTransferEligibilityResult**](ValidateProductTransferEligibilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

