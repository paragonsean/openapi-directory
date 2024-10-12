# BillbeeApi.CustomerAddressesApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAddressesCreate**](CustomerAddressesApi.md#customerAddressesCreate) | **POST** /api/v1/customer-addresses | Creates a new customer address
[**customerAddressesGetAll**](CustomerAddressesApi.md#customerAddressesGetAll) | **GET** /api/v1/customer-addresses | Get a list of all customer addresses
[**customerAddressesGetOne**](CustomerAddressesApi.md#customerAddressesGetOne) | **GET** /api/v1/customer-addresses/{id} | Queries a single customer address by id
[**customerAddressesUpdate**](CustomerAddressesApi.md#customerAddressesUpdate) | **PUT** /api/v1/customer-addresses/{id} | Updates a customer address by id



## customerAddressesCreate

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesCreate(billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Creates a new customer address

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomerAddressesApi();
let billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | 
apiInstance.customerAddressesCreate(billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## customerAddressesGetAll

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesGetAll(opts)

Get a list of all customer addresses

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomerAddressesApi();
let opts = {
  'page': 56, // Number | The current page to request starting with 1 (default is 1)
  'pageSize': 56 // Number | The page size for the result list. Values between 1 and 250 are allowed. (default is 50)
};
apiInstance.customerAddressesGetAll(opts, (error, data, response) => {
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
 **page** | **Number**| The current page to request starting with 1 (default is 1) | [optional] 
 **pageSize** | **Number**| The page size for the result list. Values between 1 and 250 are allowed. (default is 50) | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerAddressesGetOne

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesGetOne(id)

Queries a single customer address by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomerAddressesApi();
let id = 789; // Number | The id of the address to query
apiInstance.customerAddressesGetOne(id, (error, data, response) => {
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
 **id** | **Number**| The id of the address to query | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## customerAddressesUpdate

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel customerAddressesUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel)

Updates a customer address by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.CustomerAddressesApi();
let id = 789; // Number | The id of the address
let billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel(); // BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel | 
apiInstance.customerAddressesUpdate(id, billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelCustomerAddressApiModel** | [**BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

