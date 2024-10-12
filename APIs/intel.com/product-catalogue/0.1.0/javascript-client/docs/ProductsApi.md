# IntelProductCatalogueService.ProductsApi

All URIs are relative to *https://productapi.intel.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCodeName**](ProductsApi.md#getCodeName) | **GET** /api/products/get-codename | 5. Get list of codename details for Intel products.
[**getProductInfo**](ProductsApi.md#getProductInfo) | **GET** /api/products/get-products-info | 2. Get complete product info with product id.
[**getProductList**](ProductsApi.md#getProductList) | **GET** /api/products/get-products | 1. Find products by product id or category id
[**getorderinginfo**](ProductsApi.md#getorderinginfo) | **GET** /api/products/get-ordering-info | 3. Get ordering info for product id&#39;s requested.



## getCodeName

> CompleteCodenameLsit getCodeName(localeGeoId)

5. Get list of codename details for Intel products.

Use this to get codename details for Intel products. No pagination supported.

### Example

```javascript
import IntelProductCatalogueService from 'intel_product_catalogue_service';
let defaultClient = IntelProductCatalogueService.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ClientId
let ClientId = defaultClient.authentications['ClientId'];
ClientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientId.apiKeyPrefix = 'Token';

let apiInstance = new IntelProductCatalogueService.ProductsApi();
let localeGeoId = "localeGeoId_example"; // String | Locale and Geo code used to get localised data.<br/><br/>
apiInstance.getCodeName(localeGeoId, (error, data, response) => {
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
 **localeGeoId** | **String**| Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt; | 

### Return type

[**CompleteCodenameLsit**](CompleteCodenameLsit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ClientId](../README.md#ClientId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getProductInfo

> DetailedProductInformation getProductInfo(localeGeoId, productId, opts)

2. Get complete product info with product id.

Use this to get complete product info. No pagination supported.

### Example

```javascript
import IntelProductCatalogueService from 'intel_product_catalogue_service';
let defaultClient = IntelProductCatalogueService.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ClientId
let ClientId = defaultClient.authentications['ClientId'];
ClientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientId.apiKeyPrefix = 'Token';

let apiInstance = new IntelProductCatalogueService.ProductsApi();
let localeGeoId = "localeGeoId_example"; // String | Locale and Geo code used to get localised data.<br/><br/>
let productId = "productId_example"; // String | Product id's that needs to be filtered. Only max of 40 products are supported now. Values must be enclosed in [ square brackets ] and each value must be in \"double quotes\". Use comma to add multiple values.<br/><br/>Example: [\"223\",\"224\"]
let opts = {
  'includeReference': "includeReference_example" // String | If send \"true\", this will fetch variant/compatible info into result set. Default is false.
};
apiInstance.getProductInfo(localeGeoId, productId, opts, (error, data, response) => {
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
 **localeGeoId** | **String**| Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt; | 
 **productId** | **String**| Product id&#39;s that needs to be filtered. Only max of 40 products are supported now. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values.&lt;br/&gt;&lt;br/&gt;Example: [\&quot;223\&quot;,\&quot;224\&quot;] | 
 **includeReference** | **String**| If send \&quot;true\&quot;, this will fetch variant/compatible info into result set. Default is false. | [optional] 

### Return type

[**DetailedProductInformation**](DetailedProductInformation.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ClientId](../README.md#ClientId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getProductList

> ProductListingLevelInfo getProductList(localeGeoId, opts)

1. Find products by product id or category id

Use this to get basic details of products with pagination. Can be used to generate listing page for products.

### Example

```javascript
import IntelProductCatalogueService from 'intel_product_catalogue_service';
let defaultClient = IntelProductCatalogueService.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ClientId
let ClientId = defaultClient.authentications['ClientId'];
ClientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientId.apiKeyPrefix = 'Token';

let apiInstance = new IntelProductCatalogueService.ProductsApi();
let localeGeoId = "localeGeoId_example"; // String | Locale and Geo code used to get localised data.<br/><br/>
let opts = {
  'categoryId': "categoryId_example", // String | Filter products based on one or multiple category id. Either category id or product id is mandatory for any request. Values must be enclosed in [ square brackets ] and each value must be in \"double quotes\". Use comma to add multiple values. <br/><br/>Example: [\"873\"]<br/><br/>Categories Available:<br/> Processors = 873, Server Products = 1201, Mini PC's = 98414, Wireless Networking = 59485, Ethernet Products = 36773, Fabric products = 70021, Memory and Storage = 35125, Chipsets = 53, Graphics Drivers = 80939 <br/><br/>
  'productId': "productId_example", // String | Filter products based on one or multiple product id. Either category id or product id is mandatory for any request. Values must be enclosed in [ square brackets ] and each value must be in \"double quotes\". Use comma to add multiple values. <br/><br/>Example: [\"123003\"]<br/><br/>
  'highlights': "highlights_example", // String | Specification values which needs to be pulled from product data. Values must be enclosed in [ square brackets ] and each value must be in \"double quotes\". Use comma to add multiple values. <br/><br/>Example: [\"CoreCount\", \"StatusCodeText\"]<br/><br/>
  'sort': "sort_example", // String | Indicates sorting fields. Accepts array of objects in format like: [{\"field\":\"name\",\"order\":\"ASC\"}].<br/><br/>Any specification that we get from get-product-info can be used to sort result. Other generic sort field is \"name\".<br/><br/>
  'filters': "filters_example", // String | Allows to filter data.<br/><br/>Format of filter: [{\"type\":\"specvalue\",\"name\":\"ThreadCount\",\"gteq\":\"4\"}]<br/><br/><b>Available operators are:</b> \"eq\": equal to, \"neq\": not equal to, \"lteq\": less than or equal to, \"gteq\": greater than or equal to, \"swc\": starts with characters, \"nswc\": not starting with characters, \"cts\": contains, \"ncts\": not contains<br/><br/><b>Conditions:</b> By default all objects works on an AND condition. But inside an object we have the capability to put an \"OR\" or \"AND\" condition.<br/>Example conditions: [{\"type\":\"specvalue\",\"name\":\"ThreadCount\",\"ncts\":\"4,5\",\"cond\":\"AND\"}]<br/><br/><br/>
  'perPage': 56, // Number | Filter number of products in response to desired size.
  'pageNo': 56 // Number | Indicates page number for pagination of results.
};
apiInstance.getProductList(localeGeoId, opts, (error, data, response) => {
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
 **localeGeoId** | **String**| Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt; | 
 **categoryId** | **String**| Filter products based on one or multiple category id. Either category id or product id is mandatory for any request. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;873\&quot;]&lt;br/&gt;&lt;br/&gt;Categories Available:&lt;br/&gt; Processors &#x3D; 873, Server Products &#x3D; 1201, Mini PC&#39;s &#x3D; 98414, Wireless Networking &#x3D; 59485, Ethernet Products &#x3D; 36773, Fabric products &#x3D; 70021, Memory and Storage &#x3D; 35125, Chipsets &#x3D; 53, Graphics Drivers &#x3D; 80939 &lt;br/&gt;&lt;br/&gt; | [optional] 
 **productId** | **String**| Filter products based on one or multiple product id. Either category id or product id is mandatory for any request. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;123003\&quot;]&lt;br/&gt;&lt;br/&gt; | [optional] 
 **highlights** | **String**| Specification values which needs to be pulled from product data. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;CoreCount\&quot;, \&quot;StatusCodeText\&quot;]&lt;br/&gt;&lt;br/&gt; | [optional] 
 **sort** | **String**| Indicates sorting fields. Accepts array of objects in format like: [{\&quot;field\&quot;:\&quot;name\&quot;,\&quot;order\&quot;:\&quot;ASC\&quot;}].&lt;br/&gt;&lt;br/&gt;Any specification that we get from get-product-info can be used to sort result. Other generic sort field is \&quot;name\&quot;.&lt;br/&gt;&lt;br/&gt; | [optional] 
 **filters** | **String**| Allows to filter data.&lt;br/&gt;&lt;br/&gt;Format of filter: [{\&quot;type\&quot;:\&quot;specvalue\&quot;,\&quot;name\&quot;:\&quot;ThreadCount\&quot;,\&quot;gteq\&quot;:\&quot;4\&quot;}]&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Available operators are:&lt;/b&gt; \&quot;eq\&quot;: equal to, \&quot;neq\&quot;: not equal to, \&quot;lteq\&quot;: less than or equal to, \&quot;gteq\&quot;: greater than or equal to, \&quot;swc\&quot;: starts with characters, \&quot;nswc\&quot;: not starting with characters, \&quot;cts\&quot;: contains, \&quot;ncts\&quot;: not contains&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Conditions:&lt;/b&gt; By default all objects works on an AND condition. But inside an object we have the capability to put an \&quot;OR\&quot; or \&quot;AND\&quot; condition.&lt;br/&gt;Example conditions: [{\&quot;type\&quot;:\&quot;specvalue\&quot;,\&quot;name\&quot;:\&quot;ThreadCount\&quot;,\&quot;ncts\&quot;:\&quot;4,5\&quot;,\&quot;cond\&quot;:\&quot;AND\&quot;}]&lt;br/&gt;&lt;br/&gt;&lt;br/&gt; | [optional] 
 **perPage** | **Number**| Filter number of products in response to desired size. | [optional] 
 **pageNo** | **Number**| Indicates page number for pagination of results. | [optional] 

### Return type

[**ProductListingLevelInfo**](ProductListingLevelInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ClientId](../README.md#ClientId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getorderinginfo

> DetailedOrderingLevelInfo getorderinginfo(productId, localeGeoId)

3. Get ordering info for product id&#39;s requested.

Use this to fetch ordering info details for Intel products. No pagination supported.

### Example

```javascript
import IntelProductCatalogueService from 'intel_product_catalogue_service';
let defaultClient = IntelProductCatalogueService.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ClientId
let ClientId = defaultClient.authentications['ClientId'];
ClientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientId.apiKeyPrefix = 'Token';

let apiInstance = new IntelProductCatalogueService.ProductsApi();
let productId = "productId_example"; // String | Filter ordering info details based on one or multiple product id's. Values must be enclosed in [ square brackets ] and each value must be in \"double quotes\". Use comma to add multiple values. <br/><br/>Example: [\"123003\"]
let localeGeoId = "localeGeoId_example"; // String | Locale and Geo code used to get localised data.<br/><br/>
apiInstance.getorderinginfo(productId, localeGeoId, (error, data, response) => {
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
 **productId** | **String**| Filter ordering info details based on one or multiple product id&#39;s. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;123003\&quot;] | 
 **localeGeoId** | **String**| Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt; | 

### Return type

[**DetailedOrderingLevelInfo**](DetailedOrderingLevelInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ClientId](../README.md#ClientId)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

