# AmazonSageMakerFeatureStoreRuntime.BatchGetRecordRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**[BatchGetRecordIdentifier]**](BatchGetRecordIdentifier.md) | A list containing the name or Amazon Resource Name (ARN) of the &lt;code&gt;FeatureGroup&lt;/code&gt;, the list of names of &lt;code&gt;Feature&lt;/code&gt;s to be retrieved, and the corresponding &lt;code&gt;RecordIdentifier&lt;/code&gt; values as strings. | 
**expirationTimeResponse** | **String** | Parameter to request &lt;code&gt;ExpiresAt&lt;/code&gt; in response. If &lt;code&gt;Enabled&lt;/code&gt;, &lt;code&gt;BatchGetRecord&lt;/code&gt; will return the value of &lt;code&gt;ExpiresAt&lt;/code&gt;, if it is not null. If &lt;code&gt;Disabled&lt;/code&gt; and null, &lt;code&gt;BatchGetRecord&lt;/code&gt; will return null. | [optional] 



## Enum: ExpirationTimeResponseEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




