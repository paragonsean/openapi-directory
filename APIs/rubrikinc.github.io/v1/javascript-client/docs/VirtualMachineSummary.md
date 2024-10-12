# RubrikRestApi.VirtualMachineSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
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
**cloudInstantiationSpec** | [**CloudInstantiationSpec**](CloudInstantiationSpec.md) |  | [optional] 
**clusterName** | **String** |  | [optional] 
**folderPath** | [**[VmPathPoint]**](VmPathPoint.md) | Brief info of all the objects in the folder path to this VM. | 
**guestCredentialAuthorizationStatus** | **String** | Status of authentication with a specific virtual machine using guest credentials. Possible values are: SUCCESSFUL, PENDING, or FAILED. | 
**guestOsName** | **String** |  | [optional] 
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
**snapshotConsistencyMandate** | **String** | Consistency level mandated for this VM or empty string for none. | 
**toolsInstalled** | **Boolean** |  | [optional] 
**vcenterId** | **String** |  | [optional] 
**vmwareToolsInstalled** | **Boolean** |  | 



## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)





## Enum: SnapshotConsistencyMandateEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `INCONSISTENT` (value: `"INCONSISTENT"`)

* `CRASH_CONSISTENT` (value: `"CRASH_CONSISTENT"`)

* `FILE_SYSTEM_CONSISTENT` (value: `"FILE_SYSTEM_CONSISTENT"`)

* `VSS_CONSISTENT` (value: `"VSS_CONSISTENT"`)

* `APP_CONSISTENT` (value: `"APP_CONSISTENT"`)




