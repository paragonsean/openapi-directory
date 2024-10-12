# Labs64NetLicensingResTfulApiTestCenter.ProductModuleApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProductModule**](ProductModuleApi.md#createProductModule) | **POST** /productmodule | Create Product Module
[**deleteProductModule**](ProductModuleApi.md#deleteProductModule) | **DELETE** /productmodule/{productModuleNumber} | Delete Product Module
[**getProductModule**](ProductModuleApi.md#getProductModule) | **GET** /productmodule/{productModuleNumber} | Get Product Module
[**listProductModules**](ProductModuleApi.md#listProductModules) | **GET** /productmodule | List Product Modules
[**updateProductModule**](ProductModuleApi.md#updateProductModule) | **POST** /productmodule/{productModuleNumber} | Update Product Module



## createProductModule

> Netlicensing createProductModule(active, licensingModel, name, productNumber, opts)

Create Product Module

Creates a new Product Module

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductModuleApi();
let active = true; // Boolean | If set to 'false', the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module.
let licensingModel = "licensingModel_example"; // String | Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation.
let name = "name_example"; // String | Product Module name that is visible to the end customers in NetLicensing Shop.
let productNumber = "productNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
let opts = {
  'licenseTemplate': ["'TIMEVOLUME'"], // [String] | License Template. Mandatory for 'Try &amp; Buy' licensing model.
  'maxCheckoutValidity': 56, // Number | Maximum checkout validity (days). Mandatory for 'Floating' licensing model.
  'nodeSecretMode': ["'PREDEFINED'"], // [String] | Secret Mode. Mandatory for 'Node-Locked' licensing model.
  'number': "number_example", // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
  'redThreshold': 56, // Number | Remaining time volume for red level. Mandatory for 'Rental' licensing model.
  'yellowThreshold': 56 // Number | Remaining time volume for yellow level. Mandatory for 'Rental' licensing model.
};
apiInstance.createProductModule(active, licensingModel, name, productNumber, opts, (error, data, response) => {
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
 **active** | **Boolean**| If set to &#39;false&#39;, the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module. | 
 **licensingModel** | **String**| Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation. | 
 **name** | **String**| Product Module name that is visible to the end customers in NetLicensing Shop. | 
 **productNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | 
 **licenseTemplate** | [**[String]**](String.md)| License Template. Mandatory for &#39;Try &amp;amp; Buy&#39; licensing model. | [optional] [default to &#39;TIMEVOLUME&#39;]
 **maxCheckoutValidity** | **Number**| Maximum checkout validity (days). Mandatory for &#39;Floating&#39; licensing model. | [optional] 
 **nodeSecretMode** | [**[String]**](String.md)| Secret Mode. Mandatory for &#39;Node-Locked&#39; licensing model. | [optional] [default to &#39;PREDEFINED&#39;]
 **number** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | [optional] 
 **redThreshold** | **Number**| Remaining time volume for red level. Mandatory for &#39;Rental&#39; licensing model. | [optional] 
 **yellowThreshold** | **Number**| Remaining time volume for yellow level. Mandatory for &#39;Rental&#39; licensing model. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteProductModule

> Netlicensing deleteProductModule(productModuleNumber, opts)

Delete Product Module

Delete a Product Module by &#39;number&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductModuleApi();
let productModuleNumber = "productModuleNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module.
let opts = {
  'forceCascade': true // Boolean | Force object deletion and all descendants.
};
apiInstance.deleteProductModule(productModuleNumber, opts, (error, data, response) => {
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
 **productModuleNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. | 
 **forceCascade** | **Boolean**| Force object deletion and all descendants. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProductModule

> Netlicensing getProductModule(productModuleNumber)

Get Product Module

Return a Product Module by &#39;productModuleNumber&#39;

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductModuleApi();
let productModuleNumber = "productModuleNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
apiInstance.getProductModule(productModuleNumber, (error, data, response) => {
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
 **productModuleNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## listProductModules

> [Netlicensing] listProductModules()

List Product Modules

Return a list of all Product Modules for the current Vendor

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductModuleApi();
apiInstance.listProductModules((error, data, response) => {
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


## updateProductModule

> Netlicensing updateProductModule(productModuleNumber, opts)

Update Product Module

Sets the provided properties to a Product Module. Return an updated Product Module

### Example

```javascript
import Labs64NetLicensingResTfulApiTestCenter from 'labs64_net_licensing_res_tful_api_test_center';
let defaultClient = Labs64NetLicensingResTfulApiTestCenter.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new Labs64NetLicensingResTfulApiTestCenter.ProductModuleApi();
let productModuleNumber = "productModuleNumber_example"; // String | Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product.
let opts = {
  'active': true, // Boolean | If set to 'false', the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module.
  'licenseTemplate': ["'TIMEVOLUME'"], // [String] | License Template. Mandatory for 'Try &amp; Buy' licensing model.
  'licensingModel': "licensingModel_example", // String | Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation.
  'maxCheckoutValidity': 56, // Number | Maximum checkout validity (days). Mandatory for 'Floating' licensing model.
  'name': "name_example", // String | Product Module name that is visible to the end customers in NetLicensing Shop.
  'nodeSecretMode': ["'PREDEFINED'"], // [String] | Secret Mode. Mandatory for 'Node-Locked' licensing model.
  'number': "number_example", // String | New Product Module number (update).
  'redThreshold': 56, // Number | Remaining time volume for red level. Mandatory for 'Rental' licensing model.
  'yellowThreshold': 56 // Number | Remaining time volume for yellow level. Mandatory for 'Rental' licensing model.
};
apiInstance.updateProductModule(productModuleNumber, opts, (error, data, response) => {
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
 **productModuleNumber** | **String**| Unique number (across all Products of a Vendor) that identifies the Product Module. Vendor can assign this number when creating a Product Module or let NetLicensing generate one. Read-only after creation of the first Licensee for the Product. | 
 **active** | **Boolean**| If set to &#39;false&#39;, the Product Module is disabled. Licensees can not obtain any new Licenses for this Product Module. | [optional] 
 **licenseTemplate** | [**[String]**](String.md)| License Template. Mandatory for &#39;Try &amp;amp; Buy&#39; licensing model. | [optional] [default to &#39;TIMEVOLUME&#39;]
 **licensingModel** | **String**| Licensing model applied to this Product Module. Defines what License Templates can be configured for the Product Module and how Licenses for this Product Module are processed during validation. | [optional] 
 **maxCheckoutValidity** | **Number**| Maximum checkout validity (days). Mandatory for &#39;Floating&#39; licensing model. | [optional] 
 **name** | **String**| Product Module name that is visible to the end customers in NetLicensing Shop. | [optional] 
 **nodeSecretMode** | [**[String]**](String.md)| Secret Mode. Mandatory for &#39;Node-Locked&#39; licensing model. | [optional] [default to &#39;PREDEFINED&#39;]
 **number** | **String**| New Product Module number (update). | [optional] 
 **redThreshold** | **Number**| Remaining time volume for red level. Mandatory for &#39;Rental&#39; licensing model. | [optional] 
 **yellowThreshold** | **Number**| Remaining time volume for yellow level. Mandatory for &#39;Rental&#39; licensing model. | [optional] 

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

