# AirbyteConfigurationApi.WorkspaceApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWorkspace**](WorkspaceApi.md#createWorkspace) | **POST** /v1/workspaces/create | Creates a workspace
[**deleteWorkspace**](WorkspaceApi.md#deleteWorkspace) | **POST** /v1/workspaces/delete | Deletes a workspace
[**getWorkspace**](WorkspaceApi.md#getWorkspace) | **POST** /v1/workspaces/get | Find workspace by ID
[**getWorkspaceByConnectionId**](WorkspaceApi.md#getWorkspaceByConnectionId) | **POST** /v1/workspaces/get_by_connection_id | Find workspace by connection id
[**getWorkspaceBySlug**](WorkspaceApi.md#getWorkspaceBySlug) | **POST** /v1/workspaces/get_by_slug | Find workspace by slug
[**listWorkspaces**](WorkspaceApi.md#listWorkspaces) | **POST** /v1/workspaces/list | List all workspaces registered in the current Airbyte deployment
[**updateWorkspace**](WorkspaceApi.md#updateWorkspace) | **POST** /v1/workspaces/update | Update workspace state
[**updateWorkspaceFeedback**](WorkspaceApi.md#updateWorkspaceFeedback) | **POST** /v1/workspaces/tag_feedback_status_as_done | Update workspace feedback state
[**updateWorkspaceName**](WorkspaceApi.md#updateWorkspaceName) | **POST** /v1/workspaces/update_name | Update workspace name



## createWorkspace

> WorkspaceRead createWorkspace(workspaceCreate)

Creates a workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let workspaceCreate = new AirbyteConfigurationApi.WorkspaceCreate(); // WorkspaceCreate | 
apiInstance.createWorkspace(workspaceCreate, (error, data, response) => {
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
 **workspaceCreate** | [**WorkspaceCreate**](WorkspaceCreate.md)|  | 

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteWorkspace

> deleteWorkspace(workspaceIdRequestBody)

Deletes a workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let workspaceIdRequestBody = new AirbyteConfigurationApi.WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
apiInstance.deleteWorkspace(workspaceIdRequestBody, (error, data, response) => {
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
 **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkspace

> WorkspaceRead getWorkspace(workspaceIdRequestBody)

Find workspace by ID

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let workspaceIdRequestBody = new AirbyteConfigurationApi.WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
apiInstance.getWorkspace(workspaceIdRequestBody, (error, data, response) => {
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
 **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | 

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkspaceByConnectionId

> WorkspaceRead getWorkspaceByConnectionId(connectionIdRequestBody)

Find workspace by connection id

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let connectionIdRequestBody = new AirbyteConfigurationApi.ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
apiInstance.getWorkspaceByConnectionId(connectionIdRequestBody, (error, data, response) => {
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
 **connectionIdRequestBody** | [**ConnectionIdRequestBody**](ConnectionIdRequestBody.md)|  | 

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkspaceBySlug

> WorkspaceRead getWorkspaceBySlug(slugRequestBody)

Find workspace by slug

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let slugRequestBody = new AirbyteConfigurationApi.SlugRequestBody(); // SlugRequestBody | 
apiInstance.getWorkspaceBySlug(slugRequestBody, (error, data, response) => {
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
 **slugRequestBody** | [**SlugRequestBody**](SlugRequestBody.md)|  | 

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listWorkspaces

> WorkspaceReadList listWorkspaces()

List all workspaces registered in the current Airbyte deployment

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
apiInstance.listWorkspaces((error, data, response) => {
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

[**WorkspaceReadList**](WorkspaceReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWorkspace

> WorkspaceRead updateWorkspace(workspaceUpdate)

Update workspace state

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let workspaceUpdate = new AirbyteConfigurationApi.WorkspaceUpdate(); // WorkspaceUpdate | 
apiInstance.updateWorkspace(workspaceUpdate, (error, data, response) => {
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
 **workspaceUpdate** | [**WorkspaceUpdate**](WorkspaceUpdate.md)|  | 

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkspaceFeedback

> updateWorkspaceFeedback(workspaceGiveFeedback)

Update workspace feedback state

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let workspaceGiveFeedback = new AirbyteConfigurationApi.WorkspaceGiveFeedback(); // WorkspaceGiveFeedback | 
apiInstance.updateWorkspaceFeedback(workspaceGiveFeedback, (error, data, response) => {
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
 **workspaceGiveFeedback** | [**WorkspaceGiveFeedback**](WorkspaceGiveFeedback.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateWorkspaceName

> WorkspaceRead updateWorkspaceName(workspaceUpdateName)

Update workspace name

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WorkspaceApi();
let workspaceUpdateName = new AirbyteConfigurationApi.WorkspaceUpdateName(); // WorkspaceUpdateName | 
apiInstance.updateWorkspaceName(workspaceUpdateName, (error, data, response) => {
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
 **workspaceUpdateName** | [**WorkspaceUpdateName**](WorkspaceUpdateName.md)|  | 

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

