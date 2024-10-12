# BlockchainManagementClient.BlockchainMemberApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blockchainMembersCreate**](BlockchainMemberApi.md#blockchainMembersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} | 
[**blockchainMembersDelete**](BlockchainMemberApi.md#blockchainMembersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} | 
[**blockchainMembersGet**](BlockchainMemberApi.md#blockchainMembersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} | 
[**blockchainMembersList**](BlockchainMemberApi.md#blockchainMembersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers | 
[**blockchainMembersListAll**](BlockchainMemberApi.md#blockchainMembersListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/blockchainMembers | 
[**blockchainMembersListApiKeys**](BlockchainMemberApi.md#blockchainMembersListApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/listApiKeys | 
[**blockchainMembersListConsortiumMembers**](BlockchainMemberApi.md#blockchainMembersListConsortiumMembers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/consortiumMembers | 
[**blockchainMembersListRegenerateApiKeys**](BlockchainMemberApi.md#blockchainMembersListRegenerateApiKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/regenerateApiKeys | 
[**blockchainMembersUpdate**](BlockchainMemberApi.md#blockchainMembersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName} | 



## blockchainMembersCreate

> BlockchainMember blockchainMembersCreate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, opts)



Create a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let opts = {
  'blockchainMember': new BlockchainManagementClient.BlockchainMember() // BlockchainMember | Payload to create a blockchain member.
};
apiInstance.blockchainMembersCreate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **blockchainMember** | [**BlockchainMember**](BlockchainMember.md)| Payload to create a blockchain member. | [optional] 

### Return type

[**BlockchainMember**](BlockchainMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blockchainMembersDelete

> blockchainMembersDelete(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Delete a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.blockchainMembersDelete(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **blockchainMemberName** | **String**| Blockchain member name | 
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


## blockchainMembersGet

> BlockchainMember blockchainMembersGet(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Get details about a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.blockchainMembersGet(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

[**BlockchainMember**](BlockchainMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainMembersList

> BlockchainMemberCollection blockchainMembersList(apiVersion, subscriptionId, resourceGroupName)



Lists the blockchain members for a resource group.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.blockchainMembersList(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 

### Return type

[**BlockchainMemberCollection**](BlockchainMemberCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainMembersListAll

> BlockchainMemberCollection blockchainMembersListAll(apiVersion, subscriptionId)



Lists the blockchain members for a subscription.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
apiInstance.blockchainMembersListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 

### Return type

[**BlockchainMemberCollection**](BlockchainMemberCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainMembersListApiKeys

> ApiKeyCollection blockchainMembersListApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Lists the API keys for a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.blockchainMembersListApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainMembersListConsortiumMembers

> ConsortiumMemberCollection blockchainMembersListConsortiumMembers(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName)



Lists the consortium members for a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.blockchainMembersListConsortiumMembers(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

[**ConsortiumMemberCollection**](ConsortiumMemberCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blockchainMembersListRegenerateApiKeys

> ApiKeyCollection blockchainMembersListRegenerateApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, opts)



Regenerate the API keys for a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let opts = {
  'apiKey': new BlockchainManagementClient.ApiKey() // ApiKey | api key to be regenerate
};
apiInstance.blockchainMembersListRegenerateApiKeys(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **apiKey** | [**ApiKey**](ApiKey.md)| api key to be regenerate | [optional] 

### Return type

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blockchainMembersUpdate

> BlockchainMember blockchainMembersUpdate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, opts)



Update a blockchain member.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.BlockchainMemberApi();
let blockchainMemberName = "blockchainMemberName_example"; // String | Blockchain member name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let opts = {
  'blockchainMember': new BlockchainManagementClient.BlockchainMemberUpdate() // BlockchainMemberUpdate | Payload to update the blockchain member.
};
apiInstance.blockchainMembersUpdate(blockchainMemberName, apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **blockchainMember** | [**BlockchainMemberUpdate**](BlockchainMemberUpdate.md)| Payload to update the blockchain member. | [optional] 

### Return type

[**BlockchainMember**](BlockchainMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

