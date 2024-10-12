# NetworkExperiments.NetworkExperimentProfilesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkExperimentProfilesCreateOrUpdate**](NetworkExperimentProfilesApi.md#networkExperimentProfilesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Creates an NetworkExperiment Profile
[**networkExperimentProfilesDelete**](NetworkExperimentProfilesApi.md#networkExperimentProfilesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Deletes an NetworkExperiment Profile by ProfileName
[**networkExperimentProfilesGet**](NetworkExperimentProfilesApi.md#networkExperimentProfilesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Gets an NetworkExperiment Profile by ProfileName
[**networkExperimentProfilesList**](NetworkExperimentProfilesApi.md#networkExperimentProfilesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/NetworkExperimentProfiles | Gets a list of Network Experiment Profiles under a subscription
[**networkExperimentProfilesListByResourceGroup**](NetworkExperimentProfilesApi.md#networkExperimentProfilesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles | Gets a list of Network Experiment Profiles within a resource group under a subscription
[**networkExperimentProfilesUpdate**](NetworkExperimentProfilesApi.md#networkExperimentProfilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName} | Updates an NetworkExperimentProfiles by NetworkExperimentProfile name



## networkExperimentProfilesCreateOrUpdate

> Profile networkExperimentProfilesCreateOrUpdate(profileName, subscriptionId, apiVersion, resourceGroupName, parameters)

Creates an NetworkExperiment Profile

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.NetworkExperimentProfilesApi();
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let parameters = new NetworkExperiments.Profile(); // Profile | An Network Experiment Profile
apiInstance.networkExperimentProfilesCreateOrUpdate(profileName, subscriptionId, apiVersion, resourceGroupName, parameters, (error, data, response) => {
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
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **parameters** | [**Profile**](Profile.md)| An Network Experiment Profile | 

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## networkExperimentProfilesDelete

> networkExperimentProfilesDelete(subscriptionId, apiVersion, resourceGroupName, profileName)

Deletes an NetworkExperiment Profile by ProfileName

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.NetworkExperimentProfilesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
apiInstance.networkExperimentProfilesDelete(subscriptionId, apiVersion, resourceGroupName, profileName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkExperimentProfilesGet

> Profile networkExperimentProfilesGet(subscriptionId, apiVersion, resourceGroupName, profileName)

Gets an NetworkExperiment Profile by ProfileName

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.NetworkExperimentProfilesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
apiInstance.networkExperimentProfilesGet(subscriptionId, apiVersion, resourceGroupName, profileName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkExperimentProfilesList

> ProfileList networkExperimentProfilesList(subscriptionId, apiVersion)

Gets a list of Network Experiment Profiles under a subscription

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.NetworkExperimentProfilesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.networkExperimentProfilesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**ProfileList**](ProfileList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkExperimentProfilesListByResourceGroup

> ProfileList networkExperimentProfilesListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Gets a list of Network Experiment Profiles within a resource group under a subscription

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.NetworkExperimentProfilesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
apiInstance.networkExperimentProfilesListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 

### Return type

[**ProfileList**](ProfileList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## networkExperimentProfilesUpdate

> Profile networkExperimentProfilesUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, parameters)

Updates an NetworkExperimentProfiles by NetworkExperimentProfile name

Updates an NetworkExperimentProfiles

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.NetworkExperimentProfilesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let parameters = new NetworkExperiments.ProfileUpdateModel(); // ProfileUpdateModel | The Profile Update Model
apiInstance.networkExperimentProfilesUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 
 **parameters** | [**ProfileUpdateModel**](ProfileUpdateModel.md)| The Profile Update Model | 

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

