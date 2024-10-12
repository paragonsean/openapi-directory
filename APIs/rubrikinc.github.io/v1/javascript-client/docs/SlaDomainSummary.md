# RubrikRestApi.SlaDomainSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numNutanixVms** | **Number** | The number of Nutanix virtual machines protected under this SLA domain. | [optional] 
**numEc2Instances** | **Number** | The number of EC2 instances protected under this SLA Domain. | [optional] 
**numHypervVms** | **Number** | The number of Hyper-V virtual machines protected under this SLA domain. | [optional] 
**numManagedVolumes** | **Number** | The number of Managed volumes protected under this SLA Domain. | [optional] 
**numDbs** | **Number** | The number of actively protected databases under this SLA domain. | [optional] 
**numVcdVapps** | **Number** | The number of vApps protected under this SLA Domain. | [optional] 
**numFilesets** | **Number** | The number of filesets protected under this SLA Domain. | [optional] 
**numLinuxHosts** | **Number** | The number of Linux servers with filesets protected under this SLA Domain. | [optional] 
**numOracleDbs** | **Number** | The number of actively protected oracle databases under this SLA Domain. | [optional] 
**numProtectedObjects** | **Number** | The total number of protected ojects under this SLA Domain. | [optional] 
**numShares** | **Number** | The number of shares protected under this SLA Domain. | [optional] 
**numStorageArrayVolumeGroups** | **Number** | The number of storage array volume groups protected under this SLA Domain. | [optional] 
**numVms** | **Number** |  | [optional] 
**numWindowsHosts** | **Number** | The number of Windows servers with filesets protected under this SLA Domain. | [optional] 
**numWindowsVolumeGroups** | **Number** | The number of Windows volume groups protected under this SLA Domain. | [optional] 
**allowedBackupWindows** | [**[BackupWindow]**](BackupWindow.md) |  | 
**archivalSpecs** | [**[ArchivalSpec]**](ArchivalSpec.md) | Specification for archival locations on this SLA. | [optional] 
**firstFullAllowedBackupWindows** | [**[BackupWindow]**](BackupWindow.md) |  | 
**frequencies** | [**[SlaFrequency]**](SlaFrequency.md) |  | 
**id** | **String** |  | 
**isDefault** | **Boolean** |  | 
**isPaused** | **Boolean** | A Boolean value that specifies whether protection for all the snappables that are protected by the specified SLA Domain is paused. When the value is &#39;true&#39; protection is paused. | [optional] 
**isRetentionLocked** | **Boolean** | Boolean value that identifies a Retention Lock SLA Domain. Value is true when an SLA Domain is Retention Locked and false when it is not. | [optional] 
**localRetentionLimit** | **Number** | Retention limit for snapshots on the local Rubrik system. If none, they will remain as long as SLA requires. | [optional] 
**maxLocalRetentionLimit** | **Number** | Maximum limit for snapshots to be retained on the local Rubrik system. For local sla, it would be max of frequencies but for remote sla, it would be the retentionLimit set on the replication target location. (Local location is the replication target location for remote sla). | 
**name** | **String** |  | 
**primaryClusterId** | **String** |  | 
**replicationSpecs** | [**[ReplicationSpec]**](ReplicationSpec.md) | Specification for replication locations on this SLA. | [optional] 
**uiColor** | **String** |  | [optional] 


