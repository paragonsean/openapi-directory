# CatalogApiSellerPortal.SKUApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSKU**](SKUApi.md#listSKU) | **GET** /api/catalog-seller-portal/skus/ids | Get List of SKUs
[**searchSKU**](SKUApi.md#searchSKU) | **GET** /api/catalog-seller-portal/skus/_search | Search for SKU



## listSKU

> ListSKU200Response listSKU(contentType, accept, opts)

Get List of SKUs

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about all SKUs.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;data\&quot;: [          \&quot;1\&quot;,          \&quot;10\&quot;,          \&quot;11\&quot;,          \&quot;12\&quot;,          \&quot;13\&quot;,          \&quot;14\&quot;,          \&quot;15\&quot;,          \&quot;16\&quot;,          \&quot;19\&quot;,          \&quot;2\&quot;,          \&quot;20\&quot;,          \&quot;21\&quot;,          \&quot;22\&quot;,          \&quot;23\&quot;,          \&quot;24\&quot;      ],      \&quot;_metadata\&quot;: {          \&quot;total\&quot;: 65,          \&quot;from\&quot;: 1,          \&quot;to\&quot;: 15      }  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
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

let apiInstance = new CatalogApiSellerPortal.SKUApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'from': "1", // String | The first page of the interval of the product list.
  'to': "50" // String | The last page of the interval of the product list.
};
apiInstance.listSKU(contentType, accept, opts, (error, data, response) => {
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
 **from** | **String**| The first page of the interval of the product list. | [optional] 
 **to** | **String**| The last page of the interval of the product list. | [optional] 

### Return type

[**ListSKU200Response**](ListSKU200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchSKU

> SearchSKU200Response searchSKU(contentType, accept, opts)

Search for SKU

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about an SKU taking into consideration the defined search criteria. It is mandatory to use at least one query parameter.     ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;data\&quot;: [      {        \&quot;id\&quot;: \&quot;2\&quot;,        \&quot;productId\&quot;: \&quot;2\&quot;,        \&quot;externalId\&quot;: \&quot;1909621862\&quot;      }    ],    \&quot;_metadata\&quot;: {      \&quot;total\&quot;: 1,      \&quot;from\&quot;: 1,      \&quot;to\&quot;: 15    }  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
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

let apiInstance = new CatalogApiSellerPortal.SKUApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'from': "1", // String | The first page of the interval of the product list.
  'to': "50", // String | The last page of the interval of the product list.
  'id': 1, // Number | SKU unique idenfier number.
  'externalid': 123456789 // Number | SKU reference unique identifier number in the store.
};
apiInstance.searchSKU(contentType, accept, opts, (error, data, response) => {
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
 **from** | **String**| The first page of the interval of the product list. | [optional] 
 **to** | **String**| The last page of the interval of the product list. | [optional] 
 **id** | **Number**| SKU unique idenfier number. | [optional] 
 **externalid** | **Number**| SKU reference unique identifier number in the store. | [optional] 

### Return type

[**SearchSKU200Response**](SearchSKU200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

