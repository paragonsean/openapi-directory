# MagentoB2B.RequisitionListsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requisitionListRequisitionListRepositoryV1SavePost**](RequisitionListsApi.md#requisitionListRequisitionListRepositoryV1SavePost) | **POST** /V1/requisition_lists | requisition_lists



## requisitionListRequisitionListRepositoryV1SavePost

> RequisitionListDataRequisitionListInterface requisitionListRequisitionListRepositoryV1SavePost(opts)

requisition_lists

Save Requisition List

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.RequisitionListsApi();
let opts = {
  'requisitionListRequisitionListRepositoryV1SavePostRequest': new MagentoB2B.RequisitionListRequisitionListRepositoryV1SavePostRequest() // RequisitionListRequisitionListRepositoryV1SavePostRequest | 
};
apiInstance.requisitionListRequisitionListRepositoryV1SavePost(opts, (error, data, response) => {
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
 **requisitionListRequisitionListRepositoryV1SavePostRequest** | [**RequisitionListRequisitionListRepositoryV1SavePostRequest**](RequisitionListRequisitionListRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**RequisitionListDataRequisitionListInterface**](RequisitionListDataRequisitionListInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

