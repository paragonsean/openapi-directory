# ManagementApi.TerminalOrdersCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompaniesCompanyIdBillingEntities**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdBillingEntities) | **GET** /companies/{companyId}/billingEntities | Get a list of billing entities
[**getCompaniesCompanyIdShippingLocations**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdShippingLocations) | **GET** /companies/{companyId}/shippingLocations | Get a list of shipping locations
[**getCompaniesCompanyIdTerminalModels**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalModels) | **GET** /companies/{companyId}/terminalModels | Get a list of terminal models
[**getCompaniesCompanyIdTerminalOrders**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalOrders) | **GET** /companies/{companyId}/terminalOrders | Get a list of orders
[**getCompaniesCompanyIdTerminalOrdersOrderId**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalOrdersOrderId) | **GET** /companies/{companyId}/terminalOrders/{orderId} | Get an order
[**getCompaniesCompanyIdTerminalProducts**](TerminalOrdersCompanyLevelApi.md#getCompaniesCompanyIdTerminalProducts) | **GET** /companies/{companyId}/terminalProducts | Get a list of terminal products
[**patchCompaniesCompanyIdTerminalOrdersOrderId**](TerminalOrdersCompanyLevelApi.md#patchCompaniesCompanyIdTerminalOrdersOrderId) | **PATCH** /companies/{companyId}/terminalOrders/{orderId} | Update an order
[**postCompaniesCompanyIdShippingLocations**](TerminalOrdersCompanyLevelApi.md#postCompaniesCompanyIdShippingLocations) | **POST** /companies/{companyId}/shippingLocations | Create a shipping location
[**postCompaniesCompanyIdTerminalOrders**](TerminalOrdersCompanyLevelApi.md#postCompaniesCompanyIdTerminalOrders) | **POST** /companies/{companyId}/terminalOrders | Create an order
[**postCompaniesCompanyIdTerminalOrdersOrderIdCancel**](TerminalOrdersCompanyLevelApi.md#postCompaniesCompanyIdTerminalOrdersOrderIdCancel) | **POST** /companies/{companyId}/terminalOrders/{orderId}/cancel | Cancel an order



## getCompaniesCompanyIdBillingEntities

> BillingEntitiesResponse getCompaniesCompanyIdBillingEntities(companyId, opts)

Get a list of billing entities

Returns the billing entities of the company identified in the path and all merchant accounts belonging to the company. A billing entity is a legal entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'name': "name_example" // String | The name of the billing entity.
};
apiInstance.getCompaniesCompanyIdBillingEntities(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **name** | **String**| The name of the billing entity. | [optional] 

### Return type

[**BillingEntitiesResponse**](BillingEntitiesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdShippingLocations

> ShippingLocationsResponse getCompaniesCompanyIdShippingLocations(companyId, opts)

Get a list of shipping locations

Returns the shipping locations for the company identified in the path and all merchant accounts belonging to the company. A shipping location includes the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'name': "name_example", // String | The name of the shipping location.
  'offset': 56, // Number | The number of locations to skip.
  'limit': 56 // Number | The number of locations to return.
};
apiInstance.getCompaniesCompanyIdShippingLocations(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **name** | **String**| The name of the shipping location. | [optional] 
 **offset** | **Number**| The number of locations to skip. | [optional] 
 **limit** | **Number**| The number of locations to return. | [optional] 

### Return type

[**ShippingLocationsResponse**](ShippingLocationsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdTerminalModels

> TerminalModelsResponse getCompaniesCompanyIdTerminalModels(companyId)

Get a list of terminal models

Returns a list of payment terminal models that the company identified in the path has access to. The response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a list of products for ordering.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
apiInstance.getCompaniesCompanyIdTerminalModels(companyId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 

### Return type

[**TerminalModelsResponse**](TerminalModelsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdTerminalOrders

> TerminalOrdersResponse getCompaniesCompanyIdTerminalOrders(companyId, opts)

Get a list of orders

Returns a lists of terminal products orders for the company identified in the path. To filter the list, use one or more of the query parameters.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'customerOrderReference': "customerOrderReference_example", // String | Your purchase order number.
  'status': "status_example", // String | The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered.
  'offset': 56, // Number | The number of orders to skip.
  'limit': 56 // Number | The number of orders to return.
};
apiInstance.getCompaniesCompanyIdTerminalOrders(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **customerOrderReference** | **String**| Your purchase order number. | [optional] 
 **status** | **String**| The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered. | [optional] 
 **offset** | **Number**| The number of orders to skip. | [optional] 
 **limit** | **Number**| The number of orders to return. | [optional] 

### Return type

[**TerminalOrdersResponse**](TerminalOrdersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdTerminalOrdersOrderId

> TerminalOrder getCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId)

Get an order

Returns the details of the terminal products order identified in the path.  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let orderId = "orderId_example"; // String | The unique identifier of the order.
apiInstance.getCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **orderId** | **String**| The unique identifier of the order. | 

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdTerminalProducts

> TerminalProductsResponse getCompaniesCompanyIdTerminalProducts(companyId, country, opts)

Get a list of terminal products

Returns a country-specific list of payment terminal packages and parts that the company identified in the path has access to.   To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let country = "country_example"; // String | The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US**
let opts = {
  'terminalModelId': "terminalModelId_example", // String | The terminal model to return products for. Use the ID returned in the [GET `/terminalModels`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) response. For example, **Verifone.M400**
  'offset': 56, // Number | The number of products to skip.
  'limit': 56 // Number | The number of products to return.
};
apiInstance.getCompaniesCompanyIdTerminalProducts(companyId, country, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **country** | **String**| The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US** | 
 **terminalModelId** | **String**| The terminal model to return products for. Use the ID returned in the [GET &#x60;/terminalModels&#x60;](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) response. For example, **Verifone.M400** | [optional] 
 **offset** | **Number**| The number of products to skip. | [optional] 
 **limit** | **Number**| The number of products to return. | [optional] 

### Return type

[**TerminalProductsResponse**](TerminalProductsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchCompaniesCompanyIdTerminalOrdersOrderId

> TerminalOrder patchCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId, opts)

Update an order

Updates the terminal products order identified in the path. Updating is only possible while the order has the status **Placed**.  The request body only needs to contain what you want to change.  However, to update the products in the &#x60;items&#x60; array, you must provide the entire array. For example, if the array has three items:  To remove one item, the array must include the remaining two items. Or to add one item, the array must include all four items.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let orderId = "orderId_example"; // String | The unique identifier of the order.
let opts = {
  'terminalOrderRequest': new ManagementApi.TerminalOrderRequest() // TerminalOrderRequest | 
};
apiInstance.patchCompaniesCompanyIdTerminalOrdersOrderId(companyId, orderId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **orderId** | **String**| The unique identifier of the order. | 
 **terminalOrderRequest** | [**TerminalOrderRequest**](TerminalOrderRequest.md)|  | [optional] 

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdShippingLocations

> ShippingLocation postCompaniesCompanyIdShippingLocations(companyId, opts)

Create a shipping location

Creates a shipping location for the company identified in the path. A shipping location defines an address where orders can be delivered.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'shippingLocation': new ManagementApi.ShippingLocation() // ShippingLocation | 
};
apiInstance.postCompaniesCompanyIdShippingLocations(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **shippingLocation** | [**ShippingLocation**](ShippingLocation.md)|  | [optional] 

### Return type

[**ShippingLocation**](ShippingLocation.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdTerminalOrders

> TerminalOrder postCompaniesCompanyIdTerminalOrders(companyId, opts)

Create an order

Creates an order for payment terminal products for the company identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write &gt;Requests to the Management API test endpoint do not create actual orders for test terminals. To order test terminals, you need to [submit a sales order](https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps) in your Customer Area.

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'terminalOrderRequest': new ManagementApi.TerminalOrderRequest() // TerminalOrderRequest | 
};
apiInstance.postCompaniesCompanyIdTerminalOrders(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **terminalOrderRequest** | [**TerminalOrderRequest**](TerminalOrderRequest.md)|  | [optional] 

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCompaniesCompanyIdTerminalOrdersOrderIdCancel

> TerminalOrder postCompaniesCompanyIdTerminalOrdersOrderIdCancel(companyId, orderId)

Cancel an order

Cancels the terminal products order identified in the path. Cancelling is only possible while the order has the status **Placed**. To cancel an order, make a POST call without a request body. The response returns the full order details, but with the status changed to **Cancelled**.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal ordering read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalOrdersCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let orderId = "orderId_example"; // String | The unique identifier of the order.
apiInstance.postCompaniesCompanyIdTerminalOrdersOrderIdCancel(companyId, orderId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **orderId** | **String**| The unique identifier of the order. | 

### Return type

[**TerminalOrder**](TerminalOrder.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

