# IntuneResourceManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androidAddAppForMAMPolicy**](DefaultApi.md#androidAddAppForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/apps/{appName} | 
[**androidAddGroupForMAMPolicy**](DefaultApi.md#androidAddGroupForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/groups/{groupId} | 
[**androidCreateOrUpdateMAMPolicy**](DefaultApi.md#androidCreateOrUpdateMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} | 
[**androidDeleteAppForMAMPolicy**](DefaultApi.md#androidDeleteAppForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/apps/{appName} | 
[**androidDeleteGroupForMAMPolicy**](DefaultApi.md#androidDeleteGroupForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/groups/{groupId} | 
[**androidDeleteMAMPolicy**](DefaultApi.md#androidDeleteMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} | 
[**androidGetAppForMAMPolicy**](DefaultApi.md#androidGetAppForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/AndroidPolicies/{policyName}/apps | 
[**androidGetGroupsForMAMPolicy**](DefaultApi.md#androidGetGroupsForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/groups | 
[**androidGetMAMPolicies**](DefaultApi.md#androidGetMAMPolicies) | **GET** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies | 
[**androidGetMAMPolicyByName**](DefaultApi.md#androidGetMAMPolicyByName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} | 
[**androidPatchMAMPolicy**](DefaultApi.md#androidPatchMAMPolicy) | **PATCH** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} | 
[**getApps**](DefaultApi.md#getApps) | **GET** /providers/Microsoft.Intune/locations/{hostName}/apps | 
[**getLocationByHostName**](DefaultApi.md#getLocationByHostName) | **GET** /providers/Microsoft.Intune/locations/hostName | 
[**getLocations**](DefaultApi.md#getLocations) | **GET** /providers/Microsoft.Intune/locations | 
[**getMAMFlaggedUserByName**](DefaultApi.md#getMAMFlaggedUserByName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/flaggedUsers/{userName} | 
[**getMAMFlaggedUsers**](DefaultApi.md#getMAMFlaggedUsers) | **GET** /providers/Microsoft.Intune/locations/{hostName}/flaggedUsers | 
[**getMAMStatuses**](DefaultApi.md#getMAMStatuses) | **GET** /providers/Microsoft.Intune/locations/{hostName}/statuses/default | 
[**getMAMUserDeviceByDeviceName**](DefaultApi.md#getMAMUserDeviceByDeviceName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/users/{userName}/devices/{deviceName} | 
[**getMAMUserDevices**](DefaultApi.md#getMAMUserDevices) | **GET** /providers/Microsoft.Intune/locations/{hostName}/users/{userName}/devices | 
[**getMAMUserFlaggedEnrolledApps**](DefaultApi.md#getMAMUserFlaggedEnrolledApps) | **GET** /providers/Microsoft.Intune/locations/{hostName}/flaggedUsers/{userName}/flaggedEnrolledApps | 
[**getOperationResults**](DefaultApi.md#getOperationResults) | **GET** /providers/Microsoft.Intune/locations/{hostName}/operationResults | 
[**iosAddAppForMAMPolicy**](DefaultApi.md#iosAddAppForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps/{appName} | 
[**iosAddGroupForMAMPolicy**](DefaultApi.md#iosAddGroupForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups/{groupId} | 
[**iosCreateOrUpdateMAMPolicy**](DefaultApi.md#iosCreateOrUpdateMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} | 
[**iosDeleteAppForMAMPolicy**](DefaultApi.md#iosDeleteAppForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps/{appName} | 
[**iosDeleteGroupForMAMPolicy**](DefaultApi.md#iosDeleteGroupForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups/{groupId} | 
[**iosDeleteMAMPolicy**](DefaultApi.md#iosDeleteMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} | 
[**iosGetAppForMAMPolicy**](DefaultApi.md#iosGetAppForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps | 
[**iosGetGroupsForMAMPolicy**](DefaultApi.md#iosGetGroupsForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups | 
[**iosGetMAMPolicies**](DefaultApi.md#iosGetMAMPolicies) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies | 
[**iosGetMAMPolicyByName**](DefaultApi.md#iosGetMAMPolicyByName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} | 
[**iosPatchMAMPolicy**](DefaultApi.md#iosPatchMAMPolicy) | **PATCH** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} | 
[**wipeMAMUserDevice**](DefaultApi.md#wipeMAMUserDevice) | **POST** /providers/Microsoft.Intune/locations/{hostName}/users/{userName}/devices/{deviceName}/wipe | 



## androidAddAppForMAMPolicy

> androidAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters)



Add app to an AndroidMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let appName = "appName_example"; // String | application unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to the Create or update app to an android policy operation.
apiInstance.androidAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **appName** | **String**| application unique Name | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to the Create or update app to an android policy operation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidAddGroupForMAMPolicy

> androidAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters)



Add group to an AndroidMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let groupId = "groupId_example"; // String | group Id
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to the Create or update app to an android policy operation.
apiInstance.androidAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **groupId** | **String**| group Id | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to the Create or update app to an android policy operation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidCreateOrUpdateMAMPolicy

> AndroidMAMPolicy androidCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters)



Creates or updates AndroidMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.AndroidMAMPolicy(); // AndroidMAMPolicy | Parameters supplied to the Create or update an android policy operation.
apiInstance.androidCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**AndroidMAMPolicy**](AndroidMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | 

### Return type

[**AndroidMAMPolicy**](AndroidMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androidDeleteAppForMAMPolicy

> androidDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion)



Delete App for Android Policy

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let appName = "appName_example"; // String | application unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.androidDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **appName** | **String**| application unique Name | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidDeleteGroupForMAMPolicy

> androidDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion)



Delete Group for Android Policy

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let groupId = "groupId_example"; // String | application unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.androidDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **groupId** | **String**| application unique Name | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidDeleteMAMPolicy

> androidDeleteMAMPolicy(hostName, policyName, apiVersion)



Delete Android Policy

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.androidDeleteMAMPolicy(hostName, policyName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidGetAppForMAMPolicy

> ApplicationCollection androidGetAppForMAMPolicy(hostName, policyName, apiVersion, opts)



Get apps for an AndroidMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.androidGetAppForMAMPolicy(hostName, policyName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**ApplicationCollection**](ApplicationCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidGetGroupsForMAMPolicy

> GroupsCollection androidGetGroupsForMAMPolicy(hostName, policyName, apiVersion)



Returns groups for a given AndroidMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | policy name for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.androidGetGroupsForMAMPolicy(hostName, policyName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| policy name for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

[**GroupsCollection**](GroupsCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidGetMAMPolicies

> AndroidMAMPolicyCollection androidGetMAMPolicies(hostName, apiVersion, opts)



Returns Intune Android policies.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.androidGetMAMPolicies(hostName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**AndroidMAMPolicyCollection**](AndroidMAMPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidGetMAMPolicyByName

> AndroidMAMPolicy androidGetMAMPolicyByName(hostName, policyName, apiVersion, opts)



Returns AndroidMAMPolicy with given name.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.androidGetMAMPolicyByName(hostName, policyName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**AndroidMAMPolicy**](AndroidMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androidPatchMAMPolicy

> AndroidMAMPolicy androidPatchMAMPolicy(hostName, policyName, apiVersion, parameters)



Patch AndroidMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.AndroidMAMPolicy(); // AndroidMAMPolicy | Parameters supplied to the Create or update an android policy operation.
apiInstance.androidPatchMAMPolicy(hostName, policyName, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**AndroidMAMPolicy**](AndroidMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | 

### Return type

[**AndroidMAMPolicy**](AndroidMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getApps

> ApplicationCollection getApps(hostName, apiVersion, opts)



Returns Intune Manageable apps.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getApps(hostName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**ApplicationCollection**](ApplicationCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLocationByHostName

> Location getLocationByHostName(apiVersion)



Returns location for given tenant.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.getLocationByHostName(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Service Api Version. | 

### Return type

[**Location**](Location.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLocations

> LocationCollection getLocations(apiVersion)



Returns location for user tenant.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.getLocations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Service Api Version. | 

### Return type

[**LocationCollection**](LocationCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMAMFlaggedUserByName

> FlaggedUser getMAMFlaggedUserByName(hostName, userName, apiVersion, opts)



Returns Intune flagged user details

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let userName = "userName_example"; // String | Flagged userName
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getMAMFlaggedUserByName(hostName, userName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **userName** | **String**| Flagged userName | 
 **apiVersion** | **String**| Service Api Version. | 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**FlaggedUser**](FlaggedUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMAMFlaggedUsers

> FlaggedUserCollection getMAMFlaggedUsers(hostName, apiVersion, opts)



Returns Intune flagged user collection

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getMAMFlaggedUsers(hostName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**FlaggedUserCollection**](FlaggedUserCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMAMStatuses

> StatusesDefault getMAMStatuses(hostName, apiVersion)



Returns Intune Tenant level statuses.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.getMAMStatuses(hostName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

[**StatusesDefault**](StatusesDefault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMAMUserDeviceByDeviceName

> Device getMAMUserDeviceByDeviceName(hostName, userName, deviceName, apiVersion, opts)



Get a unique device for a user.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let userName = "userName_example"; // String | unique user name
let deviceName = "deviceName_example"; // String | device name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getMAMUserDeviceByDeviceName(hostName, userName, deviceName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **userName** | **String**| unique user name | 
 **deviceName** | **String**| device name | 
 **apiVersion** | **String**| Service Api Version. | 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMAMUserDevices

> DeviceCollection getMAMUserDevices(hostName, userName, apiVersion, opts)



Get devices for a user.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let userName = "userName_example"; // String | user unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getMAMUserDevices(hostName, userName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **userName** | **String**| user unique Name | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**DeviceCollection**](DeviceCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMAMUserFlaggedEnrolledApps

> FlaggedEnrolledAppCollection getMAMUserFlaggedEnrolledApps(hostName, userName, apiVersion, opts)



Returns Intune flagged enrolled app collection for the User

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let userName = "userName_example"; // String | User name for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getMAMUserFlaggedEnrolledApps(hostName, userName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **userName** | **String**| User name for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**FlaggedEnrolledAppCollection**](FlaggedEnrolledAppCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOperationResults

> OperationResultCollection getOperationResults(hostName, apiVersion, opts)



Returns operationResults.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.getOperationResults(hostName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**OperationResultCollection**](OperationResultCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosAddAppForMAMPolicy

> iosAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters)



Add app to an iOSMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let appName = "appName_example"; // String | application unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to add an app to an ios policy.
apiInstance.iosAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **appName** | **String**| application unique Name | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to add an app to an ios policy. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iosAddGroupForMAMPolicy

> iosAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters)



Add group to an iOSMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let groupId = "groupId_example"; // String | group Id
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to the Create or update app to an android policy operation.
apiInstance.iosAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **groupId** | **String**| group Id | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to the Create or update app to an android policy operation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iosCreateOrUpdateMAMPolicy

> IOSMAMPolicy iosCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters)



Creates or updates iOSMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.IOSMAMPolicy(); // IOSMAMPolicy | Parameters supplied to the Create or update an android policy operation.
apiInstance.iosCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**IOSMAMPolicy**](IOSMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | 

### Return type

[**IOSMAMPolicy**](IOSMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## iosDeleteAppForMAMPolicy

> iosDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion)



Delete App for Ios Policy

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let appName = "appName_example"; // String | application unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.iosDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **appName** | **String**| application unique Name | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosDeleteGroupForMAMPolicy

> iosDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion)



Delete Group for iOS Policy

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let groupId = "groupId_example"; // String | application unique Name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.iosDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **groupId** | **String**| application unique Name | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosDeleteMAMPolicy

> iosDeleteMAMPolicy(hostName, policyName, apiVersion)



Delete Ios Policy

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.iosDeleteMAMPolicy(hostName, policyName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosGetAppForMAMPolicy

> ApplicationCollection iosGetAppForMAMPolicy(hostName, policyName, apiVersion, opts)



Get apps for an iOSMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.iosGetAppForMAMPolicy(hostName, policyName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**ApplicationCollection**](ApplicationCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosGetGroupsForMAMPolicy

> GroupsCollection iosGetGroupsForMAMPolicy(hostName, policyName, apiVersion)



Returns groups for a given iOSMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | policy name for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.iosGetGroupsForMAMPolicy(hostName, policyName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| policy name for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

[**GroupsCollection**](GroupsCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosGetMAMPolicies

> IOSMAMPolicyCollection iosGetMAMPolicies(hostName, apiVersion, opts)



Returns Intune iOSPolicies.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56, // Number | 
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.iosGetMAMPolicies(hostName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **apiVersion** | **String**| Service Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**|  | [optional] 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**IOSMAMPolicyCollection**](IOSMAMPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosGetMAMPolicyByName

> IOSMAMPolicy iosGetMAMPolicyByName(hostName, policyName, apiVersion, opts)



Returns Intune iOS policies.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let opts = {
  'select': "select_example" // String | select specific fields in entity.
};
apiInstance.iosGetMAMPolicyByName(hostName, policyName, apiVersion, opts, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **select** | **String**| select specific fields in entity. | [optional] 

### Return type

[**IOSMAMPolicy**](IOSMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iosPatchMAMPolicy

> IOSMAMPolicy iosPatchMAMPolicy(hostName, policyName, apiVersion, parameters)



 patch an iOSMAMPolicy.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let policyName = "policyName_example"; // String | Unique name for the policy
let apiVersion = "apiVersion_example"; // String | Service Api Version.
let parameters = new IntuneResourceManagementClient.IOSMAMPolicy(); // IOSMAMPolicy | Parameters supplied to the Create or update an android policy operation.
apiInstance.iosPatchMAMPolicy(hostName, policyName, apiVersion, parameters, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **policyName** | **String**| Unique name for the policy | 
 **apiVersion** | **String**| Service Api Version. | 
 **parameters** | [**IOSMAMPolicy**](IOSMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | 

### Return type

[**IOSMAMPolicy**](IOSMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wipeMAMUserDevice

> WipeDeviceOperationResult wipeMAMUserDevice(hostName, userName, deviceName, apiVersion)



Wipe a device for a user.

### Example

```javascript
import IntuneResourceManagementClient from 'intune_resource_management_client';

let apiInstance = new IntuneResourceManagementClient.DefaultApi();
let hostName = "hostName_example"; // String | Location hostName for the tenant
let userName = "userName_example"; // String | unique user name
let deviceName = "deviceName_example"; // String | device name
let apiVersion = "apiVersion_example"; // String | Service Api Version.
apiInstance.wipeMAMUserDevice(hostName, userName, deviceName, apiVersion, (error, data, response) => {
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
 **hostName** | **String**| Location hostName for the tenant | 
 **userName** | **String**| unique user name | 
 **deviceName** | **String**| device name | 
 **apiVersion** | **String**| Service Api Version. | 

### Return type

[**WipeDeviceOperationResult**](WipeDeviceOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

