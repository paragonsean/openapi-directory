# RubrikRestApi.SlaDomainApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignSlaToDownloadedSnapshots**](SlaDomainApi.md#assignSlaToDownloadedSnapshots) | **POST** /sla_domain/assign_to_downloaded_snapshots | Assign retention SLA Domain to the downloaded snapshots of a single object
[**createSlaDomain**](SlaDomainApi.md#createSlaDomain) | **POST** /sla_domain | Create SLA Domain
[**deleteSlaDomain**](SlaDomainApi.md#deleteSlaDomain) | **DELETE** /sla_domain/{id} | Remove SLA Domain
[**getSlaDomain**](SlaDomainApi.md#getSlaDomain) | **GET** /sla_domain/{id} | Get SLA Domain details
[**patchSlaDomain**](SlaDomainApi.md#patchSlaDomain) | **PATCH** /sla_domain/{id} | Patch SLA Domain
[**querySlaDomain**](SlaDomainApi.md#querySlaDomain) | **GET** /sla_domain | Get list of SLA Domains
[**updateSlaDomain**](SlaDomainApi.md#updateSlaDomain) | **PUT** /sla_domain/{id} | Update SLA Domain



## assignSlaToDownloadedSnapshots

> BatchAsyncRequestStatus assignSlaToDownloadedSnapshots(downloadedSnapshotSlaAssignmentInfo)

Assign retention SLA Domain to the downloaded snapshots of a single object

Assigns an SLA Domain to a list of downloaded snapshots. The SLA Domain manages retention for the snapshots in the downloaded location. The assignment does not affect the retention of the snapshots in other locations.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let downloadedSnapshotSlaAssignmentInfo = new RubrikRestApi.DownloadedSnapshotSlaAssignmentInfo(); // DownloadedSnapshotSlaAssignmentInfo | An object ID and a list of IDs for the downloaded snapshots. The specified SLA Domain manages retention for the downloaded copy of snapshots assigned to the specified IDs.
apiInstance.assignSlaToDownloadedSnapshots(downloadedSnapshotSlaAssignmentInfo, (error, data, response) => {
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
 **downloadedSnapshotSlaAssignmentInfo** | [**DownloadedSnapshotSlaAssignmentInfo**](DownloadedSnapshotSlaAssignmentInfo.md)| An object ID and a list of IDs for the downloaded snapshots. The specified SLA Domain manages retention for the downloaded copy of snapshots assigned to the specified IDs. | 

### Return type

[**BatchAsyncRequestStatus**](BatchAsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSlaDomain

> SlaDomainSummary createSlaDomain(slaDomainDefinition)

Create SLA Domain

Create a new SLA Domain on a Rubrik cluster by specifying Domain Rules and policies. Only Managed Volume objects support minute frequency to take transaction log backup. SLA assignment on other objects will be disallowed.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let slaDomainDefinition = new RubrikRestApi.SlaDomainDefinition(); // SlaDomainDefinition | SLA Domain definition. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using Rubrik cluster timezone.
apiInstance.createSlaDomain(slaDomainDefinition, (error, data, response) => {
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
 **slaDomainDefinition** | [**SlaDomainDefinition**](SlaDomainDefinition.md)| SLA Domain definition. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using Rubrik cluster timezone. | 

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSlaDomain

> deleteSlaDomain(id)

Remove SLA Domain

Delete an SLA Domain from a Rubrik cluster. The SLA Domain must not be assigned to any VMs, filesets or databases.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let id = "id_example"; // String | ID of the SLA Domain.
apiInstance.deleteSlaDomain(id, (error, data, response) => {
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
 **id** | **String**| ID of the SLA Domain. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSlaDomain

> SlaDomainSummary getSlaDomain(id)

Get SLA Domain details

Retrieve summary information for a specified SLA Domain.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let id = "id_example"; // String | ID of the SLA Domain.
apiInstance.getSlaDomain(id, (error, data, response) => {
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
 **id** | **String**| ID of the SLA Domain. | 

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSlaDomain

> SlaDomainSummary patchSlaDomain(id, slaDomainPatchDefinition, opts)

Patch SLA Domain

(DEPRECATED) Patch the properties of an SLA Domain. The recommended endpoint is v3/sla_domain/{id}.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let id = "id_example"; // String | ID of the SLA Domain.
let slaDomainPatchDefinition = new RubrikRestApi.SlaDomainPatchDefinition(); // SlaDomainPatchDefinition | Object containing the fields to be edited for SLA Domain. The SLA Domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using the Rubrik cluster timezone. Remote SLA Domain only supports edit to the archival specification.
let opts = {
  'shouldApplyToExistingSnapshots': true // Boolean | A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is 'true' by default.
};
apiInstance.patchSlaDomain(id, slaDomainPatchDefinition, opts, (error, data, response) => {
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
 **id** | **String**| ID of the SLA Domain. | 
 **slaDomainPatchDefinition** | [**SlaDomainPatchDefinition**](SlaDomainPatchDefinition.md)| Object containing the fields to be edited for SLA Domain. The SLA Domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snapshot. Specify times using the Rubrik cluster timezone. Remote SLA Domain only supports edit to the archival specification. | 
 **shouldApplyToExistingSnapshots** | **Boolean**| A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is &#39;true&#39; by default. | [optional] 

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## querySlaDomain

> SlaDomainSummaryListResponse querySlaDomain(opts)

Get list of SLA Domains

Retrieve summary information for all SLA Domains.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | Limits the information retrieved to those SLA Domains that are associated with the Rubrik cluster ID that is specified by primary_cluster_id. Use **local** for the Rubrik cluster that is hosting the current REST API session.
  'name': "name_example", // String | Limit the list information to those SLA Domains which match the specified SLA Domain 'name' value.
  'sortBy': "sortBy_example", // String | Attribute to use to sort the SLA Domains summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order.
  'sortOrder': "sortOrder_example", // String | Sort order, either ascending or descending. If not specified, SLA Domain summary results will be sorted in ascending order.
  'dataSources': ["null"], // [String] | Limit the list information to SLA Domains that can be assigned to specified data sources.
  'snapshotIds': ["null"] // [String] | Limit the list information to SLA Domains that can be assigned to specified snapshots.
};
apiInstance.querySlaDomain(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| Limits the information retrieved to those SLA Domains that are associated with the Rubrik cluster ID that is specified by primary_cluster_id. Use **local** for the Rubrik cluster that is hosting the current REST API session. | [optional] 
 **name** | **String**| Limit the list information to those SLA Domains which match the specified SLA Domain &#39;name&#39; value. | [optional] 
 **sortBy** | **String**| Attribute to use to sort the SLA Domains summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. If not specified, SLA Domain summary results will be sorted in ascending order. | [optional] 
 **dataSources** | [**[String]**](String.md)| Limit the list information to SLA Domains that can be assigned to specified data sources. | [optional] 
 **snapshotIds** | [**[String]**](String.md)| Limit the list information to SLA Domains that can be assigned to specified snapshots. | [optional] 

### Return type

[**SlaDomainSummaryListResponse**](SlaDomainSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSlaDomain

> SlaDomainSummary updateSlaDomain(id, slaDomainDefinition, opts)

Update SLA Domain

Update the properties of an SLA Domain.

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

let apiInstance = new RubrikRestApi.SlaDomainApi();
let id = "id_example"; // String | ID of the SLA Domain.
let slaDomainDefinition = new RubrikRestApi.SlaDomainDefinition(); // SlaDomainDefinition | Object containing the updated SLA Domain. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snpashot. Specify times using the Rubrik cluster time zone.
let opts = {
  'shouldApplyToExistingSnapshots': true // Boolean | A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is 'true' by default.
};
apiInstance.updateSlaDomain(id, slaDomainDefinition, opts, (error, data, response) => {
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
 **id** | **String**| ID of the SLA Domain. | 
 **slaDomainDefinition** | [**SlaDomainDefinition**](SlaDomainDefinition.md)| Object containing the updated SLA Domain. The SLA domain accepts two backup windows, one for a regular backup or snapshot and one for the first full backup or snpashot. Specify times using the Rubrik cluster time zone. | 
 **shouldApplyToExistingSnapshots** | **Boolean**| A Boolean that determines whether the new configuration retains existing snapshots of data sources that are currently retained by this SLA Domain. The value is &#39;true&#39; by default. | [optional] 

### Return type

[**SlaDomainSummary**](SlaDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

