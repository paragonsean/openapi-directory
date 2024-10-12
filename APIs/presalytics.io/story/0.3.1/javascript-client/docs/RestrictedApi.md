# Story.RestrictedApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collaboratorsPost**](RestrictedApi.md#collaboratorsPost) | **POST** /collaborators | Collborators: Bulk Update (Admin Only)



## collaboratorsPost

> [PermissionType] collaboratorsPost(collaboratorBulkUpdateRequest)

Collborators: Bulk Update (Admin Only)

Allows for bulk updates on collaborator metadata.  Restricted to internal admins

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.RestrictedApi();
let collaboratorBulkUpdateRequest = new Story.CollaboratorBulkUpdateRequest(); // CollaboratorBulkUpdateRequest | parameters to identify an update a collaborator across multiple stories
apiInstance.collaboratorsPost(collaboratorBulkUpdateRequest, (error, data, response) => {
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
 **collaboratorBulkUpdateRequest** | [**CollaboratorBulkUpdateRequest**](CollaboratorBulkUpdateRequest.md)| parameters to identify an update a collaborator across multiple stories | 

### Return type

[**[PermissionType]**](PermissionType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

