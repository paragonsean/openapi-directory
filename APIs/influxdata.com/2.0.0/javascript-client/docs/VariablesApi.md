# InfluxOssApiService.VariablesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteVariablesID**](VariablesApi.md#deleteVariablesID) | **DELETE** /variables/{variableID} | Delete a variable
[**deleteVariablesIDLabelsID**](VariablesApi.md#deleteVariablesIDLabelsID) | **DELETE** /variables/{variableID}/labels/{labelID} | Delete a label from a variable
[**getVariables**](VariablesApi.md#getVariables) | **GET** /variables | List all variables
[**getVariablesID**](VariablesApi.md#getVariablesID) | **GET** /variables/{variableID} | Retrieve a variable
[**getVariablesIDLabels**](VariablesApi.md#getVariablesIDLabels) | **GET** /variables/{variableID}/labels | List all labels for a variable
[**patchVariablesID**](VariablesApi.md#patchVariablesID) | **PATCH** /variables/{variableID} | Update a variable
[**postVariables**](VariablesApi.md#postVariables) | **POST** /variables | Create a variable
[**postVariablesIDLabels**](VariablesApi.md#postVariablesIDLabels) | **POST** /variables/{variableID}/labels | Add a label to a variable
[**putVariablesID**](VariablesApi.md#putVariablesID) | **PUT** /variables/{variableID} | Replace a variable



## deleteVariablesID

> deleteVariablesID(variableID, opts)

Delete a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteVariablesID(variableID, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVariablesIDLabelsID

> deleteVariablesIDLabelsID(variableID, labelID, opts)

Delete a label from a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let labelID = "labelID_example"; // String | The label ID to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteVariablesIDLabelsID(variableID, labelID, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **labelID** | **String**| The label ID to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariables

> Variables getVariables(opts)

List all variables

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'org': "org_example", // String | The name of the organization.
  'orgID': "orgID_example" // String | The organization ID.
};
apiInstance.getVariables(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **org** | **String**| The name of the organization. | [optional] 
 **orgID** | **String**| The organization ID. | [optional] 

### Return type

[**Variables**](Variables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariablesID

> Variable getVariablesID(variableID, opts)

Retrieve a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getVariablesID(variableID, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariablesIDLabels

> LabelsResponse getVariablesIDLabels(variableID, opts)

List all labels for a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getVariablesIDLabels(variableID, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchVariablesID

> Variable patchVariablesID(variableID, variable, opts)

Update a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let variable = new InfluxOssApiService.Variable(); // Variable | Variable update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchVariablesID(variableID, variable, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **variable** | [**Variable**](Variable.md)| Variable update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postVariables

> Variable postVariables(variable, opts)

Create a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variable = new InfluxOssApiService.Variable(); // Variable | Variable to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postVariables(variable, opts, (error, data, response) => {
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
 **variable** | [**Variable**](Variable.md)| Variable to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postVariablesIDLabels

> LabelResponse postVariablesIDLabels(variableID, labelMapping, opts)

Add a label to a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postVariablesIDLabels(variableID, labelMapping, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVariablesID

> Variable putVariablesID(variableID, variable, opts)

Replace a variable

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.VariablesApi();
let variableID = "variableID_example"; // String | The variable ID.
let variable = new InfluxOssApiService.Variable(); // Variable | Variable to replace
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putVariablesID(variableID, variable, opts, (error, data, response) => {
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
 **variableID** | **String**| The variable ID. | 
 **variable** | [**Variable**](Variable.md)| Variable to replace | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

