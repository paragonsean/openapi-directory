# AirbyteConfigurationApi.StateApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createOrUpdateState**](StateApi.md#createOrUpdateState) | **POST** /v1/state/create_or_update | Create or update the state for a connection.
[**getState**](StateApi.md#getState) | **POST** /v1/state/get | Fetch the current state for a connection.



## createOrUpdateState

> ConnectionState createOrUpdateState(connectionStateCreateOrUpdate)

Create or update the state for a connection.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.StateApi();
let connectionStateCreateOrUpdate = new AirbyteConfigurationApi.ConnectionStateCreateOrUpdate(); // ConnectionStateCreateOrUpdate | 
apiInstance.createOrUpdateState(connectionStateCreateOrUpdate, (error, data, response) => {
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
 **connectionStateCreateOrUpdate** | [**ConnectionStateCreateOrUpdate**](ConnectionStateCreateOrUpdate.md)|  | 

### Return type

[**ConnectionState**](ConnectionState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getState

> ConnectionState getState(connectionIdRequestBody)

Fetch the current state for a connection.

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.StateApi();
let connectionIdRequestBody = new AirbyteConfigurationApi.ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
apiInstance.getState(connectionIdRequestBody, (error, data, response) => {
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

[**ConnectionState**](ConnectionState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

