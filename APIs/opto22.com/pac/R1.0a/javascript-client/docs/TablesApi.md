# PacControlRestApi.TablesApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readFloatTableElement_0**](TablesApi.md#readFloatTableElement_0) | **GET** /device/strategy/tables/floats/{tableName}/{index} | 
[**readFloatTable_0**](TablesApi.md#readFloatTable_0) | **GET** /device/strategy/tables/floats/{tableName} | 
[**readFloatTables_0**](TablesApi.md#readFloatTables_0) | **GET** /device/strategy/tables/floats | 
[**readInt32TableElement_0**](TablesApi.md#readInt32TableElement_0) | **GET** /device/strategy/tables/int32s/{tableName}/{index} | 
[**readInt32Table_0**](TablesApi.md#readInt32Table_0) | **GET** /device/strategy/tables/int32s/{tableName} | 
[**readInt32Tables_0**](TablesApi.md#readInt32Tables_0) | **GET** /device/strategy/tables/int32s | 
[**readInt64TableAsString_0**](TablesApi.md#readInt64TableAsString_0) | **GET** /device/strategy/tables/int64s/{tableName}/_string | 
[**readInt64TableElementAsString_0**](TablesApi.md#readInt64TableElementAsString_0) | **GET** /device/strategy/tables/int64s/{tableName}/{index}/_string | 
[**readInt64TableElement_0**](TablesApi.md#readInt64TableElement_0) | **GET** /device/strategy/tables/int64s/{tableName}/{index} | 
[**readInt64Table_0**](TablesApi.md#readInt64Table_0) | **GET** /device/strategy/tables/int64s/{tableName} | 
[**readInt64Tables_0**](TablesApi.md#readInt64Tables_0) | **GET** /device/strategy/tables/int64s | 
[**readStringTableElement_0**](TablesApi.md#readStringTableElement_0) | **GET** /device/strategy/tables/strings/{tableName}/{index} | 
[**readStringTable_0**](TablesApi.md#readStringTable_0) | **GET** /device/strategy/tables/strings/{tableName} | 
[**readStringTables_0**](TablesApi.md#readStringTables_0) | **GET** /device/strategy/tables/strings | 
[**writeFloatTableElement_0**](TablesApi.md#writeFloatTableElement_0) | **POST** /device/strategy/tables/floats/{tableName}/{index} | 
[**writeFloatTable_0**](TablesApi.md#writeFloatTable_0) | **POST** /device/strategy/tables/floats/{tableName} | 
[**writeInt32TableElement_0**](TablesApi.md#writeInt32TableElement_0) | **POST** /device/strategy/tables/int32s/{tableName}/{index} | 
[**writeInt32Table_0**](TablesApi.md#writeInt32Table_0) | **POST** /device/strategy/tables/int32s/{tableName} | 
[**writeInt64TableAsString_0**](TablesApi.md#writeInt64TableAsString_0) | **POST** /device/strategy/tables/int64s/{tableName}/_string | 
[**writeInt64TableElementAsString_0**](TablesApi.md#writeInt64TableElementAsString_0) | **POST** /device/strategy/tables/int64s/{tableName}/{index}/_string | 
[**writeInt64TableElement_0**](TablesApi.md#writeInt64TableElement_0) | **POST** /device/strategy/tables/int64s/{tableName}/{index} | 
[**writeInt64Table_0**](TablesApi.md#writeInt64Table_0) | **POST** /device/strategy/tables/int64s/{tableName} | 
[**writeStringTableElement_0**](TablesApi.md#writeStringTableElement_0) | **POST** /device/strategy/tables/strings/{tableName}/{index} | 
[**writeStringTable_0**](TablesApi.md#writeStringTable_0) | **POST** /device/strategy/tables/strings/{tableName} | 



## readFloatTableElement_0

> FloatValueObject readFloatTableElement_0(tableName, index)



Read specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of float table to read
let index = 56; // Number | Index of element to read
apiInstance.readFloatTableElement_0(tableName, index, (error, data, response) => {
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
 **tableName** | **String**| Name of float table to read | 
 **index** | **Number**| Index of element to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readFloatTable_0

> [Number] readFloatTable_0(tableName, opts)



Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of float table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readFloatTable_0(tableName, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of float table to read; starting index and number of elements may be specified (defaults to all elements) | 
 **startIndex** | **Number**| Index of first element to read (default is 0) | [optional] 
 **numElements** | **Number**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readFloatTables_0

> [TableDef] readFloatTables_0()



Returns an array of the name and length of all the float tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
apiInstance.readFloatTables_0((error, data, response) => {
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

[**[TableDef]**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt32TableElement_0

> Int32ValueObject readInt32TableElement_0(tableName, index)



Read specified integer32 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of the integer32 table to read
let index = 56; // Number | Index of element to read
apiInstance.readInt32TableElement_0(tableName, index, (error, data, response) => {
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
 **tableName** | **String**| Name of the integer32 table to read | 
 **index** | **Number**| Index of element to read | 

### Return type

[**Int32ValueObject**](Int32ValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt32Table_0

> [Number] readInt32Table_0(tableName, opts)



\&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readInt32Table_0(tableName, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements) | 
 **startIndex** | **Number**| Index of first element to read (default is 0) | [optional] 
 **numElements** | **Number**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt32Tables_0

> [TableDef] readInt32Tables_0()



Returns an array of the name and length of all the integer32 tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
apiInstance.readInt32Tables_0((error, data, response) => {
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

[**[TableDef]**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64TableAsString_0

> [String] readInt64TableAsString_0(tableName, opts)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readInt64TableAsString_0(tableName, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements) | 
 **startIndex** | **Number**| Index of first element to read (default is 0) | [optional] 
 **numElements** | **Number**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64TableElementAsString_0

> Int64StringValueObject readInt64TableElementAsString_0(tableName, index)



Read specified integer64 table element as string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of integer64 table to read
let index = 56; // Number | Index of element to read
apiInstance.readInt64TableElementAsString_0(tableName, index, (error, data, response) => {
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
 **tableName** | **String**| Name of integer64 table to read | 
 **index** | **Number**| Index of element to read | 

### Return type

[**Int64StringValueObject**](Int64StringValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64TableElement_0

> Int64ValueObject readInt64TableElement_0(tableName, index)



Read specified integer64 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of integer64 table to read
let index = 56; // Number | Index of element to read
apiInstance.readInt64TableElement_0(tableName, index, (error, data, response) => {
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
 **tableName** | **String**| Name of integer64 table to read | 
 **index** | **Number**| Index of element to read | 

### Return type

[**Int64ValueObject**](Int64ValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64Table_0

> [Number] readInt64Table_0(tableName, opts)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readInt64Table_0(tableName, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements) | 
 **startIndex** | **Number**| Index of first element to read (default is 0) | [optional] 
 **numElements** | **Number**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] 

### Return type

**[Number]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64Tables_0

> [TableDef] readInt64Tables_0()



Returns an array of the name and length of all the integer64 tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
apiInstance.readInt64Tables_0((error, data, response) => {
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

[**[TableDef]**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStringTableElement_0

> StringValueObject readStringTableElement_0(tableName, index)



Read specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of string table to read
let index = 56; // Number | Index of element to read
apiInstance.readStringTableElement_0(tableName, index, (error, data, response) => {
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
 **tableName** | **String**| Name of string table to read | 
 **index** | **Number**| Index of element to read | 

### Return type

[**StringValueObject**](StringValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStringTable_0

> [String] readStringTable_0(tableName, opts)



\&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of string table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readStringTable_0(tableName, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of string table to read; starting index and number of elements may be specified (defaults to all elements) | 
 **startIndex** | **Number**| Index of first element to read (default is 0) | [optional] 
 **numElements** | **Number**| Number of elements to read (default is number of elements in the table minus startIndex) | [optional] 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStringTables_0

> [TableDef] readStringTables_0()



Returns an array of the name and length of all the string tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
apiInstance.readStringTables_0((error, data, response) => {
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

[**[TableDef]**](TableDef.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## writeFloatTableElement_0

> writeFloatTableElement_0(tableName, index, floatElementObject)



Write specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of float table to write
let index = 56; // Number | Index of element to write
let floatElementObject = new PacControlRestApi.FloatValueObject(); // FloatValueObject | Element to write starting at index
apiInstance.writeFloatTableElement_0(tableName, index, floatElementObject, (error, data, response) => {
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
 **tableName** | **String**| Name of float table to write | 
 **index** | **Number**| Index of element to write | 
 **floatElementObject** | [**FloatValueObject**](FloatValueObject.md)| Element to write starting at index | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeFloatTable_0

> writeFloatTable_0(tableName, floatArray, opts)



Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of float table to write; starting index may be specified
let floatArray = [null]; // [Number] | Array of element values to write starting at startIndex
let opts = {
  'startIndex': 56 // Number | Index of first element to write (default is 0)
};
apiInstance.writeFloatTable_0(tableName, floatArray, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of float table to write; starting index may be specified | 
 **floatArray** | [**[Number]**](Number.md)| Array of element values to write starting at startIndex | 
 **startIndex** | **Number**| Index of first element to write (default is 0) | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt32TableElement_0

> writeInt32TableElement_0(tableName, index, int32ElementObject)



Write specified integer32 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of the integer32 table to write
let index = 56; // Number | Index of element to write
let int32ElementObject = new PacControlRestApi.Int32ValueObject(); // Int32ValueObject | Element to write at index specified
apiInstance.writeInt32TableElement_0(tableName, index, int32ElementObject, (error, data, response) => {
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
 **tableName** | **String**| Name of the integer32 table to write | 
 **index** | **Number**| Index of element to write | 
 **int32ElementObject** | [**Int32ValueObject**](Int32ValueObject.md)| Element to write at index specified | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt32Table_0

> writeInt32Table_0(tableName, int32Array, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of integer32 table to write; starting index may be specified
let int32Array = [null]; // [Number] | Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored
let opts = {
  'startIndex': 56 // Number | Index of first element to write (default is 0)
};
apiInstance.writeInt32Table_0(tableName, int32Array, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of integer32 table to write; starting index may be specified | 
 **int32Array** | [**[Number]**](Number.md)| Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored | 
 **startIndex** | **Number**| Index of first element to write (default is 0) | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt64TableAsString_0

> writeInt64TableAsString_0(tableName, int64AsStringArray, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
let int64AsStringArray = ["null"]; // [String] | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
let opts = {
  'startIndex': 56 // Number | Index of first element to write; default is 0.
};
apiInstance.writeInt64TableAsString_0(tableName, int64AsStringArray, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of integer64 table to write; starting index may be specified | 
 **int64AsStringArray** | [**[String]**](String.md)| Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored | 
 **startIndex** | **Number**| Index of first element to write; default is 0. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt64TableElementAsString_0

> writeInt64TableElementAsString_0(tableName, index, int64ElementObject)



Write specified integer64 table element as string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to write
let index = 56; // Number | Index of element to write
let int64ElementObject = new PacControlRestApi.Int64StringValueObject(); // Int64StringValueObject | Element to write starting at index specified
apiInstance.writeInt64TableElementAsString_0(tableName, index, int64ElementObject, (error, data, response) => {
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
 **tableName** | **String**| Name of the integer64 table to write | 
 **index** | **Number**| Index of element to write | 
 **int64ElementObject** | [**Int64StringValueObject**](Int64StringValueObject.md)| Element to write starting at index specified | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt64TableElement_0

> writeInt64TableElement_0(tableName, index, int64ElementObject)



Write specified integer64 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to write
let index = 56; // Number | Index of element to write
let int64ElementObject = new PacControlRestApi.Int64ValueObject(); // Int64ValueObject | Element to write starting at index specified
apiInstance.writeInt64TableElement_0(tableName, index, int64ElementObject, (error, data, response) => {
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
 **tableName** | **String**| Name of the integer64 table to write | 
 **index** | **Number**| Index of element to write | 
 **int64ElementObject** | [**Int64ValueObject**](Int64ValueObject.md)| Element to write starting at index specified | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt64Table_0

> writeInt64Table_0(tableName, int64Array, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
let int64Array = [null]; // [Number] | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
let opts = {
  'startIndex': 56 // Number | Index of first element to write; default is 0
};
apiInstance.writeInt64Table_0(tableName, int64Array, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of integer64 table to write; starting index may be specified | 
 **int64Array** | [**[Number]**](Number.md)| Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored | 
 **startIndex** | **Number**| Index of first element to write; default is 0 | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeStringTableElement_0

> writeStringTableElement_0(tableName, index, stringElementObject)



Write specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of string table to write
let index = 56; // Number | Index of element to write
let stringElementObject = new PacControlRestApi.StringValueObject(); // StringValueObject | Element to write starting at index
apiInstance.writeStringTableElement_0(tableName, index, stringElementObject, (error, data, response) => {
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
 **tableName** | **String**| Name of string table to write | 
 **index** | **Number**| Index of element to write | 
 **stringElementObject** | [**StringValueObject**](StringValueObject.md)| Element to write starting at index | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeStringTable_0

> ErrorResponse200OKish writeStringTable_0(tableName, stringArray, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.TablesApi();
let tableName = "tableName_example"; // String | Name of string table to write; starting index may be specified
let stringArray = ["null"]; // [String] | Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit
let opts = {
  'startIndex': 56 // Number | Index of first element to write (default is 0)
};
apiInstance.writeStringTable_0(tableName, stringArray, opts, (error, data, response) => {
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
 **tableName** | **String**| Name of string table to write; starting index may be specified | 
 **stringArray** | [**[String]**](String.md)| Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit | 
 **startIndex** | **Number**| Index of first element to write (default is 0) | [optional] 

### Return type

[**ErrorResponse200OKish**](ErrorResponse200OKish.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

