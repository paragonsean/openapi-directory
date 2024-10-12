# CleverCloudApi.NetworkgroupsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createNetworkGroupExternalPeer_1**](NetworkgroupsApi.md#createNetworkGroupExternalPeer_1) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers | Add external peer
[**createNetworkGroupMember_1**](NetworkgroupsApi.md#createNetworkGroupMember_1) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | Add member
[**createNetworkGroup_1**](NetworkgroupsApi.md#createNetworkGroup_1) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups | Create Network Group
[**deleteNetworkGroupExternalPeer_1**](NetworkgroupsApi.md#deleteNetworkGroupExternalPeer_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers/{peerId} | Remove external peer
[**deleteNetworkGroupMember_1**](NetworkgroupsApi.md#deleteNetworkGroupMember_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Remove member
[**deleteNetworkGroupPeer_1**](NetworkgroupsApi.md#deleteNetworkGroupPeer_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Remove peer
[**deleteNetworkGroup_1**](NetworkgroupsApi.md#deleteNetworkGroup_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Delete Network Group
[**getNetworkGroupMember_1**](NetworkgroupsApi.md#getNetworkGroupMember_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Get member
[**getNetworkGroupPeer_1**](NetworkgroupsApi.md#getNetworkGroupPeer_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Get peer
[**getNetworkGroupStream_1**](NetworkgroupsApi.md#getNetworkGroupStream_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/stream | Network Group SSE
[**getNetworkGroupWireGuardConfigurationStream_1**](NetworkgroupsApi.md#getNetworkGroupWireGuardConfigurationStream_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration/stream | Get WireGuard® configuration
[**getNetworkGroupWireGuardConfiguration_1**](NetworkgroupsApi.md#getNetworkGroupWireGuardConfiguration_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration | Get WireGuard® configuration
[**getNetworkGroup_1**](NetworkgroupsApi.md#getNetworkGroup_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Get Network Group
[**listNetworkGroupMembers_1**](NetworkgroupsApi.md#listNetworkGroupMembers_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | List members
[**listNetworkGroupPeers_1**](NetworkgroupsApi.md#listNetworkGroupPeers_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers | List peers
[**listNetworkGroups_1**](NetworkgroupsApi.md#listNetworkGroups_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups | List Network Groups



## createNetworkGroupExternalPeer_1

> Object createNetworkGroupExternalPeer_1(ownerId, networkGroupId, opts)

Add external peer

Adds an external peer to a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.createNetworkGroupExternalPeer_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain; charset=UTF-8


## createNetworkGroupMember_1

> createNetworkGroupMember_1(ownerId, networkGroupId, opts)

Add member

Adds a member to a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'schema2': new CleverCloudApi.Schema2() // Schema2 | 
};
apiInstance.createNetworkGroupMember_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **schema2** | [**Schema2**](Schema2.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createNetworkGroup_1

> Object createNetworkGroup_1(ownerId, opts)

Create Network Group

Creates a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.createNetworkGroup_1(ownerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, text/plain; charset=UTF-8


## deleteNetworkGroupExternalPeer_1

> deleteNetworkGroupExternalPeer_1(ownerId, networkGroupId, peerId, opts)

Remove external peer

Removes an external peer from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupExternalPeer_1(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroupMember_1

> deleteNetworkGroupMember_1(ownerId, networkGroupId, memberId, opts)

Remove member

Removes a member from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let memberId = "memberId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupMember_1(ownerId, networkGroupId, memberId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **memberId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroupPeer_1

> deleteNetworkGroupPeer_1(ownerId, networkGroupId, peerId, opts)

Remove peer

Removes a peer from a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroupPeer_1(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteNetworkGroup_1

> deleteNetworkGroup_1(ownerId, networkGroupId, opts)

Delete Network Group

Deletes a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.deleteNetworkGroup_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getNetworkGroupMember_1

> Schema1 getNetworkGroupMember_1(ownerId, networkGroupId, memberId, opts)

Get member

Gets details of a Network Group member.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let memberId = "memberId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupMember_1(ownerId, networkGroupId, memberId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **memberId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

[**Schema1**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroupPeer_1

> Object getNetworkGroupPeer_1(ownerId, networkGroupId, peerId, opts)

Get peer

Gets details of a Network Group peer.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupPeer_1(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroupStream_1

> Object getNetworkGroupStream_1(ownerId, networkGroupId, opts)

Network Group SSE

Retrieves the current Network Group details as a Server Sent Event.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupStream_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


## getNetworkGroupWireGuardConfigurationStream_1

> Object getNetworkGroupWireGuardConfigurationStream_1(ownerId, networkGroupId, peerId, opts)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupWireGuardConfigurationStream_1(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


## getNetworkGroupWireGuardConfiguration_1

> Object getNetworkGroupWireGuardConfiguration_1(ownerId, networkGroupId, peerId, opts)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let peerId = "peerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroupWireGuardConfiguration_1(ownerId, networkGroupId, peerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **peerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworkGroup_1

> Object getNetworkGroup_1(ownerId, networkGroupId, opts)

Get Network Group

Gets details of a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.getNetworkGroup_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkGroupMembers_1

> [Schema1] listNetworkGroupMembers_1(ownerId, networkGroupId, opts)

List members

Lists members in a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroupMembers_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

[**[Schema1]**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkGroupPeers_1

> [Object] listNetworkGroupPeers_1(ownerId, networkGroupId, opts)

List peers

Lists peers in a Network Group.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let networkGroupId = "networkGroupId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroupPeers_1(ownerId, networkGroupId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **networkGroupId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNetworkGroups_1

> [Object] listNetworkGroups_1(ownerId, opts)

List Network Groups

Lists Network Groups from an owner.

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.NetworkgroupsApi();
let ownerId = "ownerId_example"; // String | Automatically added
let opts = {
  'body': null // Object | 
};
apiInstance.listNetworkGroups_1(ownerId, opts, (error, data, response) => {
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
 **ownerId** | **String**| Automatically added | 
 **body** | **Object**|  | [optional] 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

