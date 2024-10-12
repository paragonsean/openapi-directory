# ConsumptionManagementClient.EventsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsByBillingProfileList**](EventsApi.md#eventsByBillingProfileList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/providers/Microsoft.Consumption/events | 



## eventsByBillingProfileList

> Events eventsByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate)



Lists the events by billingAccountId and billingProfileId for given start and end date.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.EventsApi();
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let billingProfileId = "billingProfileId_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let startDate = "startDate_example"; // String | Start date
let endDate = "endDate_example"; // String | End date
apiInstance.eventsByBillingProfileList(billingAccountId, billingProfileId, apiVersion, startDate, endDate, (error, data, response) => {
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

[**Events**](Events.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

