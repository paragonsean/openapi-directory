# AgcoApi.ReportingApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportingBundleStatusSummary**](ReportingApi.md#reportingBundleStatusSummary) | **GET** /api/v2/Reporting/BundleStatusSummary | Get a summary of all Packages in a Bundle
[**reportingBundlesInUpdateGroup**](ReportingApi.md#reportingBundlesInUpdateGroup) | **GET** /api/v2/Reporting/BundlesInUpdateGroup | Get a list of bundles for UpdateGroup.
[**reportingClientInfo**](ReportingApi.md#reportingClientInfo) | **GET** /api/v2/Reporting/ClientInfo | Get Client Information
[**reportingCurrentPackagesInUpdateGroup**](ReportingApi.md#reportingCurrentPackagesInUpdateGroup) | **GET** /api/v2/Reporting/CurrentPackagesInUpdateGroup | Get the current packages for an update group.
[**reportingGetClient**](ReportingApi.md#reportingGetClient) | **GET** /api/v2/Reporting/GetClient | Get a Client in the Update System.
[**reportingGetSubscriptions**](ReportingApi.md#reportingGetSubscriptions) | **GET** /api/v2/Reporting/GetSubscriptions | Get a list of current Client Subscriptions.
[**reportingPackageStatusSummary**](ReportingApi.md#reportingPackageStatusSummary) | **GET** /api/v2/Reporting/PackageStatusSummary | Get a summary report for a Specific Package
[**reportingRegisteredClients**](ReportingApi.md#reportingRegisteredClients) | **GET** /api/v2/Reporting/RegisteredClients | Get a list of subscribed clients
[**reportingUpdateGroups**](ReportingApi.md#reportingUpdateGroups) | **GET** /api/v2/Reporting/UpdateGroups | Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.
[**reportingUpdateMetrics**](ReportingApi.md#reportingUpdateMetrics) | **GET** /api/v2/Reporting/UpdateMetrics | Get data for pie charts in UpdateMetrics.



## reportingBundleStatusSummary

> APIPagedResponseUpdateSystemModelsPackageStatusSummary reportingBundleStatusSummary(bundleID, opts)

Get a summary of all Packages in a Bundle

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let bundleID = "bundleID_example"; // String | The BundleID
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.reportingBundleStatusSummary(bundleID, opts, (error, data, response) => {
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
 **bundleID** | **String**| The BundleID | 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsPackageStatusSummary**](APIPagedResponseUpdateSystemModelsPackageStatusSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## reportingBundlesInUpdateGroup

> APIPagedResponseUpdateSystemModelsBundle reportingBundlesInUpdateGroup(ID, includeInactive, opts)

Get a list of bundles for UpdateGroup.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let ID = "ID_example"; // String | The UpdateGroupID
let includeInactive = true; // Boolean | Include Inactive Bundles (true|false)
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.reportingBundlesInUpdateGroup(ID, includeInactive, opts, (error, data, response) => {
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
 **ID** | **String**| The UpdateGroupID | 
 **includeInactive** | **Boolean**| Include Inactive Bundles (true|false) | 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsBundle**](APIPagedResponseUpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## reportingClientInfo

> UpdateSystemModelsClientInfo reportingClientInfo(clientID)

Get Client Information

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let clientID = "clientID_example"; // String | The Client ID
apiInstance.reportingClientInfo(clientID, (error, data, response) => {
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
 **clientID** | **String**| The Client ID | 

### Return type

[**UpdateSystemModelsClientInfo**](UpdateSystemModelsClientInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reportingCurrentPackagesInUpdateGroup

> [UpdateSystemModelsPackage] reportingCurrentPackagesInUpdateGroup(ID, opts)

Get the current packages for an update group.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let ID = "ID_example"; // String | The UpdateGroupID
let opts = {
  'subscriptionTypeFilter': "subscriptionTypeFilter_example" // String | Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.
};
apiInstance.reportingCurrentPackagesInUpdateGroup(ID, opts, (error, data, response) => {
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
 **ID** | **String**| The UpdateGroupID | 
 **subscriptionTypeFilter** | **String**| Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned. | [optional] 

### Return type

[**[UpdateSystemModelsPackage]**](UpdateSystemModelsPackage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reportingGetClient

> UpdateSystemModelsClient reportingGetClient(ID)

Get a Client in the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let ID = "ID_example"; // String | The Client ID
apiInstance.reportingGetClient(ID, (error, data, response) => {
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
 **ID** | **String**| The Client ID | 

### Return type

[**UpdateSystemModelsClient**](UpdateSystemModelsClient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reportingGetSubscriptions

> APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship reportingGetSubscriptions(opts)

Get a list of current Client Subscriptions.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let opts = {
  'clientID': "clientID_example", // String | Optional. Filter by Client ID
  'updateGroupID': "updateGroupID_example", // String | Optional. Filter by Update Group ID
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.reportingGetSubscriptions(opts, (error, data, response) => {
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
 **clientID** | **String**| Optional. Filter by Client ID | [optional] 
 **updateGroupID** | **String**| Optional. Filter by Update Group ID | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship**](APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## reportingPackageStatusSummary

> UpdateSystemModelsPackageStatusSummary reportingPackageStatusSummary(packageID)

Get a summary report for a Specific Package

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let packageID = "packageID_example"; // String | The Package ID
apiInstance.reportingPackageStatusSummary(packageID, (error, data, response) => {
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
 **packageID** | **String**| The Package ID | 

### Return type

[**UpdateSystemModelsPackageStatusSummary**](UpdateSystemModelsPackageStatusSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## reportingRegisteredClients

> APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata reportingRegisteredClients(opts)

Get a list of subscribed clients

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let opts = {
  'updateGroupID': "updateGroupID_example", // String | Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.
  'clientID': "clientID_example", // String | Optional. Filter where ClientID matches a value. Wildcards are supported (*).
  'tag': "tag_example", // String | Optional. Filter where Tag matches a value. Wildcards are supported (*).
  'reportResult': "reportResult_example", // String | Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).
  'reportResultIsValid': true, // Boolean | Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.
  'reportValue': "reportValue_example", // String | Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).
  'lastCheckInBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter where LastCheckIn occured before the provided date.
  'lastCheckInAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Filter where LastCheckIn occured after the provided date.
  'orderBy': "orderBy_example", // String | Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...                 If sort direction is not provided for a field, it will be sorted ascending.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.reportingRegisteredClients(opts, (error, data, response) => {
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
 **updateGroupID** | **String**| Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned. | [optional] 
 **clientID** | **String**| Optional. Filter where ClientID matches a value. Wildcards are supported (*). | [optional] 
 **tag** | **String**| Optional. Filter where Tag matches a value. Wildcards are supported (*). | [optional] 
 **reportResult** | **String**| Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*). | [optional] 
 **reportResultIsValid** | **Boolean**| Optional and UpdateGroupID must be included. When &#39;true&#39; filters results where ReportResult equals ReportResultExpected.  When &#39;false&#39; filters results where ValueToValidate does not equal ReportResults. | [optional] 
 **reportValue** | **String**| Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*). | [optional] 
 **lastCheckInBefore** | **Date**| Optional. Filter where LastCheckIn occured before the provided date. | [optional] 
 **lastCheckInAfter** | **Date**| Optional. Filter where LastCheckIn occured after the provided date. | [optional] 
 **orderBy** | **String**| Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...                 If sort direction is not provided for a field, it will be sorted ascending. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata**](APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## reportingUpdateGroups

> APIPagedResponseUpdateSystemModelsUpdateGroup reportingUpdateGroups(opts)

Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.reportingUpdateGroups(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroup**](APIPagedResponseUpdateSystemModelsUpdateGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## reportingUpdateMetrics

> UpdateSystemModelsUpdateMetricsData reportingUpdateMetrics(updateGroupID, opts)

Get data for pie charts in UpdateMetrics.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ReportingApi();
let updateGroupID = "updateGroupID_example"; // String | The UpdateType in which clients must be for the report to include them.
let opts = {
  'bundleNumber': 56 // Number | Optional. Tells us which chart to show based upon filter.
};
apiInstance.reportingUpdateMetrics(updateGroupID, opts, (error, data, response) => {
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
 **updateGroupID** | **String**| The UpdateType in which clients must be for the report to include them. | 
 **bundleNumber** | **Number**| Optional. Tells us which chart to show based upon filter. | [optional] 

### Return type

[**UpdateSystemModelsUpdateMetricsData**](UpdateSystemModelsUpdateMetricsData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

