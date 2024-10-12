# ApiV100.OrderApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orderApiAll**](OrderApi.md#orderApiAll) | **GET** /api/order/all | Return all orders for the account
[**orderApiChangeShippingDetails**](OrderApi.md#orderApiChangeShippingDetails) | **POST** /api/order/changeshippingdetails | Change order shipping details
[**orderApiChangeStatus**](OrderApi.md#orderApiChangeStatus) | **POST** /api/order/changestatus | Change order status
[**orderApiDelete**](OrderApi.md#orderApiDelete) | **POST** /api/order/delete | Delete an existing order
[**orderApiDetails**](OrderApi.md#orderApiDetails) | **GET** /api/order/details | Return order details
[**orderApiNew**](OrderApi.md#orderApiNew) | **POST** /api/order/new | Create an order



## orderApiAll

> ListResultOrderDetailsApiModel orderApiAll(xAuthKey, xAuthSecret, opts)

Return all orders for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.OrderApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'queryOptionsPage': 56, // Number | 
  'queryOptionsPageSize': 56 // Number | 
};
apiInstance.orderApiAll(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **queryOptionsPage** | **Number**|  | [optional] 
 **queryOptionsPageSize** | **Number**|  | [optional] 

### Return type

[**ListResultOrderDetailsApiModel**](ListResultOrderDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## orderApiChangeShippingDetails

> orderApiChangeShippingDetails(orderId, xAuthKey, xAuthSecret, orderShippingDetailsApiModel)

Change order shipping details

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.OrderApi();
let orderId = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let orderShippingDetailsApiModel = new ApiV100.OrderShippingDetailsApiModel(); // OrderShippingDetailsApiModel | 
apiInstance.orderApiChangeShippingDetails(orderId, xAuthKey, xAuthSecret, orderShippingDetailsApiModel, (error, data, response) => {
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
 **orderId** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **orderShippingDetailsApiModel** | [**OrderShippingDetailsApiModel**](OrderShippingDetailsApiModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: Not defined


## orderApiChangeStatus

> orderApiChangeStatus(xAuthKey, xAuthSecret, changeOrderStatusApiModel)

Change order status

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.OrderApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let changeOrderStatusApiModel = new ApiV100.ChangeOrderStatusApiModel(); // ChangeOrderStatusApiModel | 
apiInstance.orderApiChangeStatus(xAuthKey, xAuthSecret, changeOrderStatusApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **changeOrderStatusApiModel** | [**ChangeOrderStatusApiModel**](ChangeOrderStatusApiModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: Not defined


## orderApiDelete

> Number orderApiDelete(xAuthKey, xAuthSecret, orderDeleteApiModel)

Delete an existing order

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.OrderApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let orderDeleteApiModel = new ApiV100.OrderDeleteApiModel(); // OrderDeleteApiModel | 
apiInstance.orderApiDelete(xAuthKey, xAuthSecret, orderDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **orderDeleteApiModel** | [**OrderDeleteApiModel**](OrderDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## orderApiDetails

> OrderFullDetailsApiModel orderApiDetails(id, xAuthKey, xAuthSecret)

Return order details

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.OrderApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.orderApiDetails(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**OrderFullDetailsApiModel**](OrderFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## orderApiNew

> Number orderApiNew(xAuthKey, xAuthSecret, orderCreateApiModel)

Create an order

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.OrderApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let orderCreateApiModel = new ApiV100.OrderCreateApiModel(); // OrderCreateApiModel | 
apiInstance.orderApiNew(xAuthKey, xAuthSecret, orderCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **orderCreateApiModel** | [**OrderCreateApiModel**](OrderCreateApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml

