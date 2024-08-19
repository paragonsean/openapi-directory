# AmazonElasticFileSystem.UpdateFileSystemRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**throughputMode** | **String** | (Optional) Updates the file system&#39;s throughput mode. If you&#39;re not updating your throughput mode, you don&#39;t need to provide this value in your request. If you are changing the &lt;code&gt;ThroughputMode&lt;/code&gt; to &lt;code&gt;provisioned&lt;/code&gt;, you must also set a value for &lt;code&gt;ProvisionedThroughputInMibps&lt;/code&gt;. | [optional] 
**provisionedThroughputInMibps** | **Number** | (Optional) Sets the amount of provisioned throughput, in MiB/s, for the file system. Valid values are 1-1024. If you are changing the throughput mode to provisioned, you must also provide the amount of provisioned throughput. Required if &lt;code&gt;ThroughputMode&lt;/code&gt; is changed to &lt;code&gt;provisioned&lt;/code&gt; on update. | [optional] 



## Enum: ThroughputModeEnum


* `bursting` (value: `"bursting"`)

* `provisioned` (value: `"provisioned"`)

* `elastic` (value: `"elastic"`)




