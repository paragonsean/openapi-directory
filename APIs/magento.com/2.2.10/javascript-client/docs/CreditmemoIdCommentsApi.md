# MagentoB2B.CreditmemoIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesCreditmemoCommentRepositoryV1SavePost**](CreditmemoIdCommentsApi.md#salesCreditmemoCommentRepositoryV1SavePost) | **POST** /V1/creditmemo/{id}/comments | creditmemo/{id}/comments
[**salesCreditmemoManagementV1GetCommentsListGet**](CreditmemoIdCommentsApi.md#salesCreditmemoManagementV1GetCommentsListGet) | **GET** /V1/creditmemo/{id}/comments | creditmemo/{id}/comments



## salesCreditmemoCommentRepositoryV1SavePost

> SalesDataCreditmemoCommentInterface salesCreditmemoCommentRepositoryV1SavePost(id, opts)

creditmemo/{id}/comments

Performs persist operations for a specified entity.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoIdCommentsApi();
let id = "id_example"; // String | 
let opts = {
  'salesCreditmemoCommentRepositoryV1SavePostRequest': new MagentoB2B.SalesCreditmemoCommentRepositoryV1SavePostRequest() // SalesCreditmemoCommentRepositoryV1SavePostRequest | 
};
apiInstance.salesCreditmemoCommentRepositoryV1SavePost(id, opts, (error, data, response) => {
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
 **salesCreditmemoCommentRepositoryV1SavePostRequest** | [**SalesCreditmemoCommentRepositoryV1SavePostRequest**](SalesCreditmemoCommentRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesDataCreditmemoCommentInterface**](SalesDataCreditmemoCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## salesCreditmemoManagementV1GetCommentsListGet

> SalesDataCreditmemoCommentSearchResultInterface salesCreditmemoManagementV1GetCommentsListGet(id)

creditmemo/{id}/comments

Lists comments for a specified credit memo.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CreditmemoIdCommentsApi();
let id = 56; // Number | The credit memo ID.
apiInstance.salesCreditmemoManagementV1GetCommentsListGet(id, (error, data, response) => {
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
 **id** | **Number**| The credit memo ID. | 

### Return type

[**SalesDataCreditmemoCommentSearchResultInterface**](SalesDataCreditmemoCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

