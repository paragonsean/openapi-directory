# RubrikRestApi.FilesetDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**forceFull** | **Boolean** | Whether to force a full on the whole fileset or certain partitions of the fileset. If this is set to true and no partitionIds are provided, then a full will be forced on the whole fileset. If set to true and partitionIds are provided, then we will force a full on only those partitions. | [optional] 
**forceFullPartitionIds** | **[Number]** | Assign partition ids to set the force full. In order for this to be valid input, forceFull must be set to true. | [optional] 
**snapMirrorLabelForFullBackup** | **String** | Rubrik CDM uses a prefix match to select the latest SnapMirror snapshot that matches this value during a full backup of a SnapMirror destination share. | [optional] 
**snapMirrorLabelForIncrementalBackup** | **String** | Rubrik CDM selects the latest SnapMirror snapshot that matches this value using a prefix match during an incremental backup of a SnapMirror destination share. | [optional] 
**allowBackupHiddenFoldersInNetworkMounts** | **Boolean** | Include or exclude hidden folders inside locally-mounted remote file systems from backups. | [optional] 
**allowBackupNetworkMounts** | **Boolean** | Include or exclude locally-mounted remote file systems from backups. | [optional] 
**useWindowsVss** | **Boolean** | Use VSS during Windows backups. | [optional] 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | The ID of the Rubrik object. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | The name of the Rubrik object. | 
**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**arraySpec** | [**FilesetArraySpec**](FilesetArraySpec.md) |  | [optional] 
**effectiveSlaDomainId** | **String** | The ID of the effective SLA Domain for this fileset. | [optional] 
**effectiveSlaDomainName** | **String** | The name of the effective SLA Domain for this fileset. | [optional] 
**effectiveSlaDomainPolarisManagedId** | **String** | Optional field containing Polaris managed ID of the effective SLA domain if it is Polaris managed. | [optional] 
**enableHardlinkSupport** | **Boolean** | A Boolean value that determines whether to recognize and dedupe hardlinks in a fileset. When &#39;true,&#39; performs a hardlink deduplication. When &#39;false,&#39; performs a normal backup that treats hardlinks as normal files. If not specified, this defaults to false. | [optional] 
**enableSymlinkResolution** | **Boolean** | A Boolean value that determines whether to resolve symlink in a fileset. When &#39;true,&#39; performs a symlink resolution. When &#39;false,&#39; performs no symlink resolution. If not specified, this defaults to false. | [optional] 
**exceptions** | **[String]** |  | [optional] 
**excludes** | **[String]** |  | [optional] 
**failoverClusterAppId** | **String** | ID of the failover cluster app. | [optional] 
**failoverClusterAppName** | **String** | The name of the failover cluster app. | [optional] 
**hostId** | **String** |  | [optional] 
**hostName** | **String** |  | 
**includes** | **[String]** |  | 
**isEffectiveSlaDomainRetentionLocked** | **Boolean** | An optional Boolean value that specifies whether the effective SLA Domain of a fileset is Retention Locked. When this value is &#39;true,&#39; the SLA Domain is retention locked. When this value is &#39;false,&#39; the SLA Domain is not Retention Locked. | [optional] 
**isPassthrough** | **Boolean** | A Boolean value that determines whether to take a direct archive backup. When &#39;true,&#39; performs a direct archive backup. When &#39;false,&#39; performs a normal backup. If not specified, this defaults to false. | [optional] 
**isRelic** | **Boolean** |  | 
**operatingSystemType** | **String** |  | [optional] 
**pendingSlaDomain** | [**ManagedObjectPendingSlaInfo**](ManagedObjectPendingSlaInfo.md) |  | [optional] 
**shareId** | **String** |  | [optional] 
**templateId** | **String** |  | 
**templateName** | **String** |  | 
**archiveStorage** | **Number** |  | [optional] 
**archivedSnapshotCount** | **Number** |  | [optional] 
**backupScriptErrorHandling** | **String** | Action taken if script fails. Options are \&quot;abort\&quot;, \&quot;continue\&quot;. | [optional] 
**backupScriptTimeout** | **Number** | Number of seconds after which the script is killed if it has not completed execution. | [optional] 
**localStorage** | **Number** |  | [optional] 
**postBackupScript** | **String** | Script to run after backup of this Fileset ends. | [optional] 
**preBackupScript** | **String** | Script to run before backup of this Fileset starts. | [optional] 
**protectionDate** | **Date** |  | [optional] 
**snapshotCount** | **Number** |  | 
**snapshots** | [**[FilesetSnapshotSummary]**](FilesetSnapshotSummary.md) |  | [optional] 


