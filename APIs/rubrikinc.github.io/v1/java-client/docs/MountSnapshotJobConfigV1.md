

# MountSnapshotJobConfigV1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableNetwork** | **Boolean** | Sets the state of the network interfaces when the virtual machine is mounted or exported. Use &#39;false&#39; to enable the network interfaces. Use &#39;true&#39; to disable the network interfaces. Disabling the interfaces can prevent IP conflicts. |  [optional] |
|**keepMacAddresses** | **Boolean** | Determines whether the MAC addresses of the network interfaces on the source virtual machine are assigned to the new virtual machine. Set to &#39;true&#39; to assign the original MAC addresses to the new virtual machine. Set to &#39;false&#39; to assign new MAC addresses. The default is &#39;false&#39;. When removeNetworkDevices is set to true, this property is ignored. |  [optional] |
|**powerOn** | **Boolean** | Determines whether the virtual machine should be powered on after mount or export. Set to &#39;true&#39; to power on the virtual machine. Set to &#39;false&#39; to mount or export the virtual machine but not power it on. The default is &#39;true&#39;. |  [optional] |
|**removeNetworkDevices** | **Boolean** | Determines whether to remove the network interfaces from the mounted or exported virtual machine. Set to &#39;true&#39; to remove all network interfaces. The default value is &#39;false&#39;. |  [optional] |
|**vmName** | **String** | Name of the new VM created by mount or export. |  [optional] |
|**createDatastoreOnly** | **Boolean** | The job creates a datastore that contains the VMDK, but does not create the corresponding virtual machine. |  [optional] |
|**dataStoreName** | **String** | Obsolete parameter. |  [optional] |
|**hostId** | **String** | ID of the ESXi host to mount the new virtual machine on. |  [optional] |
|**shouldRecoverTags** | **Boolean** | The job recovers the tags that were assigned to the virtual machine. |  [optional] |
|**vlan** | **Integer** | VLAN ID for the VLAN ESXi host prefer to use for mounting the datastore. |  [optional] |



