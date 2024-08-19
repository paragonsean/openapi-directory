# PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributeTemplateCreateAttributeTemplate**](AttributeTemplateApi.md#attributeTemplateCreateAttributeTemplate) | **POST** /attributetemplates/{webId}/attributetemplates | Create an attribute template as a child of another attribute template.
[**attributeTemplateDelete**](AttributeTemplateApi.md#attributeTemplateDelete) | **DELETE** /attributetemplates/{webId} | Delete an attribute template.
[**attributeTemplateGet**](AttributeTemplateApi.md#attributeTemplateGet) | **GET** /attributetemplates/{webId} | Retrieve an attribute template.
[**attributeTemplateGetAttributeTemplates**](AttributeTemplateApi.md#attributeTemplateGetAttributeTemplates) | **GET** /attributetemplates/{webId}/attributetemplates | Retrieve an attribute template&#39;s child attribute templates.
[**attributeTemplateGetByPath**](AttributeTemplateApi.md#attributeTemplateGetByPath) | **GET** /attributetemplates | Retrieve an attribute template by path.
[**attributeTemplateGetCategories**](AttributeTemplateApi.md#attributeTemplateGetCategories) | **GET** /attributetemplates/{webId}/categories | Get an attribute template&#39;s categories.
[**attributeTemplateUpdate**](AttributeTemplateApi.md#attributeTemplateUpdate) | **PATCH** /attributetemplates/{webId} | Update an existing attribute template by replacing items in its definition.



## attributeTemplateCreateAttributeTemplate

> attributeTemplateCreateAttributeTemplate(webId, template, opts)

Create an attribute template as a child of another attribute template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let webId = "webId_example"; // String | The ID of the parent attribute template on which to create the attribute template.
let template = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplate(); // AttributeTemplate | The attribute template definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeTemplateCreateAttributeTemplate(webId, template, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent attribute template on which to create the attribute template. | 
 **template** | [**AttributeTemplate**](AttributeTemplate.md)| The attribute template definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## attributeTemplateDelete

> attributeTemplateDelete(webId)

Delete an attribute template.

Deleting an attribute template will delete the attributes that were created based on the template

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let webId = "webId_example"; // String | The ID of the attribute template.
apiInstance.attributeTemplateDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute template. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## attributeTemplateGet

> AttributeTemplate attributeTemplateGet(webId, opts)

Retrieve an attribute template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let webId = "webId_example"; // String | The ID of the attribute template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeTemplateGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AttributeTemplate**](AttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeTemplateGetAttributeTemplates

> ItemsAttributeTemplate attributeTemplateGetAttributeTemplates(webId, opts)

Retrieve an attribute template&#39;s child attribute templates.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let webId = "webId_example"; // String | The ID of the attribute template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeTemplateGetAttributeTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttributeTemplate**](ItemsAttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeTemplateGetByPath

> AttributeTemplate attributeTemplateGetByPath(path, opts)

Retrieve an attribute template by path.

This method returns an attribute template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let path = "path_example"; // String | The path to the attribute template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeTemplateGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the attribute template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AttributeTemplate**](AttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeTemplateGetCategories

> ItemsAttributeCategory attributeTemplateGetCategories(webId, opts)

Get an attribute template&#39;s categories.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let webId = "webId_example"; // String | The ID of the attribute template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeTemplateGetCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttributeCategory**](ItemsAttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeTemplateUpdate

> attributeTemplateUpdate(webId, template)

Update an existing attribute template by replacing items in its definition.

Updating an attribute template will propagate changes to the attributes that were created based on the template

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplateApi();
let webId = "webId_example"; // String | The ID of the attribute template.
let template = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplate(); // AttributeTemplate | A partial attribute template containing the desired changes.
apiInstance.attributeTemplateUpdate(webId, template, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute template. | 
 **template** | [**AttributeTemplate**](AttributeTemplate.md)| A partial attribute template containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

