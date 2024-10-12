# AirbyteConfigurationApi.LogsApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLogs**](LogsApi.md#getLogs) | **POST** /v1/logs/get | Get logs



## getLogs

> File getLogs(logsRequestBody)

Get logs

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.LogsApi();
let logsRequestBody = new AirbyteConfigurationApi.LogsRequestBody(); // LogsRequestBody | 
apiInstance.getLogs(logsRequestBody, (error, data, response) => {
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
 **logsRequestBody** | [**LogsRequestBody**](LogsRequestBody.md)|  | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain, application/json

