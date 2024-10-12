# ConsumptionManagementClient.LotsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lotsByBillingProfileList**](LotsApi.md#lotsByBillingProfileList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/lots | 



## lotsByBillingProfileList

> Lots lotsByBillingProfileList(billingAccountId, billingProfileId, apiVersion)



Lists the lots by billingAccountId and billingProfileId for given start and end date.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.LotsApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let billingProfileId = "billingProfileId_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.lotsByBillingProfileList(billingAccountId, billingProfileId, apiVersion, (error, data, response) => {
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

### Return type

[**Lots**](Lots.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

