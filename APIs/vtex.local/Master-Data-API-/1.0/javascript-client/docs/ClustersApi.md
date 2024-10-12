# MasterDataApiV2.ClustersApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validatedocumentbyclusters**](ClustersApi.md#validatedocumentbyclusters) | **POST** /api/dataentities/{dataEntityName}/documents/{id}/clusters | Validate document by clusters



## validatedocumentbyclusters

> validatedocumentbyclusters(dataEntityName, accept, id, body)

Validate document by clusters

Check if a document is present in one or more clusters (specific set of field values).    &gt; There is a limit of five rules per request.

### Example

```javascript
import MasterDataApiV2 from 'master_data_api_v2';
let defaultClient = MasterDataApiV2.ApiClient.instance;
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

let apiInstance = new MasterDataApiV2.ClustersApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
let body = [
    {
        "name": "male",        
        "rule": "gender=male"
    },
    {
        "name": "complex",
        "rule": "((gender=male AND percent=0.35) AND any is null) AND (name=*go*)"
    },    
    {
        "name": "complex2",
        "rule": "((gender=male AND percent=0.35) AND any is not null) OR (name=*go*)"
    },
    {
        "name": "createdIn",
        "rule": "createdIn between 2015-10-28 AND 2015-10-30"
    }
]; // String | Request body for validating a document by clusters
apiInstance.validatedocumentbyclusters(dataEntityName, accept, id, body, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 
 **body** | **String**| Request body for validating a document by clusters | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

