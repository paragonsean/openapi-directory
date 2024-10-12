# AirbyteConfigurationApi.SourceDefinitionApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomSourceDefinition**](SourceDefinitionApi.md#createCustomSourceDefinition) | **POST** /v1/source_definitions/create_custom | Creates a custom sourceDefinition for the given workspace
[**deleteSourceDefinition**](SourceDefinitionApi.md#deleteSourceDefinition) | **POST** /v1/source_definitions/delete | Delete a source definition
[**getSourceDefinition**](SourceDefinitionApi.md#getSourceDefinition) | **POST** /v1/source_definitions/get | Get source
[**getSourceDefinitionForWorkspace**](SourceDefinitionApi.md#getSourceDefinitionForWorkspace) | **POST** /v1/source_definitions/get_for_workspace | Get a sourceDefinition that is configured for the given workspace
[**grantSourceDefinitionToWorkspace**](SourceDefinitionApi.md#grantSourceDefinitionToWorkspace) | **POST** /v1/source_definitions/grant_definition | grant a private, non-custom sourceDefinition to a given workspace
[**listLatestSourceDefinitions**](SourceDefinitionApi.md#listLatestSourceDefinitions) | **POST** /v1/source_definitions/list_latest | List the latest sourceDefinitions Airbyte supports
[**listPrivateSourceDefinitions**](SourceDefinitionApi.md#listPrivateSourceDefinitions) | **POST** /v1/source_definitions/list_private | List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.
[**listSourceDefinitions**](SourceDefinitionApi.md#listSourceDefinitions) | **POST** /v1/source_definitions/list | List all the sourceDefinitions the current Airbyte deployment is configured to use
[**listSourceDefinitionsForWorkspace**](SourceDefinitionApi.md#listSourceDefinitionsForWorkspace) | **POST** /v1/source_definitions/list_for_workspace | List all the sourceDefinitions the given workspace is configured to use
[**revokeSourceDefinitionFromWorkspace**](SourceDefinitionApi.md#revokeSourceDefinitionFromWorkspace) | **POST** /v1/source_definitions/revoke_definition | revoke a grant to a private, non-custom sourceDefinition from a given workspace
[**updateSourceDefinition**](SourceDefinitionApi.md#updateSourceDefinition) | **POST** /v1/source_definitions/update | Update a sourceDefinition



## createCustomSourceDefinition

> SourceDefinitionRead createCustomSourceDefinition(opts)

Creates a custom sourceDefinition for the given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let opts = {
  'customSourceDefinitionCreate': new AirbyteConfigurationApi.CustomSourceDefinitionCreate() // CustomSourceDefinitionCreate | 
};
apiInstance.createCustomSourceDefinition(opts, (error, data, response) => {
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
 **customSourceDefinitionCreate** | [**CustomSourceDefinitionCreate**](CustomSourceDefinitionCreate.md)|  | [optional] 

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSourceDefinition

> deleteSourceDefinition(sourceDefinitionIdRequestBody)

Delete a source definition

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let sourceDefinitionIdRequestBody = new AirbyteConfigurationApi.SourceDefinitionIdRequestBody(); // SourceDefinitionIdRequestBody | 
apiInstance.deleteSourceDefinition(sourceDefinitionIdRequestBody, (error, data, response) => {
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
 **sourceDefinitionIdRequestBody** | [**SourceDefinitionIdRequestBody**](SourceDefinitionIdRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSourceDefinition

> SourceDefinitionRead getSourceDefinition(sourceDefinitionIdRequestBody)

Get source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let sourceDefinitionIdRequestBody = new AirbyteConfigurationApi.SourceDefinitionIdRequestBody(); // SourceDefinitionIdRequestBody | 
apiInstance.getSourceDefinition(sourceDefinitionIdRequestBody, (error, data, response) => {
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
 **sourceDefinitionIdRequestBody** | [**SourceDefinitionIdRequestBody**](SourceDefinitionIdRequestBody.md)|  | 

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSourceDefinitionForWorkspace

> SourceDefinitionRead getSourceDefinitionForWorkspace(sourceDefinitionIdWithWorkspaceId)

Get a sourceDefinition that is configured for the given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let sourceDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
apiInstance.getSourceDefinitionForWorkspace(sourceDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | 

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## grantSourceDefinitionToWorkspace

> PrivateSourceDefinitionRead grantSourceDefinitionToWorkspace(sourceDefinitionIdWithWorkspaceId)

grant a private, non-custom sourceDefinition to a given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let sourceDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
apiInstance.grantSourceDefinitionToWorkspace(sourceDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | 

### Return type

[**PrivateSourceDefinitionRead**](PrivateSourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLatestSourceDefinitions

> SourceDefinitionReadList listLatestSourceDefinitions()

List the latest sourceDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported sources.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
apiInstance.listLatestSourceDefinitions((error, data, response) => {
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

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPrivateSourceDefinitions

> PrivateSourceDefinitionReadList listPrivateSourceDefinitions(opts)

List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let opts = {
  'workspaceIdRequestBody': new AirbyteConfigurationApi.WorkspaceIdRequestBody() // WorkspaceIdRequestBody | 
};
apiInstance.listPrivateSourceDefinitions(opts, (error, data, response) => {
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
 **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional] 

### Return type

[**PrivateSourceDefinitionReadList**](PrivateSourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSourceDefinitions

> SourceDefinitionReadList listSourceDefinitions()

List all the sourceDefinitions the current Airbyte deployment is configured to use

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
apiInstance.listSourceDefinitions((error, data, response) => {
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

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSourceDefinitionsForWorkspace

> SourceDefinitionReadList listSourceDefinitionsForWorkspace(opts)

List all the sourceDefinitions the given workspace is configured to use

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let opts = {
  'workspaceIdRequestBody': new AirbyteConfigurationApi.WorkspaceIdRequestBody() // WorkspaceIdRequestBody | 
};
apiInstance.listSourceDefinitionsForWorkspace(opts, (error, data, response) => {
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
 **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | [optional] 

### Return type

[**SourceDefinitionReadList**](SourceDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeSourceDefinitionFromWorkspace

> revokeSourceDefinitionFromWorkspace(sourceDefinitionIdWithWorkspaceId)

revoke a grant to a private, non-custom sourceDefinition from a given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let sourceDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.SourceDefinitionIdWithWorkspaceId(); // SourceDefinitionIdWithWorkspaceId | 
apiInstance.revokeSourceDefinitionFromWorkspace(sourceDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **sourceDefinitionIdWithWorkspaceId** | [**SourceDefinitionIdWithWorkspaceId**](SourceDefinitionIdWithWorkspaceId.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSourceDefinition

> SourceDefinitionRead updateSourceDefinition(opts)

Update a sourceDefinition

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceDefinitionApi();
let opts = {
  'sourceDefinitionUpdate': new AirbyteConfigurationApi.SourceDefinitionUpdate() // SourceDefinitionUpdate | 
};
apiInstance.updateSourceDefinition(opts, (error, data, response) => {
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
 **sourceDefinitionUpdate** | [**SourceDefinitionUpdate**](SourceDefinitionUpdate.md)|  | [optional] 

### Return type

[**SourceDefinitionRead**](SourceDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

