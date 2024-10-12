# BlockchainManagementClient.TransactionNodeApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionNodesCreate**](TransactionNodeApi.md#transactionNodesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} | 
[**transactionNodesDelete**](TransactionNodeApi.md#transactionNodesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} | 
[**transactionNodesGet**](TransactionNodeApi.md#transactionNodesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} | 
[**transactionNodesList**](TransactionNodeApi.md#transactionNodesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes | 
[**transactionNodesListApiKeys**](TransactionNodeApi.md#transactionNodesListApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}/listApiKeys | 
[**transactionNodesListRegenerateApiKeys**](TransactionNodeApi.md#transactionNodesListRegenerateApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}/regenerateApiKeys | 
[**transactionNodesUpdate**](TransactionNodeApi.md#transactionNodesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName} | 



## transactionNodesCreate

> TransactionNode transactionNodesCreate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, opts)



Create or update the transaction node.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let opts = {
  'transactionNode': new BlockchainManagementClient.TransactionNode() // TransactionNode | Payload to create the transaction node.
};
apiInstance.transactionNodesCreate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **transactionNodeName** | **String**| Transaction node name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **transactionNode** | [**TransactionNode**](TransactionNode.md)| Payload to create the transaction node. | [optional] 

### Return type

[**TransactionNode**](TransactionNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionNodesDelete

> transactionNodesDelete(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName)



Delete the transaction node.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.transactionNodesDelete(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **transactionNodeName** | **String**| Transaction node name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## transactionNodesGet

> TransactionNode transactionNodesGet(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName)



Get the details of the transaction node.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.transactionNodesGet(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **transactionNodeName** | **String**| Transaction node name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 

### Return type

[**TransactionNode**](TransactionNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionNodesList

> TransactionNodeCollection transactionNodesList(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Lists the transaction nodes for a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.transactionNodesList(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 

### Return type

[**TransactionNodeCollection**](TransactionNodeCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionNodesListApiKeys

> ApiKeyCollection transactionNodesListApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName)



List the API keys for the transaction node.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.transactionNodesListApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **transactionNodeName** | **String**| Transaction node name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 

### Return type

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionNodesListRegenerateApiKeys

> ApiKeyCollection transactionNodesListRegenerateApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, opts)



Regenerate the API keys for the blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let opts = {
  'apiKey': new BlockchainManagementClient.ApiKey() // ApiKey | api key to be regenerated
};
apiInstance.transactionNodesListRegenerateApiKeys(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **transactionNodeName** | **String**| Transaction node name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **apiKey** | [**ApiKey**](ApiKey.md)| api key to be regenerated | [optional] 

### Return type

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transactionNodesUpdate

> TransactionNode transactionNodesUpdate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, opts)



Update the transaction node.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.TransactionNodeApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let transactionNodeName = "transactionNodeName_example"; // String | Transaction node name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let opts = {
  'transactionNode': new BlockchainManagementClient.TransactionNodeUpdate() // TransactionNodeUpdate | Payload to create the transaction node.
};
apiInstance.transactionNodesUpdate(blockchainMemberName, transactionNodeName, apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name. | 
 **transactionNodeName** | **String**| Transaction node name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **transactionNode** | [**TransactionNodeUpdate**](TransactionNodeUpdate.md)| Payload to create the transaction node. | [optional] 

### Return type

[**TransactionNode**](TransactionNode.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

