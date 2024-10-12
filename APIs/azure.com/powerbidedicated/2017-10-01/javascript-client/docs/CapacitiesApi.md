# PowerBiDedicated.CapacitiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capacitiesCheckNameAvailability**](CapacitiesApi.md#capacitiesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBIDedicated/locations/{location}/checkNameAvailability | 
[**capacitiesCreate**](CapacitiesApi.md#capacitiesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} | 
[**capacitiesDelete**](CapacitiesApi.md#capacitiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} | 
[**capacitiesGetDetails**](CapacitiesApi.md#capacitiesGetDetails) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} | 
[**capacitiesList**](CapacitiesApi.md#capacitiesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBIDedicated/capacities | 
[**capacitiesListByResourceGroup**](CapacitiesApi.md#capacitiesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities | 
[**capacitiesListSkusForCapacity**](CapacitiesApi.md#capacitiesListSkusForCapacity) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}/skus | 
[**capacitiesResume**](CapacitiesApi.md#capacitiesResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}/resume | 
[**capacitiesSuspend**](CapacitiesApi.md#capacitiesSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName}/suspend | 
[**capacitiesUpdate**](CapacitiesApi.md#capacitiesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBIDedicated/capacities/{dedicatedCapacityName} | 



## capacitiesCheckNameAvailability

> CheckCapacityNameAvailabilityResult capacitiesCheckNameAvailability(location, apiVersion, subscriptionId, capacityParameters)



Check the name availability in the target location.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let location = "location_example"; // String | The region name which the operation will lookup into.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let capacityParameters = new PowerBiDedicated.CheckCapacityNameAvailabilityParameters(); // CheckCapacityNameAvailabilityParameters | The name of the capacity.
apiInstance.capacitiesCheckNameAvailability(location, apiVersion, subscriptionId, capacityParameters, (error, data, response) => {
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
 **location** | **String**| The region name which the operation will lookup into. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **capacityParameters** | [**CheckCapacityNameAvailabilityParameters**](CheckCapacityNameAvailabilityParameters.md)| The name of the capacity. | 

### Return type

[**CheckCapacityNameAvailabilityResult**](CheckCapacityNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## capacitiesCreate

> DedicatedCapacity capacitiesCreate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityParameters)



Provisions the specified Dedicated capacity based on the configuration specified in the request.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let capacityParameters = new PowerBiDedicated.DedicatedCapacity(); // DedicatedCapacity | Contains the information used to provision the Dedicated capacity.
apiInstance.capacitiesCreate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **capacityParameters** | [**DedicatedCapacity**](DedicatedCapacity.md)| Contains the information used to provision the Dedicated capacity. | 

### Return type

[**DedicatedCapacity**](DedicatedCapacity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## capacitiesDelete

> capacitiesDelete(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Deletes the specified Dedicated capacity.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesDelete(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## capacitiesGetDetails

> DedicatedCapacity capacitiesGetDetails(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Gets details about the specified dedicated capacity.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesGetDetails(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DedicatedCapacity**](DedicatedCapacity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## capacitiesList

> DedicatedCapacities capacitiesList(apiVersion, subscriptionId)



Lists all the Dedicated capacities for the given subscription.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DedicatedCapacities**](DedicatedCapacities.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## capacitiesListByResourceGroup

> DedicatedCapacities capacitiesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all the Dedicated capacities for the given resource group.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DedicatedCapacities**](DedicatedCapacities.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## capacitiesListSkusForCapacity

> SkuEnumerationForExistingResourceResult capacitiesListSkusForCapacity(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Lists eligible SKUs for a PowerBI Dedicated resource.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesListSkusForCapacity(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SkuEnumerationForExistingResourceResult**](SkuEnumerationForExistingResourceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## capacitiesResume

> capacitiesResume(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Resumes operation of the specified Dedicated capacity instance.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesResume(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## capacitiesSuspend

> capacitiesSuspend(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId)



Suspends operation of the specified dedicated capacity instance.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesSuspend(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## capacitiesUpdate

> DedicatedCapacity capacitiesUpdate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityUpdateParameters)



Updates the current state of the specified Dedicated capacity.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.CapacitiesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
let dedicatedCapacityName = "dedicatedCapacityName_example"; // String | The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let capacityUpdateParameters = new PowerBiDedicated.DedicatedCapacityUpdateParameters(); // DedicatedCapacityUpdateParameters | Request object that contains the updated information for the capacity.
apiInstance.capacitiesUpdate(resourceGroupName, dedicatedCapacityName, apiVersion, subscriptionId, capacityUpdateParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90. | 
 **dedicatedCapacityName** | **String**| The name of the Dedicated capacity. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **capacityUpdateParameters** | [**DedicatedCapacityUpdateParameters**](DedicatedCapacityUpdateParameters.md)| Request object that contains the updated information for the capacity. | 

### Return type

[**DedicatedCapacity**](DedicatedCapacity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

