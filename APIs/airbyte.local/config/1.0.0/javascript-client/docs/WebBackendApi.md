# AirbyteConfigurationApi.WebBackendApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStateType**](WebBackendApi.md#getStateType) | **POST** /v1/web_backend/state/get_type | Fetch the current state type for a connection.
[**webBackendCheckUpdates**](WebBackendApi.md#webBackendCheckUpdates) | **POST** /v1/web_backend/check_updates | Returns a summary of source and destination definitions that could be updated.
[**webBackendCreateConnection**](WebBackendApi.md#webBackendCreateConnection) | **POST** /v1/web_backend/connections/create | Create a connection
[**webBackendGetConnection**](WebBackendApi.md#webBackendGetConnection) | **POST** /v1/web_backend/connections/get | Get a connection
[**webBackendGetWorkspaceState**](WebBackendApi.md#webBackendGetWorkspaceState) | **POST** /v1/web_backend/workspace/state | Returns the current state of a workspace
[**webBackendListConnectionsForWorkspace**](WebBackendApi.md#webBackendListConnectionsForWorkspace) | **POST** /v1/web_backend/connections/list | Returns all non-deleted connections for a workspace.
[**webBackendListGeographies**](WebBackendApi.md#webBackendListGeographies) | **POST** /v1/web_backend/geographies/list | Returns available geographies can be selected to run data syncs in a particular geography. The &#39;auto&#39; entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than &#39;auto&#39; are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 
[**webBackendUpdateConnection**](WebBackendApi.md#webBackendUpdateConnection) | **POST** /v1/web_backend/connections/update | Update a connection



## getStateType

> ConnectionStateType getStateType(connectionIdRequestBody)

Fetch the current state type for a connection.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
let connectionIdRequestBody = new AirbyteConfigurationApi.ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
apiInstance.getStateType(connectionIdRequestBody, (error, data, response) => {
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

[**ConnectionStateType**](ConnectionStateType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webBackendCheckUpdates

> WebBackendCheckUpdatesRead webBackendCheckUpdates()

Returns a summary of source and destination definitions that could be updated.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
apiInstance.webBackendCheckUpdates((error, data, response) => {
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

[**WebBackendCheckUpdatesRead**](WebBackendCheckUpdatesRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webBackendCreateConnection

> WebBackendConnectionRead webBackendCreateConnection(webBackendConnectionCreate)

Create a connection

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
let webBackendConnectionCreate = new AirbyteConfigurationApi.WebBackendConnectionCreate(); // WebBackendConnectionCreate | 
apiInstance.webBackendCreateConnection(webBackendConnectionCreate, (error, data, response) => {
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
 **webBackendConnectionCreate** | [**WebBackendConnectionCreate**](WebBackendConnectionCreate.md)|  | 

### Return type

[**WebBackendConnectionRead**](WebBackendConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webBackendGetConnection

> WebBackendConnectionRead webBackendGetConnection(webBackendConnectionRequestBody)

Get a connection

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
let webBackendConnectionRequestBody = new AirbyteConfigurationApi.WebBackendConnectionRequestBody(); // WebBackendConnectionRequestBody | 
apiInstance.webBackendGetConnection(webBackendConnectionRequestBody, (error, data, response) => {
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
 **webBackendConnectionRequestBody** | [**WebBackendConnectionRequestBody**](WebBackendConnectionRequestBody.md)|  | 

### Return type

[**WebBackendConnectionRead**](WebBackendConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webBackendGetWorkspaceState

> WebBackendWorkspaceStateResult webBackendGetWorkspaceState(opts)

Returns the current state of a workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
let opts = {
  'webBackendWorkspaceState': new AirbyteConfigurationApi.WebBackendWorkspaceState() // WebBackendWorkspaceState | 
};
apiInstance.webBackendGetWorkspaceState(opts, (error, data, response) => {
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
 **webBackendWorkspaceState** | [**WebBackendWorkspaceState**](WebBackendWorkspaceState.md)|  | [optional] 

### Return type

[**WebBackendWorkspaceStateResult**](WebBackendWorkspaceStateResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webBackendListConnectionsForWorkspace

> WebBackendConnectionReadList webBackendListConnectionsForWorkspace(webBackendConnectionListRequestBody)

Returns all non-deleted connections for a workspace.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
let webBackendConnectionListRequestBody = new AirbyteConfigurationApi.WebBackendConnectionListRequestBody(); // WebBackendConnectionListRequestBody | 
apiInstance.webBackendListConnectionsForWorkspace(webBackendConnectionListRequestBody, (error, data, response) => {
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
 **webBackendConnectionListRequestBody** | [**WebBackendConnectionListRequestBody**](WebBackendConnectionListRequestBody.md)|  | 

### Return type

[**WebBackendConnectionReadList**](WebBackendConnectionReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webBackendListGeographies

> WebBackendGeographiesListResult webBackendListGeographies()

Returns available geographies can be selected to run data syncs in a particular geography. The &#39;auto&#39; entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than &#39;auto&#39; are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 

Returns all available geographies in which a data sync can run.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
apiInstance.webBackendListGeographies((error, data, response) => {
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

[**WebBackendGeographiesListResult**](WebBackendGeographiesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webBackendUpdateConnection

> WebBackendConnectionRead webBackendUpdateConnection(webBackendConnectionUpdate)

Update a connection

Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the connection along with the rest of the operationIds in the request body. Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Note that if a catalog is present in the request body, the connection&#39;s entire catalog will be replaced with the catalog from the request. This means that to modify a single stream, the entire new catalog containing the updated stream needs to be sent. 

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.WebBackendApi();
let webBackendConnectionUpdate = new AirbyteConfigurationApi.WebBackendConnectionUpdate(); // WebBackendConnectionUpdate | 
apiInstance.webBackendUpdateConnection(webBackendConnectionUpdate, (error, data, response) => {
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
 **webBackendConnectionUpdate** | [**WebBackendConnectionUpdate**](WebBackendConnectionUpdate.md)|  | 

### Return type

[**WebBackendConnectionRead**](WebBackendConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

