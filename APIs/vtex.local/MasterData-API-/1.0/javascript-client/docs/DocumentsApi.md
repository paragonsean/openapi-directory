# MasterDataApiV1.DocumentsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createnewdocument**](DocumentsApi.md#createnewdocument) | **POST** /api/dataentities/{acronym}/documents | Create new document
[**createorupdateentiredocument**](DocumentsApi.md#createorupdateentiredocument) | **PUT** /api/dataentities/{acronym}/documents | Create or update entire document
[**createorupdatepartialdocument**](DocumentsApi.md#createorupdatepartialdocument) | **PATCH** /api/dataentities/{acronym}/documents | Create or update partial document
[**deletedocument**](DocumentsApi.md#deletedocument) | **DELETE** /api/dataentities/{acronym}/documents/{id} | Delete document
[**getdocument**](DocumentsApi.md#getdocument) | **GET** /api/dataentities/{acronym}/documents/{id} | Get document
[**updateentiredocument**](DocumentsApi.md#updateentiredocument) | **PUT** /api/dataentities/{acronym}/documents/{id} | Update entire document
[**updatepartialdocument**](DocumentsApi.md#updatepartialdocument) | **PATCH** /api/dataentities/{acronym}/documents/{id} | Update partial document



## createnewdocument

> Createnewdocument createnewdocument(accept, acronym, body)

Create new document

Creates documents through a JSON object where the key is the name of the field.

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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Identifies the kind of data
let body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."}; // Object | 
apiInstance.createnewdocument(accept, acronym, body, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to &#39;application/vnd.vtex.ds.v10+json&#39;]
 **acronym** | **String**| Identifies the kind of data | [default to &#39;{{acronym}}&#39;]
 **body** | **Object**|  | 

### Return type

[**Createnewdocument**](Createnewdocument.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createorupdateentiredocument

> createorupdateentiredocument(accept, acronym, body)

Create or update entire document



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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Identifies the kind of data
let body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit.... ","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","id":"4e4c55ac-e491-11e6-94f4-0ac138d2d42e"}; // Object | 
apiInstance.createorupdateentiredocument(accept, acronym, body, (error, data, response) => {
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
 **acronym** | **String**| Identifies the kind of data | [default to &#39;{{acronym}}&#39;]
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createorupdatepartialdocument

> createorupdatepartialdocument(accept, acronym, body)

Create or update partial document



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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Identifies the kind of data
let body = {"Boolean":true,"id":"4e4c55ac-e491-11e6-94f4-0ac138d2d42e"}; // Object | 
apiInstance.createorupdatepartialdocument(accept, acronym, body, (error, data, response) => {
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
 **acronym** | **String**| Identifies the kind of data | [default to &#39;{{acronym}}&#39;]
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deletedocument

> deletedocument(contentType, accept, acronym, id)

Delete document

It allows to delete a document.

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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
apiInstance.deletedocument(contentType, accept, acronym, id, (error, data, response) => {
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
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getdocument

> Usingfilters getdocument(contentType, accept, acronym, id)

Get document

Retrieves a document.    Assign the &#x60;_fields&#x60; parameter in the query string to retrieve the desired fields. If you want to return all the fields use &#x60;_fields&#x3D;_all&#x60;.

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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let contentType = "'application/json'"; // String | Type of the content being sent
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
apiInstance.getdocument(contentType, accept, acronym, id, (error, data, response) => {
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
 **acronym** | **String**| Two letter word that identifies the data structure | [default to &#39;{{acronym}}&#39;]
 **id** | **String**| Id of the document | [default to &#39;{{id}}&#39;]

### Return type

[**Usingfilters**](Usingfilters.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateentiredocument

> updateentiredocument(accept, acronym, id, body)

Update entire document



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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let body = {"Boolean":true,"Currency":2.5,"Date":"1992-11-17","Date_Time":"2016-09-14T19:21:01.3163733Z","Decimal":2.5,"Email":"meu@email.com","Integer":1000000,"Long":1000000000,"Percent":85.42,"Relationship":"5eb31afb-7ab0-11e6-94b4-0a44686e393f","Text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Time":1430,"URL":"http://www.vtex.com","Varchar10":"Lorem ipsu","Varchar100":"Lorem ipsum dolor sit amet, consectetur adipiscing elit...","Varchar50":"Lorem ipsum dolor sit amet, consectetur adipiscing","Varchar750":"Lorem ipsum dolor sit amet, consectetur adipiscing elit..."}; // Object | 
apiInstance.updateentiredocument(accept, acronym, id, body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatepartialdocument

> updatepartialdocument(accept, acronym, id, body)

Update partial document



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

let apiInstance = new MasterDataApiV1.DocumentsApi();
let accept = "'application/vnd.vtex.ds.v10+json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let acronym = "'{{acronym}}'"; // String | Two letter word that identifies the data structure
let id = "'{{id}}'"; // String | Id of the document
let body = {"Boolean":false}; // Object | 
apiInstance.updatepartialdocument(accept, acronym, id, body, (error, data, response) => {
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
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

