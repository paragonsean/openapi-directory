# CatalogApi.BrandApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtBrandBrandIdDelete**](BrandApi.md#apiCatalogPvtBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/brand/{brandId} | Delete Brand
[**apiCatalogPvtBrandBrandIdGet**](BrandApi.md#apiCatalogPvtBrandBrandIdGet) | **GET** /api/catalog/pvt/brand/{brandId} | Get Brand and context
[**apiCatalogPvtBrandBrandIdPut**](BrandApi.md#apiCatalogPvtBrandBrandIdPut) | **PUT** /api/catalog/pvt/brand/{brandId} | Update Brand
[**apiCatalogPvtBrandPost**](BrandApi.md#apiCatalogPvtBrandPost) | **POST** /api/catalog/pvt/brand | Create Brand
[**brand**](BrandApi.md#brand) | **GET** /api/catalog_system/pvt/brand/{brandId} | Get Brand
[**brandList**](BrandApi.md#brandList) | **GET** /api/catalog_system/pvt/brand/list | Get Brand List
[**brandListPerPage**](BrandApi.md#brandListPerPage) | **GET** /api/catalog_system/pvt/brand/pagedlist | Get Brand List Per Page



## apiCatalogPvtBrandBrandIdDelete

> apiCatalogPvtBrandBrandIdDelete(brandId, contentType, accept)

Delete Brand

Deletes an existing Brand.

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

let apiInstance = new CatalogApi.BrandApi();
let brandId = "123"; // String | Brand’s unique numerical identifier.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.apiCatalogPvtBrandBrandIdDelete(brandId, contentType, accept, (error, data, response) => {
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
 **brandId** | **String**| Brand’s unique numerical identifier. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtBrandBrandIdGet

> BrandCreateUpdate apiCatalogPvtBrandBrandIdGet(contentType, accept, brandId)

Get Brand and context

Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.BrandApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let brandId = "123"; // String | Brand ID.
apiInstance.apiCatalogPvtBrandBrandIdGet(contentType, accept, brandId, (error, data, response) => {
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
 **brandId** | **String**| Brand ID. | 

### Return type

[**BrandCreateUpdate**](BrandCreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtBrandBrandIdPut

> BrandCreateUpdate apiCatalogPvtBrandBrandIdPut(brandId, contentType, accept, opts)

Update Brand

Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.BrandApi();
let brandId = "123"; // String | Brand’s unique numerical identifier.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'brandCreateUpdate': new CatalogApi.BrandCreateUpdate() // BrandCreateUpdate | 
};
apiInstance.apiCatalogPvtBrandBrandIdPut(brandId, contentType, accept, opts, (error, data, response) => {
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
 **brandId** | **String**| Brand’s unique numerical identifier. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **brandCreateUpdate** | [**BrandCreateUpdate**](BrandCreateUpdate.md)|  | [optional] 

### Return type

[**BrandCreateUpdate**](BrandCreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtBrandPost

> BrandCreateUpdate apiCatalogPvtBrandPost(contentType, accept, opts)

Create Brand

Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.BrandApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'brandCreateUpdate': new CatalogApi.BrandCreateUpdate() // BrandCreateUpdate | Request body.
};
apiInstance.apiCatalogPvtBrandPost(contentType, accept, opts, (error, data, response) => {
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
 **brandCreateUpdate** | [**BrandCreateUpdate**](BrandCreateUpdate.md)| Request body. | [optional] 

### Return type

[**BrandCreateUpdate**](BrandCreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## brand

> BrandGet brand(contentType, accept, brandId)

Get Brand

Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.BrandApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let brandId = "123"; // String | Brand ID.
apiInstance.brand(contentType, accept, brandId, (error, data, response) => {
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
 **brandId** | **String**| Brand ID. | 

### Return type

[**BrandGet**](BrandGet.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## brandList

> [BrandGet] brandList(contentType, accept)

Get Brand List

Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.BrandApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.brandList(contentType, accept, (error, data, response) => {
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

### Return type

[**[BrandGet]**](BrandGet.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## brandListPerPage

> BrandListPerPage200Response brandListPerPage(contentType, accept, pageSize, page)

Get Brand List Per Page

Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.BrandApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let pageSize = 5; // Number | Quantity of brands per page.
let page = 1; // Number | Page number of the brand list.
apiInstance.brandListPerPage(contentType, accept, pageSize, page, (error, data, response) => {
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
 **pageSize** | **Number**| Quantity of brands per page. | 
 **page** | **Number**| Page number of the brand list. | 

### Return type

[**BrandListPerPage200Response**](BrandListPerPage200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

