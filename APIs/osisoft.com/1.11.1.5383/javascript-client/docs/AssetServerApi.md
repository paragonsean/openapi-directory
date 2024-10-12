# PiWebApi2018Sp1SwaggerSpec.AssetServerApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assetServerCreateAssetDatabase**](AssetServerApi.md#assetServerCreateAssetDatabase) | **POST** /assetservers/{webId}/assetdatabases | Create an asset database.
[**assetServerCreateNotificationContactTemplate**](AssetServerApi.md#assetServerCreateNotificationContactTemplate) | **POST** /assetservers/{webId}/notificationcontacttemplates | Create a notification contact template.
[**assetServerCreateSecurityEntry**](AssetServerApi.md#assetServerCreateSecurityEntry) | **POST** /assetservers/{webId}/securityentries | Create a security entry owned by the asset server.
[**assetServerCreateSecurityIdentity**](AssetServerApi.md#assetServerCreateSecurityIdentity) | **POST** /assetservers/{webId}/securityidentities | Create a security identity.
[**assetServerCreateSecurityMapping**](AssetServerApi.md#assetServerCreateSecurityMapping) | **POST** /assetservers/{webId}/securitymappings | Create a security mapping.
[**assetServerCreateUnitClass**](AssetServerApi.md#assetServerCreateUnitClass) | **POST** /assetservers/{webId}/unitclasses | Create a unit class in the specified Asset Server.
[**assetServerDeleteSecurityEntry**](AssetServerApi.md#assetServerDeleteSecurityEntry) | **DELETE** /assetservers/{webId}/securityentries/{name} | Delete a security entry owned by the asset server.
[**assetServerGet**](AssetServerApi.md#assetServerGet) | **GET** /assetservers/{webId} | Retrieve an Asset Server.
[**assetServerGetAnalysisRulePlugIns**](AssetServerApi.md#assetServerGetAnalysisRulePlugIns) | **GET** /assetservers/{webId}/analysisruleplugins | Retrieve a list of all Analysis Rule Plug-in&#39;s.
[**assetServerGetByName**](AssetServerApi.md#assetServerGetByName) | **GET** /assetservers#name | Retrieve an Asset Server by name.
[**assetServerGetByPath**](AssetServerApi.md#assetServerGetByPath) | **GET** /assetservers#path | Retrieve an Asset Server by path.
[**assetServerGetDatabases**](AssetServerApi.md#assetServerGetDatabases) | **GET** /assetservers/{webId}/assetdatabases | Retrieve a list of all Asset Databases on the specified Asset Server.
[**assetServerGetNotificationContactTemplates**](AssetServerApi.md#assetServerGetNotificationContactTemplates) | **GET** /assetservers/{webId}/notificationcontacttemplates | Retrieve a list of all notification contact templates on the specified Asset Server.
[**assetServerGetNotificationPlugIns**](AssetServerApi.md#assetServerGetNotificationPlugIns) | **GET** /assetservers/{webId}/notificationplugins | Retrieve a list of all notification plugins on the specified Asset Server.
[**assetServerGetSecurity**](AssetServerApi.md#assetServerGetSecurity) | **GET** /assetservers/{webId}/security | Get the security information of the specified security item associated with the asset server for a specified user.
[**assetServerGetSecurityEntries**](AssetServerApi.md#assetServerGetSecurityEntries) | **GET** /assetservers/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.
[**assetServerGetSecurityEntryByName**](AssetServerApi.md#assetServerGetSecurityEntryByName) | **GET** /assetservers/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset server with the specified name.
[**assetServerGetSecurityIdentities**](AssetServerApi.md#assetServerGetSecurityIdentities) | **GET** /assetservers/{webId}/securityidentities | Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.
[**assetServerGetSecurityIdentitiesForUser**](AssetServerApi.md#assetServerGetSecurityIdentitiesForUser) | **GET** /assetservers/{webId}/securityidentities#userIdentity | Retrieve security identities for a specific user.
[**assetServerGetSecurityMappings**](AssetServerApi.md#assetServerGetSecurityMappings) | **GET** /assetservers/{webId}/securitymappings | Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.
[**assetServerGetTimeRulePlugIns**](AssetServerApi.md#assetServerGetTimeRulePlugIns) | **GET** /assetservers/{webId}/timeruleplugins | Retrieve a list of all Time Rule Plug-in&#39;s.
[**assetServerGetUnitClasses**](AssetServerApi.md#assetServerGetUnitClasses) | **GET** /assetservers/{webId}/unitclasses | Retrieve a list of all unit classes on the specified Asset Server.
[**assetServerList**](AssetServerApi.md#assetServerList) | **GET** /assetservers | Retrieve a list of all Asset Servers known to this service.
[**assetServerUpdateSecurityEntry**](AssetServerApi.md#assetServerUpdateSecurityEntry) | **PUT** /assetservers/{webId}/securityentries/{name} | Update a security entry owned by the asset server.



## assetServerCreateAssetDatabase

> assetServerCreateAssetDatabase(webId, database, opts)

Create an asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server on which to create the database.
let database = new PiWebApi2018Sp1SwaggerSpec.AssetDatabase(); // AssetDatabase | The new database definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerCreateAssetDatabase(webId, database, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server on which to create the database. | 
 **database** | [**AssetDatabase**](AssetDatabase.md)| The new database definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetServerCreateNotificationContactTemplate

> assetServerCreateNotificationContactTemplate(webId, notificationContactTemplate, opts)

Create a notification contact template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server on which to create the notification contact template.
let notificationContactTemplate = new PiWebApi2018Sp1SwaggerSpec.NotificationContactTemplate(); // NotificationContactTemplate | The new notification contact template definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerCreateNotificationContactTemplate(webId, notificationContactTemplate, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server on which to create the notification contact template. | 
 **notificationContactTemplate** | [**NotificationContactTemplate**](NotificationContactTemplate.md)| The new notification contact template definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetServerCreateSecurityEntry

> assetServerCreateSecurityEntry(webId, securityEntry, opts)

Create a security entry owned by the asset server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server where the security entry will be created.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'securityItem': "securityItem_example", // String | The security item of the desired security entries to be created. If the parameter is not specified, security entries of the 'Default' security item will be created.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerCreateSecurityEntry(webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server where the security entry will be created. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **securityItem** | **String**| The security item of the desired security entries to be created. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be created. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetServerCreateSecurityIdentity

> assetServerCreateSecurityIdentity(webId, securityIdentity, opts)

Create a security identity.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server on which to create the security identity.
let securityIdentity = new PiWebApi2018Sp1SwaggerSpec.SecurityIdentity(); // SecurityIdentity | The new security identity definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerCreateSecurityIdentity(webId, securityIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server on which to create the security identity. | 
 **securityIdentity** | [**SecurityIdentity**](SecurityIdentity.md)| The new security identity definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetServerCreateSecurityMapping

> assetServerCreateSecurityMapping(webId, securityMapping, opts)

Create a security mapping.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server on which to create the security mapping.
let securityMapping = new PiWebApi2018Sp1SwaggerSpec.SecurityMapping(); // SecurityMapping | The new security mapping definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerCreateSecurityMapping(webId, securityMapping, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server on which to create the security mapping. | 
 **securityMapping** | [**SecurityMapping**](SecurityMapping.md)| The new security mapping definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetServerCreateUnitClass

> assetServerCreateUnitClass(webId, unitClass, opts)

Create a unit class in the specified Asset Server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let unitClass = new PiWebApi2018Sp1SwaggerSpec.UnitClass(); // UnitClass | The new unit class definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerCreateUnitClass(webId, unitClass, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **unitClass** | [**UnitClass**](UnitClass.md)| The new unit class definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetServerDeleteSecurityEntry

> assetServerDeleteSecurityEntry(name, webId, opts)

Delete a security entry owned by the asset server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the asset server where the security entry will be deleted.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'securityItem': "securityItem_example" // String | The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the 'Default' security item will be deleted.
};
apiInstance.assetServerDeleteSecurityEntry(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server where the security entry will be deleted. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **securityItem** | **String**| The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assetServerGet

> AssetServer assetServerGet(webId, opts)

Retrieve an Asset Server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AssetServer**](AssetServer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetAnalysisRulePlugIns

> ItemsAnalysisRulePlugIn assetServerGetAnalysisRulePlugIns(webId, opts)

Retrieve a list of all Analysis Rule Plug-in&#39;s.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server, where the Analysis Rule Plug-in's are installed.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetAnalysisRulePlugIns(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server, where the Analysis Rule Plug-in&#39;s are installed. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnalysisRulePlugIn**](ItemsAnalysisRulePlugIn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetByName

> AssetServer assetServerGetByName(name, opts)

Retrieve an Asset Server by name.

This method returns an asset server based on the name associated with it. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let name = "name_example"; // String | The name of the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetByName(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AssetServer**](AssetServer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetByPath

> AssetServer assetServerGetByPath(path, opts)

Retrieve an Asset Server by path.

This method returns an asset server based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let path = "path_example"; // String | The path to the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AssetServer**](AssetServer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetDatabases

> ItemsAssetDatabase assetServerGetDatabases(webId, opts)

Retrieve a list of all Asset Databases on the specified Asset Server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetDatabases(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAssetDatabase**](ItemsAssetDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetNotificationContactTemplates

> ItemsNotificationContactTemplate assetServerGetNotificationContactTemplates(webId, opts)

Retrieve a list of all notification contact templates on the specified Asset Server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetNotificationContactTemplates(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsNotificationContactTemplate**](ItemsNotificationContactTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetNotificationPlugIns

> ItemsNotificationPlugIn assetServerGetNotificationPlugIns(webId, opts)

Retrieve a list of all notification plugins on the specified Asset Server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetNotificationPlugIns(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsNotificationPlugIn**](ItemsNotificationPlugIn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetSecurity

> ItemsSecurityRights assetServerGetSecurity(webId, securityItem, userIdentity, opts)

Get the security information of the specified security item associated with the asset server for a specified user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server for the security to be checked.
let securityItem = ["null"]; // [String] | The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only 'Default' security item of the security information will be returned.
let userIdentity = ["null"]; // [String] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
let opts = {
  'forceRefresh': true, // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetSecurity(webId, securityItem, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server for the security to be checked. | 
 **securityItem** | [**[String]**](String.md)| The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only &#39;Default&#39; security item of the security information will be returned. | 
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


## assetServerGetSecurityEntries

> ItemsSecurityEntry assetServerGetSecurityEntries(webId, opts)

Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server.
let opts = {
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering security entries. The default is no filter.
  'securityItem': "securityItem_example", // String | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetSecurityEntries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server. | 
 **nameFilter** | **String**| The name query string used for filtering security entries. The default is no filter. | [optional] 
 **securityItem** | **String**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetSecurityEntryByName

> SecurityEntry assetServerGetSecurityEntryByName(name, webId, opts)

Retrieve the security entry of the specified security item associated with the asset server with the specified name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the asset server.
let opts = {
  'securityItem': "securityItem_example", // String | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetSecurityEntryByName(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server. | 
 **securityItem** | **String**| The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetSecurityIdentities

> ItemsSecurityIdentity assetServerGetSecurityIdentities(webId, opts)

Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server to search.
let opts = {
  'field': "field_example", // String | Specifies which of the object's properties are searched. The default is 'Name'.
  'maxCount': 56, // Number | The maximum number of objects to be returned. The default is 1000.
  'query': "query_example", // String | The query string used for finding objects. The default is no query string.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetSecurityIdentities(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server to search. | 
 **field** | **String**| Specifies which of the object&#39;s properties are searched. The default is &#39;Name&#39;. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **query** | **String**| The query string used for finding objects. The default is no query string. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityIdentity**](ItemsSecurityIdentity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetSecurityIdentitiesForUser

> ItemsSecurityIdentity assetServerGetSecurityIdentitiesForUser(webId, userIdentity, opts)

Retrieve security identities for a specific user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let userIdentity = "userIdentity_example"; // String | The user identity to search for.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetSecurityIdentitiesForUser(webId, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **userIdentity** | **String**| The user identity to search for. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityIdentity**](ItemsSecurityIdentity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetSecurityMappings

> ItemsSecurityMapping assetServerGetSecurityMappings(webId, opts)

Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server to search.
let opts = {
  'field': "field_example", // String | Specifies which of the object's properties are searched. The default is 'Name'.
  'maxCount': 56, // Number | The maximum number of objects to be returned. The default is 1000.
  'query': "query_example", // String | The query string used for finding objects. The default is no query string.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetSecurityMappings(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server to search. | 
 **field** | **String**| Specifies which of the object&#39;s properties are searched. The default is &#39;Name&#39;. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned. The default is 1000. | [optional] 
 **query** | **String**| The query string used for finding objects. The default is no query string. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityMapping**](ItemsSecurityMapping.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetTimeRulePlugIns

> ItemsTimeRulePlugIn assetServerGetTimeRulePlugIns(webId, opts)

Retrieve a list of all Time Rule Plug-in&#39;s.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the asset server, where the Time Rule Plug-in's are installed.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetTimeRulePlugIns(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server, where the Time Rule Plug-in&#39;s are installed. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsTimeRulePlugIn**](ItemsTimeRulePlugIn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerGetUnitClasses

> ItemsUnitClass assetServerGetUnitClasses(webId, opts)

Retrieve a list of all unit classes on the specified Asset Server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let webId = "webId_example"; // String | The ID of the server.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerGetUnitClasses(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the server. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsUnitClass**](ItemsUnitClass.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerList

> ItemsAssetServer assetServerList(opts)

Retrieve a list of all Asset Servers known to this service.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetServerList(opts, (error, data, response) => {
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
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAssetServer**](ItemsAssetServer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetServerUpdateSecurityEntry

> assetServerUpdateSecurityEntry(name, webId, securityEntry, opts)

Update a security entry owned by the asset server.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetServerApi();
let name = "name_example"; // String | The name of the security entry.
let webId = "webId_example"; // String | The ID of the asset server where the security entry will be updated.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'securityItem': "securityItem_example" // String | The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the 'Default' security item will be updated.
};
apiInstance.assetServerUpdateSecurityEntry(name, webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset server where the security entry will be updated. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **securityItem** | **String**| The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be updated. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

