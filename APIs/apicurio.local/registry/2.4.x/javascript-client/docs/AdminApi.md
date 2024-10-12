# ApicurioRegistryApiV2.AdminApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGlobalRule_0**](AdminApi.md#createGlobalRule_0) | **POST** /admin/rules | Create global rule
[**createRoleMapping**](AdminApi.md#createRoleMapping) | **POST** /admin/roleMappings | Create a new role mapping
[**deleteAllGlobalRules_0**](AdminApi.md#deleteAllGlobalRules_0) | **DELETE** /admin/rules | Delete all global rules
[**deleteGlobalRule_0**](AdminApi.md#deleteGlobalRule_0) | **DELETE** /admin/rules/{rule} | Delete global rule
[**deleteRoleMapping**](AdminApi.md#deleteRoleMapping) | **DELETE** /admin/roleMappings/{principalId} | Delete a role mapping
[**exportData**](AdminApi.md#exportData) | **GET** /admin/export | Export registry data
[**getConfigProperty**](AdminApi.md#getConfigProperty) | **GET** /admin/config/properties/{propertyName} | Get configuration property value
[**getGlobalRuleConfig_0**](AdminApi.md#getGlobalRuleConfig_0) | **GET** /admin/rules/{rule} | Get global rule configuration
[**getLogConfiguration**](AdminApi.md#getLogConfiguration) | **GET** /admin/loggers/{logger} | Get a single logger configuration
[**getRoleMapping**](AdminApi.md#getRoleMapping) | **GET** /admin/roleMappings/{principalId} | Return a single role mapping
[**importData**](AdminApi.md#importData) | **POST** /admin/import | Import registry data
[**listArtifactTypes_0**](AdminApi.md#listArtifactTypes_0) | **GET** /admin/artifactTypes | List artifact types
[**listConfigProperties**](AdminApi.md#listConfigProperties) | **GET** /admin/config/properties | List all configuration properties
[**listGlobalRules_0**](AdminApi.md#listGlobalRules_0) | **GET** /admin/rules | List global rules
[**listLogConfigurations**](AdminApi.md#listLogConfigurations) | **GET** /admin/loggers | List logging configurations
[**listRoleMappings**](AdminApi.md#listRoleMappings) | **GET** /admin/roleMappings | List all role mappings
[**removeLogConfiguration**](AdminApi.md#removeLogConfiguration) | **DELETE** /admin/loggers/{logger} | Removes logger configuration
[**resetConfigProperty**](AdminApi.md#resetConfigProperty) | **DELETE** /admin/config/properties/{propertyName} | Reset a configuration property
[**setLogConfiguration**](AdminApi.md#setLogConfiguration) | **PUT** /admin/loggers/{logger} | Set a logger&#39;s configuration
[**updateConfigProperty**](AdminApi.md#updateConfigProperty) | **PUT** /admin/config/properties/{propertyName} | Update a configuration property
[**updateGlobalRuleConfig_0**](AdminApi.md#updateGlobalRuleConfig_0) | **PUT** /admin/rules/{rule} | Update global rule configuration
[**updateRoleMapping**](AdminApi.md#updateRoleMapping) | **PUT** /admin/roleMappings/{principalId} | Update a role mapping



## createGlobalRule_0

> createGlobalRule_0(rule)

Create global rule

Adds a rule to the list of globally configured rules.  This operation can fail for the following reasons:  * The rule type is unknown (HTTP error &#x60;400&#x60;) * The rule already exists (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let rule = new ApicurioRegistryApiV2.Rule(); // Rule | 
apiInstance.createGlobalRule_0(rule, (error, data, response) => {
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
 **rule** | [**Rule**](Rule.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoleMapping

> createRoleMapping(roleMapping)

Create a new role mapping

Creates a new mapping between a user/principal and a role.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;)  

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let roleMapping = new ApicurioRegistryApiV2.RoleMapping(); // RoleMapping | 
apiInstance.createRoleMapping(roleMapping, (error, data, response) => {
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
 **roleMapping** | [**RoleMapping**](RoleMapping.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAllGlobalRules_0

> deleteAllGlobalRules_0()

Delete all global rules

Deletes all globally configured rules.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
apiInstance.deleteAllGlobalRules_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGlobalRule_0

> deleteGlobalRule_0(rule)

Delete global rule

Deletes a single global rule.  If this is the only rule configured, this is the same as deleting **all** rules.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * Rule cannot be deleted (HTTP error &#x60;409&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let rule = new ApicurioRegistryApiV2.RuleType(); // RuleType | The unique name/type of a rule.
apiInstance.deleteGlobalRule_0(rule, (error, data, response) => {
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
 **rule** | [**RuleType**](.md)| The unique name/type of a rule. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRoleMapping

> deleteRoleMapping(principalId)

Delete a role mapping

Deletes a single role mapping, effectively denying access to a user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let principalId = "principalId_example"; // String | Unique id of a principal (typically either a user or service account).
apiInstance.deleteRoleMapping(principalId, (error, data, response) => {
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
 **principalId** | **String**| Unique id of a principal (typically either a user or service account). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportData

> DownloadRef exportData(opts)

Export registry data

Exports registry data as a ZIP archive.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let opts = {
  'forBrowser': true // Boolean | Indicates if the operation is done for a browser.  If true, the response will be a JSON payload with a property called `href`.  This `href` will be a single-use, naked download link suitable for use by a web browser to download the content.
};
apiInstance.exportData(opts, (error, data, response) => {
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
 **forBrowser** | **Boolean**| Indicates if the operation is done for a browser.  If true, the response will be a JSON payload with a property called &#x60;href&#x60;.  This &#x60;href&#x60; will be a single-use, naked download link suitable for use by a web browser to download the content. | [optional] 

### Return type

[**DownloadRef**](DownloadRef.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/zip


## getConfigProperty

> ConfigurationProperty getConfigProperty(propertyName)

Get configuration property value

Returns the value of a single configuration property.  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let propertyName = "propertyName_example"; // String | The name of a configuration property.
apiInstance.getConfigProperty(propertyName, (error, data, response) => {
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
 **propertyName** | **String**| The name of a configuration property. | 

### Return type

[**ConfigurationProperty**](ConfigurationProperty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGlobalRuleConfig_0

> Rule getGlobalRuleConfig_0(rule)

Get global rule configuration

Returns information about the named globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let rule = new ApicurioRegistryApiV2.RuleType(); // RuleType | The unique name/type of a rule.
apiInstance.getGlobalRuleConfig_0(rule, (error, data, response) => {
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
 **rule** | [**RuleType**](.md)| The unique name/type of a rule. | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLogConfiguration

> NamedLogConfiguration getLogConfiguration(logger)

Get a single logger configuration

Returns the configured logger configuration for the provided logger name, if no logger configuration is persisted it will return the current default log configuration in the system.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let logger = "logger_example"; // String | The name of a single logger.
apiInstance.getLogConfiguration(logger, (error, data, response) => {
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
 **logger** | **String**| The name of a single logger. | 

### Return type

[**NamedLogConfiguration**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoleMapping

> RoleMapping getRoleMapping(principalId)

Return a single role mapping

Gets the details of a single role mapping (by &#x60;principalId&#x60;).  This operation can fail for the following reasons:  * No role mapping for the &#x60;principalId&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let principalId = "principalId_example"; // String | Unique id of a principal (typically either a user or service account).
apiInstance.getRoleMapping(principalId, (error, data, response) => {
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
 **principalId** | **String**| Unique id of a principal (typically either a user or service account). | 

### Return type

[**RoleMapping**](RoleMapping.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importData

> importData(body, opts)

Import registry data

Imports registry data that was previously exported using the &#x60;/admin/export&#x60; operation.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let body = "/path/to/file"; // File | The ZIP file representing the previously exported registry data.
let opts = {
  'xRegistryPreserveGlobalId': true, // Boolean | If this header is set to false, global ids of imported data will be ignored and replaced by next id in global id sequence. This allows to import any data even thought the global ids would cause a conflict.
  'xRegistryPreserveContentId': true // Boolean | If this header is set to false, content ids of imported data will be ignored and replaced by next id in content id sequence. The mapping between content and artifacts will be preserved. This allows to import any data even thought the content ids would cause a conflict.
};
apiInstance.importData(body, opts, (error, data, response) => {
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
 **body** | **File**| The ZIP file representing the previously exported registry data. | 
 **xRegistryPreserveGlobalId** | **Boolean**| If this header is set to false, global ids of imported data will be ignored and replaced by next id in global id sequence. This allows to import any data even thought the global ids would cause a conflict. | [optional] 
 **xRegistryPreserveContentId** | **Boolean**| If this header is set to false, content ids of imported data will be ignored and replaced by next id in content id sequence. The mapping between content and artifacts will be preserved. This allows to import any data even thought the content ids would cause a conflict. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/zip
- **Accept**: application/json


## listArtifactTypes_0

> [ArtifactTypeInfo] listArtifactTypes_0()

List artifact types

Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
apiInstance.listArtifactTypes_0((error, data, response) => {
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

[**[ArtifactTypeInfo]**](ArtifactTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigProperties

> [ConfigurationProperty] listConfigProperties()

List all configuration properties

Returns a list of all configuration properties that have been set.  The list is not paged.  This operation may fail for one of the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
apiInstance.listConfigProperties((error, data, response) => {
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

[**[ConfigurationProperty]**](ConfigurationProperty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listGlobalRules_0

> [RuleType] listGlobalRules_0()

List global rules

Gets a list of all the currently configured global rules (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
apiInstance.listGlobalRules_0((error, data, response) => {
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

[**[RuleType]**](RuleType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLogConfigurations

> [NamedLogConfiguration] listLogConfigurations()

List logging configurations

List all of the configured logging levels.  These override the default logging configuration.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
apiInstance.listLogConfigurations((error, data, response) => {
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

[**[NamedLogConfiguration]**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoleMappings

> [RoleMapping] listRoleMappings()

List all role mappings

Gets a list of all role mappings configured in the registry (if any).  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
apiInstance.listRoleMappings((error, data, response) => {
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

[**[RoleMapping]**](RoleMapping.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeLogConfiguration

> NamedLogConfiguration removeLogConfiguration(logger)

Removes logger configuration

Removes the configured logger configuration (if any) for the given logger.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let logger = "logger_example"; // String | The name of a single logger.
apiInstance.removeLogConfiguration(logger, (error, data, response) => {
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
 **logger** | **String**| The name of a single logger. | 

### Return type

[**NamedLogConfiguration**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetConfigProperty

> resetConfigProperty(propertyName)

Reset a configuration property

Resets the value of a single configuration property.  This will return the property to its default value (see external documentation for supported properties and their default values).  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let propertyName = "propertyName_example"; // String | The name of a configuration property.
apiInstance.resetConfigProperty(propertyName, (error, data, response) => {
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
 **propertyName** | **String**| The name of a configuration property. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setLogConfiguration

> NamedLogConfiguration setLogConfiguration(logger, logConfiguration)

Set a logger&#39;s configuration

Configures the logger referenced by the provided logger name with the given configuration.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let logger = "logger_example"; // String | The name of a single logger.
let logConfiguration = new ApicurioRegistryApiV2.LogConfiguration(); // LogConfiguration | The new logger configuration.
apiInstance.setLogConfiguration(logger, logConfiguration, (error, data, response) => {
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
 **logger** | **String**| The name of a single logger. | 
 **logConfiguration** | [**LogConfiguration**](LogConfiguration.md)| The new logger configuration. | 

### Return type

[**NamedLogConfiguration**](NamedLogConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfigProperty

> updateConfigProperty(propertyName, updateConfigurationProperty)

Update a configuration property

Updates the value of a single configuration property.  This operation may fail for one of the following reasons:  * Property not found or not configured (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let propertyName = "propertyName_example"; // String | The name of a configuration property.
let updateConfigurationProperty = new ApicurioRegistryApiV2.UpdateConfigurationProperty(); // UpdateConfigurationProperty | 
apiInstance.updateConfigProperty(propertyName, updateConfigurationProperty, (error, data, response) => {
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
 **propertyName** | **String**| The name of a configuration property. | 
 **updateConfigurationProperty** | [**UpdateConfigurationProperty**](UpdateConfigurationProperty.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGlobalRuleConfig_0

> Rule updateGlobalRuleConfig_0(rule, rule2)

Update global rule configuration

Updates the configuration for a globally configured rule.  This operation can fail for the following reasons:  * Invalid rule name/type (HTTP error &#x60;400&#x60;) * No rule with name/type &#x60;rule&#x60; exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let rule = new ApicurioRegistryApiV2.RuleType(); // RuleType | The unique name/type of a rule.
let rule2 = new ApicurioRegistryApiV2.Rule(); // Rule | 
apiInstance.updateGlobalRuleConfig_0(rule, rule2, (error, data, response) => {
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
 **rule** | [**RuleType**](.md)| The unique name/type of a rule. | 
 **rule2** | [**Rule**](Rule.md)|  | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoleMapping

> updateRoleMapping(principalId, updateRole)

Update a role mapping

Updates a single role mapping for one user/principal.  This operation can fail for the following reasons:  * No role mapping for the principalId exists (HTTP error &#x60;404&#x60;) * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.AdminApi();
let principalId = "principalId_example"; // String | Unique id of a principal (typically either a user or service account).
let updateRole = new ApicurioRegistryApiV2.UpdateRole(); // UpdateRole | 
apiInstance.updateRoleMapping(principalId, updateRole, (error, data, response) => {
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
 **principalId** | **String**| Unique id of a principal (typically either a user or service account). | 
 **updateRole** | [**UpdateRole**](UpdateRole.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

