

# CreateFileSystemLustreConfiguration

<p>The Lustre configuration for the file system being created.</p> <note> <p>The following parameters are not supported for file systems with a data repository association created with .</p> <ul> <li> <p> <code>AutoImportPolicy</code> </p> </li> <li> <p> <code>ExportPath</code> </p> </li> <li> <p> <code>ImportedChunkSize</code> </p> </li> <li> <p> <code>ImportPath</code> </p> </li> </ul> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**weeklyMaintenanceStartTime** | [**String**](String.md) |  |  [optional] |
|**importPath** | [**String**](String.md) |  |  [optional] |
|**exportPath** | [**String**](String.md) |  |  [optional] |
|**importedFileChunkSize** | [**Integer**](Integer.md) |  |  [optional] |
|**deploymentType** | [**LustreDeploymentType**](LustreDeploymentType.md) |  |  [optional] |
|**autoImportPolicy** | [**AutoImportPolicyType**](AutoImportPolicyType.md) |  |  [optional] |
|**perUnitStorageThroughput** | [**Integer**](Integer.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | **String** | A recurring daily time, in the format &lt;code&gt;HH:MM&lt;/code&gt;. &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. For example, &lt;code&gt;05:00&lt;/code&gt; specifies 5 AM daily.  |  [optional] |
|**automaticBackupRetentionDays** | [**Integer**](Integer.md) |  |  [optional] |
|**copyTagsToBackups** | [**Boolean**](Boolean.md) |  |  [optional] |
|**driveCacheType** | [**DriveCacheType**](DriveCacheType.md) |  |  [optional] |
|**dataCompressionType** | [**DataCompressionType**](DataCompressionType.md) |  |  [optional] |
|**logConfiguration** | [**CreateFileSystemLustreConfigurationLogConfiguration**](CreateFileSystemLustreConfigurationLogConfiguration.md) |  |  [optional] |
|**rootSquashConfiguration** | [**CreateFileSystemLustreConfigurationRootSquashConfiguration**](CreateFileSystemLustreConfigurationRootSquashConfiguration.md) |  |  [optional] |



