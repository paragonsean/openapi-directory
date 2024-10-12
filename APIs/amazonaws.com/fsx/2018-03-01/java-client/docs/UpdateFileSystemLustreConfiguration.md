

# UpdateFileSystemLustreConfiguration

The configuration object for Amazon FSx for Lustre file systems used in the <code>UpdateFileSystem</code> operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**weeklyMaintenanceStartTime** | [**String**](String.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | **String** | A recurring daily time, in the format &lt;code&gt;HH:MM&lt;/code&gt;. &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. For example, &lt;code&gt;05:00&lt;/code&gt; specifies 5 AM daily.  |  [optional] |
|**automaticBackupRetentionDays** | [**Integer**](Integer.md) |  |  [optional] |
|**autoImportPolicy** | [**AutoImportPolicyType**](AutoImportPolicyType.md) |  |  [optional] |
|**dataCompressionType** | [**DataCompressionType**](DataCompressionType.md) |  |  [optional] |
|**logConfiguration** | [**UpdateFileSystemLustreConfigurationLogConfiguration**](UpdateFileSystemLustreConfigurationLogConfiguration.md) |  |  [optional] |
|**rootSquashConfiguration** | [**UpdateFileSystemLustreConfigurationRootSquashConfiguration**](UpdateFileSystemLustreConfigurationRootSquashConfiguration.md) |  |  [optional] |



