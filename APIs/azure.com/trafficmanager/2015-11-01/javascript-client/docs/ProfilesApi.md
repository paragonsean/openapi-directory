# TrafficManagerManagementClient.ProfilesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profilesCheckTrafficManagerRelativeDnsNameAvailability**](ProfilesApi.md#profilesCheckTrafficManagerRelativeDnsNameAvailability) | **POST** /providers/Microsoft.Network/checkTrafficManagerNameAvailability | 
[**profilesCreateOrUpdate**](ProfilesApi.md#profilesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} | 
[**profilesDelete**](ProfilesApi.md#profilesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} | 
[**profilesGet**](ProfilesApi.md#profilesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} | 
[**profilesListAll**](ProfilesApi.md#profilesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/trafficmanagerprofiles | 
[**profilesListAllInResourceGroup**](ProfilesApi.md#profilesListAllInResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles | 
[**profilesUpdate**](ProfilesApi.md#profilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} | 



## profilesCheckTrafficManagerRelativeDnsNameAvailability

> TrafficManagerNameAvailability profilesCheckTrafficManagerRelativeDnsNameAvailability(apiVersion, parameters)



Checks the availability of a Traffic Manager Relative DNS name.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new TrafficManagerManagementClient.CheckTrafficManagerRelativeDnsNameAvailabilityParameters(); // CheckTrafficManagerRelativeDnsNameAvailabilityParameters | The Traffic Manager name parameters supplied to the CheckTrafficManagerNameAvailability operation.
apiInstance.profilesCheckTrafficManagerRelativeDnsNameAvailability(apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**CheckTrafficManagerRelativeDnsNameAvailabilityParameters**](CheckTrafficManagerRelativeDnsNameAvailabilityParameters.md)| The Traffic Manager name parameters supplied to the CheckTrafficManagerNameAvailability operation. | 

### Return type

[**TrafficManagerNameAvailability**](TrafficManagerNameAvailability.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## profilesCreateOrUpdate

> Profile profilesCreateOrUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters)



Create or update a Traffic Manager profile.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new TrafficManagerManagementClient.Profile(); // Profile | The Traffic Manager profile parameters supplied to the CreateOrUpdate operation.
apiInstance.profilesCreateOrUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Profile**](Profile.md)| The Traffic Manager profile parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## profilesDelete

> profilesDelete(resourceGroupName, profileName, apiVersion, subscriptionId)



Deletes a Traffic Manager profile.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile to be deleted.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.profilesDelete(resourceGroupName, profileName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile to be deleted. | 
 **profileName** | **String**| The name of the Traffic Manager profile to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## profilesGet

> Profile profilesGet(resourceGroupName, profileName, apiVersion, subscriptionId)



Gets a Traffic Manager profile.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.profilesGet(resourceGroupName, profileName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## profilesListAll

> ProfileListResult profilesListAll(apiVersion, subscriptionId)



Lists all Traffic Manager profiles within a subscription.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.profilesListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## profilesListAllInResourceGroup

> ProfileListResult profilesListAllInResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all Traffic Manager profiles within a resource group.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profiles to be listed.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.profilesListAllInResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profiles to be listed. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## profilesUpdate

> Profile profilesUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters)



Update a Traffic Manager profile.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';

let apiInstance = new TrafficManagerManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new TrafficManagerManagementClient.Profile(); // Profile | The Traffic Manager profile parameters supplied to the Update operation.
apiInstance.profilesUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Profile**](Profile.md)| The Traffic Manager profile parameters supplied to the Update operation. | 

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

