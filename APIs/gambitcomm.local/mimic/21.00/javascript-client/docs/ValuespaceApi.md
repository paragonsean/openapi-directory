# MimicRestApi.ValuespaceApi

All URIs are relative to *http://gambitcomm.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ValuespaceApi.md#add) | **POST** /mimic/agent/{agentNum}/value/add/{object}/{instance} | Add an entry to a table.
[**evalValue**](ValuespaceApi.md#evalValue) | **GET** /mimic/agent/{agentNum}/value/eval/{object}/{instance} | Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.
[**getInfo**](ValuespaceApi.md#getInfo) | **GET** /mimic/agent/{agentNum}/value/info/{object} | Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.
[**getInstances**](ValuespaceApi.md#getInstances) | **GET** /mimic/agent/{agentNum}/value/instances/{object} | Display the MIB object instances for the specified object.
[**getMib**](ValuespaceApi.md#getMib) | **GET** /mimic/agent/{agentNum}/value/mib/{object} | Return the MIB that defines the specified object.
[**getName**](ValuespaceApi.md#getName) | **GET** /mimic/agent/{agentNum}/value/name/{OID} | Return the symbolic name of the specified object identifier.
[**getObjects**](ValuespaceApi.md#getObjects) | **GET** /mimic/agent/{agentNum}/value/list/{OID} | Display the MIB objects below the current position
[**getOid**](ValuespaceApi.md#getOid) | **GET** /mimic/agent/{agentNum}/value/oid/{object} | Return the numeric OID of the specified object.
[**getState**](ValuespaceApi.md#getState) | **GET** /mimic/agent/{agentNum}/value/state/get/{object} | Get the state of a MIB object object.
[**getValue**](ValuespaceApi.md#getValue) | **GET** /mimic/agent/{agentNum}/value/get/{object}/{instance}/{variable} | Get a variable in the Value Space.
[**getVariables**](ValuespaceApi.md#getVariables) | **GET** /mimic/agent/{agentNum}/value/variables/{object}/{instance} | Display the variables for the specified instance instance for the specified MIB object object
[**mevalValue**](ValuespaceApi.md#mevalValue) | **GET** /mimic/agent/{agentNum}/value/meval/{objInsArray} | Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.
[**mgetValue**](ValuespaceApi.md#mgetValue) | **GET** /mimic/agent/{agentNum}/value/mget/{objInsVarArray} | Get multiple variables in the Value Space.
[**msetValue**](ValuespaceApi.md#msetValue) | **PUT** /mimic/agent/{agentNum}/value/mset | Set multiple variables in the Value Space.
[**munsetValue**](ValuespaceApi.md#munsetValue) | **PUT** /mimic/agent/{agentNum}/value/munset | Unset multiple variables in the Value Space
[**remove**](ValuespaceApi.md#remove) | **DELETE** /mimic/agent/{agentNum}/value/remove/{object}/{instance} | Remove an entry from a table.
[**setState**](ValuespaceApi.md#setState) | **PUT** /mimic/agent/{agentNum}/value/state/set/{object}/{state} | Set the state of a MIB object object
[**setValue**](ValuespaceApi.md#setValue) | **PUT** /mimic/agent/{agentNum}/value/set/{object}/{instance}/{variable} | Set a variable in the Value Space.
[**splitOid**](ValuespaceApi.md#splitOid) | **GET** /mimic/agent/{agentNum}/value/split/{OID} | Split the numerical OID into the object OID and instance OID.
[**unsetValue**](ValuespaceApi.md#unsetValue) | **PUT** /mimic/agent/{agentNum}/value/unset/{object}/{instance}/{variable} | Unset a variable in the Value Space in order to free its memory.



## add

> String add(agentNum, object, instance)

Add an entry to a table.

The object needs to specify the MIB object with the INDEX clause, usually an object whose name ends with Entry.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Object (column) of the table in the agent's value space
let instance = "instance_example"; // String | Object (column) of the table in the agent's value space
apiInstance.add(agentNum, object, instance, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Object (column) of the table in the agent&#39;s value space | 
 **instance** | **String**| Object (column) of the table in the agent&#39;s value space | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## evalValue

> String evalValue(agentNum, object, instance)

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
let instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
apiInstance.evalValue(agentNum, object, instance, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | 
 **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInfo

> String getInfo(agentNum, object)

Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.

Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent to show the information of the object
let object = "object_example"; // String | Object
apiInstance.getInfo(agentNum, object, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the information of the object | 
 **object** | **String**| Object | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInstances

> [String] getInstances(agentNum, object)

Display the MIB object instances for the specified object.

This enables MIB browsing of the MIB on the current agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Object (column) of the table in the agent's value space
apiInstance.getInstances(agentNum, object, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Object (column) of the table in the agent&#39;s value space | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMib

> String getMib(agentNum, object)

Return the MIB that defines the specified object.

This will only return a MIB name if the object is unmistakeably defined in a MIB.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent to show the MIB
let object = "object_example"; // String | Object
apiInstance.getMib(agentNum, object, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the MIB | 
 **object** | **String**| Object | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getName

> String getName(agentNum, OID)

Return the symbolic name of the specified object identifier.

Return the symbolic name of the specified object identifier.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent to show the object
let OID = "OID_example"; // String | OID
apiInstance.getName(agentNum, OID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the object | 
 **OID** | **String**| OID | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getObjects

> [String] getObjects(agentNum, OID)

Display the MIB objects below the current position

This command is similar to the ls or dir operating system commands to list filesystem directories.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent to show the OID branches
let OID = "OID_example"; // String | Current OID
apiInstance.getObjects(agentNum, OID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the OID branches | 
 **OID** | **String**| Current OID | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOid

> String getOid(agentNum, object)

Return the numeric OID of the specified object.

Return the numeric OID of the specified object.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent to show the OID
let object = "object_example"; // String | Object
apiInstance.getOid(agentNum, object, (error, data, response) => {
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
 **agentNum** | **Number**| Agent to show the OID | 
 **object** | **String**| Object | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getState

> String getState(agentNum, object)

Get the state of a MIB object object.

To disable traversal into a MIB object and any subtree underneath, set the state to 0, else set the state to 1.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Object
apiInstance.getState(agentNum, object, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Object | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getValue

> String getValue(agentNum, object, instance, variable)

Get a variable in the Value Space.

Get a variable in the Value Space.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Object (column) of the table in the agent's value space
let instance = "instance_example"; // String | Object (column) of the table in the agent's value space
let variable = "variable_example"; // String | Object (column) of the table in the agent's value space
apiInstance.getValue(agentNum, object, instance, variable, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Object (column) of the table in the agent&#39;s value space | 
 **instance** | **String**| Object (column) of the table in the agent&#39;s value space | 
 **variable** | **String**| Object (column) of the table in the agent&#39;s value space | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVariables

> [String] getVariables(agentNum, object, instance)

Display the variables for the specified instance instance for the specified MIB object object

This enables variable browsing of the MIB on the current agent.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
let instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
apiInstance.getVariables(agentNum, object, instance, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | 
 **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mevalValue

> [String] mevalValue(agentNum, objInsArray)

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let objInsArray = [null]; // [[String]] | Multiple objects or object (column) of the table in the agent's value space.
apiInstance.mevalValue(agentNum, objInsArray, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **objInsArray** | [**[[String]]**]([String].md)| Multiple objects or object (column) of the table in the agent&#39;s value space. | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mgetValue

> [String] mgetValue(agentNum, objInsVarArray)

Get multiple variables in the Value Space.

This is a performance optimization of the mimic value get command, to be used when many variables are requested.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let objInsVarArray = [null]; // [[String]] | Multiple objects or object (column) of the table in the agent's value space.
apiInstance.mgetValue(agentNum, objInsVarArray, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **objInsVarArray** | [**[[String]]**]([String].md)| Multiple objects or object (column) of the table in the agent&#39;s value space. | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## msetValue

> String msetValue(agentNum, opts)

Set multiple variables in the Value Space.

This is a performance optimization of the mimic value set command, to be used when many variables are to be set.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let opts = {
  'requestBody': [null] // [[String]] | objInsVarValArray
};
apiInstance.msetValue(agentNum, opts, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **requestBody** | [**[[String]]**](Array.md)| objInsVarValArray | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## munsetValue

> String munsetValue(agentNum, opts)

Unset multiple variables in the Value Space

This is a performance optimization of the mimic value unset command, to be used when many variables are to be unset.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let opts = {
  'requestBody': [null] // [[String]] | objInsVarArray
};
apiInstance.munsetValue(agentNum, opts, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **requestBody** | [**[[String]]**](Array.md)| objInsVarArray | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## remove

> String remove(agentNum, object, instance)

Remove an entry from a table.

The object needs to specify the MIB object with the INDEX clause, usually an object whose name ends with Entry.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Object (column) of the table in the agent's value space
let instance = "instance_example"; // String | Object (column) of the table in the agent's value space
apiInstance.remove(agentNum, object, instance, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Object (column) of the table in the agent&#39;s value space | 
 **instance** | **String**| Object (column) of the table in the agent&#39;s value space | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setState

> String setState(agentNum, object, state)

Set the state of a MIB object object

To disable traversal into a MIB object and any subtree underneath, set the state to 0, else set the state to 1.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Object
let state = 56; // Number | State
apiInstance.setState(agentNum, object, state, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Object | 
 **state** | **Number**| State | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setValue

> String setValue(agentNum, object, instance, variable, opts)

Set a variable in the Value Space.

NOTE to set a binary string value, specify a string starting with \\\\x followed by pairs of hexadecimal digits, eg. \&quot;\\\\x 01 23 45\&quot;. This command also assigns SNMP PDU action scripts for GET* and SET requests on a MIB object. The instance parameter must be 0. The following variables enable actions, g - The specified TCL script will be run on GET or GETNEXT requests. It has to exist under the simulation directory. s - The specified script will be run on SET requests. It has to exist under the simulation directory. This command also controls advanced trap generation functionality. The following variables control trap generation r, tu, c - These variables together represent the rate settings for the trap. r and tu is the actual per second rate and c represents the total duration in seconds for which the trap is sent. As soon as the c variable is set, the trap generation begins, for this reason it should be the last variable set for a particular trap. The following variables have to be set before setting the c variable to modify the behavior of the generated trap(s). OBJECT - An object name when used as a variable is looked up during the trap send and the value of that variable is included in the PDU. OBJECT.i - This type of variable will be used to assign an optional instance for the specified object in the traps varbind. The value of this variable identifies the index. e.g. The commands below will send ifIndex.2 with a value of 5 in the linkUp trap PDU. i - This variable is used to specify any extra version specific information to the trap generation code. Here is what it can be used to represent for various SNMP versions SNMPv1 - [community_string][,[enterprise][,agent_addr]] SNMPv2c - community_string SNMPv2 - source_party,destination_party,context SNMPv3 - user_name,context v - This variable lets the user override the version of the PDU being generated. The possible values are - \&quot;1\&quot;, \&quot;2c\&quot;, \&quot;2\&quot; and \&quot;3\&quot;. o - This variable is used for traps that need extra variables to be added to the PDU along with the ones defined in the MIB as its variables. This lets the user force extra objects (along with instances if needed). All variables to be sent need to be assigned to the o variable. O - To omit any variables which are defined in the MIB you can use the O (capital o) variable. This needs to be set to the list of OIDs of the variable bindings in the order defined in the MIB. ip - The variable ip is used for generating the trap from the N-th IP alias address. a - This variable associates an action script to the trap or INFORM request. The action script specified in the value of this variable has to exist in the simulation directory. It will be executed before each instance of the trap is sent out. I - This optional variable controls the generation of INFORM PDUs. An INFORM is sent only if the variable is non-zero, else a TRAP is generated. R, T, E - This variable associates an action script to the INFORM request. The action script specified in the value of this variable has to exist in the simulation directory. The action script associated with the R variable will be executed on receiving a INFORM RESPONSE, the one associated with the T variable on a timeout (ie. no response), the one associated with the E variable on a report PDU. eid.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine id for the destination specified by IP-ADDRESS and optionally by PORT. eb.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine boots. et.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine time.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
let instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
let variable = "variable_example"; // String | Variable
let opts = {
  'body': "body_example" // String | Value
};
apiInstance.setValue(agentNum, object, instance, variable, opts, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | 
 **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | 
 **variable** | **String**| Variable | 
 **body** | **String**| Value | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## splitOid

> [String] splitOid(agentNum, OID)

Split the numerical OID into the object OID and instance OID.

This is useful if you have an OID which is a combination of object and instance.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let OID = "OID_example"; // String | OID
apiInstance.splitOid(agentNum, OID, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **OID** | **String**| OID | 

### Return type

**[String]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unsetValue

> String unsetValue(agentNum, object, instance, variable)

Unset a variable in the Value Space in order to free its memory.

Only variables that have previously been set can be unset.

### Example

```javascript
import MimicRestApi from 'mimic_rest_api';
let defaultClient = MimicRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new MimicRestApi.ValuespaceApi();
let agentNum = 56; // Number | Agent of the value space
let object = "object_example"; // String | Single instance object or object (column) of the table in the agent's value space.
let instance = "instance_example"; // String | Row of the table in the agent's value space. 0 for single instance objects
let variable = "variable_example"; // String | Variable
apiInstance.unsetValue(agentNum, object, instance, variable, (error, data, response) => {
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
 **agentNum** | **Number**| Agent of the value space | 
 **object** | **String**| Single instance object or object (column) of the table in the agent&#39;s value space. | 
 **instance** | **String**| Row of the table in the agent&#39;s value space. 0 for single instance objects | 
 **variable** | **String**| Variable | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

