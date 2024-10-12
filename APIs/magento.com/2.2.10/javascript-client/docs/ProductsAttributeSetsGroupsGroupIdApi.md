# MagentoB2B.ProductsAttributeSetsGroupsGroupIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogProductAttributeGroupRepositoryV1DeleteByIdDelete**](ProductsAttributeSetsGroupsGroupIdApi.md#catalogProductAttributeGroupRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/attribute-sets/groups/{groupId} | products/attribute-sets/groups/{groupId}



## catalogProductAttributeGroupRepositoryV1DeleteByIdDelete

> Boolean catalogProductAttributeGroupRepositoryV1DeleteByIdDelete(groupId)

products/attribute-sets/groups/{groupId}

Remove attribute group by id

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsAttributeSetsGroupsGroupIdApi();
let groupId = 56; // Number | 
apiInstance.catalogProductAttributeGroupRepositoryV1DeleteByIdDelete(groupId, (error, data, response) => {
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
 **groupId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

