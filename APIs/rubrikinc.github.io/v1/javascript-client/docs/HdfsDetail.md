# RubrikRestApi.HdfsDetail

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
**effectiveSlaDomainId** | **String** | The ID of the effective SLA Domain for a HDFS directory. | [optional] 
**effectiveSlaDomainName** | **String** | The name of the effective SLA Domain for this HDFS directory. | [optional] 
**effectiveSlaDomainPolarisManagedId** | **String** | An optional field that contains the Polaris managed ID of the effective SLA Domain. Only applicable to SLA Domains managed by Polaris. | [optional] 
**exceptions** | **[String]** |  | [optional] 
**excludes** | **[String]** |  | [optional] 
**hostId** | **String** |  | [optional] 
**hostName** | **String** |  | 
**includes** | **[String]** |  | 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | An optional Boolean value that specifies whether the effective SLA Domain of a HDFS directory is Retention Locked. When this value is &#39;true,&#39; the SLA Domain is retention locked. When this value is &#39;false,&#39; the SLA Domain is not Retention Locked. | [optional] 
**isRelic** | **Boolean** |  | 
**templateId** | **String** |  | 
**templateName** | **String** |  | 
**localStorage** | **Number** |  | [optional] 
**protectionDate** | **Date** |  | [optional] 
**snapshotCount** | **Number** |  | 
**snapshots** | [**[HdfsSnapshotSummary]**](HdfsSnapshotSummary.md) |  | [optional] 


