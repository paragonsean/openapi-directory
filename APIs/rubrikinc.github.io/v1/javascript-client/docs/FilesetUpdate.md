# RubrikRestApi.FilesetUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | Assign Fileset to SLA domain. Existing snapshots of the object will be retained with the configuration of specified SLA Domain. | [optional] 
**forceFull** | **Boolean** | Whether to force a full on the whole fileset or certain partitions of the fileset. If this is set to true and no partitionIds are provided, then a full will be forced on the whole fileset. If set to true and partitionIds are provided, then we will force a full on only those partitions. | [optional] 
**forceFullPartitionIds** | **[Number]** | Assign partition ids to set the force full. In order for this to be valid input, forceFull must be set to true. | [optional] 
**snapMirrorLabelForFullBackup** | **String** | Rubrik CDM uses a prefix match to select the latest SnapMirror snapshot that matches this value during a full backup of a SnapMirror destination share. | [optional] 
**snapMirrorLabelForIncrementalBackup** | **String** | Rubrik CDM selects the latest SnapMirror snapshot that matches this value using a prefix match during an incremental backup of a SnapMirror destination share. | [optional] 


