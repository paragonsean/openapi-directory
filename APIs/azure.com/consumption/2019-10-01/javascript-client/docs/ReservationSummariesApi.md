# ConsumptionManagementClient.ReservationSummariesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationsSummariesList**](ReservationSummariesApi.md#reservationsSummariesList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationSummaries | 
[**reservationsSummariesListByReservationOrder**](ReservationSummariesApi.md#reservationsSummariesListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationSummaries | 
[**reservationsSummariesListByReservationOrderAndReservation**](ReservationSummariesApi.md#reservationsSummariesListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationSummaries | 



## reservationsSummariesList

> ReservationSummariesListResult reservationsSummariesList(scope, grain, apiVersion, opts)



Lists the reservations summaries for the defined scope daily or monthly grain.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationSummariesApi();
let scope = "scope_example"; // String | The scope associated with reservations summaries operations. This includes '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope (legacy), and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope (modern). 
let grain = "grain_example"; // String | Can be daily or monthly
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let opts = {
  'startDate': "startDate_example", // String | Start date
  'endDate': "endDate_example", // String | End date
  'filter': "filter_example" // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
};
apiInstance.reservationsSummariesList(scope, grain, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope associated with reservations summaries operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope (legacy), and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope (modern).  | 
 **grain** | **String**| Can be daily or monthly | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 
 **startDate** | **String**| Start date | [optional] 
 **endDate** | **String**| End date | [optional] 
 **filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] 

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationsSummariesListByReservationOrder

> ReservationSummariesListResult reservationsSummariesListByReservationOrder(reservationOrderId, grain, apiVersion, opts)



Lists the reservations summaries for daily or monthly grain.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationSummariesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let grain = "grain_example"; // String | Can be daily or monthly
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let opts = {
  'filter': "filter_example" // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
};
apiInstance.reservationsSummariesListByReservationOrder(reservationOrderId, grain, apiVersion, opts, (error, data, response) => {
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
 **reservationOrderId** | **String**| Order Id of the reservation | 
 **grain** | **String**| Can be daily or monthly | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 
 **filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] 

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationsSummariesListByReservationOrderAndReservation

> ReservationSummariesListResult reservationsSummariesListByReservationOrderAndReservation(reservationOrderId, reservationId, grain, apiVersion, opts)



Lists the reservations summaries for daily or monthly grain.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationSummariesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the reservation
let grain = "grain_example"; // String | Can be daily or monthly
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let opts = {
  'filter': "filter_example" // String | Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge'
};
apiInstance.reservationsSummariesListByReservationOrderAndReservation(reservationOrderId, reservationId, grain, apiVersion, opts, (error, data, response) => {
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
 **reservationOrderId** | **String**| Order Id of the reservation | 
 **reservationId** | **String**| Id of the reservation | 
 **grain** | **String**| Can be daily or monthly | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 
 **filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] 

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

