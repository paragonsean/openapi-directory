

# ServersGet200ResponseServersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupWindow** | **String** | Time window (UTC) in which the backup will run, or null if the backups are not enabled |  |
|**created** | **String** | Point in time when the Resource was created (in ISO-8601 format) |  |
|**datacenter** | [**ServersGet200ResponseServersInnerDatacenter**](ServersGet200ResponseServersInnerDatacenter.md) |  |  |
|**id** | **Integer** | ID of the Resource |  |
|**image** | [**ServersGet200ResponseServersInnerImage**](ServersGet200ResponseServersInnerImage.md) |  |  |
|**includedTraffic** | **BigDecimal** | Free Traffic for the current billing period in bytes |  |
|**ingoingTraffic** | **BigDecimal** | Inbound Traffic for the current billing period in bytes |  |
|**iso** | [**ServersGet200ResponseServersInnerIso**](ServersGet200ResponseServersInnerIso.md) |  |  |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels (key-value pairs) |  |
|**loadBalancers** | **List&lt;Integer&gt;** |  |  [optional] |
|**locked** | **Boolean** | True if Server has been locked and is not available to user |  |
|**name** | **String** | Name of the Server (must be unique per Project and a valid hostname as per RFC 1123) |  |
|**outgoingTraffic** | **BigDecimal** | Outbound Traffic for the current billing period in bytes |  |
|**placementGroup** | [**PlacementGroupNullable**](PlacementGroupNullable.md) |  |  [optional] |
|**primaryDiskSize** | **BigDecimal** | Size of the primary Disk |  |
|**privateNet** | [**List&lt;ServersGet200ResponseServersInnerPrivateNetInner&gt;**](ServersGet200ResponseServersInnerPrivateNetInner.md) | Private networks information |  |
|**protection** | [**ServersGet200ResponseServersInnerProtection**](ServersGet200ResponseServersInnerProtection.md) |  |  |
|**publicNet** | [**ServersGet200ResponseServersInnerPublicNet**](ServersGet200ResponseServersInnerPublicNet.md) |  |  |
|**rescueEnabled** | **Boolean** | True if rescue mode is enabled. Server will then boot into rescue system on next reboot |  |
|**serverType** | [**ServersGet200ResponseServersInnerServerType**](ServersGet200ResponseServersInnerServerType.md) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Server |  |
|**volumes** | **List&lt;Integer&gt;** | IDs of Volumes assigned to this Server |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;running&quot; |
| INITIALIZING | &quot;initializing&quot; |
| STARTING | &quot;starting&quot; |
| STOPPING | &quot;stopping&quot; |
| FALSE | &quot;false&quot; |
| DELETING | &quot;deleting&quot; |
| MIGRATING | &quot;migrating&quot; |
| REBUILDING | &quot;rebuilding&quot; |
| UNKNOWN | &quot;unknown&quot; |



