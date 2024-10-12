# CostManagementClient.CloudConnectorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudConnectorCreateOrUpdate**](CloudConnectorsApi.md#cloudConnectorCreateOrUpdate) | **PUT** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} | 
[**cloudConnectorDelete**](CloudConnectorsApi.md#cloudConnectorDelete) | **DELETE** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} | 
[**cloudConnectorGet**](CloudConnectorsApi.md#cloudConnectorGet) | **GET** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} | 
[**cloudConnectorList**](CloudConnectorsApi.md#cloudConnectorList) | **GET** /providers/Microsoft.CostManagement/cloudConnectors | 
[**cloudConnectorUpdate**](CloudConnectorsApi.md#cloudConnectorUpdate) | **PATCH** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} | 



## cloudConnectorCreateOrUpdate

> ConnectorDefinition cloudConnectorCreateOrUpdate(apiVersion, connectorName, connector)



Create or update a cloud connector definition

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.CloudConnectorsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let connectorName = "connectorName_example"; // String | Connector Name.
let connector = new CostManagementClient.ConnectorDefinition(); // ConnectorDefinition | Connector details
apiInstance.cloudConnectorCreateOrUpdate(apiVersion, connectorName, connector, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **connectorName** | **String**| Connector Name. | 
 **connector** | [**ConnectorDefinition**](ConnectorDefinition.md)| Connector details | 

### Return type

[**ConnectorDefinition**](ConnectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cloudConnectorDelete

> cloudConnectorDelete(apiVersion, connectorName)



Delete a cloud connector definition

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.CloudConnectorsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let connectorName = "connectorName_example"; // String | Connector Name.
apiInstance.cloudConnectorDelete(apiVersion, connectorName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **connectorName** | **String**| Connector Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectorGet

> ConnectorDefinition cloudConnectorGet(apiVersion, connectorName, opts)



Get a cloud connector definition

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.CloudConnectorsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let connectorName = "connectorName_example"; // String | Connector Name.
let opts = {
  'expand': "expand_example" // String | May be used to expand the collectionInfo property. By default, collectionInfo is not included.
};
apiInstance.cloudConnectorGet(apiVersion, connectorName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **connectorName** | **String**| Connector Name. | 
 **expand** | **String**| May be used to expand the collectionInfo property. By default, collectionInfo is not included. | [optional] 

### Return type

[**ConnectorDefinition**](ConnectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectorList

> ConnectorDefinitionListResult cloudConnectorList(apiVersion)



List all cloud connector definitions

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.CloudConnectorsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
apiInstance.cloudConnectorList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 

### Return type

[**ConnectorDefinitionListResult**](ConnectorDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudConnectorUpdate

> ConnectorDefinition cloudConnectorUpdate(apiVersion, connectorName, connector)



Update a cloud connector definition

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.CloudConnectorsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let connectorName = "connectorName_example"; // String | Connector Name.
let connector = new CostManagementClient.ConnectorDefinition(); // ConnectorDefinition | Connector details
apiInstance.cloudConnectorUpdate(apiVersion, connectorName, connector, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **connectorName** | **String**| Connector Name. | 
 **connector** | [**ConnectorDefinition**](ConnectorDefinition.md)| Connector details | 

### Return type

[**ConnectorDefinition**](ConnectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

