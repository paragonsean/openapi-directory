# MagentoB2B.SharedCatalogSharedCatalogIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete**](SharedCatalogSharedCatalogIdApi.md#sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete) | **DELETE** /V1/sharedCatalog/{sharedCatalogId} | sharedCatalog/{sharedCatalogId}
[**sharedCatalogSharedCatalogRepositoryV1GetGet**](SharedCatalogSharedCatalogIdApi.md#sharedCatalogSharedCatalogRepositoryV1GetGet) | **GET** /V1/sharedCatalog/{sharedCatalogId} | sharedCatalog/{sharedCatalogId}



## sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete

> Boolean sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete(sharedCatalogId)

sharedCatalog/{sharedCatalogId}

Delete a shared catalog by ID.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogSharedCatalogIdApi();
let sharedCatalogId = 56; // Number | 
apiInstance.sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete(sharedCatalogId, (error, data, response) => {
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
 **sharedCatalogId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## sharedCatalogSharedCatalogRepositoryV1GetGet

> SharedCatalogDataSharedCatalogInterface sharedCatalogSharedCatalogRepositoryV1GetGet(sharedCatalogId)

sharedCatalog/{sharedCatalogId}

Return the following properties for the selected shared catalog: ID, Store Group ID, Name, Type, Description, Customer Group, Tax Class.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.SharedCatalogSharedCatalogIdApi();
let sharedCatalogId = 56; // Number | 
apiInstance.sharedCatalogSharedCatalogRepositoryV1GetGet(sharedCatalogId, (error, data, response) => {
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
 **sharedCatalogId** | **Number**|  | 

### Return type

[**SharedCatalogDataSharedCatalogInterface**](SharedCatalogDataSharedCatalogInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

