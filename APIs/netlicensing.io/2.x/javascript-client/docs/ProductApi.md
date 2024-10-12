# Labs64NetLicensingResTfulApiTestCenter.ProductApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProduct**](ProductApi.md#createProduct) | **POST** /product | Create Product
[**deleteProduct**](ProductApi.md#deleteProduct) | **DELETE** /product/{productNumber} | Delete Product
[**listProducts**](ProductApi.md#listProducts) | **GET** /product | List Products
[**productNumber**](ProductApi.md#productNumber) | **GET** /product/{productNumber} | Get Product
[**updateProduct**](ProductApi.md#updateProduct) | **POST** /product/{productNumber} | Update Product



## createProduct

> Netlicensing createProduct(active, name, version, opts)

Create Product

Creates a new Product

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductApi();
let active = true; // Boolean | If set to 'false', the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses.
let name = "name_example"; // String | Product name. Together with the version identifies the Product for the end customer.
let version = "version_example"; // String | Product version. Convenience parameter, additional to the Product name.
let opts = {
  'description': "description_example", // String | Product description.
  'licenseeAutoCreate': true, // Boolean | If set to 'true', non-existing Licensees will be created at first validation attempt.
  'licensingInfo': "licensingInfo_example", // String | Licensing information.
  'number': "number_example", // String | Unique number that identifies the Product. Vendor can assign this number when creating a Product or let NetLicensing generate one.
  'vatMode': "vatMode_example" // String | Vat mode for Product. Supported types: GROSS, NET
};
apiInstance.createProduct(active, name, version, opts, (error, data, response) => {
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
 **active** | **Boolean**| If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses. | 
 **name** | **String**| Product name. Together with the version identifies the Product for the end customer. | 
 **version** | **String**| Product version. Convenience parameter, additional to the Product name. | 
 **description** | **String**| Product description. | [optional] 
 **licenseeAutoCreate** | **Boolean**| If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt. | [optional] 
 **licensingInfo** | **String**| Licensing information. | [optional] 
 **number** | **String**| Unique number that identifies the Product. Vendor can assign this number when creating a Product or let NetLicensing generate one. | [optional] 
 **vatMode** | **String**| Vat mode for Product. Supported types: GROSS, NET | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteProduct

> Netlicensing deleteProduct(productNumber, opts)

Delete Product

Delete a Product by &#39;number&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductApi();
let productNumber = "productNumber_example"; // String | Unique number that identifies the Product.
let opts = {
  'forceCascade': true // Boolean | Force object deletion and all descendants.
};
apiInstance.deleteProduct(productNumber, opts, (error, data, response) => {
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
 **productNumber** | **String**| Unique number that identifies the Product. | 
 **forceCascade** | **Boolean**| Force object deletion and all descendants. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listProducts

> [Netlicensing] listProducts()

List Products

Return a list of all configured Products for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductApi();
apiInstance.listProducts((error, data, response) => {
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

[**[Netlicensing]**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## productNumber

> Netlicensing productNumber(productNumber)

Get Product

Return a Product by &#39;productNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductApi();
let productNumber = "productNumber_example"; // String | Unique number that identifies the Product.
apiInstance.productNumber(productNumber, (error, data, response) => {
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
 **productNumber** | **String**| Unique number that identifies the Product. | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateProduct

> Netlicensing updateProduct(productNumber, opts)

Update Product

Sets the provided properties to a Product. Return an updated Product

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductApi();
let productNumber = "productNumber_example"; // String | Unique number that identifies the Product.
let opts = {
  'active': true, // Boolean | If set to 'false', the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses.
  'description': "description_example", // String | Product description.
  'licenseeAutoCreate': true, // Boolean | If set to 'true', non-existing Licensees will be created at first validation attempt.
  'licensingInfo': "licensingInfo_example", // String | Licensing information.
  'name': "name_example", // String | Product name. Together with the version identifies the Product for the end customer.
  'number': "number_example", // String | New Product number (update)
  'vatMode': "vatMode_example", // String | Vat mode for Product. Supported types: GROSS, NET
  'version': "version_example" // String | Product version. Convenience parameter, additional to the Product name.
};
apiInstance.updateProduct(productNumber, opts, (error, data, response) => {
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
 **productNumber** | **String**| Unique number that identifies the Product. | 
 **active** | **Boolean**| If set to &#39;false&#39;, the Product is disabled. No new Licensees can be registered for the Product, existing Licensees can not obtain new Licenses. | [optional] 
 **description** | **String**| Product description. | [optional] 
 **licenseeAutoCreate** | **Boolean**| If set to &#39;true&#39;, non-existing Licensees will be created at first validation attempt. | [optional] 
 **licensingInfo** | **String**| Licensing information. | [optional] 
 **name** | **String**| Product name. Together with the version identifies the Product for the end customer. | [optional] 
 **number** | **String**| New Product number (update) | [optional] 
 **vatMode** | **String**| Vat mode for Product. Supported types: GROSS, NET | [optional] 
 **version** | **String**| Product version. Convenience parameter, additional to the Product name. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

