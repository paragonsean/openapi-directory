# BrandLoversMarketplaceApiV1.ProductApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productPost**](ProductApi.md#productPost) | **POST** /product | Create a new product to the marketplace
[**productSkuSellerIdGet**](ProductApi.md#productSkuSellerIdGet) | **GET** /product/{skuSellerId} | Returns details of a single product using the seller &#x60;skuSellerId&#x60;
[**productSkuSellerIdPricesPut**](ProductApi.md#productSkuSellerIdPricesPut) | **PUT** /product/{skuSellerId}/prices | Allows seller to update prices of a single SKU
[**productSkuSellerIdStatusPut**](ProductApi.md#productSkuSellerIdStatusPut) | **PUT** /product/{skuSellerId}/status | Enable/disable a single product in the Marketplace
[**productSkuSellerIdStockPut**](ProductApi.md#productSkuSellerIdStockPut) | **PUT** /product/{skuSellerId}/stock | Update a single product stock



## productPost

> productPost(authorization, product)

Create a new product to the marketplace

Use this enpoint to create a single new product to the Marketplace. This enpoint expects a json document with one product. If you whant to upload multiple products in a single API call use POST /products method. The server will load each product as an individual item that can be manipulated using your own &#x60;skuSellerId&#x60;. This system is idenpontent, this means that once a &#x60;skuSellerId&#x60; is created it cannot be re-created using this tool. In order to update, edit a product use the PUT method with the correct reference to your &#x60;skuSellerId&#x60;

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let product = new BrandLoversMarketplaceApiV1.Product(); // Product | New Produt that will be create
apiInstance.productPost(authorization, product, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **product** | [**Product**](Product.md)| New Produt that will be create | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productSkuSellerIdGet

> GetProduct productSkuSellerIdGet(authorization, skuSellerId)

Returns details of a single product using the seller &#x60;skuSellerId&#x60;

Returns detailed information of a single product with the seller &#x60;skuSellerId&#x60;. This service will return a json document with product detail, status, price, invetory among other infomarion availble in the Brand Lovers marketplace

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';
let defaultClient = BrandLoversMarketplaceApiV1.ApiClient.instance;
// Configure API key authorization: authorization
let authorization = defaultClient.authentications['authorization'];
authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//authorization.apiKeyPrefix = 'Token';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let skuSellerId = "skuSellerId_example"; // String | SKU ID do Lojista.
apiInstance.productSkuSellerIdGet(authorization, skuSellerId, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **skuSellerId** | **String**| SKU ID do Lojista. | 

### Return type

[**GetProduct**](GetProduct.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSkuSellerIdPricesPut

> productSkuSellerIdPricesPut(authorization, skuSellerId, body)

Allows seller to update prices of a single SKU

Allows seller to set the SKU prices (MSRP and/or offer price). All prices must be informed in cents. No commas or periods are accepeted. For example one dollar should be informed as 100. Same as $1,2345.67 must be informed solely as 1234567

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let skuSellerId = "skuSellerId_example"; // String | Product SKU
let body = new BrandLoversMarketplaceApiV1.ProductPrice(); // ProductPrice | JSON document with the SKU price
apiInstance.productSkuSellerIdPricesPut(authorization, skuSellerId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **skuSellerId** | **String**| Product SKU | 
 **body** | [**ProductPrice**](ProductPrice.md)| JSON document with the SKU price | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productSkuSellerIdStatusPut

> productSkuSellerIdStatusPut(authorization, skuSellerId, body)

Enable/disable a single product in the Marketplace

Update product status in the Marketplace. Set to &#x60;true&#x60; to enable, &#x60;false&#x60; to disable sale.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let skuSellerId = "skuSellerId_example"; // String | Unique Product Id (SKU) in the seller system
let body = new BrandLoversMarketplaceApiV1.SellerItemStatus(); // SellerItemStatus | Seller SKU that will be enabled or disabled
apiInstance.productSkuSellerIdStatusPut(authorization, skuSellerId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **skuSellerId** | **String**| Unique Product Id (SKU) in the seller system | 
 **body** | [**SellerItemStatus**](SellerItemStatus.md)| Seller SKU that will be enabled or disabled | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productSkuSellerIdStockPut

> productSkuSellerIdStockPut(authorization, skuSellerId, body)

Update a single product stock

Update a single product inventory information. Products with zero stock will not be eligible for sale.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let skuSellerId = "skuSellerId_example"; // String | Unique Product Id (SKU) in the seller system that will be updated
let body = new BrandLoversMarketplaceApiV1.Stock(); // Stock | New product inventory information
apiInstance.productSkuSellerIdStockPut(authorization, skuSellerId, body, (error, data, response) => {
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
 **authorization** | **String**| Authorization token. The Authorization token can be found in your Admin console. | 
 **skuSellerId** | **String**| Unique Product Id (SKU) in the seller system that will be updated | 
 **body** | [**Stock**](Stock.md)| New product inventory information | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

