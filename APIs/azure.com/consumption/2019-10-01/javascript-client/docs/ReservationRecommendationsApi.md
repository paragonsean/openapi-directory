# ConsumptionManagementClient.ReservationRecommendationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationRecommendationsList**](ReservationRecommendationsApi.md#reservationRecommendationsList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationRecommendations | 



## reservationRecommendationsList

> ReservationRecommendationsListResult reservationRecommendationsList(apiVersion, scope, opts)



List of recommendations for purchasing reserved instances.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationRecommendationsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let scope = "scope_example"; // String | The scope associated with reservation recommendations operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope
let opts = {
  'filter': "filter_example" // String | May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod.
};
apiInstance.reservationRecommendationsList(apiVersion, scope, opts, (error, data, response) => {
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
 **scope** | **String**| The scope associated with reservation recommendations operations. This includes &#39;/subscriptions/{subscriptionId}/&#39; for subscription scope, &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope, and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for billingProfile scope | 
 **filter** | **String**| May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod. | [optional] 

### Return type

[**ReservationRecommendationsListResult**](ReservationRecommendationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

