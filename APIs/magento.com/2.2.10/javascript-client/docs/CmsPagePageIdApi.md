# MagentoB2B.CmsPagePageIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cmsPageRepositoryV1DeleteByIdDelete**](CmsPagePageIdApi.md#cmsPageRepositoryV1DeleteByIdDelete) | **DELETE** /V1/cmsPage/{pageId} | cmsPage/{pageId}
[**cmsPageRepositoryV1GetByIdGet**](CmsPagePageIdApi.md#cmsPageRepositoryV1GetByIdGet) | **GET** /V1/cmsPage/{pageId} | cmsPage/{pageId}



## cmsPageRepositoryV1DeleteByIdDelete

> Boolean cmsPageRepositoryV1DeleteByIdDelete(pageId)

cmsPage/{pageId}

Delete page by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsPagePageIdApi();
let pageId = 56; // Number | 
apiInstance.cmsPageRepositoryV1DeleteByIdDelete(pageId, (error, data, response) => {
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
 **pageId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## cmsPageRepositoryV1GetByIdGet

> CmsDataPageInterface cmsPageRepositoryV1GetByIdGet(pageId)

cmsPage/{pageId}

Retrieve page.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CmsPagePageIdApi();
let pageId = 56; // Number | 
apiInstance.cmsPageRepositoryV1GetByIdGet(pageId, (error, data, response) => {
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
 **pageId** | **Number**|  | 

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

