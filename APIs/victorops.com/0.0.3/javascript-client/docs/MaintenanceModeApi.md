# VictorOps.MaintenanceModeApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1MaintenancemodeGet**](MaintenanceModeApi.md#apiPublicV1MaintenancemodeGet) | **GET** /api-public/v1/maintenancemode | Get an organization&#39;s current maintenance mode state
[**apiPublicV1MaintenancemodeMaintenancemodeidEndPut**](MaintenanceModeApi.md#apiPublicV1MaintenancemodeMaintenancemodeidEndPut) | **PUT** /api-public/v1/maintenancemode/{maintenancemodeid}/end | End maintenance mode for routing keys
[**apiPublicV1MaintenancemodeStartPost**](MaintenanceModeApi.md#apiPublicV1MaintenancemodeStartPost) | **POST** /api-public/v1/maintenancemode/start | Start maintenance mode for routing keys



## apiPublicV1MaintenancemodeGet

> MaintenanceModeState apiPublicV1MaintenancemodeGet(xVOApiId, xVOApiKey)

Get an organization&#39;s current maintenance mode state

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.MaintenanceModeApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1MaintenancemodeGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**MaintenanceModeState**](MaintenanceModeState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1MaintenancemodeMaintenancemodeidEndPut

> MaintenanceModeState apiPublicV1MaintenancemodeMaintenancemodeidEndPut(xVOApiId, xVOApiKey, maintenancemodeid)

End maintenance mode for routing keys

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.MaintenanceModeApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let maintenancemodeid = "maintenancemodeid_example"; // String | The id of the maintenance mode found in the active maintenance mode object
apiInstance.apiPublicV1MaintenancemodeMaintenancemodeidEndPut(xVOApiId, xVOApiKey, maintenancemodeid, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **maintenancemodeid** | **String**| The id of the maintenance mode found in the active maintenance mode object | 

### Return type

[**MaintenanceModeState**](MaintenanceModeState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1MaintenancemodeStartPost

> MaintenanceModeState apiPublicV1MaintenancemodeStartPost(xVOApiId, xVOApiKey, body)

Start maintenance mode for routing keys

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.MaintenanceModeApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.ApiPublicV1MaintenancemodeStartPostRequest(); // ApiPublicV1MaintenancemodeStartPostRequest | the definition of the maintenance mode you want to start
apiInstance.apiPublicV1MaintenancemodeStartPost(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**ApiPublicV1MaintenancemodeStartPostRequest**](ApiPublicV1MaintenancemodeStartPostRequest.md)| the definition of the maintenance mode you want to start | 

### Return type

[**MaintenanceModeState**](MaintenanceModeState.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

