# RubrikRestApi.VmwareHostDetail

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
**computeClusterId** | **String** |  | [optional] 
**datacenterId** | **String** |  | [optional] 
**datastores** | [**[DataStoreSummary]**](DataStoreSummary.md) |  | [optional] 
**esxiVersion** | **String** | API Version of the ESXi Host. | [optional] 
**ioFilterStatus** | [**HostFilterStatus**](HostFilterStatus.md) |  | 
**ioFilterUiStatus** | [**HostUiFilterStatus**](HostUiFilterStatus.md) |  | [optional] 
**isInVmc** | **Boolean** |  | [optional] 
**datacenter** | [**DataCenterSummary**](DataCenterSummary.md) |  | [optional] 
**moid** | **String** |  | [optional] 
**virtualMachines** | [**[VirtualMachineSummary]**](VirtualMachineSummary.md) |  | [optional] 


