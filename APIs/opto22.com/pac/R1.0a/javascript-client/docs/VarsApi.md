# PacControlRestApi.VarsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readDownTimerValue_0**](VarsApi.md#readDownTimerValue_0) | **GET** /device/strategy/vars/downTimers/{downTimerName}/value | 
[**readDownTimerVars_0**](VarsApi.md#readDownTimerVars_0) | **GET** /device/strategy/vars/downTimers | 
[**readFloatVar_0**](VarsApi.md#readFloatVar_0) | **GET** /device/strategy/vars/floats/{floatName} | 
[**readFloatVars_0**](VarsApi.md#readFloatVars_0) | **GET** /device/strategy/vars/floats | 
[**readInt32Var_0**](VarsApi.md#readInt32Var_0) | **GET** /device/strategy/vars/int32s/{int32Name} | 
[**readInt32Vars_0**](VarsApi.md#readInt32Vars_0) | **GET** /device/strategy/vars/int32s | 
[**readInt64VarAsString_0**](VarsApi.md#readInt64VarAsString_0) | **GET** /device/strategy/vars/int64s/{int64Name}/_string | 
[**readInt64Var_0**](VarsApi.md#readInt64Var_0) | **GET** /device/strategy/vars/int64s/{int64Name} | 
[**readInt64VarsAsStrings_0**](VarsApi.md#readInt64VarsAsStrings_0) | **GET** /device/strategy/vars/int64s/_string | 
[**readInt64Vars_0**](VarsApi.md#readInt64Vars_0) | **GET** /device/strategy/vars/int64s | 
[**readStringVar_0**](VarsApi.md#readStringVar_0) | **GET** /device/strategy/vars/strings/{stringName} | 
[**readStringVars_0**](VarsApi.md#readStringVars_0) | **GET** /device/strategy/vars/strings | 
[**readUpTimerValue_0**](VarsApi.md#readUpTimerValue_0) | **GET** /device/strategy/vars/upTimers/{upTimerName}/value | 
[**readUpTimerVars_0**](VarsApi.md#readUpTimerVars_0) | **GET** /device/strategy/vars/upTimers | 
[**writeFloatVar_0**](VarsApi.md#writeFloatVar_0) | **POST** /device/strategy/vars/floats/{floatName} | 
[**writeInt32Var_0**](VarsApi.md#writeInt32Var_0) | **POST** /device/strategy/vars/int32s/{int32Name} | 
[**writeInt64VarAsString_0**](VarsApi.md#writeInt64VarAsString_0) | **POST** /device/strategy/vars/int64s/{int64Name}/_string | 
[**writeInt64Var_0**](VarsApi.md#writeInt64Var_0) | **POST** /device/strategy/vars/int64s/{int64Name} | 
[**writeStringVar_0**](VarsApi.md#writeStringVar_0) | **POST** /device/strategy/vars/strings/{stringName} | 



## readDownTimerValue_0

> FloatValueObject readDownTimerValue_0(downTimerName)



Returns current value of the specified down timer

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let downTimerName = "downTimerName_example"; // String | Name of the down timer variable to read
apiInstance.readDownTimerValue_0(downTimerName, (error, data, response) => {
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


## readDownTimerVars_0

> [FloatVar] readDownTimerVars_0()



Returns the name and current value of all down timers in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readDownTimerVars_0((error, data, response) => {
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


## readFloatVar_0

> FloatValueObject readFloatVar_0(floatName)



Returns value of the specified float variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let floatName = "floatName_example"; // String | Name of float variable to read
apiInstance.readFloatVar_0(floatName, (error, data, response) => {
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


## readFloatVars_0

> [FloatVar] readFloatVars_0()



Returns the name and value of all (single-precision) float variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readFloatVars_0((error, data, response) => {
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


## readInt32Var_0

> Int32ValueObject readInt32Var_0(int32Name)



Returns value of the specified integer32 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let int32Name = "int32Name_example"; // String | Name of integer32 variable to read
apiInstance.readInt32Var_0(int32Name, (error, data, response) => {
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


## readInt32Vars_0

> [Int32Var] readInt32Vars_0()



Returns the name and value of all integer32 variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readInt32Vars_0((error, data, response) => {
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


## readInt64VarAsString_0

> Int64StringValueObject readInt64VarAsString_0(int64Name)



Returns value of the specified integer64 variable as a string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to read
apiInstance.readInt64VarAsString_0(int64Name, (error, data, response) => {
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


## readInt64Var_0

> Int64ValueObject readInt64Var_0(int64Name)



Returns value of the specified integer64 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to read
apiInstance.readInt64Var_0(int64Name, (error, data, response) => {
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


## readInt64VarsAsStrings_0

> [Int64VarAsString] readInt64VarsAsStrings_0()



Returns the name and value as a string of all integer64 variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readInt64VarsAsStrings_0((error, data, response) => {
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


## readInt64Vars_0

> [Int64Var] readInt64Vars_0()



Returns the name and value of all integer64 variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readInt64Vars_0((error, data, response) => {
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


## readStringVar_0

> StringValueObject readStringVar_0(stringName)



Returns value of the specified string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let stringName = "stringName_example"; // String | Name of string variable to read
apiInstance.readStringVar_0(stringName, (error, data, response) => {
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


## readStringVars_0

> [StringVar] readStringVars_0()



Returns the name and value of all string variables in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readStringVars_0((error, data, response) => {
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


## readUpTimerValue_0

> FloatValueObject readUpTimerValue_0(upTimerName)



Returns current value of the specified up timer

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let upTimerName = "upTimerName_example"; // String | Name of the up timer variable to read
apiInstance.readUpTimerValue_0(upTimerName, (error, data, response) => {
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


## readUpTimerVars_0

> [FloatVar] readUpTimerVars_0()



Returns the name and current value of all up timers in the strategy

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
apiInstance.readUpTimerVars_0((error, data, response) => {
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


## writeFloatVar_0

> writeFloatVar_0(floatName, body)



Sets the value of a float variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let floatName = "floatName_example"; // String | Name of the float variable to write
let body = new PacControlRestApi.FloatValueObject(); // FloatValueObject | Value to write to the float variable
apiInstance.writeFloatVar_0(floatName, body, (error, data, response) => {
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


## writeInt32Var_0

> writeInt32Var_0(int32Name, body)



Sets the value of an integer32 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let int32Name = "int32Name_example"; // String | Name of integer32 variable to write
let body = new PacControlRestApi.Int32ValueObject(); // Int32ValueObject | Value to write to the integer32 variable
apiInstance.writeInt32Var_0(int32Name, body, (error, data, response) => {
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


## writeInt64VarAsString_0

> writeInt64VarAsString_0(int64Name, body)



Sets the value of an integer64 variable as a string

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to write
let body = new PacControlRestApi.Int64StringValueObject(); // Int64StringValueObject | Value to write to the integer64 variable
apiInstance.writeInt64VarAsString_0(int64Name, body, (error, data, response) => {
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


## writeInt64Var_0

> writeInt64Var_0(int64Name, body)



Sets the value of an integer64 variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let int64Name = "int64Name_example"; // String | Name of integer64 variable to write
let body = new PacControlRestApi.Int64ValueObject(); // Int64ValueObject | Value to write to the integer64 variable
apiInstance.writeInt64Var_0(int64Name, body, (error, data, response) => {
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


## writeStringVar_0

> ErrorResponse200OKish writeStringVar_0(stringName, body)



Sets the value of a string variable

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.VarsApi();
let stringName = "stringName_example"; // String | Name of string variable to write
let body = new PacControlRestApi.StringValueObject(); // StringValueObject | String to write. If the value is longer than the string width, the string will be truncated to fit.
apiInstance.writeStringVar_0(stringName, body, (error, data, response) => {
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

