# CatalogApi.SpecificationValueApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSpecificationvaluePost**](SpecificationValueApi.md#apiCatalogPvtSpecificationvaluePost) | **POST** /api/catalog/pvt/specificationvalue | Create Specification Value
[**apiCatalogPvtSpecificationvalueSpecificationValueIdGet**](SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdGet) | **GET** /api/catalog/pvt/specificationvalue/{specificationValueId} | Get Specification Value
[**apiCatalogPvtSpecificationvalueSpecificationValueIdPut**](SpecificationValueApi.md#apiCatalogPvtSpecificationvalueSpecificationValueIdPut) | **PUT** /api/catalog/pvt/specificationvalue/{specificationValueId} | Update Specification Value



## apiCatalogPvtSpecificationvaluePost

> ApiCatalogPvtSpecificationvaluePost200Response apiCatalogPvtSpecificationvaluePost(contentType, accept, opts)

Create Specification Value

Creates a new Specification Value for a Category.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 193,      \&quot;Name\&quot;: \&quot;Metal\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 1    }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;FieldValueId\&quot;: 360,    \&quot;FieldId\&quot;: 193,    \&quot;Name\&quot;: \&quot;Metal\&quot;,    \&quot;Text\&quot;: null,    \&quot;IsActive\&quot;: true,    \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationValueApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'apiCatalogPvtSpecificationvaluePostRequest': new CatalogApi.ApiCatalogPvtSpecificationvaluePostRequest() // ApiCatalogPvtSpecificationvaluePostRequest | 
};
apiInstance.apiCatalogPvtSpecificationvaluePost(contentType, accept, opts, (error, data, response) => {
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
 **apiCatalogPvtSpecificationvaluePostRequest** | [**ApiCatalogPvtSpecificationvaluePostRequest**](ApiCatalogPvtSpecificationvaluePostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSpecificationvaluePost200Response**](ApiCatalogPvtSpecificationvaluePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSpecificationvalueSpecificationValueIdGet

> ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response apiCatalogPvtSpecificationvalueSpecificationValueIdGet(contentType, accept, specificationValueId)

Get Specification Value

Retrieves general information about a Specification Value.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationValueApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationValueId = 143; // Number | Specification Value’s unique numerical identifier.
apiInstance.apiCatalogPvtSpecificationvalueSpecificationValueIdGet(contentType, accept, specificationValueId, (error, data, response) => {
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
 **specificationValueId** | **Number**| Specification Value’s unique numerical identifier. | 

### Return type

[**ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response**](ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSpecificationvalueSpecificationValueIdPut

> ApiCatalogPvtSpecificationvaluePost200Response apiCatalogPvtSpecificationvalueSpecificationValueIdPut(contentType, accept, specificationValueId, opts)

Update Specification Value

Updates a new Specification Value for a Category.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 193,      \&quot;Name\&quot;: \&quot;Metal\&quot;,      \&quot;Text\&quot;: null,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 1    }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;FieldValueId\&quot;: 360,    \&quot;FieldId\&quot;: 193,    \&quot;Name\&quot;: \&quot;Metal\&quot;,    \&quot;Text\&quot;: null,    \&quot;IsActive\&quot;: true,    \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationValueApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationValueId = 1; // Number |  Specification Value’s unique numerical identifier.
let opts = {
  'apiCatalogPvtSpecificationvaluePostRequest': new CatalogApi.ApiCatalogPvtSpecificationvaluePostRequest() // ApiCatalogPvtSpecificationvaluePostRequest | 
};
apiInstance.apiCatalogPvtSpecificationvalueSpecificationValueIdPut(contentType, accept, specificationValueId, opts, (error, data, response) => {
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
 **specificationValueId** | **Number**|  Specification Value’s unique numerical identifier. | 
 **apiCatalogPvtSpecificationvaluePostRequest** | [**ApiCatalogPvtSpecificationvaluePostRequest**](ApiCatalogPvtSpecificationvaluePostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSpecificationvaluePost200Response**](ApiCatalogPvtSpecificationvaluePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

