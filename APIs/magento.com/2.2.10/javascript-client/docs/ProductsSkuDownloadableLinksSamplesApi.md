# MagentoB2B.ProductsSkuDownloadableLinksSamplesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadableSampleRepositoryV1GetListGet**](ProductsSkuDownloadableLinksSamplesApi.md#downloadableSampleRepositoryV1GetListGet) | **GET** /V1/products/{sku}/downloadable-links/samples | products/{sku}/downloadable-links/samples
[**downloadableSampleRepositoryV1SavePost**](ProductsSkuDownloadableLinksSamplesApi.md#downloadableSampleRepositoryV1SavePost) | **POST** /V1/products/{sku}/downloadable-links/samples | products/{sku}/downloadable-links/samples



## downloadableSampleRepositoryV1GetListGet

> [DownloadableDataSampleInterface] downloadableSampleRepositoryV1GetListGet(sku)

products/{sku}/downloadable-links/samples

List of samples for downloadable product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuDownloadableLinksSamplesApi();
let sku = "sku_example"; // String | 
apiInstance.downloadableSampleRepositoryV1GetListGet(sku, (error, data, response) => {
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

[**[DownloadableDataSampleInterface]**](DownloadableDataSampleInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## downloadableSampleRepositoryV1SavePost

> Number downloadableSampleRepositoryV1SavePost(sku, opts)

products/{sku}/downloadable-links/samples

Update downloadable sample of the given product

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.ProductsSkuDownloadableLinksSamplesApi();
let sku = "sku_example"; // String | 
let opts = {
  'downloadableSampleRepositoryV1SavePostRequest': new MagentoB2B.DownloadableSampleRepositoryV1SavePostRequest() // DownloadableSampleRepositoryV1SavePostRequest | 
};
apiInstance.downloadableSampleRepositoryV1SavePost(sku, opts, (error, data, response) => {
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
 **downloadableSampleRepositoryV1SavePostRequest** | [**DownloadableSampleRepositoryV1SavePostRequest**](DownloadableSampleRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

