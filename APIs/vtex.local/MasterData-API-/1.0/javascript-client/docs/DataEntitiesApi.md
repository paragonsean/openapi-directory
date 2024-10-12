# MasterDataApiV1.DataEntitiesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getdataentitystructure**](DataEntitiesApi.md#getdataentitystructure) | **GET** /api/dataentities/{acronym} | Get data entity structure
[**listdataentities**](DataEntitiesApi.md#listdataentities) | **GET** /api/dataentities | List data entities



## getdataentitystructure

> Getdataentityfields getdataentitystructure(contentType, accept, acronym)

Get data entity structure

Returns the data entity structure with its respective fields and data type.    ### Response status code    1. Status Code &#x60;403&#x60;: Access not allowed  2. Status Code &#x60;200&#x60;: Retrieves data entity structure    &gt; All headers listed below are required.

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

let apiInstance = new MasterDataApiV1.DataEntitiesApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Identifies the kind of data
apiInstance.getdataentitystructure(contentType, accept, acronym, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Identifies the kind of data | [default to &#39;{{acronym}}&#39;]

### Return type

[**Getdataentityfields**](Getdataentityfields.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listdataentities

> [Listdataentity] listdataentities(contentType, accept)

List data entities

Retrieves the list of existing data entities in the store.    ### Response status code    1. Status Code &#x60;403&#x60;: Access not allowed  2. Status Code &#x60;200&#x60;: Retrieves data entity list    &gt; All headers listed below are required.

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

let apiInstance = new MasterDataApiV1.DataEntitiesApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
apiInstance.listdataentities(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]

### Return type

[**[Listdataentity]**](Listdataentity.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

