# KnowledgeGraphSearchApi.EntitiesApi

All URIs are relative to *https://kgsearch.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kgsearchEntitiesSearch**](EntitiesApi.md#kgsearchEntitiesSearch) | **GET** /v1/entities:search | 



## kgsearchEntitiesSearch

> SearchResponse kgsearchEntitiesSearch(opts)



Searches Knowledge Graph for entities that match the constraints. A list of matched entities will be returned in response, which will be in JSON-LD format and compatible with http://schema.org

### Example

```javascript
import KnowledgeGraphSearchApi from 'knowledge_graph_search_api';

let apiInstance = new KnowledgeGraphSearchApi.EntitiesApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'ids': ["null"], // [String] | The list of entity id to be used for search instead of query string. To specify multiple ids in the HTTP request, repeat the parameter in the URL as in ...?ids=A&ids=B
  'indent': true, // Boolean | Enables indenting of json results.
  'languages': ["null"], // [String] | The list of language codes (defined in ISO 693) to run the query with, e.g. 'en'.
  'limit': 56, // Number | Limits the number of entities to be returned.
  'prefix': true, // Boolean | Enables prefix match against names and aliases of entities
  'query': "query_example", // String | The literal query string for search.
  'types': ["null"] // [String] | Restricts returned entities with these types, e.g. Person (as defined in http://schema.org/Person). If multiple types are specified, returned entities will contain one or more of these types.
};
apiInstance.kgsearchEntitiesSearch(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **ids** | [**[String]**](String.md)| The list of entity id to be used for search instead of query string. To specify multiple ids in the HTTP request, repeat the parameter in the URL as in ...?ids&#x3D;A&amp;ids&#x3D;B | [optional] 
 **indent** | **Boolean**| Enables indenting of json results. | [optional] 
 **languages** | [**[String]**](String.md)| The list of language codes (defined in ISO 693) to run the query with, e.g. &#39;en&#39;. | [optional] 
 **limit** | **Number**| Limits the number of entities to be returned. | [optional] 
 **prefix** | **Boolean**| Enables prefix match against names and aliases of entities | [optional] 
 **query** | **String**| The literal query string for search. | [optional] 
 **types** | [**[String]**](String.md)| Restricts returned entities with these types, e.g. Person (as defined in http://schema.org/Person). If multiple types are specified, returned entities will contain one or more of these types. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

