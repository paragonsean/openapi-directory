

# LinodeConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** | Optional field for arbitrary User comments on this Config. |  [optional] |
|**devices** | [**Devices**](Devices.md) |  |  [optional] |
|**helpers** | [**LinodeConfigHelpers**](LinodeConfigHelpers.md) |  |  [optional] |
|**id** | **Integer** | The ID of this Config. |  [optional] [readonly] |
|**interfaces** | [**List&lt;LinodeConfigInterface&gt;**](LinodeConfigInterface.md) | An array of Network Interfaces to add to this Linode&#39;s Configuration Profile.  Up to three interface objects can be entered in this array. The position in the array determines the interface to which the settings apply:  - First/0:  eth0 - Second/1: eth1 - Third/2:  eth2  When updating a Linode&#39;s interfaces, *each interface must be redefined*. An empty interfaces array results in a default public interface configuration only.  If no public interface is configured, public IP addresses are still assigned to the Linode but will not be usable without manual configuration.  **Note:** Changes to Linode interface configurations can be enabled by rebooting the Linode.  **Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  **Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) guide to view additional specifications and limitations.  |  [optional] |
|**kernel** | **String** | A Kernel ID to boot a Linode with. Defaults to \&quot;linode/latest-64bit\&quot;. |  [optional] |
|**label** | **String** | The Config&#39;s label is for display purposes only.  |  [optional] |
|**memoryLimit** | **Integer** | Defaults to the total RAM of the Linode.  |  [optional] |
|**rootDevice** | **String** | The root device to boot. * If no value or an invalid value is provided, root device will default to &#x60;/dev/sda&#x60;. * If the device specified at the root device location is not mounted, the Linode will not boot until a device is mounted.  |  [optional] |
|**runLevel** | [**RunLevelEnum**](#RunLevelEnum) | Defines the state of your Linode after booting. Defaults to &#x60;default&#x60;.  |  [optional] |
|**virtMode** | [**VirtModeEnum**](#VirtModeEnum) | Controls the virtualization mode. Defaults to &#x60;paravirt&#x60;. * &#x60;paravirt&#x60; is suitable for most cases. Linodes running in paravirt mode   share some qualities with the host, ultimately making it run faster since   there is less transition between it and the host. * &#x60;fullvirt&#x60; affords more customization, but is slower because 100% of the VM   is virtualized.  |  [optional] |



## Enum: RunLevelEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;default&quot; |
| SINGLE | &quot;single&quot; |
| BINBASH | &quot;binbash&quot; |



## Enum: VirtModeEnum

| Name | Value |
|---- | -----|
| PARAVIRT | &quot;paravirt&quot; |
| FULLVIRT | &quot;fullvirt&quot; |



