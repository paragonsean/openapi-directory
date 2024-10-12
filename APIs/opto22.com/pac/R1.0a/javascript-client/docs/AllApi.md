# PacControlRestApi.AllApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readAnalogInputEu**](AllApi.md#readAnalogInputEu) | **GET** /device/strategy/ios/analogInputs/{ioName}/eu | 
[**readAnalogInputs**](AllApi.md#readAnalogInputs) | **GET** /device/strategy/ios/analogInputs | 
[**readAnalogOutputEu**](AllApi.md#readAnalogOutputEu) | **GET** /device/strategy/ios/analogOutputs/{ioName}/eu | 
[**readAnalogOutputs**](AllApi.md#readAnalogOutputs) | **GET** /device/strategy/ios/analogOutputs | 
[**readDeviceDetails**](AllApi.md#readDeviceDetails) | **GET** /device | 
[**readDigitalInputState**](AllApi.md#readDigitalInputState) | **GET** /device/strategy/ios/digitalInputs/{ioName}/state | 
[**readDigitalInputs**](AllApi.md#readDigitalInputs) | **GET** /device/strategy/ios/digitalInputs | 
[**readDigitalOutputState**](AllApi.md#readDigitalOutputState) | **GET** /device/strategy/ios/digitalOutputs/{ioName}/state | 
[**readDigitalOutputs**](AllApi.md#readDigitalOutputs) | **GET** /device/strategy/ios/digitalOutputs | 
[**readDownTimerValue**](AllApi.md#readDownTimerValue) | **GET** /device/strategy/vars/downTimers/{downTimerName}/value | 
[**readDownTimerVars**](AllApi.md#readDownTimerVars) | **GET** /device/strategy/vars/downTimers | 
[**readFloatTable**](AllApi.md#readFloatTable) | **GET** /device/strategy/tables/floats/{tableName} | 
[**readFloatTableElement**](AllApi.md#readFloatTableElement) | **GET** /device/strategy/tables/floats/{tableName}/{index} | 
[**readFloatTables**](AllApi.md#readFloatTables) | **GET** /device/strategy/tables/floats | 
[**readFloatVar**](AllApi.md#readFloatVar) | **GET** /device/strategy/vars/floats/{floatName} | 
[**readFloatVars**](AllApi.md#readFloatVars) | **GET** /device/strategy/vars/floats | 
[**readInt32Table**](AllApi.md#readInt32Table) | **GET** /device/strategy/tables/int32s/{tableName} | 
[**readInt32TableElement**](AllApi.md#readInt32TableElement) | **GET** /device/strategy/tables/int32s/{tableName}/{index} | 
[**readInt32Tables**](AllApi.md#readInt32Tables) | **GET** /device/strategy/tables/int32s | 
[**readInt32Var**](AllApi.md#readInt32Var) | **GET** /device/strategy/vars/int32s/{int32Name} | 
[**readInt32Vars**](AllApi.md#readInt32Vars) | **GET** /device/strategy/vars/int32s | 
[**readInt64Table**](AllApi.md#readInt64Table) | **GET** /device/strategy/tables/int64s/{tableName} | 
[**readInt64TableAsString**](AllApi.md#readInt64TableAsString) | **GET** /device/strategy/tables/int64s/{tableName}/_string | 
[**readInt64TableElement**](AllApi.md#readInt64TableElement) | **GET** /device/strategy/tables/int64s/{tableName}/{index} | 
[**readInt64TableElementAsString**](AllApi.md#readInt64TableElementAsString) | **GET** /device/strategy/tables/int64s/{tableName}/{index}/_string | 
[**readInt64Tables**](AllApi.md#readInt64Tables) | **GET** /device/strategy/tables/int64s | 
[**readInt64Var**](AllApi.md#readInt64Var) | **GET** /device/strategy/vars/int64s/{int64Name} | 
[**readInt64VarAsString**](AllApi.md#readInt64VarAsString) | **GET** /device/strategy/vars/int64s/{int64Name}/_string | 
[**readInt64Vars**](AllApi.md#readInt64Vars) | **GET** /device/strategy/vars/int64s | 
[**readInt64VarsAsStrings**](AllApi.md#readInt64VarsAsStrings) | **GET** /device/strategy/vars/int64s/_string | 
[**readStrategyDetails**](AllApi.md#readStrategyDetails) | **GET** /device/strategy | 
[**readStringTable**](AllApi.md#readStringTable) | **GET** /device/strategy/tables/strings/{tableName} | 
[**readStringTableElement**](AllApi.md#readStringTableElement) | **GET** /device/strategy/tables/strings/{tableName}/{index} | 
[**readStringTables**](AllApi.md#readStringTables) | **GET** /device/strategy/tables/strings | 
[**readStringVar**](AllApi.md#readStringVar) | **GET** /device/strategy/vars/strings/{stringName} | 
[**readStringVars**](AllApi.md#readStringVars) | **GET** /device/strategy/vars/strings | 
[**readUpTimerValue**](AllApi.md#readUpTimerValue) | **GET** /device/strategy/vars/upTimers/{upTimerName}/value | 
[**readUpTimerVars**](AllApi.md#readUpTimerVars) | **GET** /device/strategy/vars/upTimers | 
[**writeAnalogOutputEu**](AllApi.md#writeAnalogOutputEu) | **POST** /device/strategy/ios/analogOutputs/{ioName}/eu | 
[**writeDigitalOutputState**](AllApi.md#writeDigitalOutputState) | **POST** /device/strategy/ios/digitalOutputs/{ioName}/state | 
[**writeFloatTable**](AllApi.md#writeFloatTable) | **POST** /device/strategy/tables/floats/{tableName} | 
[**writeFloatTableElement**](AllApi.md#writeFloatTableElement) | **POST** /device/strategy/tables/floats/{tableName}/{index} | 
[**writeFloatVar**](AllApi.md#writeFloatVar) | **POST** /device/strategy/vars/floats/{floatName} | 
[**writeInt32Table**](AllApi.md#writeInt32Table) | **POST** /device/strategy/tables/int32s/{tableName} | 
[**writeInt32TableElement**](AllApi.md#writeInt32TableElement) | **POST** /device/strategy/tables/int32s/{tableName}/{index} | 
[**writeInt32Var**](AllApi.md#writeInt32Var) | **POST** /device/strategy/vars/int32s/{int32Name} | 
[**writeInt64Table**](AllApi.md#writeInt64Table) | **POST** /device/strategy/tables/int64s/{tableName} | 
[**writeInt64TableAsString**](AllApi.md#writeInt64TableAsString) | **POST** /device/strategy/tables/int64s/{tableName}/_string | 
[**writeInt64TableElement**](AllApi.md#writeInt64TableElement) | **POST** /device/strategy/tables/int64s/{tableName}/{index} | 
[**writeInt64TableElementAsString**](AllApi.md#writeInt64TableElementAsString) | **POST** /device/strategy/tables/int64s/{tableName}/{index}/_string | 
[**writeInt64Var**](AllApi.md#writeInt64Var) | **POST** /device/strategy/vars/int64s/{int64Name} | 
[**writeInt64VarAsString**](AllApi.md#writeInt64VarAsString) | **POST** /device/strategy/vars/int64s/{int64Name}/_string | 
[**writeStringTable**](AllApi.md#writeStringTable) | **POST** /device/strategy/tables/strings/{tableName} | 
[**writeStringTableElement**](AllApi.md#writeStringTableElement) | **POST** /device/strategy/tables/strings/{tableName}/{index} | 
[**writeStringVar**](AllApi.md#writeStringVar) | **POST** /device/strategy/vars/strings/{stringName} | 



## readAnalogInputEu

> FloatValueObject readAnalogInputEu(ioName)



Reads the value in engineering units (EU) of the specified analog input

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let ioName = "ioName_example"; // String | Name of the analog input point to read
apiInstance.readAnalogInputEu(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of the analog input point to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readAnalogInputs

> [FloatVar] readAnalogInputs()



Returns the name and engineering units (EU) for all analog input points in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readAnalogInputs((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readAnalogOutputEu

> FloatValueObject readAnalogOutputEu(ioName)



Reads the value in engineering units (EU) of the specified analog output

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let ioName = "ioName_example"; // String | Name of analog output point to read
apiInstance.readAnalogOutputEu(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of analog output point to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readAnalogOutputs

> [FloatVar] readAnalogOutputs()



Returns the name and engineering units (EU) for all analog output points in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readAnalogOutputs((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDeviceDetails

> ControllerResponse readDeviceDetails()



Returns controller&#39;s type; firmware version; both mac addresses; and uptime in seconds

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readDeviceDetails((error, data, response) => {
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

[**ControllerResponse**](ControllerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalInputState

> DigitalPointStateObject readDigitalInputState(ioName)



Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let ioName = "ioName_example"; // String | Name of the digital input point to read
apiInstance.readDigitalInputState(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of the digital input point to read | 

### Return type

[**DigitalPointStateObject**](DigitalPointStateObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalInputs

> [DigitalPointStateVar] readDigitalInputs()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readDigitalInputs((error, data, response) => {
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

[**[DigitalPointStateVar]**](DigitalPointStateVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalOutputState

> DigitalPointStateObject readDigitalOutputState(ioName)



Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let ioName = "ioName_example"; // String | Name of the digit output point to read
apiInstance.readDigitalOutputState(ioName, (error, data, response) => {
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
 **ioName** | **String**| Name of the digit output point to read | 

### Return type

[**DigitalPointStateObject**](DigitalPointStateObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDigitalOutputs

> [DigitalPointStateVar] readDigitalOutputs()



Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readDigitalOutputs((error, data, response) => {
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

[**[DigitalPointStateVar]**](DigitalPointStateVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDownTimerValue

> FloatValueObject readDownTimerValue(downTimerName)



Returns current value of the specified down timer

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let downTimerName = "downTimerName_example"; // String | Name of the down timer variable to read
apiInstance.readDownTimerValue(downTimerName, (error, data, response) => {
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
 **downTimerName** | **String**| Name of the down timer variable to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readDownTimerVars

> [FloatVar] readDownTimerVars()



Returns the name and current value of all down timers in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readDownTimerVars((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readFloatTable

> [Number] readFloatTable(tableName, opts)



Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of float table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readFloatTable(tableName, opts, (error, data, response) => {
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


## readFloatTableElement

> FloatValueObject readFloatTableElement(tableName, index)



Read specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of float table to read
let index = 56; // Number | Index of element to read
apiInstance.readFloatTableElement(tableName, index, (error, data, response) => {
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


## readFloatTables

> [TableDef] readFloatTables()



Returns an array of the name and length of all the float tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readFloatTables((error, data, response) => {
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


## readFloatVar

> FloatValueObject readFloatVar(floatName)



Returns value of the specified float variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let floatName = "floatName_example"; // String | Name of float variable to read
apiInstance.readFloatVar(floatName, (error, data, response) => {
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
 **floatName** | **String**| Name of float variable to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readFloatVars

> [FloatVar] readFloatVars()



Returns the name and value of all (single-precision) float variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readFloatVars((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt32Table

> [Number] readInt32Table(tableName, opts)



\&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of integer32 table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readInt32Table(tableName, opts, (error, data, response) => {
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


## readInt32TableElement

> Int32ValueObject readInt32TableElement(tableName, index)



Read specified integer32 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of the integer32 table to read
let index = 56; // Number | Index of element to read
apiInstance.readInt32TableElement(tableName, index, (error, data, response) => {
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


## readInt32Tables

> [TableDef] readInt32Tables()



Returns an array of the name and length of all the integer32 tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readInt32Tables((error, data, response) => {
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


## readInt32Var

> Int32ValueObject readInt32Var(int32Name)



Returns value of the specified integer32 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let int32Name = "int32Name_example"; // String | Name of integer32 variable to read
apiInstance.readInt32Var(int32Name, (error, data, response) => {
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
 **int32Name** | **String**| Name of integer32 variable to read | 

### Return type

[**Int32ValueObject**](Int32ValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt32Vars

> [Int32Var] readInt32Vars()



Returns the name and value of all integer32 variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readInt32Vars((error, data, response) => {
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

[**[Int32Var]**](Int32Var.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64Table

> [Number] readInt64Table(tableName, opts)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readInt64Table(tableName, opts, (error, data, response) => {
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


## readInt64TableAsString

> [String] readInt64TableAsString(tableName, opts)



\&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readInt64TableAsString(tableName, opts, (error, data, response) => {
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


## readInt64TableElement

> Int64ValueObject readInt64TableElement(tableName, index)



Read specified integer64 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of integer64 table to read
let index = 56; // Number | Index of element to read
apiInstance.readInt64TableElement(tableName, index, (error, data, response) => {
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


## readInt64TableElementAsString

> Int64StringValueObject readInt64TableElementAsString(tableName, index)



Read specified integer64 table element as string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of integer64 table to read
let index = 56; // Number | Index of element to read
apiInstance.readInt64TableElementAsString(tableName, index, (error, data, response) => {
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


## readInt64Tables

> [TableDef] readInt64Tables()



Returns an array of the name and length of all the integer64 tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readInt64Tables((error, data, response) => {
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


## readInt64Var

> Int64ValueObject readInt64Var(int64Name)



Returns value of the specified integer64 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to read
apiInstance.readInt64Var(int64Name, (error, data, response) => {
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
 **int64Name** | **String**| Name of integer64 variable to read | 

### Return type

[**Int64ValueObject**](Int64ValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64VarAsString

> Int64StringValueObject readInt64VarAsString(int64Name)



Returns value of the specified integer64 variable as a string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to read
apiInstance.readInt64VarAsString(int64Name, (error, data, response) => {
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
 **int64Name** | **String**| Name of integer64 variable to read | 

### Return type

[**Int64StringValueObject**](Int64StringValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64Vars

> [Int64Var] readInt64Vars()



Returns the name and value of all integer64 variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readInt64Vars((error, data, response) => {
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

[**[Int64Var]**](Int64Var.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readInt64VarsAsStrings

> [Int64VarAsString] readInt64VarsAsStrings()



Returns the name and value as a string of all integer64 variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readInt64VarsAsStrings((error, data, response) => {
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

[**[Int64VarAsString]**](Int64VarAsString.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStrategyDetails

> StrategyResponse readStrategyDetails()



Returns the name, date, time, and CRC of the strategy currently in the controller, and the number of charts currently running. Empty strings and a 0 will be returned when there is no strategy.

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readStrategyDetails((error, data, response) => {
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

[**StrategyResponse**](StrategyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStringTable

> [String] readStringTable(tableName, opts)



\&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of string table to read; starting index and number of elements may be specified (defaults to all elements)
let opts = {
  'startIndex': 56, // Number | Index of first element to read (default is 0)
  'numElements': 56 // Number | Number of elements to read (default is number of elements in the table minus startIndex)
};
apiInstance.readStringTable(tableName, opts, (error, data, response) => {
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


## readStringTableElement

> StringValueObject readStringTableElement(tableName, index)



Read specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of string table to read
let index = 56; // Number | Index of element to read
apiInstance.readStringTableElement(tableName, index, (error, data, response) => {
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


## readStringTables

> [TableDef] readStringTables()



Returns an array of the name and length of all the string tables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readStringTables((error, data, response) => {
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


## readStringVar

> StringValueObject readStringVar(stringName)



Returns value of the specified string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let stringName = "stringName_example"; // String | Name of string variable to read
apiInstance.readStringVar(stringName, (error, data, response) => {
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
 **stringName** | **String**| Name of string variable to read | 

### Return type

[**StringValueObject**](StringValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readStringVars

> [StringVar] readStringVars()



Returns the name and value of all string variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readStringVars((error, data, response) => {
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

[**[StringVar]**](StringVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readUpTimerValue

> FloatValueObject readUpTimerValue(upTimerName)



Returns current value of the specified up timer

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let upTimerName = "upTimerName_example"; // String | Name of the up timer variable to read
apiInstance.readUpTimerValue(upTimerName, (error, data, response) => {
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
 **upTimerName** | **String**| Name of the up timer variable to read | 

### Return type

[**FloatValueObject**](FloatValueObject.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readUpTimerVars

> [FloatVar] readUpTimerVars()



Returns the name and current value of all up timers in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
apiInstance.readUpTimerVars((error, data, response) => {
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

[**[FloatVar]**](FloatVar.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## writeAnalogOutputEu

> writeAnalogOutputEu(ioName, body)



Sets the value of the specified analog output point

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let ioName = "ioName_example"; // String | Name of the analog output point to write
let body = new PacControlRestApi.FloatValueObject(); // FloatValueObject | Value to write
apiInstance.writeAnalogOutputEu(ioName, body, (error, data, response) => {
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
 **ioName** | **String**| Name of the analog output point to write | 
 **body** | [**FloatValueObject**](FloatValueObject.md)| Value to write | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeDigitalOutputState

> writeDigitalOutputState(ioName, body)



Sets the value of the specified digital output point

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let ioName = "ioName_example"; // String | Name of the digital output point to write
let body = new PacControlRestApi.DigitalPointStateObject(); // DigitalPointStateObject | Value to write
apiInstance.writeDigitalOutputState(ioName, body, (error, data, response) => {
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
 **ioName** | **String**| Name of the digital output point to write | 
 **body** | [**DigitalPointStateObject**](DigitalPointStateObject.md)| Value to write | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeFloatTable

> writeFloatTable(tableName, floatArray, opts)



Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of float table to write; starting index may be specified
let floatArray = [null]; // [Number] | Array of element values to write starting at startIndex
let opts = {
  'startIndex': 56 // Number | Index of first element to write (default is 0)
};
apiInstance.writeFloatTable(tableName, floatArray, opts, (error, data, response) => {
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


## writeFloatTableElement

> writeFloatTableElement(tableName, index, floatElementObject)



Write specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of float table to write
let index = 56; // Number | Index of element to write
let floatElementObject = new PacControlRestApi.FloatValueObject(); // FloatValueObject | Element to write starting at index
apiInstance.writeFloatTableElement(tableName, index, floatElementObject, (error, data, response) => {
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


## writeFloatVar

> writeFloatVar(floatName, body)



Sets the value of a float variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let floatName = "floatName_example"; // String | Name of the float variable to write
let body = new PacControlRestApi.FloatValueObject(); // FloatValueObject | Value to write to the float variable
apiInstance.writeFloatVar(floatName, body, (error, data, response) => {
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
 **floatName** | **String**| Name of the float variable to write | 
 **body** | [**FloatValueObject**](FloatValueObject.md)| Value to write to the float variable | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt32Table

> writeInt32Table(tableName, int32Array, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of integer32 table to write; starting index may be specified
let int32Array = [null]; // [Number] | Array of element values to write starting at startIndex; if the list of elements is too long to fit in the specified table, extra elements will be ignored
let opts = {
  'startIndex': 56 // Number | Index of first element to write (default is 0)
};
apiInstance.writeInt32Table(tableName, int32Array, opts, (error, data, response) => {
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


## writeInt32TableElement

> writeInt32TableElement(tableName, index, int32ElementObject)



Write specified integer32 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of the integer32 table to write
let index = 56; // Number | Index of element to write
let int32ElementObject = new PacControlRestApi.Int32ValueObject(); // Int32ValueObject | Element to write at index specified
apiInstance.writeInt32TableElement(tableName, index, int32ElementObject, (error, data, response) => {
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


## writeInt32Var

> writeInt32Var(int32Name, body)



Sets the value of an integer32 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let int32Name = "int32Name_example"; // String | Name of integer32 variable to write
let body = new PacControlRestApi.Int32ValueObject(); // Int32ValueObject | Value to write to the integer32 variable
apiInstance.writeInt32Var(int32Name, body, (error, data, response) => {
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
 **int32Name** | **String**| Name of integer32 variable to write | 
 **body** | [**Int32ValueObject**](Int32ValueObject.md)| Value to write to the integer32 variable | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt64Table

> writeInt64Table(tableName, int64Array, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
let int64Array = [null]; // [Number] | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
let opts = {
  'startIndex': 56 // Number | Index of first element to write; default is 0
};
apiInstance.writeInt64Table(tableName, int64Array, opts, (error, data, response) => {
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


## writeInt64TableAsString

> writeInt64TableAsString(tableName, int64AsStringArray, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of integer64 table to write; starting index may be specified
let int64AsStringArray = ["null"]; // [String] | Array of element values to write starting at startIndex; if the array of elements is too long  to fit in the specified table, extra elements will be ignored
let opts = {
  'startIndex': 56 // Number | Index of first element to write; default is 0.
};
apiInstance.writeInt64TableAsString(tableName, int64AsStringArray, opts, (error, data, response) => {
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


## writeInt64TableElement

> writeInt64TableElement(tableName, index, int64ElementObject)



Write specified integer64 table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to write
let index = 56; // Number | Index of element to write
let int64ElementObject = new PacControlRestApi.Int64ValueObject(); // Int64ValueObject | Element to write starting at index specified
apiInstance.writeInt64TableElement(tableName, index, int64ElementObject, (error, data, response) => {
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


## writeInt64TableElementAsString

> writeInt64TableElementAsString(tableName, index, int64ElementObject)



Write specified integer64 table element as string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of the integer64 table to write
let index = 56; // Number | Index of element to write
let int64ElementObject = new PacControlRestApi.Int64StringValueObject(); // Int64StringValueObject | Element to write starting at index specified
apiInstance.writeInt64TableElementAsString(tableName, index, int64ElementObject, (error, data, response) => {
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


## writeInt64Var

> writeInt64Var(int64Name, body)



Sets the value of an integer64 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to write
let body = new PacControlRestApi.Int64ValueObject(); // Int64ValueObject | Value to write to the integer64 variable
apiInstance.writeInt64Var(int64Name, body, (error, data, response) => {
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
 **int64Name** | **String**| Name of integer64 variable to write | 
 **body** | [**Int64ValueObject**](Int64ValueObject.md)| Value to write to the integer64 variable | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeInt64VarAsString

> writeInt64VarAsString(int64Name, body)



Sets the value of an integer64 variable as a string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to write
let body = new PacControlRestApi.Int64StringValueObject(); // Int64StringValueObject | Value to write to the integer64 variable
apiInstance.writeInt64VarAsString(int64Name, body, (error, data, response) => {
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
 **int64Name** | **String**| Name of integer64 variable to write | 
 **body** | [**Int64StringValueObject**](Int64StringValueObject.md)| Value to write to the integer64 variable | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeStringTable

> ErrorResponse200OKish writeStringTable(tableName, stringArray, opts)



\&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of string table to write; starting index may be specified
let stringArray = ["null"]; // [String] | Array of element values to write starting at startIndex; if an element value is longer than the string width, the string will be truncated to fit
let opts = {
  'startIndex': 56 // Number | Index of first element to write (default is 0)
};
apiInstance.writeStringTable(tableName, stringArray, opts, (error, data, response) => {
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


## writeStringTableElement

> writeStringTableElement(tableName, index, stringElementObject)



Write specified table element

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let tableName = "tableName_example"; // String | Name of string table to write
let index = 56; // Number | Index of element to write
let stringElementObject = new PacControlRestApi.StringValueObject(); // StringValueObject | Element to write starting at index
apiInstance.writeStringTableElement(tableName, index, stringElementObject, (error, data, response) => {
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


## writeStringVar

> ErrorResponse200OKish writeStringVar(stringName, body)



Sets the value of a string variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.AllApi();
let stringName = "stringName_example"; // String | Name of string variable to write
let body = new PacControlRestApi.StringValueObject(); // StringValueObject | String to write. If the value is longer than the string width, the string will be truncated to fit.
apiInstance.writeStringVar(stringName, body, (error, data, response) => {
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
 **stringName** | **String**| Name of string variable to write | 
 **body** | [**StringValueObject**](StringValueObject.md)| String to write. If the value is longer than the string width, the string will be truncated to fit. | 

### Return type

[**ErrorResponse200OKish**](ErrorResponse200OKish.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

