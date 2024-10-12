# MagentoB2B.ProductsSkuDownloadableLinksApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadableLinkRepositoryV1GetListGet**](ProductsSkuDownloadableLinksApi.md#downloadableLinkRepositoryV1GetListGet) | **GET** /V1/products/{sku}/downloadable-links | products/{sku}/downloadable-links
[**downloadableLinkRepositoryV1SavePost**](ProductsSkuDownloadableLinksApi.md#downloadableLinkRepositoryV1SavePost) | **POST** /V1/products/{sku}/downloadable-links | products/{sku}/downloadable-links



## downloadableLinkRepositoryV1GetListGet

> [DownloadableDataLinkInterface] downloadableLinkRepositoryV1GetListGet(sku)

products/{sku}/downloadable-links

List of links with associated samples

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuDownloadableLinksApi();
let sku = "sku_example"; // String | 
apiInstance.downloadableLinkRepositoryV1GetListGet(sku, (error, data, response) => {
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

### Return type

[**[DownloadableDataLinkInterface]**](DownloadableDataLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## downloadableLinkRepositoryV1SavePost

> Number downloadableLinkRepositoryV1SavePost(sku, opts)

products/{sku}/downloadable-links

Update downloadable link of the given product (link type and its resources cannot be changed)

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuDownloadableLinksApi();
let sku = "sku_example"; // String | 
let opts = {
  'downloadableLinkRepositoryV1SavePostRequest': new MagentoB2B.DownloadableLinkRepositoryV1SavePostRequest() // DownloadableLinkRepositoryV1SavePostRequest | 
};
apiInstance.downloadableLinkRepositoryV1SavePost(sku, opts, (error, data, response) => {
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
 **downloadableLinkRepositoryV1SavePostRequest** | [**DownloadableLinkRepositoryV1SavePostRequest**](DownloadableLinkRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

