# RubrikRestApi.VappExportSnapshotJobConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exportMode** | [**VappExportMode**](VappExportMode.md) |  | 
**networksToRestore** | [**[CreateVappNetworkParams]**](CreateVappNetworkParams.md) | Array of vApp networks that are in the specified vApp snapshot and should be set up as part of the export operation. A vApp network that is not included in the array will not be set up in the exported vApp. | 
**newVappParams** | [**CreateNewVappParams**](CreateNewVappParams.md) |  | [optional] 
**shouldPowerOnVappAfterExport** | **Boolean** | Boolean value that indicates whether to power on the exported vApp. Use &#39;true&#39; to turn the power on for the exported vApp or use &#39;false&#39; to leave the power off for the exported vApp. | [optional] [default to false]
**targetVappId** | **String** | ID assigned to the target vApp object, when the export is into an existing vApp. When the export is not into a target vApp, remove the &#39;targetVappId&#39; member. | [optional] 
**vmsToExport** | [**[VappVmRestoreSpec]**](VappVmRestoreSpec.md) | An array containing summary information for the virtual machines included in the vApp export. | 


