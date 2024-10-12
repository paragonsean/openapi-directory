# RubrikRestApi.OracleDbSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | ID assigned to the Oracle database. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | Service name of the Oracle database. | 
**primaryClusterId** | **String** |  | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainName** | **String** | The name of the SLA Domain that controls the protection of the Rubrik object. | 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional. This field contains the managed ID of of the Polaris-managed effective SLA Domain. | [optional] 
**effectiveSlaSourceObjectId** | **String** | The ID of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**effectiveSlaSourceObjectName** | **String** | The name of the parent of the Rubrik object from which the SLA Domain that controls the protection of Rubrik object is inherited. | [optional] 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | Indicates whether the effective SLA Domain is Retention Locked. When this value is &#39;true&#39;, the effective SLA domain is a Retention Lock SLA Domain. | [optional] 
**retentionSlaDomainId** | **String** | The ID of the SLA Domain whose retention policy is in use. | [optional] 
**slaAssignment** | **String** | The SLA assignment type. Direct SLA assignment means that a SLA Domain was configured directly on the Rubrik object by the user. Derived SLA assignment means that the Rubrik object inherits an SLA Domain from its parent Rubrik object. | 
**archiveLogDestinations** | **[String]** | An array that contains the archive log destinations for the specified Oracle database. | [optional] 
**currentBackupTaskInfo** | [**BackupTaskDiagnosticInfo**](BackupTaskDiagnosticInfo.md) |  | [optional] 
**dataGuardGroupId** | **String** | Rubrik ID of the Data Guard group to which this database belongs. | [optional] 
**dataGuardGroupMembers** | [**[DataGuardGroupMember]**](DataGuardGroupMember.md) | List of Data Guard group members. | [optional] 
**dataGuardGroupName** | **String** | Name of the Data Guard group to which this database belongs. | [optional] 
**dataGuardType** | [**DataGuardType**](DataGuardType.md) |  | [optional] 
**databaseRole** | **String** | Current role of the database. | [optional] 
**dbUniqueName** | **String** | Unique name for the Oracle database (DB_UNIQUE_NAME). | [optional] 
**hostLogRetentionHours** | **Number** | Specifies an interval in hours. The next log snapshot job deletes archived Oracle redo log files whose &#39;nextTime&#39; field specifies a time more than the specified number of hours ago. To immediately delete archived redo log files regardless of age, specify an interval of -1. To preserve all archived redo log files, specify an interval of -2. | 
**includeBackupTaskInfo** | **Boolean** | True/false value indicating if backup task information is included in the response. | [optional] 
**infraPath** | [**[ManagedHierarchyObjectAncestor]**](ManagedHierarchyObjectAncestor.md) | An array that contains information about the objects in the infrastructure path of a specified Oracle database. | 
**instances** | [**[OracleInstanceProperties]**](OracleInstanceProperties.md) | Details of the instances of the Oracle database. | [optional] 
**isArchiveLogModeEnabled** | **Boolean** | Boolean value that indicates whether the ARCHIVELOG mode is enabled on the Oracle database or not. | [optional] 
**isDbLocalToTheCluster** | **Boolean** | A Boolean value that specifies whether the Oracle database is local to the cluster. When this value is &#39;true&#39;, the Oracle database is local to the cluster. | 
**isPrimary** | **Boolean** | Indicates whether the current DATABASE_ROLE is PRIMARY which specifies the database is accepting read/write transactions as the primary database in a Data Guard configuration. | [optional] 
**isRelic** | **Boolean** | Boolean value that indicates whether a Oracle database object is in an archived state and has retained snapshots. Value is true when the object is archived with retained snapshots. | 
**lastSnapshotTime** | **Date** | The timestamp of the previous snapshot. | [optional] 
**logBackupFrequencyInMinutes** | **Number** | Specifies an interval in minutes. This interval is the period between successive log backups. | [optional] 
**numInstances** | **Number** | Count of the number of instances of the Oracle database. | [optional] 
**numMissedSnapshot** | **Number** | An integer that specifies the number of missed snapshots. | 
**numTablespaces** | **Number** | Count of the number of table spaces in Oracle database. | 
**racId** | **String** | Rubrik ID of the RAC on which this database is hosted. This field will be empty if the database is not hosted on a RAC environment. | [optional] 
**racName** | **String** | RAC name of the cluster database. | [optional] 
**sid** | **String** | System identifier (SID) of the Oracle database. | [optional] 
**standaloneHostId** | **String** | Rubrik ID of the standalone Oracle host on which this database is hosted. This field will be empty if the database is not hosted on a standalone system. | [optional] 
**standaloneHostName** | **String** | Hostname of the standalone Oracle database host. | [optional] 



## Enum: SlaAssignmentEnum


* `Derived` (value: `"Derived"`)

* `Direct` (value: `"Direct"`)

* `Unassigned` (value: `"Unassigned"`)




