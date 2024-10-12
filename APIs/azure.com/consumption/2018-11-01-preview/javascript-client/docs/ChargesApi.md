# ConsumptionManagementClient.ChargesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chargesByBillingAccountList**](ChargesApi.md#chargesByBillingAccountList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/charges | 
[**chargesByBillingProfileList**](ChargesApi.md#chargesByBillingProfileList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/charges | 
[**chargesByInvoiceSectionList**](ChargesApi.md#chargesByInvoiceSectionList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}/providers/Microsoft.Consumption/charges | 



## chargesByBillingAccountList

> ChargesListByBillingAccount chargesByBillingAccountList(billingAccountId, apiVersion, startDate, endDate, opts)



Lists the charges by billingAccountId for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let startDate = "startDate_example"; // String | Start date
let endDate = "endDate_example"; // String | End date
let opts = {
  'apply': "apply_example" // String | May be used to group charges by properties/billingProfileId, or properties/invoiceSectionId.
};
apiInstance.chargesByBillingAccountList(billingAccountId, apiVersion, startDate, endDate, opts, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **startDate** | **String**| Start date | 
 **endDate** | **String**| End date | 
 **apply** | **String**| May be used to group charges by properties/billingProfileId, or properties/invoiceSectionId. | [optional] 

### Return type

[**ChargesListByBillingAccount**](ChargesListByBillingAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chargesByBillingProfileList

> ChargesListByBillingProfile chargesByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate)



Lists the charges by billing profile id for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let billingProfileId = "billingProfileId_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let startDate = "startDate_example"; // String | Start date
let endDate = "endDate_example"; // String | End date
apiInstance.chargesByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **billingProfileId** | **String**| Billing Profile Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **startDate** | **String**| Start date | 
 **endDate** | **String**| End date | 

### Return type

[**ChargesListByBillingProfile**](ChargesListByBillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chargesByInvoiceSectionList

> ChargesListByInvoiceSection chargesByInvoiceSectionList(billingAccountId, invoiceSectionId, apiVersion, startDate, endDate, opts)



Lists the charges by invoice section id for given start and end date. Start and end date are used to determine the billing period. For current month, the data will be provided from month to date. If there are no charges for a month then that month will show all zeroes.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ChargesApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let invoiceSectionId = "invoiceSectionId_example"; // String | Invoice Section Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let startDate = "startDate_example"; // String | Start date
let endDate = "endDate_example"; // String | End date
let opts = {
  'apply': "apply_example" // String | May be used to group charges by properties/productName.
};
apiInstance.chargesByInvoiceSectionList(billingAccountId, invoiceSectionId, apiVersion, startDate, endDate, opts, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **invoiceSectionId** | **String**| Invoice Section Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **startDate** | **String**| Start date | 
 **endDate** | **String**| End date | 
 **apply** | **String**| May be used to group charges by properties/productName. | [optional] 

### Return type

[**ChargesListByInvoiceSection**](ChargesListByInvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

