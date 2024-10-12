# UebermapsApiEndpoints.CollaboratorsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsIdCollaboratorsGet**](CollaboratorsApi.md#mapsIdCollaboratorsGet) | **GET** /maps/{id}/collaborators/ | List collaborators of a map
[**mapsIdCollaboratorsUserIdDelete**](CollaboratorsApi.md#mapsIdCollaboratorsUserIdDelete) | **DELETE** /maps/{id}/collaborators/{user_id} | Delete collaboration
[**mapsIdCollaboratorsUserIdPatch**](CollaboratorsApi.md#mapsIdCollaboratorsUserIdPatch) | **PATCH** /maps/{id}/collaborators/{user_id} | Update collaborator



## mapsIdCollaboratorsGet

> [Collaborator] mapsIdCollaboratorsGet(id)

List collaborators of a map

List collaborators of a map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorsApi();
let id = 56; // Number | Map id
apiInstance.mapsIdCollaboratorsGet(id, (error, data, response) => {
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
 **id** | **Number**| Map id | 

### Return type

[**[Collaborator]**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdCollaboratorsUserIdDelete

> Collaborator mapsIdCollaboratorsUserIdDelete(id, userId)

Delete collaboration

Delete collaboration.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorsApi();
let id = 56; // Number | map id
let userId = 56; // Number | user id
apiInstance.mapsIdCollaboratorsUserIdDelete(id, userId, (error, data, response) => {
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
 **id** | **Number**| map id | 
 **userId** | **Number**| user id | 

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdCollaboratorsUserIdPatch

> Collaborator mapsIdCollaboratorsUserIdPatch(id, userId, opts)

Update collaborator

Update collaborator. Wrap collaborator parameters in [collaborator]

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CollaboratorsApi();
let id = 56; // Number | map id
let userId = 56; // Number | user id
let opts = {
  'collaborator': new UebermapsApiEndpoints.CollaboratorEditable() // CollaboratorEditable | collaborator attributes
};
apiInstance.mapsIdCollaboratorsUserIdPatch(id, userId, opts, (error, data, response) => {
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
 **id** | **Number**| map id | 
 **userId** | **Number**| user id | 
 **collaborator** | [**CollaboratorEditable**](CollaboratorEditable.md)| collaborator attributes | [optional] 

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

