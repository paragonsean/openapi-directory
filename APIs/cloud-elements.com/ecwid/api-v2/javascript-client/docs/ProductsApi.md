# Ecwid.ProductsApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProduct**](ProductsApi.md#createProduct) | **POST** /products | Create a new product in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Product&#39; model are those required to create a new product
[**deleteProductById**](ProductsApi.md#deleteProductById) | **DELETE** /products/{id} | Delete a product associated with a given ID from your eCommerce system. Specifying a product associated with a given ID that does not exist will result in an error message
[**getProductById**](ProductsApi.md#getProductById) | **GET** /products/{id} | Retrieve a product associated with a given ID from the eCommerce system. Specifying a product with an ID that does not exist will result in an error response
[**getProducts**](ProductsApi.md#getProducts) | **GET** /products | Find products in the eCommerce system, using the provided CEQL search expression. The search expression in CEQL is the WHERE clause in a typical SQL query, but without the WHERE keyword.  If no search expression is provided, all records will be retrieved
[**updateProductById**](ProductsApi.md#updateProductById) | **PATCH** /products/{id} | Update a product associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the product object will be updated, and those fields not provided will be left alone. Updating a product with a specified ID that does not exist will result in an error response. &lt;p&gt;&lt;strong&gt;Update supports the following fields: sku, quantity, trackQuantity, quantityDelta, warningLimit, name, price, weight, tangible, enabled, fixedShippingRateOnly, fixedShippingRate, description, wholesalePrices, compareAtPrice, productClassId&lt;/strong&gt;



## createProduct

> Product createProduct(authorization, product)

Create a new product in eCommerce system.With the exception of the &#39;id&#39; field, the required fields indicated in the &#39;Product&#39; model are those required to create a new product

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ProductsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let product = new Ecwid.ProductPost(); // ProductPost | The product object to be created
apiInstance.createProduct(authorization, product, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **product** | [**ProductPost**](ProductPost.md)| The product object to be created | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## deleteProductById

> deleteProductById(authorization, id)

Delete a product associated with a given ID from your eCommerce system. Specifying a product associated with a given ID that does not exist will result in an error message

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ProductsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the product to delete from the eCommerce system
apiInstance.deleteProductById(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the product to delete from the eCommerce system | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductById

> Product getProductById(authorization, id)

Retrieve a product associated with a given ID from the eCommerce system. Specifying a product with an ID that does not exist will result in an error response

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ProductsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the product to retrieve from the eCommerce system
apiInstance.getProductById(authorization, id, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the product to retrieve from the eCommerce system | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getProducts

> [Product] getProducts(authorization, opts)

Find products in the eCommerce system, using the provided CEQL search expression. The search expression in CEQL is the WHERE clause in a typical SQL query, but without the WHERE keyword.  If no search expression is provided, all records will be retrieved

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ProductsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let opts = {
  'where': "where_example", // String | The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field='value'). <p>Supported search terms: category, hidden_products. All other search criteria are ignored
  'pageSize': 789, // Number | The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned
  'nextPage': "nextPage_example", // String | The next page cursor, taken from the response header: `elements-next-page-token`
  'fields': "fields_example" // String | The fields to return on the response. Can be a single field or a comma-separated list of fields
};
apiInstance.getProducts(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **where** | **String**| The CEQL search expression, or the where clause, without the WHERE keyword, in a typical SQL query (i.e. field&#x3D;&#39;value&#39;). &lt;p&gt;Supported search terms: category, hidden_products. All other search criteria are ignored | [optional] 
 **pageSize** | **Number**| The number of results to fetch in a given page. When this parameter is omitted, a maximum of 200 results are returned | [optional] 
 **nextPage** | **String**| The next page cursor, taken from the response header: &#x60;elements-next-page-token&#x60; | [optional] 
 **fields** | **String**| The fields to return on the response. Can be a single field or a comma-separated list of fields | [optional] 

### Return type

[**[Product]**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateProductById

> Product updateProductById(authorization, id, product)

Update a product associated with a given ID in the eCommerce system. The update API uses the PATCH HTTP verb, so only those fields provided in the product object will be updated, and those fields not provided will be left alone. Updating a product with a specified ID that does not exist will result in an error response. &lt;p&gt;&lt;strong&gt;Update supports the following fields: sku, quantity, trackQuantity, quantityDelta, warningLimit, name, price, weight, tangible, enabled, fixedShippingRateOnly, fixedShippingRate, description, wholesalePrices, compareAtPrice, productClassId&lt;/strong&gt;

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ProductsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let id = "id_example"; // String | The ID of the product to update in the eCommerce system
let product = new Ecwid.ProductPatch(); // ProductPatch | The product object, with those fields that are to be updated
apiInstance.updateProductById(authorization, id, product, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **id** | **String**| The ID of the product to update in the eCommerce system | 
 **product** | [**ProductPatch**](ProductPatch.md)| The product object, with those fields that are to be updated | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

