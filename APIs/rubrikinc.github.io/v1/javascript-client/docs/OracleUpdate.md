# RubrikRestApi.OracleUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostLogRetentionHours** | **Number** | Specifies an interval in hours. For Oracle archived redo log files whose nextTime is before (now - interval), the next log snapshot job will delete them from the host. Set to 0 for inheriting the value from its parent; -1 for immediate deletion; and -2 to skip log deletion. | [optional] 
**hostMount** | **String** | Path where the NFS share is mounted on the host. | [optional] 
**logBackupFrequencyInMinutes** | **Number** | Specifies an interval in minutes. This interval is the period between successive log backups. | [optional] 
**logRetentionHours** | **Number** | Specifies an interval in hours. Log backups are retained for the duration of the interval. | [optional] 
**numChannels** | **Number** | Number of channels used to backup the Oracle database. | [optional] 
**configuredSlaDomainIdDeprecated** | **String** | ID of the SLA domain protecting the specified Oracle object. Log backup jobs are no longer scheduled if the SLA domain indicates the Oracle object is unprotected. The specified SLA domain is not used to configure the protection or retention for this Oracle object. This is a DEPRECATED field, and will be removed in later releases. | [optional] 
**nodeOrder** | [**[OracleNodeOrder]**](OracleNodeOrder.md) | Specifies an order for the RAC nodes. Automated Oracle backups use the RAC nodes in the specified order. | [optional] 


