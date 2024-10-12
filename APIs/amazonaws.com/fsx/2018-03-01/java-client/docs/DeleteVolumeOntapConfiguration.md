

# DeleteVolumeOntapConfiguration

Use to specify skipping a final backup, adding tags to a final backup, or bypassing the retention period of an FSx for ONTAP SnapLock Enterprise volume when deleting an FSx for ONTAP volume. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**skipFinalBackup** | [**Boolean**](Boolean.md) |  |  [optional] |
|**finalBackupTags** | [**List&lt;Tag&gt;**](Tag.md) | A list of &lt;code&gt;Tag&lt;/code&gt; values, with a maximum of 50 elements. |  [optional] |
|**bypassSnaplockEnterpriseRetention** | [**Boolean**](Boolean.md) |  |  [optional] |



