# AirbyteConfigurationApi.DestinationApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkConnectionToDestination**](DestinationApi.md#checkConnectionToDestination) | **POST** /v1/destinations/check_connection | Check connection to the destination
[**checkConnectionToDestinationForUpdate**](DestinationApi.md#checkConnectionToDestinationForUpdate) | **POST** /v1/destinations/check_connection_for_update | Check connection for a proposed update to a destination
[**cloneDestination**](DestinationApi.md#cloneDestination) | **POST** /v1/destinations/clone | Clone destination
[**createDestination**](DestinationApi.md#createDestination) | **POST** /v1/destinations/create | Create a destination
[**deleteDestination**](DestinationApi.md#deleteDestination) | **POST** /v1/destinations/delete | Delete the destination
[**getDestination**](DestinationApi.md#getDestination) | **POST** /v1/destinations/get | Get configured destination
[**listDestinationsForWorkspace**](DestinationApi.md#listDestinationsForWorkspace) | **POST** /v1/destinations/list | List configured destinations for a workspace
[**searchDestinations**](DestinationApi.md#searchDestinations) | **POST** /v1/destinations/search | Search destinations
[**updateDestination**](DestinationApi.md#updateDestination) | **POST** /v1/destinations/update | Update a destination



## checkConnectionToDestination

> CheckConnectionRead checkConnectionToDestination(destinationIdRequestBody)

Check connection to the destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationIdRequestBody = new AirbyteConfigurationApi.DestinationIdRequestBody(); // DestinationIdRequestBody | 
apiInstance.checkConnectionToDestination(destinationIdRequestBody, (error, data, response) => {
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
 **destinationIdRequestBody** | [**DestinationIdRequestBody**](DestinationIdRequestBody.md)|  | 

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkConnectionToDestinationForUpdate

> CheckConnectionRead checkConnectionToDestinationForUpdate(destinationUpdate)

Check connection for a proposed update to a destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationUpdate = new AirbyteConfigurationApi.DestinationUpdate(); // DestinationUpdate | 
apiInstance.checkConnectionToDestinationForUpdate(destinationUpdate, (error, data, response) => {
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
 **destinationUpdate** | [**DestinationUpdate**](DestinationUpdate.md)|  | 

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloneDestination

> DestinationRead cloneDestination(destinationCloneRequestBody)

Clone destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationCloneRequestBody = new AirbyteConfigurationApi.DestinationCloneRequestBody(); // DestinationCloneRequestBody | 
apiInstance.cloneDestination(destinationCloneRequestBody, (error, data, response) => {
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
 **destinationCloneRequestBody** | [**DestinationCloneRequestBody**](DestinationCloneRequestBody.md)|  | 

### Return type

[**DestinationRead**](DestinationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDestination

> DestinationRead createDestination(destinationCreate)

Create a destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationCreate = new AirbyteConfigurationApi.DestinationCreate(); // DestinationCreate | 
apiInstance.createDestination(destinationCreate, (error, data, response) => {
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
 **destinationCreate** | [**DestinationCreate**](DestinationCreate.md)|  | 

### Return type

[**DestinationRead**](DestinationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDestination

> deleteDestination(destinationIdRequestBody)

Delete the destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationIdRequestBody = new AirbyteConfigurationApi.DestinationIdRequestBody(); // DestinationIdRequestBody | 
apiInstance.deleteDestination(destinationIdRequestBody, (error, data, response) => {
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
 **destinationIdRequestBody** | [**DestinationIdRequestBody**](DestinationIdRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDestination

> DestinationRead getDestination(destinationIdRequestBody)

Get configured destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationIdRequestBody = new AirbyteConfigurationApi.DestinationIdRequestBody(); // DestinationIdRequestBody | 
apiInstance.getDestination(destinationIdRequestBody, (error, data, response) => {
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
 **destinationIdRequestBody** | [**DestinationIdRequestBody**](DestinationIdRequestBody.md)|  | 

### Return type

[**DestinationRead**](DestinationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDestinationsForWorkspace

> DestinationReadList listDestinationsForWorkspace(workspaceIdRequestBody)

List configured destinations for a workspace

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let workspaceIdRequestBody = new AirbyteConfigurationApi.WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
apiInstance.listDestinationsForWorkspace(workspaceIdRequestBody, (error, data, response) => {
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

[**DestinationReadList**](DestinationReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchDestinations

> DestinationReadList searchDestinations(destinationSearch)

Search destinations

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationSearch = new AirbyteConfigurationApi.DestinationSearch(); // DestinationSearch | 
apiInstance.searchDestinations(destinationSearch, (error, data, response) => {
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
 **destinationSearch** | [**DestinationSearch**](DestinationSearch.md)|  | 

### Return type

[**DestinationReadList**](DestinationReadList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDestination

> DestinationRead updateDestination(destinationUpdate)

Update a destination

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.DestinationApi();
let destinationUpdate = new AirbyteConfigurationApi.DestinationUpdate(); // DestinationUpdate | 
apiInstance.updateDestination(destinationUpdate, (error, data, response) => {
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
 **destinationUpdate** | [**DestinationUpdate**](DestinationUpdate.md)|  | 

### Return type

[**DestinationRead**](DestinationRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

