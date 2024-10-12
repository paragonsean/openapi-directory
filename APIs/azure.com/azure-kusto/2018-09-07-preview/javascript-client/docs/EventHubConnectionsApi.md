# KustoManagementClient.EventHubConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventHubConnectionsCreateOrUpdate**](EventHubConnectionsApi.md#eventHubConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} | 
[**eventHubConnectionsDelete**](EventHubConnectionsApi.md#eventHubConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} | 
[**eventHubConnectionsEventhubConnectionValidation**](EventHubConnectionsApi.md#eventHubConnectionsEventhubConnectionValidation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubConnectionValidation | 
[**eventHubConnectionsGet**](EventHubConnectionsApi.md#eventHubConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} | 
[**eventHubConnectionsListByDatabase**](EventHubConnectionsApi.md#eventHubConnectionsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections | 
[**eventHubConnectionsUpdate**](EventHubConnectionsApi.md#eventHubConnectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} | 



## eventHubConnectionsCreateOrUpdate

> EventHubConnection eventHubConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters)



Creates or updates a Event Hub connection.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.EventHubConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.EventHubConnection(); // EventHubConnection | The Event Hub connection parameters supplied to the CreateOrUpdate operation.
apiInstance.eventHubConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **databaseName** | **String**| The name of the database in the Kusto cluster. | 
 **eventHubConnectionName** | **String**| The name of the event hub connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**EventHubConnection**](EventHubConnection.md)| The Event Hub connection parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**EventHubConnection**](EventHubConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## eventHubConnectionsDelete

> eventHubConnectionsDelete(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion)



Deletes the Event Hub connection with the given name.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.EventHubConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.eventHubConnectionsDelete(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **databaseName** | **String**| The name of the database in the Kusto cluster. | 
 **eventHubConnectionName** | **String**| The name of the event hub connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubConnectionsEventhubConnectionValidation

> EventHubConnectionValidationListResult eventHubConnectionsEventhubConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters)



Checks that the Event Hub data connection parameters are valid.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.EventHubConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KustoManagementClient.EventHubConnectionValidation(); // EventHubConnectionValidation | The Event Hub connection parameters supplied to the CreateOrUpdate operation.
apiInstance.eventHubConnectionsEventhubConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **databaseName** | **String**| The name of the database in the Kusto cluster. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**EventHubConnectionValidation**](EventHubConnectionValidation.md)| The Event Hub connection parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**EventHubConnectionValidationListResult**](EventHubConnectionValidationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## eventHubConnectionsGet

> EventHubConnection eventHubConnectionsGet(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion)



Returns an Event Hub connection.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.EventHubConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.eventHubConnectionsGet(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **databaseName** | **String**| The name of the database in the Kusto cluster. | 
 **eventHubConnectionName** | **String**| The name of the event hub connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**EventHubConnection**](EventHubConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubConnectionsListByDatabase

> EventHubConnectionListResult eventHubConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns the list of Event Hub connections of the given Kusto database.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.EventHubConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.eventHubConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **databaseName** | **String**| The name of the database in the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**EventHubConnectionListResult**](EventHubConnectionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventHubConnectionsUpdate

> EventHubConnection eventHubConnectionsUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters)



Updates a Event Hub connection.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.EventHubConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.EventHubConnectionUpdate(); // EventHubConnectionUpdate | The Event Hub connection parameters supplied to the Update operation.
apiInstance.eventHubConnectionsUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **databaseName** | **String**| The name of the database in the Kusto cluster. | 
 **eventHubConnectionName** | **String**| The name of the event hub connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**EventHubConnectionUpdate**](EventHubConnectionUpdate.md)| The Event Hub connection parameters supplied to the Update operation. | 

### Return type

[**EventHubConnection**](EventHubConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

