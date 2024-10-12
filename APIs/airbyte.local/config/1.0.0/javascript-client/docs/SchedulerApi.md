# AirbyteConfigurationApi.SchedulerApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**executeDestinationCheckConnection**](SchedulerApi.md#executeDestinationCheckConnection) | **POST** /v1/scheduler/destinations/check_connection | Run check connection for a given destination configuration
[**executeSourceCheckConnection**](SchedulerApi.md#executeSourceCheckConnection) | **POST** /v1/scheduler/sources/check_connection | Run check connection for a given source configuration
[**executeSourceDiscoverSchema**](SchedulerApi.md#executeSourceDiscoverSchema) | **POST** /v1/scheduler/sources/discover_schema | Run discover schema for a given source a source configuration



## executeDestinationCheckConnection

> CheckConnectionRead executeDestinationCheckConnection(destinationCoreConfig)

Run check connection for a given destination configuration

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SchedulerApi();
let destinationCoreConfig = new AirbyteConfigurationApi.DestinationCoreConfig(); // DestinationCoreConfig | 
apiInstance.executeDestinationCheckConnection(destinationCoreConfig, (error, data, response) => {
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
 **destinationCoreConfig** | [**DestinationCoreConfig**](DestinationCoreConfig.md)|  | 

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## executeSourceCheckConnection

> CheckConnectionRead executeSourceCheckConnection(sourceCoreConfig)

Run check connection for a given source configuration

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SchedulerApi();
let sourceCoreConfig = new AirbyteConfigurationApi.SourceCoreConfig(); // SourceCoreConfig | 
apiInstance.executeSourceCheckConnection(sourceCoreConfig, (error, data, response) => {
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
 **sourceCoreConfig** | [**SourceCoreConfig**](SourceCoreConfig.md)|  | 

### Return type

[**CheckConnectionRead**](CheckConnectionRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## executeSourceDiscoverSchema

> SourceDiscoverSchemaRead executeSourceDiscoverSchema(sourceCoreConfig)

Run discover schema for a given source a source configuration

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.SchedulerApi();
let sourceCoreConfig = new AirbyteConfigurationApi.SourceCoreConfig(); // SourceCoreConfig | 
apiInstance.executeSourceDiscoverSchema(sourceCoreConfig, (error, data, response) => {
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
 **sourceCoreConfig** | [**SourceCoreConfig**](SourceCoreConfig.md)|  | 

### Return type

[**SourceDiscoverSchemaRead**](SourceDiscoverSchemaRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

