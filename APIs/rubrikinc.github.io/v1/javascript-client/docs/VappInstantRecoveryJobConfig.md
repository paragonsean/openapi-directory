# RubrikRestApi.VappInstantRecoveryJobConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shouldPowerOnVmsAfterRecovery** | **Boolean** | Boolean value that indicates whether to power on the recovered virtual machines in a vApp after Instant Recovery. Use &#39;true&#39; to turn the power on for the recovered virtual machines or use &#39;false&#39; to leave the power off for the virtual machines. | [optional] [default to false]
**vmsToRestore** | [**[VappVmRestoreSpec]**](VappVmRestoreSpec.md) | An array containing the restore specification for an Instant Recovery of virtual machines in a vApp snapshot. | 


