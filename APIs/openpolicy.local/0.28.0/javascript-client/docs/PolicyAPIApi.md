# OpenPolicyAgentOpaRestApi.PolicyAPIApi

All URIs are relative to *http://openpolicy.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePolicyModule**](PolicyAPIApi.md#deletePolicyModule) | **DELETE** /v1/policies/{id} | Delete a policy module
[**getPolicies**](PolicyAPIApi.md#getPolicies) | **GET** /v1/policies | List policies
[**getPolicyModule**](PolicyAPIApi.md#getPolicyModule) | **GET** /v1/policies/{id} | Get a policy module
[**putPolicyModule**](PolicyAPIApi.md#putPolicyModule) | **PUT** /v1/policies/{id} | Create or update a policy module



## deletePolicyModule

> GetDocumentWithWebHook200Response deletePolicyModule(id, opts)

Delete a policy module

This API endpoint removes an existing policy module from the server

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.PolicyAPIApi();
let id = "example1"; // String | The name of a policy module
let opts = {
  'pretty': true // Boolean | If true, response will be in a human-readable format.
};
apiInstance.deletePolicyModule(id, opts, (error, data, response) => {
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
 **id** | **String**| The name of a policy module | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPolicies

> Model200Result getPolicies(opts)

List policies

This API endpoint responds with a list of all policy modules on the server (result response)

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.PolicyAPIApi();
let opts = {
  'pretty': true // Boolean | If true, response will be in a human-readable format.
};
apiInstance.getPolicies(opts, (error, data, response) => {
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

### Return type

[**Model200Result**](Model200Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPolicyModule

> Model200Result getPolicyModule(id, opts)

Get a policy module

This API endpoint returns the details of the specified policy module (&#x60;{id}&#x60;)

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.PolicyAPIApi();
let id = "example1"; // String | The name of a policy module
let opts = {
  'pretty': true // Boolean | If true, response will be in a human-readable format.
};
apiInstance.getPolicyModule(id, opts, (error, data, response) => {
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
 **id** | **String**| The name of a policy module | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 

### Return type

[**Model200Result**](Model200Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putPolicyModule

> Model200Result putPolicyModule(id, body, opts)

Create or update a policy module

- If the policy module does not exist, it is created. - If the policy module already exists, it is replaced.  If the policy module isn&#39;t correctly defined, a *bad request* (400) response is returned.  ### Example policy module &#x60;&#x60;&#x60;yaml package opa.examples  import data.servers import data.networks import data.ports  public_servers[server] {   some k, m    server :&#x3D; servers[_]    server.ports[_] &#x3D;&#x3D; ports[k].id    ports[k].networks[_] &#x3D;&#x3D; networks[m].id    networks[m].public &#x3D;&#x3D; true } &#x60;&#x60;&#x60;

### Example

```javascript
import OpenPolicyAgentOpaRestApi from 'open_policy_agent__opa_rest_api';

let apiInstance = new OpenPolicyAgentOpaRestApi.PolicyAPIApi();
let id = "example1"; // String | The name of a policy module
let body = "body_example"; // String | 
let opts = {
  'pretty': true, // Boolean | If true, response will be in a human-readable format.
  'metrics': false // Boolean | If true, compiler performance metrics will be returned in the response.
};
apiInstance.putPolicyModule(id, body, opts, (error, data, response) => {
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
 **id** | **String**| The name of a policy module | 
 **body** | **String**|  | 
 **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] 
 **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] 

### Return type

[**Model200Result**](Model200Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

