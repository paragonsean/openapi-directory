# MagentoB2B.EavAttributeSetsAttributeSetIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eavAttributeSetRepositoryV1DeleteByIdDelete**](EavAttributeSetsAttributeSetIdApi.md#eavAttributeSetRepositoryV1DeleteByIdDelete) | **DELETE** /V1/eav/attribute-sets/{attributeSetId} | eav/attribute-sets/{attributeSetId}
[**eavAttributeSetRepositoryV1GetGet**](EavAttributeSetsAttributeSetIdApi.md#eavAttributeSetRepositoryV1GetGet) | **GET** /V1/eav/attribute-sets/{attributeSetId} | eav/attribute-sets/{attributeSetId}
[**eavAttributeSetRepositoryV1SavePut**](EavAttributeSetsAttributeSetIdApi.md#eavAttributeSetRepositoryV1SavePut) | **PUT** /V1/eav/attribute-sets/{attributeSetId} | eav/attribute-sets/{attributeSetId}



## eavAttributeSetRepositoryV1DeleteByIdDelete

> Boolean eavAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId)

eav/attribute-sets/{attributeSetId}

Remove attribute set by given ID

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.EavAttributeSetsAttributeSetIdApi();
let attributeSetId = 56; // Number | 
apiInstance.eavAttributeSetRepositoryV1DeleteByIdDelete(attributeSetId, (error, data, response) => {
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
 **attributeSetId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## eavAttributeSetRepositoryV1GetGet

> EavDataAttributeSetInterface eavAttributeSetRepositoryV1GetGet(attributeSetId)

eav/attribute-sets/{attributeSetId}

Retrieve attribute set information based on given ID

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.EavAttributeSetsAttributeSetIdApi();
let attributeSetId = 56; // Number | 
apiInstance.eavAttributeSetRepositoryV1GetGet(attributeSetId, (error, data, response) => {
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
 **attributeSetId** | **Number**|  | 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## eavAttributeSetRepositoryV1SavePut

> EavDataAttributeSetInterface eavAttributeSetRepositoryV1SavePut(attributeSetId, opts)

eav/attribute-sets/{attributeSetId}

Save attribute set data

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.EavAttributeSetsAttributeSetIdApi();
let attributeSetId = "attributeSetId_example"; // String | 
let opts = {
  'eavAttributeSetRepositoryV1SavePutRequest': new MagentoB2B.EavAttributeSetRepositoryV1SavePutRequest() // EavAttributeSetRepositoryV1SavePutRequest | 
};
apiInstance.eavAttributeSetRepositoryV1SavePut(attributeSetId, opts, (error, data, response) => {
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
 **attributeSetId** | **String**|  | 
 **eavAttributeSetRepositoryV1SavePutRequest** | [**EavAttributeSetRepositoryV1SavePutRequest**](EavAttributeSetRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

