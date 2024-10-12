# ConsumptionManagementClient.ReservedInstancesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationsDetailsListByReservationOrder**](ReservedInstancesApi.md#reservationsDetailsListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationDetails | 
[**reservationsDetailsListByReservationOrderAndReservation**](ReservedInstancesApi.md#reservationsDetailsListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationDetails | 
[**reservationsSummariesListByReservationOrder**](ReservedInstancesApi.md#reservationsSummariesListByReservationOrder) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/providers/Microsoft.Consumption/reservationSummaries | 
[**reservationsSummariesListByReservationOrderAndReservation**](ReservedInstancesApi.md#reservationsSummariesListByReservationOrderAndReservation) | **GET** /providers/Microsoft.Capacity/reservationorders/{reservationOrderId}/reservations/{reservationId}/providers/Microsoft.Consumption/reservationSummaries | 



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

let apiInstance = new ConsumptionManagementClient.ReservedInstancesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let filter = "filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 

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

let apiInstance = new ConsumptionManagementClient.ReservedInstancesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the reservation
let filter = "filter_example"; // String | Filter reservation details by date range. The properties/UsageDate for start date and end date. The filter supports 'le' and  'ge' 
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 

### Return type

[**ReservationDetailsListResult**](ReservationDetailsListResult.md)

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

let apiInstance = new ConsumptionManagementClient.ReservedInstancesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let grain = "grain_example"; // String | Can be daily or monthly
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 
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

let apiInstance = new ConsumptionManagementClient.ReservedInstancesApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the reservation
let grain = "grain_example"; // String | Can be daily or monthly
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 
 **filter** | **String**| Required only for daily grain. The properties/UsageDate for start date and end date. The filter supports &#39;le&#39; and  &#39;ge&#39; | [optional] 

### Return type

[**ReservationSummariesListResult**](ReservationSummariesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

