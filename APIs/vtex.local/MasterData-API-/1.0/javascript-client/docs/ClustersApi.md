# MasterDataApiV1.ClustersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validateDocumentbyClusters**](ClustersApi.md#validateDocumentbyClusters) | **POST** /api/dataentities/{acronym}/documents/{id}/clusters | Validate Document by Clusters



## validateDocumentbyClusters

> validateDocumentbyClusters(accept, acronym, id, requestBody)

Validate Document by Clusters



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

let apiInstance = new MasterDataApiV1.ClustersApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let requestBody = [{"name":"male","rule":"gender=male"},{"name":"complex","rule":"((gender=male AND percent=0.35) AND any is null) AND (name=*go*)"},{"name":"complex2","rule":"((gender=male AND percent=0.35) AND any is not null) OR (name=*go*)"},{"name":"createdIn","rule":"createdIn between 2015-10-28 AND 2015-10-30"}]; // [Object] | 
apiInstance.validateDocumentbyClusters(accept, acronym, id, requestBody, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]
 **requestBody** | [**[Object]**](Object.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

