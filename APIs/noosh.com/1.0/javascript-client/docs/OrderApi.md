# NooshApiApplication.OrderApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBuyOrder**](OrderApi.md#getBuyOrder) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders/{order_id} | Get a specific buy order
[**getBuyOrderList**](OrderApi.md#getBuyOrderList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders | List the buy orders
[**getBuyOrderListOfWorkgroup**](OrderApi.md#getBuyOrderListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/buyOrders | List the buy orders of workgroup
[**getBuyOrderOfWorkgroup**](OrderApi.md#getBuyOrderOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/buyOrders/{order_id} | Get a specific buy order of workgroup
[**getOrder**](OrderApi.md#getOrder) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/orders/{order_id} | Get a specific buy/sell order
[**getSellOrder**](OrderApi.md#getSellOrder) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders/{order_id} | Get a specific sell order
[**getSellOrderList**](OrderApi.md#getSellOrderList) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders | List the sell orders
[**getSellOrderListOfWorkgroup**](OrderApi.md#getSellOrderListOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/sellOrders | List the sell orders of workgrop
[**getSellOrderOfWorkgroup**](OrderApi.md#getSellOrderOfWorkgroup) | **GET** /v1/workgroups/{workgroup_id}/sellOrders/{order_id} | Get a specific sell order
[**postBuyOrder**](OrderApi.md#postBuyOrder) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders | Create a quick buy order
[**putBuyOrder**](OrderApi.md#putBuyOrder) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/buyOrders/{order_id} | Update a specific buy order
[**putSellOrder**](OrderApi.md#putSellOrder) | **PUT** /v1/workgroups/{workgroup_id}/projects/{project_id}/sellOrders/{order_id} | Update / Accept or Reject a specific sell order



## getBuyOrder

> OrderDetailVO getBuyOrder(workgroupId, projectId, orderId)

Get a specific buy order

Get a specific buy order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let orderId = "orderId_example"; // String | 
apiInstance.getBuyOrder(workgroupId, projectId, orderId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderId** | **String**|  | 

### Return type

[**OrderDetailVO**](OrderDetailVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getBuyOrderList

> OrderListVO getBuyOrderList(workgroupId, projectId)

List the buy orders

List the buy orders

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getBuyOrderList(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**OrderListVO**](OrderListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getBuyOrderListOfWorkgroup

> OrderWorkgroupLevelListVO getBuyOrderListOfWorkgroup(workgroupId)

List the buy orders of workgroup

List the buy orders of workgroup

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getBuyOrderListOfWorkgroup(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**OrderWorkgroupLevelListVO**](OrderWorkgroupLevelListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getBuyOrderOfWorkgroup

> OrderExpandWorkgroupLevelVO getBuyOrderOfWorkgroup(workgroupId, orderId)

Get a specific buy order of workgroup

Get a specific buy order of workgroup

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let orderId = "orderId_example"; // String | 
apiInstance.getBuyOrderOfWorkgroup(workgroupId, orderId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **orderId** | **String**|  | 

### Return type

[**OrderExpandWorkgroupLevelVO**](OrderExpandWorkgroupLevelVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getOrder

> OrderDetailWithIndicatorVO getOrder(workgroupId, projectId, orderId)

Get a specific buy/sell order

Get a specific buy/sell order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let orderId = "orderId_example"; // String | 
apiInstance.getOrder(workgroupId, projectId, orderId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderId** | **String**|  | 

### Return type

[**OrderDetailWithIndicatorVO**](OrderDetailWithIndicatorVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSellOrder

> OrderDetailVO getSellOrder(workgroupId, projectId, orderId)

Get a specific sell order

Get a specific sell order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let orderId = "orderId_example"; // String | 
apiInstance.getSellOrder(workgroupId, projectId, orderId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderId** | **String**|  | 

### Return type

[**OrderDetailVO**](OrderDetailVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSellOrderList

> OrderListVO getSellOrderList(workgroupId, projectId)

List the sell orders

List the sell orders

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getSellOrderList(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**OrderListVO**](OrderListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSellOrderListOfWorkgroup

> OrderWorkgroupLevelListVO getSellOrderListOfWorkgroup(workgroupId)

List the sell orders of workgrop

List the sell orders of workgrop

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getSellOrderListOfWorkgroup(workgroupId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 

### Return type

[**OrderWorkgroupLevelListVO**](OrderWorkgroupLevelListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getSellOrderOfWorkgroup

> OrderExpandWorkgroupLevelVO getSellOrderOfWorkgroup(workgroupId, orderId)

Get a specific sell order

Get a specific sell order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let orderId = "orderId_example"; // String | 
apiInstance.getSellOrderOfWorkgroup(workgroupId, orderId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **orderId** | **String**|  | 

### Return type

[**OrderExpandWorkgroupLevelVO**](OrderExpandWorkgroupLevelVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postBuyOrder

> OrderPO postBuyOrder(workgroupId, projectId, opts)

Create a quick buy order

Create a quick buy order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'orderPO': new NooshApiApplication.OrderPO() // OrderPO | 
};
apiInstance.postBuyOrder(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderPO** | [**OrderPO**](OrderPO.md)|  | [optional] 

### Return type

[**OrderPO**](OrderPO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putBuyOrder

> OrderVO putBuyOrder(workgroupId, projectId, orderId, opts)

Update a specific buy order

Update a specific buy order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let orderId = "orderId_example"; // String | 
let opts = {
  'orderUpdPersistVO': new NooshApiApplication.OrderUpdPersistVO() // OrderUpdPersistVO | 
};
apiInstance.putBuyOrder(workgroupId, projectId, orderId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderId** | **String**|  | 
 **orderUpdPersistVO** | [**OrderUpdPersistVO**](OrderUpdPersistVO.md)|  | [optional] 

### Return type

[**OrderVO**](OrderVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## putSellOrder

> OrderVO putSellOrder(workgroupId, projectId, orderId, opts)

Update / Accept or Reject a specific sell order

Update / Accept or Reject a specific sell order

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.OrderApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let orderId = "orderId_example"; // String | 
let opts = {
  'orderUpdPersistVO': new NooshApiApplication.OrderUpdPersistVO() // OrderUpdPersistVO | 
};
apiInstance.putSellOrder(workgroupId, projectId, orderId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **orderId** | **String**|  | 
 **orderUpdPersistVO** | [**OrderUpdPersistVO**](OrderUpdPersistVO.md)|  | [optional] 

### Return type

[**OrderVO**](OrderVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

