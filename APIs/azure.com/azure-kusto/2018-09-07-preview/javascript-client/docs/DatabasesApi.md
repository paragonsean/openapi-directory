# KustoManagementClient.DatabasesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databasesAddPrincipals**](DatabasesApi.md#databasesAddPrincipals) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/addPrincipals | 
[**databasesCheckNameAvailability**](DatabasesApi.md#databasesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/checkNameAvailability | 
[**databasesCreateOrUpdate**](DatabasesApi.md#databasesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} | 
[**databasesDelete**](DatabasesApi.md#databasesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} | 
[**databasesGet**](DatabasesApi.md#databasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} | 
[**databasesListByCluster**](DatabasesApi.md#databasesListByCluster) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases | 
[**databasesListPrincipals**](DatabasesApi.md#databasesListPrincipals) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/listPrincipals | 
[**databasesRemovePrincipals**](DatabasesApi.md#databasesRemovePrincipals) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/removePrincipals | 
[**databasesUpdate**](DatabasesApi.md#databasesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} | 



## databasesAddPrincipals

> DatabasePrincipalListResult databasesAddPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToAdd)



Add Database principals permissions.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let databasePrincipalsToAdd = new KustoManagementClient.DatabasePrincipalListRequest(); // DatabasePrincipalListRequest | List of database principals to add.
apiInstance.databasesAddPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToAdd, (error, data, response) => {
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
 **databasePrincipalsToAdd** | [**DatabasePrincipalListRequest**](DatabasePrincipalListRequest.md)| List of database principals to add. | 

### Return type

[**DatabasePrincipalListResult**](DatabasePrincipalListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasesCheckNameAvailability

> CheckNameResult databasesCheckNameAvailability(resourceGroupName, clusterName, apiVersion, subscriptionId, databaseName)



Checks that the database name is valid and is not already in use.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let databaseName = new KustoManagementClient.DatabaseCheckNameRequest(); // DatabaseCheckNameRequest | The name of the database.
apiInstance.databasesCheckNameAvailability(resourceGroupName, clusterName, apiVersion, subscriptionId, databaseName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **databaseName** | [**DatabaseCheckNameRequest**](DatabaseCheckNameRequest.md)| The name of the database. | 

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasesCreateOrUpdate

> Database databasesCreateOrUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters)



Creates or updates a database.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.Database(); // Database | The database parameters supplied to the CreateOrUpdate operation.
apiInstance.databasesCreateOrUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**Database**](Database.md)| The database parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasesDelete

> databasesDelete(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Deletes the database with the given name.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.databasesDelete(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasesGet

> Database databasesGet(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns a database.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.databasesGet(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasesListByCluster

> DatabaseListResult databasesListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion)



Returns the list of databases of the given Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.databasesListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**DatabaseListResult**](DatabaseListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasesListPrincipals

> DatabasePrincipalListResult databasesListPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns a list of database principals of the given Kusto cluster and database.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.databasesListPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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

[**DatabasePrincipalListResult**](DatabasePrincipalListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasesRemovePrincipals

> DatabasePrincipalListResult databasesRemovePrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToRemove)



Remove Database principals permissions.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let databasePrincipalsToRemove = new KustoManagementClient.DatabasePrincipalListRequest(); // DatabasePrincipalListRequest | List of database principals to remove.
apiInstance.databasesRemovePrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToRemove, (error, data, response) => {
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
 **databasePrincipalsToRemove** | [**DatabasePrincipalListRequest**](DatabasePrincipalListRequest.md)| List of database principals to remove. | 

### Return type

[**DatabasePrincipalListResult**](DatabasePrincipalListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasesUpdate

> Database databasesUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters)



Updates a database.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.DatabaseUpdate(); // DatabaseUpdate | The database parameters supplied to the Update operation.
apiInstance.databasesUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**DatabaseUpdate**](DatabaseUpdate.md)| The database parameters supplied to the Update operation. | 

### Return type

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

