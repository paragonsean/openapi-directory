# AgcoApi.UpdateGroupsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2UpdateGroupsIDGet**](UpdateGroupsApi.md#apiV2UpdateGroupsIDGet) | **GET** /api/v2/UpdateGroups/{ID} | Get a specific Update Group by ID.
[**updateGroupsAddUpdateGroupUser**](UpdateGroupsApi.md#updateGroupsAddUpdateGroupUser) | **POST** /api/v2/UpdateGroups/{id}/Users/{userID} | Add an updateGroup that a user can see.
[**updateGroupsDelete**](UpdateGroupsApi.md#updateGroupsDelete) | **DELETE** /api/v2/UpdateGroups/{ID} | Delete an Update Group.
[**updateGroupsGet**](UpdateGroupsApi.md#updateGroupsGet) | **GET** /api/v2/UpdateGroups | Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.
[**updateGroupsGetUpdateGroupBundles**](UpdateGroupsApi.md#updateGroupsGetUpdateGroupBundles) | **GET** /api/v2/UpdateGroups/{ID}/Bundles | Get a list of bundles for UpdateGroup.
[**updateGroupsPost**](UpdateGroupsApi.md#updateGroupsPost) | **POST** /api/v2/UpdateGroups | Add a new Update Group.  The report field is a string that has a dot based request for a specific piece of submitted data.
[**updateGroupsPut**](UpdateGroupsApi.md#updateGroupsPut) | **PUT** /api/v2/UpdateGroups/{ID} | Modify an Update Group.
[**updateGroupsRemoveUpdateGroupUser**](UpdateGroupsApi.md#updateGroupsRemoveUpdateGroupUser) | **DELETE** /api/v2/UpdateGroups/{id}/Users/{userID} | Deletes an update group a user could see.



## apiV2UpdateGroupsIDGet

> UpdateSystemModelsUpdateGroup apiV2UpdateGroupsIDGet(ID)

Get a specific Update Group by ID.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let ID = "ID_example"; // String | The ID of the Update Group
apiInstance.apiV2UpdateGroupsIDGet(ID, (error, data, response) => {
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
 **ID** | **String**| The ID of the Update Group | 

### Return type

[**UpdateSystemModelsUpdateGroup**](UpdateSystemModelsUpdateGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## updateGroupsAddUpdateGroupUser

> updateGroupsAddUpdateGroupUser(id, userID)

Add an updateGroup that a user can see.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let id = "id_example"; // String | The ID of the update group
let userID = 56; // Number | The userID to link to the update group
apiInstance.updateGroupsAddUpdateGroupUser(id, userID, (error, data, response) => {
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
 **id** | **String**| The ID of the update group | 
 **userID** | **Number**| The userID to link to the update group | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateGroupsDelete

> updateGroupsDelete(ID)

Delete an Update Group.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let ID = "ID_example"; // String | The ID of the Update Group to Delete
apiInstance.updateGroupsDelete(ID, (error, data, response) => {
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
 **ID** | **String**| The ID of the Update Group to Delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateGroupsGet

> APIPagedResponseUpdateSystemModelsUpdateGroup updateGroupsGet(opts)

Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'userID': 56 // Number | Optional. The user ID to sort update groups by the user's access
};
apiInstance.updateGroupsGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 
 **userID** | **Number**| Optional. The user ID to sort update groups by the user&#39;s access | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroup**](APIPagedResponseUpdateSystemModelsUpdateGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## updateGroupsGetUpdateGroupBundles

> APIPagedResponseUpdateSystemModelsBundle updateGroupsGetUpdateGroupBundles(ID, includeInactive, opts)

Get a list of bundles for UpdateGroup.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let ID = "ID_example"; // String | The UpdateGroupID
let includeInactive = true; // Boolean | Include Inactive Bundles (true|false)
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.updateGroupsGetUpdateGroupBundles(ID, includeInactive, opts, (error, data, response) => {
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
 **ID** | **String**| The UpdateGroupID | 
 **includeInactive** | **Boolean**| Include Inactive Bundles (true|false) | 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsBundle**](APIPagedResponseUpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## updateGroupsPost

> String updateGroupsPost(updateSystemModelsUpdateGroup)

Add a new Update Group.  The report field is a string that has a dot based request for a specific piece of submitted data.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let updateSystemModelsUpdateGroup = new AgcoApi.UpdateSystemModelsUpdateGroup(); // UpdateSystemModelsUpdateGroup | 
apiInstance.updateGroupsPost(updateSystemModelsUpdateGroup, (error, data, response) => {
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
 **updateSystemModelsUpdateGroup** | [**UpdateSystemModelsUpdateGroup**](UpdateSystemModelsUpdateGroup.md)|  | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## updateGroupsPut

> updateGroupsPut(ID, updateSystemModelsUpdateGroup)

Modify an Update Group.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let ID = "ID_example"; // String | ID of the Update Group
let updateSystemModelsUpdateGroup = new AgcoApi.UpdateSystemModelsUpdateGroup(); // UpdateSystemModelsUpdateGroup | The Update Group to update.
apiInstance.updateGroupsPut(ID, updateSystemModelsUpdateGroup, (error, data, response) => {
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
 **ID** | **String**| ID of the Update Group | 
 **updateSystemModelsUpdateGroup** | [**UpdateSystemModelsUpdateGroup**](UpdateSystemModelsUpdateGroup.md)| The Update Group to update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## updateGroupsRemoveUpdateGroupUser

> updateGroupsRemoveUpdateGroupUser(id, userID)

Deletes an update group a user could see.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupsApi();
let id = "id_example"; // String | The ID of the update group
let userID = 56; // Number | The userID to link to the update group
apiInstance.updateGroupsRemoveUpdateGroupUser(id, userID, (error, data, response) => {
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
 **id** | **String**| The ID of the update group | 
 **userID** | **Number**| The userID to link to the update group | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

