# OpenPolicyAgentOpaRestApi.QueryAPIApi

All URIs are relative to *http://openpolicy.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQuery**](QueryAPIApi.md#getQuery) | **GET** /v1/query | Execute an ad-hoc query (simple)
[**postQuery**](QueryAPIApi.md#postQuery) | **POST** /v1/query | Execute an ad-hoc query (complex)
[**postSimpleQuery**](QueryAPIApi.md#postSimpleQuery) | **POST** / | Execute a simple query



## getQuery

> PostCompile200Response getQuery(q, opts)

Execute an ad-hoc query (simple)

This API endpoint returns bindings for the variables in the query.  For more complex JSON queries, use &#x60;POST /v1/query&#x60; instead.

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.QueryAPIApi();
let q = "{\"query\": \"data.servers[i].ports[_] = \\\"p2\\\"; data.servers[i].name = name\"}"; // String | The [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) ad-hoc query to execute.
let opts = {
  'pretty': true, // Boolean | If true, response will be in a human-readable format.
  'explain': "full", // String | If set to *full*, response will include query explanations in addition to the result.
  'metrics': false // Boolean | If true, compiler performance metrics will be returned in the response.
};
apiInstance.getQuery(q, opts, (error, data, response) => {
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
 **q** | **String**| The [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) ad-hoc query to execute. | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 
 **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] 
 **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] 

### Return type

[**PostCompile200Response**](PostCompile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postQuery

> PostCompile200Response postQuery(requestBody, opts)

Execute an ad-hoc query (complex)

This API endpoint returns bindings for the variables in the query.  For simpler JSON queries, you may use &#x60;GET /v1/query&#x60; instead.

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.QueryAPIApi();
let requestBody = {key: null}; // {String: Object} | The test of the query (in JSON format)
let opts = {
  'pretty': true, // Boolean | If true, response will be in a human-readable format.
  'explain': "full", // String | If set to *full*, response will include query explanations in addition to the result.
  'metrics': false // Boolean | If true, compiler performance metrics will be returned in the response.
};
apiInstance.postQuery(requestBody, opts, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)| The test of the query (in JSON format) | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 
 **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] 
 **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] 

### Return type

[**PostCompile200Response**](PostCompile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-yaml
- **Accept**: application/json


## postSimpleQuery

> postSimpleQuery(requestBody, opts)

Execute a simple query

This API queries the document at *_/data/system/main* by default (however, you can [configure OPA](https://www.openpolicyagent.org/docs/latest/configuration/) to use a different path to serve these queries). That document defines the response. For example, use the following in &#x60;PUT /v1/policies/{path}&#x60;) to define a rule that will produce a value for the *_/data/system/main* document:    &#x60;&#x60;&#x60;yaml   package system   main &#x3D; msg {     msg :&#x3D; sprintf(\&quot;hello, %v\&quot;, input.user)   }   &#x60;&#x60;&#x60;  The server will return a *not found* (404) response if *_/data/system/main* is undefined.

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.QueryAPIApi();
let requestBody = {key: null}; // {String: Object} | The text of the input document (in JSON format)
let opts = {
  'pretty': true // Boolean | If true, response will be in a human-readable format.
};
apiInstance.postSimpleQuery(requestBody, opts, (error, data, response) => {
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
 **requestBody** | [**{String: Object}**](Object.md)| The text of the input document (in JSON format) | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

