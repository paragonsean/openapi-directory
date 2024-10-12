# AirbyteConfigurationApi.DestinationDefinitionApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomDestinationDefinition**](DestinationDefinitionApi.md#createCustomDestinationDefinition) | **POST** /v1/destination_definitions/create_custom | Creates a custom destinationDefinition for the given workspace
[**deleteDestinationDefinition**](DestinationDefinitionApi.md#deleteDestinationDefinition) | **POST** /v1/destination_definitions/delete | Delete a destination definition
[**getDestinationDefinition**](DestinationDefinitionApi.md#getDestinationDefinition) | **POST** /v1/destination_definitions/get | Get destinationDefinition
[**getDestinationDefinitionForWorkspace**](DestinationDefinitionApi.md#getDestinationDefinitionForWorkspace) | **POST** /v1/destination_definitions/get_for_workspace | Get a destinationDefinition that is configured for the given workspace
[**grantDestinationDefinitionToWorkspace**](DestinationDefinitionApi.md#grantDestinationDefinitionToWorkspace) | **POST** /v1/destination_definitions/grant_definition | grant a private, non-custom destinationDefinition to a given workspace
[**listDestinationDefinitions**](DestinationDefinitionApi.md#listDestinationDefinitions) | **POST** /v1/destination_definitions/list | List all the destinationDefinitions the current Airbyte deployment is configured to use
[**listDestinationDefinitionsForWorkspace**](DestinationDefinitionApi.md#listDestinationDefinitionsForWorkspace) | **POST** /v1/destination_definitions/list_for_workspace | List all the destinationDefinitions the given workspace is configured to use
[**listLatestDestinationDefinitions**](DestinationDefinitionApi.md#listLatestDestinationDefinitions) | **POST** /v1/destination_definitions/list_latest | List the latest destinationDefinitions Airbyte supports
[**listPrivateDestinationDefinitions**](DestinationDefinitionApi.md#listPrivateDestinationDefinitions) | **POST** /v1/destination_definitions/list_private | List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.
[**revokeDestinationDefinitionFromWorkspace**](DestinationDefinitionApi.md#revokeDestinationDefinitionFromWorkspace) | **POST** /v1/destination_definitions/revoke_definition | revoke a grant to a private, non-custom destinationDefinition from a given workspace
[**updateDestinationDefinition**](DestinationDefinitionApi.md#updateDestinationDefinition) | **POST** /v1/destination_definitions/update | Update destinationDefinition



## createCustomDestinationDefinition

> DestinationDefinitionRead createCustomDestinationDefinition(opts)

Creates a custom destinationDefinition for the given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let opts = {
  'customDestinationDefinitionCreate': new AirbyteConfigurationApi.CustomDestinationDefinitionCreate() // CustomDestinationDefinitionCreate | 
};
apiInstance.createCustomDestinationDefinition(opts, (error, data, response) => {
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
 **customDestinationDefinitionCreate** | [**CustomDestinationDefinitionCreate**](CustomDestinationDefinitionCreate.md)|  | [optional] 

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDestinationDefinition

> deleteDestinationDefinition(destinationDefinitionIdRequestBody)

Delete a destination definition

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let destinationDefinitionIdRequestBody = new AirbyteConfigurationApi.DestinationDefinitionIdRequestBody(); // DestinationDefinitionIdRequestBody | 
apiInstance.deleteDestinationDefinition(destinationDefinitionIdRequestBody, (error, data, response) => {
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
 **destinationDefinitionIdRequestBody** | [**DestinationDefinitionIdRequestBody**](DestinationDefinitionIdRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDestinationDefinition

> DestinationDefinitionRead getDestinationDefinition(destinationDefinitionIdRequestBody)

Get destinationDefinition

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let destinationDefinitionIdRequestBody = new AirbyteConfigurationApi.DestinationDefinitionIdRequestBody(); // DestinationDefinitionIdRequestBody | 
apiInstance.getDestinationDefinition(destinationDefinitionIdRequestBody, (error, data, response) => {
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
 **destinationDefinitionIdRequestBody** | [**DestinationDefinitionIdRequestBody**](DestinationDefinitionIdRequestBody.md)|  | 

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDestinationDefinitionForWorkspace

> DestinationDefinitionRead getDestinationDefinitionForWorkspace(destinationDefinitionIdWithWorkspaceId)

Get a destinationDefinition that is configured for the given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let destinationDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
apiInstance.getDestinationDefinitionForWorkspace(destinationDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | 

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## grantDestinationDefinitionToWorkspace

> PrivateDestinationDefinitionRead grantDestinationDefinitionToWorkspace(destinationDefinitionIdWithWorkspaceId)

grant a private, non-custom destinationDefinition to a given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let destinationDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
apiInstance.grantDestinationDefinitionToWorkspace(destinationDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | 

### Return type

[**PrivateDestinationDefinitionRead**](PrivateDestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDestinationDefinitions

> DestinationDefinitionReadList listDestinationDefinitions()

List all the destinationDefinitions the current Airbyte deployment is configured to use

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
apiInstance.listDestinationDefinitions((error, data, response) => {
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

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDestinationDefinitionsForWorkspace

> DestinationDefinitionReadList listDestinationDefinitionsForWorkspace(opts)

List all the destinationDefinitions the given workspace is configured to use

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let opts = {
  'workspaceIdRequestBody': new AirbyteConfigurationApi.WorkspaceIdRequestBody() // WorkspaceIdRequestBody | 
};
apiInstance.listDestinationDefinitionsForWorkspace(opts, (error, data, response) => {
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

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLatestDestinationDefinitions

> DestinationDefinitionReadList listLatestDestinationDefinitions()

List the latest destinationDefinitions Airbyte supports

Guaranteed to retrieve the latest information on supported destinations.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
apiInstance.listLatestDestinationDefinitions((error, data, response) => {
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

[**DestinationDefinitionReadList**](DestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPrivateDestinationDefinitions

> PrivateDestinationDefinitionReadList listPrivateDestinationDefinitions(opts)

List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace&#39;s grants.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let opts = {
  'workspaceIdRequestBody': new AirbyteConfigurationApi.WorkspaceIdRequestBody() // WorkspaceIdRequestBody | 
};
apiInstance.listPrivateDestinationDefinitions(opts, (error, data, response) => {
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

[**PrivateDestinationDefinitionReadList**](PrivateDestinationDefinitionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## revokeDestinationDefinitionFromWorkspace

> revokeDestinationDefinitionFromWorkspace(destinationDefinitionIdWithWorkspaceId)

revoke a grant to a private, non-custom destinationDefinition from a given workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let destinationDefinitionIdWithWorkspaceId = new AirbyteConfigurationApi.DestinationDefinitionIdWithWorkspaceId(); // DestinationDefinitionIdWithWorkspaceId | 
apiInstance.revokeDestinationDefinitionFromWorkspace(destinationDefinitionIdWithWorkspaceId, (error, data, response) => {
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
 **destinationDefinitionIdWithWorkspaceId** | [**DestinationDefinitionIdWithWorkspaceId**](DestinationDefinitionIdWithWorkspaceId.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDestinationDefinition

> DestinationDefinitionRead updateDestinationDefinition(destinationDefinitionUpdate)

Update destinationDefinition

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationDefinitionApi();
let destinationDefinitionUpdate = new AirbyteConfigurationApi.DestinationDefinitionUpdate(); // DestinationDefinitionUpdate | 
apiInstance.updateDestinationDefinition(destinationDefinitionUpdate, (error, data, response) => {
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
 **destinationDefinitionUpdate** | [**DestinationDefinitionUpdate**](DestinationDefinitionUpdate.md)|  | 

### Return type

[**DestinationDefinitionRead**](DestinationDefinitionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

