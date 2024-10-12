# CatalogApi.LegacyCollectionApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtCollectionCollectionIdDelete**](LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdDelete) | **DELETE** /api/catalog/pvt/collection/{collectionId} | Delete Collection
[**apiCatalogPvtCollectionCollectionIdGet**](LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdGet) | **GET** /api/catalog/pvt/collection/{collectionId} | Get Collection
[**apiCatalogPvtCollectionCollectionIdPut**](LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdPut) | **PUT** /api/catalog/pvt/collection/{collectionId} | Update Collection
[**apiCatalogPvtCollectionPost**](LegacyCollectionApi.md#apiCatalogPvtCollectionPost) | **POST** /api/catalog/pvt/collection | Create Collection



## apiCatalogPvtCollectionCollectionIdDelete

> apiCatalogPvtCollectionCollectionIdDelete(contentType, accept, collectionId)

Delete Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously existing Collection.

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

let apiInstance = new CatalogApi.LegacyCollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 151; // Number | Collection’s unique numerical identifier.
apiInstance.apiCatalogPvtCollectionCollectionIdDelete(contentType, accept, collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtCollectionCollectionIdGet

> ApiCatalogPvtCollectionPost200Response apiCatalogPvtCollectionCollectionIdGet(contentType, accept, collectionId)

Get Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves general information of a Collection.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacyCollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 151; // Number | Collection’s unique numerical identifier.
apiInstance.apiCatalogPvtCollectionCollectionIdGet(contentType, accept, collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection’s unique numerical identifier. | 

### Return type

[**ApiCatalogPvtCollectionPost200Response**](ApiCatalogPvtCollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtCollectionCollectionIdPut

> ApiCatalogPvtCollectionPost200Response apiCatalogPvtCollectionCollectionIdPut(contentType, accept, collectionId, opts)

Update Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacyCollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 151; // Number | Collection’s unique numerical identifier.
let opts = {
  'resquestBody1': new CatalogApi.ResquestBody1() // ResquestBody1 | 
};
apiInstance.apiCatalogPvtCollectionCollectionIdPut(contentType, accept, collectionId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection’s unique numerical identifier. | 
 **resquestBody1** | [**ResquestBody1**](ResquestBody1.md)|  | [optional] 

### Return type

[**ApiCatalogPvtCollectionPost200Response**](ApiCatalogPvtCollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtCollectionPost

> ApiCatalogPvtCollectionPost200Response apiCatalogPvtCollectionPost(contentType, accept, opts)

Create Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacyCollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'resquestBody': new CatalogApi.ResquestBody() // ResquestBody | 
};
apiInstance.apiCatalogPvtCollectionPost(contentType, accept, opts, (error, data, response) => {
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
 **resquestBody** | [**ResquestBody**](ResquestBody.md)|  | [optional] 

### Return type

[**ApiCatalogPvtCollectionPost200Response**](ApiCatalogPvtCollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

