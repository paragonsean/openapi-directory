# MagentoB2B.OrdersIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesOrderManagementV1AddCommentPost**](OrdersIdCommentsApi.md#salesOrderManagementV1AddCommentPost) | **POST** /V1/orders/{id}/comments | orders/{id}/comments
[**salesOrderManagementV1GetCommentsListGet**](OrdersIdCommentsApi.md#salesOrderManagementV1GetCommentsListGet) | **GET** /V1/orders/{id}/comments | orders/{id}/comments



## salesOrderManagementV1AddCommentPost

> Boolean salesOrderManagementV1AddCommentPost(id, opts)

orders/{id}/comments

Adds a comment to a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdCommentsApi();
let id = 56; // Number | The order ID.
let opts = {
  'salesOrderManagementV1AddCommentPostRequest': new MagentoB2B.SalesOrderManagementV1AddCommentPostRequest() // SalesOrderManagementV1AddCommentPostRequest | 
};
apiInstance.salesOrderManagementV1AddCommentPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| The order ID. | 
 **salesOrderManagementV1AddCommentPostRequest** | [**SalesOrderManagementV1AddCommentPostRequest**](SalesOrderManagementV1AddCommentPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## salesOrderManagementV1GetCommentsListGet

> SalesDataOrderStatusHistorySearchResultInterface salesOrderManagementV1GetCommentsListGet(id)

orders/{id}/comments

Lists comments for a specified order.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.OrdersIdCommentsApi();
let id = 56; // Number | The order ID.
apiInstance.salesOrderManagementV1GetCommentsListGet(id, (error, data, response) => {
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
 **id** | **Number**| The order ID. | 

### Return type

[**SalesDataOrderStatusHistorySearchResultInterface**](SalesDataOrderStatusHistorySearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

