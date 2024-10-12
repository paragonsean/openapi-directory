# RubrikRestApi.VirtualMachineDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudInstantiationSpec** | [**CloudInstantiationSpec**](CloudInstantiationSpec.md) |  | [optional] 
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**isArrayIntegrationEnabled** | **Boolean** | Boolean value that determines whether the available storage array integration is used with the specified virtual machine. Set to &#39;true&#39; to use storage array integration and set to &#39;false&#39; to not use storage array integration. Refer to the value of &#39;isArrayIntegrationPossible&#39; to determine whether storage array integration is available for a virtual machine. | 
**isVmPaused** | **Boolean** | Whether to pause or resume backups/archival for this VM. | [optional] 
**maxNestedVsphereSnapshots** | **Number** |  | 
**postBackupScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  | [optional] 
**postSnapScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  | [optional] 
**preBackupScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  | [optional] 
**snapshotConsistencyMandate** | **String** | Consistency level mandated for this VM or empty string for none. | 
**throttlingSettings** | [**VmwareAdaptiveThrottlingSettings**](VmwareAdaptiveThrottlingSettings.md) |  | [optional] 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | The ID of the Rubrik object. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | The name of the Rubrik object. | 
**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. | [optional] 
**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. | [optional] 
**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. | [optional] 
**slaAssignment** | **String** | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. | 
**agentStatus** | [**AgentStatus**](AgentStatus.md) |  | [optional] 
**clusterName** | **String** |  | [optional] 
**folderPath** | [**[VmPathPoint]**](VmPathPoint.md) | Brief info of all the objects in the folder path to this VM. | 
**guestCredentialAuthorizationStatus** | **String** | Status of authentication with a specific virtual machine using guest credentials. Possible values are: SUCCESSFUL, PENDING, or FAILED. | 
**guestOsName** | **String** | Long form name, including type and release designation, for the operating system that is installed on a virtual machine. | [optional] 
**hostId** | **String** |  | [optional] 
**hostName** | **String** |  | [optional] 
**infraPath** | [**[VmPathPoint]**](VmPathPoint.md) | Brief info of all the objects in the infrastructure path to this VM. | 
**ipAddress** | **String** |  | 
**isRelic** | **Boolean** |  | 
**isReplicationEnabled** | **Boolean** |  | 
**moid** | **String** |  | 
**parentAppInfo** | [**ParentAppInfo**](ParentAppInfo.md) |  | [optional] 
**powerStatus** | **String** | The power status of VM(ON,OFF,SLEEP etc.). | [optional] 
**protectionDate** | **Date** |  | [optional] 
**toolsInstalled** | **Boolean** |  | [optional] 
**vcenterId** | **String** |  | [optional] 
**vmwareToolsInstalled** | **Boolean** |  | 
**blackoutWindowStatus** | [**BlackoutWindowStatus**](BlackoutWindowStatus.md) |  | 
**blackoutWindows** | [**BlackoutWindows**](BlackoutWindows.md) |  | 
**cdpState** | [**CdpState**](CdpState.md) |  | 
**currentHost** | [**VmwareHostSummary**](VmwareHostSummary.md) |  | [optional] 
**effectiveSlaDomain** | [**SlaDomainSummary**](SlaDomainSummary.md) |  | 
**guestCredential** | [**BaseGuestCredentialDetail**](BaseGuestCredentialDetail.md) |  | [optional] 
**guestOsType** | **String** | Type of operating system used by the VMware virtual machine. | 
**isAgentRegistered** | **Boolean** | Boolean value that indicates whether the Rubrik Backup Service is installed and registered for the specified virtual machine. Set to &#39;true&#39; when the Rubrik Backup Service is installed and registered and in all other cases set to &#39;false&#39;. | [optional] 
**isArrayIntegrationPossible** | **Boolean** | Boolean value that indicates whether the performance enhancements of storage array integration are available for the specified virtual machine object. Storage array integration is available when all of the datastores that are assigned to the virtual machine reside on a qualified storage array. Set to &#39;true&#39; when storage array integration is available and set to &#39;false&#39; when storage array integration is not available. | 
**isCdpEnabled** | **Boolean** |  | 
**isInVmc** | **Boolean** | A Boolean that specifies whether the virtual machine is in a VMC environment. | 
**latestRecoveryPoint** | **Date** | Latest point in time that we can recover to if this is a CDP enabled VM. | [optional] 
**logicalSize** | **Number** | This returns the sum of all virtual disk sizes in the specified virtual machine. | [optional] 
**oldestRecoveryPoint** | **Date** | Oldest point in time that we can recover to if this is a CDP enabled VM. | [optional] 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**physicalStorage** | **Number** |  | 
**snapshotCount** | **Number** |  | [optional] 
**snapshots** | [**[VmSnapshotSummary]**](VmSnapshotSummary.md) |  | [optional] 
**vcenterName** | **String** | The name of vCenter that the virtual machine belongs to. | 
**virtualDiskIds** | **[String]** |  | [optional] 



## Enum: SnapshotConsistencyMandateEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `INCONSISTENT` (value: `"INCONSISTENT"`)

* `CRASH_CONSISTENT` (value: `"CRASH_CONSISTENT"`)

* `FILE_SYSTEM_CONSISTENT` (value: `"FILE_SYSTEM_CONSISTENT"`)

* `VSS_CONSISTENT` (value: `"VSS_CONSISTENT"`)

* `APP_CONSISTENT` (value: `"APP_CONSISTENT"`)





## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)





## Enum: GuestOsTypeEnum


* `Linux` (value: `"Linux"`)

* `Windows` (value: `"Windows"`)

* `Unknown` (value: `"Unknown"`)




