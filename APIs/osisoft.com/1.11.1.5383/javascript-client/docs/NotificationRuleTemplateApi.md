# PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notificationRuleTemplateCreateNotificationRuleTemplateSubscriber**](NotificationRuleTemplateApi.md#notificationRuleTemplateCreateNotificationRuleTemplateSubscriber) | **POST** /notificationruletemplates/{webId}/notificationrulesubscribers | Create a notification rule subscriber.
[**notificationRuleTemplateCreateSecurityEntry**](NotificationRuleTemplateApi.md#notificationRuleTemplateCreateSecurityEntry) | **POST** /notificationruletemplates/{webId}/securityentries | Create a security entry owned by the notification rule template.
[**notificationRuleTemplateDelete**](NotificationRuleTemplateApi.md#notificationRuleTemplateDelete) | **DELETE** /notificationruletemplates/{webId} | Delete a notification rule template.
[**notificationRuleTemplateDeleteSecurityEntry**](NotificationRuleTemplateApi.md#notificationRuleTemplateDeleteSecurityEntry) | **DELETE** /notificationruletemplates/{webId}/securityentries/{name} | Delete a security entry owned by the notification rule template.
[**notificationRuleTemplateGet**](NotificationRuleTemplateApi.md#notificationRuleTemplateGet) | **GET** /notificationruletemplates/{webId} | Get the specified notification rule template.
[**notificationRuleTemplateGetByPath**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetByPath) | **GET** /notificationruletemplates | Retrieve a notification rule template by path.
[**notificationRuleTemplateGetNotificationRuleTemplateSubscribers**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetNotificationRuleTemplateSubscribers) | **GET** /notificationruletemplates/{webId}/notificationrulesubscribers | Retrieve notification rule template subscribers.
[**notificationRuleTemplateGetNotificationRuleTemplatesQuery**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetNotificationRuleTemplatesQuery) | **GET** /notificationruletemplates/search | Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string.
[**notificationRuleTemplateGetSecurity**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetSecurity) | **GET** /notificationruletemplates/{webId}/security | Get the security information of the specified security item associated with the notification rule template for a specified user.
[**notificationRuleTemplateGetSecurityEntries**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetSecurityEntries) | **GET** /notificationruletemplates/{webId}/securityentries | Retrieve the security entries associated with the notification rule template based on the specified criteria. By default, all security entries for this notification rule template are returned.
[**notificationRuleTemplateGetSecurityEntryByName**](NotificationRuleTemplateApi.md#notificationRuleTemplateGetSecurityEntryByName) | **GET** /notificationruletemplates/{webId}/securityentries/{name} | Retrieve the security entry associated with the notification rule template with the specified name.
[**notificationRuleTemplateUpdate**](NotificationRuleTemplateApi.md#notificationRuleTemplateUpdate) | **PATCH** /notificationruletemplates/{webId} | Update a notification rule template by replacing items in its definition.
[**notificationRuleTemplateUpdateSecurityEntry**](NotificationRuleTemplateApi.md#notificationRuleTemplateUpdateSecurityEntry) | **PUT** /notificationruletemplates/{webId}/securityentries/{name} | Update a security entry owned by the notification rule template.



## notificationRuleTemplateCreateNotificationRuleTemplateSubscriber

> notificationRuleTemplateCreateNotificationRuleTemplateSubscriber(webId, notificationRuleSubscriber, opts)

Create a notification rule subscriber.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template on which to create the notification rule subscriber.
let notificationRuleSubscriber = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleSubscriber(); // NotificationRuleSubscriber | The new notification rule subscriber definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateCreateNotificationRuleTemplateSubscriber(webId, notificationRuleSubscriber, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template on which to create the notification rule subscriber. | 
 **notificationRuleSubscriber** | [**NotificationRuleSubscriber**](NotificationRuleSubscriber.md)| The new notification rule subscriber definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## notificationRuleTemplateCreateSecurityEntry

> notificationRuleTemplateCreateSecurityEntry(webId, securityEntry, opts)

Create a security entry owned by the notification rule template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template, where the security entry will be created.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateCreateSecurityEntry(webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template, where the security entry will be created. | 
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


## notificationRuleTemplateDelete

> notificationRuleTemplateDelete(webId)

Delete a notification rule template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template.
apiInstance.notificationRuleTemplateDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationRuleTemplateDeleteSecurityEntry

> notificationRuleTemplateDeleteSecurityEntry(name, webId, opts)

Delete a security entry owned by the notification rule template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the notification rule template, where the security entry will be deleted.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.notificationRuleTemplateDeleteSecurityEntry(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template, where the security entry will be deleted. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## notificationRuleTemplateGet

> NotificationRuleTemplate notificationRuleTemplateGet(webId, opts)

Get the specified notification rule template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**NotificationRuleTemplate**](NotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleTemplateGetByPath

> NotificationRuleTemplate notificationRuleTemplateGetByPath(path, opts)

Retrieve a notification rule template by path.

This method returns a Notification Rule Template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let path = "path_example"; // String | The path to the notification rule template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the notification rule template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**NotificationRuleTemplate**](NotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleTemplateGetNotificationRuleTemplateSubscribers

> ItemsNotificationRuleSubscriber notificationRuleTemplateGetNotificationRuleTemplateSubscribers(webId, opts)

Retrieve notification rule template subscribers.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGetNotificationRuleTemplateSubscribers(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the resource to use as the root of the search. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsNotificationRuleSubscriber**](ItemsNotificationRuleSubscriber.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleTemplateGetNotificationRuleTemplatesQuery

> ItemsNotificationRuleTemplate notificationRuleTemplateGetNotificationRuleTemplatesQuery(opts)

Retrieve Notification rule templates based on the specified conditions. Returns Notification rule templates using the specified search query string.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let opts = {
  'databaseWebId': "databaseWebId_example", // String | The ID of the asset database to use as the root of the query.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'query': "query_example", // String | The query string is a list of filters used to perform an AFSearch for the Notification rule templates in the asset database. An example would be: \"query=NotificationRuleTemplate:{ Name:='MyNotificationRuleTemplate' } Type:=Int32\".
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGetNotificationRuleTemplatesQuery(opts, (error, data, response) => {
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
 **databaseWebId** | **String**| The ID of the asset database to use as the root of the query. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **String**| The query string is a list of filters used to perform an AFSearch for the Notification rule templates in the asset database. An example would be: \&quot;query&#x3D;NotificationRuleTemplate:{ Name:&#x3D;&#39;MyNotificationRuleTemplate&#39; } Type:&#x3D;Int32\&quot;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsNotificationRuleTemplate**](ItemsNotificationRuleTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleTemplateGetSecurity

> ItemsSecurityRights notificationRuleTemplateGetSecurity(webId, userIdentity, opts)

Get the security information of the specified security item associated with the notification rule template for a specified user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template for the security to be checked.
let userIdentity = ["null"]; // [String] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
let opts = {
  'forceRefresh': true, // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGetSecurity(webId, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template for the security to be checked. | 
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


## notificationRuleTemplateGetSecurityEntries

> ItemsSecurityEntry notificationRuleTemplateGetSecurityEntries(webId, opts)

Retrieve the security entries associated with the notification rule template based on the specified criteria. By default, all security entries for this notification rule template are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template.
let opts = {
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering security entries. The default is no filter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGetSecurityEntries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template. | 
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


## notificationRuleTemplateGetSecurityEntryByName

> SecurityEntry notificationRuleTemplateGetSecurityEntryByName(name, webId, opts)

Retrieve the security entry associated with the notification rule template with the specified name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the notification rule template.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.notificationRuleTemplateGetSecurityEntryByName(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## notificationRuleTemplateUpdate

> notificationRuleTemplateUpdate(webId, notificationRuleTemplate)

Update a notification rule template by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let webId = "webId_example"; // String | The ID of the notification rule template to update.
let notificationRuleTemplate = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplate(); // NotificationRuleTemplate | A partial notification rule template containing the desired changes.
apiInstance.notificationRuleTemplateUpdate(webId, notificationRuleTemplate, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template to update. | 
 **notificationRuleTemplate** | [**NotificationRuleTemplate**](NotificationRuleTemplate.md)| A partial notification rule template containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## notificationRuleTemplateUpdateSecurityEntry

> notificationRuleTemplateUpdateSecurityEntry(name, webId, securityEntry, opts)

Update a security entry owned by the notification rule template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.NotificationRuleTemplateApi();
let name = "name_example"; // String | The name of the security entry.
let webId = "webId_example"; // String | The ID of the notification rule template, where the security entry will be updated.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.notificationRuleTemplateUpdateSecurityEntry(name, webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the notification rule template, where the security entry will be updated. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

