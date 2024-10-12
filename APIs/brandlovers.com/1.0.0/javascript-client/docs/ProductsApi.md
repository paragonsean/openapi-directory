# BrandLoversMarketplaceApiV1.ProductsApi

All URIs are relative to *https://api.brandlovers.com/marketplace/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productSkuSellerIdPut**](ProductsApi.md#productSkuSellerIdPut) | **PUT** /product/{skuSellerId} | Update product details
[**productsGet**](ProductsApi.md#productsGet) | **GET** /products | Returns a list of products loaded into BrandLovers Marketplace
[**productsPost**](ProductsApi.md#productsPost) | **POST** /products | Allows new products from the seller to be loaded into the marketplace
[**productsPricesPut**](ProductsApi.md#productsPricesPut) | **PUT** /products/prices | Allows bulk update of product prices.
[**productsStatusGet**](ProductsApi.md#productsStatusGet) | **GET** /products/status | Returns seller products status in the marketplace
[**productsStatusPut**](ProductsApi.md#productsStatusPut) | **PUT** /products/status | Bulk enable/disable products in the marketplace
[**productsStatusSellingGet**](ProductsApi.md#productsStatusSellingGet) | **GET** /products/status/selling | Returns products that are successfully listed for sale.
[**productsStocksPut**](ProductsApi.md#productsStocksPut) | **PUT** /products/stocks | Bulk product stock update



## productSkuSellerIdPut

> productSkuSellerIdPut(authorization, skuSellerId, body)

Update product details

Update a single product information such as name, brand, attribute, dimension, etc. Please note that data from your request will be merged with existing data. This allows you to easliy update only certain fields without the need to re-inform the other unchanged fields. For example in order to update just the field &#x60;title&#x60; simply send just this field with new information, remaining fields will not be changed. In order to erase an item the field must be informed as its default value, for example in order to erase the &#x60;videos&#x60; field must be sent as videos:[]. The &#x60;skuSellerId&#x60; field is always mandatory in the path and in the product json Object.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';
let defaultClient = BrandLoversMarketplaceApiV1.ApiClient.instance;
// Configure API key authorization: authorization
let authorization = defaultClient.authentications['authorization'];
authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//authorization.apiKeyPrefix = 'Token';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let skuSellerId = "skuSellerId_example"; // String | Unique Product Id (SKU) in the seller system that will be updated.
let body = new BrandLoversMarketplaceApiV1.ProductUpdate(); // ProductUpdate | New product information.
apiInstance.productSkuSellerIdPut(authorization, skuSellerId, body, (error, data, response) => {
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
 **skuSellerId** | **String**| Unique Product Id (SKU) in the seller system that will be updated. | 
 **body** | [**ProductUpdate**](ProductUpdate.md)| New product information. | 

### Return type

null (empty response body)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsGet

> GetProductsResponse productsGet(authorization, opts)

Returns a list of products loaded into BrandLovers Marketplace

Get a list of my products loaded into the Marketplace. This dosen&#39;t means that products are eligible for sale, just that they are loaded in the database.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';
let defaultClient = BrandLoversMarketplaceApiV1.ApiClient.instance;
// Configure API key authorization: authorization
let authorization = defaultClient.authentications['authorization'];
authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//authorization.apiKeyPrefix = 'Token';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number of items to retun. Defaults to 100. Max alowed is 200. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.productsGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number of items to retun. Defaults to 100. Max alowed is 200. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetProductsResponse**](GetProductsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsPost

> productsPost(authorization, products)

Allows new products from the seller to be loaded into the marketplace

This enpoint to creates new products in the Marketplace using &#x60;skuSellerId&#x60; as a primary key. This enpoint expects a json document with array of products. The server will load each product as an individual item that can be manipulated using your own &#x60;skuSellerId&#x60;. All requests to This endpoint are idenpontent with respect of the &#x60;skuSellerId&#x60;, this means that once a &#x60;skuSellerId&#x60; is created it cannot be re-created using this tool. In order to update use the PUT method with the correct &#x60;skuSellerId&#x60;. You can also use the POST /product to create a single product per request

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let products = [new BrandLoversMarketplaceApiV1.Product()]; // [Product] | JSON with a list of new products to be updloaded to the platform
apiInstance.productsPost(authorization, products, (error, data, response) => {
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
 **products** | [**[Product]**](Product.md)| JSON with a list of new products to be updloaded to the platform | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsPricesPut

> productsPricesPut(authorization, body)

Allows bulk update of product prices.

Allows bulk update of product prices. This endpoint expects a json document with an array of products with the &#x60;skuSellerId&#x60; and the new price. Server will process each new product update individually and will ackwlodge as much updates as possible, even if a single product update fails. After this request you can query product final status with GET /product/status

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let body = [new BrandLoversMarketplaceApiV1.SellerItemPrices()]; // [SellerItemPrices] | Data for bulk product price update
apiInstance.productsPricesPut(authorization, body, (error, data, response) => {
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
 **body** | [**[SellerItemPrices]**](SellerItemPrices.md)| Data for bulk product price update | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsStatusGet

> GetSellerProductsStatus productsStatusGet(authorization, opts)

Returns seller products status in the marketplace

Returns a list with seller products status. Please note that this endpoint will not return all details of each product, just the skuSellerId and status. Also please note that this endpoint will return 250 products per call. For full details of a given procuct use GET /product/{skuSellerId}

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number of items to return in this query. Defaults to 250. Maximum 1000. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.productsStatusGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number of items to return in this query. Defaults to 250. Maximum 1000. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetSellerProductsStatus**](GetSellerProductsStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsStatusPut

> productsStatusPut(authorization, body)

Bulk enable/disable products in the marketplace

Bulk enable/disable products in the marketplace. This endpoint requires an array of objects with the seller SKU &#x60;skuSellerId&#x60; and boolean value that defines if the product is enabled or not for sale. This endpoint can be used to set a single product or many products.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let body = [new BrandLoversMarketplaceApiV1.ProductStatusUpdate()]; // [ProductStatusUpdate] | List of seller products with new status information
apiInstance.productsStatusPut(authorization, body, (error, data, response) => {
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
 **body** | [**[ProductStatusUpdate]**](ProductStatusUpdate.md)| List of seller products with new status information | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsStatusSellingGet

> GetProductsStatusSelling productsStatusSellingGet(authorization, opts)

Returns products that are successfully listed for sale.

Returns products that are successfully listed for sale.

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let opts = {
  'offset': 56, // Number | Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with `limit` to paginate across the results.
  'limit': 56 // Number | Number or items to return when executing query. Defaults to 10. Use this conjuction with `offset` to paginate across the results.
};
apiInstance.productsStatusSellingGet(authorization, opts, (error, data, response) => {
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
 **offset** | **Number**| Number or items to skip when executing query. List starts at zero. If omitted will default to zero. Use this conjuction with &#x60;limit&#x60; to paginate across the results. | [optional] 
 **limit** | **Number**| Number or items to return when executing query. Defaults to 10. Use this conjuction with &#x60;offset&#x60; to paginate across the results. | [optional] 

### Return type

[**GetProductsStatusSelling**](GetProductsStatusSelling.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsStocksPut

> productsStocksPut(authorization, body)

Bulk product stock update

Bulk product stock update. This endpoint expect a array of products &#x60;skuSellerId&#x60; with new inventory data

### Example

```javascript
import BrandLoversMarketplaceApiV1 from 'brand_lovers_marketplace_api_v1';

let apiInstance = new BrandLoversMarketplaceApiV1.ProductsApi();
let authorization = "authorization_example"; // String | Authorization token. The Authorization token can be found in your Admin console.
let body = [new BrandLoversMarketplaceApiV1.ProductStock()]; // [ProductStock] | Array of product SKUs.
apiInstance.productsStocksPut(authorization, body, (error, data, response) => {
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
 **body** | [**[ProductStock]**](ProductStock.md)| Array of product SKUs. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

