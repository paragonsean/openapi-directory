# TurbineLabsApi.AuditLogApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changelogAdhocGet**](AuditLogApi.md#changelogAdhocGet) | **GET** /changelog/adhoc | Allows an arbitrary filter to be specified and applied to the org\\&#39;s change log.
[**changelogClusterGraphClusterKeyGet**](AuditLogApi.md#changelogClusterGraphClusterKeyGet) | **GET** /changelog/cluster-graph/{clusterKey} | get changes related to the indicated cluster
[**changelogDomainGraphDomainKeyGet**](AuditLogApi.md#changelogDomainGraphDomainKeyGet) | **GET** /changelog/domain-graph/{domainKey} | get changes related to the indicated domain
[**changelogRouteGraphRouteKeyGet**](AuditLogApi.md#changelogRouteGraphRouteKeyGet) | **GET** /changelog/route-graph/{routeKey} | get changes related to the indicated route
[**changelogSharedRulesGraphSharedRulesKeyGet**](AuditLogApi.md#changelogSharedRulesGraphSharedRulesKeyGet) | **GET** /changelog/shared-rules-graph/{sharedRulesKey} | get changes related to the indicated SharedRules
[**changelogZoneZoneKeyGet**](AuditLogApi.md#changelogZoneZoneKeyGet) | **GET** /changelog/zone/{zoneKey} | get changes in a specified zone



## changelogAdhocGet

> PaginatedChangeDescriptions changelogAdhocGet(opts)

Allows an arbitrary filter to be specified and applied to the org\\&#39;s change log.

Perform an adhoc query against the change log for your org. The filter is a JSON encoded FilterSum as defined in this file.

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.AuditLogApi();
let opts = {
  'filter': "filter_example" // String | Encoded FilterSums representing the query you would like to execute. See object definition for details.
};
apiInstance.changelogAdhocGet(opts, (error, data, response) => {
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
 **filter** | **String**| Encoded FilterSums representing the query you would like to execute. See object definition for details. | [optional] 

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changelogClusterGraphClusterKeyGet

> PaginatedChangeDescriptions changelogClusterGraphClusterKeyGet(clusterKey, opts)

get changes related to the indicated cluster

Gets all changes to a cluster. 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.AuditLogApi();
let clusterKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the cluster key to see an audit log for
let opts = {
  'start': 3.4, // Number | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'end': 3.4, // Number | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'maxResults': 3.4, // Number | Determines how many ChangeDescription object should be returned to the calling code. 
  'refId': "refId_example", // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
  'direction': "direction_example" // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
};
apiInstance.changelogClusterGraphClusterKeyGet(clusterKey, opts, (error, data, response) => {
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
 **clusterKey** | **String**| the cluster key to see an audit log for | 
 **start** | **Number**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **end** | **Number**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **maxResults** | **Number**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] 
 **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] 
 **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] 

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changelogDomainGraphDomainKeyGet

> PaginatedChangeDescriptions changelogDomainGraphDomainKeyGet(domainKey, opts)

get changes related to the indicated domain

Gets all changes to a domain, the proxies that front the specified domain, routes within that domain, the shared rules of each route, the clusters connected via route or shared rules. 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.AuditLogApi();
let domainKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the domain key to see an audit log for
let opts = {
  'start': 3.4, // Number | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'end': 3.4, // Number | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'maxResults': 3.4, // Number | Determines how many ChangeDescription object should be returned to the calling code. 
  'refId': "refId_example", // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
  'direction': "direction_example" // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
};
apiInstance.changelogDomainGraphDomainKeyGet(domainKey, opts, (error, data, response) => {
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
 **domainKey** | **String**| the domain key to see an audit log for | 
 **start** | **Number**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **end** | **Number**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **maxResults** | **Number**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] 
 **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] 
 **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] 

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changelogRouteGraphRouteKeyGet

> PaginatedChangeDescriptions changelogRouteGraphRouteKeyGet(routeKey, opts)

get changes related to the indicated route

Gets all changes to a route, the domains associated with it, the shared rules it references, and the clusters connected to it. 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.AuditLogApi();
let routeKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the route key to see an audit log for
let opts = {
  'start': 3.4, // Number | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'end': 3.4, // Number | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'maxResults': 3.4, // Number | Determines how many ChangeDescription object should be returned to the calling code. 
  'refId': "refId_example", // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
  'direction': "direction_example" // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
};
apiInstance.changelogRouteGraphRouteKeyGet(routeKey, opts, (error, data, response) => {
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
 **routeKey** | **String**| the route key to see an audit log for | 
 **start** | **Number**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **end** | **Number**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **maxResults** | **Number**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] 
 **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] 
 **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] 

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changelogSharedRulesGraphSharedRulesKeyGet

> PaginatedChangeDescriptions changelogSharedRulesGraphSharedRulesKeyGet(sharedRulesKey, opts)

get changes related to the indicated SharedRules

Gets all changes associated with set of Shared Rules; the domains using it and the clusters referenced by it. 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.AuditLogApi();
let sharedRulesKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the shared rules key to see an audit log for
let opts = {
  'start': 3.4, // Number | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'end': 3.4, // Number | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'maxResults': 3.4, // Number | Determines how many ChangeDescription object should be returned to the calling code. 
  'refId': "refId_example", // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
  'direction': "direction_example" // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
};
apiInstance.changelogSharedRulesGraphSharedRulesKeyGet(sharedRulesKey, opts, (error, data, response) => {
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
 **sharedRulesKey** | **String**| the shared rules key to see an audit log for | 
 **start** | **Number**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **end** | **Number**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **maxResults** | **Number**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] 
 **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] 
 **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] 

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changelogZoneZoneKeyGet

> PaginatedChangeDescriptions changelogZoneZoneKeyGet(zoneKey, opts)

get changes in a specified zone

Retrieve all changes in the specified zone.

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.AuditLogApi();
let zoneKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the zone key to see an audit log for
let opts = {
  'start': 3.4, // Number | The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'end': 3.4, // Number | The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
  'maxResults': 3.4, // Number | Determines how many ChangeDescription object should be returned to the calling code. 
  'refId': "refId_example", // String | When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
  'direction': "direction_example" // String | If set to \"before\" then changes will be returned that occurred before reference ID. If \"after\" then changes will be returned that have occurred since the reference ID. 
};
apiInstance.changelogZoneZoneKeyGet(zoneKey, opts, (error, data, response) => {
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
 **zoneKey** | **String**| the zone key to see an audit log for | 
 **start** | **Number**| The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **end** | **Number**| The end of the window we want to see changes for; measured in microseconds since Unix Epoch.  | [optional] 
 **maxResults** | **Number**| Determines how many ChangeDescription object should be returned to the calling code.  | [optional] 
 **refId** | **String**| When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument).  | [optional] 
 **direction** | **String**| If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID.  | [optional] 

### Return type

[**PaginatedChangeDescriptions**](PaginatedChangeDescriptions.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

