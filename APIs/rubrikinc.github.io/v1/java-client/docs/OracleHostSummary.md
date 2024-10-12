

# OracleHostSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | ID assigned to the standalone Oracle host. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | Hostname of the standalone Oracle host. |  |
|**primaryClusterId** | **String** |  |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**infraPath** | [**List&lt;ManagedHierarchyObjectAncestor&gt;**](ManagedHierarchyObjectAncestor.md) | An array that contains information about the objects in the infrastructure path of a specified Oracle database. |  |
|**numDbs** | **Integer** | Count of the number of databases on the Oracle RAC. |  |
|**status** | **String** | Connectivity status of the Oracle RAC. |  |



