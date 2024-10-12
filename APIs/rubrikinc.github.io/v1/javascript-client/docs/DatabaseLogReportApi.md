# RubrikRestApi.DatabaseLogReportApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryLogReport**](DatabaseLogReportApi.md#queryLogReport) | **GET** /database/log_report | Get the database log backup delay information
[**queryReportProperties**](DatabaseLogReportApi.md#queryReportProperties) | **GET** /database/log_report/defaults | Get the database log backup report properties
[**updateReportProperties**](DatabaseLogReportApi.md#updateReportProperties) | **PATCH** /database/log_report/defaults | Update the database log backup report properties



## queryLogReport

> DbLogReportSummaryListResponse queryLogReport(opts)

Get the database log backup delay information

Get the database log backup delay information.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.DatabaseLogReportApi();
let opts = {
  'effectiveSlaDomainId': "effectiveSlaDomainId_example", // String | Filter by effective SLA domain.
  'name': "name_example", // String | Filter by the database name substring.
  'databaseType': "databaseType_example", // String | Filter by the database type.
  'location': "location_example", // String | Filter by the database location.
  'logBackupDelay': 56, // Number | Filter by the database log backup delay in seconds, greater than this value.
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Integer specifying the number of initial matches to ignore.
  'sortBy': "sortBy_example", // String | Specifies the attribute to use while sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.queryLogReport(opts, (error, data, response) => {
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
 **effectiveSlaDomainId** | **String**| Filter by effective SLA domain. | [optional] 
 **name** | **String**| Filter by the database name substring. | [optional] 
 **databaseType** | **String**| Filter by the database type. | [optional] 
 **location** | **String**| Filter by the database location. | [optional] 
 **logBackupDelay** | **Number**| Filter by the database log backup delay in seconds, greater than this value. | [optional] 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Integer specifying the number of initial matches to ignore. | [optional] 
 **sortBy** | **String**| Specifies the attribute to use while sorting the summary information. Performs an ASCII sort using the specified attribute, in the order specified by sort_order. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**DbLogReportSummaryListResponse**](DbLogReportSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryReportProperties

> DbLogReportProperties queryReportProperties()

Get the database log backup report properties

Get the properties for the database (SQL and Oracle) log backup delay email notification creation. The properties are logDelayThresholdInMin and logDelayNotificationFrequencyInMin.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.DatabaseLogReportApi();
apiInstance.queryReportProperties((error, data, response) => {
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

[**DbLogReportProperties**](DbLogReportProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateReportProperties

> DbLogReportProperties updateReportProperties(dbLogReportPropertiesUpdate)

Update the database log backup report properties

Update the properties for the database (SQL and Oracle) log backup delay email notification creation. The properties are logDelayThresholdInMin and logDelayNotificationFrequencyInMin.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.DatabaseLogReportApi();
let dbLogReportPropertiesUpdate = new RubrikRestApi.DbLogReportPropertiesUpdate(); // DbLogReportPropertiesUpdate | Updated report properties.
apiInstance.updateReportProperties(dbLogReportPropertiesUpdate, (error, data, response) => {
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
 **dbLogReportPropertiesUpdate** | [**DbLogReportPropertiesUpdate**](DbLogReportPropertiesUpdate.md)| Updated report properties. | 

### Return type

[**DbLogReportProperties**](DbLogReportProperties.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

