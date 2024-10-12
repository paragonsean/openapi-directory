# MasterDataApiV1.SearchApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchdocuments**](SearchApi.md#searchdocuments) | **GET** /api/dataentities/{acronym}/search | Search documents



## searchdocuments

> searchdocuments(contentType, accept, rESTRange, acronym, opts)

Search documents

Search documents by the query parameters described below.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;503&#x60;.

### Example

```javascript
import MasterDataApiV1 from 'master_data_api_v1';
let defaultClient = MasterDataApiV1.ApiClient.instance;
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

let apiInstance = new MasterDataApiV1.SearchApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let rESTRange = "'resources=0-10'"; // String | Range of documents to show
let acronym = "'{{acronym}}'"; // String | Identifies the kind of data
let opts = {
  'fields': "'email,firstName,document'", // String | Fields that will be returned by document
  'where': "'firstName is not null'", // String | Specification of filters. As seen below
  'schema': "'{{schema}}'", // String | Enter with the name of the schema to filter documents by compatibility of the schema.
  'keyword': "'String to search'", // String | String to search
  'sort': "'firstName ASC'" // String | Use ASC value to sort ascending or DESC value to sort descending. 
};
apiInstance.searchdocuments(contentType, accept, rESTRange, acronym, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **rESTRange** | **String**| Range of documents to show | [default to &#39;resources&#x3D;0-10&#39;]
 **acronym** | **String**| Identifies the kind of data | [default to &#39;{{acronym}}&#39;]
 **fields** | **String**| Fields that will be returned by document | [optional] [default to &#39;email,firstName,document&#39;]
 **where** | **String**| Specification of filters. As seen below | [optional] [default to &#39;firstName is not null&#39;]
 **schema** | **String**| Enter with the name of the schema to filter documents by compatibility of the schema. | [optional] [default to &#39;{{schema}}&#39;]
 **keyword** | **String**| String to search | [optional] [default to &#39;String to search&#39;]
 **sort** | **String**| Use ASC value to sort ascending or DESC value to sort descending.  | [optional] [default to &#39;firstName ASC&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

