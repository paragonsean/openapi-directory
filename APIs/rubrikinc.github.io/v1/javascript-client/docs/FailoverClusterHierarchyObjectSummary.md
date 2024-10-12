# RubrikRestApi.FailoverClusterHierarchyObjectSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | ID assigned to the failover cluster hierarchy object. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | The name of the Rubrik object. | 
**primaryClusterId** | **String** |  | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. | [optional] 
**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. | [optional] 
**descendentCount** | [**FailoverClusterHierarchyObjectDescendentCount**](FailoverClusterHierarchyObjectDescendentCount.md) |  | 
**failoverClusterAppConnectionStatus** | [**FailoverClusterAppConnectionStatus**](FailoverClusterAppConnectionStatus.md) |  | [optional] 
**failoverClusterAppName** | **String** | Failover cluster app name of this failover cluster hierarchy object. Only valid for failover cluster apps. | [optional] 
**failoverClusterAppSource** | [**FailoverClusterAppSource**](FailoverClusterAppSource.md) |  | [optional] 
**failoverClusterConnectionStatus** | [**FailoverClusterConnectionStatus**](FailoverClusterConnectionStatus.md) |  | [optional] 
**failoverClusterName** | **String** | The failover cluster name for the failover cluster hierarchy object. Only valid for failover clusters. | [optional] 
**failoverClusterType** | [**FailoverClusterType**](FailoverClusterType.md) |  | [optional] 
**filesets** | [**[FilesetSummary]**](FilesetSummary.md) | Fileset summary for the failover cluster hierarchy object. Only valid for failover cluster apps. | [optional] 
**isDeleted** | **Boolean** | A Boolean that indicates whether the failover cluster hierarchy object has been deleted. When this value is &#39;true,&#39; the hierarchy object has been deleted. | 
**nodes** | [**[FailoverClusterNode]**](FailoverClusterNode.md) | Node details for the failover cluster hierarchy object. Only valid for failover clusters. | [optional] 
**numFailoverClusterApps** | **Number** | The number of failover cluster apps in the failover cluster hierarchy object. Only valid for failover clusters. | [optional] 
**numNodes** | **Number** | The number of nodes in the failover cluster hierarchy object. Only valid for failover clusters. | [optional] 
**objectType** | [**FailoverClusterObjectType**](FailoverClusterObjectType.md) |  | 
**operatingSystemType** | [**FailoverClusterOsType**](FailoverClusterOsType.md) |  | [optional] 
**slaAssignment** | [**SlaAssignment**](SlaAssignment.md) |  | [optional] 


