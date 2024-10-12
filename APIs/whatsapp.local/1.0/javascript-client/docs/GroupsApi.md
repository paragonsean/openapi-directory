# WhatsAppBusinessApi.GroupsApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](GroupsApi.md#createGroup) | **POST** /groups | Create-Group
[**deleteGroupIcon**](GroupsApi.md#deleteGroupIcon) | **DELETE** /groups/{GroupId}/icon | Delete-Group-Icon
[**deleteGroupInvite**](GroupsApi.md#deleteGroupInvite) | **DELETE** /groups/{GroupId}/invite | Delete-Group-Invite
[**demoteGroupAdmin**](GroupsApi.md#demoteGroupAdmin) | **DELETE** /groups/{GroupId}/admins | Demote-Group-Admin
[**getAllGroups**](GroupsApi.md#getAllGroups) | **GET** /groups | Get-All-Groups
[**getGroupIconBinary**](GroupsApi.md#getGroupIconBinary) | **GET** /groups/{GroupId}/icon | Get-Group-Icon-Binary
[**getGroupInfo**](GroupsApi.md#getGroupInfo) | **GET** /groups/{GroupId} | Get-Group-Info
[**getGroupInvite**](GroupsApi.md#getGroupInvite) | **GET** /groups/{GroupId}/invite | Get-Group-Invite
[**leaveGroup**](GroupsApi.md#leaveGroup) | **POST** /groups/{GroupId}/leave | Leave-Group
[**promoteToGroupAdmin**](GroupsApi.md#promoteToGroupAdmin) | **PATCH** /groups/{GroupId}/admins | Promote-To-Group-Admin
[**removeGroupParticipant**](GroupsApi.md#removeGroupParticipant) | **DELETE** /groups/{GroupId}/participants | Remove-Group-Participant
[**setGroupIcon**](GroupsApi.md#setGroupIcon) | **POST** /groups/{GroupId}/icon | Set-Group-Icon
[**updateGroupInfo**](GroupsApi.md#updateGroupInfo) | **PUT** /groups/{GroupId} | Update-Group-Info



## createGroup

> GroupsResponse createGroup(createGroupRequestBody)

Create-Group

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let createGroupRequestBody = {"subject":"<Group Subject>"}; // CreateGroupRequestBody | 
apiInstance.createGroup(createGroupRequestBody, (error, data, response) => {
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
 **createGroupRequestBody** | [**CreateGroupRequestBody**](CreateGroupRequestBody.md)|  | 

### Return type

[**GroupsResponse**](GroupsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteGroupIcon

> deleteGroupIcon(groupId, file)

Delete-Group-Icon

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
let file = "/path/to/file"; // File | 
apiInstance.deleteGroupIcon(groupId, file, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **file** | **File**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## deleteGroupInvite

> deleteGroupInvite(groupId)

Delete-Group-Invite

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
apiInstance.deleteGroupInvite(groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## demoteGroupAdmin

> demoteGroupAdmin(groupId, groupAdminRequestBody)

Demote-Group-Admin

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
let groupAdminRequestBody = {"wa_ids":["<Recipient WA-ID, from Contacts API>"]}; // GroupAdminRequestBody | 
apiInstance.demoteGroupAdmin(groupId, groupAdminRequestBody, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **groupAdminRequestBody** | [**GroupAdminRequestBody**](GroupAdminRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getAllGroups

> GroupsResponse getAllGroups()

Get-All-Groups

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
apiInstance.getAllGroups((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GroupsResponse**](GroupsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupIconBinary

> getGroupIconBinary(groupId)

Get-Group-Icon-Binary

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
apiInstance.getGroupIconBinary(groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGroupInfo

> GroupResponse getGroupInfo(groupId)

Get-Group-Info

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
apiInstance.getGroupInfo(groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

[**GroupResponse**](GroupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupInvite

> GroupInviteResponse getGroupInvite(groupId)

Get-Group-Invite

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
apiInstance.getGroupInvite(groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

[**GroupInviteResponse**](GroupInviteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## leaveGroup

> leaveGroup(groupId)

Leave-Group

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
apiInstance.leaveGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## promoteToGroupAdmin

> promoteToGroupAdmin(groupId, groupAdminRequestBody)

Promote-To-Group-Admin

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
let groupAdminRequestBody = {"wa_ids":["<Recipient WA-ID, from Contacts API>"]}; // GroupAdminRequestBody | 
apiInstance.promoteToGroupAdmin(groupId, groupAdminRequestBody, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **groupAdminRequestBody** | [**GroupAdminRequestBody**](GroupAdminRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## removeGroupParticipant

> removeGroupParticipant(groupId, removeGroupParticipantRequestBody)

Remove-Group-Participant

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
let removeGroupParticipantRequestBody = {"wa_ids":["{{Recipient-WA-ID}}"]}; // RemoveGroupParticipantRequestBody | 
apiInstance.removeGroupParticipant(groupId, removeGroupParticipantRequestBody, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **removeGroupParticipantRequestBody** | [**RemoveGroupParticipantRequestBody**](RemoveGroupParticipantRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## setGroupIcon

> setGroupIcon(groupId, file)

Set-Group-Icon

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
let file = "/path/to/file"; // File | 
apiInstance.setGroupIcon(groupId, file, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **file** | **File**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## updateGroupInfo

> updateGroupInfo(groupId, updateGroupInfoRequestBody)

Update-Group-Info

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.GroupsApi();
let groupId = "groupId_example"; // String | 
let updateGroupInfoRequestBody = {"subject":"<New Group Subject>"}; // UpdateGroupInfoRequestBody | 
apiInstance.updateGroupInfo(groupId, updateGroupInfoRequestBody, (error, data, response) => {
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
 **groupId** | **String**|  | 
 **updateGroupInfoRequestBody** | [**UpdateGroupInfoRequestBody**](UpdateGroupInfoRequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

