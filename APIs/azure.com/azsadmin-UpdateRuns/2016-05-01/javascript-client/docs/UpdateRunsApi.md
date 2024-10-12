# UpdateAdminClient.UpdateRunsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateRunsGet**](UpdateRunsApi.md#updateRunsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updates/{updateName}/updateRuns/{runName} | 
[**updateRunsGetTopLevel**](UpdateRunsApi.md#updateRunsGetTopLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updateRuns/{runName} | 
[**updateRunsList**](UpdateRunsApi.md#updateRunsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updates/{updateName}/updateRuns | 
[**updateRunsListTopLevel**](UpdateRunsApi.md#updateRunsListTopLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updateRuns | 
[**updateRunsRerun**](UpdateRunsApi.md#updateRunsRerun) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation}/updates/{updateName}/updateRuns/{runName}/rerun | 



## updateRunsGet

> UpdateRun updateRunsGet(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion)



Get an instance of update run using the ID.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateRunsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let updateLocation = "updateLocation_example"; // String | The name of the update location.
let updateName = "updateName_example"; // String | Name of the update.
let runName = "runName_example"; // String | Update run identifier.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateRunsGet(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **updateLocation** | **String**| The name of the update location. | 
 **updateName** | **String**| Name of the update. | 
 **runName** | **String**| Update run identifier. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**UpdateRun**](UpdateRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRunsGetTopLevel

> UpdateRun updateRunsGetTopLevel(subscriptionId, resourceGroupName, updateLocation, runName, apiVersion)



Get an instance of update run using the ID.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateRunsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let updateLocation = "updateLocation_example"; // String | The name of the update location.
let runName = "runName_example"; // String | Update run identifier.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateRunsGetTopLevel(subscriptionId, resourceGroupName, updateLocation, runName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **updateLocation** | **String**| The name of the update location. | 
 **runName** | **String**| Update run identifier. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**UpdateRun**](UpdateRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRunsList

> UpdateRunList updateRunsList(subscriptionId, resourceGroupName, updateLocation, updateName, apiVersion)



Get the list of update runs.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateRunsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let updateLocation = "updateLocation_example"; // String | The name of the update location.
let updateName = "updateName_example"; // String | Name of the update.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateRunsList(subscriptionId, resourceGroupName, updateLocation, updateName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **updateLocation** | **String**| The name of the update location. | 
 **updateName** | **String**| Name of the update. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**UpdateRunList**](UpdateRunList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRunsListTopLevel

> UpdateRunList updateRunsListTopLevel(subscriptionId, resourceGroupName, updateLocation, apiVersion)



Get the list of update runs.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateRunsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let updateLocation = "updateLocation_example"; // String | The name of the update location.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateRunsListTopLevel(subscriptionId, resourceGroupName, updateLocation, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **updateLocation** | **String**| The name of the update location. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**UpdateRunList**](UpdateRunList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRunsRerun

> updateRunsRerun(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion)



Resume a failed update.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateRunsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let updateLocation = "updateLocation_example"; // String | The name of the update location.
let updateName = "updateName_example"; // String | Name of the update.
let runName = "runName_example"; // String | Update run identifier.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateRunsRerun(subscriptionId, resourceGroupName, updateLocation, updateName, runName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **updateLocation** | **String**| The name of the update location. | 
 **updateName** | **String**| Name of the update. | 
 **runName** | **String**| Update run identifier. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

