

# CreateFileSystemWindowsConfiguration

The configuration object for the Microsoft Windows file system used in <code>CreateFileSystem</code> and <code>CreateFileSystemFromBackup</code> operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeDirectoryId** | [**String**](String.md) |  |  [optional] |
|**selfManagedActiveDirectoryConfiguration** | [**SelfManagedActiveDirectoryConfiguration**](SelfManagedActiveDirectoryConfiguration.md) |  |  [optional] |
|**deploymentType** | [**WindowsDeploymentType**](WindowsDeploymentType.md) |  |  [optional] |
|**preferredSubnetId** | [**String**](String.md) |  |  [optional] |
|**throughputCapacity** | [**Integer**](Integer.md) |  |  |
|**weeklyMaintenanceStartTime** | [**String**](String.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | [**String**](String.md) |  |  [optional] |
|**automaticBackupRetentionDays** | [**Integer**](Integer.md) |  |  [optional] |
|**copyTagsToBackups** | [**Boolean**](Boolean.md) |  |  [optional] |
|**aliases** | [**List**](List.md) |  |  [optional] |
|**auditLogConfiguration** | [**CreateFileSystemWindowsConfigurationAuditLogConfiguration**](CreateFileSystemWindowsConfigurationAuditLogConfiguration.md) |  |  [optional] |



