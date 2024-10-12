# PiWebApi2018Sp1SwaggerSpec.PointApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pointDelete**](PointApi.md#pointDelete) | **DELETE** /points/{webId} | Delete a point.
[**pointGet**](PointApi.md#pointGet) | **GET** /points/{webId} | Get a point.
[**pointGetAttributeByName**](PointApi.md#pointGetAttributeByName) | **GET** /points/{webId}/attributes/{name} | Get a point attribute by name.
[**pointGetAttributes**](PointApi.md#pointGetAttributes) | **GET** /points/{webId}/attributes | Get point attributes.
[**pointGetByPath**](PointApi.md#pointGetByPath) | **GET** /points | Get a point by path.
[**pointGetMultiple**](PointApi.md#pointGetMultiple) | **GET** /points/multiple | Retrieve multiple points by web id or path.
[**pointUpdate**](PointApi.md#pointUpdate) | **PATCH** /points/{webId} | Update a point. The only PI Point attributes that can be updated include: Name, Descriptor, EngineeringUnits, Step, and DisplayDigits. Other PI Point attributes cannot be updated through PI Web API.



## pointDelete

> pointDelete(webId)

Delete a point.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let webId = "webId_example"; // String | The ID of the point.
apiInstance.pointDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the point. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pointGet

> Point pointGet(webId, opts)

Get a point.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let webId = "webId_example"; // String | The ID of the point.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.pointGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the point. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**Point**](Point.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## pointGetAttributeByName

> PointAttribute pointGetAttributeByName(name, webId, opts)

Get a point attribute by name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let name = "name_example"; // String | The name of the attribute.
let webId = "webId_example"; // String | The ID of the point.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.pointGetAttributeByName(name, webId, opts, (error, data, response) => {
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
 **name** | **String**| The name of the attribute. | 
 **webId** | **String**| The ID of the point. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**PointAttribute**](PointAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## pointGetAttributes

> ItemsPointAttribute pointGetAttributes(webId, opts)

Get point attributes.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let webId = "webId_example"; // String | The ID of the point.
let opts = {
  'name': ["null"], // [String] | The name of a point attribute to be returned. Multiple attributes may be specified with multiple instances of the parameter.
  'nameFilter': "nameFilter_example", // String | The filter to the names of the list of point attributes to be returned. The default is no filter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.pointGetAttributes(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the point. | 
 **name** | [**[String]**](String.md)| The name of a point attribute to be returned. Multiple attributes may be specified with multiple instances of the parameter. | [optional] 
 **nameFilter** | **String**| The filter to the names of the list of point attributes to be returned. The default is no filter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsPointAttribute**](ItemsPointAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## pointGetByPath

> Point pointGetByPath(path, opts)

Get a point by path.

This method returns a PI Point based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let path = "path_example"; // String | The path to the point.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.pointGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the point. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**Point**](Point.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## pointGetMultiple

> ItemsItemPoint pointGetMultiple(opts)

Retrieve multiple points by web id or path.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let opts = {
  'asParallel': true, // Boolean | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested points. The default is 'false'.
  'includeMode': "includeMode_example", // String | The include mode for the return list. The default is 'All'.
  'path': ["null"], // [String] | The path of a point. Multiple points may be specified with multiple instances of the parameter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webId': ["null"], // [String] | The ID of a point. Multiple points may be specified with multiple instances of the parameter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.pointGetMultiple(opts, (error, data, response) => {
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
 **asParallel** | **Boolean**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested points. The default is &#39;false&#39;. | [optional] 
 **includeMode** | **String**| The include mode for the return list. The default is &#39;All&#39;. | [optional] 
 **path** | [**[String]**](String.md)| The path of a point. Multiple points may be specified with multiple instances of the parameter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webId** | [**[String]**](String.md)| The ID of a point. Multiple points may be specified with multiple instances of the parameter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsItemPoint**](ItemsItemPoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## pointUpdate

> pointUpdate(webId, pointDTO)

Update a point. The only PI Point attributes that can be updated include: Name, Descriptor, EngineeringUnits, Step, and DisplayDigits. Other PI Point attributes cannot be updated through PI Web API.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.PointApi();
let webId = "webId_example"; // String | The ID of the point.
let pointDTO = new PiWebApi2018Sp1SwaggerSpec.Point(); // Point | A partial point containing the desired changes.
apiInstance.pointUpdate(webId, pointDTO, (error, data, response) => {
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
 **webId** | **String**| The ID of the point. | 
 **pointDTO** | [**Point**](Point.md)| A partial point containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

