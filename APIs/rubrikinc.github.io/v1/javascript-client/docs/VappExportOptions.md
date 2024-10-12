# RubrikRestApi.VappExportOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allChildVmsWithDefaultNetworkConnections** | [**[VappVmRestoreSpec]**](VappVmRestoreSpec.md) | Array containing summary information for the vApp virtual machines in the specified vApp snapshot, including the default network mappings. | 
**availableStoragePolicies** | [**[VcdOrgVdcStorageProfile]**](VcdOrgVdcStorageProfile.md) | Storage policies that can be used as a target for virtual machines being exported. | 
**restorableNetworks** | [**[CreateVappNetworkParams]**](CreateVappNetworkParams.md) | Array of vApp networks in the vApp snapshot being exported that can be enabled at the export location. | 
**targetVappNetworks** | [**[VappNetworkSummary]**](VappNetworkSummary.md) | Array of vApp networks at the export location that can be connected to the vApp virtual machines in the exported vApp snapshot. | [optional] 


