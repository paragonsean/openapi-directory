

# UpdateFileSystemWindowsConfiguration

Updates the configuration for an existing Amazon FSx for Windows File Server file system. Amazon FSx only overwrites existing properties with non-null values provided in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**weeklyMaintenanceStartTime** | [**String**](String.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | [**String**](String.md) |  |  [optional] |
|**automaticBackupRetentionDays** | [**Integer**](Integer.md) |  |  [optional] |
|**throughputCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**selfManagedActiveDirectoryConfiguration** | [**UpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfiguration**](UpdateFileSystemWindowsConfigurationSelfManagedActiveDirectoryConfiguration.md) |  |  [optional] |
|**auditLogConfiguration** | [**UpdateFileSystemWindowsConfigurationAuditLogConfiguration**](UpdateFileSystemWindowsConfigurationAuditLogConfiguration.md) |  |  [optional] |



