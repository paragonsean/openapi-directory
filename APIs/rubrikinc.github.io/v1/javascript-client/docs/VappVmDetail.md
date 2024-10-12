# RubrikRestApi.VappVmDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the specified vApp virtual machine within vCloud. | 
**networkConnections** | [**[VappVmNetworkConnection]**](VappVmNetworkConnection.md) |  | 
**storagePolicyId** | **String** | Storage policy where this vApp virtual machine should be restored to. If omitted, the virtual machines will be exported to the default storage policy of the target Organization VDC. | 
**vcdMoid** | **String** | vCloud managed object ID (moid) of the specified vApp virtual machine. | 
**vcenterVm** | [**VirtualMachineDetail**](VirtualMachineDetail.md) |  | [optional] 


