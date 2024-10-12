# BeezUpMerchantApi.ChannelCatalogsGlobalApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addChannelCatalog**](ChannelCatalogsGlobalApi.md#addChannelCatalog) | **POST** /v2/user/channelCatalogs/ | Add a new channel catalog
[**deleteChannelCatalog**](ChannelCatalogsGlobalApi.md#deleteChannelCatalog) | **DELETE** /v2/user/channelCatalogs/{channelCatalogId} | Delete the channel catalog
[**getChannelCatalog**](ChannelCatalogsGlobalApi.md#getChannelCatalog) | **GET** /v2/user/channelCatalogs/{channelCatalogId} | Get the channel catalog information
[**getChannelCatalogFilterOperators**](ChannelCatalogsGlobalApi.md#getChannelCatalogFilterOperators) | **GET** /v2/user/channelCatalogs/filterOperators | Get channel catalog filter operators
[**getChannelCatalogs**](ChannelCatalogsGlobalApi.md#getChannelCatalogs) | **GET** /v2/user/channelCatalogs/ | List all your current channel catalogs



## addChannelCatalog

> LinksGetChannelCatalogLink addChannelCatalog(addChannelCatalogRequest)

Add a new channel catalog

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsGlobalApi();
let addChannelCatalogRequest = new BeezUpMerchantApi.AddChannelCatalogRequest(); // AddChannelCatalogRequest | 
apiInstance.addChannelCatalog(addChannelCatalogRequest, (error, data, response) => {
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
 **addChannelCatalogRequest** | [**AddChannelCatalogRequest**](AddChannelCatalogRequest.md)|  | 

### Return type

[**LinksGetChannelCatalogLink**](LinksGetChannelCatalogLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteChannelCatalog

> deleteChannelCatalog(channelCatalogId)

Delete the channel catalog

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsGlobalApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.deleteChannelCatalog(channelCatalogId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelCatalogId** | **String**| The channel catalog identifier | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalog

> ChannelCatalog getChannelCatalog(channelCatalogId)

Get the channel catalog information

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsGlobalApi();
let channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
apiInstance.getChannelCatalog(channelCatalogId, (error, data, response) => {
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

[**ChannelCatalog**](ChannelCatalog.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogFilterOperators

> [FilterOperator] getChannelCatalogFilterOperators()

Get channel catalog filter operators

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsGlobalApi();
apiInstance.getChannelCatalogFilterOperators((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[FilterOperator]**](FilterOperator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelCatalogs

> ChannelCatalogList getChannelCatalogs(opts)

List all your current channel catalogs

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.ChannelCatalogsGlobalApi();
let opts = {
  'storeId': "04730364-9826-4ff3-92e4-51fccd02bf10" // String | The store identifier
};
apiInstance.getChannelCatalogs(opts, (error, data, response) => {
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
 **storeId** | **String**| The store identifier | [optional] 

### Return type

[**ChannelCatalogList**](ChannelCatalogList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

