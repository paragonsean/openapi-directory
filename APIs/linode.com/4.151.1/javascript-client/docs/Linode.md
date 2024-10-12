# LinodeApi.Linode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**LinodeAlerts**](LinodeAlerts.md) |  | [optional] 
**backups** | [**LinodeBackups**](LinodeBackups.md) |  | [optional] 
**created** | **Date** | When this Linode was created. | [optional] [readonly] 
**group** | **String** | A deprecated property denoting a group label for this Linode.  | [optional] 
**hostUuid** | **String** | The Linode&#39;s host machine, as a UUID. | [optional] [readonly] 
**hypervisor** | **String** | The virtualization software powering this Linode.  | [optional] [readonly] 
**id** | **Number** | This Linode&#39;s ID which must be provided for all operations impacting this Linode.  | [optional] [readonly] 
**image** | **String** |  | [optional] [readonly] 
**ipv4** | **[String]** | This Linode&#39;s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single private IPv4 address if needed. You may need to [open a support ticket](/docs/api/support/#support-ticket-open) to get additional IPv4 addresses.  IPv4 addresses may be reassigned between your Linodes, or shared with other Linodes. See the [/networking](/docs/api/networking/) endpoints for details.  | [optional] [readonly] 
**ipv6** | **String** | This Linode&#39;s IPv6 SLAAC address. This address is specific to a Linode, and may not be shared. If the Linode has not been assigned an IPv6 address, the return value will be &#x60;null&#x60;.  | [optional] [readonly] 
**label** | **String** | The Linode&#39;s label is for display purposes only. If no label is provided for a Linode, a default will be assigned.  Linode labels have the following constraints:    * Must begin and end with an alphanumeric character.   * May only consist of alphanumeric characters, dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   * Cannot have two dashes (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row.  | [optional] 
**region** | **String** | This is the [Region](/docs/api/regions/#regions-list) where the Linode was deployed. A Linode&#39;s region can only be changed by initiating a [cross data center migration](/docs/api/linode-instances/#dc-migrationpending-host-migration-initiate).  | [optional] [readonly] 
**specs** | [**LinodeSpecs**](LinodeSpecs.md) |  | [optional] 
**status** | **String** | A brief description of this Linode&#39;s current state. This field may change without direct action from you. For example, when a Linode goes into maintenance mode its status will display \&quot;stopped\&quot;.  | [optional] [readonly] 
**tags** | **[String]** | An array of tags applied to this object.  Tags are for organizational purposes only.  | [optional] 
**type** | **String** | This is the [Linode Type](/docs/api/linode-types/#types-list) that this Linode was deployed with. To change a Linode&#39;s Type, use [POST /linode/instances/{linodeId}/resize](/docs/api/linode-instances/#linode-resize).  | [optional] [readonly] 
**updated** | **Date** | When this Linode was last updated. | [optional] [readonly] 
**watchdogEnabled** | **Boolean** | The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and will reboot it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie will give up if there have been more than 5 boot jobs issued within 15 minutes.  | [optional] 



## Enum: HypervisorEnum


* `kvm` (value: `"kvm"`)





## Enum: StatusEnum


* `running` (value: `"running"`)

* `offline` (value: `"offline"`)

* `booting` (value: `"booting"`)

* `rebooting` (value: `"rebooting"`)

* `shutting_down` (value: `"shutting_down"`)

* `provisioning` (value: `"provisioning"`)

* `deleting` (value: `"deleting"`)

* `migrating` (value: `"migrating"`)

* `rebuilding` (value: `"rebuilding"`)

* `cloning` (value: `"cloning"`)

* `restoring` (value: `"restoring"`)

* `stopped` (value: `"stopped"`)




