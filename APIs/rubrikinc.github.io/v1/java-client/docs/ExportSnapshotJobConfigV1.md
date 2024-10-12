

# ExportSnapshotJobConfigV1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableNetwork** | **Boolean** | Sets the state of the network interfaces when the virtual machine is mounted or exported. Use &#39;false&#39; to enable the network interfaces. Use &#39;true&#39; to disable the network interfaces. Disabling the interfaces can prevent IP conflicts. |  [optional] |
|**keepMacAddresses** | **Boolean** | Determines whether the MAC addresses of the network interfaces on the source virtual machine are assigned to the new virtual machine. Set to &#39;true&#39; to assign the original MAC addresses to the new virtual machine. Set to &#39;false&#39; to assign new MAC addresses. The default is &#39;false&#39;. When removeNetworkDevices is set to true, this property is ignored. |  [optional] |
|**powerOn** | **Boolean** | Determines whether the virtual machine should be powered on after mount or export. Set to &#39;true&#39; to power on the virtual machine. Set to &#39;false&#39; to mount or export the virtual machine but not power it on. The default is &#39;true&#39;. |  [optional] |
|**removeNetworkDevices** | **Boolean** | Determines whether to remove the network interfaces from the mounted or exported virtual machine. Set to &#39;true&#39; to remove all network interfaces. The default value is &#39;false&#39;. |  [optional] |
|**vmName** | **String** | Name of the new VM created by mount or export. |  [optional] |
|**datastoreId** | **String** | ID of the datastore to assign to the exported virtual machine. |  |
|**hostId** | **String** | ID of the ESXi host to export the new virtual machine to. |  [optional] |
|**shouldRecoverTags** | **Boolean** | The job recovers any tags that were assigned to the virtual machine. |  [optional] |
|**unregisterVm** | **Boolean** | Determines whether the new virtual machine created from a snapshot is registered with the vCenter Server. Use &#39;true&#39; to remove the registration from vCenter Server. Use &#39;false&#39; to keep the registration with the vCenter Server. The default is &#39;false&#39;. |  [optional] |



