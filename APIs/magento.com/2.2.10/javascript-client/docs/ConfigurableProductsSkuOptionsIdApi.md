# MagentoB2B.ConfigurableProductsSkuOptionsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurableProductOptionRepositoryV1DeleteByIdDelete**](ConfigurableProductsSkuOptionsIdApi.md#configurableProductOptionRepositoryV1DeleteByIdDelete) | **DELETE** /V1/configurable-products/{sku}/options/{id} | configurable-products/{sku}/options/{id}
[**configurableProductOptionRepositoryV1GetGet**](ConfigurableProductsSkuOptionsIdApi.md#configurableProductOptionRepositoryV1GetGet) | **GET** /V1/configurable-products/{sku}/options/{id} | configurable-products/{sku}/options/{id}
[**configurableProductOptionRepositoryV1SavePut**](ConfigurableProductsSkuOptionsIdApi.md#configurableProductOptionRepositoryV1SavePut) | **PUT** /V1/configurable-products/{sku}/options/{id} | configurable-products/{sku}/options/{id}



## configurableProductOptionRepositoryV1DeleteByIdDelete

> Boolean configurableProductOptionRepositoryV1DeleteByIdDelete(sku, id)

configurable-products/{sku}/options/{id}

Remove option from configurable product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuOptionsIdApi();
let sku = "sku_example"; // String | 
let id = 56; // Number | 
apiInstance.configurableProductOptionRepositoryV1DeleteByIdDelete(sku, id, (error, data, response) => {
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
 **sku** | **String**|  | 
 **id** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## configurableProductOptionRepositoryV1GetGet

> ConfigurableProductDataOptionInterface configurableProductOptionRepositoryV1GetGet(sku, id)

configurable-products/{sku}/options/{id}

Get option for configurable product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuOptionsIdApi();
let sku = "sku_example"; // String | 
let id = 56; // Number | 
apiInstance.configurableProductOptionRepositoryV1GetGet(sku, id, (error, data, response) => {
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
 **sku** | **String**|  | 
 **id** | **Number**|  | 

### Return type

[**ConfigurableProductDataOptionInterface**](ConfigurableProductDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## configurableProductOptionRepositoryV1SavePut

> Number configurableProductOptionRepositoryV1SavePut(sku, id, opts)

configurable-products/{sku}/options/{id}

Save option

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ConfigurableProductsSkuOptionsIdApi();
let sku = "sku_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'configurableProductOptionRepositoryV1SavePostRequest': new MagentoB2B.ConfigurableProductOptionRepositoryV1SavePostRequest() // ConfigurableProductOptionRepositoryV1SavePostRequest | 
};
apiInstance.configurableProductOptionRepositoryV1SavePut(sku, id, opts, (error, data, response) => {
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
 **sku** | **String**|  | 
 **id** | **String**|  | 
 **configurableProductOptionRepositoryV1SavePostRequest** | [**ConfigurableProductOptionRepositoryV1SavePostRequest**](ConfigurableProductOptionRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

