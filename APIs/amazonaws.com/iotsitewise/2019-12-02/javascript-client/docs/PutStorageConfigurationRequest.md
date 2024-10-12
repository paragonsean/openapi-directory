# AwsIoTSiteWise.PutStorageConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storageType** | **String** | &lt;p&gt;The storage tier that you specified for your data. The &lt;code&gt;storageType&lt;/code&gt; parameter can be one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SITEWISE_DEFAULT_STORAGE&lt;/code&gt; – IoT SiteWise saves your data into the hot tier. The hot tier is a service-managed database.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MULTI_LAYER_STORAGE&lt;/code&gt; – IoT SiteWise saves your data in both the cold tier and the hot tier. The cold tier is a customer-managed Amazon S3 bucket.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**multiLayerStorage** | [**PutStorageConfigurationRequestMultiLayerStorage**](PutStorageConfigurationRequestMultiLayerStorage.md) |  | [optional] 
**disassociatedDataStorage** | **String** | &lt;p&gt;Contains the storage configuration for time series (data streams) that aren&#39;t associated with asset properties. The &lt;code&gt;disassociatedDataStorage&lt;/code&gt; can be one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ENABLED&lt;/code&gt; – IoT SiteWise accepts time series that aren&#39;t associated with asset properties.&lt;/p&gt; &lt;important&gt; &lt;p&gt;After the &lt;code&gt;disassociatedDataStorage&lt;/code&gt; is enabled, you can&#39;t disable it.&lt;/p&gt; &lt;/important&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DISABLED&lt;/code&gt; – IoT SiteWise doesn&#39;t accept time series (data streams) that aren&#39;t associated with asset properties.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html\&quot;&gt;Data streams&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; | [optional] 
**retentionPeriod** | [**PutStorageConfigurationRequestRetentionPeriod**](PutStorageConfigurationRequestRetentionPeriod.md) |  | [optional] 



## Enum: StorageTypeEnum


* `SITEWISE_DEFAULT_STORAGE` (value: `"SITEWISE_DEFAULT_STORAGE"`)

* `MULTI_LAYER_STORAGE` (value: `"MULTI_LAYER_STORAGE"`)





## Enum: DisassociatedDataStorageEnum


* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)




