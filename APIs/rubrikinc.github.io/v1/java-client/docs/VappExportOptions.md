

# VappExportOptions


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allChildVmsWithDefaultNetworkConnections** | [**List&lt;VappVmRestoreSpec&gt;**](VappVmRestoreSpec.md) | Array containing summary information for the vApp virtual machines in the specified vApp snapshot, including the default network mappings. |  |
|**availableStoragePolicies** | [**List&lt;VcdOrgVdcStorageProfile&gt;**](VcdOrgVdcStorageProfile.md) | Storage policies that can be used as a target for virtual machines being exported. |  |
|**restorableNetworks** | [**List&lt;CreateVappNetworkParams&gt;**](CreateVappNetworkParams.md) | Array of vApp networks in the vApp snapshot being exported that can be enabled at the export location. |  |
|**targetVappNetworks** | [**List&lt;VappNetworkSummary&gt;**](VappNetworkSummary.md) | Array of vApp networks at the export location that can be connected to the vApp virtual machines in the exported vApp snapshot. |  [optional] |



