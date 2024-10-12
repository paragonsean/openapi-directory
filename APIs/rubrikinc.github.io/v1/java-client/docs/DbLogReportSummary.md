

# DbLogReportSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseType** | **DatabaseType** |  |  |
|**effectiveSlaDomainId** | **String** | ID of the SLA Domain controlling the database protection. |  |
|**effectiveSlaDomainName** | **String** | Name of the SLA Domain controlling the database protection. |  |
|**id** | **String** |  |  |
|**lastSnapshotTime** | **OffsetDateTime** | Time, in UTC, of the last database backup. |  [optional] |
|**latestRecoveryTime** | **OffsetDateTime** | Latest point in time, in UTC, to which the database can be restored. |  [optional] |
|**location** | **String** | Location of the customer database. For a standalone SQL database, this includes the host and instance name. |  |
|**logBackupDelay** | **Long** | Amount of time, in seconds, that has elapsed since the next expected log backup. |  [optional] |
|**logBackupFrequency** | **Integer** | Frequency, in seconds, of the database log backup. |  [optional] |
|**name** | **String** | Name of the database. |  |
|**primaryClusterId** | **String** | ID of the primary Rubrik cluster on which the database is located. |  |



