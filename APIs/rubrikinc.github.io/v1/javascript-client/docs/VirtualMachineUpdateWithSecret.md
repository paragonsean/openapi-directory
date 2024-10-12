# RubrikRestApi.VirtualMachineUpdateWithSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudInstantiationSpec** | [**CloudInstantiationSpec**](CloudInstantiationSpec.md) |  | [optional] 
**configuredSlaDomainId** | **String** | Assign this VM to the given SLA domain. Existing snapshots of the object will be retained with the configuration of specified SLA Domain. | [optional] 
**isArrayIntegrationEnabled** | **Boolean** | User setting to dictate whether to use storage array snaphots for ingest. This setting only makes sense for VMs where array based ingest is possible. | [optional] 
**isVmPaused** | **Boolean** | Whether to pause or resume backups/archival for this VM. | [optional] 
**maxNestedVsphereSnapshots** | **Number** |  | [optional] 
**postBackupScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  | [optional] 
**postSnapScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  | [optional] 
**preBackupScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  | [optional] 
**snapshotConsistencyMandate** | **String** | Consistency level mandated for this VM or empty string for none. | [optional] 
**throttlingSettings** | [**VmwareAdaptiveThrottlingSettings**](VmwareAdaptiveThrottlingSettings.md) |  | [optional] 
**guestCredential** | [**BaseGuestCredential**](BaseGuestCredential.md) |  | [optional] 
**shouldRefreshCacheAfterUpdate** | **Boolean** | A boolean value that specifies whether an update also refreshes the in-memory cache. When &#39;false&#39; updates do not refresh the in-memory cache. When &#39;true&#39; updates refresh the in-memory cache. By default, this value is &#39;true&#39;. Setting this value to &#39;false&#39; reduces the time required for updates to complete. | [optional] 



## Enum: SnapshotConsistencyMandateEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `INCONSISTENT` (value: `"INCONSISTENT"`)

* `CRASH_CONSISTENT` (value: `"CRASH_CONSISTENT"`)

* `FILE_SYSTEM_CONSISTENT` (value: `"FILE_SYSTEM_CONSISTENT"`)

* `VSS_CONSISTENT` (value: `"VSS_CONSISTENT"`)

* `APP_CONSISTENT` (value: `"APP_CONSISTENT"`)




