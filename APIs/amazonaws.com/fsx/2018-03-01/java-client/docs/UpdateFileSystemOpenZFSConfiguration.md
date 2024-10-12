

# UpdateFileSystemOpenZFSConfiguration

The configuration updates for an Amazon FSx for OpenZFS file system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automaticBackupRetentionDays** | **Integer** | The number of days to retain automatic backups. Setting this property to &lt;code&gt;0&lt;/code&gt; disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is &lt;code&gt;30&lt;/code&gt;. |  [optional] |
|**copyTagsToBackups** | [**Boolean**](Boolean.md) |  |  [optional] |
|**copyTagsToVolumes** | [**Boolean**](Boolean.md) |  |  [optional] |
|**dailyAutomaticBackupStartTime** | **String** | A recurring daily time, in the format &lt;code&gt;HH:MM&lt;/code&gt;. &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. For example, &lt;code&gt;05:00&lt;/code&gt; specifies 5 AM daily.  |  [optional] |
|**throughputCapacity** | [**Integer**](Integer.md) |  |  [optional] |
|**weeklyMaintenanceStartTime** | **String** | &lt;p&gt;A recurring weekly time, in the format &lt;code&gt;D:HH:MM&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;D&lt;/code&gt; is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_week_date\&quot;&gt;the ISO-8601 spec as described on Wikipedia&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. &lt;/p&gt; &lt;p&gt;For example, &lt;code&gt;1:05:00&lt;/code&gt; specifies maintenance at 5 AM Monday.&lt;/p&gt; |  [optional] |
|**diskIopsConfiguration** | [**DiskIopsConfiguration**](DiskIopsConfiguration.md) |  |  [optional] |



