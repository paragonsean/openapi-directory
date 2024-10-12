# MagentoB2B.SharedCatalogIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogSharedCatalogRepositoryV1SavePut**](SharedCatalogIdApi.md#sharedCatalogSharedCatalogRepositoryV1SavePut) | **PUT** /V1/sharedCatalog/{id} | sharedCatalog/{id}



## sharedCatalogSharedCatalogRepositoryV1SavePut

> Number sharedCatalogSharedCatalogRepositoryV1SavePut(id, opts)

sharedCatalog/{id}

Create or update Shared Catalog service.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogIdApi();
let id = "id_example"; // String | 
let opts = {
  'sharedCatalogSharedCatalogRepositoryV1SavePostRequest': new MagentoB2B.SharedCatalogSharedCatalogRepositoryV1SavePostRequest() // SharedCatalogSharedCatalogRepositoryV1SavePostRequest | 
};
apiInstance.sharedCatalogSharedCatalogRepositoryV1SavePut(id, opts, (error, data, response) => {
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
 **sharedCatalogSharedCatalogRepositoryV1SavePostRequest** | [**SharedCatalogSharedCatalogRepositoryV1SavePostRequest**](SharedCatalogSharedCatalogRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

