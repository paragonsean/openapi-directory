# DataShareManagementClient.InvitationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invitationsCreate**](InvitationApi.md#invitationsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations/{invitationName} | Sends a new invitation to a recipient to access a share.
[**invitationsDelete**](InvitationApi.md#invitationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations/{invitationName} | Delete Invitation in a share.
[**invitationsGet**](InvitationApi.md#invitationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations/{invitationName} | Get Invitation in a share.
[**invitationsListByShare**](InvitationApi.md#invitationsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/invitations | List all Invitations in a share.



## invitationsCreate

> Invitation invitationsCreate(subscriptionId, resourceGroupName, accountName, shareName, invitationName, apiVersion, invitation)

Sends a new invitation to a recipient to access a share.

Create an invitation 

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.InvitationApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share to send the invitation for.
let invitationName = "invitationName_example"; // String | The name of the invitation.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let invitation = new DataShareManagementClient.Invitation(); // Invitation | Invitation details.
apiInstance.invitationsCreate(subscriptionId, resourceGroupName, accountName, shareName, invitationName, apiVersion, invitation, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share to send the invitation for. | 
 **invitationName** | **String**| The name of the invitation. | 
 **apiVersion** | **String**| The api version to use. | 
 **invitation** | [**Invitation**](Invitation.md)| Invitation details. | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invitationsDelete

> invitationsDelete(subscriptionId, resourceGroupName, accountName, shareName, invitationName, apiVersion)

Delete Invitation in a share.

Delete an invitation in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.InvitationApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let invitationName = "invitationName_example"; // String | The name of the invitation.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.invitationsDelete(subscriptionId, resourceGroupName, accountName, shareName, invitationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share. | 
 **invitationName** | **String**| The name of the invitation. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invitationsGet

> Invitation invitationsGet(subscriptionId, resourceGroupName, accountName, shareName, invitationName, apiVersion)

Get Invitation in a share.

Get an invitation in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.InvitationApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let invitationName = "invitationName_example"; // String | The name of the invitation.
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.invitationsGet(subscriptionId, resourceGroupName, accountName, shareName, invitationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share. | 
 **invitationName** | **String**| The name of the invitation. | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**Invitation**](Invitation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invitationsListByShare

> InvitationList invitationsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts)

List all Invitations in a share.

List invitations in a share

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.InvitationApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let accountName = "accountName_example"; // String | The name of the share account.
let shareName = "shareName_example"; // String | The name of the share.
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | The continuation token
};
apiInstance.invitationsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier | 
 **resourceGroupName** | **String**| The resource group name. | 
 **accountName** | **String**| The name of the share account. | 
 **shareName** | **String**| The name of the share. | 
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| The continuation token | [optional] 

### Return type

[**InvitationList**](InvitationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

