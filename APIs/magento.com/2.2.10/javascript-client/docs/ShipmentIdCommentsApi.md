# MagentoB2B.ShipmentIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesShipmentCommentRepositoryV1SavePost**](ShipmentIdCommentsApi.md#salesShipmentCommentRepositoryV1SavePost) | **POST** /V1/shipment/{id}/comments | shipment/{id}/comments
[**salesShipmentManagementV1GetCommentsListGet**](ShipmentIdCommentsApi.md#salesShipmentManagementV1GetCommentsListGet) | **GET** /V1/shipment/{id}/comments | shipment/{id}/comments



## salesShipmentCommentRepositoryV1SavePost

> SalesDataShipmentCommentInterface salesShipmentCommentRepositoryV1SavePost(id, opts)

shipment/{id}/comments

Performs persist operations for a specified shipment comment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentIdCommentsApi();
let id = "id_example"; // String | 
let opts = {
  'salesShipmentCommentRepositoryV1SavePostRequest': new MagentoB2B.SalesShipmentCommentRepositoryV1SavePostRequest() // SalesShipmentCommentRepositoryV1SavePostRequest | 
};
apiInstance.salesShipmentCommentRepositoryV1SavePost(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **salesShipmentCommentRepositoryV1SavePostRequest** | [**SalesShipmentCommentRepositoryV1SavePostRequest**](SalesShipmentCommentRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataShipmentCommentInterface**](SalesDataShipmentCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## salesShipmentManagementV1GetCommentsListGet

> SalesDataShipmentCommentSearchResultInterface salesShipmentManagementV1GetCommentsListGet(id)

shipment/{id}/comments

Lists comments for a specified shipment.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ShipmentIdCommentsApi();
let id = 56; // Number | The shipment ID.
apiInstance.salesShipmentManagementV1GetCommentsListGet(id, (error, data, response) => {
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
 **id** | **Number**| The shipment ID. | 

### Return type

[**SalesDataShipmentCommentSearchResultInterface**](SalesDataShipmentCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

