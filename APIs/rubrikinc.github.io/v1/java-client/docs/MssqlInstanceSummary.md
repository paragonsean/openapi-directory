

# MssqlInstanceSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copyOnly** | **Boolean** | Boolean value that specifies whether or not to perform copy-only backups of the database. When true, database backups are copy-only backups. When false, database backups are full backups. |  [optional] |
|**logBackupFrequencyInSeconds** | **Integer** | Seconds between two log backups. A value of 0 disables log backup. |  [optional] |
|**logRetentionHours** | **Integer** | Number of hours to retain a log backup. When the value is set to -1 the Rubrik cluster retains the log backup until the database snapshots that precede the log backup have expired. |  [optional] |
|**clusterInstanceAddress** | **String** | The address of the instance in a Windows server failover cluster, populated only if it belongs to one. |  [optional] |
|**configuredSlaDomainId** | **String** | SLA Domain ID assigned to instance. |  [optional] |
|**configuredSlaDomainName** | **String** | SLA Domain name assigned to instance. |  [optional] |
|**configuredSlaDomainType** | **String** | Specifies whether the SLA Domain is used for protection or retention. |  [optional] |
|**id** | **String** |  |  |
|**internalTimestamp** | **Long** |  |  [optional] |
|**isRetentionLocked** | **Boolean** | Boolean value that identifies a Retention Lock SLA Domain. Value is true when the SLA Domain assigned to the instance is Retention Locked and false when it is not. |  [optional] |
|**name** | **String** |  |  [optional] |
|**primaryClusterId** | **String** |  |  |
|**protectionDate** | **LocalDate** |  |  [optional] |
|**rootProperties** | [**MssqlRootProperties**](MssqlRootProperties.md) |  |  |
|**unprotectableReasons** | **List&lt;String&gt;** | A list of reasons that all the SQL Server databases in a SQL Server instance cannot be protected by the Rubrik CDM. |  [optional] |
|**version** | **String** |  |  [optional] |



