# MagentoB2B.CmsBlockBlockIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmsBlockRepositoryV1DeleteByIdDelete**](CmsBlockBlockIdApi.md#cmsBlockRepositoryV1DeleteByIdDelete) | **DELETE** /V1/cmsBlock/{blockId} | cmsBlock/{blockId}
[**cmsBlockRepositoryV1GetByIdGet**](CmsBlockBlockIdApi.md#cmsBlockRepositoryV1GetByIdGet) | **GET** /V1/cmsBlock/{blockId} | cmsBlock/{blockId}



## cmsBlockRepositoryV1DeleteByIdDelete

> Boolean cmsBlockRepositoryV1DeleteByIdDelete(blockId)

cmsBlock/{blockId}

Delete block by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsBlockBlockIdApi();
let blockId = 56; // Number | 
apiInstance.cmsBlockRepositoryV1DeleteByIdDelete(blockId, (error, data, response) => {
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
 **blockId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## cmsBlockRepositoryV1GetByIdGet

> CmsDataBlockInterface cmsBlockRepositoryV1GetByIdGet(blockId)

cmsBlock/{blockId}

Retrieve block.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsBlockBlockIdApi();
let blockId = 56; // Number | 
apiInstance.cmsBlockRepositoryV1GetByIdGet(blockId, (error, data, response) => {
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
 **blockId** | **Number**|  | 

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

