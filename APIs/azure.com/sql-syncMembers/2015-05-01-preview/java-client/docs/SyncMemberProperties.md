

# SyncMemberProperties

Properties of a sync member.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseName** | **String** | Database name of the member database in the sync member. |  [optional] |
|**databaseType** | [**DatabaseTypeEnum**](#DatabaseTypeEnum) | Database type of the sync member. |  [optional] |
|**password** | **String** | Password of the member database in the sync member. |  [optional] |
|**serverName** | **String** | Server name of the member database in the sync member |  [optional] |
|**sqlServerDatabaseId** | **UUID** | SQL Server database id of the sync member. |  [optional] |
|**syncAgentId** | **String** | ARM resource id of the sync agent in the sync member. |  [optional] |
|**syncDirection** | [**SyncDirectionEnum**](#SyncDirectionEnum) | Sync direction of the sync member. |  [optional] |
|**syncState** | [**SyncStateEnum**](#SyncStateEnum) | Sync state of the sync member. |  [optional] [readonly] |
|**userName** | **String** | User name of the member database in the sync member. |  [optional] |



## Enum: DatabaseTypeEnum

| Name | Value |
|---- | -----|
| AZURE_SQL_DATABASE | &quot;AzureSqlDatabase&quot; |
| SQL_SERVER_DATABASE | &quot;SqlServerDatabase&quot; |



## Enum: SyncDirectionEnum

| Name | Value |
|---- | -----|
| BIDIRECTIONAL | &quot;Bidirectional&quot; |
| ONE_WAY_MEMBER_TO_HUB | &quot;OneWayMemberToHub&quot; |
| ONE_WAY_HUB_TO_MEMBER | &quot;OneWayHubToMember&quot; |



## Enum: SyncStateEnum

| Name | Value |
|---- | -----|
| SYNC_IN_PROGRESS | &quot;SyncInProgress&quot; |
| SYNC_SUCCEEDED | &quot;SyncSucceeded&quot; |
| SYNC_FAILED | &quot;SyncFailed&quot; |
| DISABLED_TOMBSTONE_CLEANUP | &quot;DisabledTombstoneCleanup&quot; |
| DISABLED_BACKUP_RESTORE | &quot;DisabledBackupRestore&quot; |
| SYNC_SUCCEEDED_WITH_WARNINGS | &quot;SyncSucceededWithWarnings&quot; |
| SYNC_CANCELLING | &quot;SyncCancelling&quot; |
| SYNC_CANCELLED | &quot;SyncCancelled&quot; |
| UN_PROVISIONED | &quot;UnProvisioned&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| PROVISIONED | &quot;Provisioned&quot; |
| PROVISION_FAILED | &quot;ProvisionFailed&quot; |
| DE_PROVISIONING | &quot;DeProvisioning&quot; |
| DE_PROVISIONED | &quot;DeProvisioned&quot; |
| DE_PROVISION_FAILED | &quot;DeProvisionFailed&quot; |
| REPROVISIONING | &quot;Reprovisioning&quot; |
| REPROVISION_FAILED | &quot;ReprovisionFailed&quot; |
| UN_REPROVISIONED | &quot;UnReprovisioned&quot; |



