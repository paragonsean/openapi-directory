# BrandLoversMarketplaceApiV1.OrdersApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ordersGet**](OrdersApi.md#ordersGet) | **GET** /orders | Returns orders details
[**ordersShipmentsDeliveredGet**](OrdersApi.md#ordersShipmentsDeliveredGet) | **GET** /orders/shipments/delivered | Returns list of shipments
[**ordersShipmentsDeliveredPost**](OrdersApi.md#ordersShipmentsDeliveredPost) | **POST** /orders/shipments/delivered | Bulk update of order shipments
[**ordersShipmentsShippedGet**](OrdersApi.md#ordersShipmentsShippedGet) | **GET** /orders/shipments/shipped | Returns a list of shipments shipped
[**ordersShipmentsShippedPost**](OrdersApi.md#ordersShipmentsShippedPost) | **POST** /orders/shipments/shipped | Bulk update of order shipments
[**ordersStatusApprovedGet**](OrdersApi.md#ordersStatusApprovedGet) | **GET** /orders/status/approved | Return list of approved orders
[**ordersStatusCanceledGet**](OrdersApi.md#ordersStatusCanceledGet) | **GET** /orders/status/canceled | Returns lists of canceled orders
[**ordersStatusDeliveredGet**](OrdersApi.md#ordersStatusDeliveredGet) | **GET** /orders/status/delivered | Returns a list of orders successfully delivered associated with this seller.
[**ordersStatusNewGet**](OrdersApi.md#ordersStatusNewGet) | **GET** /orders/status/new | Returns a list of orders flagged as new.
[**ordersStatusPartiallyDeliveredGet**](OrdersApi.md#ordersStatusPartiallyDeliveredGet) | **GET** /orders/status/partiallyDelivered | Returns a list of partially deliverd orders
[**ordersStatusPartiallySentGet**](OrdersApi.md#ordersStatusPartiallySentGet) | **GET** /orders/status/partiallySent | Returns a list of orders partially fullfiled
[**ordersStatusSentGet**](OrdersApi.md#ordersStatusSentGet) | **GET** /orders/status/sent | Returns a list with orders fully sent



## ordersGet

> GetOrders ordersGet(authorization, opts)

Returns orders details

Retuns a list of orders associated with this seller. The list is ordered by dateCreated.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersShipmentsDeliveredGet

> GetOrdersShipments ordersShipmentsDeliveredGet(authorization, opts)

Returns list of shipments

Returns list of shipments. By default this will return list of the last shipments ordered by dateCreated, folowed by last update date.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'status': "status_example", // String | Query by shippment status.
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersShipmentsDeliveredGet(authorization, opts, (error, data, response) => {
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
 **status** | **String**| Query by shippment status. | [optional] 
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrdersShipments**](GetOrdersShipments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersShipmentsDeliveredPost

> ordersShipmentsDeliveredPost(authorization, ordersshipments)

Bulk update of order shipments

Bulk update of order shipments status. This alows to inform multiple shipments status

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let ordersshipments = new BrandLoversMarketplaceApiV1.OrdersShipments(); // OrdersShipments | JSON body with list of shipments to be updated.
apiInstance.ordersShipmentsDeliveredPost(authorization, ordersshipments, (error, data, response) => {
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
 **ordersshipments** | [**OrdersShipments**](OrdersShipments.md)| JSON body with list of shipments to be updated. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## ordersShipmentsShippedGet

> GetOrdersShipments ordersShipmentsShippedGet(authorization, opts)

Returns a list of shipments shipped

Returns a list of shipments shipped. By Default returns items ordered by dateCreated folowed by last update

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'status': "status_example", // String | Product status.
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersShipmentsShippedGet(authorization, opts, (error, data, response) => {
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
 **status** | **String**| Product status. | [optional] 
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrdersShipments**](GetOrdersShipments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersShipmentsShippedPost

> ordersShipmentsShippedPost(ordersshipments)

Bulk update of order shipments

Allows bulk updates of orders shippments.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let ordersshipments = new BrandLoversMarketplaceApiV1.OrdersShipments(); // OrdersShipments | JSON payload with list of shippments of orders.
apiInstance.ordersShipmentsShippedPost(ordersshipments, (error, data, response) => {
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
 **ordersshipments** | [**OrdersShipments**](OrdersShipments.md)| JSON payload with list of shippments of orders. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## ordersStatusApprovedGet

> GetOrders ordersStatusApprovedGet(authorization, opts)

Return list of approved orders

Returns a list of approved orders. Orders in the &#x60;approved&#x60; state must be fullfiled imediadetelly.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 100, max 200. Use this in conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusApprovedGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 100, max 200. Use this in conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersStatusCanceledGet

> GetOrders ordersStatusCanceledGet(authorization, opts)

Returns lists of canceled orders

Returns a list with canceled orders. Canceled orders should not be fullfiled.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 100 // Number | Number or items to return when executing query. Default 100, max 250. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusCanceledGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Default 100, max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] [default to 100]

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersStatusDeliveredGet

> GetOrders ordersStatusDeliveredGet(authorization, opts)

Returns a list of orders successfully delivered associated with this seller.

Returns a list of orders successfully delivered associated with this seller.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusDeliveredGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersStatusNewGet

> GetOrders ordersStatusNewGet(authorization, opts)

Returns a list of orders flagged as new.

Returns a list of orders flagged as new. New orders should not be fullfiled until marketplace flags them as approved.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 100 // Number | Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusNewGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] [default to 100]

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersStatusPartiallyDeliveredGet

> GetOrders ordersStatusPartiallyDeliveredGet(authorization, opts)

Returns a list of partially deliverd orders

Returns a list of partially deliverd orders. This is a list of orders with items shipped but with not all items ackwlodged as deliverd

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 100 // Number | Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusPartiallyDeliveredGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 100. Max 250. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] [default to 100]

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersStatusPartiallySentGet

> GetOrders ordersStatusPartiallySentGet(authorization, opts)

Returns a list of orders partially fullfiled

Returns a list of orders that contain one (or more) items that where not shipped. This will list the entire order as well the items with peding shipment. Use this service to track orders that need to be fullfiled.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 100. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusPartiallySentGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 100. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersStatusSentGet

> GetOrders ordersStatusSentGet(authorization, opts)

Returns a list with orders fully sent

Returns a list with orders completely fullfiled, this means orders with all items sent. Orders will ordered by dateCreated fowllowed by last update

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.OrdersApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.ordersStatusSentGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetOrders**](GetOrders.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

