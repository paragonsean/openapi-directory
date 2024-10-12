# PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elementTemplateCreateAttributeTemplate**](ElementTemplateApi.md#elementTemplateCreateAttributeTemplate) | **POST** /elementtemplates/{webId}/attributetemplates | Create an attribute template.
[**elementTemplateCreateNotificationRuleTemplate**](ElementTemplateApi.md#elementTemplateCreateNotificationRuleTemplate) | **POST** /elementtemplates/{webId}/notificationruletemplates | Create a notification rule template.
[**elementTemplateCreateSecurityEntry**](ElementTemplateApi.md#elementTemplateCreateSecurityEntry) | **POST** /elementtemplates/{webId}/securityentries | Create a security entry owned by the element template.
[**elementTemplateDelete**](ElementTemplateApi.md#elementTemplateDelete) | **DELETE** /elementtemplates/{webId} | Delete an element template.
[**elementTemplateDeleteSecurityEntry**](ElementTemplateApi.md#elementTemplateDeleteSecurityEntry) | **DELETE** /elementtemplates/{webId}/securityentries/{name} | Delete a security entry owned by the element template.
[**elementTemplateGet**](ElementTemplateApi.md#elementTemplateGet) | **GET** /elementtemplates/{webId} | Retrieve an element template.
[**elementTemplateGetAnalysisTemplates**](ElementTemplateApi.md#elementTemplateGetAnalysisTemplates) | **GET** /elementtemplates/{webId}/analysistemplates | Get analysis templates for an element template.
[**elementTemplateGetAttributeTemplates**](ElementTemplateApi.md#elementTemplateGetAttributeTemplates) | **GET** /elementtemplates/{webId}/attributetemplates | Get child attribute templates for an element template.
[**elementTemplateGetBaseElementTemplates**](ElementTemplateApi.md#elementTemplateGetBaseElementTemplates) | **GET** /elementtemplates/{webId}/baseelementtemplates | Get base element templates for an element template.
[**elementTemplateGetByPath**](ElementTemplateApi.md#elementTemplateGetByPath) | **GET** /elementtemplates | Retrieve an element template by path.
[**elementTemplateGetCategories**](ElementTemplateApi.md#elementTemplateGetCategories) | **GET** /elementtemplates/{webId}/categories | Get an element template&#39;s categories.
[**elementTemplateGetDerivedElementTemplates**](ElementTemplateApi.md#elementTemplateGetDerivedElementTemplates) | **GET** /elementtemplates/{webId}/derivedelementtemplates | Get derived element templates for an element template.
[**elementTemplateGetNotificationRuleTemplates**](ElementTemplateApi.md#elementTemplateGetNotificationRuleTemplates) | **GET** /elementtemplates/{webId}/notificationruletemplates | Get notification rule templates for an element template
[**elementTemplateGetSecurity**](ElementTemplateApi.md#elementTemplateGetSecurity) | **GET** /elementtemplates/{webId}/security | Get the security information of the specified security item associated with the element template for a specified user.
[**elementTemplateGetSecurityEntries**](ElementTemplateApi.md#elementTemplateGetSecurityEntries) | **GET** /elementtemplates/{webId}/securityentries | Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.
[**elementTemplateGetSecurityEntryByName**](ElementTemplateApi.md#elementTemplateGetSecurityEntryByName) | **GET** /elementtemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the element template with the specified name.
[**elementTemplateUpdate**](ElementTemplateApi.md#elementTemplateUpdate) | **PATCH** /elementtemplates/{webId} | Update an element template by replacing items in its definition.
[**elementTemplateUpdateSecurityEntry**](ElementTemplateApi.md#elementTemplateUpdateSecurityEntry) | **PUT** /elementtemplates/{webId}/securityentries/{name} | Update a security entry owned by the element template.



## elementTemplateCreateAttributeTemplate

> elementTemplateCreateAttributeTemplate(webId, template, opts)

Create an attribute template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template on which to create the attribute template.
let template = new PiWebApi2018Sp1SwaggerSpec.AttributeTemplate(); // AttributeTemplate | The attribute template definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateCreateAttributeTemplate(webId, template, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template on which to create the attribute template. | 
 **template** | [**AttributeTemplate**](AttributeTemplate.md)| The attribute template definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## elementTemplateCreateNotificationRuleTemplate

> elementTemplateCreateNotificationRuleTemplate(webId, notificationRuleTemplate, opts)

Create a notification rule template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element on which to create the notification rule template.
let notificationRuleTemplate = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplate(); // NotificationRuleTemplate | The new notification rule template.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateCreateNotificationRuleTemplate(webId, notificationRuleTemplate, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element on which to create the notification rule template. | 
 **notificationRuleTemplate** | [**NotificationRuleTemplate**](NotificationRuleTemplate.md)| The new notification rule template. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## elementTemplateCreateSecurityEntry

> elementTemplateCreateSecurityEntry(webId, securityEntry, opts)

Create a security entry owned by the element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template where the security entry will be created.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateCreateSecurityEntry(webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template where the security entry will be created. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## elementTemplateDelete

> elementTemplateDelete(webId)

Delete an element template.

Deleting an element template will delete all associated templated data from elements which were created from it.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template to update.
apiInstance.elementTemplateDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## elementTemplateDeleteSecurityEntry

> elementTemplateDeleteSecurityEntry(name, webId, opts)

Delete a security entry owned by the element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the element template where the security entry will be deleted.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.elementTemplateDeleteSecurityEntry(name, webId, opts, (error, data, response) => {
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
 **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **webId** | **String**| The ID of the element template where the security entry will be deleted. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## elementTemplateGet

> ElementTemplate elementTemplateGet(webId, opts)

Retrieve an element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ElementTemplate**](ElementTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetAnalysisTemplates

> ItemsAnalysisTemplate elementTemplateGetAnalysisTemplates(webId, opts)

Get analysis templates for an element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetAnalysisTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnalysisTemplate**](ItemsAnalysisTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetAttributeTemplates

> ItemsAttributeTemplate elementTemplateGetAttributeTemplates(webId, opts)

Get child attribute templates for an element template.

If &#39;showInherited&#39; and &#39;showDescendants&#39; are &#39;true&#39;, it returns all the attribute templates from current element template and the base template.  If &#39;showInherited&#39; is &#39;false&#39;, it returns all the attribute templates from the current element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'depthFirstTraverse': true, // Boolean | When 'true', a Depth First traversal will be performed; this starts at the root and explores as far as possible along each branch before backtracking. When 'false', a Breadth First traversal will be performed; this starts at the tree root and explores the neighbor nodes first, then moves onto the next level of neighbors. The default is 'false' (Breadth First).
  'maxCount': 56, // Number | The maximum number of objects to be returned. The default is 1000.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showDescendants': true, // Boolean | Specifies if the result should include all descendant attribute templates from the current element template, even indirect ones. The default is 'false'.
  'showInherited': true, // Boolean | Specifies if the result should include attribute templates inherited from base element templates. The default is 'false'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetAttributeTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **depthFirstTraverse** | **Boolean**| When &#39;true&#39;, a Depth First traversal will be performed; this starts at the root and explores as far as possible along each branch before backtracking. When &#39;false&#39;, a Breadth First traversal will be performed; this starts at the tree root and explores the neighbor nodes first, then moves onto the next level of neighbors. The default is &#39;false&#39; (Breadth First). | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showDescendants** | **Boolean**| Specifies if the result should include all descendant attribute templates from the current element template, even indirect ones. The default is &#39;false&#39;. | [optional] 
 **showInherited** | **Boolean**| Specifies if the result should include attribute templates inherited from base element templates. The default is &#39;false&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttributeTemplate**](ItemsAttributeTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetBaseElementTemplates

> ItemsElementTemplate elementTemplateGetBaseElementTemplates(webId, opts)

Get base element templates for an element template.

The root template will be returned first, followed by successive templates in the inheritance chain.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'maxCount': 56, // Number | The maximum number of objects to be returned. The default is 1000.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetBaseElementTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **maxCount** | **Number**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElementTemplate**](ItemsElementTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetByPath

> ElementTemplate elementTemplateGetByPath(path, opts)

Retrieve an element template by path.

This method returns an element template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let path = "path_example"; // String | The path to the element template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the element template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ElementTemplate**](ElementTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetCategories

> ItemsElementCategory elementTemplateGetCategories(webId, opts)

Get an element template&#39;s categories.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showInherited': true, // Boolean | Specifies if the result should include categories inherited from base element templates. The default is 'false'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showInherited** | **Boolean**| Specifies if the result should include categories inherited from base element templates. The default is &#39;false&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElementCategory**](ItemsElementCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetDerivedElementTemplates

> ItemsElementTemplate elementTemplateGetDerivedElementTemplates(webId, opts)

Get derived element templates for an element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'maxCount': 56, // Number | The maximum number of objects to be returned. The default is 1000.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showDescendants': true, // Boolean | Specifies if the result should include all descendant element templates from the current element template, even indirect ones. The default is 'false'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetDerivedElementTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **maxCount** | **Number**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showDescendants** | **Boolean**| Specifies if the result should include all descendant element templates from the current element template, even indirect ones. The default is &#39;false&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElementTemplate**](ItemsElementTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetNotificationRuleTemplates

> ItemsNotificationRuleTemplate elementTemplateGetNotificationRuleTemplates(webId, opts)

Get notification rule templates for an element template

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetNotificationRuleTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsNotificationRuleTemplate**](ItemsNotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetSecurity

> ItemsSecurityRights elementTemplateGetSecurity(webId, userIdentity, opts)

Get the security information of the specified security item associated with the element template for a specified user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template for the security to be checked.
let userIdentity = ["null"]; // [String] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
let opts = {
  'forceRefresh': true, // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetSecurity(webId, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template for the security to be checked. | 
 **userIdentity** | [**[String]**](String.md)| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned. | 
 **forceRefresh** | **Boolean**| Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityRights**](ItemsSecurityRights.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetSecurityEntries

> ItemsSecurityEntry elementTemplateGetSecurityEntries(webId, opts)

Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering security entries. The default is no filter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetSecurityEntries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template. | 
 **nameFilter** | **String**| The name query string used for filtering security entries. The default is no filter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateGetSecurityEntryByName

> ItemsSecurityEntry elementTemplateGetSecurityEntryByName(name, webId, opts)

Retrieve the security entry associated with the element template with the specified name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the element template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.elementTemplateGetSecurityEntryByName(name, webId, opts, (error, data, response) => {
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
 **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **webId** | **String**| The ID of the element template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## elementTemplateUpdate

> elementTemplateUpdate(webId, template)

Update an element template by replacing items in its definition.

Updating the InstanceType property of an element template will not affect any elements that have already been created from this template; it will only affect any future elements created from this template. All other changes will be propagated to elements based on this template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let webId = "webId_example"; // String | The ID of the element template to update.
let template = new PiWebApi2018Sp1SwaggerSpec.ElementTemplate(); // ElementTemplate | A partial element template containing the desired changes.
apiInstance.elementTemplateUpdate(webId, template, (error, data, response) => {
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
 **webId** | **String**| The ID of the element template to update. | 
 **template** | [**ElementTemplate**](ElementTemplate.md)| A partial element template containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## elementTemplateUpdateSecurityEntry

> elementTemplateUpdateSecurityEntry(name, webId, securityEntry, opts)

Update a security entry owned by the element template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.ElementTemplateApi();
let name = "name_example"; // String | The name of the security entry.
let webId = "webId_example"; // String | The ID of the element template where the security entry will be updated.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.elementTemplateUpdateSecurityEntry(name, webId, securityEntry, opts, (error, data, response) => {
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
 **name** | **String**| The name of the security entry. | 
 **webId** | **String**| The ID of the element template where the security entry will be updated. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

