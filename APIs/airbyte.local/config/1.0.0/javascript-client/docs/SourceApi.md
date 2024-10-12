# AirbyteConfigurationApi.SourceApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkConnectionToSource**](SourceApi.md#checkConnectionToSource) | **POST** /v1/sources/check_connection | Check connection to the source
[**checkConnectionToSourceForUpdate**](SourceApi.md#checkConnectionToSourceForUpdate) | **POST** /v1/sources/check_connection_for_update | Check connection for a proposed update to a source
[**cloneSource**](SourceApi.md#cloneSource) | **POST** /v1/sources/clone | Clone source
[**createSource**](SourceApi.md#createSource) | **POST** /v1/sources/create | Create a source
[**deleteSource**](SourceApi.md#deleteSource) | **POST** /v1/sources/delete | Delete a source
[**discoverSchemaForSource**](SourceApi.md#discoverSchemaForSource) | **POST** /v1/sources/discover_schema | Discover the schema catalog of the source
[**getMostRecentSourceActorCatalog**](SourceApi.md#getMostRecentSourceActorCatalog) | **POST** /v1/sources/most_recent_source_actor_catalog | Get most recent ActorCatalog for source
[**getSource**](SourceApi.md#getSource) | **POST** /v1/sources/get | Get source
[**listSourcesForWorkspace**](SourceApi.md#listSourcesForWorkspace) | **POST** /v1/sources/list | List sources for workspace
[**searchSources**](SourceApi.md#searchSources) | **POST** /v1/sources/search | Search sources
[**updateSource**](SourceApi.md#updateSource) | **POST** /v1/sources/update | Update a source
[**writeDiscoverCatalogResult**](SourceApi.md#writeDiscoverCatalogResult) | **POST** /v1/sources/write_discover_catalog_result | Should only called from worker, to write result from discover activity back to DB.



## checkConnectionToSource

> CheckConnectionRead checkConnectionToSource(sourceIdRequestBody)

Check connection to the source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceIdRequestBody = new AirbyteConfigurationApi.SourceIdRequestBody(); // SourceIdRequestBody | 
apiInstance.checkConnectionToSource(sourceIdRequestBody, (error, data, response) => {
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
 **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | 

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkConnectionToSourceForUpdate

> CheckConnectionRead checkConnectionToSourceForUpdate(sourceUpdate)

Check connection for a proposed update to a source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceUpdate = new AirbyteConfigurationApi.SourceUpdate(); // SourceUpdate | 
apiInstance.checkConnectionToSourceForUpdate(sourceUpdate, (error, data, response) => {
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
 **sourceUpdate** | [**SourceUpdate**](SourceUpdate.md)|  | 

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloneSource

> SourceRead cloneSource(sourceCloneRequestBody)

Clone source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceCloneRequestBody = new AirbyteConfigurationApi.SourceCloneRequestBody(); // SourceCloneRequestBody | 
apiInstance.cloneSource(sourceCloneRequestBody, (error, data, response) => {
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
 **sourceCloneRequestBody** | [**SourceCloneRequestBody**](SourceCloneRequestBody.md)|  | 

### Return type

[**SourceRead**](SourceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSource

> SourceRead createSource(sourceCreate)

Create a source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceCreate = new AirbyteConfigurationApi.SourceCreate(); // SourceCreate | 
apiInstance.createSource(sourceCreate, (error, data, response) => {
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
 **sourceCreate** | [**SourceCreate**](SourceCreate.md)|  | 

### Return type

[**SourceRead**](SourceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSource

> deleteSource(sourceIdRequestBody)

Delete a source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceIdRequestBody = new AirbyteConfigurationApi.SourceIdRequestBody(); // SourceIdRequestBody | 
apiInstance.deleteSource(sourceIdRequestBody, (error, data, response) => {
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
 **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## discoverSchemaForSource

> SourceDiscoverSchemaRead discoverSchemaForSource(sourceDiscoverSchemaRequestBody)

Discover the schema catalog of the source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceDiscoverSchemaRequestBody = new AirbyteConfigurationApi.SourceDiscoverSchemaRequestBody(); // SourceDiscoverSchemaRequestBody | 
apiInstance.discoverSchemaForSource(sourceDiscoverSchemaRequestBody, (error, data, response) => {
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
 **sourceDiscoverSchemaRequestBody** | [**SourceDiscoverSchemaRequestBody**](SourceDiscoverSchemaRequestBody.md)|  | 

### Return type

[**SourceDiscoverSchemaRead**](SourceDiscoverSchemaRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMostRecentSourceActorCatalog

> ActorCatalogWithUpdatedAt getMostRecentSourceActorCatalog(sourceIdRequestBody)

Get most recent ActorCatalog for source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceIdRequestBody = new AirbyteConfigurationApi.SourceIdRequestBody(); // SourceIdRequestBody | 
apiInstance.getMostRecentSourceActorCatalog(sourceIdRequestBody, (error, data, response) => {
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
 **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | 

### Return type

[**ActorCatalogWithUpdatedAt**](ActorCatalogWithUpdatedAt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSource

> SourceRead getSource(sourceIdRequestBody)

Get source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceIdRequestBody = new AirbyteConfigurationApi.SourceIdRequestBody(); // SourceIdRequestBody | 
apiInstance.getSource(sourceIdRequestBody, (error, data, response) => {
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
 **sourceIdRequestBody** | [**SourceIdRequestBody**](SourceIdRequestBody.md)|  | 

### Return type

[**SourceRead**](SourceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSourcesForWorkspace

> SourceReadList listSourcesForWorkspace(workspaceIdRequestBody)

List sources for workspace

List sources for workspace. Does not return deleted sources.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let workspaceIdRequestBody = new AirbyteConfigurationApi.WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
apiInstance.listSourcesForWorkspace(workspaceIdRequestBody, (error, data, response) => {
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

[**SourceReadList**](SourceReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchSources

> SourceReadList searchSources(sourceSearch)

Search sources

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceSearch = new AirbyteConfigurationApi.SourceSearch(); // SourceSearch | 
apiInstance.searchSources(sourceSearch, (error, data, response) => {
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
 **sourceSearch** | [**SourceSearch**](SourceSearch.md)|  | 

### Return type

[**SourceReadList**](SourceReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSource

> SourceRead updateSource(sourceUpdate)

Update a source

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceUpdate = new AirbyteConfigurationApi.SourceUpdate(); // SourceUpdate | 
apiInstance.updateSource(sourceUpdate, (error, data, response) => {
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
 **sourceUpdate** | [**SourceUpdate**](SourceUpdate.md)|  | 

### Return type

[**SourceRead**](SourceRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## writeDiscoverCatalogResult

> DiscoverCatalogResult writeDiscoverCatalogResult(sourceDiscoverSchemaWriteRequestBody)

Should only called from worker, to write result from discover activity back to DB.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SourceApi();
let sourceDiscoverSchemaWriteRequestBody = new AirbyteConfigurationApi.SourceDiscoverSchemaWriteRequestBody(); // SourceDiscoverSchemaWriteRequestBody | 
apiInstance.writeDiscoverCatalogResult(sourceDiscoverSchemaWriteRequestBody, (error, data, response) => {
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
 **sourceDiscoverSchemaWriteRequestBody** | [**SourceDiscoverSchemaWriteRequestBody**](SourceDiscoverSchemaWriteRequestBody.md)|  | 

### Return type

[**DiscoverCatalogResult**](DiscoverCatalogResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

