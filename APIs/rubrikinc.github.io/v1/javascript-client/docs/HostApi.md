# RubrikRestApi.HostApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkRegisterHostAsync**](HostApi.md#bulkRegisterHostAsync) | **POST** /host/bulk_background | Register hosts
[**deleteHost**](HostApi.md#deleteHost) | **DELETE** /host/{id} | Delete a registered host
[**discoverNasShares**](HostApi.md#discoverNasShares) | **GET** /host/{id}/nas_share_discover | Discover and return all shares on a NAS host
[**getHost**](HostApi.md#getHost) | **GET** /host/{id} | Get summary information for a host
[**getRbsHostInfo**](HostApi.md#getRbsHostInfo) | **GET** /host/rbs | Get the Rubrik Backup Service details for a host
[**hostMakePrimary**](HostApi.md#hostMakePrimary) | **POST** /host/make_primary | Make this cluster the primary for agents on a set of hosts
[**queryHost**](HostApi.md#queryHost) | **GET** /host | Get summary information for hosts
[**queryHostVolume**](HostApi.md#queryHostVolume) | **GET** /host/{id}/volume | Get list of Volume Group volumes
[**rbsInstall**](HostApi.md#rbsInstall) | **POST** /host/rbs/install | Install Rubrik Backup Service on a host
[**rbsUninstall**](HostApi.md#rbsUninstall) | **POST** /host/rbs/uninstall | Uninstall Rubrik Backup Service from a host
[**rbsUpgrade**](HostApi.md#rbsUpgrade) | **POST** /host/rbs/upgrade | Upgrade Rubrik Backup Service on a host
[**refreshHost**](HostApi.md#refreshHost) | **POST** /host/{id}/refresh | Refresh a host
[**registerHost**](HostApi.md#registerHost) | **POST** /host | Register a host
[**registerHostAsync**](HostApi.md#registerHostAsync) | **POST** /host/background | Register a host
[**searchHost**](HostApi.md#searchHost) | **GET** /host/{id}/search | Search for a file within the host
[**updateCertificateHost**](HostApi.md#updateCertificateHost) | **PUT** /host/certificate/{id} | Update certificate
[**updateHost**](HostApi.md#updateHost) | **PATCH** /host/{id} | Modify information for a registered host



## bulkRegisterHostAsync

> [HostDetail] bulkRegisterHostAsync(hostRegister)

Register hosts

Register multiple hosts and perform discovery for databases and Microsoft SQL Server instances. When called, this API returns a success message, but completes the host registration in the background. Monitor the status of the background host discovery with the \&quot;status\&quot; field in GET API on /hosts. The POST API on /hosts can take longer for discovery, depending on the number of hosts on the system. POST on this API can be used instead to perform the discovery in the background and quickly register the host. Doing this requires that you install RBS for Linux and Windows hosts, similar to regular register using POST on /hosts.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let hostRegister = [new RubrikRestApi.HostRegister()]; // [HostRegister] | Registration definition for each host.
apiInstance.bulkRegisterHostAsync(hostRegister, (error, data, response) => {
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
 **hostRegister** | [**[HostRegister]**](HostRegister.md)| Registration definition for each host. | 

### Return type

[**[HostDetail]**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteHost

> deleteHost(id)

Delete a registered host

Delete host by specifying the host ID.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | ID of the host to delete.
apiInstance.deleteHost(id, (error, data, response) => {
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
 **id** | **String**| ID of the host to delete. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## discoverNasShares

> [DiscoveredNasShare] discoverNasShares(id)

Discover and return all shares on a NAS host

Discover and return all shares on the identified NAS host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | The discoverable NAS host ID.
apiInstance.discoverNasShares(id, (error, data, response) => {
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
 **id** | **String**| The discoverable NAS host ID. | 

### Return type

[**[DiscoveredNasShare]**](DiscoveredNasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHost

> HostDetail getHost(id)

Get summary information for a host

Retrieve summary information for a registered host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | ID of the registered host.
apiInstance.getHost(id, (error, data, response) => {
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
 **id** | **String**| ID of the registered host. | 

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRbsHostInfo

> RbsHostSummary getRbsHostInfo(name, username, password, opts)

Get the Rubrik Backup Service details for a host

Get the details of the Rubrik Backup Service (RBS) installed on a specific host. Specify the details of the host to check whether RBS is installed on the host or not. If RBS is installed, the response will include the RBS details.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let name = "name_example"; // String | IP address or hostname of the host.
let username = "username_example"; // String | Name of the user account that has sudo/admin privileges on the RBS host. This is required to install/uninstall/upgrade RBS packages on the RBS host.
let password = "password_example"; // String | Password associated with the username that has access to the host.
let opts = {
  'operationTimeout': 600 // Number | Number of seconds after which the operation is terminated if it has not completed execution. Default value is 600 seconds.
};
apiInstance.getRbsHostInfo(name, username, password, opts, (error, data, response) => {
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
 **name** | **String**| IP address or hostname of the host. | 
 **username** | **String**| Name of the user account that has sudo/admin privileges on the RBS host. This is required to install/uninstall/upgrade RBS packages on the RBS host. | 
 **password** | **String**| Password associated with the username that has access to the host. | 
 **operationTimeout** | **Number**| Number of seconds after which the operation is terminated if it has not completed execution. Default value is 600 seconds. | [optional] [default to 600]

### Return type

[**RbsHostSummary**](RbsHostSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hostMakePrimary

> AsyncRequestStatus hostMakePrimary(hostMakePrimaryRequest)

Make this cluster the primary for agents on a set of hosts

Migrate the primary cluster with which the agent is able to perform regular operations (backup, restore etc). This can be done on a specified set of hosts or for all hosts that currently have a specified primary cluster for disaster recovery. Specify exactly one of &#x60;ids&#x60; or &#x60;oldPrimaryClusterUuid&#x60;.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let hostMakePrimaryRequest = new RubrikRestApi.HostMakePrimaryRequest(); // HostMakePrimaryRequest | Description of hosts to migrate.
apiInstance.hostMakePrimary(hostMakePrimaryRequest, (error, data, response) => {
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
 **hostMakePrimaryRequest** | [**HostMakePrimaryRequest**](HostMakePrimaryRequest.md)| Description of hosts to migrate. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryHost

> HostSummaryListResponse queryHost(opts)

Get summary information for hosts

Retrieve summary information for all hosts that are registered with a Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let opts = {
  'operatingSystemType': "operatingSystemType_example", // String | Filter the summary information based on the operating system type. Accepted values are 'Windows', 'UnixLike', 'ANY', 'NONE'. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set.
  'operatingSystem': "operatingSystem_example", // String | Filter the summary information based on the operating system. Use **_AIX_**, **_Linux_** or **_Solaris_** to restrict the returned information to hosts with operating systems within the specified operating system family. Use a specific operating system release version to restrict the returned information to hosts with operating systems that match the specified version.
  'primaryClusterId': "primaryClusterId_example", // String | Filters the summary information based on the Rubrik cluster specified by the value of primary_cluster_id. Use 'local' for the Rubrik cluster that is hosting the current REST API session.
  'name': "name_example", // String | Retrieve hosts with a host name matching the provided name. The search type is infix.
  'hostname': "hostname_example", // String | (Deprecated) Retrieve hosts with a host name matching the provided name. The search type is infix.
  'sortBy': "sortBy_example", // String | Specifies the host attribute to use in sorting the host summary information. Performs an ASCII sort of the summary information using the specified attribute, in the order specified. Valid attributes are 'hostname'.
  'sortOrder': "sortOrder_example", // String | Sort order, either ascending or descending.
  'snappableStatus': "snappableStatus_example" // String | Determines whether to fetch hosts with additional privilege checks.
};
apiInstance.queryHost(opts, (error, data, response) => {
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
 **operatingSystemType** | **String**| Filter the summary information based on the operating system type. Accepted values are &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set. | [optional] 
 **operatingSystem** | **String**| Filter the summary information based on the operating system. Use **_AIX_**, **_Linux_** or **_Solaris_** to restrict the returned information to hosts with operating systems within the specified operating system family. Use a specific operating system release version to restrict the returned information to hosts with operating systems that match the specified version. | [optional] 
 **primaryClusterId** | **String**| Filters the summary information based on the Rubrik cluster specified by the value of primary_cluster_id. Use &#39;local&#39; for the Rubrik cluster that is hosting the current REST API session. | [optional] 
 **name** | **String**| Retrieve hosts with a host name matching the provided name. The search type is infix. | [optional] 
 **hostname** | **String**| (Deprecated) Retrieve hosts with a host name matching the provided name. The search type is infix. | [optional] 
 **sortBy** | **String**| Specifies the host attribute to use in sorting the host summary information. Performs an ASCII sort of the summary information using the specified attribute, in the order specified. Valid attributes are &#39;hostname&#39;. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 
 **snappableStatus** | **String**| Determines whether to fetch hosts with additional privilege checks. | [optional] 

### Return type

[**HostSummaryListResponse**](HostSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryHostVolume

> HostVolumeSummaryListResponse queryHostVolume(id)

Get list of Volume Group volumes

Retrieve summary information for each volume on a specified Volume Group host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | The ID of the host.
apiInstance.queryHostVolume(id, (error, data, response) => {
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
 **id** | **String**| The ID of the host. | 

### Return type

[**HostVolumeSummaryListResponse**](HostVolumeSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rbsInstall

> RbsHostOperationResponse rbsInstall(rbsHostOperationRequest)

Install Rubrik Backup Service on a host

Install Rubrik Backup Service on a host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let rbsHostOperationRequest = new RubrikRestApi.RbsHostOperationRequest(); // RbsHostOperationRequest | Configuration parameters to install RBS on a host.
apiInstance.rbsInstall(rbsHostOperationRequest, (error, data, response) => {
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
 **rbsHostOperationRequest** | [**RbsHostOperationRequest**](RbsHostOperationRequest.md)| Configuration parameters to install RBS on a host. | 

### Return type

[**RbsHostOperationResponse**](RbsHostOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rbsUninstall

> RbsHostOperationResponse rbsUninstall(rbsHostOperationRequest)

Uninstall Rubrik Backup Service from a host

Uninstall Rubrik Backup Service from a host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let rbsHostOperationRequest = new RubrikRestApi.RbsHostOperationRequest(); // RbsHostOperationRequest | Configuration parameters to uninstall RBS from a host.
apiInstance.rbsUninstall(rbsHostOperationRequest, (error, data, response) => {
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
 **rbsHostOperationRequest** | [**RbsHostOperationRequest**](RbsHostOperationRequest.md)| Configuration parameters to uninstall RBS from a host. | 

### Return type

[**RbsHostOperationResponse**](RbsHostOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rbsUpgrade

> RbsHostOperationResponse rbsUpgrade(rbsHostOperationRequest)

Upgrade Rubrik Backup Service on a host

Upgrade Rubrik Backup Service on a host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let rbsHostOperationRequest = new RubrikRestApi.RbsHostOperationRequest(); // RbsHostOperationRequest | Configuration parameters to upgrade RBS on a host.
apiInstance.rbsUpgrade(rbsHostOperationRequest, (error, data, response) => {
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
 **rbsHostOperationRequest** | [**RbsHostOperationRequest**](RbsHostOperationRequest.md)| Configuration parameters to upgrade RBS on a host. | 

### Return type

[**RbsHostOperationResponse**](RbsHostOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## refreshHost

> HostDetail refreshHost(id)

Refresh a host

Refresh the properties of a host object when changes on the host are not seen in the Rubrik web UI.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | ID assigned to a host object.
apiInstance.refreshHost(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a host object. | 

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registerHost

> HostDetail registerHost(hostRegister)

Register a host

Register a host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let hostRegister = new RubrikRestApi.HostRegister(); // HostRegister | Registration definition for a host.
apiInstance.registerHost(hostRegister, (error, data, response) => {
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
 **hostRegister** | [**HostRegister**](HostRegister.md)| Registration definition for a host. | 

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registerHostAsync

> HostDetail registerHostAsync(hostRegister)

Register a host

Register a host and perform discovery for databases and Microsoft SQL Server instances. When called, this API returns a success message, but completes the host registration in the background. Monitor the status of the background host discovery with the \&quot;status\&quot; field in GET API on /hosts. The POST API on /hosts can take longer for discovery, depending on the number of hosts on the system. POST on this API can be used instead to perform the discovery in the background and quickly register the host. Doing this requires that you install RBS for Linux and Windows hosts, similar to regular register using POST on /hosts.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let hostRegister = new RubrikRestApi.HostRegister(); // HostRegister | Registration definition for a host.
apiInstance.registerHostAsync(hostRegister, (error, data, response) => {
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
 **hostRegister** | [**HostRegister**](HostRegister.md)| Registration definition for a host. | 

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchHost

> SearchResponseListResponse searchHost(id, path)

Search for a file within the host

Search for a file within the host. Search via full path prefix or filename prefix.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | ID of the host to search.
let path = "path_example"; // String | The path query. Either path prefix or filename prefix.
apiInstance.searchHost(id, path, (error, data, response) => {
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
 **id** | **String**| ID of the host to search. | 
 **path** | **String**| The path query. Either path prefix or filename prefix. | 

### Return type

[**SearchResponseListResponse**](SearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCertificateHost

> HostDetail updateCertificateHost(id)

Update certificate

Provide an updated certificate for a specified host.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | ID of the host.
apiInstance.updateCertificateHost(id, (error, data, response) => {
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
 **id** | **String**| ID of the host. | 

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateHost

> HostDetail updateHost(id, hostUpdate)

Modify information for a registered host

Change the FQDN and IPv4 address that is assigned to a host object. Enable or disable pre-transfer data compression. Enable or disable change block tracking (CBT) for backups of SQL Server databases on Windows hosts. Enable or disable volume filter driver (VFD) for volume backups on Windows hosts. Set an Oracle user with sysdba privileges to permit Oracle discovery queries.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.HostApi();
let id = "id_example"; // String | ID of the registered host.
let hostUpdate = new RubrikRestApi.HostUpdate(); // HostUpdate | Properties of host to update.
apiInstance.updateHost(id, hostUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the registered host. | 
 **hostUpdate** | [**HostUpdate**](HostUpdate.md)| Properties of host to update. | 

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

