# RecoveryServicesBackupClient.AzureVmWorkloadProtectableItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isAutoProtectable** | **Boolean** | Indicates if protectable item is auto-protectable | [optional] 
**isAutoProtected** | **Boolean** | Indicates if protectable item is auto-protected | [optional] 
**parentName** | **String** | Name for instance or AG | [optional] 
**parentUniqueName** | **String** | Parent Unique Name is added to provide the service formatted URI Name of the Parent  Only Applicable for data bases where the parent would be either Instance or a SQL AG. | [optional] 
**prebackupvalidation** | [**PreBackupValidation**](PreBackupValidation.md) |  | [optional] 
**serverName** | **String** | Host/Cluster Name for instance or AG | [optional] 
**subinquireditemcount** | **Number** | For instance or AG, indicates number of DB&#39;s present | [optional] 
**subprotectableitemcount** | **Number** | For instance or AG, indicates number of DB&#39;s to be protected | [optional] 


