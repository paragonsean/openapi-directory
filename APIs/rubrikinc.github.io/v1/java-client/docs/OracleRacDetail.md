

# OracleRacDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | ID assigned to the Oracle RAC. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | Cluster name assigned to the Oracle RAC. |  |
|**primaryClusterId** | **String** |  |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**nodeOrder** | [**List&lt;OracleNodeOrder&gt;**](OracleNodeOrder.md) | Specifies an order for the RAC nodes. Automated Oracle backups use the RAC nodes in the specified order. |  |
|**nodes** | [**List&lt;OracleNodeProperties&gt;**](OracleNodeProperties.md) | Details of the nodes of this Oracle RAC. |  |
|**numDbs** | **Integer** | Count of the number of databases on the Oracle RAC. |  |
|**numNodes** | **Integer** | Count of the number of nodes on the Oracle RAC. |  |
|**status** | **String** | Connectivity status of the Oracle RAC. |  |
|**hostLogRetentionHours** | **Integer** | Specifies an interval in hours. The next log snapshot job deletes archived Oracle redo log files whose &#39;nextTime&#39; field specifies a time more than the specified number of hours ago. To immediately delete archived redo log files regardless of age, specify an interval of -1. To preserve all archived redo log files, specify an interval of -2. |  |
|**hostMount** | **String** | Path where the NFS share is mounted on the host. |  |
|**logBackupFrequencyInMinutes** | **Integer** | Specifies an interval in minutes. This interval is the period between successive log backups. |  |
|**logRetentionHours** | **Integer** | Specifies an interval in hours. Log backups are retained for the duration of the interval. |  |
|**numChannels** | **Integer** | Number of channels used to backup the Oracle database. |  |
|**scan** | **String** | Single Client Access Name (SCAN) of the Oracle RAC cluster. |  |



