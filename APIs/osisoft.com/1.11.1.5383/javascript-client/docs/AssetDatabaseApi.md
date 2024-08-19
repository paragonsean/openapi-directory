# PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assetDatabaseAddReferencedElement**](AssetDatabaseApi.md#assetDatabaseAddReferencedElement) | **POST** /assetdatabases/{webId}/referencedelements | Add a reference to an existing element to the specified database.
[**assetDatabaseCreateAnalysisCategory**](AssetDatabaseApi.md#assetDatabaseCreateAnalysisCategory) | **POST** /assetdatabases/{webId}/analysiscategories | Create an analysis category at the Asset Database root.
[**assetDatabaseCreateAnalysisTemplate**](AssetDatabaseApi.md#assetDatabaseCreateAnalysisTemplate) | **POST** /assetdatabases/{webId}/analysistemplates | Create an analysis template at the Asset Database root.
[**assetDatabaseCreateAttributeCategory**](AssetDatabaseApi.md#assetDatabaseCreateAttributeCategory) | **POST** /assetdatabases/{webId}/attributecategories | Create an attribute category at the Asset Database root.
[**assetDatabaseCreateElement**](AssetDatabaseApi.md#assetDatabaseCreateElement) | **POST** /assetdatabases/{webId}/elements | Create a child element.
[**assetDatabaseCreateElementCategory**](AssetDatabaseApi.md#assetDatabaseCreateElementCategory) | **POST** /assetdatabases/{webId}/elementcategories | Create an element category at the Asset Database root.
[**assetDatabaseCreateElementTemplate**](AssetDatabaseApi.md#assetDatabaseCreateElementTemplate) | **POST** /assetdatabases/{webId}/elementtemplates | Create a template at the Asset Database root. Specify InstanceType of \&quot;Element\&quot; or \&quot;EventFrame\&quot; to create element or event frame template respectively. Only these two types of templates can be created.
[**assetDatabaseCreateEnumerationSet**](AssetDatabaseApi.md#assetDatabaseCreateEnumerationSet) | **POST** /assetdatabases/{webId}/enumerationsets | Create an enumeration set at the Asset Database.
[**assetDatabaseCreateEventFrame**](AssetDatabaseApi.md#assetDatabaseCreateEventFrame) | **POST** /assetdatabases/{webId}/eventframes | Create an event frame.
[**assetDatabaseCreateSecurityEntry**](AssetDatabaseApi.md#assetDatabaseCreateSecurityEntry) | **POST** /assetdatabases/{webId}/securityentries | Create a security entry owned by the asset database.
[**assetDatabaseCreateTable**](AssetDatabaseApi.md#assetDatabaseCreateTable) | **POST** /assetdatabases/{webId}/tables | Create a table on the Asset Database.
[**assetDatabaseCreateTableCategory**](AssetDatabaseApi.md#assetDatabaseCreateTableCategory) | **POST** /assetdatabases/{webId}/tablecategories | Create a table category on the Asset Database.
[**assetDatabaseDelete**](AssetDatabaseApi.md#assetDatabaseDelete) | **DELETE** /assetdatabases/{webId} | Delete an asset database.
[**assetDatabaseDeleteSecurityEntry**](AssetDatabaseApi.md#assetDatabaseDeleteSecurityEntry) | **DELETE** /assetdatabases/{webId}/securityentries/{name} | Delete a security entry owned by the asset database.
[**assetDatabaseExport**](AssetDatabaseApi.md#assetDatabaseExport) | **GET** /assetdatabases/{webId}/export | Export the asset database.
[**assetDatabaseFindAnalyses**](AssetDatabaseApi.md#assetDatabaseFindAnalyses) | **GET** /assetdatabases/{webId}/analyses | Retrieve analyses based on the specified conditions.
[**assetDatabaseFindElementAttributes**](AssetDatabaseApi.md#assetDatabaseFindElementAttributes) | **GET** /assetdatabases/{webId}/elementattributes | Retrieves a list of element attributes matching the specified filters from the specified asset database.
[**assetDatabaseFindEventFrameAttributes**](AssetDatabaseApi.md#assetDatabaseFindEventFrameAttributes) | **GET** /assetdatabases/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified asset database.
[**assetDatabaseGet**](AssetDatabaseApi.md#assetDatabaseGet) | **GET** /assetdatabases/{webId} | Retrieve an Asset Database.
[**assetDatabaseGetAnalysisCategories**](AssetDatabaseApi.md#assetDatabaseGetAnalysisCategories) | **GET** /assetdatabases/{webId}/analysiscategories | Retrieve analysis categories for a given Asset Database.
[**assetDatabaseGetAnalysisTemplates**](AssetDatabaseApi.md#assetDatabaseGetAnalysisTemplates) | **GET** /assetdatabases/{webId}/analysistemplates | Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.
[**assetDatabaseGetAttributeCategories**](AssetDatabaseApi.md#assetDatabaseGetAttributeCategories) | **GET** /assetdatabases/{webId}/attributecategories | Retrieve attribute categories for a given Asset Database.
[**assetDatabaseGetByPath**](AssetDatabaseApi.md#assetDatabaseGetByPath) | **GET** /assetdatabases | Retrieve an Asset Database by path.
[**assetDatabaseGetElementCategories**](AssetDatabaseApi.md#assetDatabaseGetElementCategories) | **GET** /assetdatabases/{webId}/elementcategories | Retrieve element categories for a given Asset Database.
[**assetDatabaseGetElementTemplates**](AssetDatabaseApi.md#assetDatabaseGetElementTemplates) | **GET** /assetdatabases/{webId}/elementtemplates | Retrieve element templates based on the specified criteria. Only templates of instance type \&quot;Element\&quot; and \&quot;EventFrame\&quot; are returned. By default, all element and event frame templates in the specified Asset Database are returned.
[**assetDatabaseGetElements**](AssetDatabaseApi.md#assetDatabaseGetElements) | **GET** /assetdatabases/{webId}/elements | Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.
[**assetDatabaseGetEnumerationSets**](AssetDatabaseApi.md#assetDatabaseGetEnumerationSets) | **GET** /assetdatabases/{webId}/enumerationsets | Retrieve enumeration sets for given asset database.
[**assetDatabaseGetEventFrames**](AssetDatabaseApi.md#assetDatabaseGetEventFrames) | **GET** /assetdatabases/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours.
[**assetDatabaseGetReferencedElements**](AssetDatabaseApi.md#assetDatabaseGetReferencedElements) | **GET** /assetdatabases/{webId}/referencedelements | Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.
[**assetDatabaseGetSecurity**](AssetDatabaseApi.md#assetDatabaseGetSecurity) | **GET** /assetdatabases/{webId}/security | Get the security information of the specified security item associated with the asset database for a specified user.
[**assetDatabaseGetSecurityEntries**](AssetDatabaseApi.md#assetDatabaseGetSecurityEntries) | **GET** /assetdatabases/{webId}/securityentries | Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.
[**assetDatabaseGetSecurityEntryByName**](AssetDatabaseApi.md#assetDatabaseGetSecurityEntryByName) | **GET** /assetdatabases/{webId}/securityentries/{name} | Retrieve the security entry of the specified security item associated with the asset database with the specified name.
[**assetDatabaseGetTableCategories**](AssetDatabaseApi.md#assetDatabaseGetTableCategories) | **GET** /assetdatabases/{webId}/tablecategories | Retrieve table categories for a given Asset Database.
[**assetDatabaseGetTables**](AssetDatabaseApi.md#assetDatabaseGetTables) | **GET** /assetdatabases/{webId}/tables | Retrieve tables for given Asset Database.
[**assetDatabaseImport**](AssetDatabaseApi.md#assetDatabaseImport) | **POST** /assetdatabases/{webId}/import | Import an asset database.
[**assetDatabaseRemoveReferencedElement**](AssetDatabaseApi.md#assetDatabaseRemoveReferencedElement) | **DELETE** /assetdatabases/{webId}/referencedelements | Remove a reference to an existing element from the specified database.
[**assetDatabaseUpdate**](AssetDatabaseApi.md#assetDatabaseUpdate) | **PATCH** /assetdatabases/{webId} | Update an asset database by replacing items in its definition.
[**assetDatabaseUpdateSecurityEntry**](AssetDatabaseApi.md#assetDatabaseUpdateSecurityEntry) | **PUT** /assetdatabases/{webId}/securityentries/{name} | Update a security entry owned by the asset database.



## assetDatabaseAddReferencedElement

> assetDatabaseAddReferencedElement(webId, referencedElementWebId, opts)

Add a reference to an existing element to the specified database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database which the referenced element will be added to.
let referencedElementWebId = ["null"]; // [String] | The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
let opts = {
  'referenceType': "referenceType_example" // String | The name of the reference type between the parent and the referenced element. This must be a \"strong\" reference type. The default is \"parent-child\".
};
apiInstance.assetDatabaseAddReferencedElement(webId, referencedElementWebId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database which the referenced element will be added to. | 
 **referencedElementWebId** | [**[String]**](String.md)| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter. | 
 **referenceType** | **String**| The name of the reference type between the parent and the referenced element. This must be a \&quot;strong\&quot; reference type. The default is \&quot;parent-child\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseCreateAnalysisCategory

> assetDatabaseCreateAnalysisCategory(webId, analysisCategory, opts)

Create an analysis category at the Asset Database root.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the analysis category.
let analysisCategory = new PiWebApi2018Sp1SwaggerSpec.AnalysisCategory(); // AnalysisCategory | The new analysis category definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateAnalysisCategory(webId, analysisCategory, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the analysis category. | 
 **analysisCategory** | [**AnalysisCategory**](AnalysisCategory.md)| The new analysis category definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateAnalysisTemplate

> assetDatabaseCreateAnalysisTemplate(webId, template, opts)

Create an analysis template at the Asset Database root.

Analyses that are based on an analysis template will inherit characteristics defined in the template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the analysis template.
let template = new PiWebApi2018Sp1SwaggerSpec.AnalysisTemplate(); // AnalysisTemplate | The new analysis template definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateAnalysisTemplate(webId, template, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the analysis template. | 
 **template** | [**AnalysisTemplate**](AnalysisTemplate.md)| The new analysis template definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateAttributeCategory

> assetDatabaseCreateAttributeCategory(webId, attributeCategory, opts)

Create an attribute category at the Asset Database root.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the attribute category.
let attributeCategory = new PiWebApi2018Sp1SwaggerSpec.AttributeCategory(); // AttributeCategory | The new attribute category definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateAttributeCategory(webId, attributeCategory, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the attribute category. | 
 **attributeCategory** | [**AttributeCategory**](AttributeCategory.md)| The new attribute category definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateElement

> assetDatabaseCreateElement(webId, element, opts)

Create a child element.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database on which to create the element.
let element = new PiWebApi2018Sp1SwaggerSpec.Element(); // Element | The new element definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateElement(webId, element, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database on which to create the element. | 
 **element** | [**Element**](Element.md)| The new element definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateElementCategory

> assetDatabaseCreateElementCategory(webId, elementCategory, opts)

Create an element category at the Asset Database root.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the element category.
let elementCategory = new PiWebApi2018Sp1SwaggerSpec.ElementCategory(); // ElementCategory | The new element category definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateElementCategory(webId, elementCategory, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the element category. | 
 **elementCategory** | [**ElementCategory**](ElementCategory.md)| The new element category definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateElementTemplate

> assetDatabaseCreateElementTemplate(webId, template, opts)

Create a template at the Asset Database root. Specify InstanceType of \&quot;Element\&quot; or \&quot;EventFrame\&quot; to create element or event frame template respectively. Only these two types of templates can be created.

Elements and event frames that are based on an element template will inherit characteristics defined in the template.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the element template.
let template = new PiWebApi2018Sp1SwaggerSpec.ElementTemplate(); // ElementTemplate | The new element template definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateElementTemplate(webId, template, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the element template. | 
 **template** | [**ElementTemplate**](ElementTemplate.md)| The new element template definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateEnumerationSet

> assetDatabaseCreateEnumerationSet(webId, enumerationSet, opts)

Create an enumeration set at the Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the enumeration set.
let enumerationSet = new PiWebApi2018Sp1SwaggerSpec.EnumerationSet(); // EnumerationSet | The new enumeration set definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateEnumerationSet(webId, enumerationSet, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the enumeration set. | 
 **enumerationSet** | [**EnumerationSet**](EnumerationSet.md)| The new enumeration set definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateEventFrame

> assetDatabaseCreateEventFrame(webId, eventFrame, opts)

Create an event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database on which to create the event frame.
let eventFrame = new PiWebApi2018Sp1SwaggerSpec.EventFrame(); // EventFrame | The new event frame definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateEventFrame(webId, eventFrame, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database on which to create the event frame. | 
 **eventFrame** | [**EventFrame**](EventFrame.md)| The new event frame definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateSecurityEntry

> assetDatabaseCreateSecurityEntry(webId, securityEntry, opts)

Create a security entry owned by the asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database where the security entry will be created.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'securityItem': "securityItem_example", // String | The security item of the desired security entries to be created. If the parameter is not specified, security entries of the 'Default' security item will be created.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateSecurityEntry(webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database where the security entry will be created. | 
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


## assetDatabaseCreateTable

> assetDatabaseCreateTable(webId, table, opts)

Create a table on the Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the table.
let table = new PiWebApi2018Sp1SwaggerSpec.Table(); // Table | The new table definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateTable(webId, table, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the table. | 
 **table** | [**Table**](Table.md)| The new table definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseCreateTableCategory

> assetDatabaseCreateTableCategory(webId, tableCategory, opts)

Create a table category on the Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database in which to create the table category.
let tableCategory = new PiWebApi2018Sp1SwaggerSpec.TableCategory(); // TableCategory | The new table category definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseCreateTableCategory(webId, tableCategory, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database in which to create the table category. | 
 **tableCategory** | [**TableCategory**](TableCategory.md)| The new table category definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseDelete

> assetDatabaseDelete(webId)

Delete an asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
apiInstance.assetDatabaseDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assetDatabaseDeleteSecurityEntry

> assetDatabaseDeleteSecurityEntry(name, webId, opts)

Delete a security entry owned by the asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the asset database where the security entry will be deleted.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'securityItem': "securityItem_example" // String | The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the 'Default' security item will be deleted.
};
apiInstance.assetDatabaseDeleteSecurityEntry(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database where the security entry will be deleted. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **securityItem** | **String**| The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assetDatabaseExport

> assetDatabaseExport(webId, opts)

Export the asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'endTime': "endTime_example", // String | The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*'.
  'exportMode': ["null"], // [String] | Indicates the type of export to perform. The default is 'StrongReferences'. Multiple export modes may be specified by using multiple instances of exportMode.
  'startTime': "startTime_example" // String | The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is '*-30d'.
};
apiInstance.assetDatabaseExport(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **endTime** | **String**| The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*&#39;. | [optional] 
 **exportMode** | [**[String]**](String.md)| Indicates the type of export to perform. The default is &#39;StrongReferences&#39;. Multiple export modes may be specified by using multiple instances of exportMode. | [optional] 
 **startTime** | **String**| The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*-30d&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assetDatabaseFindAnalyses

> ItemsAnalysis assetDatabaseFindAnalyses(webId, field, opts)

Retrieve analyses based on the specified conditions.

Users can search for the analyses based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the analyses that match the default search.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database to search for the analyses.
let field = ["null"]; // [String] | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
let opts = {
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'query': "query_example", // String | The query string used for finding analyses. The default is null.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseFindAnalyses(webId, field, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database to search for the analyses. | 
 **field** | [**[String]**](String.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **String**| The query string used for finding analyses. The default is null. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnalysis**](ItemsAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseFindElementAttributes

> ItemsAttribute assetDatabaseFindElementAttributes(webId, opts)

Retrieves a list of element attributes matching the specified filters from the specified asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database to use as the root of the search.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'attributeCategory': "attributeCategory_example", // String | Specify that returned attributes must have this category. The default is no filter.
  'attributeDescriptionFilter': "attributeDescriptionFilter_example", // String | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
  'attributeNameFilter': "attributeNameFilter_example", // String | The attribute name filter string used for finding objects. The default is no filter.
  'attributeType': "attributeType_example", // String | Specify that returned attributes' value type must be this value type. The default is no filter.
  'elementCategory': "elementCategory_example", // String | Specify that the owner of the returned attributes must have this category. The default is no filter.
  'elementDescriptionFilter': "elementDescriptionFilter_example", // String | The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
  'elementNameFilter': "elementNameFilter_example", // String | The element name filter string used for finding objects. The default is no filter.
  'elementTemplate': "elementTemplate_example", // String | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
  'elementType': "elementType_example", // String | Specify that the element of the returned attributes must have this AFElementType. The default is no filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned (the page size). The default is 1000.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseFindElementAttributes(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database to use as the root of the search. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **attributeCategory** | **String**| Specify that returned attributes must have this category. The default is no filter. | [optional] 
 **attributeDescriptionFilter** | **String**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **attributeNameFilter** | **String**| The attribute name filter string used for finding objects. The default is no filter. | [optional] 
 **attributeType** | **String**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] 
 **elementCategory** | **String**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] 
 **elementDescriptionFilter** | **String**| The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **elementNameFilter** | **String**| The element name filter string used for finding objects. The default is no filter. | [optional] 
 **elementTemplate** | **String**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] 
 **elementType** | **String**| Specify that the element of the returned attributes must have this AFElementType. The default is no filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseFindEventFrameAttributes

> ItemsAttribute assetDatabaseFindEventFrameAttributes(webId, opts)

Retrieves a list of event frame attributes matching the specified filters from the specified asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database to use as the root of the search.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'attributeCategory': "attributeCategory_example", // String | Specify that returned attributes must have this category. The default is no filter.
  'attributeDescriptionFilter': "attributeDescriptionFilter_example", // String | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
  'attributeNameFilter': "attributeNameFilter_example", // String | The attribute name filter string used for finding objects. The default is no filter.
  'attributeType': "attributeType_example", // String | Specify that returned attributes' value type must be this value type. The default is no filter.
  'endTime': "endTime_example", // String | A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is '*'.
  'eventFrameCategory': "eventFrameCategory_example", // String | Specify that the owner of the returned attributes must have this category. The default is no filter.
  'eventFrameDescriptionFilter': "eventFrameDescriptionFilter_example", // String | The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
  'eventFrameNameFilter': "eventFrameNameFilter_example", // String | The event frame name filter string used for finding objects. The default is no filter.
  'eventFrameTemplate': "eventFrameTemplate_example", // String | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned (the page size). The default is 1000.
  'referencedElementNameFilter': "referencedElementNameFilter_example", // String | The name query string which must match the name of a referenced element. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.
  'searchMode': "searchMode_example", // String | Determines how the startTime and endTime parameters are treated when searching for event frames. The default is 'Overlapped'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'startTime': "startTime_example", // String | A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is '*-8h'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseFindEventFrameAttributes(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database to use as the root of the search. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **attributeCategory** | **String**| Specify that returned attributes must have this category. The default is no filter. | [optional] 
 **attributeDescriptionFilter** | **String**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **attributeNameFilter** | **String**| The attribute name filter string used for finding objects. The default is no filter. | [optional] 
 **attributeType** | **String**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] 
 **endTime** | **String**| A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is &#39;*&#39;. | [optional] 
 **eventFrameCategory** | **String**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] 
 **eventFrameDescriptionFilter** | **String**| The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **eventFrameNameFilter** | **String**| The event frame name filter string used for finding objects. The default is no filter. | [optional] 
 **eventFrameTemplate** | **String**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] 
 **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] 
 **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frames. The default is &#39;Overlapped&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **startTime** | **String**| A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is &#39;*-8h&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGet

> AssetDatabase assetDatabaseGet(webId, opts)

Retrieve an Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AssetDatabase**](AssetDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetAnalysisCategories

> ItemsAnalysisCategory assetDatabaseGetAnalysisCategories(webId, opts)

Retrieve analysis categories for a given Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetAnalysisCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnalysisCategory**](ItemsAnalysisCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetAnalysisTemplates

> ItemsAnalysisTemplate assetDatabaseGetAnalysisTemplates(webId, field, opts)

Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.

Users can search for the analysis templates based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database to search.
let field = ["null"]; // [String] | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
let opts = {
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'query': "query_example", // String | The query string used for finding objects. The default is no query string.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetAnalysisTemplates(webId, field, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database to search. | 
 **field** | [**[String]**](String.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **String**| The query string used for finding objects. The default is no query string. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnalysisTemplate**](ItemsAnalysisTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetAttributeCategories

> ItemsAttributeCategory assetDatabaseGetAttributeCategories(webId, opts)

Retrieve attribute categories for a given Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetAttributeCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttributeCategory**](ItemsAttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetByPath

> AssetDatabase assetDatabaseGetByPath(path, opts)

Retrieve an Asset Database by path.

This method returns an asset database based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let path = "path_example"; // String | The path to the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AssetDatabase**](AssetDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetElementCategories

> ItemsElementCategory assetDatabaseGetElementCategories(webId, opts)

Retrieve element categories for a given Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetElementCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElementCategory**](ItemsElementCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetElementTemplates

> ItemsElementTemplate assetDatabaseGetElementTemplates(webId, field, opts)

Retrieve element templates based on the specified criteria. Only templates of instance type \&quot;Element\&quot; and \&quot;EventFrame\&quot; are returned. By default, all element and event frame templates in the specified Asset Database are returned.

Users can search for the element and event frame template based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database to search.
let field = ["null"]; // [String] | Specifies which of the object's properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is 'Name'.
let opts = {
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'query': "query_example", // String | The query string used for finding objects. The default is no query string.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetElementTemplates(webId, field, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database to search. | 
 **field** | [**[String]**](String.md)| Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;. | 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **String**| The query string used for finding objects. The default is no query string. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElementTemplate**](ItemsElementTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetElements

> ItemsElement assetDatabaseGetElements(webId, opts)

Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.

Users can search for the elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database to use as the root of the search.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
  'categoryName': "categoryName_example", // String | Specify that returned elements must have this category. The default is no category filter.
  'descriptionFilter': "descriptionFilter_example", // String | Specify that returned elements must have this description. The default is no description filter.
  'elementType': "elementType_example", // String | Specify that returned elements must have this type. The default type is 'Any'.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding objects. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'templateName': "templateName_example", // String | Specify that returned elements must have this template or a template derived from this template. The default is no template filter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetElements(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database to use as the root of the search. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned. | [optional] 
 **categoryName** | **String**| Specify that returned elements must have this category. The default is no category filter. | [optional] 
 **descriptionFilter** | **String**| Specify that returned elements must have this description. The default is no description filter. | [optional] 
 **elementType** | **String**| Specify that returned elements must have this type. The default type is &#39;Any&#39;. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding objects. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **templateName** | **String**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElement**](ItemsElement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetEnumerationSets

> ItemsEnumerationSet assetDatabaseGetEnumerationSets(webId, opts)

Retrieve enumeration sets for given asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetEnumerationSets(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsEnumerationSet**](ItemsEnumerationSet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetEventFrames

> ItemsEventFrame assetDatabaseGetEventFrames(webId, opts)

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database to use as the root of the search.
let opts = {
  'canBeAcknowledged': true, // Boolean | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.
  'categoryName': "categoryName_example", // String | Specify that returned event frames must have this category. The default is no category filter.
  'endTime': "endTime_example", // String | The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values.
  'isAcknowledged': true, // Boolean | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding event frames. The default is no filter.
  'referencedElementNameFilter': "referencedElementNameFilter_example", // String | The name query string which must match the name of a referenced element. The default is no filter.
  'referencedElementTemplateName': "referencedElementTemplateName_example", // String | Specify that returned event frames must have an element in the event frame's referenced elements collection that derives from the template. Specify this parameter by name.
  'searchFullHierarchy': true, // Boolean | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.
  'searchMode': "searchMode_example", // String | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the 'Backward*' or 'Forward*' values, none of endTime, sortField, or sortOrder may be specified. The default is 'Overlapped'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'severity': ["null"], // [String] | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name' if searchMode is not one of the 'Backward*' or 'Forward*' values.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending' if searchMode is not one of the 'Backward*' or 'Forward*' values.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'startTime': "startTime_example", // String | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.
  'templateName': "templateName_example", // String | Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetEventFrames(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database to use as the root of the search. | 
 **canBeAcknowledged** | **Boolean**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] 
 **categoryName** | **String**| Specify that returned event frames must have this category. The default is no category filter. | [optional] 
 **endTime** | **String**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **isAcknowledged** | **Boolean**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding event frames. The default is no filter. | [optional] 
 **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **referencedElementTemplateName** | **String**| Specify that returned event frames must have an element in the event frame&#39;s referenced elements collection that derives from the template. Specify this parameter by name. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] 
 **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the &#39;Backward*&#39; or &#39;Forward*&#39; values, none of endTime, sortField, or sortOrder may be specified. The default is &#39;Overlapped&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **severity** | [**[String]**](String.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **startTime** | **String**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] 
 **templateName** | **String**| Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetReferencedElements

> ItemsElement assetDatabaseGetReferencedElements(webId, opts)

Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.

Users can search for the referenced elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the resource to use as the root of the search.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
  'categoryName': "categoryName_example", // String | Specify that returned elements must have this category. The default is no category filter.
  'descriptionFilter': "descriptionFilter_example", // String | Specify that returned elements must have this description. The default is no description filter.
  'elementType': "elementType_example", // String | Specify that returned elements must have this type. The default type is 'Any'.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding objects. The default is no filter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'templateName': "templateName_example", // String | Specify that returned elements must have this template or a template derived from this template. The default is no template filter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetReferencedElements(webId, opts, (error, data, response) => {
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
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned. | [optional] 
 **categoryName** | **String**| Specify that returned elements must have this category. The default is no category filter. | [optional] 
 **descriptionFilter** | **String**| Specify that returned elements must have this description. The default is no description filter. | [optional] 
 **elementType** | **String**| Specify that returned elements must have this type. The default type is &#39;Any&#39;. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding objects. The default is no filter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **templateName** | **String**| Specify that returned elements must have this template or a template derived from this template. The default is no template filter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElement**](ItemsElement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetSecurity

> ItemsSecurityRights assetDatabaseGetSecurity(webId, securityItem, userIdentity, opts)

Get the security information of the specified security item associated with the asset database for a specified user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database for the security to be checked.
let securityItem = ["null"]; // [String] | The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only 'Default' security item of the security information will be returned.
let userIdentity = ["null"]; // [String] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
let opts = {
  'forceRefresh': true, // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetSecurity(webId, securityItem, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database for the security to be checked. | 
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


## assetDatabaseGetSecurityEntries

> ItemsSecurityEntry assetDatabaseGetSecurityEntries(webId, opts)

Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database.
let opts = {
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering security entries. The default is no filter.
  'securityItem': "securityItem_example", // String | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetSecurityEntries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database. | 
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


## assetDatabaseGetSecurityEntryByName

> SecurityEntry assetDatabaseGetSecurityEntryByName(name, webId, opts)

Retrieve the security entry of the specified security item associated with the asset database with the specified name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the asset database.
let opts = {
  'securityItem': "securityItem_example", // String | The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the 'Default' security item will be returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetSecurityEntryByName(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database. | 
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


## assetDatabaseGetTableCategories

> ItemsTableCategory assetDatabaseGetTableCategories(webId, opts)

Retrieve table categories for a given Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetTableCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsTableCategory**](ItemsTableCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseGetTables

> ItemsTable assetDatabaseGetTables(webId, opts)

Retrieve tables for given Asset Database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.assetDatabaseGetTables(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsTable**](ItemsTable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## assetDatabaseImport

> assetDatabaseImport(webId, opts)

Import an asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the asset database.
let opts = {
  'importMode': ["null"] // [String] | Indicates the type of import to perform. The default is 'AllowCreate | AllowUpdate | AutoCheckIn'. Multiple import modes may be specified by using multiple instances of importMode.
};
apiInstance.assetDatabaseImport(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database. | 
 **importMode** | [**[String]**](String.md)| Indicates the type of import to perform. The default is &#39;AllowCreate | AllowUpdate | AutoCheckIn&#39;. Multiple import modes may be specified by using multiple instances of importMode. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assetDatabaseRemoveReferencedElement

> assetDatabaseRemoveReferencedElement(webId, referencedElementWebId)

Remove a reference to an existing element from the specified database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database which the referenced element will be removed from.
let referencedElementWebId = ["null"]; // [String] | The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
apiInstance.assetDatabaseRemoveReferencedElement(webId, referencedElementWebId, (error, data, response) => {
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
 **webId** | **String**| The ID of the database which the referenced element will be removed from. | 
 **referencedElementWebId** | [**[String]**](String.md)| The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assetDatabaseUpdate

> assetDatabaseUpdate(webId, database)

Update an asset database by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let webId = "webId_example"; // String | The ID of the database.
let database = new PiWebApi2018Sp1SwaggerSpec.AssetDatabase(); // AssetDatabase | A partial database containing the desired changes.
apiInstance.assetDatabaseUpdate(webId, database, (error, data, response) => {
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
 **webId** | **String**| The ID of the database. | 
 **database** | [**AssetDatabase**](AssetDatabase.md)| A partial database containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## assetDatabaseUpdateSecurityEntry

> assetDatabaseUpdateSecurityEntry(name, webId, securityEntry, opts)

Update a security entry owned by the asset database.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AssetDatabaseApi();
let name = "name_example"; // String | The name of the security entry.
let webId = "webId_example"; // String | The ID of the asset database where the security entry will be updated.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'securityItem': "securityItem_example" // String | The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the 'Default' security item will be updated.
};
apiInstance.assetDatabaseUpdateSecurityEntry(name, webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the asset database where the security entry will be updated. | 
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

