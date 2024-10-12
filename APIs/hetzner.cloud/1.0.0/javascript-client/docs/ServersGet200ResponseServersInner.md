# HetznerCloudApi.ServersGet200ResponseServersInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupWindow** | **String** | Time window (UTC) in which the backup will run, or null if the backups are not enabled | 
**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) | 
**datacenter** | [**ServersGet200ResponseServersInnerDatacenter**](ServersGet200ResponseServersInnerDatacenter.md) |  | 
**id** | **Number** | ID of the Resource | 
**image** | [**ServersGet200ResponseServersInnerImage**](ServersGet200ResponseServersInnerImage.md) |  | 
**includedTraffic** | **Number** | Free Traffic for the current billing period in bytes | 
**ingoingTraffic** | **Number** | Inbound Traffic for the current billing period in bytes | 
**iso** | [**ServersGet200ResponseServersInnerIso**](ServersGet200ResponseServersInnerIso.md) |  | 
**labels** | **{String: String}** | User-defined labels (key-value pairs) | 
**loadBalancers** | **[Number]** |  | [optional] 
**locked** | **Boolean** | True if Server has been locked and is not available to user | 
**name** | **String** | Name of the Server (must be unique per Project and a valid hostname as per RFC 1123) | 
**outgoingTraffic** | **Number** | Outbound Traffic for the current billing period in bytes | 
**placementGroup** | [**PlacementGroupNullable**](PlacementGroupNullable.md) |  | [optional] 
**primaryDiskSize** | **Number** | Size of the primary Disk | 
**privateNet** | [**[ServersGet200ResponseServersInnerPrivateNetInner]**](ServersGet200ResponseServersInnerPrivateNetInner.md) | Private networks information | 
**protection** | [**ServersGet200ResponseServersInnerProtection**](ServersGet200ResponseServersInnerProtection.md) |  | 
**publicNet** | [**ServersGet200ResponseServersInnerPublicNet**](ServersGet200ResponseServersInnerPublicNet.md) |  | 
**rescueEnabled** | **Boolean** | True if rescue mode is enabled. Server will then boot into rescue system on next reboot | 
**serverType** | [**ServersGet200ResponseServersInnerServerType**](ServersGet200ResponseServersInnerServerType.md) |  | 
**status** | **String** | Status of the Server | 
**volumes** | **[Number]** | IDs of Volumes assigned to this Server | [optional] 



## Enum: StatusEnum


* `running` (value: `"running"`)

* `initializing` (value: `"initializing"`)

* `starting` (value: `"starting"`)

* `stopping` (value: `"stopping"`)

* `false` (value: `"false"`)

* `deleting` (value: `"deleting"`)

* `migrating` (value: `"migrating"`)

* `rebuilding` (value: `"rebuilding"`)

* `unknown` (value: `"unknown"`)




