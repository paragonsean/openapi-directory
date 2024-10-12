# AirflowApiStable.VariableApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteVariable**](VariableApi.md#deleteVariable) | **DELETE** /variables/{variable_key} | Delete a variable
[**getVariable**](VariableApi.md#getVariable) | **GET** /variables/{variable_key} | Get a variable
[**getVariables**](VariableApi.md#getVariables) | **GET** /variables | List variables
[**patchVariable**](VariableApi.md#patchVariable) | **PATCH** /variables/{variable_key} | Update a variable
[**postVariables**](VariableApi.md#postVariables) | **POST** /variables | Create a variable



## deleteVariable

> deleteVariable(variableKey)

Delete a variable

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.VariableApi();
let variableKey = "variableKey_example"; // String | The variable Key.
apiInstance.deleteVariable(variableKey, (error, data, response) => {
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
 **variableKey** | **String**| The variable Key. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariable

> Variable getVariable(variableKey)

Get a variable

Get a variable by key.

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.VariableApi();
let variableKey = "variableKey_example"; // String | The variable Key.
apiInstance.getVariable(variableKey, (error, data, response) => {
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
 **variableKey** | **String**| The variable Key. | 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariables

> VariableCollection getVariables(opts)

List variables

The collection does not contain data. To get data, you must get a single entity.

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.VariableApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
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
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**VariableCollection**](VariableCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchVariable

> Variable patchVariable(variableKey, variable, opts)

Update a variable

Update a variable by key.

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.VariableApi();
let variableKey = "variableKey_example"; // String | The variable Key.
let variable = new AirflowApiStable.Variable(); // Variable | 
let opts = {
  'updateMask': ["null"] // [String] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
};
apiInstance.patchVariable(variableKey, variable, opts, (error, data, response) => {
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
 **variableKey** | **String**| The variable Key. | 
 **variable** | [**Variable**](Variable.md)|  | 
 **updateMask** | [**[String]**](String.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postVariables

> Variable postVariables(variable)

Create a variable

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.VariableApi();
let variable = new AirflowApiStable.Variable(); // Variable | 
apiInstance.postVariables(variable, (error, data, response) => {
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
 **variable** | [**Variable**](Variable.md)|  | 

### Return type

[**Variable**](Variable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

