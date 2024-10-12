# LinodeApi.LinodeInstancesApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addLinodeConfig**](LinodeInstancesApi.md#addLinodeConfig) | **POST** /linode/instances/{linodeId}/configs | Configuration Profile Create
[**addLinodeDisk**](LinodeInstancesApi.md#addLinodeDisk) | **POST** /linode/instances/{linodeId}/disks | Disk Create
[**addLinodeIP**](LinodeInstancesApi.md#addLinodeIP) | **POST** /linode/instances/{linodeId}/ips | IPv4 Address Allocate
[**bootLinodeInstance**](LinodeInstancesApi.md#bootLinodeInstance) | **POST** /linode/instances/{linodeId}/boot | Linode Boot
[**cancelBackups**](LinodeInstancesApi.md#cancelBackups) | **POST** /linode/instances/{linodeId}/backups/cancel | Backups Cancel
[**cloneLinodeDisk**](LinodeInstancesApi.md#cloneLinodeDisk) | **POST** /linode/instances/{linodeId}/disks/{diskId}/clone | Disk Clone
[**cloneLinodeInstance**](LinodeInstancesApi.md#cloneLinodeInstance) | **POST** /linode/instances/{linodeId}/clone | Linode Clone
[**createLinodeInstance**](LinodeInstancesApi.md#createLinodeInstance) | **POST** /linode/instances | Linode Create
[**createSnapshot**](LinodeInstancesApi.md#createSnapshot) | **POST** /linode/instances/{linodeId}/backups | Snapshot Create
[**deleteDisk**](LinodeInstancesApi.md#deleteDisk) | **DELETE** /linode/instances/{linodeId}/disks/{diskId} | Disk Delete
[**deleteLinodeConfig**](LinodeInstancesApi.md#deleteLinodeConfig) | **DELETE** /linode/instances/{linodeId}/configs/{configId} | Configuration Profile Delete
[**deleteLinodeInstance**](LinodeInstancesApi.md#deleteLinodeInstance) | **DELETE** /linode/instances/{linodeId} | Linode Delete
[**enableBackups**](LinodeInstancesApi.md#enableBackups) | **POST** /linode/instances/{linodeId}/backups/enable | Backups Enable
[**getBackup**](LinodeInstancesApi.md#getBackup) | **GET** /linode/instances/{linodeId}/backups/{backupId} | Backup View
[**getBackups**](LinodeInstancesApi.md#getBackups) | **GET** /linode/instances/{linodeId}/backups | Backups List
[**getKernel**](LinodeInstancesApi.md#getKernel) | **GET** /linode/kernels/{kernelId} | Kernel View
[**getKernels**](LinodeInstancesApi.md#getKernels) | **GET** /linode/kernels | Kernels List
[**getLinodeConfig**](LinodeInstancesApi.md#getLinodeConfig) | **GET** /linode/instances/{linodeId}/configs/{configId} | Configuration Profile View
[**getLinodeConfigs**](LinodeInstancesApi.md#getLinodeConfigs) | **GET** /linode/instances/{linodeId}/configs | Configuration Profiles List
[**getLinodeDisk**](LinodeInstancesApi.md#getLinodeDisk) | **GET** /linode/instances/{linodeId}/disks/{diskId} | Disk View
[**getLinodeDisks**](LinodeInstancesApi.md#getLinodeDisks) | **GET** /linode/instances/{linodeId}/disks | Disks List
[**getLinodeFirewalls**](LinodeInstancesApi.md#getLinodeFirewalls) | **GET** /linode/instances/{linodeId}/firewalls | Firewalls List
[**getLinodeIP**](LinodeInstancesApi.md#getLinodeIP) | **GET** /linode/instances/{linodeId}/ips/{address} | IP Address View
[**getLinodeIPs**](LinodeInstancesApi.md#getLinodeIPs) | **GET** /linode/instances/{linodeId}/ips | Networking Information List
[**getLinodeInstance**](LinodeInstancesApi.md#getLinodeInstance) | **GET** /linode/instances/{linodeId} | Linode View
[**getLinodeInstances**](LinodeInstancesApi.md#getLinodeInstances) | **GET** /linode/instances | Linodes List
[**getLinodeNodeBalancers**](LinodeInstancesApi.md#getLinodeNodeBalancers) | **GET** /linode/instances/{linodeId}/nodebalancers | Linode NodeBalancers View
[**getLinodeStats**](LinodeInstancesApi.md#getLinodeStats) | **GET** /linode/instances/{linodeId}/stats | Linode Statistics View
[**getLinodeStatsByYearMonth**](LinodeInstancesApi.md#getLinodeStatsByYearMonth) | **GET** /linode/instances/{linodeId}/stats/{year}/{month} | Statistics View (year/month)
[**getLinodeTransfer**](LinodeInstancesApi.md#getLinodeTransfer) | **GET** /linode/instances/{linodeId}/transfer | Network Transfer View
[**getLinodeTransferByYearMonth**](LinodeInstancesApi.md#getLinodeTransferByYearMonth) | **GET** /linode/instances/{linodeId}/transfer/{year}/{month} | Network Transfer View (year/month)
[**getLinodeVolumes**](LinodeInstancesApi.md#getLinodeVolumes) | **GET** /linode/instances/{linodeId}/volumes | Linode&#39;s Volumes List
[**migrateLinodeInstance**](LinodeInstancesApi.md#migrateLinodeInstance) | **POST** /linode/instances/{linodeId}/migrate | DC Migration/Pending Host Migration Initiate
[**mutateLinodeInstance**](LinodeInstancesApi.md#mutateLinodeInstance) | **POST** /linode/instances/{linodeId}/mutate | Linode Upgrade
[**rebootLinodeInstance**](LinodeInstancesApi.md#rebootLinodeInstance) | **POST** /linode/instances/{linodeId}/reboot | Linode Reboot
[**rebuildLinodeInstance**](LinodeInstancesApi.md#rebuildLinodeInstance) | **POST** /linode/instances/{linodeId}/rebuild | Linode Rebuild
[**removeLinodeIP**](LinodeInstancesApi.md#removeLinodeIP) | **DELETE** /linode/instances/{linodeId}/ips/{address} | IPv4 Address Delete
[**rescueLinodeInstance**](LinodeInstancesApi.md#rescueLinodeInstance) | **POST** /linode/instances/{linodeId}/rescue | Linode Boot into Rescue Mode
[**resetDiskPassword**](LinodeInstancesApi.md#resetDiskPassword) | **POST** /linode/instances/{linodeId}/disks/{diskId}/password | Disk Root Password Reset
[**resetLinodePassword**](LinodeInstancesApi.md#resetLinodePassword) | **POST** /linode/instances/{linodeId}/password | Linode Root Password Reset
[**resizeDisk**](LinodeInstancesApi.md#resizeDisk) | **POST** /linode/instances/{linodeId}/disks/{diskId}/resize | Disk Resize
[**resizeLinodeInstance**](LinodeInstancesApi.md#resizeLinodeInstance) | **POST** /linode/instances/{linodeId}/resize | Linode Resize
[**restoreBackup**](LinodeInstancesApi.md#restoreBackup) | **POST** /linode/instances/{linodeId}/backups/{backupId}/restore | Backup Restore
[**shutdownLinodeInstance**](LinodeInstancesApi.md#shutdownLinodeInstance) | **POST** /linode/instances/{linodeId}/shutdown | Linode Shut Down
[**updateDisk**](LinodeInstancesApi.md#updateDisk) | **PUT** /linode/instances/{linodeId}/disks/{diskId} | Disk Update
[**updateLinodeConfig**](LinodeInstancesApi.md#updateLinodeConfig) | **PUT** /linode/instances/{linodeId}/configs/{configId} | Configuration Profile Update
[**updateLinodeIP**](LinodeInstancesApi.md#updateLinodeIP) | **PUT** /linode/instances/{linodeId}/ips/{address} | IP Address Update
[**updateLinodeInstance**](LinodeInstancesApi.md#updateLinodeInstance) | **PUT** /linode/instances/{linodeId} | Linode Update



## addLinodeConfig

> LinodeConfig addLinodeConfig(linodeId, linodeConfig)

Configuration Profile Create

Adds a new Configuration profile to a Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up Configuration profiles for.
let linodeConfig = new LinodeApi.LinodeConfig(); // LinodeConfig | The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with. 
apiInstance.addLinodeConfig(linodeId, linodeConfig, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up Configuration profiles for. | 
 **linodeConfig** | [**LinodeConfig**](LinodeConfig.md)| The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with.  | 

### Return type

[**LinodeConfig**](LinodeConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addLinodeDisk

> Disk addLinodeDisk(linodeId, diskRequest)

Disk Create

Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a &#x60;label&#x60; is required.  * If no &#x60;label&#x60; is provided, an &#x60;image&#x60; is required instead.  * When creating a Disk from an Image, &#x60;root_pass&#x60; is required.  * The default filesystem for new Disks is &#x60;ext4&#x60;. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskRequest = new LinodeApi.DiskRequest(); // DiskRequest | The parameters to set when creating the Disk. 
apiInstance.addLinodeDisk(linodeId, diskRequest, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskRequest** | [**DiskRequest**](DiskRequest.md)| The parameters to set when creating the Disk.  | 

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addLinodeIP

> IPAddress addLinodeIP(linodeId, addLinodeIPRequest)

IPv4 Address Allocate

Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let addLinodeIPRequest = new LinodeApi.AddLinodeIPRequest(); // AddLinodeIPRequest | Information about the address you are creating.
apiInstance.addLinodeIP(linodeId, addLinodeIPRequest, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **addLinodeIPRequest** | [**AddLinodeIPRequest**](AddLinodeIPRequest.md)| Information about the address you are creating. | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bootLinodeInstance

> Object bootLinodeInstance(linodeId, opts)

Linode Boot

Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode to boot.
let opts = {
  'bootLinodeInstanceRequest': new LinodeApi.BootLinodeInstanceRequest() // BootLinodeInstanceRequest | Optional configuration to boot into (see above).
};
apiInstance.bootLinodeInstance(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode to boot. | 
 **bootLinodeInstanceRequest** | [**BootLinodeInstanceRequest**](BootLinodeInstanceRequest.md)| Optional configuration to boot into (see above). | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelBackups

> Object cancelBackups(linodeId)

Backups Cancel

Cancels the Backup service on the given Linode. Deletes all of this Linode&#39;s existing backups forever. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode to cancel backup service for.
apiInstance.cancelBackups(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode to cancel backup service for. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloneLinodeDisk

> Disk cloneLinodeDisk(linodeId, diskId)

Disk Clone

Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskId = 56; // Number | ID of the Disk to clone.
apiInstance.cloneLinodeDisk(linodeId, diskId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskId** | **Number**| ID of the Disk to clone. | 

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloneLinodeInstance

> Linode cloneLinodeInstance(linodeId, cloneLinodeInstanceRequest)

Linode Clone

You can clone your Linode&#39;s existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to clone.
let cloneLinodeInstanceRequest = new LinodeApi.CloneLinodeInstanceRequest(); // CloneLinodeInstanceRequest | The requested state your Linode will be cloned into.
apiInstance.cloneLinodeInstance(linodeId, cloneLinodeInstanceRequest, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to clone. | 
 **cloneLinodeInstanceRequest** | [**CloneLinodeInstanceRequest**](CloneLinodeInstanceRequest.md)| The requested state your Linode will be cloned into. | 

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLinodeInstance

> Linode createLinodeInstance(createLinodeInstanceRequest)

Linode Create

Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type&#39;s specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * A default config with two Disks, one being a 512 swap disk, is created.     * &#x60;swap_size&#x60; can be used to customize the swap disk size.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode&#39;s backups.   * You must create a Linode large enough to accommodate the Backup&#39;s size.   * The Disks and Config will match that of the Linode that was backed up.   * The &#x60;root_pass&#x60; will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the &#x60;interfaces&#x60; property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain &#x60;offline&#x60; and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let createLinodeInstanceRequest = new LinodeApi.CreateLinodeInstanceRequest(); // CreateLinodeInstanceRequest | The requested initial state of a new Linode.
apiInstance.createLinodeInstance(createLinodeInstanceRequest, (error, data, response) => {
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
 **createLinodeInstanceRequest** | [**CreateLinodeInstanceRequest**](CreateLinodeInstanceRequest.md)| The requested initial state of a new Linode. | 

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSnapshot

> Backup createSnapshot(linodeId, createSnapshotRequest)

Snapshot Create

Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode the backups belong to.
let createSnapshotRequest = new LinodeApi.CreateSnapshotRequest(); // CreateSnapshotRequest | 
apiInstance.createSnapshot(linodeId, createSnapshotRequest, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode the backups belong to. | 
 **createSnapshotRequest** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | 

### Return type

[**Backup**](Backup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDisk

> Object deleteDisk(linodeId, diskId)

Disk Delete

Deletes a Disk you have permission to &#x60;read_write&#x60;.  **Deleting a Disk is a destructive action and cannot be undone.** 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskId = 56; // Number | ID of the Disk to look up.
apiInstance.deleteDisk(linodeId, diskId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskId** | **Number**| ID of the Disk to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLinodeConfig

> Object deleteLinodeConfig(linodeId, configId)

Configuration Profile Delete

Deletes the specified Configuration profile from the specified Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode whose Configuration profile to look up.
let configId = 56; // Number | The ID of the Configuration profile to look up.
apiInstance.deleteLinodeConfig(linodeId, configId, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode whose Configuration profile to look up. | 
 **configId** | **Number**| The ID of the Configuration profile to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLinodeInstance

> Object deleteLinodeInstance(linodeId)

Linode Delete

Deletes a Linode you have permission to &#x60;read_write&#x60;.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up
apiInstance.deleteLinodeInstance(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableBackups

> Object enableBackups(linodeId)

Backups Enable

Enables backups for the specified Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode to enable backup service for.
apiInstance.enableBackups(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode to enable backup service for. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackup

> Backup getBackup(linodeId, backupId)

Backup View

Returns information about a Backup. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode the Backup belongs to.
let backupId = 56; // Number | The ID of the Backup to look up.
apiInstance.getBackup(linodeId, backupId, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode the Backup belongs to. | 
 **backupId** | **Number**| The ID of the Backup to look up. | 

### Return type

[**Backup**](Backup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackups

> GetBackups200Response getBackups(linodeId)

Backups List

Returns information about this Linode&#39;s available backups. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode the backups belong to.
apiInstance.getBackups(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode the backups belong to. | 

### Return type

[**GetBackups200Response**](GetBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKernel

> Kernel getKernel(kernelId)

Kernel View

Returns information about a single Kernel. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let kernelId = "kernelId_example"; // String | ID of the Kernel to look up.
apiInstance.getKernel(kernelId, (error, data, response) => {
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
 **kernelId** | **String**| ID of the Kernel to look up. | 

### Return type

[**Kernel**](Kernel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKernels

> GetKernels200Response getKernels(opts)

Kernels List

Lists available Kernels. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getKernels(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetKernels200Response**](GetKernels200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeConfig

> LinodeConfig getLinodeConfig(linodeId, configId)

Configuration Profile View

Returns information about a specific Configuration profile. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode whose Configuration profile to look up.
let configId = 56; // Number | The ID of the Configuration profile to look up.
apiInstance.getLinodeConfig(linodeId, configId, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode whose Configuration profile to look up. | 
 **configId** | **Number**| The ID of the Configuration profile to look up. | 

### Return type

[**LinodeConfig**](LinodeConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeConfigs

> GetLinodeConfigs200Response getLinodeConfigs(linodeId, opts)

Configuration Profiles List

Lists Configuration profiles associated with a Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up Configuration profiles for.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLinodeConfigs(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up Configuration profiles for. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeConfigs200Response**](GetLinodeConfigs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeDisk

> Disk getLinodeDisk(linodeId, diskId)

Disk View

View Disk information for a Disk associated with this Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskId = 56; // Number | ID of the Disk to look up.
apiInstance.getLinodeDisk(linodeId, diskId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskId** | **Number**| ID of the Disk to look up. | 

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeDisks

> GetLinodeDisks200Response getLinodeDisks(linodeId, opts)

Disks List

View Disk information for Disks associated with this Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLinodeDisks(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeDisks200Response**](GetLinodeDisks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeFirewalls

> GetLinodeFirewalls200Response getLinodeFirewalls(linodeId, opts)

Firewalls List

View Firewall information for Firewalls associated with this Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLinodeFirewalls(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeFirewalls200Response**](GetLinodeFirewalls200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeIP

> IPAddress getLinodeIP(linodeId, address)

IP Address View

View information about the specified IP address associated with the specified Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode to look up.
let address = "address_example"; // String | The IP address to look up.
apiInstance.getLinodeIP(linodeId, address, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode to look up. | 
 **address** | **String**| The IP address to look up. | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeIPs

> GetLinodeIPs200Response getLinodeIPs(linodeId)

Networking Information List

Returns networking information for a single Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
apiInstance.getLinodeIPs(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 

### Return type

[**GetLinodeIPs200Response**](GetLinodeIPs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeInstance

> Linode getLinodeInstance(linodeId)

Linode View

Get a specific Linode by ID.

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up
apiInstance.getLinodeInstance(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up | 

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeInstances

> GetLinodeInstances200Response getLinodeInstances(opts)

Linodes List

Returns a paginated list of Linodes you have permission to view. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLinodeInstances(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeInstances200Response**](GetLinodeInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeNodeBalancers

> GetLinodeNodeBalancers200Response getLinodeNodeBalancers(linodeId)

Linode NodeBalancers View

Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User&#39;s Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up
apiInstance.getLinodeNodeBalancers(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up | 

### Return type

[**GetLinodeNodeBalancers200Response**](GetLinodeNodeBalancers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeStats

> LinodeStats getLinodeStats(linodeId)

Linode Statistics View

Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
apiInstance.getLinodeStats(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 

### Return type

[**LinodeStats**](LinodeStats.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeStatsByYearMonth

> LinodeStats getLinodeStatsByYearMonth(linodeId, year, month)

Statistics View (year/month)

Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let year = 56; // Number | Numeric value representing the year to look up.
let month = 56; // Number | Numeric value representing the month to look up.
apiInstance.getLinodeStatsByYearMonth(linodeId, year, month, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **year** | **Number**| Numeric value representing the year to look up. | 
 **month** | **Number**| Numeric value representing the month to look up. | 

### Return type

[**LinodeStats**](LinodeStats.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeTransfer

> GetLinodeTransfer200Response getLinodeTransfer(linodeId)

Network Transfer View

Returns a Linode&#39;s network transfer pool statistics for the current month. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
apiInstance.getLinodeTransfer(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 

### Return type

[**GetLinodeTransfer200Response**](GetLinodeTransfer200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeTransferByYearMonth

> GetLinodeTransferByYearMonth200Response getLinodeTransferByYearMonth(linodeId, year, month)

Network Transfer View (year/month)

Returns a Linode&#39;s network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let year = 56; // Number | Numeric value representing the year to look up.
let month = 56; // Number | Numeric value representing the month to look up.
apiInstance.getLinodeTransferByYearMonth(linodeId, year, month, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **year** | **Number**| Numeric value representing the year to look up. | 
 **month** | **Number**| Numeric value representing the month to look up. | 

### Return type

[**GetLinodeTransferByYearMonth200Response**](GetLinodeTransferByYearMonth200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinodeVolumes

> GetLinodeVolumes200Response getLinodeVolumes(linodeId, opts)

Linode&#39;s Volumes List

View Block Storage Volumes attached to this Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getLinodeVolumes(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetLinodeVolumes200Response**](GetLinodeVolumes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrateLinodeInstance

> Object migrateLinodeInstance(linodeId, opts)

DC Migration/Pending Host Migration Initiate

Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a &#x60;region&#x60; parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 &#x60;/116&#x60; pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to migrate.
let opts = {
  'migrateLinodeInstanceRequest': new LinodeApi.MigrateLinodeInstanceRequest() // MigrateLinodeInstanceRequest | 
};
apiInstance.migrateLinodeInstance(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to migrate. | 
 **migrateLinodeInstanceRequest** | [**MigrateLinodeInstanceRequest**](MigrateLinodeInstanceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mutateLinodeInstance

> Object mutateLinodeInstance(linodeId, opts)

Linode Upgrade

Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to mutate.
let opts = {
  'mutateLinodeInstanceRequest': new LinodeApi.MutateLinodeInstanceRequest() // MutateLinodeInstanceRequest | Whether to automatically resize disks or not.
};
apiInstance.mutateLinodeInstance(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to mutate. | 
 **mutateLinodeInstanceRequest** | [**MutateLinodeInstanceRequest**](MutateLinodeInstanceRequest.md)| Whether to automatically resize disks or not. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rebootLinodeInstance

> Object rebootLinodeInstance(linodeId, opts)

Linode Reboot

Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the linode to reboot.
let opts = {
  'rebootLinodeInstanceRequest': new LinodeApi.RebootLinodeInstanceRequest() // RebootLinodeInstanceRequest | Optional reboot parameters.
};
apiInstance.rebootLinodeInstance(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the linode to reboot. | 
 **rebootLinodeInstanceRequest** | [**RebootLinodeInstanceRequest**](RebootLinodeInstanceRequest.md)| Optional reboot parameters. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rebuildLinodeInstance

> Linode rebuildLinodeInstance(linodeId, UNKNOWN_BASE_TYPE)

Linode Rebuild

Rebuilds a Linode you have the &#x60;read_write&#x60; permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new &#x60;image&#x60; to the Linode with the given attributes. Additionally:    * Requires an &#x60;image&#x60; be supplied.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the     &#x60;authorized_keys&#x60; field. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to rebuild.
let UNKNOWN_BASE_TYPE = {key: null}; // UNKNOWN_BASE_TYPE | The requested state your Linode will be rebuilt into.
apiInstance.rebuildLinodeInstance(linodeId, UNKNOWN_BASE_TYPE, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to rebuild. | 
 **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The requested state your Linode will be rebuilt into. | 

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeLinodeIP

> Object removeLinodeIP(linodeId, address)

IPv4 Address Delete

Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode&#39;s last remaining public IPv4 address. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode to look up.
let address = "address_example"; // String | The IP address to look up.
apiInstance.removeLinodeIP(linodeId, address, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode to look up. | 
 **address** | **String**| The IP address to look up. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rescueLinodeInstance

> Object rescueLinodeInstance(linodeId, opts)

Linode Boot into Rescue Mode

Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \&quot;sdh\&quot; is reserved and unavailable during rescue. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to rescue.
let opts = {
  'rescueLinodeInstanceRequest': new LinodeApi.RescueLinodeInstanceRequest() // RescueLinodeInstanceRequest | Optional object of devices to be mounted.
};
apiInstance.rescueLinodeInstance(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to rescue. | 
 **rescueLinodeInstanceRequest** | [**RescueLinodeInstanceRequest**](RescueLinodeInstanceRequest.md)| Optional object of devices to be mounted. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetDiskPassword

> Object resetDiskPassword(linodeId, diskId, resetDiskPasswordRequest)

Disk Root Password Reset

Resets the password of a Disk you have permission to &#x60;read_write&#x60;. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskId = 56; // Number | ID of the Disk to look up.
let resetDiskPasswordRequest = new LinodeApi.ResetDiskPasswordRequest(); // ResetDiskPasswordRequest | The new password.
apiInstance.resetDiskPassword(linodeId, diskId, resetDiskPasswordRequest, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskId** | **Number**| ID of the Disk to look up. | 
 **resetDiskPasswordRequest** | [**ResetDiskPasswordRequest**](ResetDiskPasswordRequest.md)| The new password. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetLinodePassword

> Object resetLinodePassword(linodeId, opts)

Linode Root Password Reset

Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk&#39;s root password. * A &#x60;password_reset&#x60; event is generated when a root password reset is successful. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode for which to reset its root password.
let opts = {
  'resetLinodePasswordRequest': new LinodeApi.ResetLinodePasswordRequest() // ResetLinodePasswordRequest | This Linode's new root password.
};
apiInstance.resetLinodePassword(linodeId, opts, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode for which to reset its root password. | 
 **resetLinodePasswordRequest** | [**ResetLinodePasswordRequest**](ResetLinodePasswordRequest.md)| This Linode&#39;s new root password. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resizeDisk

> Object resizeDisk(linodeId, diskId, resizeDiskRequest)

Disk Resize

Resizes a Disk you have permission to &#x60;read_write&#x60;.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode&#39;s active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskId = 56; // Number | ID of the Disk to look up.
let resizeDiskRequest = new LinodeApi.ResizeDiskRequest(); // ResizeDiskRequest | The new size of the Disk.
apiInstance.resizeDisk(linodeId, diskId, resizeDiskRequest, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskId** | **Number**| ID of the Disk to look up. | 
 **resizeDiskRequest** | [**ResizeDiskRequest**](ResizeDiskRequest.md)| The new size of the Disk. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resizeLinodeInstance

> Object resizeLinodeInstance(linodeId, resizeLinodeInstanceRequest)

Linode Resize

Resizes a Linode you have the &#x60;read_write&#x60; permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to resize.
let resizeLinodeInstanceRequest = new LinodeApi.ResizeLinodeInstanceRequest(); // ResizeLinodeInstanceRequest | The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode's disks. 
apiInstance.resizeLinodeInstance(linodeId, resizeLinodeInstanceRequest, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to resize. | 
 **resizeLinodeInstanceRequest** | [**ResizeLinodeInstanceRequest**](ResizeLinodeInstanceRequest.md)| The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode&#39;s disks.  | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## restoreBackup

> Object restoreBackup(linodeId, backupId, restoreBackupRequest)

Backup Restore

Restores a Linode&#39;s Backup to the specified Linode. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode that the Backup belongs to.
let backupId = 56; // Number | The ID of the Backup to restore.
let restoreBackupRequest = new LinodeApi.RestoreBackupRequest(); // RestoreBackupRequest | Parameters to provide when restoring the Backup.
apiInstance.restoreBackup(linodeId, backupId, restoreBackupRequest, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode that the Backup belongs to. | 
 **backupId** | **Number**| The ID of the Backup to restore. | 
 **restoreBackupRequest** | [**RestoreBackupRequest**](RestoreBackupRequest.md)| Parameters to provide when restoring the Backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shutdownLinodeInstance

> Object shutdownLinodeInstance(linodeId)

Linode Shut Down

Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to shutdown.
apiInstance.shutdownLinodeInstance(linodeId, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to shutdown. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDisk

> Disk updateDisk(linodeId, diskId, disk)

Disk Update

Updates a Disk that you have permission to &#x60;read_write&#x60;. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up.
let diskId = 56; // Number | ID of the Disk to look up.
let disk = new LinodeApi.Disk(); // Disk | Updates the parameters of a single Disk. 
apiInstance.updateDisk(linodeId, diskId, disk, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up. | 
 **diskId** | **Number**| ID of the Disk to look up. | 
 **disk** | [**Disk**](Disk.md)| Updates the parameters of a single Disk.  | 

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLinodeConfig

> LinodeConfig updateLinodeConfig(linodeId, configId, linodeConfig)

Configuration Profile Update

Updates a Configuration profile. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode whose Configuration profile to look up.
let configId = 56; // Number | The ID of the Configuration profile to look up.
let linodeConfig = new LinodeApi.LinodeConfig(); // LinodeConfig | The Configuration profile parameters to modify.
apiInstance.updateLinodeConfig(linodeId, configId, linodeConfig, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode whose Configuration profile to look up. | 
 **configId** | **Number**| The ID of the Configuration profile to look up. | 
 **linodeConfig** | [**LinodeConfig**](LinodeConfig.md)| The Configuration profile parameters to modify. | 

### Return type

[**LinodeConfig**](LinodeConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLinodeIP

> IPAddress updateLinodeIP(linodeId, address, opts)

IP Address Update

Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to &#x60;null&#x60; for a public IPv4 address, resets it to the default \&quot;ip.linodeusercontent.com\&quot; RDNS value. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | The ID of the Linode to look up.
let address = "address_example"; // String | The IP address to look up.
let opts = {
  'updateLinodeIPRequest': new LinodeApi.UpdateLinodeIPRequest() // UpdateLinodeIPRequest | The information to update for the IP address.
};
apiInstance.updateLinodeIP(linodeId, address, opts, (error, data, response) => {
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
 **linodeId** | **Number**| The ID of the Linode to look up. | 
 **address** | **String**| The IP address to look up. | 
 **updateLinodeIPRequest** | [**UpdateLinodeIPRequest**](UpdateLinodeIPRequest.md)| The information to update for the IP address. | [optional] 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLinodeInstance

> Linode updateLinodeInstance(linodeId, linode)

Linode Update

Updates a Linode that you have permission to &#x60;read_write&#x60;.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.LinodeInstancesApi();
let linodeId = 56; // Number | ID of the Linode to look up
let linode = new LinodeApi.Linode(); // Linode | Any field that is not marked as `readOnly` may be updated. Fields that are marked `readOnly` will be ignored. If any updated field fails to pass validation, the Linode will not be updated. 
apiInstance.updateLinodeInstance(linodeId, linode, (error, data, response) => {
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
 **linodeId** | **Number**| ID of the Linode to look up | 
 **linode** | [**Linode**](Linode.md)| Any field that is not marked as &#x60;readOnly&#x60; may be updated. Fields that are marked &#x60;readOnly&#x60; will be ignored. If any updated field fails to pass validation, the Linode will not be updated.  | 

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

