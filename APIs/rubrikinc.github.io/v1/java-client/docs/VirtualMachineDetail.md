

# VirtualMachineDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudInstantiationSpec** | [**CloudInstantiationSpec**](CloudInstantiationSpec.md) |  |  [optional] |
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**isArrayIntegrationEnabled** | **Boolean** | Boolean value that determines whether the available storage array integration is used with the specified virtual machine. Set to &#39;true&#39; to use storage array integration and set to &#39;false&#39; to not use storage array integration. Refer to the value of &#39;isArrayIntegrationPossible&#39; to determine whether storage array integration is available for a virtual machine. |  |
|**isVmPaused** | **Boolean** | Whether to pause or resume backups/archival for this VM. |  [optional] |
|**maxNestedVsphereSnapshots** | **Integer** |  |  |
|**postBackupScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  |  [optional] |
|**postSnapScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  |  [optional] |
|**preBackupScript** | [**VirtualMachineScriptDetail**](VirtualMachineScriptDetail.md) |  |  [optional] |
|**snapshotConsistencyMandate** | [**SnapshotConsistencyMandateEnum**](#SnapshotConsistencyMandateEnum) | Consistency level mandated for this VM or empty string for none. |  |
|**throttlingSettings** | [**VmwareAdaptiveThrottlingSettings**](VmwareAdaptiveThrottlingSettings.md) |  |  [optional] |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | The ID of the Rubrik object. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the Rubrik object. |  |
|**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. |  [optional] |
|**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. |  [optional] |
|**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. |  [optional] |
|**slaAssignment** | [**SlaAssignmentEnum**](#SlaAssignmentEnum) | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. |  |
|**agentStatus** | [**AgentStatus**](AgentStatus.md) |  |  [optional] |
|**clusterName** | **String** |  |  [optional] |
|**folderPath** | [**List&lt;VmPathPoint&gt;**](VmPathPoint.md) | Brief info of all the objects in the folder path to this VM. |  |
|**guestCredentialAuthorizationStatus** | **String** | Status of authentication with a specific virtual machine using guest credentials. Possible values are: SUCCESSFUL, PENDING, or FAILED. |  |
|**guestOsName** | **String** | Long form name, including type and release designation, for the operating system that is installed on a virtual machine. |  [optional] |
|**hostId** | **String** |  |  [optional] |
|**hostName** | **String** |  |  [optional] |
|**infraPath** | [**List&lt;VmPathPoint&gt;**](VmPathPoint.md) | Brief info of all the objects in the infrastructure path to this VM. |  |
|**ipAddress** | **String** |  |  |
|**isRelic** | **Boolean** |  |  |
|**isReplicationEnabled** | **Boolean** |  |  |
|**moid** | **String** |  |  |
|**parentAppInfo** | [**ParentAppInfo**](ParentAppInfo.md) |  |  [optional] |
|**powerStatus** | **String** | The power status of VM(ON,OFF,SLEEP etc.). |  [optional] |
|**protectionDate** | **OffsetDateTime** |  |  [optional] |
|**toolsInstalled** | **Boolean** |  |  [optional] |
|**vcenterId** | **String** |  |  [optional] |
|**vmwareToolsInstalled** | **Boolean** |  |  |
|**blackoutWindowStatus** | [**BlackoutWindowStatus**](BlackoutWindowStatus.md) |  |  |
|**blackoutWindows** | [**BlackoutWindows**](BlackoutWindows.md) |  |  |
|**cdpState** | **CdpState** |  |  |
|**currentHost** | [**VmwareHostSummary**](VmwareHostSummary.md) |  |  [optional] |
|**effectiveSlaDomain** | [**SlaDomainSummary**](SlaDomainSummary.md) |  |  |
|**guestCredential** | [**BaseGuestCredentialDetail**](BaseGuestCredentialDetail.md) |  |  [optional] |
|**guestOsType** | [**GuestOsTypeEnum**](#GuestOsTypeEnum) | Type of operating system used by the VMware virtual machine. |  |
|**isAgentRegistered** | **Boolean** | Boolean value that indicates whether the Rubrik Backup Service is installed and registered for the specified virtual machine. Set to &#39;true&#39; when the Rubrik Backup Service is installed and registered and in all other cases set to &#39;false&#39;. |  [optional] |
|**isArrayIntegrationPossible** | **Boolean** | Boolean value that indicates whether the performance enhancements of storage array integration are available for the specified virtual machine object. Storage array integration is available when all of the datastores that are assigned to the virtual machine reside on a qualified storage array. Set to &#39;true&#39; when storage array integration is available and set to &#39;false&#39; when storage array integration is not available. |  |
|**isCdpEnabled** | **Boolean** |  |  |
|**isInVmc** | **Boolean** | A Boolean that specifies whether the virtual machine is in a VMC environment. |  |
|**latestRecoveryPoint** | **OffsetDateTime** | Latest point in time that we can recover to if this is a CDP enabled VM. |  [optional] |
|**logicalSize** | **Long** | This returns the sum of all virtual disk sizes in the specified virtual machine. |  [optional] |
|**oldestRecoveryPoint** | **OffsetDateTime** | Oldest point in time that we can recover to if this is a CDP enabled VM. |  [optional] |
|**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  |  [optional] |
|**physicalStorage** | **Long** |  |  |
|**snapshotCount** | **Integer** |  |  [optional] |
|**snapshots** | [**List&lt;VmSnapshotSummary&gt;**](VmSnapshotSummary.md) |  |  [optional] |
|**vcenterName** | **String** | The name of vCenter that the virtual machine belongs to. |  |
|**virtualDiskIds** | **List&lt;String&gt;** |  |  [optional] |



## Enum: SnapshotConsistencyMandateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| INCONSISTENT | &quot;INCONSISTENT&quot; |
| CRASH_CONSISTENT | &quot;CRASH_CONSISTENT&quot; |
| FILE_SYSTEM_CONSISTENT | &quot;FILE_SYSTEM_CONSISTENT&quot; |
| VSS_CONSISTENT | &quot;VSS_CONSISTENT&quot; |
| APP_CONSISTENT | &quot;APP_CONSISTENT&quot; |



## Enum: SlaAssignmentEnum

| Name | Value |
|---- | -----|
| DERIVED | &quot;Derived&quot; |
| DIRECT | &quot;Direct&quot; |
| UNASSIGNED | &quot;Unassigned&quot; |



## Enum: GuestOsTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |
| WINDOWS | &quot;Windows&quot; |
| UNKNOWN | &quot;Unknown&quot; |



