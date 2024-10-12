# AirflowApiStable.ConnectionApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteConnection**](ConnectionApi.md#deleteConnection) | **DELETE** /connections/{connection_id} | Delete a connection
[**getConnection**](ConnectionApi.md#getConnection) | **GET** /connections/{connection_id} | Get a connection
[**getConnections**](ConnectionApi.md#getConnections) | **GET** /connections | List connections
[**patchConnection**](ConnectionApi.md#patchConnection) | **PATCH** /connections/{connection_id} | Update a connection
[**postConnection**](ConnectionApi.md#postConnection) | **POST** /connections | Create a connection
[**testConnection**](ConnectionApi.md#testConnection) | **POST** /connections/test | Test a connection



## deleteConnection

> deleteConnection(connectionId)

Delete a connection

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ConnectionApi();
let connectionId = "connectionId_example"; // String | The connection ID.
apiInstance.deleteConnection(connectionId, (error, data, response) => {
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
 **connectionId** | **String**| The connection ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConnection

> Connection getConnection(connectionId)

Get a connection

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ConnectionApi();
let connectionId = "connectionId_example"; // String | The connection ID.
apiInstance.getConnection(connectionId, (error, data, response) => {
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
 **connectionId** | **String**| The connection ID. | 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConnections

> ConnectionCollection getConnections(opts)

List connections

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ConnectionApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getConnections(opts, (error, data, response) => {
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

[**ConnectionCollection**](ConnectionCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchConnection

> Connection patchConnection(connectionId, connection, opts)

Update a connection

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ConnectionApi();
let connectionId = "connectionId_example"; // String | The connection ID.
let connection = new AirflowApiStable.Connection(); // Connection | 
let opts = {
  'updateMask': ["null"] // [String] | The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields. 
};
apiInstance.patchConnection(connectionId, connection, opts, (error, data, response) => {
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
 **connectionId** | **String**| The connection ID. | 
 **connection** | [**Connection**](Connection.md)|  | 
 **updateMask** | [**[String]**](String.md)| The fields to update on the resource. If absent or empty, all modifiable fields are updated. A comma-separated list of fully qualified names of fields.  | [optional] 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postConnection

> Connection postConnection(connection)

Create a connection

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ConnectionApi();
let connection = new AirflowApiStable.Connection(); // Connection | 
apiInstance.postConnection(connection, (error, data, response) => {
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
 **connection** | [**Connection**](Connection.md)|  | 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## testConnection

> ConnectionTest testConnection(connection)

Test a connection

Test a connection.  *New in version 2.2.0* 

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.ConnectionApi();
let connection = new AirflowApiStable.Connection(); // Connection | 
apiInstance.testConnection(connection, (error, data, response) => {
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
 **connection** | [**Connection**](Connection.md)|  | 

### Return type

[**ConnectionTest**](ConnectionTest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

