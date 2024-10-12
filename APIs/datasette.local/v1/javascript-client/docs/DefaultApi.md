# DatasetteApi.DefaultApi

All URIs are relative to *http://datasette.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](DefaultApi.md#query) | **GET** /content.json | Execute a SQLite SQL query against the content database



## query

> [Object] query(sql, shape)

Execute a SQLite SQL query against the content database

Accepts SQLite SQL query, returns JSON. Does not allow PRAGMA statements.

### Example

```javascript
import DatasetteApi from 'datasette_api';

let apiInstance = new DatasetteApi.DefaultApi();
let sql = "sql_example"; // String | The SQL query to be executed
let shape = "shape_example"; // String | The shape of the response data. Must be \"array\"
apiInstance.query(sql, shape, (error, data, response) => {
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
 **sql** | **String**| The SQL query to be executed | 
 **shape** | **String**| The shape of the response data. Must be \&quot;array\&quot; | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

