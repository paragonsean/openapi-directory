# ConsumptionManagementClient.LotsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lotsList**](LotsApi.md#lotsList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/lots | 



## lotsList

> Lots lotsList(billingAccountId, billingProfileId, apiVersion)



Lists the lots by billingAccountId and billingProfileId.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.LotsApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let billingProfileId = "billingProfileId_example"; // String | Azure Billing Profile ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
apiInstance.lotsList(billingAccountId, billingProfileId, apiVersion, (error, data, response) => {
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
 **billingProfileId** | **String**| Azure Billing Profile ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 

### Return type

[**Lots**](Lots.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

