# KustoManagementClient.DataConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataConnectionsCheckNameAvailability**](DataConnectionsApi.md#dataConnectionsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/checkNameAvailability | 
[**dataConnectionsCreateOrUpdate**](DataConnectionsApi.md#dataConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} | 
[**dataConnectionsDataConnectionValidation**](DataConnectionsApi.md#dataConnectionsDataConnectionValidation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnectionValidation | 
[**dataConnectionsDelete**](DataConnectionsApi.md#dataConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} | 
[**dataConnectionsGet**](DataConnectionsApi.md#dataConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} | 
[**dataConnectionsListByDatabase**](DataConnectionsApi.md#dataConnectionsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections | 
[**dataConnectionsUpdate**](DataConnectionsApi.md#dataConnectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} | 



## dataConnectionsCheckNameAvailability

> CheckNameResult dataConnectionsCheckNameAvailability(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, dataConnectionName)



Checks that the data connection name is valid and is not already in use.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let dataConnectionName = new KustoManagementClient.DataConnectionCheckNameRequest(); // DataConnectionCheckNameRequest | The name of the data connection.
apiInstance.dataConnectionsCheckNameAvailability(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, dataConnectionName, (error, data, response) => {
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
 **dataConnectionName** | [**DataConnectionCheckNameRequest**](DataConnectionCheckNameRequest.md)| The name of the data connection. | 

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataConnectionsCreateOrUpdate

> DataConnection dataConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters)



Creates or updates a data connection.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.DataConnection(); // DataConnection | The data connection parameters supplied to the CreateOrUpdate operation.
apiInstance.dataConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **dataConnectionName** | **String**| The name of the data connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**DataConnection**](DataConnection.md)| The data connection parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataConnectionsDataConnectionValidation

> DataConnectionValidationListResult dataConnectionsDataConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters)



Checks that the data connection parameters are valid.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KustoManagementClient.DataConnectionValidation(); // DataConnectionValidation | The data connection parameters supplied to the CreateOrUpdate operation.
apiInstance.dataConnectionsDataConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**DataConnectionValidation**](DataConnectionValidation.md)| The data connection parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**DataConnectionValidationListResult**](DataConnectionValidationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataConnectionsDelete

> dataConnectionsDelete(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion)



Deletes the data connection with the given name.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.dataConnectionsDelete(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, (error, data, response) => {
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
 **dataConnectionName** | **String**| The name of the data connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataConnectionsGet

> DataConnection dataConnectionsGet(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion)



Returns a data connection.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.dataConnectionsGet(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, (error, data, response) => {
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
 **dataConnectionName** | **String**| The name of the data connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataConnectionsListByDatabase

> DataConnectionListResult dataConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns the list of data connections of the given Kusto database.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.dataConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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

[**DataConnectionListResult**](DataConnectionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataConnectionsUpdate

> DataConnection dataConnectionsUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters)



Updates a data connection.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DataConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.DataConnection(); // DataConnection | The data connection parameters supplied to the Update operation.
apiInstance.dataConnectionsUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **dataConnectionName** | **String**| The name of the data connection. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**DataConnection**](DataConnection.md)| The data connection parameters supplied to the Update operation. | 

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

