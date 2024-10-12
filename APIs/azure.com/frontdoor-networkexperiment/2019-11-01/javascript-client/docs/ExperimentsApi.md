# NetworkExperiments.ExperimentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experimentsCreateOrUpdate**](ExperimentsApi.md#experimentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName} | Creates or updates an Experiment
[**experimentsDelete**](ExperimentsApi.md#experimentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName} | Deletes an Experiment
[**experimentsGet**](ExperimentsApi.md#experimentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName} | Gets an Experiment by ExperimentName
[**experimentsListByProfile**](ExperimentsApi.md#experimentsListByProfile) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments | Gets a list of Experiments
[**experimentsUpdate**](ExperimentsApi.md#experimentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName} | Updates an Experiment by Experiment id



## experimentsCreateOrUpdate

> Experiment experimentsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, parameters)

Creates or updates an Experiment

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ExperimentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
let parameters = new NetworkExperiments.Experiment(); // Experiment | The Experiment resource
apiInstance.experimentsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, parameters, (error, data, response) => {
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
 **experimentName** | **String**| The Experiment identifier associated with the Experiment | 
 **parameters** | [**Experiment**](Experiment.md)| The Experiment resource | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## experimentsDelete

> experimentsDelete(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName)

Deletes an Experiment

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ExperimentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
apiInstance.experimentsDelete(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, (error, data, response) => {
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
 **experimentName** | **String**| The Experiment identifier associated with the Experiment | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## experimentsGet

> Experiment experimentsGet(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName)

Gets an Experiment by ExperimentName

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ExperimentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
apiInstance.experimentsGet(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, (error, data, response) => {
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
 **experimentName** | **String**| The Experiment identifier associated with the Experiment | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## experimentsListByProfile

> ExperimentList experimentsListByProfile(subscriptionId, apiVersion, resourceGroupName, profileName)

Gets a list of Experiments

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ExperimentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
apiInstance.experimentsListByProfile(subscriptionId, apiVersion, resourceGroupName, profileName, (error, data, response) => {
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

[**ExperimentList**](ExperimentList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## experimentsUpdate

> Experiment experimentsUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, parameters)

Updates an Experiment by Experiment id

Updates an Experiment

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ExperimentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
let parameters = new NetworkExperiments.ExperimentUpdateModel(); // ExperimentUpdateModel | The Experiment Update Model
apiInstance.experimentsUpdate(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, parameters, (error, data, response) => {
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
 **experimentName** | **String**| The Experiment identifier associated with the Experiment | 
 **parameters** | [**ExperimentUpdateModel**](ExperimentUpdateModel.md)| The Experiment Update Model | 

### Return type

[**Experiment**](Experiment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

