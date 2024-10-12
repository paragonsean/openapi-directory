

# LustreFileSystemConfiguration

The configuration for the Amazon FSx for Lustre file system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**weeklyMaintenanceStartTime** | [**String**](String.md) |  |  [optional] |
|**dataRepositoryConfiguration** | [**DataRepositoryConfiguration**](DataRepositoryConfiguration.md) |  |  [optional] |
|**deploymentType** | [**LustreDeploymentType**](LustreDeploymentType.md) |  |  [optional] |
|**perUnitStorageThroughput** | [**Integer**](Integer.md) |  |  [optional] |
|**mountName** | [**String**](String.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | **String** | A recurring daily time, in the format &lt;code&gt;HH:MM&lt;/code&gt;. &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. For example, &lt;code&gt;05:00&lt;/code&gt; specifies 5 AM daily.  |  [optional] |
|**automaticBackupRetentionDays** | **Integer** | The number of days to retain automatic backups. Setting this property to &lt;code&gt;0&lt;/code&gt; disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is &lt;code&gt;30&lt;/code&gt;. |  [optional] |
|**copyTagsToBackups** | [**Boolean**](Boolean.md) |  |  [optional] |
|**driveCacheType** | [**DriveCacheType**](DriveCacheType.md) |  |  [optional] |
|**dataCompressionType** | [**DataCompressionType**](DataCompressionType.md) |  |  [optional] |
|**logConfiguration** | [**LustreFileSystemConfigurationLogConfiguration**](LustreFileSystemConfigurationLogConfiguration.md) |  |  [optional] |
|**rootSquashConfiguration** | [**LustreFileSystemConfigurationRootSquashConfiguration**](LustreFileSystemConfigurationRootSquashConfiguration.md) |  |  [optional] |



