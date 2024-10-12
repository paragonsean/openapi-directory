# BeezUpMerchantApi.ChannelCatalogsProductsApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportChannelCatalogProductInfoList**](ChannelCatalogsProductsApi.md#exportChannelCatalogProductInfoList) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products/export | Export channel catalog product information list
[**getChannelCatalogProductByChannelCatalog**](ChannelCatalogsProductsApi.md#getChannelCatalogProductByChannelCatalog) | **POST** /v2/user/channelCatalogs/products | Get channel catalog products related to these channel catalogs
[**getChannelCatalogProductInfo**](ChannelCatalogsProductsApi.md#getChannelCatalogProductInfo) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId} | Get channel catalog product information
[**getChannelCatalogProductInfoList**](ChannelCatalogsProductsApi.md#getChannelCatalogProductInfoList) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products | Get channel catalog product information list
[**getChannelCatalogProductsCounters**](ChannelCatalogsProductsApi.md#getChannelCatalogProductsCounters) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/products/counters | Get channel catalog products&#39; counters



## exportChannelCatalogProductInfoList

> BeezUPCommonLink3 exportChannelCatalogProductInfoList(channelCatalogId, format, getChannelCatalogProductInfoListRequest)

Export channel catalog product information list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let format = "format_example"; // String | The file type of the exportation
let getChannelCatalogProductInfoListRequest = new BeezUpMerchantApi.GetChannelCatalogProductInfoListRequest(); // GetChannelCatalogProductInfoListRequest | The channel catalog product list filter
apiInstance.exportChannelCatalogProductInfoList(channelCatalogId, format, getChannelCatalogProductInfoListRequest, (error, data, response) => {
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
 **channelCatalogId** | **String**| The channel catalog identifier | 
 **format** | **String**| The file type of the exportation | 
 **getChannelCatalogProductInfoListRequest** | [**GetChannelCatalogProductInfoListRequest**](GetChannelCatalogProductInfoListRequest.md)| The channel catalog product list filter | 

### Return type

[**BeezUPCommonLink3**](BeezUPCommonLink3.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannelCatalogProductByChannelCatalog

> ChannelCatalogProductByChannelCatalogResponse getChannelCatalogProductByChannelCatalog(channelCatalogProductByChannelCatalogRequest)

Get channel catalog products related to these channel catalogs

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsApi();
let channelCatalogProductByChannelCatalogRequest = new BeezUpMerchantApi.ChannelCatalogProductByChannelCatalogRequest(); // ChannelCatalogProductByChannelCatalogRequest | 
apiInstance.getChannelCatalogProductByChannelCatalog(channelCatalogProductByChannelCatalogRequest, (error, data, response) => {
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
 **channelCatalogProductByChannelCatalogRequest** | [**ChannelCatalogProductByChannelCatalogRequest**](ChannelCatalogProductByChannelCatalogRequest.md)|  | 

### Return type

[**ChannelCatalogProductByChannelCatalogResponse**](ChannelCatalogProductByChannelCatalogResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannelCatalogProductInfo

> ChannelCatalogProductInfo getChannelCatalogProductInfo(channelCatalogId, productId)

Get channel catalog product information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
apiInstance.getChannelCatalogProductInfo(channelCatalogId, productId, (error, data, response) => {
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
 **channelCatalogId** | **String**| The channel catalog identifier | 
 **productId** | **String**| The product identifier | 

### Return type

[**ChannelCatalogProductInfo**](ChannelCatalogProductInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogProductInfoList

> ChannelCatalogProductInfoList getChannelCatalogProductInfoList(channelCatalogId, getChannelCatalogProductInfoListRequest)

Get channel catalog product information list

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
let getChannelCatalogProductInfoListRequest = new BeezUpMerchantApi.GetChannelCatalogProductInfoListRequest(); // GetChannelCatalogProductInfoListRequest | The channel catalog product list filter
apiInstance.getChannelCatalogProductInfoList(channelCatalogId, getChannelCatalogProductInfoListRequest, (error, data, response) => {
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
 **channelCatalogId** | **String**| The channel catalog identifier | 
 **getChannelCatalogProductInfoListRequest** | [**GetChannelCatalogProductInfoListRequest**](GetChannelCatalogProductInfoListRequest.md)| The channel catalog product list filter | 

### Return type

[**ChannelCatalogProductInfoList**](ChannelCatalogProductInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChannelCatalogProductsCounters

> ChannelCatalogProductsCounters getChannelCatalogProductsCounters(channelCatalogId)

Get channel catalog products&#39; counters

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsProductsApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.getChannelCatalogProductsCounters(channelCatalogId, (error, data, response) => {
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
 **channelCatalogId** | **String**| The channel catalog identifier | 

### Return type

[**ChannelCatalogProductsCounters**](ChannelCatalogProductsCounters.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

