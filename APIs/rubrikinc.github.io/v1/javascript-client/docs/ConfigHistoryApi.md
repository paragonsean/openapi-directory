# RubrikRestApi.ConfigHistoryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryConfigurationHistoryUpdates**](ConfigHistoryApi.md#queryConfigurationHistoryUpdates) | **GET** /config/history/list_updates | View a list of filtered configuration updates
[**retrieveConfigurationValues**](ConfigHistoryApi.md#retrieveConfigurationValues) | **GET** /config/history/ondate | View a list of configurations and their values on a given date



## queryConfigurationHistoryUpdates

> ConfigurationUpdateSummaryListResponse queryConfigurationHistoryUpdates(opts)

View a list of filtered configuration updates

View a list of cluster configuration options that have updated within a specified time window.

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

let apiInstance = new RubrikRestApi.ConfigHistoryApi();
let opts = {
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'apiUser': "apiUser_example", // String | The username of the account. Applies a filter to the configuration updates performed by the specified username.
  'nodeId': "nodeId_example", // String | The node ID. Applies a filter to the configuration updates for the specified node. When no node_id is specified, the filter shows both local and cluster-wide configurations. Specify 'cluster' for filtering out cluster-wide configuration updates.
  'namespace': "namespace_example", // String | The configuration namespace. Applies a filter to the configuration updates for the specified namespace.
  'name': "name_example", // String | Name of the configuration. Applies a filter to the configuration updates for the specified configuration name.
  'source': "source_example", // String | Source for configuration updates. Applies a filter to the configuration updates for the specified source.
  'afterTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The earliest time configuration history is needed. Applies a filter that only shows configuration updates after the specified time.
  'beforeTime': new Date("2013-10-20T19:20:30+01:00") // Date | The latest time configuration history is needed. Applies filter to display only configuration updates prior to the specified time. The default value is the current time.
};
apiInstance.queryConfigurationHistoryUpdates(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **apiUser** | **String**| The username of the account. Applies a filter to the configuration updates performed by the specified username. | [optional] 
 **nodeId** | **String**| The node ID. Applies a filter to the configuration updates for the specified node. When no node_id is specified, the filter shows both local and cluster-wide configurations. Specify &#39;cluster&#39; for filtering out cluster-wide configuration updates. | [optional] 
 **namespace** | **String**| The configuration namespace. Applies a filter to the configuration updates for the specified namespace. | [optional] 
 **name** | **String**| Name of the configuration. Applies a filter to the configuration updates for the specified configuration name. | [optional] 
 **source** | **String**| Source for configuration updates. Applies a filter to the configuration updates for the specified source. | [optional] 
 **afterTime** | **Date**| The earliest time configuration history is needed. Applies a filter that only shows configuration updates after the specified time. | [optional] 
 **beforeTime** | **Date**| The latest time configuration history is needed. Applies filter to display only configuration updates prior to the specified time. The default value is the current time. | [optional] 

### Return type

[**ConfigurationUpdateSummaryListResponse**](ConfigurationUpdateSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveConfigurationValues

> ConfigurationSummaryListResponse retrieveConfigurationValues(namespace, onDate, opts)

View a list of configurations and their values on a given date

View a list of configurations and their values on a given date.

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

let apiInstance = new RubrikRestApi.ConfigHistoryApi();
let namespace = "namespace_example"; // String | The configuration namespace. Applies a filter to the configuration updates for the specified namespace.
let onDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The timestamp for which to retrieve configuration values.
let opts = {
  'limit': 56, // Number | Limit the number of matches returned.
  'offset': 56, // Number | Ignore these many matches in the beginning.
  'nodeId': "nodeId_example", // String | The name of the node that require configuration values. Applies a filter specific to the name of node. When no node_id is specified, the filter shows both local and cluster-wide configurations.
  'name': "name_example" // String | The name of the configuration option. Applies a filter to the configuration updates for the specified option.
};
apiInstance.retrieveConfigurationValues(namespace, onDate, opts, (error, data, response) => {
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
 **namespace** | **String**| The configuration namespace. Applies a filter to the configuration updates for the specified namespace. | 
 **onDate** | **Date**| The timestamp for which to retrieve configuration values. | 
 **limit** | **Number**| Limit the number of matches returned. | [optional] 
 **offset** | **Number**| Ignore these many matches in the beginning. | [optional] 
 **nodeId** | **String**| The name of the node that require configuration values. Applies a filter specific to the name of node. When no node_id is specified, the filter shows both local and cluster-wide configurations. | [optional] 
 **name** | **String**| The name of the configuration option. Applies a filter to the configuration updates for the specified option. | [optional] 

### Return type

[**ConfigurationSummaryListResponse**](ConfigurationSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

