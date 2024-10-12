# AzureAnalysisServices.ServersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serversCheckNameAvailability**](ServersApi.md#serversCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/checkNameAvailability | 
[**serversCreate**](ServersApi.md#serversCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} | 
[**serversDelete**](ServersApi.md#serversDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} | 
[**serversDissociateGateway**](ServersApi.md#serversDissociateGateway) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/dissociateGateway | 
[**serversGetDetails**](ServersApi.md#serversGetDetails) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} | 
[**serversList**](ServersApi.md#serversList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/servers | 
[**serversListByResourceGroup**](ServersApi.md#serversListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers | 
[**serversListGatewayStatus**](ServersApi.md#serversListGatewayStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/listGatewayStatus | 
[**serversListOperationResults**](ServersApi.md#serversListOperationResults) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationresults/{operationId} | 
[**serversListOperationStatuses**](ServersApi.md#serversListOperationStatuses) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AnalysisServices/locations/{location}/operationstatuses/{operationId} | 
[**serversListSkusForExisting**](ServersApi.md#serversListSkusForExisting) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/skus | 
[**serversResume**](ServersApi.md#serversResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/resume | 
[**serversSuspend**](ServersApi.md#serversSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName}/suspend | 
[**serversUpdate**](ServersApi.md#serversUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AnalysisServices/servers/{serverName} | 



## serversCheckNameAvailability

> CheckServerNameAvailabilityResult serversCheckNameAvailability(location, apiVersion, subscriptionId, serverParameters)



Check the name availability in the target location.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let location = "location_example"; // String | The region name which the operation will lookup into.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let serverParameters = new AzureAnalysisServices.CheckServerNameAvailabilityParameters(); // CheckServerNameAvailabilityParameters | Contains the information used to provision the Analysis Services server.
apiInstance.serversCheckNameAvailability(location, apiVersion, subscriptionId, serverParameters, (error, data, response) => {
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
 **serverParameters** | [**CheckServerNameAvailabilityParameters**](CheckServerNameAvailabilityParameters.md)| Contains the information used to provision the Analysis Services server. | 

### Return type

[**CheckServerNameAvailabilityResult**](CheckServerNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversCreate

> AnalysisServicesServer serversCreate(resourceGroupName, serverName, apiVersion, subscriptionId, serverParameters)



Provisions the specified Analysis Services server based on the configuration specified in the request.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let serverParameters = new AzureAnalysisServices.AnalysisServicesServer(); // AnalysisServicesServer | Contains the information used to provision the Analysis Services server.
apiInstance.serversCreate(resourceGroupName, serverName, apiVersion, subscriptionId, serverParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **serverParameters** | [**AnalysisServicesServer**](AnalysisServicesServer.md)| Contains the information used to provision the Analysis Services server. | 

### Return type

[**AnalysisServicesServer**](AnalysisServicesServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversDelete

> serversDelete(resourceGroupName, serverName, apiVersion, subscriptionId)



Deletes the specified Analysis Services server.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversDelete(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serversDissociateGateway

> serversDissociateGateway(resourceGroupName, serverName, apiVersion, subscriptionId)



Dissociates a Unified Gateway associated with the server.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversDissociateGateway(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serversGetDetails

> AnalysisServicesServer serversGetDetails(resourceGroupName, serverName, apiVersion, subscriptionId)



Gets details about the specified Analysis Services server.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversGetDetails(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be a minimum of 3 characters, and a maximum of 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AnalysisServicesServer**](AnalysisServicesServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversList

> AnalysisServicesServers serversList(apiVersion, subscriptionId)



Lists all the Analysis Services servers for the given subscription.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversList(apiVersion, subscriptionId, (error, data, response) => {
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

[**AnalysisServicesServers**](AnalysisServicesServers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversListByResourceGroup

> AnalysisServicesServers serversListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all the Analysis Services servers for the given resource group.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AnalysisServicesServers**](AnalysisServicesServers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversListGatewayStatus

> GatewayListStatusLive serversListGatewayStatus(resourceGroupName, serverName, apiVersion, subscriptionId)



Return the gateway status of the specified Analysis Services server instance.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversListGatewayStatus(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**GatewayListStatusLive**](GatewayListStatusLive.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversListOperationResults

> serversListOperationResults(location, operationId, apiVersion, subscriptionId)



List the result of the specified operation.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let location = "location_example"; // String | The region name which the operation will lookup into.
let operationId = "operationId_example"; // String | The target operation Id.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversListOperationResults(location, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The region name which the operation will lookup into. | 
 **operationId** | **String**| The target operation Id. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serversListOperationStatuses

> OperationStatus serversListOperationStatuses(location, operationId, apiVersion, subscriptionId)



List the status of operation.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let location = "location_example"; // String | The region name which the operation will lookup into.
let operationId = "operationId_example"; // String | The target operation Id.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversListOperationStatuses(location, operationId, apiVersion, subscriptionId, (error, data, response) => {
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
 **operationId** | **String**| The target operation Id. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversListSkusForExisting

> SkuEnumerationForExistingResourceResult serversListSkusForExisting(resourceGroupName, serverName, apiVersion, subscriptionId)



Lists eligible SKUs for an Analysis Services resource.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversListSkusForExisting(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SkuEnumerationForExistingResourceResult**](SkuEnumerationForExistingResourceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversResume

> serversResume(resourceGroupName, serverName, apiVersion, subscriptionId)



Resumes operation of the specified Analysis Services server instance.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversResume(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serversSuspend

> serversSuspend(resourceGroupName, serverName, apiVersion, subscriptionId)



Suspends operation of the specified Analysis Services server instance.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.serversSuspend(resourceGroupName, serverName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serversUpdate

> AnalysisServicesServer serversUpdate(resourceGroupName, serverName, apiVersion, subscriptionId, serverUpdateParameters)



Updates the current state of the specified Analysis Services server.

### Example

```javascript
import AzureAnalysisServices from 'azure_analysis_services';
let defaultClient = AzureAnalysisServices.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureAnalysisServices.ServersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90.
let serverName = "serverName_example"; // String | The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63.
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let serverUpdateParameters = new AzureAnalysisServices.AnalysisServicesServerUpdateParameters(); // AnalysisServicesServerUpdateParameters | Request object that contains the updated information for the server.
apiInstance.serversUpdate(resourceGroupName, serverName, apiVersion, subscriptionId, serverUpdateParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure Resource group of which a given Analysis Services server is part. This name must be at least 1 character in length, and no more than 90. | 
 **serverName** | **String**| The name of the Analysis Services server. It must be at least 3 characters in length, and no more than 63. | 
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **serverUpdateParameters** | [**AnalysisServicesServerUpdateParameters**](AnalysisServicesServerUpdateParameters.md)| Request object that contains the updated information for the server. | 

### Return type

[**AnalysisServicesServer**](AnalysisServicesServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

