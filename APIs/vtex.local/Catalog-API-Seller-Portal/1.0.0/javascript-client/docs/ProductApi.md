# CatalogApiSellerPortal.ProductApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProduct**](ProductApi.md#getProduct) | **GET** /api/catalog-seller-portal/products/{productId} | Get Product by ID
[**getProductDescription**](ProductApi.md#getProductDescription) | **GET** /api/catalog-seller-portal/products/{productId}/description | Get Product Description by Product ID
[**getProductQuery**](ProductApi.md#getProductQuery) | **GET** /api/catalog-seller-portal/products/{param} | Get Product by external ID,  SKU ID, SKU external ID or slug
[**postProduct**](ProductApi.md#postProduct) | **POST** /api/catalog-seller-portal/products | Create Product
[**putProduct**](ProductApi.md#putProduct) | **PUT** /api/catalog-seller-portal/products/{productId} | Update Product
[**putProductDescription**](ProductApi.md#putProductDescription) | **PUT** /api/catalog-seller-portal/products/{productId}/description | Update Product Description by Product ID



## getProduct

> GetProduct200Response getProduct(contentType, accept, productId)

Get Product by ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a product by its ID. The response also has information about the product&#39;s SKUs.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;brandName\&quot;: \&quot;AOC\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;categoryNames\&quot;: [          \&quot;/sandboxintegracao/Acessórios/\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;id\&quot;: \&quot;182907\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;id\&quot;: \&quot;182908\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;transportModal\&quot;: \&quot;123\&quot;,      \&quot;taxCode\&quot;: \&quot;100\&quot;,      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-10-31T16:28:25.578067Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-10-31T17:09:12.639088Z\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApiSellerPortal.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = "189371"; // String | Product unique identifier number.
apiInstance.getProduct(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| Product unique identifier number. | 

### Return type

[**GetProduct200Response**](GetProduct200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductDescription

> GetProductDescription200Response getProductDescription(contentType, accept, productId)

Get Product Description by Product ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves the description of a product given a Product ID.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: \&quot;61\&quot;,      \&quot;description\&quot;: \&quot;Beautifully handmade laptop case/sleeve made in the Nepal Himalaya. It can be slipped inside your backpack or carried alone with space for all your work bits and pieces!\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-10-10T19:18:45.612317Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-10-11T18:12:58.825544Z\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApiSellerPortal.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = "189371"; // String | Product unique identifier number.
apiInstance.getProductDescription(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| Product unique identifier number. | 

### Return type

[**GetProductDescription200Response**](GetProductDescription200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductQuery

> GetProductQuery200Response getProductQuery(contentType, accept, param)

Get Product by external ID,  SKU ID, SKU external ID or slug

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a product by its external ID, SKU ID, SKU external ID or product slug. The response also has information about the product&#39;s SKUs.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;brandName\&quot;: \&quot;AOC\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;categoryNames\&quot;: [          \&quot;/sandboxintegracao/Acessórios/\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;id\&quot;: \&quot;182907\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;id\&quot;: \&quot;182908\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;transportModal\&quot;: \&quot;123\&quot;,      \&quot;taxCode\&quot;: \&quot;100\&quot;,      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-10-31T16:28:25.578067Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-10-31T16:28:25.578067Z\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApiSellerPortal.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let param = "external-id=189371"; // String | This part of the path must follow this format: `{param}={value}`. Replace `{param}` with the name of the parameter used to fetch a product, which can be one of the following: `external-id` (product reference unique identifier number in the store), `sku-id` (SKU unique identifier number), `sku-external-id` (SKU reference unique identifier number in the store) or `slug` (reference of the product in the URL of the store). Replace `{value}` with the value of the selected param. Make sure there is a `=` between them.
apiInstance.getProductQuery(contentType, accept, param, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **param** | **String**| This part of the path must follow this format: &#x60;{param}&#x3D;{value}&#x60;. Replace &#x60;{param}&#x60; with the name of the parameter used to fetch a product, which can be one of the following: &#x60;external-id&#x60; (product reference unique identifier number in the store), &#x60;sku-id&#x60; (SKU unique identifier number), &#x60;sku-external-id&#x60; (SKU reference unique identifier number in the store) or &#x60;slug&#x60; (reference of the product in the URL of the store). Replace &#x60;{value}&#x60; with the value of the selected param. Make sure there is a &#x60;&#x3D;&#x60; between them. | 

### Return type

[**GetProductQuery200Response**](GetProductQuery200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postProduct

> PostProduct200Response postProduct(contentType, accept, opts)

Create Product

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new product and its SKUs.       ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;description\&quot;: \&quot;Shirt number 10 by VTEX.\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;transportModal\&quot;: \&quot;110\&quot;,      \&quot;taxCode\&quot;: \&quot;234\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;brandName\&quot;: \&quot;AOC\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;categoryNames\&quot;: [          \&quot;/Men/Acessories/\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;id\&quot;: \&quot;182907\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;id\&quot;: \&quot;182908\&quot;,              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;,      \&quot;transportModal\&quot;: \&quot;110\&quot;,      \&quot;taxCode\&quot;: \&quot;234\&quot;,      \&quot;createdAt\&quot;: \&quot;2022-11-01T14:15:54.262702Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-11-01T14:15:54.262702Z\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApiSellerPortal.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'postProductRequest': {"attributes":[{"name":"Fabric","value":"Cotton"},{"name":"Gender","value":"Feminine"}],"brandId":"1","categoryIds":["732"],"description":"Shirt number 10 by VTEX.","images":[{"alt":"VTEX","id":"vtex_logo.jpg","url":"https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg"}],"name":"VTEX 10 Shirt","origin":"vtxleo7778","skus":[{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234567","name":"VTEX Shirt Black Size S","specs":[{"name":"Color","value":"Black"},{"name":"Size","value":"S"}],"weight":300},{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234568","name":"VTEX Shirt White Size L","specs":[{"name":"Color","value":"White"},{"name":"Size","value":"L"}],"weight":300}],"slug":"/vtex-shirt","specs":[{"name":"Color","values":["Black","White"]},{"name":"Size","values":["S","M","L"]}],"status":"active","taxCode":"234","transportModal":"110"} // PostProductRequest | 
};
apiInstance.postProduct(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **postProductRequest** | [**PostProductRequest**](PostProductRequest.md)|  | [optional] 

### Return type

[**PostProduct200Response**](PostProduct200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putProduct

> putProduct(contentType, accept, productId, opts)

Update Product

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates an existing product and its SKUs.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;id\&quot;: \&quot;189371\&quot;,      \&quot;status\&quot;: \&quot;active\&quot;,      \&quot;name\&quot;: \&quot;VTEX 10 Shirt\&quot;,      \&quot;description\&quot;: \&quot;Shirt number 10 by VTEX.\&quot;,      \&quot;brandId\&quot;: \&quot;1\&quot;,      \&quot;categoryIds\&quot;: [          \&quot;732\&quot;      ],      \&quot;specs\&quot;: [          {              \&quot;name\&quot;: \&quot;Color\&quot;,              \&quot;values\&quot;: [                  \&quot;Black\&quot;,                  \&quot;White\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;Size\&quot;,              \&quot;values\&quot;: [                  \&quot;S\&quot;,                  \&quot;M\&quot;,                  \&quot;L\&quot;              ]          }      ],      \&quot;attributes\&quot;: [          {              \&quot;name\&quot;: \&quot;Fabric\&quot;,              \&quot;value\&quot;: \&quot;Cotton\&quot;          },          {              \&quot;name\&quot;: \&quot;Gender\&quot;,              \&quot;value\&quot;: \&quot;Feminine\&quot;          }      ],      \&quot;slug\&quot;: \&quot;/vtex-shirt\&quot;,      \&quot;transportModal\&quot;: null,      \&quot;taxCode\&quot;: null,      \&quot;images\&quot;: [          {              \&quot;id\&quot;: \&quot;vtex_logo.jpg\&quot;,              \&quot;url\&quot;: \&quot;https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg\&quot;,              \&quot;alt\&quot;: \&quot;VTEX\&quot;          }      ],      \&quot;skus\&quot;: [          {              \&quot;name\&quot;: \&quot;VTEX Shirt Black Size S\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234567\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;Black\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;S\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          },          {              \&quot;name\&quot;: \&quot;VTEX Shirt White Size L\&quot;,              \&quot;externalId\&quot;: \&quot;1909621862\&quot;,              \&quot;manufacturerCode\&quot;: \&quot;1234568\&quot;,              \&quot;isActive\&quot;: true,              \&quot;weight\&quot;: 300,              \&quot;dimensions\&quot;: {                  \&quot;width\&quot;: 1.5,                  \&quot;height\&quot;: 2.1,                  \&quot;length\&quot;: 1.6              },              \&quot;specs\&quot;: [                  {                      \&quot;name\&quot;: \&quot;Color\&quot;,                      \&quot;value\&quot;: \&quot;White\&quot;                  },                  {                      \&quot;name\&quot;: \&quot;Size\&quot;,                      \&quot;value\&quot;: \&quot;L\&quot;                  }              ],              \&quot;images\&quot;: [                  \&quot;vtex_logo.jpg\&quot;              ]          }      ],      \&quot;origin\&quot;: \&quot;vtxleo7778\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApiSellerPortal.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = "189371"; // String | Product unique identifier number.
let opts = {
  'putProductRequest': {"attributes":[{"name":"Fabric","value":"Cotton"},{"name":"Gender","value":"Feminine"}],"brandId":"1","categoryIds":["732"],"id":"189371","images":[{"alt":"VTEX","id":"vtex_logo.jpg","url":"https://vtxleo7778.vtexassets.com/assets/vtex.catalog-images/products/vtex_logo.jpg"}],"name":"VTEX 10 Shirt","origin":"vtxleo7778","skus":[{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","id":"182907","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234567","name":"VTEX Shirt Black Size S","specs":[{"name":"Color","value":"Black"},{"name":"Size","value":"S"}],"weight":300},{"dimensions":{"height":2.1,"length":1.6,"width":1.5},"externalId":"1909621862","id":"182908","images":["vtex_logo.jpg"],"isActive":true,"manufacturerCode":"1234568","name":"VTEX Shirt White Size L","specs":[{"name":"Color","value":"White"},{"name":"Size","value":"L"}],"weight":300}],"slug":"/vtex-shirt","specs":[{"name":"Color","values":["Black","White"]},{"name":"Size","values":["S","M","L"]}],"status":"active","taxCode":null,"transportModal":null} // PutProductRequest | 
};
apiInstance.putProduct(contentType, accept, productId, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| Product unique identifier number. | 
 **putProductRequest** | [**PutProductRequest**](PutProductRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putProductDescription

> putProductDescription(contentType, accept, productId, opts)

Update Product Description by Product ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates the description of a product given a Product ID.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: \&quot;71\&quot;,      \&quot;description\&quot;: \&quot;White shirt.\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApiSellerPortal.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = "71"; // String | Product unique identifier number.
let opts = {
  'putProductDescriptionRequest': {"description":"White shirt.","productId":"71"} // PutProductDescriptionRequest | 
};
apiInstance.putProductDescription(contentType, accept, productId, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| Product unique identifier number. | 
 **putProductDescriptionRequest** | [**PutProductDescriptionRequest**](PutProductDescriptionRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

