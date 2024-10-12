# OpenPolicyAgentOpaRestApi.CompileAPIApi

All URIs are relative to *http://openpolicy.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCompile**](CompileAPIApi.md#postCompile) | **POST** /v1/compile | Compile



## postCompile

> PostCompile200Response postCompile(opts)

Compile

This API endpoint allows you to partially evaluate Rego queries and obtain a simplified version of the policy. The example below assumes that OPA has been given the following policy (use &#x60;PUT /v1/policies/{path}&#x60;):  &#x60;&#x60;&#x60;yaml package example allow {   input.subject.clearance_level &gt;&#x3D; data.reports[_].clearance_level } &#x60;&#x60;&#x60; Compile API **request body** so that it contain the following fields:  | Field | Type | Required | Description | | --- | --- | --- | --- | | &#x60;query&#x60; | &#x60;string&#x60; | Yes | The query to partially evaluate and compile. | | &#x60;input&#x60; | &#x60;any&#x60; | No | The input document to use during partial evaluation (default: undefined). | | &#x60;unknowns&#x60; | &#x60;array[string]&#x60; | No | The terms to treat as unknown during partial evaluation (default: &#x60;[\&quot;input\&quot;]&#x60;]). |  For example:  &#x60;&#x60;&#x60;json {   \&quot;query\&quot;: \&quot;data.example.allow &#x3D;&#x3D; true\&quot;,   \&quot;input\&quot;: {     \&quot;subject\&quot;: {       \&quot;clearance_level\&quot;: 4     }   },   \&quot;unknowns\&quot;: [     \&quot;data.reports\&quot;     ] } &#x60;&#x60;&#x60; ### Partial evaluation In some cases, the result of partial valuation is a conclusive, unconditional answer. See [the guidance](https://www.openpolicyagent.org/docs/latest/rest-api/#unconditional-results-from-partial-evaluation) for details.

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.CompileAPIApi();
let opts = {
  'pretty': true, // Boolean | If true, response will be in a human-readable format.
  'explain': "full", // String | If set to *full*, response will include query explanations in addition to the result.
  'metrics': false, // Boolean | If true, compiler performance metrics will be returned in the response.
  'instrument': false, // Boolean | If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
  'requestBody': {key: null} // {String: Object} | The query (in JSON format)
};
apiInstance.postCompile(opts, (error, data, response) => {
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
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 
 **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] 
 **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] 
 **instrument** | **Boolean**| If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem. | [optional] 
 **requestBody** | [**{String: Object}**](Object.md)| The query (in JSON format) | [optional] 

### Return type

[**PostCompile200Response**](PostCompile200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

