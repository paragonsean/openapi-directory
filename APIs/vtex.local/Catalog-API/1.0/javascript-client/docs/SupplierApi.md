# CatalogApi.SupplierApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSupplierPost**](SupplierApi.md#apiCatalogPvtSupplierPost) | **POST** /api/catalog/pvt/supplier | Create Supplier
[**apiCatalogPvtSupplierSupplierIdDelete**](SupplierApi.md#apiCatalogPvtSupplierSupplierIdDelete) | **DELETE** /api/catalog/pvt/supplier/{supplierId} | Delete Supplier
[**apiCatalogPvtSupplierSupplierIdPut**](SupplierApi.md#apiCatalogPvtSupplierSupplierIdPut) | **PUT** /api/catalog/pvt/supplier/{supplierId} | Update Supplier



## apiCatalogPvtSupplierPost

> SupplierResponse apiCatalogPvtSupplierPost(contentType, accept, opts)

Create Supplier

Creates a new Supplier.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SupplierApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'supplierRequest': new CatalogApi.SupplierRequest() // SupplierRequest | 
};
apiInstance.apiCatalogPvtSupplierPost(contentType, accept, opts, (error, data, response) => {
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
 **supplierRequest** | [**SupplierRequest**](SupplierRequest.md)|  | [optional] 

### Return type

[**SupplierResponse**](SupplierResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSupplierSupplierIdDelete

> apiCatalogPvtSupplierSupplierIdDelete(contentType, accept, supplierId)

Delete Supplier

Deletes an existing Supplier.

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

let apiInstance = new CatalogApi.SupplierApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let supplierId = 1; // Number | Supplier's unique numerical identifier.
apiInstance.apiCatalogPvtSupplierSupplierIdDelete(contentType, accept, supplierId, (error, data, response) => {
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
 **supplierId** | **Number**| Supplier&#39;s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSupplierSupplierIdPut

> SupplierResponse apiCatalogPvtSupplierSupplierIdPut(contentType, accept, supplierId, opts)

Update Supplier

Updates general information of an existing Supplier.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SupplierApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let supplierId = 1; // Number | Supplier's unique numerical identifier.
let opts = {
  'supplierRequest': new CatalogApi.SupplierRequest() // SupplierRequest | 
};
apiInstance.apiCatalogPvtSupplierSupplierIdPut(contentType, accept, supplierId, opts, (error, data, response) => {
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
 **supplierId** | **Number**| Supplier&#39;s unique numerical identifier. | 
 **supplierRequest** | [**SupplierRequest**](SupplierRequest.md)|  | [optional] 

### Return type

[**SupplierResponse**](SupplierResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

