# OpenPolicyAgentOpaRestApi.DataAPIApi

All URIs are relative to *http://openpolicy.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDocument**](DataAPIApi.md#deleteDocument) | **DELETE** /v1/data/{path} | Delete a document
[**getDocument**](DataAPIApi.md#getDocument) | **GET** /v1/data/{path} | Get a document
[**getDocumentWithPath**](DataAPIApi.md#getDocumentWithPath) | **POST** /v1/data/{path} | Get a document (with input)
[**getDocumentWithWebHook**](DataAPIApi.md#getDocumentWithWebHook) | **POST** /v0/data/{path} | Get a document (with webhook)
[**patchDocument**](DataAPIApi.md#patchDocument) | **PATCH** /v1/data/{path} | Update a document
[**putDocument**](DataAPIApi.md#putDocument) | **PUT** /v1/data/{path} | Create or overwrite a document



## deleteDocument

> deleteDocument(path)

Delete a document

This API endpoint deletes an existing document from the server

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.DataAPIApi();
let path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
apiInstance.deleteDocument(path, (error, data, response) => {
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
 **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocument

> GetDocumentWithWebHook200Response getDocument(path, opts)

Get a document

This API endpoint returns the document specified by &#x60;path&#x60;.  The server will return a *bad request* (400) response if either: - The query requires an input document and you do not provide it - You provide the input document but the query has already defined it.

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.DataAPIApi();
let path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
let opts = {
  'input': {key: null}, // {String: Object} | Provide the text for an [input document](https://www.openpolicyagent.org/docs/latest/kubernetes-primer/#input-document) in JSON format
  'pretty': true, // Boolean | If true, response will be in a human-readable format.
  'provenance': false, // Boolean | If true, response will include build and version information in addition to the result.
  'explain': "full", // String | If set to *full*, response will include query explanations in addition to the result.
  'metrics': false, // Boolean | If true, compiler performance metrics will be returned in the response.
  'instrument': false // Boolean | If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
};
apiInstance.getDocument(path, opts, (error, data, response) => {
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
 **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | 
 **input** | [**{String: Object}**](Object.md)| Provide the text for an [input document](https://www.openpolicyagent.org/docs/latest/kubernetes-primer/#input-document) in JSON format | [optional] 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 
 **provenance** | **Boolean**| If true, response will include build and version information in addition to the result. | [optional] 
 **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] 
 **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] 
 **instrument** | **Boolean**| If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem. | [optional] 

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentWithPath

> GetDocumentWithWebHook200Response getDocumentWithPath(path, requestBody, opts)

Get a document (with input)

The server will return a *bad request* (400) response if either: - The query requires an input document and you do not provide it - You provided an input document but the query has already defined it.  If &#x60;path&#x60; indexes into an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, a *not found* response (404) will be returned.

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.DataAPIApi();
let path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
let requestBody = {key: null}; // {String: Object} | The input document (in JSON format)
let opts = {
  'pretty': true, // Boolean | If true, response will be in a human-readable format.
  'provenance': false, // Boolean | If true, response will include build and version information in addition to the result.
  'explain': "full", // String | If set to *full*, response will include query explanations in addition to the result.
  'metrics': false, // Boolean | If true, compiler performance metrics will be returned in the response.
  'instrument': false // Boolean | If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
};
apiInstance.getDocumentWithPath(path, requestBody, opts, (error, data, response) => {
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
 **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | 
 **requestBody** | [**{String: Object}**](Object.md)| The input document (in JSON format) | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 
 **provenance** | **Boolean**| If true, response will include build and version information in addition to the result. | [optional] 
 **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] 
 **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] 
 **instrument** | **Boolean**| If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem. | [optional] 

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


## getDocumentWithWebHook

> GetDocumentWithWebHook200Response getDocumentWithWebHook(path, requestBody, opts)

Get a document (with webhook)

The example given here assumes you have created a policy (with &#x60;PUT /v1/policies/{path}&#x60;), such as:    &#x60;&#x60;&#x60;yaml   package opa.examples   import input.example.flag   allow_request { flag &#x3D;&#x3D; true }   &#x60;&#x60;&#x60;  The server will return a *not found* (404) response if the requested document is missing or undefined. 

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.DataAPIApi();
let path = "opa/examples/allow_request"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
let requestBody = {key: null}; // {String: Object} | The input document (in JSON format)
let opts = {
  'pretty': true // Boolean | If true, response will be in a human-readable format.
};
apiInstance.getDocumentWithWebHook(path, requestBody, opts, (error, data, response) => {
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
 **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | 
 **requestBody** | [**{String: Object}**](Object.md)| The input document (in JSON format) | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


## patchDocument

> patchDocument(path, patchesSchemaInner)

Update a document

This API endpoint updates an existing document on the server by describing the changes required (using [JSON patch operations](http://jsonpatch.com/))

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.DataAPIApi();
let path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
let patchesSchemaInner = [new OpenPolicyAgentOpaRestApi.PatchesSchemaInner()]; // [PatchesSchemaInner] | The list of JSON patch operations.
apiInstance.patchDocument(path, patchesSchemaInner, (error, data, response) => {
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
 **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | 
 **patchesSchemaInner** | [**[PatchesSchemaInner]**](PatchesSchemaInner.md)| The list of JSON patch operations. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDocument

> putDocument(path, body, opts)

Create or overwrite a document

If the path does not refer to an existing document (for example *us-west/servers*), the server will attempt to create all the necessary containing documents.  This behavior is similar to the Unix command [mkdir -p](https://en.wikipedia.org/wiki/Mkdir#Options).

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.DataAPIApi();
let path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
let body = null; // Object | The JSON document to write to the specified path.
let opts = {
  'ifNoneMatch': "*" // String | The server will respect the If-None-Match header if it is set to * (in other words, it will not overwrite an existing document located at the specified `path`).
};
apiInstance.putDocument(path, body, opts, (error, data, response) => {
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
 **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | 
 **body** | **Object**| The JSON document to write to the specified path. | 
 **ifNoneMatch** | **String**| The server will respect the If-None-Match header if it is set to * (in other words, it will not overwrite an existing document located at the specified &#x60;path&#x60;). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

