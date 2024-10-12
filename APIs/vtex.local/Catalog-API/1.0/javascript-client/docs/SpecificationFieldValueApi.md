# CatalogApi.SpecificationFieldValueApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**specificationsGetFieldValue**](SpecificationFieldValueApi.md#specificationsGetFieldValue) | **GET** /api/catalog_system/pvt/specification/fieldValue/{fieldValueId} | Get Specification Field Value
[**specificationsInsertFieldValue**](SpecificationFieldValueApi.md#specificationsInsertFieldValue) | **POST** /api/catalog_system/pvt/specification/fieldValue | Create Specification Field Value
[**specificationsUpdateFieldValue**](SpecificationFieldValueApi.md#specificationsUpdateFieldValue) | **PUT** /api/catalog_system/pvt/specification/fieldValue | Update Specification Field Value
[**specificationsValuesByFieldId**](SpecificationFieldValueApi.md#specificationsValuesByFieldId) | **GET** /api/catalog_system/pub/specification/fieldvalue/{fieldId} | Get Specification Values By Field ID



## specificationsGetFieldValue

> ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response specificationsGetFieldValue(contentType, accept, fieldValueId)

Get Specification Field Value

Retrieves details from a specification field&#39;s value by this value&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-specification-value-id) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;TesteInsert\&quot;,      \&quot;Text\&quot;: \&quot;Value Description\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationFieldValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let fieldValueId = "143"; // String | 
apiInstance.specificationsGetFieldValue(contentType, accept, fieldValueId, (error, data, response) => {
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
 **fieldValueId** | **String**|  | 

### Return type

[**ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response**](ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## specificationsInsertFieldValue

> ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response specificationsInsertFieldValue(contentType, accept, specificationsInsertFieldValueRequest)

Create Specification Field Value

Creates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification-value) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldValueId\&quot;: 143,      \&quot;FieldId\&quot;: 34,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationFieldValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationsInsertFieldValueRequest = {"FieldId":34,"IsActive":true,"Name":"Cotton","Position":100,"Text":"Cotton fibers"}; // SpecificationsInsertFieldValueRequest | 
apiInstance.specificationsInsertFieldValue(contentType, accept, specificationsInsertFieldValueRequest, (error, data, response) => {
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
 **specificationsInsertFieldValueRequest** | [**SpecificationsInsertFieldValueRequest**](SpecificationsInsertFieldValueRequest.md)|  | 

### Return type

[**ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response**](ApiCatalogPvtSpecificationvalueSpecificationValueIdGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## specificationsUpdateFieldValue

> String specificationsUpdateFieldValue(contentType, accept, specificationsUpdateFieldValueRequest)

Update Specification Field Value

Updates a specification field value by the specification field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification Field Value](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification-value-id) instead.      ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 1,      \&quot;FieldValueId\&quot;: 143,      \&quot;Name\&quot;: \&quot;Cotton\&quot;,      \&quot;Text\&quot;: \&quot;Cotton fibers\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;Position\&quot;: 100  }  &#x60;&#x60;&#x60;    ## Response body example (200 OK)    &#x60;&#x60;&#x60;json  \&quot;Field Value Updated\&quot;  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationFieldValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationsUpdateFieldValueRequest = {"FieldId":1,"FieldValueId":143,"IsActive":true,"Name":"Cotton","Position":100,"Text":"Cotton fibers"}; // SpecificationsUpdateFieldValueRequest | 
apiInstance.specificationsUpdateFieldValue(contentType, accept, specificationsUpdateFieldValueRequest, (error, data, response) => {
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
 **specificationsUpdateFieldValueRequest** | [**SpecificationsUpdateFieldValueRequest**](SpecificationsUpdateFieldValueRequest.md)|  | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## specificationsValuesByFieldId

> [GetSpecFieldValue] specificationsValuesByFieldId(contentType, accept, fieldId)

Get Specification Values By Field ID

Gets a list of all specification values from a Specification Field by this field&#39;s ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;FieldValueId\&quot;: 52,          \&quot;Value\&quot;: \&quot;0 a 6 meses\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 1      },      {          \&quot;FieldValueId\&quot;: 53,          \&quot;Value\&quot;: \&quot;1 a 2 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 4      },      {          \&quot;FieldValueId\&quot;: 54,          \&quot;Value\&quot;: \&quot;3 a 4 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 3      },      {          \&quot;FieldValueId\&quot;: 55,          \&quot;Value\&quot;: \&quot;5 a 6 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 2      },      {          \&quot;FieldValueId\&quot;: 56,          \&quot;Value\&quot;: \&quot;7 a 8 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 5      },      {          \&quot;FieldValueId\&quot;: 57,          \&quot;Value\&quot;: \&quot;9 a 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 6      },      {          \&quot;FieldValueId\&quot;: 58,          \&quot;Value\&quot;: \&quot;Acima de 10 anos\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;Position\&quot;: 7      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationFieldValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let fieldId = 34; // Number | Specification Field ID.
apiInstance.specificationsValuesByFieldId(contentType, accept, fieldId, (error, data, response) => {
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
 **fieldId** | **Number**| Specification Field ID. | 

### Return type

[**[GetSpecFieldValue]**](GetSpecFieldValue.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

