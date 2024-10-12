# MasterDataApiV1.ScoreApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletescorebyfield**](ScoreApi.md#deletescorebyfield) | **DELETE** /api/dataentities/{acronym}/documents/{id}/score/{field-name} | Delete score by field
[**putscorebyfield**](ScoreApi.md#putscorebyfield) | **PUT** /api/dataentities/{acronym}/documents/{id}/score/{field-name} | Put score by field
[**putscores**](ScoreApi.md#putscores) | **PUT** /api/dataentities/{acronym}/documents/{id}/score | Put scores



## deletescorebyfield

> deletescorebyfield(accept, acronym, id, fieldName, deletescorebyfieldRequest)

Delete score by field

Allows you to remove a key from a specific field.

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

let apiInstance = new MasterDataApiV1.ScoreApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let fieldName = "'{{field-name}}'"; // String | Name of the field to remove score from
let deletescorebyfieldRequest = {"key":"first key"}; // DeletescorebyfieldRequest | 
apiInstance.deletescorebyfield(accept, acronym, id, fieldName, deletescorebyfieldRequest, (error, data, response) => {
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
 **fieldName** | **String**| Name of the field to remove score from | [default to &#39;{{field-name}}&#39;]
 **deletescorebyfieldRequest** | [**DeletescorebyfieldRequest**](DeletescorebyfieldRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putscorebyfield

> putscorebyfield(accept, acronym, id, fieldName, putscorebyfieldRequest)

Put score by field

It allows to punctuate in a specific field.

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

let apiInstance = new MasterDataApiV1.ScoreApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let fieldName = "'{{field-name}}'"; // String | Name of the field to score
let putscorebyfieldRequest = {"key":"first key","point":1,"until":"10m"}; // PutscorebyfieldRequest | 
apiInstance.putscorebyfield(accept, acronym, id, fieldName, putscorebyfieldRequest, (error, data, response) => {
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
 **fieldName** | **String**| Name of the field to score | [default to &#39;{{field-name}}&#39;]
 **putscorebyfieldRequest** | [**PutscorebyfieldRequest**](PutscorebyfieldRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## putscores

> putscores(accept, acronym, id, putscoresRequest)

Put scores

It allows punctuate in more than one field and more than one key.

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

let apiInstance = new MasterDataApiV1.ScoreApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let putscoresRequest = [{"field":"carttag","key":"Payment","point":1,"until":"10m"},{"field":"scoretest","key":"Point 1","point":1,"until":"1d"}]; // [PutscoresRequest] | 
apiInstance.putscores(accept, acronym, id, putscoresRequest, (error, data, response) => {
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
 **putscoresRequest** | [**[PutscoresRequest]**](PutscoresRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

