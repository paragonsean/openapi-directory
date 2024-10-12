# FinSpacePublicApi.DefaultApi

All URIs are relative to *http://finspace-api.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateUserToPermissionGroup**](DefaultApi.md#associateUserToPermissionGroup) | **POST** /permission-group/{permissionGroupId}/users/{userId} | 
[**createChangeset**](DefaultApi.md#createChangeset) | **POST** /datasets/{datasetId}/changesetsv2 | 
[**createDataView**](DefaultApi.md#createDataView) | **POST** /datasets/{datasetId}/dataviewsv2 | 
[**createDataset**](DefaultApi.md#createDataset) | **POST** /datasetsv2 | 
[**createPermissionGroup**](DefaultApi.md#createPermissionGroup) | **POST** /permission-group | 
[**createUser**](DefaultApi.md#createUser) | **POST** /user | 
[**deleteDataset**](DefaultApi.md#deleteDataset) | **DELETE** /datasetsv2/{datasetId} | 
[**deletePermissionGroup**](DefaultApi.md#deletePermissionGroup) | **DELETE** /permission-group/{permissionGroupId} | 
[**disableUser**](DefaultApi.md#disableUser) | **POST** /user/{userId}/disable | 
[**disassociateUserFromPermissionGroup**](DefaultApi.md#disassociateUserFromPermissionGroup) | **DELETE** /permission-group/{permissionGroupId}/users/{userId} | 
[**enableUser**](DefaultApi.md#enableUser) | **POST** /user/{userId}/enable | 
[**getChangeset**](DefaultApi.md#getChangeset) | **GET** /datasets/{datasetId}/changesetsv2/{changesetId} | 
[**getDataView**](DefaultApi.md#getDataView) | **GET** /datasets/{datasetId}/dataviewsv2/{dataviewId} | 
[**getDataset**](DefaultApi.md#getDataset) | **GET** /datasetsv2/{datasetId} | 
[**getExternalDataViewAccessDetails**](DefaultApi.md#getExternalDataViewAccessDetails) | **POST** /datasets/{datasetId}/dataviewsv2/{dataviewId}/external-access-details | 
[**getPermissionGroup**](DefaultApi.md#getPermissionGroup) | **GET** /permission-group/{permissionGroupId} | 
[**getProgrammaticAccessCredentials**](DefaultApi.md#getProgrammaticAccessCredentials) | **GET** /credentials/programmatic#environmentId | 
[**getUser**](DefaultApi.md#getUser) | **GET** /user/{userId} | 
[**getWorkingLocation**](DefaultApi.md#getWorkingLocation) | **POST** /workingLocationV1 | 
[**listChangesets**](DefaultApi.md#listChangesets) | **GET** /datasets/{datasetId}/changesetsv2 | 
[**listDataViews**](DefaultApi.md#listDataViews) | **GET** /datasets/{datasetId}/dataviewsv2 | 
[**listDatasets**](DefaultApi.md#listDatasets) | **GET** /datasetsv2 | 
[**listPermissionGroups**](DefaultApi.md#listPermissionGroups) | **GET** /permission-group#maxResults | 
[**listPermissionGroupsByUser**](DefaultApi.md#listPermissionGroupsByUser) | **GET** /user/{userId}/permission-groups#maxResults | 
[**listUsers**](DefaultApi.md#listUsers) | **GET** /user#maxResults | 
[**listUsersByPermissionGroup**](DefaultApi.md#listUsersByPermissionGroup) | **GET** /permission-group/{permissionGroupId}/users#maxResults | 
[**resetUserPassword**](DefaultApi.md#resetUserPassword) | **POST** /user/{userId}/password | 
[**updateChangeset**](DefaultApi.md#updateChangeset) | **PUT** /datasets/{datasetId}/changesetsv2/{changesetId} | 
[**updateDataset**](DefaultApi.md#updateDataset) | **PUT** /datasetsv2/{datasetId} | 
[**updatePermissionGroup**](DefaultApi.md#updatePermissionGroup) | **PUT** /permission-group/{permissionGroupId} | 
[**updateUser**](DefaultApi.md#updateUser) | **PUT** /user/{userId} | 



## associateUserToPermissionGroup

> AssociateUserToPermissionGroupResponse associateUserToPermissionGroup(permissionGroupId, userId, associateUserToPermissionGroupRequest, opts)



Adds a user account to a permission group to grant permissions for actions a user can perform in FinSpace.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let permissionGroupId = "permissionGroupId_example"; // String | The unique identifier for the permission group.
let userId = "userId_example"; // String | The unique identifier for the user.
let associateUserToPermissionGroupRequest = new FinSpacePublicApi.AssociateUserToPermissionGroupRequest(); // AssociateUserToPermissionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateUserToPermissionGroup(permissionGroupId, userId, associateUserToPermissionGroupRequest, opts, (error, data, response) => {
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
 **permissionGroupId** | **String**| The unique identifier for the permission group. | 
 **userId** | **String**| The unique identifier for the user. | 
 **associateUserToPermissionGroupRequest** | [**AssociateUserToPermissionGroupRequest**](AssociateUserToPermissionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateUserToPermissionGroupResponse**](AssociateUserToPermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChangeset

> CreateChangesetResponse createChangeset(datasetId, createChangesetRequest, opts)



Creates a new Changeset in a FinSpace Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier for the FinSpace Dataset where the Changeset will be created. 
let createChangesetRequest = new FinSpacePublicApi.CreateChangesetRequest(); // CreateChangesetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChangeset(datasetId, createChangesetRequest, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier for the FinSpace Dataset where the Changeset will be created.  | 
 **createChangesetRequest** | [**CreateChangesetRequest**](CreateChangesetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChangesetResponse**](CreateChangesetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataView

> CreateDataViewResponse createDataView(datasetId, createDataViewRequest, opts)



Creates a Dataview for a Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique Dataset identifier that is used to create a Dataview.
let createDataViewRequest = new FinSpacePublicApi.CreateDataViewRequest(); // CreateDataViewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDataView(datasetId, createDataViewRequest, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique Dataset identifier that is used to create a Dataview. | 
 **createDataViewRequest** | [**CreateDataViewRequest**](CreateDataViewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDataViewResponse**](CreateDataViewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDataset

> CreateDatasetResponse createDataset(createDatasetRequest, opts)



Creates a new FinSpace Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let createDatasetRequest = new FinSpacePublicApi.CreateDatasetRequest(); // CreateDatasetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDataset(createDatasetRequest, opts, (error, data, response) => {
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
 **createDatasetRequest** | [**CreateDatasetRequest**](CreateDatasetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDatasetResponse**](CreateDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPermissionGroup

> CreatePermissionGroupResponse createPermissionGroup(createPermissionGroupRequest, opts)



Creates a group of permissions for various actions that a user can perform in FinSpace.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let createPermissionGroupRequest = new FinSpacePublicApi.CreatePermissionGroupRequest(); // CreatePermissionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPermissionGroup(createPermissionGroupRequest, opts, (error, data, response) => {
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
 **createPermissionGroupRequest** | [**CreatePermissionGroupRequest**](CreatePermissionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePermissionGroupResponse**](CreatePermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> CreateUserResponse createUser(createUserRequest, opts)



Creates a new user in FinSpace.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let createUserRequest = new FinSpacePublicApi.CreateUserRequest(); // CreateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUser(createUserRequest, opts, (error, data, response) => {
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
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDataset

> DeleteDatasetResponse deleteDataset(datasetId, opts)



Deletes a FinSpace Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier of the Dataset to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A token that ensures idempotency. This token expires in 10 minutes.
};
apiInstance.deleteDataset(datasetId, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier of the Dataset to be deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A token that ensures idempotency. This token expires in 10 minutes. | [optional] 

### Return type

[**DeleteDatasetResponse**](DeleteDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePermissionGroup

> DeletePermissionGroupResponse deletePermissionGroup(permissionGroupId, opts)



Deletes a permission group. This action is irreversible.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let permissionGroupId = "permissionGroupId_example"; // String | The unique identifier for the permission group that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A token that ensures idempotency. This token expires in 10 minutes.
};
apiInstance.deletePermissionGroup(permissionGroupId, opts, (error, data, response) => {
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
 **permissionGroupId** | **String**| The unique identifier for the permission group that you want to delete. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A token that ensures idempotency. This token expires in 10 minutes. | [optional] 

### Return type

[**DeletePermissionGroupResponse**](DeletePermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableUser

> DisableUserResponse disableUser(userId, associateUserToPermissionGroupRequest, opts)



Denies access to the FinSpace web application and API for the specified user.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let userId = "userId_example"; // String | The unique identifier for the user account that you want to disable.
let associateUserToPermissionGroupRequest = new FinSpacePublicApi.AssociateUserToPermissionGroupRequest(); // AssociateUserToPermissionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disableUser(userId, associateUserToPermissionGroupRequest, opts, (error, data, response) => {
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
 **userId** | **String**| The unique identifier for the user account that you want to disable. | 
 **associateUserToPermissionGroupRequest** | [**AssociateUserToPermissionGroupRequest**](AssociateUserToPermissionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisableUserResponse**](DisableUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateUserFromPermissionGroup

> DisassociateUserFromPermissionGroupResponse disassociateUserFromPermissionGroup(permissionGroupId, userId, opts)



Removes a user account from a permission group.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let permissionGroupId = "permissionGroupId_example"; // String | The unique identifier for the permission group.
let userId = "userId_example"; // String | The unique identifier for the user.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'clientToken': "clientToken_example" // String | A token that ensures idempotency. This token expires in 10 minutes.
};
apiInstance.disassociateUserFromPermissionGroup(permissionGroupId, userId, opts, (error, data, response) => {
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
 **permissionGroupId** | **String**| The unique identifier for the permission group. | 
 **userId** | **String**| The unique identifier for the user. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **clientToken** | **String**| A token that ensures idempotency. This token expires in 10 minutes. | [optional] 

### Return type

[**DisassociateUserFromPermissionGroupResponse**](DisassociateUserFromPermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableUser

> EnableUserResponse enableUser(userId, associateUserToPermissionGroupRequest, opts)



 Allows the specified user to access the FinSpace web application and API.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let userId = "userId_example"; // String | The unique identifier for the user account that you want to enable.
let associateUserToPermissionGroupRequest = new FinSpacePublicApi.AssociateUserToPermissionGroupRequest(); // AssociateUserToPermissionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.enableUser(userId, associateUserToPermissionGroupRequest, opts, (error, data, response) => {
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
 **userId** | **String**| The unique identifier for the user account that you want to enable. | 
 **associateUserToPermissionGroupRequest** | [**AssociateUserToPermissionGroupRequest**](AssociateUserToPermissionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**EnableUserResponse**](EnableUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getChangeset

> GetChangesetResponse getChangeset(datasetId, changesetId, opts)



Get information about a Changeset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier for the FinSpace Dataset where the Changeset is created.
let changesetId = "changesetId_example"; // String | The unique identifier of the Changeset for which to get data.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChangeset(datasetId, changesetId, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier for the FinSpace Dataset where the Changeset is created. | 
 **changesetId** | **String**| The unique identifier of the Changeset for which to get data. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChangesetResponse**](GetChangesetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataView

> GetDataViewResponse getDataView(dataviewId, datasetId, opts)



Gets information about a Dataview.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let dataviewId = "dataviewId_example"; // String | The unique identifier for the Dataview.
let datasetId = "datasetId_example"; // String | The unique identifier for the Dataset used in the Dataview.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDataView(dataviewId, datasetId, opts, (error, data, response) => {
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
 **dataviewId** | **String**| The unique identifier for the Dataview. | 
 **datasetId** | **String**| The unique identifier for the Dataset used in the Dataview. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDataViewResponse**](GetDataViewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDataset

> GetDatasetResponse getDataset(datasetId, opts)



Returns information about a Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier for a Dataset.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDataset(datasetId, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier for a Dataset. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDatasetResponse**](GetDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExternalDataViewAccessDetails

> GetExternalDataViewAccessDetailsResponse getExternalDataViewAccessDetails(dataviewId, datasetId, opts)



&lt;p&gt;Returns the credentials to access the external Dataview from an S3 location. To call this API:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must retrieve the programmatic credentials.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must be a member of a FinSpace user group, where the dataset that you want to access has &lt;code&gt;Read Dataset Data&lt;/code&gt; permissions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let dataviewId = "dataviewId_example"; // String | The unique identifier for the Dataview that you want to access.
let datasetId = "datasetId_example"; // String | The unique identifier for the Dataset.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExternalDataViewAccessDetails(dataviewId, datasetId, opts, (error, data, response) => {
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
 **dataviewId** | **String**| The unique identifier for the Dataview that you want to access. | 
 **datasetId** | **String**| The unique identifier for the Dataset. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExternalDataViewAccessDetailsResponse**](GetExternalDataViewAccessDetailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPermissionGroup

> GetPermissionGroupResponse getPermissionGroup(permissionGroupId, opts)



Retrieves the details of a specific permission group.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let permissionGroupId = "permissionGroupId_example"; // String | The unique identifier for the permission group.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPermissionGroup(permissionGroupId, opts, (error, data, response) => {
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
 **permissionGroupId** | **String**| The unique identifier for the permission group. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPermissionGroupResponse**](GetPermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProgrammaticAccessCredentials

> GetProgrammaticAccessCredentialsResponse getProgrammaticAccessCredentials(environmentId, opts)



Request programmatic credentials to use with FinSpace SDK.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let environmentId = "environmentId_example"; // String | The FinSpace environment identifier.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'durationInMinutes': 56 // Number | The time duration in which the credentials remain valid. 
};
apiInstance.getProgrammaticAccessCredentials(environmentId, opts, (error, data, response) => {
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
 **environmentId** | **String**| The FinSpace environment identifier. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **durationInMinutes** | **Number**| The time duration in which the credentials remain valid.  | [optional] 

### Return type

[**GetProgrammaticAccessCredentialsResponse**](GetProgrammaticAccessCredentialsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> GetUserResponse getUser(userId, opts)



Retrieves details for a specific user.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let userId = "userId_example"; // String | The unique identifier of the user to get data for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUser(userId, opts, (error, data, response) => {
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
 **userId** | **String**| The unique identifier of the user to get data for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkingLocation

> GetWorkingLocationResponse getWorkingLocation(getWorkingLocationRequest, opts)



A temporary Amazon S3 location, where you can copy your files from a source location to stage or use as a scratch space in FinSpace notebook.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let getWorkingLocationRequest = new FinSpacePublicApi.GetWorkingLocationRequest(); // GetWorkingLocationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWorkingLocation(getWorkingLocationRequest, opts, (error, data, response) => {
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
 **getWorkingLocationRequest** | [**GetWorkingLocationRequest**](GetWorkingLocationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWorkingLocationResponse**](GetWorkingLocationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listChangesets

> ListChangesetsResponse listChangesets(datasetId, opts)



Lists the FinSpace Changesets for a Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier for the FinSpace Dataset to which the Changeset belongs.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results per page.
  'nextToken': "nextToken_example" // String | A token that indicates where a results page should begin.
};
apiInstance.listChangesets(datasetId, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier for the FinSpace Dataset to which the Changeset belongs. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results per page. | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 

### Return type

[**ListChangesetsResponse**](ListChangesetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDataViews

> ListDataViewsResponse listDataViews(datasetId, opts)



Lists all available Dataviews for a Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier of the Dataset for which to retrieve Dataviews.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token that indicates where a results page should begin.
  'maxResults': 56 // Number | The maximum number of results per page.
};
apiInstance.listDataViews(datasetId, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier of the Dataset for which to retrieve Dataviews. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 
 **maxResults** | **Number**| The maximum number of results per page. | [optional] 

### Return type

[**ListDataViewsResponse**](ListDataViewsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDatasets

> ListDatasetsResponse listDatasets(opts)



Lists all of the active Datasets that a user has access to.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token that indicates where a results page should begin.
  'maxResults': 56 // Number | The maximum number of results per page.
};
apiInstance.listDatasets(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 
 **maxResults** | **Number**| The maximum number of results per page. | [optional] 

### Return type

[**ListDatasetsResponse**](ListDatasetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPermissionGroups

> ListPermissionGroupsResponse listPermissionGroups(maxResults, opts)



Lists all available permission groups in FinSpace.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let maxResults = 56; // Number | The maximum number of results per page.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | A token that indicates where a results page should begin.
};
apiInstance.listPermissionGroups(maxResults, opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results per page. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 

### Return type

[**ListPermissionGroupsResponse**](ListPermissionGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPermissionGroupsByUser

> ListPermissionGroupsByUserResponse listPermissionGroupsByUser(userId, maxResults, opts)



Lists all the permission groups that are associated with a specific user account.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let userId = "userId_example"; // String | The unique identifier for the user.
let maxResults = 56; // Number | The maximum number of results per page.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | A token that indicates where a results page should begin.
};
apiInstance.listPermissionGroupsByUser(userId, maxResults, opts, (error, data, response) => {
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
 **userId** | **String**| The unique identifier for the user. | 
 **maxResults** | **Number**| The maximum number of results per page. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 

### Return type

[**ListPermissionGroupsByUserResponse**](ListPermissionGroupsByUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> ListUsersResponse listUsers(maxResults, opts)



Lists all available user accounts in FinSpace.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let maxResults = 56; // Number | The maximum number of results per page.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | A token that indicates where a results page should begin.
};
apiInstance.listUsers(maxResults, opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results per page. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsersByPermissionGroup

> ListUsersByPermissionGroupResponse listUsersByPermissionGroup(permissionGroupId, maxResults, opts)



Lists details of all the users in a specific permission group.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let permissionGroupId = "permissionGroupId_example"; // String | The unique identifier for the permission group.
let maxResults = 56; // Number | The maximum number of results per page.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | A token that indicates where a results page should begin.
};
apiInstance.listUsersByPermissionGroup(permissionGroupId, maxResults, opts, (error, data, response) => {
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
 **permissionGroupId** | **String**| The unique identifier for the permission group. | 
 **maxResults** | **Number**| The maximum number of results per page. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that indicates where a results page should begin. | [optional] 

### Return type

[**ListUsersByPermissionGroupResponse**](ListUsersByPermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetUserPassword

> ResetUserPasswordResponse resetUserPassword(userId, associateUserToPermissionGroupRequest, opts)



Resets the password for a specified user ID and generates a temporary one. Only a superuser can reset password for other users. Resetting the password immediately invalidates the previous password associated with the user.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let userId = "userId_example"; // String | The unique identifier of the user that a temporary password is requested for.
let associateUserToPermissionGroupRequest = new FinSpacePublicApi.AssociateUserToPermissionGroupRequest(); // AssociateUserToPermissionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resetUserPassword(userId, associateUserToPermissionGroupRequest, opts, (error, data, response) => {
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
 **userId** | **String**| The unique identifier of the user that a temporary password is requested for. | 
 **associateUserToPermissionGroupRequest** | [**AssociateUserToPermissionGroupRequest**](AssociateUserToPermissionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResetUserPasswordResponse**](ResetUserPasswordResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChangeset

> UpdateChangesetResponse updateChangeset(datasetId, changesetId, updateChangesetRequest, opts)



Updates a FinSpace Changeset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier for the FinSpace Dataset in which the Changeset is created.
let changesetId = "changesetId_example"; // String | The unique identifier for the Changeset to update.
let updateChangesetRequest = new FinSpacePublicApi.UpdateChangesetRequest(); // UpdateChangesetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChangeset(datasetId, changesetId, updateChangesetRequest, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier for the FinSpace Dataset in which the Changeset is created. | 
 **changesetId** | **String**| The unique identifier for the Changeset to update. | 
 **updateChangesetRequest** | [**UpdateChangesetRequest**](UpdateChangesetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChangesetResponse**](UpdateChangesetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDataset

> UpdateDatasetResponse updateDataset(datasetId, updateDatasetRequest, opts)



Updates a FinSpace Dataset.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let datasetId = "datasetId_example"; // String | The unique identifier for the Dataset to update.
let updateDatasetRequest = new FinSpacePublicApi.UpdateDatasetRequest(); // UpdateDatasetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDataset(datasetId, updateDatasetRequest, opts, (error, data, response) => {
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
 **datasetId** | **String**| The unique identifier for the Dataset to update. | 
 **updateDatasetRequest** | [**UpdateDatasetRequest**](UpdateDatasetRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateDatasetResponse**](UpdateDatasetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePermissionGroup

> UpdatePermissionGroupResponse updatePermissionGroup(permissionGroupId, updatePermissionGroupRequest, opts)



Modifies the details of a permission group. You cannot modify a &lt;code&gt;permissionGroupID&lt;/code&gt;.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let permissionGroupId = "permissionGroupId_example"; // String | The unique identifier for the permission group to update.
let updatePermissionGroupRequest = new FinSpacePublicApi.UpdatePermissionGroupRequest(); // UpdatePermissionGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePermissionGroup(permissionGroupId, updatePermissionGroupRequest, opts, (error, data, response) => {
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
 **permissionGroupId** | **String**| The unique identifier for the permission group to update. | 
 **updatePermissionGroupRequest** | [**UpdatePermissionGroupRequest**](UpdatePermissionGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePermissionGroupResponse**](UpdatePermissionGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUser

> UpdateUserResponse updateUser(userId, updateUserRequest, opts)



Modifies the details of the specified user account. You cannot update the &lt;code&gt;userId&lt;/code&gt; for a user.

### Example

```javascript
import FinSpacePublicApi from 'fin_space_public_api';
let defaultClient = FinSpacePublicApi.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new FinSpacePublicApi.DefaultApi();
let userId = "userId_example"; // String | The unique identifier for the user account to update.
let updateUserRequest = new FinSpacePublicApi.UpdateUserRequest(); // UpdateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUser(userId, updateUserRequest, opts, (error, data, response) => {
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
 **userId** | **String**| The unique identifier for the user account to update. | 
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

