# AmazonFsx.CreateFileSystemFromBackupRequestWindowsConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeDirectoryId** | **String** |  | [optional] 
**selfManagedActiveDirectoryConfiguration** | [**SelfManagedActiveDirectoryConfiguration**](SelfManagedActiveDirectoryConfiguration.md) |  | [optional] 
**deploymentType** | [**WindowsDeploymentType**](WindowsDeploymentType.md) |  | [optional] 
**preferredSubnetId** | **String** |  | [optional] 
**throughputCapacity** | **Number** |  | 
**weeklyMaintenanceStartTime** | **String** |  | [optional] 
**dailyAutomaticBackupStartTime** | **String** |  | [optional] 
**automaticBackupRetentionDays** | **Number** |  | [optional] 
**copyTagsToBackups** | **Boolean** |  | [optional] 
**aliases** | **Array** |  | [optional] 
**auditLogConfiguration** | [**CreateFileSystemWindowsConfigurationAuditLogConfiguration**](CreateFileSystemWindowsConfigurationAuditLogConfiguration.md) |  | [optional] 


