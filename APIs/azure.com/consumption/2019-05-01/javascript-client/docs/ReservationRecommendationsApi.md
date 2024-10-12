# ConsumptionManagementClient.ReservationRecommendationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationRecommendationsList**](ReservationRecommendationsApi.md#reservationRecommendationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/reservationRecommendations | 
[**reservationRecommendationsListByBillingAccountId**](ReservationRecommendationsApi.md#reservationRecommendationsListByBillingAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/microsoft.consumption/ReservationRecommendations | 



## reservationRecommendationsList

> ReservationRecommendationsListResult reservationRecommendationsList(apiVersion, subscriptionId, opts)



List of recommendations for purchasing reserved instances.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationRecommendationsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-05-01.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let opts = {
  'filter': "filter_example" // String | May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod.
};
apiInstance.reservationRecommendationsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-05-01. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **filter** | **String**| May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod. | [optional] 

### Return type

[**ReservationRecommendationsListResult**](ReservationRecommendationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationRecommendationsListByBillingAccountId

> ReservationRecommendationsListResult reservationRecommendationsListByBillingAccountId(apiVersion, billingAccountId, opts)



List of recommendations for purchasing reserved instances on billing account scope

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationRecommendationsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-05-01.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let opts = {
  'filter': "filter_example" // String | May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod.
};
apiInstance.reservationRecommendationsListByBillingAccountId(apiVersion, billingAccountId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-05-01. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **filter** | **String**| May be used to filter reservationRecommendations by properties/scope and properties/lookBackPeriod. | [optional] 

### Return type

[**ReservationRecommendationsListResult**](ReservationRecommendationsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

