# BillbeeApi.ProductsApi

All URIs are relative to *https://app.billbee.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**articleCreateArticle**](ProductsApi.md#articleCreateArticle) | **POST** /api/v1/products | Creates a new product
[**articleDeleteArticle**](ProductsApi.md#articleDeleteArticle) | **DELETE** /api/v1/products/{id} | Deletes a product
[**articleDeleteImage**](ProductsApi.md#articleDeleteImage) | **DELETE** /api/v1/products/images/{imageId} | Deletes a single image by id
[**articleDeleteImageFromProduct**](ProductsApi.md#articleDeleteImageFromProduct) | **DELETE** /api/v1/products/{productId}/images/{imageId} | Deletes a single image from a product
[**articleDeleteImages**](ProductsApi.md#articleDeleteImages) | **POST** /api/v1/products/images/delete | Delete multiple images by id
[**articleGetArticle**](ProductsApi.md#articleGetArticle) | **GET** /api/v1/products/{id} | Queries a single article by id or by sku
[**articleGetCategory**](ProductsApi.md#articleGetCategory) | **GET** /api/v1/products/category | GEts a list of all defined categories
[**articleGetCustomField**](ProductsApi.md#articleGetCustomField) | **GET** /api/v1/products/custom-fields/{id} | Queries a single custom field
[**articleGetCustomFields**](ProductsApi.md#articleGetCustomFields) | **GET** /api/v1/products/custom-fields | Queries a list of all custom fields
[**articleGetImage**](ProductsApi.md#articleGetImage) | **GET** /api/v1/products/images/{imageId} | Returns a single image by id
[**articleGetImageFromProduct**](ProductsApi.md#articleGetImageFromProduct) | **GET** /api/v1/products/{productId}/images/{imageId} | Returns a single image by id
[**articleGetImages**](ProductsApi.md#articleGetImages) | **GET** /api/v1/products/{productId}/images | Returns a list of all images of the product
[**articleGetList**](ProductsApi.md#articleGetList) | **GET** /api/v1/products | Get a list of all products
[**articleGetPatchableFields**](ProductsApi.md#articleGetPatchableFields) | **GET** /api/v1/products/PatchableFields | Returns a list of fields which can be updated with the patch call
[**articleGetReservedAmount**](ProductsApi.md#articleGetReservedAmount) | **GET** /api/v1/products/reservedamount | Queries the reserved amount for a single article by id or by sku
[**articleGetStocks**](ProductsApi.md#articleGetStocks) | **GET** /api/v1/products/stocks | Query all defined stock locations
[**articlePatchArticle**](ProductsApi.md#articlePatchArticle) | **PATCH** /api/v1/products/{id} | Updates one or more fields of a product
[**articlePutImage**](ProductsApi.md#articlePutImage) | **PUT** /api/v1/products/{productId}/images/{imageId} | Add or update an existing image of a product
[**articlePutImages**](ProductsApi.md#articlePutImages) | **PUT** /api/v1/products/{productId}/images | Add multiple images to a product or replace the product images by the given images
[**articleUpdateStock**](ProductsApi.md#articleUpdateStock) | **POST** /api/v1/products/updatestock | Update the stock qty of an article
[**articleUpdateStockCode**](ProductsApi.md#articleUpdateStockCode) | **POST** /api/v1/products/updatestockcode | Update the stock code of an article
[**articleUpdateStockMultiple**](ProductsApi.md#articleUpdateStockMultiple) | **POST** /api/v1/products/updatestockmultiple | Update the stock qty for multiple articles at once
[**searchSearch**](ProductsApi.md#searchSearch) | **POST** /api/v1/search | Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax



## articleCreateArticle

> Object articleCreateArticle(billbeeInterfacesBillbeeAPIModelArticleApiModel)

Creates a new product

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let billbeeInterfacesBillbeeAPIModelArticleApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelArticleApiModel(); // BillbeeInterfacesBillbeeAPIModelArticleApiModel | 
apiInstance.articleCreateArticle(billbeeInterfacesBillbeeAPIModelArticleApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelArticleApiModel** | [**BillbeeInterfacesBillbeeAPIModelArticleApiModel**](BillbeeInterfacesBillbeeAPIModelArticleApiModel.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json


## articleDeleteArticle

> Object articleDeleteArticle(id)

Deletes a product

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let id = 789; // Number | The id of the Product
apiInstance.articleDeleteArticle(id, (error, data, response) => {
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
 **id** | **Number**| The id of the Product | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleDeleteImage

> Object articleDeleteImage(imageId)

Deletes a single image by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let imageId = 789; // Number | The image id
apiInstance.articleDeleteImage(imageId, (error, data, response) => {
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
 **imageId** | **Number**| The image id | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleDeleteImageFromProduct

> Object articleDeleteImageFromProduct(productId, imageId)

Deletes a single image from a product

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let productId = 789; // Number | The product id
let imageId = 789; // Number | The image id
apiInstance.articleDeleteImageFromProduct(productId, imageId, (error, data, response) => {
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
 **productId** | **Number**| The product id | 
 **imageId** | **Number**| The image id | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleDeleteImages

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel articleDeleteImages(requestBody)

Delete multiple images by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let requestBody = [null]; // [Number] | 
apiInstance.articleDeleteImages(requestBody, (error, data, response) => {
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
 **requestBody** | [**[Number]**](Number.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelDeletedImagesModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetArticle

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel articleGetArticle(id, opts)

Queries a single article by id or by sku

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let id = "id_example"; // String | The id or the sku of the article to query
let opts = {
  'lookupBy': "lookupBy_example" // String | Either the value id, ean or the value sku to specify the meaning of the id parameter.
};
apiInstance.articleGetArticle(id, opts, (error, data, response) => {
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
 **id** | **String**| The id or the sku of the article to query | 
 **lookupBy** | **String**| Either the value id, ean or the value sku to specify the meaning of the id parameter. | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleGetCategory

> Object articleGetCategory()

GEts a list of all defined categories

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
apiInstance.articleGetCategory((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleGetCustomField

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel articleGetCustomField(id)

Queries a single custom field

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let id = 789; // Number | The id of the custom field to query
apiInstance.articleGetCustomField(id, (error, data, response) => {
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
 **id** | **Number**| The id of the custom field to query | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetCustomFields

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel articleGetCustomFields(opts)

Queries a list of all custom fields

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let opts = {
  'page': 56, // Number | 
  'pageSize': 56 // Number | 
};
apiInstance.articleGetCustomFields(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] 
 **pageSize** | **Number**|  | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiCustomFieldDefinitionModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetImage

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articleGetImage(imageId)

Returns a single image by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let imageId = 789; // Number | The Id of the image
apiInstance.articleGetImage(imageId, (error, data, response) => {
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
 **imageId** | **Number**| The Id of the image | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetImageFromProduct

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articleGetImageFromProduct(productId, imageId)

Returns a single image by id

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let productId = 789; // Number | The Id of the product
let imageId = 789; // Number | The Id of the image
apiInstance.articleGetImageFromProduct(productId, imageId, (error, data, response) => {
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
 **productId** | **Number**| The Id of the product | 
 **imageId** | **Number**| The Id of the image | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetImages

> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articleGetImages(productId)

Returns a list of all images of the product

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let productId = 789; // Number | The Id of the product
apiInstance.articleGetImages(productId, (error, data, response) => {
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
 **productId** | **Number**| The Id of the product | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetList

> RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel articleGetList(opts)

Get a list of all products

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let opts = {
  'page': 56, // Number | The current page to request starting with 1
  'pageSize': 56, // Number | The pagesize for the result list. Values between 1 and 250 are allowed
  'minCreatedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional the oldest create date of the articles to be returned
  'minimumBillBeeArticleId': 789, // Number | 
  'maximumBillBeeArticleId': 789 // Number | 
};
apiInstance.articleGetList(opts, (error, data, response) => {
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
 **page** | **Number**| The current page to request starting with 1 | [optional] 
 **pageSize** | **Number**| The pagesize for the result list. Values between 1 and 250 are allowed | [optional] 
 **minCreatedAt** | **Date**| Optional the oldest create date of the articles to be returned | [optional] 
 **minimumBillBeeArticleId** | **Number**|  | [optional] 
 **maximumBillBeeArticleId** | **Number**|  | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel**](RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelArticleApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleGetPatchableFields

> Object articleGetPatchableFields()

Returns a list of fields which can be updated with the patch call

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
apiInstance.articleGetPatchableFields((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## articleGetReservedAmount

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData articleGetReservedAmount(id, opts)

Queries the reserved amount for a single article by id or by sku

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let id = "id_example"; // String | The id or the sku of the article to query
let opts = {
  'lookupBy': "lookupBy_example", // String | Either the value id or the value sku to specify the meaning of the id parameter
  'stockId': 789 // Number | Optional the stock id if the multi stock feature is enabled
};
apiInstance.articleGetReservedAmount(id, opts, (error, data, response) => {
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
 **id** | **String**| The id or the sku of the article to query | 
 **lookupBy** | **String**| Either the value id or the value sku to specify the meaning of the id parameter | [optional] 
 **stockId** | **Number**| Optional the stock id if the multi stock feature is enabled | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelGetReservedAmountResponseData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articleGetStocks

> RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData articleGetStocks()

Query all defined stock locations

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
apiInstance.articleGetStocks((error, data, response) => {
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

[**RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData**](RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelStockResponseData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## articlePatchArticle

> Object articlePatchArticle(id, body)

Updates one or more fields of a product

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let id = 789; // Number | The id of the Product
let body = {key: null}; // Object | 
apiInstance.articlePatchArticle(id, body, (error, data, response) => {
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
 **id** | **Number**| The id of the Product | 
 **body** | **Object**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
- **Accept**: application/json, text/json


## articlePutImage

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articlePutImage(productId, imageId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel)

Add or update an existing image of a product

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let productId = 789; // Number | The product id
let imageId = 789; // Number | The image id. If you pass 0, the image will be added
let billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel(); // BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel | The ArticleApiImageModel
apiInstance.articlePutImage(productId, imageId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel, (error, data, response) => {
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
 **productId** | **Number**| The product id | 
 **imageId** | **Number**| The image id. If you pass 0, the image will be added | 
 **billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel** | [**BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)| The ArticleApiImageModel | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## articlePutImages

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel articlePutImages(productId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel, opts)

Add multiple images to a product or replace the product images by the given images

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let productId = 789; // Number | The id of the product
let billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel = [new BillbeeApi.BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel()]; // [BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel] | An array of ArticleApiImageModel
let opts = {
  'replace': true // Boolean | If you pass true, the images will be replaced by the passed images. Otherwise the passed images will be appended to the product.
};
apiInstance.articlePutImages(productId, billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel, opts, (error, data, response) => {
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
 **productId** | **Number**| The id of the product | 
 **billbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel** | [**[BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel]**](BillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)| An array of ArticleApiImageModel | 
 **replace** | **Boolean**| If you pass true, the images will be replaced by the passed images. Otherwise the passed images will be appended to the product. | [optional] 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelArticleImageRelationApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## articleUpdateStock

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData articleUpdateStock(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel)

Update the stock qty of an article

The article is specified by sku. You have to send the absolute value for the current stock

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let billbeeInterfacesBillbeeAPIModelUpdateStockApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel(); // BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel | 
apiInstance.articleUpdateStock(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelUpdateStockApiModel** | [**BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel**](BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## articleUpdateStockCode

> RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData articleUpdateStockCode(billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel)

Update the stock code of an article

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel = new BillbeeApi.BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel(); // BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel | 
apiInstance.articleUpdateStockCode(billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel** | [**BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel**](BillbeeInterfacesBillbeeAPIModelUpdateStockCodeApiModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockCodeResponseData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## articleUpdateStockMultiple

> [RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData] articleUpdateStockMultiple(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel)

Update the stock qty for multiple articles at once

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let billbeeInterfacesBillbeeAPIModelUpdateStockApiModel = [new BillbeeApi.BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel()]; // [BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel] | 
apiInstance.articleUpdateStockMultiple(billbeeInterfacesBillbeeAPIModelUpdateStockApiModel, (error, data, response) => {
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
 **billbeeInterfacesBillbeeAPIModelUpdateStockApiModel** | [**[BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel]**](BillbeeInterfacesBillbeeAPIModelUpdateStockApiModel.md)|  | 

### Return type

[**[RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData]**](RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelUpdateStockResponseData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## searchSearch

> RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel searchSearch(rechnungsdruckWebAppControllersApiSearchControllerSearchModel)

Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

### Example

```javascript
import BillbeeApi from 'billbee_api';

let apiInstance = new BillbeeApi.ProductsApi();
let rechnungsdruckWebAppControllersApiSearchControllerSearchModel = new BillbeeApi.RechnungsdruckWebAppControllersApiSearchControllerSearchModel(); // RechnungsdruckWebAppControllersApiSearchControllerSearchModel | 
apiInstance.searchSearch(rechnungsdruckWebAppControllersApiSearchControllerSearchModel, (error, data, response) => {
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
 **rechnungsdruckWebAppControllersApiSearchControllerSearchModel** | [**RechnungsdruckWebAppControllersApiSearchControllerSearchModel**](RechnungsdruckWebAppControllersApiSearchControllerSearchModel.md)|  | 

### Return type

[**RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel**](RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

