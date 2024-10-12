# MagentoB2B.ReturnsIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rmaCommentManagementV1AddCommentPost**](ReturnsIdCommentsApi.md#rmaCommentManagementV1AddCommentPost) | **POST** /V1/returns/{id}/comments | returns/{id}/comments
[**rmaCommentManagementV1CommentsListGet**](ReturnsIdCommentsApi.md#rmaCommentManagementV1CommentsListGet) | **GET** /V1/returns/{id}/comments | returns/{id}/comments



## rmaCommentManagementV1AddCommentPost

> Boolean rmaCommentManagementV1AddCommentPost(id, opts)

returns/{id}/comments

Add comment

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdCommentsApi();
let id = "id_example"; // String | 
let opts = {
  'rmaCommentManagementV1AddCommentPostRequest': new MagentoB2B.RmaCommentManagementV1AddCommentPostRequest() // RmaCommentManagementV1AddCommentPostRequest | 
};
apiInstance.rmaCommentManagementV1AddCommentPost(id, opts, (error, data, response) => {
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
 **rmaCommentManagementV1AddCommentPostRequest** | [**RmaCommentManagementV1AddCommentPostRequest**](RmaCommentManagementV1AddCommentPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## rmaCommentManagementV1CommentsListGet

> RmaDataCommentSearchResultInterface rmaCommentManagementV1CommentsListGet(id)

returns/{id}/comments

Comments list

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ReturnsIdCommentsApi();
let id = 56; // Number | 
apiInstance.rmaCommentManagementV1CommentsListGet(id, (error, data, response) => {
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

### Return type

[**RmaDataCommentSearchResultInterface**](RmaDataCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

