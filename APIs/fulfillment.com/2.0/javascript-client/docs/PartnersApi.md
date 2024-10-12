# FulfillmentComApiv2.PartnersApi

All URIs are relative to *https://api.fulfillment.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**putOrdersIdShip**](PartnersApi.md#putOrdersIdShip) | **PUT** /orders/{id}/ship | Ship an Order
[**putOrdersIdStatus**](PartnersApi.md#putOrdersIdStatus) | **PUT** /orders/{id}/status | Update Order Status



## putOrdersIdShip

> Object putOrdersIdShip(id, body)

Ship an Order

Note, this API is used to update orders and is reserved for our shipping partners.

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.PartnersApi();
let id = 56; // Number | The FDC order Id
let body = new FulfillmentComApiv2.OrderShipV2(); // OrderShipV2 | Shipping Details
apiInstance.putOrdersIdShip(id, body, (error, data, response) => {
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
 **id** | **Number**| The FDC order Id | 
 **body** | [**OrderShipV2**](OrderShipV2.md)| Shipping Details | 

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putOrdersIdStatus

> Object putOrdersIdStatus(id, body)

Update Order Status

Note, this API is used to update orders and is reserved for our shipping partners.

### Example

```javascript
import FulfillmentComApiv2 from 'fulfillment_com_apiv2';
let defaultClient = FulfillmentComApiv2.ApiClient.instance;
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: fdcAuth
let fdcAuth = defaultClient.authentications['fdcAuth'];
fdcAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FulfillmentComApiv2.PartnersApi();
let id = 56; // Number | The FDC order Id
let body = new FulfillmentComApiv2.StatusTypeSimpleV2(); // StatusTypeSimpleV2 | New status event
apiInstance.putOrdersIdStatus(id, body, (error, data, response) => {
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
 **id** | **Number**| The FDC order Id | 
 **body** | [**StatusTypeSimpleV2**](StatusTypeSimpleV2.md)| New status event | 

### Return type

**Object**

### Authorization

[fdcAuth](../README.md#fdcAuth), [fdcAuth](../README.md#fdcAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

