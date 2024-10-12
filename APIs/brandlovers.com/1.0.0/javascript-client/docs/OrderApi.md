# BrandLoversMarketplaceApiV1.OrderApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orderOrderIdGet**](OrderApi.md#orderOrderIdGet) | **GET** /order/{orderId} | Returns all details of a order
[**orderOrderIdShipmentCancelPost**](OrderApi.md#orderOrderIdShipmentCancelPost) | **POST** /order/{orderId}/shipment/cancel | Confirm shipment canceletion (when requested by the customer) or failure to deliver
[**orderOrderIdShipmentDeliveredPost**](OrderApi.md#orderOrderIdShipmentDeliveredPost) | **POST** /order/{orderId}/shipment/delivered | Confirms that a shipment was delivered
[**orderOrderIdShipmentExchangePost**](OrderApi.md#orderOrderIdShipmentExchangePost) | **POST** /order/{orderId}/shipment/exchange | Confirm item exchange
[**orderOrderIdShipmentReturnPost**](OrderApi.md#orderOrderIdShipmentReturnPost) | **POST** /order/{orderId}/shipment/return | Confirm order item return and refund
[**orderOrderIdShipmentSentPost**](OrderApi.md#orderOrderIdShipmentSentPost) | **POST** /order/{orderId}/shipment/sent | Update new order to include shipment information



## orderOrderIdGet

> Order orderOrderIdGet(authorization, orderId)

Returns all details of a order

Returns all details of a single order, including last status, items shipped or not.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrderApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let orderId = "orderId_example"; // String | Unique Id of this order.
apiInstance.orderOrderIdGet(authorization, orderId, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **orderId** | **String**| Unique Id of this order. | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderOrderIdShipmentCancelPost

> orderOrderIdShipmentCancelPost(authorization, orderId, body)

Confirm shipment canceletion (when requested by the customer) or failure to deliver

Confirm shipment canceletion (when requested by the customer) or failure to deliver one shipment

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrderApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let orderId = "orderId_example"; // String | Unique Order Id
let body = new BrandLoversMarketplaceApiV1.NewTrackingRefund(); // NewTrackingRefund | 
apiInstance.orderOrderIdShipmentCancelPost(authorization, orderId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **orderId** | **String**| Unique Order Id | 
 **body** | [**NewTrackingRefund**](NewTrackingRefund.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## orderOrderIdShipmentDeliveredPost

> orderOrderIdShipmentDeliveredPost(authorization, orderId, body)

Confirms that a shipment was delivered

Confirms that a shipment was delivered. Must inform quantity of successfully deliverd items even if items deliverd was less than the original order

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrderApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let orderId = "orderId_example"; // String | Unique Order Id
let body = new BrandLoversMarketplaceApiV1.Newshipmentstatus(); // Newshipmentstatus | 
apiInstance.orderOrderIdShipmentDeliveredPost(authorization, orderId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **orderId** | **String**| Unique Order Id | 
 **body** | [**Newshipmentstatus**](Newshipmentstatus.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## orderOrderIdShipmentExchangePost

> orderOrderIdShipmentExchangePost(authorization, orderId, body)

Confirm item exchange

This enpoint to confirm item exchange when failure to deliver or requested by the customer. All customer requests are tracket via trouble tickets

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrderApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let orderId = "orderId_example"; // String | Unique Order Id
let body = new BrandLoversMarketplaceApiV1.NewTrackingRefund(); // NewTrackingRefund | 
apiInstance.orderOrderIdShipmentExchangePost(authorization, orderId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **orderId** | **String**| Unique Order Id | 
 **body** | [**NewTrackingRefund**](NewTrackingRefund.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## orderOrderIdShipmentReturnPost

> orderOrderIdShipmentReturnPost(authorization, orderId, body)

Confirm order item return and refund

Use this endpoint to return and refund items froma a order. In order to fully return an order list all items and applicate quantity.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrderApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let orderId = "orderId_example"; // String | Order unique Id
let body = new BrandLoversMarketplaceApiV1.NewTrackingRefund(); // NewTrackingRefund | 
apiInstance.orderOrderIdShipmentReturnPost(authorization, orderId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **orderId** | **String**| Order unique Id | 
 **body** | [**NewTrackingRefund**](NewTrackingRefund.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## orderOrderIdShipmentSentPost

> orderOrderIdShipmentSentPost(authorization, orderId, body)

Update new order to include shipment information

Updates order to include shipment shiped information. This endpoint can be used to include a single or multiple shipments for any give order. In order to inform that all items of a order where shipped list all of them, including applicable quantities in the payload.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrderApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let orderId = "orderId_example"; // String | Unique Order Id
let body = new BrandLoversMarketplaceApiV1.Newshipmentstatus(); // Newshipmentstatus | 
apiInstance.orderOrderIdShipmentSentPost(authorization, orderId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **orderId** | **String**| Unique Order Id | 
 **body** | [**Newshipmentstatus**](Newshipmentstatus.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

