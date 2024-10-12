# HetznerCloudApi.ServerActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serversIdActionsActionIdGet**](ServerActionsApi.md#serversIdActionsActionIdGet) | **GET** /servers/{id}/actions/{action_id} | Get an Action for a Server
[**serversIdActionsAddToPlacementGroupPost**](ServerActionsApi.md#serversIdActionsAddToPlacementGroupPost) | **POST** /servers/{id}/actions/add_to_placement_group | Add a Server to a Placement Group
[**serversIdActionsAttachIsoPost**](ServerActionsApi.md#serversIdActionsAttachIsoPost) | **POST** /servers/{id}/actions/attach_iso | Attach an ISO to a Server
[**serversIdActionsAttachToNetworkPost**](ServerActionsApi.md#serversIdActionsAttachToNetworkPost) | **POST** /servers/{id}/actions/attach_to_network | Attach a Server to a Network
[**serversIdActionsChangeAliasIpsPost**](ServerActionsApi.md#serversIdActionsChangeAliasIpsPost) | **POST** /servers/{id}/actions/change_alias_ips | Change alias IPs of a Network
[**serversIdActionsChangeDnsPtrPost**](ServerActionsApi.md#serversIdActionsChangeDnsPtrPost) | **POST** /servers/{id}/actions/change_dns_ptr | Change reverse DNS entry for this Server
[**serversIdActionsChangeProtectionPost**](ServerActionsApi.md#serversIdActionsChangeProtectionPost) | **POST** /servers/{id}/actions/change_protection | Change Server Protection
[**serversIdActionsChangeTypePost**](ServerActionsApi.md#serversIdActionsChangeTypePost) | **POST** /servers/{id}/actions/change_type | Change the Type of a Server
[**serversIdActionsCreateImagePost**](ServerActionsApi.md#serversIdActionsCreateImagePost) | **POST** /servers/{id}/actions/create_image | Create Image from a Server
[**serversIdActionsDetachFromNetworkPost**](ServerActionsApi.md#serversIdActionsDetachFromNetworkPost) | **POST** /servers/{id}/actions/detach_from_network | Detach a Server from a Network
[**serversIdActionsDetachIsoPost**](ServerActionsApi.md#serversIdActionsDetachIsoPost) | **POST** /servers/{id}/actions/detach_iso | Detach an ISO from a Server
[**serversIdActionsDisableBackupPost**](ServerActionsApi.md#serversIdActionsDisableBackupPost) | **POST** /servers/{id}/actions/disable_backup | Disable Backups for a Server
[**serversIdActionsDisableRescuePost**](ServerActionsApi.md#serversIdActionsDisableRescuePost) | **POST** /servers/{id}/actions/disable_rescue | Disable Rescue Mode for a Server
[**serversIdActionsEnableBackupPost**](ServerActionsApi.md#serversIdActionsEnableBackupPost) | **POST** /servers/{id}/actions/enable_backup | Enable and Configure Backups for a Server
[**serversIdActionsEnableRescuePost**](ServerActionsApi.md#serversIdActionsEnableRescuePost) | **POST** /servers/{id}/actions/enable_rescue | Enable Rescue Mode for a Server
[**serversIdActionsGet**](ServerActionsApi.md#serversIdActionsGet) | **GET** /servers/{id}/actions | Get all Actions for a Server
[**serversIdActionsPoweroffPost**](ServerActionsApi.md#serversIdActionsPoweroffPost) | **POST** /servers/{id}/actions/poweroff | Power off a Server
[**serversIdActionsPoweronPost**](ServerActionsApi.md#serversIdActionsPoweronPost) | **POST** /servers/{id}/actions/poweron | Power on a Server
[**serversIdActionsRebootPost**](ServerActionsApi.md#serversIdActionsRebootPost) | **POST** /servers/{id}/actions/reboot | Soft-reboot a Server
[**serversIdActionsRebuildPost**](ServerActionsApi.md#serversIdActionsRebuildPost) | **POST** /servers/{id}/actions/rebuild | Rebuild a Server from an Image
[**serversIdActionsRemoveFromPlacementGroupPost**](ServerActionsApi.md#serversIdActionsRemoveFromPlacementGroupPost) | **POST** /servers/{id}/actions/remove_from_placement_group | Remove from Placement Group
[**serversIdActionsRequestConsolePost**](ServerActionsApi.md#serversIdActionsRequestConsolePost) | **POST** /servers/{id}/actions/request_console | Request Console for a Server
[**serversIdActionsResetPasswordPost**](ServerActionsApi.md#serversIdActionsResetPasswordPost) | **POST** /servers/{id}/actions/reset_password | Reset root Password of a Server
[**serversIdActionsResetPost**](ServerActionsApi.md#serversIdActionsResetPost) | **POST** /servers/{id}/actions/reset | Reset a Server
[**serversIdActionsShutdownPost**](ServerActionsApi.md#serversIdActionsShutdownPost) | **POST** /servers/{id}/actions/shutdown | Shutdown a Server



## serversIdActionsActionIdGet

> ActionResponse serversIdActionsActionIdGet(id, actionId)

Get an Action for a Server

Returns a specific Action object for a Server.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let actionId = 56; // Number | ID of the Action
apiInstance.serversIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsAddToPlacementGroupPost

> ActionResponse serversIdActionsAddToPlacementGroupPost(id, opts)

Add a Server to a Placement Group

Adds a Server to a Placement Group.  Server must be powered off for this command to succeed.  #### Call specific error codes  | Code                          | Description                                                          | |-------------------------------|----------------------------------------------------------------------| | &#x60;server_not_stopped&#x60;          | The action requires a stopped server                                 | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'addToPlacementGroupRequest': new HetznerCloudApi.AddToPlacementGroupRequest() // AddToPlacementGroupRequest | 
};
apiInstance.serversIdActionsAddToPlacementGroupPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **addToPlacementGroupRequest** | [**AddToPlacementGroupRequest**](AddToPlacementGroupRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsAttachIsoPost

> ActionResponse serversIdActionsAttachIsoPost(id, opts)

Attach an ISO to a Server

Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already attached ISO will automatically be detached before the new ISO is attached.  Servers with attached ISOs have a modified boot order: They will try to boot from the ISO first before falling back to hard disk. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'serversIdActionsAttachIsoPostRequest': new HetznerCloudApi.ServersIdActionsAttachIsoPostRequest() // ServersIdActionsAttachIsoPostRequest | 
};
apiInstance.serversIdActionsAttachIsoPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **serversIdActionsAttachIsoPostRequest** | [**ServersIdActionsAttachIsoPostRequest**](ServersIdActionsAttachIsoPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsAttachToNetworkPost

> ActionResponse serversIdActionsAttachToNetworkPost(id, opts)

Attach a Server to a Network

Attaches a Server to a network. This will complement the fixed public Server interface by adding an additional ethernet interface to the Server which is connected to the specified network.  The Server will get an IP auto assigned from a subnet of type &#x60;server&#x60; in the same &#x60;network_zone&#x60;.  Using the &#x60;alias_ips&#x60; attribute you can also define one or more additional IPs to the Servers. Please note that you will have to configure these IPs by hand on your Server since only the primary IP will be given out by DHCP.  **Call specific error codes**  | Code                             | Description                                                           | |----------------------------------|-----------------------------------------------------------------------| | &#x60;server_already_attached&#x60;        | The server is already attached to the network                         | | &#x60;ip_not_available&#x60;               | The provided Network IP is not available                              | | &#x60;no_subnet_available&#x60;            | No Subnet or IP is available for the Server within the network        | | &#x60;networks_overlap&#x60;               | The network IP range overlaps with one of the server networks         | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'attachToNetworkRequest': new HetznerCloudApi.AttachToNetworkRequest() // AttachToNetworkRequest | 
};
apiInstance.serversIdActionsAttachToNetworkPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **attachToNetworkRequest** | [**AttachToNetworkRequest**](AttachToNetworkRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsChangeAliasIpsPost

> ActionResponse serversIdActionsChangeAliasIpsPost(id, opts)

Change alias IPs of a Network

Changes the alias IPs of an already attached Network. Note that the existing aliases for the specified Network will be replaced with these provided in the request body. So if you want to add an alias IP, you have to provide the existing ones from the Network plus the new alias IP in the request body.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'serversIdActionsChangeAliasIpsPostRequest': new HetznerCloudApi.ServersIdActionsChangeAliasIpsPostRequest() // ServersIdActionsChangeAliasIpsPostRequest | 
};
apiInstance.serversIdActionsChangeAliasIpsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **serversIdActionsChangeAliasIpsPostRequest** | [**ServersIdActionsChangeAliasIpsPostRequest**](ServersIdActionsChangeAliasIpsPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsChangeDnsPtrPost

> ActionResponse serversIdActionsChangeDnsPtrPost(id, opts)

Change reverse DNS entry for this Server

Changes the hostname that will appear when getting the hostname belonging to the primary IPs (IPv4 and IPv6) of this Server.  Floating IPs assigned to the Server are not affected by this. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'serversIdActionsChangeDnsPtrPostRequest': new HetznerCloudApi.ServersIdActionsChangeDnsPtrPostRequest() // ServersIdActionsChangeDnsPtrPostRequest | Select the IP address for which to change the DNS entry by passing `ip`. It can be either IPv4 or IPv6. The target hostname is set by passing `dns_ptr`.
};
apiInstance.serversIdActionsChangeDnsPtrPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **serversIdActionsChangeDnsPtrPostRequest** | [**ServersIdActionsChangeDnsPtrPostRequest**](ServersIdActionsChangeDnsPtrPostRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. It can be either IPv4 or IPv6. The target hostname is set by passing &#x60;dns_ptr&#x60;. | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsChangeProtectionPost

> ActionResponse serversIdActionsChangeProtectionPost(id, opts)

Change Server Protection

Changes the protection configuration of the Server.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'serversIdActionsChangeProtectionPostRequest': new HetznerCloudApi.ServersIdActionsChangeProtectionPostRequest() // ServersIdActionsChangeProtectionPostRequest | 
};
apiInstance.serversIdActionsChangeProtectionPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **serversIdActionsChangeProtectionPostRequest** | [**ServersIdActionsChangeProtectionPostRequest**](ServersIdActionsChangeProtectionPostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsChangeTypePost

> ActionResponse serversIdActionsChangeTypePost(id, opts)

Change the Type of a Server

Changes the type (Cores, RAM and disk sizes) of a Server.  Server must be powered off for this command to succeed.  This copies the content of its disk, and starts it again.  You can only migrate to Server types with the same &#x60;storage_type&#x60; and equal or bigger disks. Shrinking disks is not possible as it might destroy data.  If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to downgrade the Server type, set &#x60;upgrade_disk&#x60; to &#x60;false&#x60;.  #### Call specific error codes  | Code                          | Description                                                          | |-------------------------------|----------------------------------------------------------------------| | &#x60;invalid_server_type&#x60;         | The server type does not fit for the given server or is deprecated   | | &#x60;server_not_stopped&#x60;          | The action requires a stopped server                                 | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'serversIdActionsChangeTypePostRequest': new HetznerCloudApi.ServersIdActionsChangeTypePostRequest() // ServersIdActionsChangeTypePostRequest | 
};
apiInstance.serversIdActionsChangeTypePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **serversIdActionsChangeTypePostRequest** | [**ServersIdActionsChangeTypePostRequest**](ServersIdActionsChangeTypePostRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsCreateImagePost

> ServersIdActionsCreateImagePost201Response serversIdActionsCreateImagePost(id, opts)

Create Image from a Server

Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates a snapshot of the current state of the disk and copies it into an Image. If the Server is currently running you must make sure that its disk content is consistent. Otherwise, the created Image may not be readable.  To make sure disk content is consistent, we recommend to shut down the Server prior to creating an Image.  You can either create a &#x60;backup&#x60; Image that is bound to the Server and therefore will be deleted when the Server is deleted, or you can create an &#x60;snapshot&#x60; Image which is completely independent of the Server it was created from and will survive Server deletion. Backup Images are only available when the backup option is enabled for the Server. Snapshot Images are billed on a per GB basis. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'createImageRequest': new HetznerCloudApi.CreateImageRequest() // CreateImageRequest | 
};
apiInstance.serversIdActionsCreateImagePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **createImageRequest** | [**CreateImageRequest**](CreateImageRequest.md)|  | [optional] 

### Return type

[**ServersIdActionsCreateImagePost201Response**](ServersIdActionsCreateImagePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsDetachFromNetworkPost

> ActionResponse serversIdActionsDetachFromNetworkPost(id, opts)

Detach a Server from a Network

Detaches a Server from a network. The interface for this network will vanish.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'detachFromNetworkRequest': new HetznerCloudApi.DetachFromNetworkRequest() // DetachFromNetworkRequest | 
};
apiInstance.serversIdActionsDetachFromNetworkPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **detachFromNetworkRequest** | [**DetachFromNetworkRequest**](DetachFromNetworkRequest.md)|  | [optional] 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsDetachIsoPost

> ActionResponse serversIdActionsDetachIsoPost(id)

Detach an ISO from a Server

Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of the returned Action is immediately set to &#x60;success&#x60;

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsDetachIsoPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsDisableBackupPost

> ActionResponse serversIdActionsDisableBackupPost(id)

Disable Backups for a Server

Disables the automatic backup option and deletes all existing Backups for a Server. No more additional charges for backups will be made.  Caution: This immediately removes all existing backups for the Server! 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsDisableBackupPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsDisableRescuePost

> ActionResponse serversIdActionsDisableRescuePost(id)

Disable Rescue Mode for a Server

Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on next reboot.  Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.  Disabling rescue mode will not reboot your Server — you will have to do this yourself. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsDisableRescuePost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsEnableBackupPost

> ActionResponse serversIdActionsEnableBackupPost(id)

Enable and Configure Backups for a Server

Enables and configures the automatic daily backup option for the Server. Enabling automatic backups will increase the price of the Server by 20%. In return, you will get seven slots where Images of type backup can be stored.  Backups are automatically created daily. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsEnableBackupPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsEnableRescuePost

> ServersIdActionsEnableRescuePost201Response serversIdActionsEnableRescuePost(id, opts)

Enable Rescue Mode for a Server

Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue mode boots it will start a special minimal Linux distribution designed for repair and reinstall.  In case a Server cannot boot on its own you can use this to access a Server’s disks.  Rescue Mode is automatically disabled when you first boot into it or if you do not use it for 60 minutes.  Enabling rescue mode will not [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server — you will have to do this yourself. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'serversIdActionsEnableRescuePostRequest': new HetznerCloudApi.ServersIdActionsEnableRescuePostRequest() // ServersIdActionsEnableRescuePostRequest | 
};
apiInstance.serversIdActionsEnableRescuePost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **serversIdActionsEnableRescuePostRequest** | [**ServersIdActionsEnableRescuePostRequest**](ServersIdActionsEnableRescuePostRequest.md)|  | [optional] 

### Return type

[**ServersIdActionsEnableRescuePost201Response**](ServersIdActionsEnableRescuePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsGet

> ActionsResponse serversIdActionsGet(id, opts)

Get all Actions for a Server

Returns all Action objects for a Server. You can &#x60;sort&#x60; the results by using the sort URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Resource
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.serversIdActionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Resource | 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsPoweroffPost

> ActionResponse serversIdActionsPoweroffPost(id)

Power off a Server

Cuts power to the Server. This forcefully stops it without giving the Server operating system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord. Power off should only be used when shutdown does not work.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsPoweroffPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsPoweronPost

> ActionResponse serversIdActionsPoweronPost(id)

Power on a Server

Starts a Server by turning its power on.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsPoweronPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsRebootPost

> ActionResponse serversIdActionsRebootPost(id)

Soft-reboot a Server

Reboots a Server gracefully by sending an ACPI request. The Server operating system must support ACPI and react to the request, otherwise the Server will not reboot.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsRebootPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsRebuildPost

> ServersIdActionsRebuildPost201Response serversIdActionsRebuildPost(id, opts)

Rebuild a Server from an Image

Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying all data** on the target Server  The Image can either be one you have created earlier (&#x60;backup&#x60; or &#x60;snapshot&#x60; Image) or it can be a completely fresh &#x60;system&#x60; Image provided by us. You can get a list of all available Images with &#x60;GET /images&#x60;.  Your Server will automatically be powered off before the rebuild command executes. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
let opts = {
  'rebuildServerRequest': new HetznerCloudApi.RebuildServerRequest() // RebuildServerRequest | To select which Image to rebuild from you can either pass an ID or a name as the `image` argument. Passing a name only works for `system` Images since the other Image types do not have a name set.
};
apiInstance.serversIdActionsRebuildPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 
 **rebuildServerRequest** | [**RebuildServerRequest**](RebuildServerRequest.md)| To select which Image to rebuild from you can either pass an ID or a name as the &#x60;image&#x60; argument. Passing a name only works for &#x60;system&#x60; Images since the other Image types do not have a name set. | [optional] 

### Return type

[**ServersIdActionsRebuildPost201Response**](ServersIdActionsRebuildPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serversIdActionsRemoveFromPlacementGroupPost

> ActionResponse serversIdActionsRemoveFromPlacementGroupPost(id)

Remove from Placement Group

Removes a Server from a Placement Group. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsRemoveFromPlacementGroupPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsRequestConsolePost

> ServersIdActionsRequestConsolePost201Response serversIdActionsRequestConsolePost(id)

Request Console for a Server

Requests credentials for remote access via VNC over websocket to keyboard, monitor, and mouse for a Server. The provided URL is valid for 1 minute, after this period a new url needs to be created to connect to the Server. How long the connection is open after the initial connect is not subject to this timeout.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsRequestConsolePost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ServersIdActionsRequestConsolePost201Response**](ServersIdActionsRequestConsolePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsResetPasswordPost

> ServersIdActionsEnableRescuePost201Response serversIdActionsResetPasswordPost(id)

Reset root Password of a Server

Resets the root password. Only works for Linux systems that are running the qemu guest agent. Server must be powered on (status &#x60;running&#x60;) in order for this operation to succeed.  This will generate a new password for this Server and return it.  If this does not succeed you can use the rescue system to netboot the Server and manually change your Server password by hand. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsResetPasswordPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ServersIdActionsEnableRescuePost201Response**](ServersIdActionsEnableRescuePost201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsResetPost

> ActionResponse serversIdActionsResetPost(id)

Reset a Server

Cuts power to a Server and starts it again. This forcefully stops it without giving the Server operating system time to gracefully stop. This may lead to data loss, it’s equivalent to pulling the power cord and plugging it in again. Reset should only be used when reboot does not work.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsResetPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serversIdActionsShutdownPost

> ActionResponse serversIdActionsShutdownPost(id)

Shutdown a Server

Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating system must support ACPI and react to the request, otherwise the Server will not shut down.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.ServerActionsApi();
let id = 56; // Number | ID of the Server
apiInstance.serversIdActionsShutdownPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Server | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

