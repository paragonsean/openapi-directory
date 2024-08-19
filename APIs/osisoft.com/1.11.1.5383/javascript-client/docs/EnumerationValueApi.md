# PiWebApi2018Sp1SwaggerSpec.EnumerationValueApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enumerationValueDeleteEnumerationValue**](EnumerationValueApi.md#enumerationValueDeleteEnumerationValue) | **DELETE** /enumerationvalues/{webId} | Delete an enumeration value from an enumeration set.
[**enumerationValueGet**](EnumerationValueApi.md#enumerationValueGet) | **GET** /enumerationvalues/{webId} | Retrieve an enumeration value mapping
[**enumerationValueGetByPath**](EnumerationValueApi.md#enumerationValueGetByPath) | **GET** /enumerationvalues | Retrieve an enumeration value by path.
[**enumerationValueUpdateEnumerationValue**](EnumerationValueApi.md#enumerationValueUpdateEnumerationValue) | **PATCH** /enumerationvalues/{webId} | Update an enumeration value by replacing items in its definition.



## enumerationValueDeleteEnumerationValue

> enumerationValueDeleteEnumerationValue(webId)

Delete an enumeration value from an enumeration set.

Deleting a value will remove it from the enumeration set along with any value references within the PI Web API system.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EnumerationValueApi();
let webId = "webId_example"; // String | The ID of the enumeration value.
apiInstance.enumerationValueDeleteEnumerationValue(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the enumeration value. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enumerationValueGet

> EnumerationValue enumerationValueGet(webId, opts)

Retrieve an enumeration value mapping

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EnumerationValueApi();
let webId = "webId_example"; // String | The ID of the enumeration value.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.enumerationValueGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the enumeration value. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**EnumerationValue**](EnumerationValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## enumerationValueGetByPath

> EnumerationValue enumerationValueGetByPath(path, opts)

Retrieve an enumeration value by path.

This method returns a enumeration value based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EnumerationValueApi();
let path = "path_example"; // String | The path to the target enumeration value.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.enumerationValueGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the target enumeration value. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**EnumerationValue**](EnumerationValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## enumerationValueUpdateEnumerationValue

> enumerationValueUpdateEnumerationValue(webId, enumerationValue)

Update an enumeration value by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EnumerationValueApi();
let webId = "webId_example"; // String | The ID of the enumeration value to update.
let enumerationValue = new PiWebApi2018Sp1SwaggerSpec.EnumerationValue(); // EnumerationValue | A partial enumeration value containing the desired changes.
apiInstance.enumerationValueUpdateEnumerationValue(webId, enumerationValue, (error, data, response) => {
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
 **webId** | **String**| The ID of the enumeration value to update. | 
 **enumerationValue** | [**EnumerationValue**](EnumerationValue.md)| A partial enumeration value containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

