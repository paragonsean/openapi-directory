# AzureReservation.ReservationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservationGet**](ReservationApi.md#reservationGet) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId} | Get &#x60;Reservation&#x60; details.
[**reservationList**](ReservationApi.md#reservationList) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations | Get &#x60;Reservation&#x60;s in a given reservation Order
[**reservationListRevisions**](ReservationApi.md#reservationListRevisions) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}/revisions | Get &#x60;Reservation&#x60; revisions.
[**reservationOrderGet**](ReservationApi.md#reservationOrderGet) | **GET** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId} | Get a specific &#x60;ReservationOrder&#x60;.
[**reservationOrderList**](ReservationApi.md#reservationOrderList) | **GET** /providers/Microsoft.Capacity/reservationOrders | Get all &#x60;ReservationOrder&#x60;s.
[**reservationUpdate**](ReservationApi.md#reservationUpdate) | **PATCH** /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId} | Updates a &#x60;Reservation&#x60;.



## reservationGet

> ReservationResponse reservationGet(reservationId, reservationOrderId, apiVersion, opts)

Get &#x60;Reservation&#x60; details.

Get specific &#x60;Reservation&#x60; details.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationApi();
let reservationId = "reservationId_example"; // String | Id of the Reservation Item
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let opts = {
  'expand': "expand_example" // String | Supported value of this query is renewProperties
};
apiInstance.reservationGet(reservationId, reservationOrderId, apiVersion, opts, (error, data, response) => {
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
 **reservationId** | **String**| Id of the Reservation Item | 
 **reservationOrderId** | **String**| Order Id of the reservation | 
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **expand** | **String**| Supported value of this query is renewProperties | [optional] 

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationList

> ReservationList reservationList(reservationOrderId, apiVersion)

Get &#x60;Reservation&#x60;s in a given reservation Order

List &#x60;Reservation&#x60;s within a single &#x60;ReservationOrder&#x60;.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
apiInstance.reservationList(reservationOrderId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 

### Return type

[**ReservationList**](ReservationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationListRevisions

> ReservationList reservationListRevisions(reservationId, reservationOrderId, apiVersion)

Get &#x60;Reservation&#x60; revisions.

List of all the revisions for the &#x60;Reservation&#x60;.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationApi();
let reservationId = "reservationId_example"; // String | Id of the Reservation Item
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
apiInstance.reservationListRevisions(reservationId, reservationOrderId, apiVersion, (error, data, response) => {
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
 **reservationId** | **String**| Id of the Reservation Item | 
 **reservationOrderId** | **String**| Order Id of the reservation | 
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 

### Return type

[**ReservationList**](ReservationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationOrderGet

> ReservationOrderResponse reservationOrderGet(reservationOrderId, apiVersion, opts)

Get a specific &#x60;ReservationOrder&#x60;.

Get the details of the &#x60;ReservationOrder&#x60;.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let opts = {
  'expand': "expand_example" // String | May be used to expand the planInformation.
};
apiInstance.reservationOrderGet(reservationOrderId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **expand** | **String**| May be used to expand the planInformation. | [optional] 

### Return type

[**ReservationOrderResponse**](ReservationOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationOrderList

> ReservationOrderList reservationOrderList(apiVersion)

Get all &#x60;ReservationOrder&#x60;s.

List of all the &#x60;ReservationOrder&#x60;s that the user has access to in the current tenant.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationApi();
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
apiInstance.reservationOrderList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 

### Return type

[**ReservationOrderList**](ReservationOrderList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reservationUpdate

> ReservationResponse reservationUpdate(reservationOrderId, reservationId, apiVersion, parameters)

Updates a &#x60;Reservation&#x60;.

Updates the applied scopes of the &#x60;Reservation&#x60;.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.ReservationApi();
let reservationOrderId = "reservationOrderId_example"; // String | Order Id of the reservation
let reservationId = "reservationId_example"; // String | Id of the Reservation Item
let apiVersion = "apiVersion_example"; // String | Supported version for this document is 2019-04-01
let parameters = new AzureReservation.Patch(); // Patch | Information needed to patch a reservation item
apiInstance.reservationUpdate(reservationOrderId, reservationId, apiVersion, parameters, (error, data, response) => {
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
 **reservationId** | **String**| Id of the Reservation Item | 
 **apiVersion** | **String**| Supported version for this document is 2019-04-01 | 
 **parameters** | [**Patch**](Patch.md)| Information needed to patch a reservation item | 

### Return type

[**ReservationResponse**](ReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

