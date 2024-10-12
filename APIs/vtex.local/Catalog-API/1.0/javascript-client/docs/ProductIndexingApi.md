# CatalogApi.ProductIndexingApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indexedInfo**](ProductIndexingApi.md#indexedInfo) | **GET** /api/catalog_system/pvt/products/GetIndexedInfo/{productId} | Get Product Indexed Information



## indexedInfo

> indexedInfo(contentType, accept, productId)

Get Product Indexed Information

Retrieve details of a Product&#39;s Indexed Information in XML format.   ## Response body example    &#x60;&#x60;&#x60;xml  \&quot;  &lt;?xml version&#x3D;\\\&quot;1.0\\\&quot; encoding&#x3D;\\\&quot;UTF-8\\\&quot;?&gt;\\n  &lt;response&gt;\\n      &lt;lst name&#x3D;\\\&quot;responseHeader\\\&quot;&gt;          &lt;bool name&#x3D;\\\&quot;zkConnected\\\&quot;&gt;true&lt;/bool&gt;          &lt;int name&#x3D;\\\&quot;status\\\&quot;&gt;0&lt;/int&gt;          &lt;int name&#x3D;\\\&quot;QTime\\\&quot;&gt;2&lt;/int&gt;          &lt;lst name&#x3D;\\\&quot;params\\\&quot;&gt;              &lt;str name&#x3D;\\\&quot;fl\\\&quot;&gt;*&lt;/str&gt;              &lt;arr name&#x3D;\\\&quot;fq\\\&quot;&gt;                  &lt;str&gt;instanceId:394dbdc8-b1f4-4dea-adfa-1ec104f3bfe1&lt;/str&gt;                  &lt;str&gt;productId:1&lt;/str&gt;              &lt;/arr&gt;          &lt;/lst&gt;      &lt;/lst&gt;      &lt;result name&#x3D;\\\&quot;response\\\&quot; numFound&#x3D;\\\&quot;0\\\&quot; start&#x3D;\\\&quot;0\\\&quot; maxScore&#x3D;\\\&quot;0.0\\\&quot;&gt;&lt;/result&gt;      &lt;lst name&#x3D;\\\&quot;facet_counts\\\&quot;&gt;          &lt;lst name&#x3D;\\\&quot;facet_queries\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_fields\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_ranges\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_intervals\\\&quot;/&gt;          &lt;lst name&#x3D;\\\&quot;facet_heatmaps\\\&quot;/&gt;&lt;/lst&gt;\\n  &lt;/response&gt;\\n\&quot;  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.ProductIndexingApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = "1"; // String | Product’s unique numerical identifier.
apiInstance.indexedInfo(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **String**| Product’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: xml

