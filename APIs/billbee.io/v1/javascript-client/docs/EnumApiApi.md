# BillbeeApi.EnumApiApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enumApiGetOrderStates**](EnumApiApi.md#enumApiGetOrderStates) | **GET** /api/v1/enums/orderstates | Returns a list with all defined orderstates
[**enumApiGetPaymentTypes**](EnumApiApi.md#enumApiGetPaymentTypes) | **GET** /api/v1/enums/paymenttypes | Returns a list with all defined paymenttypes
[**enumApiGetShipmentTypes**](EnumApiApi.md#enumApiGetShipmentTypes) | **GET** /api/v1/enums/shipmenttypes | Returns a list with all defined shipmenttypes
[**enumApiGetShippingCarriers**](EnumApiApi.md#enumApiGetShippingCarriers) | **GET** /api/v1/enums/shippingcarriers | Returns a list with all defined shippingcarriers



## enumApiGetOrderStates

> Object enumApiGetOrderStates()

Returns a list with all defined orderstates

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.EnumApiApi();
apiInstance.enumApiGetOrderStates((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## enumApiGetPaymentTypes

> Object enumApiGetPaymentTypes()

Returns a list with all defined paymenttypes

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.EnumApiApi();
apiInstance.enumApiGetPaymentTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## enumApiGetShipmentTypes

> Object enumApiGetShipmentTypes()

Returns a list with all defined shipmenttypes

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.EnumApiApi();
apiInstance.enumApiGetShipmentTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## enumApiGetShippingCarriers

> Object enumApiGetShippingCarriers()

Returns a list with all defined shippingcarriers

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.EnumApiApi();
apiInstance.enumApiGetShippingCarriers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

