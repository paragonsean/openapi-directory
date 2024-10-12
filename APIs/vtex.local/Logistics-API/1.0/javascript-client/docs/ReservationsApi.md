# LogisticsApi.ReservationsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acknowledgmentReservation**](ReservationsApi.md#acknowledgmentReservation) | **POST** /api/logistics/pvt/inventory/reservations/{reservationId}/acknowledge | Acknowledgment reservation
[**cancelReservation**](ReservationsApi.md#cancelReservation) | **POST** /api/logistics/pvt/inventory/reservations/{reservationId}/cancel | Cancel reservation
[**confirmReservation**](ReservationsApi.md#confirmReservation) | **POST** /api/logistics/pvt/inventory/reservations/{reservationId}/confirm | Confirm reservation
[**createReservation**](ReservationsApi.md#createReservation) | **POST** /api/logistics/pvt/inventory/reservations | Create reservation
[**reservationById**](ReservationsApi.md#reservationById) | **GET** /api/logistics/pvt/inventory/reservations/{reservationId} | List reservation by ID
[**reservationbyWarehouseandSku**](ReservationsApi.md#reservationbyWarehouseandSku) | **GET** /api/logistics/pvt/inventory/reservations/{warehouseId}/{skuId} | List reservation by warehouse and SKU



## acknowledgmentReservation

> acknowledgmentReservation(contentType, accept, reservationId)

Acknowledgment reservation

Acknowledges reservations made by reservation ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ReservationsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let reservationId = "reservationId_example"; // String | 
apiInstance.acknowledgmentReservation(contentType, accept, reservationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **reservationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cancelReservation

> cancelReservation(contentType, accept, reservationId)

Cancel reservation

Cancels reservation by reservation ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ReservationsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let reservationId = "reservationId_example"; // String | 
apiInstance.cancelReservation(contentType, accept, reservationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **reservationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## confirmReservation

> confirmReservation(contentType, accept, reservationId)

Confirm reservation

Confirms reservation by reservation ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ReservationsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let reservationId = "reservationId_example"; // String | 
apiInstance.confirmReservation(contentType, accept, reservationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **reservationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createReservation

> CreateReservation200Response createReservation(accept, contentType, createReservationRequest1)

Create reservation

Creates [reservation](https://help.vtex.com/en/tutorial/how-does-reservation-work--tutorials_92).

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ReservationsApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent.
let createReservationRequest1 = {"autorizationExpirationTTL":"00:10:00","deliveryItemOptions":[{"aditionalTimeBlockedDays":"00:00:00","deliveryWindows":[],"dockId":"1a8bce3","dockTime":"00:00:00","item":{"additionalHandlingTime":"00:00:00","dimension":{"height":1,"length":1,"weight":150,"width":1},"groupItemId":null,"id":"2390059","kitItem":[],"price":0,"quantity":1},"listPrice":10.5,"location":{"country":"BRA","inStore":{"IsCheckedIn":false,"StoreId":null},"zipCode":"22220070"},"promotionalPrice":10.5,"slaType":"Expressa","slaTypeName":"Expressa","timeToDockPlusDockTime":"1.00:00:00","totalTime":"3.00:00:00","transitTime":"2.00:00:00","wareHouseId":null}],"lockId":null,"salesChannel":"1"}; // CreateReservationRequest1 | 
apiInstance.createReservation(accept, contentType, createReservationRequest1, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **createReservationRequest1** | [**CreateReservationRequest1**](CreateReservationRequest1.md)|  | 

### Return type

[**CreateReservation200Response**](CreateReservation200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json; charset=utf-8
- **Accept**: application/json; charset=utf-8


## reservationById

> ReservationById200Response reservationById(contentType, accept, reservationId)

List reservation by ID

Lists reservation&#39;s information by ID.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ReservationsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let reservationId = "reservationId_example"; // String | 
apiInstance.reservationById(contentType, accept, reservationId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **reservationId** | **String**|  | 

### Return type

[**ReservationById200Response**](ReservationById200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## reservationbyWarehouseandSku

> reservationbyWarehouseandSku(contentType, accept, warehouseId, skuId)

List reservation by warehouse and SKU

Lists reservations in your store, by searching through warehouse and SKU.

### Example

```javascript
import LogisticsApi from 'logistics_api';
let defaultClient = LogisticsApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LogisticsApi.ReservationsApi();
let contentType = "'application/json; charset=utf-8'"; // String | Type of the content being sent
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let warehouseId = "warehouseId_example"; // String | 
let skuId = "skuId_example"; // String | 
apiInstance.reservationbyWarehouseandSku(contentType, accept, warehouseId, skuId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json; charset&#x3D;utf-8&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **warehouseId** | **String**|  | 
 **skuId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

