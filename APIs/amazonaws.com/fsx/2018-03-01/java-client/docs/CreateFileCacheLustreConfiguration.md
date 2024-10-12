

# CreateFileCacheLustreConfiguration

The Amazon File Cache configuration for the cache that you are creating.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**perUnitStorageThroughput** | [**Integer**](Integer.md) |  |  |
|**deploymentType** | [**FileCacheLustreDeploymentType**](FileCacheLustreDeploymentType.md) |  |  |
|**weeklyMaintenanceStartTime** | **String** | &lt;p&gt;A recurring weekly time, in the format &lt;code&gt;D:HH:MM&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;D&lt;/code&gt; is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_week_date\&quot;&gt;the ISO-8601 spec as described on Wikipedia&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. &lt;/p&gt; &lt;p&gt;For example, &lt;code&gt;1:05:00&lt;/code&gt; specifies maintenance at 5 AM Monday.&lt;/p&gt; |  [optional] |
|**metadataConfiguration** | [**CreateFileCacheLustreConfigurationMetadataConfiguration**](CreateFileCacheLustreConfigurationMetadataConfiguration.md) |  |  |



