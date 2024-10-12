# RudderApi.ComplianceApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDirectiveComplianceId**](ComplianceApi.md#getDirectiveComplianceId) | **GET** /compliance/directives/{directiveId} | Compliance details by directive
[**getDirectivesCompliance**](ComplianceApi.md#getDirectivesCompliance) | **GET** /compliance/directives | Compliance details for all directives
[**getGlobalCompliance**](ComplianceApi.md#getGlobalCompliance) | **GET** /compliance | Global compliance
[**getNodeCompliance**](ComplianceApi.md#getNodeCompliance) | **GET** /compliance/nodes/{nodeId} | Compliance details by node
[**getNodesCompliance**](ComplianceApi.md#getNodesCompliance) | **GET** /compliance/nodes | Compliance details for all nodes
[**getRuleCompliance**](ComplianceApi.md#getRuleCompliance) | **GET** /compliance/rules/{ruleId} | Compliance details by rule
[**getRulesCompliance**](ComplianceApi.md#getRulesCompliance) | **GET** /compliance/rules | Compliance details for all rules



## getDirectiveComplianceId

> GetDirectiveComplianceId200Response getDirectiveComplianceId(directiveId, opts)

Compliance details by directive

Get current compliance of a directive of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
let directiveId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the directive
let opts = {
  'format': "[\"csv\"]" // String | format of export
};
apiInstance.getDirectiveComplianceId(directiveId, opts, (error, data, response) => {
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
 **directiveId** | **String**| Id of the directive | 
 **format** | **String**| format of export | [optional] 

### Return type

[**GetDirectiveComplianceId200Response**](GetDirectiveComplianceId200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDirectivesCompliance

> GetDirectivesCompliance200Response getDirectivesCompliance()

Compliance details for all directives

Get current compliance of all the nodes of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
apiInstance.getDirectivesCompliance((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDirectivesCompliance200Response**](GetDirectivesCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGlobalCompliance

> GetGlobalCompliance200Response getGlobalCompliance(opts)

Global compliance

Get current global compliance of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
let opts = {
  'precision': 0 // Number | Number of digits after comma in compliance percent figures
};
apiInstance.getGlobalCompliance(opts, (error, data, response) => {
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
 **precision** | **Number**| Number of digits after comma in compliance percent figures | [optional] [default to 2]

### Return type

[**GetGlobalCompliance200Response**](GetGlobalCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodeCompliance

> GetNodeCompliance200Response getNodeCompliance(nodeId, opts)

Compliance details by node

Get current compliance of a node of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
let nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
let opts = {
  'level': 4, // Number | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
  'precision': 0 // Number | Number of digits after comma in compliance percent figures
};
apiInstance.getNodeCompliance(nodeId, opts, (error, data, response) => {
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
 **nodeId** | **String**| Id of the target node | 
 **level** | **Number**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10]
 **precision** | **Number**| Number of digits after comma in compliance percent figures | [optional] [default to 2]

### Return type

[**GetNodeCompliance200Response**](GetNodeCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNodesCompliance

> GetNodesCompliance200Response getNodesCompliance(opts)

Compliance details for all nodes

Get current compliance of all the nodes of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
let opts = {
  'level': 4, // Number | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
  'precision': 0 // Number | Number of digits after comma in compliance percent figures
};
apiInstance.getNodesCompliance(opts, (error, data, response) => {
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
 **level** | **Number**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10]
 **precision** | **Number**| Number of digits after comma in compliance percent figures | [optional] [default to 2]

### Return type

[**GetNodesCompliance200Response**](GetNodesCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRuleCompliance

> GetRuleCompliance200Response getRuleCompliance(ruleId, opts)

Compliance details by rule

Get current compliance of a rule of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
let ruleId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target rule
let opts = {
  'level': 4, // Number | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
  'precision': 0 // Number | Number of digits after comma in compliance percent figures
};
apiInstance.getRuleCompliance(ruleId, opts, (error, data, response) => {
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
 **ruleId** | **String**| Id of the target rule | 
 **level** | **Number**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10]
 **precision** | **Number**| Number of digits after comma in compliance percent figures | [optional] [default to 2]

### Return type

[**GetRuleCompliance200Response**](GetRuleCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRulesCompliance

> GetRulesCompliance200Response getRulesCompliance(opts)

Compliance details for all rules

Get current compliance of all the rules of a Rudder server

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ComplianceApi();
let opts = {
  'level': 4, // Number | Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports)
  'precision': 0 // Number | Number of digits after comma in compliance percent figures
};
apiInstance.getRulesCompliance(opts, (error, data, response) => {
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
 **level** | **Number**| Number of depth level of compliance objects to display (1:rules, 2:directives, 3:components, 4:nodes, 5:values, 6:reports) | [optional] [default to 10]
 **precision** | **Number**| Number of digits after comma in compliance percent figures | [optional] [default to 2]

### Return type

[**GetRulesCompliance200Response**](GetRulesCompliance200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

