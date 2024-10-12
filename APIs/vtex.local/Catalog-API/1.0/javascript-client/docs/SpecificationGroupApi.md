# CatalogApi.SpecificationGroupApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSpecificationgroupGroupIdPut**](SpecificationGroupApi.md#apiCatalogPvtSpecificationgroupGroupIdPut) | **PUT** /api/catalog/pvt/specificationgroup/{groupId} | Update Specification Group
[**specificationGroupInsert2**](SpecificationGroupApi.md#specificationGroupInsert2) | **POST** /api/catalog/pvt/specificationgroup | Create Specification Group
[**specificationsGroupGet**](SpecificationGroupApi.md#specificationsGroupGet) | **GET** /api/catalog_system/pub/specification/groupGet/{groupId} | Get Specification Group
[**specificationsGroupListbyCategory**](SpecificationGroupApi.md#specificationsGroupListbyCategory) | **GET** /api/catalog_system/pvt/specification/groupbycategory/{categoryId} | List Specification Group by Category



## apiCatalogPvtSpecificationgroupGroupIdPut

> ApiCatalogPvtSpecificationgroupGroupIdPut200Response apiCatalogPvtSpecificationgroupGroupIdPut(contentType, accept, groupId, opts)

Update Specification Group

Update a specification group.   &gt;⚠️ It is also possible to update a Specification Group by using an alternative legacy route: &#x60;/api/catalog_system/pvt/specification/group&#x60;.    ## Request and response body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1,      \&quot;Id\&quot;: 17,      \&quot;Name\&quot;: \&quot;NewGroupName\&quot;,      \&quot;Position\&quot;: 1  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationGroupApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let groupId = 1; // Number | Group’s unique numerical identifier.
let opts = {
  'requestBody8': new CatalogApi.RequestBody8() // RequestBody8 | 
};
apiInstance.apiCatalogPvtSpecificationgroupGroupIdPut(contentType, accept, groupId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group’s unique numerical identifier. | 
 **requestBody8** | [**RequestBody8**](RequestBody8.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSpecificationgroupGroupIdPut200Response**](ApiCatalogPvtSpecificationgroupGroupIdPut200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## specificationGroupInsert2

> SpecificationGroupInsert2200Response specificationGroupInsert2(contentType, accept, specificationGroupInsertRequest)

Create Specification Group

Create a specification group.   &gt;⚠️ It is also possible to create a Specification Group by using an alternative legacy route: &#x60;/api/catalog_system/pvt/specification/group&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1,      \&quot;Name\&quot;: \&quot;Sizes\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 6,    \&quot;CategoryId\&quot;: 1,    \&quot;Name\&quot;: \&quot;Sizes\&quot;,    \&quot;Position\&quot;: 3  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationGroupApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationGroupInsertRequest = {"CategoryId":1,"Name":"Sizes"}; // SpecificationGroupInsertRequest | 
apiInstance.specificationGroupInsert2(contentType, accept, specificationGroupInsertRequest, (error, data, response) => {
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
 **specificationGroupInsertRequest** | [**SpecificationGroupInsertRequest**](SpecificationGroupInsertRequest.md)|  | 

### Return type

[**SpecificationGroupInsert2200Response**](SpecificationGroupInsert2200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## specificationsGroupGet

> SpecificationsGroup specificationsGroupGet(contentType, accept, groupId)

Get Specification Group

Retrieves details from a specification group by the ID of the group.   ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;CategoryId\&quot;: 1,    \&quot;Id\&quot;: 6,    \&quot;Name\&quot;: \&quot;Sizes\&quot;,    \&quot;Position\&quot;: 3  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationGroupApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let groupId = "6"; // String | Specification Group ID.
apiInstance.specificationsGroupGet(contentType, accept, groupId, (error, data, response) => {
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
 **groupId** | **String**| Specification Group ID. | 

### Return type

[**SpecificationsGroup**](SpecificationsGroup.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## specificationsGroupListbyCategory

> [SpecificationsGroup] specificationsGroupListbyCategory(contentType, accept, categoryId)

List Specification Group by Category

Retrieves a list of specification groups by the category ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {        \&quot;CategoryId\&quot;: 1,        \&quot;Id\&quot;: 5,        \&quot;Name\&quot;: \&quot;Materials\&quot;,        \&quot;Position\&quot;: 2      },      {        \&quot;CategoryId\&quot;: 1,        \&quot;Id\&quot;: 6,        \&quot;Name\&quot;: \&quot;Sizes\&quot;,        \&quot;Position\&quot;: 3      }    ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationGroupApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let categoryId = "1"; // String | 
apiInstance.specificationsGroupListbyCategory(contentType, accept, categoryId, (error, data, response) => {
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
 **categoryId** | **String**|  | 

### Return type

[**[SpecificationsGroup]**](SpecificationsGroup.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

