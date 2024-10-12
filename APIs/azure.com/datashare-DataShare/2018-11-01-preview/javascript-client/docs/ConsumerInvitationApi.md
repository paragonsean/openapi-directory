# DataShareManagementClient.ConsumerInvitationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerInvitationsGet**](ConsumerInvitationApi.md#consumerInvitationsGet) | **GET** /providers/Microsoft.DataShare/locations/{location}/consumerInvitations/{invitationId} | Gets the invitation identified by invitationId
[**consumerInvitationsListInvitations**](ConsumerInvitationApi.md#consumerInvitationsListInvitations) | **GET** /providers/Microsoft.DataShare/ListInvitations | List the invitations
[**consumerInvitationsRejectInvitation**](ConsumerInvitationApi.md#consumerInvitationsRejectInvitation) | **POST** /providers/Microsoft.DataShare/locations/{location}/RejectInvitation | Rejects the invitation identified by invitationId



## consumerInvitationsGet

> ConsumerInvitation consumerInvitationsGet(location, invitationId, apiVersion)

Gets the invitation identified by invitationId

Get an invitation

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ConsumerInvitationApi();
let location = "location_example"; // String | Location of the invitation
let invitationId = "invitationId_example"; // String | An invitation id
let apiVersion = "apiVersion_example"; // String | The api version to use.
apiInstance.consumerInvitationsGet(location, invitationId, apiVersion, (error, data, response) => {
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
 **location** | **String**| Location of the invitation | 
 **invitationId** | **String**| An invitation id | 
 **apiVersion** | **String**| The api version to use. | 

### Return type

[**ConsumerInvitation**](ConsumerInvitation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerInvitationsListInvitations

> ConsumerInvitationList consumerInvitationsListInvitations(apiVersion, opts)

List the invitations

Lists invitations

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ConsumerInvitationApi();
let apiVersion = "apiVersion_example"; // String | The api version to use.
let opts = {
  'skipToken': "skipToken_example" // String | The continuation token
};
apiInstance.consumerInvitationsListInvitations(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The api version to use. | 
 **skipToken** | **String**| The continuation token | [optional] 

### Return type

[**ConsumerInvitationList**](ConsumerInvitationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerInvitationsRejectInvitation

> ConsumerInvitation consumerInvitationsRejectInvitation(location, apiVersion, invitation)

Rejects the invitation identified by invitationId

Reject an invitation

### Example

```javascript
import DataShareManagementClient from 'data_share_management_client';
let defaultClient = DataShareManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataShareManagementClient.ConsumerInvitationApi();
let location = "location_example"; // String | Location of the invitation
let apiVersion = "apiVersion_example"; // String | The api version to use.
let invitation = new DataShareManagementClient.ConsumerInvitation(); // ConsumerInvitation | An invitation payload
apiInstance.consumerInvitationsRejectInvitation(location, apiVersion, invitation, (error, data, response) => {
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
 **location** | **String**| Location of the invitation | 
 **apiVersion** | **String**| The api version to use. | 
 **invitation** | [**ConsumerInvitation**](ConsumerInvitation.md)| An invitation payload | 

### Return type

[**ConsumerInvitation**](ConsumerInvitation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

