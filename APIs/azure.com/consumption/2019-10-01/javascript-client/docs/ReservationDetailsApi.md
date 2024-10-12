# ConsumptionManagementClient.ReservationDetailsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationsDetailsList**](ReservationDetailsApi.md#reservationsDetailsList) | **GET** /{scope}/providers/Microsoft.Consumption/reservationDetails | 
[**reservationsDetailsListByReservationOrder**](ReservationDetailsApi.md#reservationsDetailsListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationDetails | 
[**reservationsDetailsListByReservationOrderAndReservation**](ReservationDetailsApi.md#reservationsDetailsListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationDetails | 



## reservationsDetailsList

> ReservationDetailsListResult reservationsDetailsList(scope, apiVersion, opts)



Lists the reservations details for the defined scope and provided date range.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationDetailsApi();
let scope = "scope_example"; // String | The scope associated with reservations details operations. This includes '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for BillingAccount scope (legacy), and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope (modern). 
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
let opts = {
  'startDate': "startDate_example", // String | Start date
  'endDate': "endDate_example", // String | End date
  'filter': "filter_example" // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
};
apiInstance.reservationsDetailsList(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope associated with reservations details operations. This includes &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}&#39; for BillingAccount scope (legacy), and &#39;/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}&#39; for BillingProfile scope (modern).  | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 
 **startDate** | **String**| Start date | [optional] 
 **endDate** | **String**| End date | [optional] 
 **filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | [optional] 

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationsDetailsListByReservationOrder

> ReservationDetailsListResult reservationsDetailsListByReservationOrder(reservationOrderId, filter, apiVersion)



Lists the reservations details for provided date range.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationDetailsApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let filter = "filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
apiInstance.reservationsDetailsListByReservationOrder(reservationOrderId, filter, apiVersion, (error, data, response) => {
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
 **filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationsDetailsListByReservationOrderAndReservation

> ReservationDetailsListResult reservationsDetailsListByReservationOrderAndReservation(reservationOrderId, reservationId, filter, apiVersion)



Lists the reservations details for provided date range.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.ReservationDetailsApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the reservation
let filter = "filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01.
apiInstance.reservationsDetailsListByReservationOrderAndReservation(reservationOrderId, reservationId, filter, apiVersion, (error, data, response) => {
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
 **filter** | **String**| Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39;  | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01. | 

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

