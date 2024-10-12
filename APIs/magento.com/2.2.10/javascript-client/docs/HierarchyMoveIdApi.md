# MagentoB2B.HierarchyMoveIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyCompanyHierarchyV1MoveNodePut**](HierarchyMoveIdApi.md#companyCompanyHierarchyV1MoveNodePut) | **PUT** /V1/hierarchy/move/{id} | hierarchy/move/{id}



## companyCompanyHierarchyV1MoveNodePut

> ErrorResponse companyCompanyHierarchyV1MoveNodePut(id, opts)

hierarchy/move/{id}

Moves teams and users within the company structure.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.HierarchyMoveIdApi();
let id = 56; // Number | 
let opts = {
  'companyCompanyHierarchyV1MoveNodePutRequest': new MagentoB2B.CompanyCompanyHierarchyV1MoveNodePutRequest() // CompanyCompanyHierarchyV1MoveNodePutRequest | 
};
apiInstance.companyCompanyHierarchyV1MoveNodePut(id, opts, (error, data, response) => {
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
 **companyCompanyHierarchyV1MoveNodePutRequest** | [**CompanyCompanyHierarchyV1MoveNodePutRequest**](CompanyCompanyHierarchyV1MoveNodePutRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

