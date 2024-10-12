# UebermapsApiEndpoints.CollaboratorInvitationsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collaboratorInvitationsGet**](CollaboratorInvitationsApi.md#collaboratorInvitationsGet) | **GET** /collaborator_invitations | List your collaborator invitations
[**collaboratorInvitationsIdDelete**](CollaboratorInvitationsApi.md#collaboratorInvitationsIdDelete) | **DELETE** /collaborator_invitations/{id} | Delete collaborator invitation
[**collaboratorInvitationsIdGet**](CollaboratorInvitationsApi.md#collaboratorInvitationsIdGet) | **GET** /collaborator_invitations/{id} | Show collaborator invitation
[**collaboratorInvitationsIdPatch**](CollaboratorInvitationsApi.md#collaboratorInvitationsIdPatch) | **PATCH** /collaborator_invitations/{id} | Accept collaborator invitation.
[**collaboratorInvitationsPost**](CollaboratorInvitationsApi.md#collaboratorInvitationsPost) | **POST** /collaborator_invitations | Invite user to collaborate on map



## collaboratorInvitationsGet

> [CollaboratorInvitation] collaboratorInvitationsGet()

List your collaborator invitations

List your collaborator invitations.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorInvitationsApi();
apiInstance.collaboratorInvitationsGet((error, data, response) => {
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

[**[CollaboratorInvitation]**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collaboratorInvitationsIdDelete

> CollaboratorInvitation collaboratorInvitationsIdDelete(id)

Delete collaborator invitation

Delete collaborator invitation.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorInvitationsApi();
let id = 56; // Number | Collaborator invitation id
apiInstance.collaboratorInvitationsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| Collaborator invitation id | 

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collaboratorInvitationsIdGet

> CollaboratorInvitation collaboratorInvitationsIdGet(id)

Show collaborator invitation

Show collaborator invitation

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorInvitationsApi();
let id = 56; // Number | Collaborator invitation id
apiInstance.collaboratorInvitationsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Collaborator invitation id | 

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collaboratorInvitationsIdPatch

> CollaboratorInvitation collaboratorInvitationsIdPatch(id)

Accept collaborator invitation.

Accept collaborator invitation.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorInvitationsApi();
let id = 56; // Number | Collaborator invitation id
apiInstance.collaboratorInvitationsIdPatch(id, (error, data, response) => {
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
 **id** | **Number**| Collaborator invitation id | 

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## collaboratorInvitationsPost

> CollaboratorInvitation collaboratorInvitationsPost(opts)

Invite user to collaborate on map

Invite user to collaborate on map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorInvitationsApi();
let opts = {
  'body': new UebermapsApiEndpoints.CollaboratorInvitationCreate() // CollaboratorInvitationCreate | Supply map_id and either a comma separated list of user_ids or emails. Optionally you can provide a 'is_admin' parameter with 'true' or 'false' to give the invited users admin privileges.
};
apiInstance.collaboratorInvitationsPost(opts, (error, data, response) => {
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
 **body** | [**CollaboratorInvitationCreate**](CollaboratorInvitationCreate.md)| Supply map_id and either a comma separated list of user_ids or emails. Optionally you can provide a &#39;is_admin&#39; parameter with &#39;true&#39; or &#39;false&#39; to give the invited users admin privileges. | [optional] 

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

