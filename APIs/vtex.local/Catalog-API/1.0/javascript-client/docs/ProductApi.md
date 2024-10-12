# CatalogApi.ProductApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtProductPost**](ProductApi.md#apiCatalogPvtProductPost) | **POST** /api/catalog/pvt/product | Create Product with Category and Brand
[**apiCatalogPvtProductProductIdPut**](ProductApi.md#apiCatalogPvtProductProductIdPut) | **PUT** /api/catalog/pvt/product/{productId} | Update Product
[**getProductbyid**](ProductApi.md#getProductbyid) | **GET** /api/catalog/pvt/product/{productId} | Get Product by ID
[**productAndSkuIds**](ProductApi.md#productAndSkuIds) | **GET** /api/catalog_system/pvt/products/GetProductAndSkuIds | Get Product and SKU IDs
[**productVariations**](ProductApi.md#productVariations) | **GET** /api/catalog_system/pub/products/variations/{productId} | Get Product&#39;s SKUs by Product ID
[**productandTradePolicy**](ProductApi.md#productandTradePolicy) | **GET** /api/catalog_system/pvt/products/productget/{productId} | Get Product and its general context
[**productbyRefId**](ProductApi.md#productbyRefId) | **GET** /api/catalog_system/pvt/products/productgetbyrefid/{refId} | Get Product by RefId
[**reviewRateProduct**](ProductApi.md#reviewRateProduct) | **GET** /api/addon/pvt/review/GetProductRate/{productId} | Get Product Review Rate by Product ID



## apiCatalogPvtProductPost

> ApiCatalogPvtProductPost200Response apiCatalogPvtProductPost(contentType, accept, opts)

Create Product with Category and Brand

This endpoint allows two types of request:    **Type 1:** Creating a new Product as well as a new Category path (including subcategories) and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60; parameters.    **Type 2:** Creating a new Product given an existing &#x60;BrandId&#x60; and an existing &#x60;CategoryId&#x60;.    When creating a product, regardless of the type of request, if there is a need to create a new product with a specific custom product ID, specify the &#x60;Id&#x60; (integer) in the request body. Otherwise, VTEX will generate the ID automatically.     ## Request body examples     ### Type 1     Request to create a product, associating it to a new Category and a new Brand by using &#x60;CategoryPath&#x60; and &#x60;BrandName&#x60;:    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;CategoryPath\&quot;: \&quot;Mens/Clothing/T-Shirts\&quot;,      \&quot;BrandName\&quot;: \&quot;Nike\&quot;,      \&quot;RefId\&quot;: \&quot;31011706925\&quot;,      \&quot;Title\&quot;: \&quot;Black T-Shirt\&quot;,      \&quot;LinkId\&quot;: \&quot;tshirt-black\&quot;,      \&quot;Description\&quot;: \&quot;This is a cool Tshirt\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2022-01-01T00:00:00\&quot;,      \&quot;IsVisible\&quot;: true,      \&quot;IsActive\&quot;: true,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;MetaTagDescription\&quot;: \&quot;tshirt black\&quot;,      \&quot;ShowWithoutStock\&quot;: true,      \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ### Type 2    Request to create a product, associating it to an existing &#x60;CategoryId&#x60; and &#x60;BrandId&#x60;:    &#x60;&#x60;&#x60;json  {     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 52,     \&quot;Name\&quot;: \&quot;insert product test\&quot;,     \&quot;DepartmentId\&quot;: 1,     \&quot;CategoryId\&quot;: 2,     \&quot;BrandId\&quot;: 2000000,     \&quot;LinkId\&quot;: \&quot;insert-product-test\&quot;,     \&quot;RefId\&quot;: \&quot;310117869\&quot;,     \&quot;IsVisible\&quot;: true,     \&quot;Description\&quot;: \&quot;texto de descrição\&quot;,     \&quot;DescriptionShort\&quot;: \&quot;Utilize o CEP 04548-005 para frete grátis\&quot;,     \&quot;ReleaseDate\&quot;: \&quot;2019-01-01T00:00:00\&quot;,     \&quot;KeyWords\&quot;: \&quot;teste,teste2\&quot;,     \&quot;Title\&quot;: \&quot;product de teste\&quot;,     \&quot;IsActive\&quot;: true,     \&quot;TaxCode\&quot;: \&quot;\&quot;,     \&quot;MetaTagDescription\&quot;: \&quot;tag test\&quot;,     \&quot;SupplierId\&quot;: 1,     \&quot;ShowWithoutStock\&quot;: true,     \&quot;AdWordsRemarketingCode\&quot;: null,     \&quot;LomadeeCampaignCode\&quot;: null,     \&quot;Score\&quot;: 1  }  &#x60;&#x60;&#x60;      &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'apiCatalogPvtProductPostRequest': new CatalogApi.ApiCatalogPvtProductPostRequest() // ApiCatalogPvtProductPostRequest | 
};
apiInstance.apiCatalogPvtProductPost(contentType, accept, opts, (error, data, response) => {
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
 **apiCatalogPvtProductPostRequest** | [**ApiCatalogPvtProductPostRequest**](ApiCatalogPvtProductPostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtProductPost200Response**](ApiCatalogPvtProductPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtProductProductIdPut

> ApiCatalogPvtProductPost200Response apiCatalogPvtProductProductIdPut(contentType, accept, productId, opts)

Update Product

Updates an existing Product.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let opts = {
  'apiCatalogPvtProductProductIdPutRequest': new CatalogApi.ApiCatalogPvtProductProductIdPutRequest() // ApiCatalogPvtProductProductIdPutRequest | 
};
apiInstance.apiCatalogPvtProductProductIdPut(contentType, accept, productId, opts, (error, data, response) => {
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
 **productId** | **Number**| Product’s unique numerical identifier. | 
 **apiCatalogPvtProductProductIdPutRequest** | [**ApiCatalogPvtProductProductIdPutRequest**](ApiCatalogPvtProductProductIdPutRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtProductPost200Response**](ApiCatalogPvtProductPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getProductbyid

> GetProductbyid200Response getProductbyid(contentType, accept, productId)

Get Product by ID

Retrieves a specific Product by its ID. This information is exactly what is needed to create a new Product.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = "productId_example"; // String | Product’s unique numerical identifier.
apiInstance.getProductbyid(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| Product’s unique numerical identifier. | 

### Return type

[**GetProductbyid200Response**](GetProductbyid200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productAndSkuIds

> ProductAndSkuIds200Response productAndSkuIds(contentType, accept, opts)

Get Product and SKU IDs

Retrieves the IDs of products and SKUs.   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'categoryId': 1, // Number | ID of the category from which you need to retrieve Products and SKUs.
  'from': 1, // Number | Insert the ID that will start the request result.
  'to': 10 // Number | Insert the ID that will end the request result.
};
apiInstance.productAndSkuIds(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **categoryId** | **Number**| ID of the category from which you need to retrieve Products and SKUs. | [optional] 
 **from** | **Number**| Insert the ID that will start the request result. | [optional] 
 **to** | **Number**| Insert the ID that will end the request result. | [optional] 

### Return type

[**ProductAndSkuIds200Response**](ProductAndSkuIds200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariations

> ProductVariations200Response productVariations(contentType, accept, productId)

Get Product&#39;s SKUs by Product ID

Retrieves data about the product and all SKUs related to it by the product&#39;s ID.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;productId\&quot;: 9,      \&quot;name\&quot;: \&quot;Camisa Masculina\&quot;,      \&quot;salesChannel\&quot;: \&quot;2\&quot;,      \&quot;available\&quot;: true,      \&quot;displayMode\&quot;: \&quot;lista\&quot;,      \&quot;dimensions\&quot;: [          \&quot;Cores\&quot;,          \&quot;Tamanho\&quot;,          \&quot;País de origem\&quot;,          \&quot;Gênero\&quot;      ],      \&quot;dimensionsInputType\&quot;: {          \&quot;Cores\&quot;: \&quot;Combo\&quot;,          \&quot;Tamanho\&quot;: \&quot;Combo\&quot;,          \&quot;País de origem\&quot;: \&quot;Combo\&quot;,          \&quot;Gênero\&quot;: \&quot;Combo\&quot;      },      \&quot;dimensionsMap\&quot;: {          \&quot;Cores\&quot;: [              \&quot;Amarelo\&quot;,              \&quot;Azul\&quot;,              \&quot;Vermelho\&quot;          ],          \&quot;Tamanho\&quot;: [              \&quot;P\&quot;,              \&quot;M\&quot;,              \&quot;G\&quot;          ],          \&quot;País de origem\&quot;: [              \&quot;Brasil\&quot;          ],          \&quot;Gênero\&quot;: [              \&quot;Masculino\&quot;          ]      },      \&quot;skus\&quot;: [          {              \&quot;sku\&quot;: 310118454,              \&quot;skuname\&quot;: \&quot;Amarela - G\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Amarelo\&quot;,                  \&quot;Tamanho\&quot;: \&quot;G\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: false,              \&quot;availablequantity\&quot;: 0,              \&quot;cacheVersionUsedToCallCheckout\&quot;: null,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 9.999.876,00\&quot;,              \&quot;bestPrice\&quot;: 999987600,              \&quot;spotPrice\&quot;: 999987600,              \&quot;installments\&quot;: 0,              \&quot;installmentsValue\&quot;: 0,              \&quot;installmentsInsterestRate\&quot;: null,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155467-292-292/image-5d7ad76ad1954c53adecab4138319034.jpg?v&#x3D;637321899584500000\&quot;,              \&quot;sellerId\&quot;: \&quot;1\&quot;,              \&quot;seller\&quot;: \&quot;lojadobreno\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 1.0000,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          },          {              \&quot;sku\&quot;: 310118455,              \&quot;skuname\&quot;: \&quot;Vermelha - M\&quot;,              \&quot;dimensions\&quot;: {                  \&quot;Cores\&quot;: \&quot;Vermelho\&quot;,                  \&quot;Tamanho\&quot;: \&quot;M\&quot;,                  \&quot;País de origem\&quot;: \&quot;Brasil\&quot;,                  \&quot;Gênero\&quot;: \&quot;Masculino\&quot;              },              \&quot;available\&quot;: true,              \&quot;availablequantity\&quot;: 99999,              \&quot;cacheVersionUsedToCallCheckout\&quot;: \&quot;38395F1AEF59DF5CEAEDE472328145CD_\&quot;,              \&quot;listPriceFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;listPrice\&quot;: 0,              \&quot;taxFormated\&quot;: \&quot;R$ 0,00\&quot;,              \&quot;taxAsInt\&quot;: 0,              \&quot;bestPriceFormated\&quot;: \&quot;R$ 20,00\&quot;,              \&quot;bestPrice\&quot;: 2000,              \&quot;spotPrice\&quot;: 2000,              \&quot;installments\&quot;: 1,              \&quot;installmentsValue\&quot;: 2000,              \&quot;installmentsInsterestRate\&quot;: 0,              \&quot;image\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155468-292-292/image-601a6099aace48b89d26fc9f22e8e611.jpg?v&#x3D;637321906602470000\&quot;,              \&quot;sellerId\&quot;: \&quot;pedrostore\&quot;,              \&quot;seller\&quot;: \&quot;pedrostore\&quot;,              \&quot;measures\&quot;: {                  \&quot;cubicweight\&quot;: 0.4167,                  \&quot;height\&quot;: 5.0000,                  \&quot;length\&quot;: 20.0000,                  \&quot;weight\&quot;: 200.0000,                  \&quot;width\&quot;: 20.0000              },              \&quot;unitMultiplier\&quot;: 1.0000,              \&quot;rewardValue\&quot;: 0          }      ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.productVariations(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **Number**| Product’s unique numerical identifier. | 

### Return type

[**ProductVariations200Response**](ProductVariations200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productandTradePolicy

> ProductandTradePolicy200Response productandTradePolicy(contentType, accept, productId)

Get Product and its general context

Retrieves a specific product&#39;s general information as name, description and the trade policies that it is included.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.productandTradePolicy(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **Number**| Product’s unique numerical identifier. | 

### Return type

[**ProductandTradePolicy200Response**](ProductandTradePolicy200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productbyRefId

> ProductbyRefId200Response productbyRefId(contentType, accept, refId)

Get Product by RefId

Retrieves a specific product by its Reference ID.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let refId = "refId_example"; // String | Product Referecial Code
apiInstance.productbyRefId(contentType, accept, refId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **refId** | **String**| Product Referecial Code | 

### Return type

[**ProductbyRefId200Response**](ProductbyRefId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewRateProduct

> Number reviewRateProduct(contentType, accept, productId)

Get Product Review Rate by Product ID

Retrieves the review rate of a product by this product&#39;s ID.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.ProductApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.reviewRateProduct(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **Number**| Product’s unique numerical identifier. | 

### Return type

**Number**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

