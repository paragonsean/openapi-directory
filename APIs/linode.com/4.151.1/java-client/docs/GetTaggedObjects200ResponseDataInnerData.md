

# GetTaggedObjects200ResponseDataInnerData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alerts** | [**LinodeAlerts**](LinodeAlerts.md) |  |  [optional] |
|**backups** | [**LinodeBackups**](LinodeBackups.md) |  |  [optional] |
|**created** | **OffsetDateTime** | When this NodeBalancer was created.  |  [optional] [readonly] |
|**group** | **String** | The group this Domain belongs to.  This is for display purposes only.  |  [optional] |
|**hostUuid** | **UUID** | The Linode&#39;s host machine, as a UUID. |  [optional] [readonly] |
|**hypervisor** | [**HypervisorEnum**](#HypervisorEnum) | The virtualization software powering this Linode.  |  [optional] [readonly] |
|**id** | **Integer** | This NodeBalancer&#39;s unique ID.  |  [optional] [readonly] |
|**image** | **String** |  |  [optional] [readonly] |
|**ipv4** | **String** | This NodeBalancer&#39;s public IPv4 address.  |  [optional] [readonly] |
|**ipv6** | **String** | This NodeBalancer&#39;s public IPv6 address.  |  [optional] [readonly] |
|**label** | **String** | This NodeBalancer&#39;s label. These must be unique on your Account.  |  [optional] |
|**region** | **String** | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.  |  [optional] [readonly] |
|**specs** | [**LinodeSpecs**](LinodeSpecs.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the volume.  Can be one of:    * &#x60;creating&#x60; - the Volume is being created and is not yet available     for use.   * &#x60;active&#x60; - the Volume is online and available for use.   * &#x60;resizing&#x60; - the Volume is in the process of upgrading     its current capacity.  |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | An array of Tags applied to this object.  Tags are for organizational purposes only.  |  [optional] |
|**type** | **String** | This is the [Linode Type](/docs/api/linode-types/#types-list) that this Linode was deployed with. To change a Linode&#39;s Type, use [POST /linode/instances/{linodeId}/resize](/docs/api/linode-instances/#linode-resize).  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** | When this NodeBalancer was last updated.  |  [optional] [readonly] |
|**watchdogEnabled** | **Boolean** | The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.  |  [optional] |
|**axfrIps** | **List&lt;String&gt;** | The list of IPs that may perform a zone transfer for this Domain. The total combined length of all data within this array cannot exceed 1000 characters.  **Note**: This is potentially dangerous, and should be set to an empty list unless you intend to use it.  |  [optional] |
|**description** | **String** | A description for this Domain. This is for display purposes only.  |  [optional] |
|**domain** | **String** | The domain this Domain represents. Domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). Domains must be unique on Linode&#39;s platform, including across different Linode accounts; there cannot be two Domains representing the same domain.  |  [optional] |
|**expireSec** | **Integer** | The amount of time in seconds that may pass before this Domain is no longer authoritative.  * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  * Any other value is rounded up to the nearest valid value.  * A value of 0 is equivalent to the default value of 1209600.  |  [optional] |
|**masterIps** | **List&lt;String&gt;** | The IP addresses representing the master DNS for this Domain. At least one value is required for &#x60;type&#x60; slave Domains. The total combined length of all data within this array cannot exceed 1000 characters.  |  [optional] |
|**refreshSec** | **Integer** | The amount of time in seconds before this Domain should be refreshed.  * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  * Any other value is rounded up to the nearest valid value.  * A value of 0 is equivalent to the default value of 14400.  |  [optional] |
|**retrySec** | **Integer** | The interval, in seconds, at which a failed refresh should be retried.  * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  * Any other value is rounded up to the nearest valid value.  * A value of 0 is equivalent to the default value of 14400.  |  [optional] |
|**soaEmail** | **String** | Start of Authority email address. This is required for &#x60;type&#x60; master Domains.  |  [optional] |
|**ttlSec** | **Integer** | \&quot;Time to Live\&quot; - the amount of time in seconds that this Domain&#39;s records may be cached by resolvers or other domain servers. * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200. * Any other value is rounded up to the nearest valid value. * A value of 0 is equivalent to the default value of 86400.  |  [optional] |
|**filesystemPath** | **String** | The full filesystem path for the Volume based on the Volume&#39;s label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label.  |  [optional] [readonly] |
|**hardwareType** | [**HardwareTypeEnum**](#HardwareTypeEnum) | The storage type of this Volume. |  [optional] [readonly] |
|**linodeId** | **Integer** | If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here.  |  [optional] |
|**linodeLabel** | **String** | If a Volume is attached to a specific Linode, the label of that Linode will be displayed here.  |  [optional] [readonly] |
|**size** | **Integer** | The Volume&#39;s size, in GiB.  |  [optional] |
|**clientConnThrottle** | **Integer** | Throttle connections per second.  Set to 0 (zero) to disable throttling.  |  [optional] |
|**hostname** | **String** | This NodeBalancer&#39;s hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.  |  [optional] [readonly] |
|**transfer** | [**NodeBalancerTransfer**](NodeBalancerTransfer.md) |  |  [optional] |



## Enum: HypervisorEnum

| Name | Value |
|---- | -----|
| KVM | &quot;kvm&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;creating&quot; |
| ACTIVE | &quot;active&quot; |
| RESIZING | &quot;resizing&quot; |



## Enum: HardwareTypeEnum

| Name | Value |
|---- | -----|
| HDD | &quot;hdd&quot; |
| NVME | &quot;nvme&quot; |



