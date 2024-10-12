# AirbyteConfigurationApi.OperationApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkOperation**](OperationApi.md#checkOperation) | **POST** /v1/operations/check | Check if an operation to be created is valid
[**createOperation**](OperationApi.md#createOperation) | **POST** /v1/operations/create | Create an operation to be applied as part of a connection pipeline
[**deleteOperation**](OperationApi.md#deleteOperation) | **POST** /v1/operations/delete | Delete an operation
[**getOperation**](OperationApi.md#getOperation) | **POST** /v1/operations/get | Returns an operation
[**listOperationsForConnection**](OperationApi.md#listOperationsForConnection) | **POST** /v1/operations/list | Returns all operations for a connection.
[**updateOperation**](OperationApi.md#updateOperation) | **POST** /v1/operations/update | Update an operation



## checkOperation

> CheckOperationRead checkOperation(operatorConfiguration)

Check if an operation to be created is valid

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OperationApi();
let operatorConfiguration = new AirbyteConfigurationApi.OperatorConfiguration(); // OperatorConfiguration | 
apiInstance.checkOperation(operatorConfiguration, (error, data, response) => {
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
 **operatorConfiguration** | [**OperatorConfiguration**](OperatorConfiguration.md)|  | 

### Return type

[**CheckOperationRead**](CheckOperationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createOperation

> OperationRead createOperation(operationCreate)

Create an operation to be applied as part of a connection pipeline

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OperationApi();
let operationCreate = new AirbyteConfigurationApi.OperationCreate(); // OperationCreate | 
apiInstance.createOperation(operationCreate, (error, data, response) => {
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
 **operationCreate** | [**OperationCreate**](OperationCreate.md)|  | 

### Return type

[**OperationRead**](OperationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteOperation

> deleteOperation(operationIdRequestBody)

Delete an operation

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OperationApi();
let operationIdRequestBody = new AirbyteConfigurationApi.OperationIdRequestBody(); // OperationIdRequestBody | 
apiInstance.deleteOperation(operationIdRequestBody, (error, data, response) => {
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
 **operationIdRequestBody** | [**OperationIdRequestBody**](OperationIdRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getOperation

> OperationRead getOperation(operationIdRequestBody)

Returns an operation

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OperationApi();
let operationIdRequestBody = new AirbyteConfigurationApi.OperationIdRequestBody(); // OperationIdRequestBody | 
apiInstance.getOperation(operationIdRequestBody, (error, data, response) => {
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
 **operationIdRequestBody** | [**OperationIdRequestBody**](OperationIdRequestBody.md)|  | 

### Return type

[**OperationRead**](OperationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listOperationsForConnection

> OperationReadList listOperationsForConnection(connectionIdRequestBody)

Returns all operations for a connection.

List operations for connection.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OperationApi();
let connectionIdRequestBody = new AirbyteConfigurationApi.ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
apiInstance.listOperationsForConnection(connectionIdRequestBody, (error, data, response) => {
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
 **connectionIdRequestBody** | [**ConnectionIdRequestBody**](ConnectionIdRequestBody.md)|  | 

### Return type

[**OperationReadList**](OperationReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateOperation

> OperationRead updateOperation(operationUpdate)

Update an operation

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.OperationApi();
let operationUpdate = new AirbyteConfigurationApi.OperationUpdate(); // OperationUpdate | 
apiInstance.updateOperation(operationUpdate, (error, data, response) => {
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
 **operationUpdate** | [**OperationUpdate**](OperationUpdate.md)|  | 

### Return type

[**OperationRead**](OperationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

