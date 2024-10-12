

# FileSystemWindowsConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeDirectoryId** | [**String**](String.md) |  |  [optional] |
|**selfManagedActiveDirectoryConfiguration** | [**SelfManagedActiveDirectoryAttributes**](SelfManagedActiveDirectoryAttributes.md) |  |  [optional] |
|**deploymentType** | [**WindowsDeploymentType**](WindowsDeploymentType.md) |  |  [optional] |
|**remoteAdministrationEndpoint** | [**String**](String.md) |  |  [optional] |
|**preferredSubnetId** | [**String**](String.md) |  |  [optional] |
|**preferredFileServerIp** | [**String**](String.md) |  |  [optional] |
|**throughputCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**maintenanceOperationsInProgress** | [**List**](List.md) |  |  [optional] |
|**weeklyMaintenanceStartTime** | [**String**](String.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | [**String**](String.md) |  |  [optional] |
|**automaticBackupRetentionDays** | [**Integer**](Integer.md) |  |  [optional] |
|**copyTagsToBackups** | [**Boolean**](Boolean.md) |  |  [optional] |
|**aliases** | [**List&lt;Alias&gt;**](Alias.md) | An array of one or more DNS aliases that are currently associated with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html\&quot;&gt;DNS aliases&lt;/a&gt;. |  [optional] |
|**auditLogConfiguration** | [**WindowsFileSystemConfigurationAuditLogConfiguration**](WindowsFileSystemConfigurationAuditLogConfiguration.md) |  |  [optional] |



