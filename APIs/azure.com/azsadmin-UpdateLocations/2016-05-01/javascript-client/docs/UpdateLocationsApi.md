# UpdateAdminClient.UpdateLocationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateLocationsGet**](UpdateLocationsApi.md#updateLocationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/{updateLocation} | 
[**updateLocationsList**](UpdateLocationsApi.md#updateLocationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Update.Admin/updateLocations/ | 



## updateLocationsGet

> UpdateLocation updateLocationsGet(subscriptionId, resourceGroupName, updateLocation, apiVersion)



Get an update location based on name.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateLocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let updateLocation = "updateLocation_example"; // String | The name of the update location.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateLocationsGet(subscriptionId, resourceGroupName, updateLocation, apiVersion, (error, data, response) => {
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

[**UpdateLocation**](UpdateLocation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateLocationsList

> UpdateLocationList updateLocationsList(subscriptionId, resourceGroupName, apiVersion)



Get the list of update locations.

### Example

```javascript
import UpdateAdminClient from 'update_admin_client';
let defaultClient = UpdateAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateAdminClient.UpdateLocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.  The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.updateLocationsList(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**UpdateLocationList**](UpdateLocationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

