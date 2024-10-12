# NetworkResourceProviderClient.ExpressRouteCircuitsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCircuitsCreateOrUpdate**](ExpressRouteCircuitsApi.md#expressRouteCircuitsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/ | 
[**expressRouteCircuitsDelete**](ExpressRouteCircuitsApi.md#expressRouteCircuitsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/ | 
[**expressRouteCircuitsGet**](ExpressRouteCircuitsApi.md#expressRouteCircuitsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/ | 
[**expressRouteCircuitsList**](ExpressRouteCircuitsApi.md#expressRouteCircuitsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits | 
[**expressRouteCircuitsListAll**](ExpressRouteCircuitsApi.md#expressRouteCircuitsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/expressRouteCircuits | 
[**expressRouteCircuitsListArpTable**](ExpressRouteCircuitsApi.md#expressRouteCircuitsListArpTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}arpTable | 
[**expressRouteCircuitsListRoutesTable**](ExpressRouteCircuitsApi.md#expressRouteCircuitsListRoutesTable) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}routesTable | 
[**expressRouteCircuitsListStats**](ExpressRouteCircuitsApi.md#expressRouteCircuitsListStats) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}stats | 



## expressRouteCircuitsCreateOrUpdate

> ExpressRouteCircuit expressRouteCircuitsCreateOrUpdate(resourceGroupName, circuitName, apiVersion, subscriptionId, parameters)



The Put ExpressRouteCircuit operation creates/updates a ExpressRouteCircuit

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the circuit.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkResourceProviderClient.ExpressRouteCircuit(); // ExpressRouteCircuit | Parameters supplied to the create/delete ExpressRouteCircuit operation
apiInstance.expressRouteCircuitsCreateOrUpdate(resourceGroupName, circuitName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **circuitName** | **String**| The name of the circuit. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ExpressRouteCircuit**](ExpressRouteCircuit.md)| Parameters supplied to the create/delete ExpressRouteCircuit operation | 

### Return type

[**ExpressRouteCircuit**](ExpressRouteCircuit.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## expressRouteCircuitsDelete

> expressRouteCircuitsDelete(resourceGroupName, circuitName, apiVersion, subscriptionId)



The delete ExpressRouteCircuit operation deletes the specified ExpressRouteCircuit.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route Circuit.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsDelete(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **circuitName** | **String**| The name of the express route Circuit. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expressRouteCircuitsGet

> ExpressRouteCircuit expressRouteCircuitsGet(resourceGroupName, circuitName, apiVersion, subscriptionId)



The Get ExpressRouteCircuit operation retrieves information about the specified ExpressRouteCircuit.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the circuit.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsGet(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **circuitName** | **String**| The name of the circuit. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuit**](ExpressRouteCircuit.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expressRouteCircuitsList

> ExpressRouteCircuitListResult expressRouteCircuitsList(resourceGroupName, apiVersion, subscriptionId)



The List ExpressRouteCircuit operation retrieves all the ExpressRouteCircuits in a resource group.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitListResult**](ExpressRouteCircuitListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expressRouteCircuitsListAll

> ExpressRouteCircuitListResult expressRouteCircuitsListAll(apiVersion, subscriptionId)



The List ExpressRouteCircuit operation retrieves all the ExpressRouteCircuits in a subscription.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsListAll(apiVersion, subscriptionId, (error, data, response) => {
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

[**ExpressRouteCircuitListResult**](ExpressRouteCircuitListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expressRouteCircuitsListArpTable

> ExpressRouteCircuitsArpTableListResult expressRouteCircuitsListArpTable(resourceGroupName, circuitName, apiVersion, subscriptionId)



The ListArpTable from ExpressRouteCircuit operation retrieves the currently advertised arp table associated with the ExpressRouteCircuits in a resource group.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the circuit.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsListArpTable(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **circuitName** | **String**| The name of the circuit. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitsArpTableListResult**](ExpressRouteCircuitsArpTableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expressRouteCircuitsListRoutesTable

> ExpressRouteCircuitsRoutesTableListResult expressRouteCircuitsListRoutesTable(resourceGroupName, circuitName, apiVersion, subscriptionId)



The ListRoutesTable from ExpressRouteCircuit operation retrieves the currently advertised routes table associated with the ExpressRouteCircuits in a resource group.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the circuit.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsListRoutesTable(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **circuitName** | **String**| The name of the circuit. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitsRoutesTableListResult**](ExpressRouteCircuitsRoutesTableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## expressRouteCircuitsListStats

> ExpressRouteCircuitsStatsListResult expressRouteCircuitsListStats(resourceGroupName, circuitName, apiVersion, subscriptionId)



The ListStats ExpressRouteCircuit operation retrieves all the stats from a ExpressRouteCircuits in a resource group.

### Example

```javascript
import NetworkResourceProviderClient from 'network_resource_provider_client';
let defaultClient = NetworkResourceProviderClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkResourceProviderClient.ExpressRouteCircuitsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the loadBalancer.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsListStats(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **circuitName** | **String**| The name of the loadBalancer. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitsStatsListResult**](ExpressRouteCircuitsStatsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

