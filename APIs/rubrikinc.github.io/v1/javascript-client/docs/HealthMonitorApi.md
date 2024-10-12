# RubrikRestApi.HealthMonitorApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPolicies**](HealthMonitorApi.md#getPolicies) | **GET** /health_monitor/policies | Get details of health monitor policies
[**getPolicyStatus**](HealthMonitorApi.md#getPolicyStatus) | **GET** /health_monitor/policy_status | Get the status of health monitor policy enforcement
[**runPolicies**](HealthMonitorApi.md#runPolicies) | **POST** /health_monitor/run_policy | Enforce health monitor policies



## getPolicies

> [HealthMonitorPolicy] getPolicies(opts)

Get details of health monitor policies

Retrieves the details of all the health monitor policies when policy IDs are not specified in the query parameter. If the request includes a list of policy IDs in the query parameter, the response will include the details of the specified policies.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HealthMonitorApi();
let opts = {
  'policyIds': ["null"] // [String] | Optional list of policy IDs.
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
 **policyIds** | [**[String]**](String.md)| Optional list of policy IDs. | [optional] 

### Return type

[**[HealthMonitorPolicy]**](HealthMonitorPolicy.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPolicyStatus

> [NodePolicyCheckResult] getPolicyStatus(opts)

Get the status of health monitor policy enforcement

Retrieves the status of the policy enforcement for a list of nodes if specified. If nodes are not specified, the response includes the policy enforcement status for all the nodes on the Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HealthMonitorApi();
let opts = {
  'policyIds': ["null"], // [String] | Optional list of policy IDs. If not provided, the response includes the status of all the policies.
  'nodeIds': ["null"], // [String] | Optional list of Node IDs. If not provided, the response includes the status of all the nodes.
  'hasDetailedStatus': true // Boolean | Indicates if the policy enforcement status should include expanded result for each policy.
};
apiInstance.getPolicyStatus(opts, (error, data, response) => {
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
 **policyIds** | [**[String]**](String.md)| Optional list of policy IDs. If not provided, the response includes the status of all the policies. | [optional] 
 **nodeIds** | [**[String]**](String.md)| Optional list of Node IDs. If not provided, the response includes the status of all the nodes. | [optional] 
 **hasDetailedStatus** | **Boolean**| Indicates if the policy enforcement status should include expanded result for each policy. | [optional] 

### Return type

[**[NodePolicyCheckResult]**](NodePolicyCheckResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runPolicies

> [NodePolicyCheckResult] runPolicies(runPolicyArg)

Enforce health monitor policies

Triggers on-demand enforcement of the set of policies specified in the request body. If a list of nodes is provided, policies are run against these nodes, otherwise the policies are run on all active nodes of the Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HealthMonitorApi();
let runPolicyArg = new RubrikRestApi.RunPolicyArg(); // RunPolicyArg | The request object.
apiInstance.runPolicies(runPolicyArg, (error, data, response) => {
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
 **runPolicyArg** | [**RunPolicyArg**](RunPolicyArg.md)| The request object. | 

### Return type

[**[NodePolicyCheckResult]**](NodePolicyCheckResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

