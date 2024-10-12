# LinodeApi.LinodeBackups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **Boolean** | Whether Backups for this Linode are available for restoration.  Backups undergoing maintenance are not available for restoration.  | [optional] [readonly] 
**enabled** | **Boolean** | If this Linode has the Backup service enabled. To enable backups, see [POST /linode/instances/{linodeId}/backups/enable](/docs/api/linode-instances/#backups-enable).  | [optional] [readonly] 
**lastSuccessful** | **Date** | The last successful backup date. &#39;null&#39; if there was no previous backup. | [optional] [readonly] 
**schedule** | [**LinodeBackupsSchedule**](LinodeBackupsSchedule.md) |  | [optional] 


