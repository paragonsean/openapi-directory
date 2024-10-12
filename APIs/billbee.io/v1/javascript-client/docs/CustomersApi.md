# BillbeeApi.CustomersApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddCustomerAddress**](CustomersApi.md#customerAddCustomerAddress) | **POST** /api/v1/customers/{id}/addresses | Adds a new address to a customer
[**customerCreate**](CustomersApi.md#customerCreate) | **POST** /api/v1/customers | Creates a new customer
[**customerGetAll**](CustomersApi.md#customerGetAll) | **GET** /api/v1/customers | Get a list of all customers
[**customerGetCustomerAddress**](CustomersApi.md#customerGetCustomerAddress) | **GET** /api/v1/customers/addresses/{id} | Queries a single address from a customer
[**customerGetCustomerAddresses**](CustomersApi.md#customerGetCustomerAddresses) | **GET** /api/v1/customers/{id}/addresses | Queries a list of addresses from a customer
[**customerGetCustomerOrders**](CustomersApi.md#customerGetCustomerOrders) | **GET** /api/v1/customers/{id}/orders | Queries a list of orders from a customer
[**customerGetOne**](CustomersApi.md#customerGetOne) | **GET** /api/v1/customers/{id} | Queries a single customer by id
[**customerPatchAddress**](CustomersApi.md#customerPatchAddress) | **PATCH** /api/v1/customers/addresses/{id} | Updates one or more fields of an address
[**customerUpdate**](CustomersApi.md#customerUpdate) | **PUT** /api/v1/customers/{id} | Updates a customer by id
[**customerUpdateAddress**](CustomersApi.md#customerUpdateAddress) | **PUT** /api/v1/customers/addresses/{id} | Updates all fields of an address
[**searchSearch_0**](CustomersApi.md#searchSearch_0) | **POST** /api/v1/search | Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax



## customerAddCustomerAddress

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddCustomerAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Adds a new address to a customer

Id and  CustomerId will be ignored in model. If Id is set, the addition will be stopped.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | CustomerId to attach the new address to.
let billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | Model containing the address, that should be attached.
apiInstance.customerAddCustomerAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel, (error, data, response) => {
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
 **id** | **Number**| CustomerId to attach the new address to. | 
 **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)| Model containing the address, that should be attached. | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## customerCreate

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerCreate(billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel)

Creates a new customer

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel(); // BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel | 
apiInstance.customerCreate(billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelCreateCustomerApiModel** | [**BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel**](BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## customerGetAll

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerGetAll(opts)

Get a list of all customers

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let opts = {
  'page': 56, // Number | The current page to request starting with 1
  'pageSize': 56 // Number | The pagesize for the result list. Values between 1 and 250 are allowed
};
apiInstance.customerGetAll(opts, (error, data, response) => {
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
 **page** | **Number**| The current page to request starting with 1 | [optional] 
 **pageSize** | **Number**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerGetCustomerAddress

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerGetCustomerAddress(id)

Queries a single address from a customer

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the address
apiInstance.customerGetCustomerAddress(id, (error, data, response) => {
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
 **id** | **Number**| The id of the address | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerGetCustomerAddresses

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerGetCustomerAddresses(id, opts)

Queries a list of addresses from a customer

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the customer
let opts = {
  'page': 56, // Number | The current page to request starting with 1
  'pageSize': 56 // Number | The pagesize for the result list. Values between 1 and 250 are allowed
};
apiInstance.customerGetCustomerAddresses(id, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the customer | 
 **page** | **Number**| The current page to request starting with 1 | [optional] 
 **pageSize** | **Number**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerGetCustomerOrders

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder customerGetCustomerOrders(id, opts)

Queries a list of orders from a customer

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the customer
let opts = {
  'page': 56, // Number | The current page to request starting with 1
  'pageSize': 56 // Number | The pagesize for the result list. Values between 1 and 250 are allowed
};
apiInstance.customerGetCustomerOrders(id, opts, (error, data, response) => {
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
 **id** | **Number**| The id of the customer | 
 **page** | **Number**| The current page to request starting with 1 | [optional] 
 **pageSize** | **Number**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerGetOne

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerGetOne(id)

Queries a single customer by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the customer to query
apiInstance.customerGetOne(id, (error, data, response) => {
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
 **id** | **Number**| The id of the customer to query | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerPatchAddress

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerPatchAddress(id, body)

Updates one or more fields of an address

Id and CustomerId cannot be changed

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the address
let body = {key: null}; // Object | The address fields to be changed. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed.
apiInstance.customerPatchAddress(id, body, (error, data, response) => {
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
 **id** | **Number**| The id of the address | 
 **body** | **Object**| The address fields to be changed. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed. | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, application/xml, text/json, text/xml


## customerUpdate

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel customerUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerApiModel)

Updates a customer by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the customer
let billbeeInterfacesBillbeeAPIModelCustomerApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCustomerApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerApiModel | 
apiInstance.customerUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerApiModel, (error, data, response) => {
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
 **id** | **Number**| The id of the customer | 
 **billbeeInterfacesBillbeeAPIModelCustomerApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## customerUpdateAddress

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerUpdateAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Updates all fields of an address

Id and CustomerId cannot be changed. Fields you do not send will become empty.

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let id = 789; // Number | The id of the address
let billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | The updated address. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed.
apiInstance.customerUpdateAddress(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel, (error, data, response) => {
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
 **id** | **Number**| The id of the address | 
 **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)| The updated address. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed. | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## searchSearch_0

> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel searchSearch_0(rechnungsdruckWebAppControllersApiSearchControllerSearchModel)

Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomersApi();
let rechnungsdruckWebAppControllersApiSearchControllerSearchModel = new BillbeeApi.RechnungsdruckWebAppControllersApiSearchControllerSearchModel(); // RechnungsdruckWebAppControllersApiSearchControllerSearchModel | 
apiInstance.searchSearch_0(rechnungsdruckWebAppControllersApiSearchControllerSearchModel, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiSearchControllerSearchModel** | [**RechnungsdruckWebAppControllersApiSearchControllerSearchModel**](RechnungsdruckWebAppControllersApiSearchControllerSearchModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

