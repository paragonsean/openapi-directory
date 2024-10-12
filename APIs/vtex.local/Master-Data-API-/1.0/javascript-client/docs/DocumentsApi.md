# MasterDataApiV2.DocumentsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createnewdocument**](DocumentsApi.md#createnewdocument) | **POST** /api/dataentities/{dataEntityName}/documents | Create new document
[**createorupdatepartialdocument**](DocumentsApi.md#createorupdatepartialdocument) | **PATCH** /api/dataentities/{dataEntityName}/documents | Create partial document
[**deletedocument**](DocumentsApi.md#deletedocument) | **DELETE** /api/dataentities/{dataEntityName}/documents/{id} | Delete document
[**getdocument**](DocumentsApi.md#getdocument) | **GET** /api/dataentities/{dataEntityName}/documents/{id} | Get document
[**updateentiredocument**](DocumentsApi.md#updateentiredocument) | **PUT** /api/dataentities/{dataEntityName}/documents/{id} | Update entire document
[**updatepartialdocument**](DocumentsApi.md#updatepartialdocument) | **PATCH** /api/dataentities/{dataEntityName}/documents/{id} | Update partial document



## createnewdocument

> DocumentResponse createnewdocument(contentType, accept, dataEntityName, requestBody, opts)

Create new document

This request allows you to create a new document corresponding to a given data entity. For example, you can create a new customer profile or address.    &gt; You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to create.    ## Example use cases    ### Client profile    In order to create a new customer profile, choose the &#x60;CL&#x60; data entity and send a request similar to this:    POST  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;email\&quot;: \&quot;clark.kent@examplemail.com\&quot;,      \&quot;firstName\&quot;: \&quot;Clark\&quot;,      \&quot;lastName\&quot;: \&quot;Kent\&quot;,      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;documentType\&quot;: \&quot;CPF\&quot;,      \&quot;document\&quot;: \&quot;12345678900\&quot;      \&quot;isCorporate\&quot;: false,      \&quot;isNewsletterOptIn\&quot;: false,      \&quot;localeDefault\&quot;: \&quot;en-US\&quot;   }  &#x60;&#x60;&#x60;    ### Client address    For a new address, the data entity is &#x60;AD&#x60; and the request would look like this:    POST  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;addressName\&quot;: \&quot;My House\&quot;,      \&quot;addressType\&quot;: \&quot;residential\&quot;,      \&quot;city\&quot;: \&quot;Metropolis\&quot;,      \&quot;complement\&quot;: \&quot;\&quot;,      \&quot;country\&quot;: \&quot;USA\&quot;,      \&quot;postalCode\&quot;: \&quot;11375\&quot;,      \&quot;receiverName\&quot;: \&quot;Clark Kent\&quot;,      \&quot;reference\&quot;: null,      \&quot;state\&quot;: \&quot;MP\&quot;,      \&quot;street\&quot;: \&quot;Baker Street\&quot;,      \&quot;neighborhood\&quot;: \&quot;Upper east side\&quot;,      \&quot;number\&quot;: \&quot;21\&quot;,      \&quot;userId\&quot;: \&quot;7e03m794-a33a-11e9-84rt6-0adfa64s5a8e\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new MasterDataApiV2.DocumentsApi();
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let requestBody = {key: "null"}; // {String: String} | 
let opts = {
  'schema': "schema" // String | Name of the schema the document to be created needs to be compliant with.
};
apiInstance.createnewdocument(contentType, accept, dataEntityName, requestBody, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **requestBody** | [**{String: String}**](String.md)|  | 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createorupdatepartialdocument

> DocumentResponse createorupdatepartialdocument(dataEntityName, contentType, accept, requestBody, opts)

Create partial document

This request allows you to partially update a document corresponding to a given data entity.    &gt; You can use this request to create documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to create a customer profile&#39;s &#x60;phone&#x60; and &#x60;isNewsletterOptIn&#x60; fields, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;isNewsletterOptIn\&quot;: false   }  &#x60;&#x60;&#x60;    ### Client address    In order to update the &#x60;receiverName&#x60; of an existing address, the data entity is &#x60;AD&#x60; and the request would look like this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;receiverName\&quot;: \&quot;Lois Lane\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new MasterDataApiV2.DocumentsApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let requestBody = {key: "null"}; // {String: String} | JSON with the fields to be updated.
let opts = {
  'schema': "schema" // String | Name of the schema the document to be created needs to be compliant with.
};
apiInstance.createorupdatepartialdocument(dataEntityName, contentType, accept, requestBody, opts, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **requestBody** | [**{String: String}**](String.md)| JSON with the fields to be updated. | 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deletedocument

> deletedocument(dataEntityName, contentType, accept, id)

Delete document

It allows to delete a document.

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

let apiInstance = new MasterDataApiV2.DocumentsApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
apiInstance.deletedocument(dataEntityName, contentType, accept, id, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getdocument

> UsingFieldsAll getdocument(dataEntityName, contentType, accept, id)

Get document

Gets document by ID.    &gt; Assign the &#x60;_fields&#x60; parameter in the query string to retrieve the desired fields. If you want to return all the fields use &#x60;_fields&#x3D;_all&#x60;.

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

let apiInstance = new MasterDataApiV2.DocumentsApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let contentType = "application/json"; // String | Type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
apiInstance.getdocument(dataEntityName, contentType, accept, id, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **contentType** | **String**| Type of the content being sent. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 

### Return type

[**UsingFieldsAll**](UsingFieldsAll.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateentiredocument

> DocumentResponse updateentiredocument(dataEntityName, accept, id, requestBody, opts)

Update entire document

Update an existing document corresponding to a given data entity. For example, you can update a customer profile or address.    &gt; You can use this request to update documents in any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to update an existing customer profile, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PUT  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;email\&quot;: \&quot;clark.kent@examplemail.com\&quot;,      \&quot;firstName\&quot;: \&quot;Clark\&quot;,      \&quot;lastName\&quot;: \&quot;Kent\&quot;,      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;documentType\&quot;: \&quot;CPF\&quot;,      \&quot;document\&quot;: \&quot;12345678900\&quot;      \&quot;isCorporate\&quot;: false,      \&quot;isNewsletterOptIn\&quot;: false,      \&quot;localeDefault\&quot;: \&quot;en-US\&quot;   }  &#x60;&#x60;&#x60;    ### Client address    To update an address, the data entity is &#x60;AD&#x60; and the request would look like this:    PUT  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;addressName\&quot;: \&quot;My House\&quot;,      \&quot;addressType\&quot;: \&quot;residential\&quot;,      \&quot;city\&quot;: \&quot;Metropolis\&quot;,      \&quot;complement\&quot;: \&quot;\&quot;,      \&quot;country\&quot;: \&quot;USA\&quot;,      \&quot;postalCode\&quot;: \&quot;11375\&quot;,      \&quot;receiverName\&quot;: \&quot;Clark Kent\&quot;,      \&quot;reference\&quot;: null,      \&quot;state\&quot;: \&quot;MP\&quot;,      \&quot;street\&quot;: \&quot;Baker Street\&quot;,      \&quot;neighborhood\&quot;: \&quot;Upper east side\&quot;,      \&quot;number\&quot;: \&quot;21\&quot;,      \&quot;userId\&quot;: \&quot;7e03m794-a33a-11e9-84rt6-0adfa64s5a8e\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new MasterDataApiV2.DocumentsApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
let requestBody = {key: "null"}; // {String: String} | 
let opts = {
  'where': "firstName is not null.", // String | Filter specification.
  'schema': "schema" // String | Name of the schema the document to be created needs to be compliant with.
};
apiInstance.updateentiredocument(dataEntityName, accept, id, requestBody, opts, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 
 **requestBody** | [**{String: String}**](String.md)|  | 
 **where** | **String**| Filter specification. | [optional] 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatepartialdocument

> DocumentResponse updatepartialdocument(dataEntityName, accept, id, requestBody, opts)

Update partial document

This request allows you to partially update a document corresponding to a given data entity. For example, you can update some fields of a customer profile or address.    &gt; You can use this request to update documents for any given data entity. Because of this, you are not restricted to using the fields exemplified below in your requests. But you should be aware of the fields allowed or required for each document you wish to update.    ## Example use cases    ### Client profile    In order to update a customer profile&#39;s &#x60;phone&#x60; and &#x60;isNewsletterOptIn&#x60; fields, choose the &#x60;CL&#x60; data entity and send a request similar to this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Client/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;phone\&quot;: \&quot;+12025550195\&quot;,      \&quot;isNewsletterOptIn\&quot;: false   }  &#x60;&#x60;&#x60;    ### Client address    In order to update the &#x60;receiverName&#x60; of an existing address, the data entity is &#x60;AD&#x60; and the request would look like this:    PATCH  &#x60;&#x60;&#x60;  https://examplestore.vtexcommercestable.com.br/api/dataentities/Address/documents/123456789abc  &#x60;&#x60;&#x60;    Request body  &#x60;&#x60;&#x60;json  {      \&quot;receiverName\&quot;: \&quot;Lois Lane\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new MasterDataApiV2.DocumentsApi();
let dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = "Client-b818cbda-e489-11e6-94f4-0ac138d2d42e"; // String | ID of the Document.
let requestBody = {key: "null"}; // {String: String} | 
let opts = {
  'where': "firstName is not null.", // String | Filter specification.
  'schema': "schema" // String | Name of the schema the document to be created needs to be compliant with.
};
apiInstance.updatepartialdocument(dataEntityName, accept, id, requestBody, opts, (error, data, response) => {
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
 **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **id** | **String**| ID of the Document. | 
 **requestBody** | [**{String: String}**](String.md)|  | 
 **where** | **String**| Filter specification. | [optional] 
 **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] 

### Return type

[**DocumentResponse**](DocumentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

