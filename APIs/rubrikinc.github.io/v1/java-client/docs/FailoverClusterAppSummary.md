

# FailoverClusterAppSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | ID of the SLA Domain that is assigned to the specified failover cluster app. Existing snapshots of the object will be retained with the configuration of specified SLA Domain. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | ID assigned to the failover cluster app. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | Name of the failover cluster app. |  |
|**primaryClusterId** | **String** |  |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. |  |
|**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. |  [optional] |
|**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. |  [optional] |
|**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. |  [optional] |
|**failoverClusterAppSource** | [**FailoverClusterAppSource**](FailoverClusterAppSource.md) |  |  |
|**failoverClusterId** | **String** | Cluster ID of the failover cluster app. |  |
|**failoverClusterType** | **FailoverClusterType** |  |  |
|**connectionStatus** | **FailoverClusterAppConnectionStatus** |  |  |
|**failoverClusterName** | **String** | The failover cluster name of the failover cluster app. The failover cluster is a group of hosts that provides high availability for running failover clustered applications. |  |
|**operatingSystemType** | **FailoverClusterOsType** |  |  [optional] |
|**slaAssignment** | **SlaAssignment** |  |  [optional] |



