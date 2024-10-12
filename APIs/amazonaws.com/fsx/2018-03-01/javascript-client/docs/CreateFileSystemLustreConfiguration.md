# AmazonFsx.CreateFileSystemLustreConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weeklyMaintenanceStartTime** | **String** |  | [optional] 
**importPath** | **String** |  | [optional] 
**exportPath** | **String** |  | [optional] 
**importedFileChunkSize** | **Number** |  | [optional] 
**deploymentType** | [**LustreDeploymentType**](LustreDeploymentType.md) |  | [optional] 
**autoImportPolicy** | [**AutoImportPolicyType**](AutoImportPolicyType.md) |  | [optional] 
**perUnitStorageThroughput** | **Number** |  | [optional] 
**dailyAutomaticBackupStartTime** | **String** | A recurring daily time, in the format &lt;code&gt;HH:MM&lt;/code&gt;. &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. For example, &lt;code&gt;05:00&lt;/code&gt; specifies 5 AM daily.  | [optional] 
**automaticBackupRetentionDays** | **Number** |  | [optional] 
**copyTagsToBackups** | **Boolean** |  | [optional] 
**driveCacheType** | [**DriveCacheType**](DriveCacheType.md) |  | [optional] 
**dataCompressionType** | [**DataCompressionType**](DataCompressionType.md) |  | [optional] 
**logConfiguration** | [**CreateFileSystemLustreConfigurationLogConfiguration**](CreateFileSystemLustreConfigurationLogConfiguration.md) |  | [optional] 
**rootSquashConfiguration** | [**CreateFileSystemLustreConfigurationRootSquashConfiguration**](CreateFileSystemLustreConfigurationRootSquashConfiguration.md) |  | [optional] 


