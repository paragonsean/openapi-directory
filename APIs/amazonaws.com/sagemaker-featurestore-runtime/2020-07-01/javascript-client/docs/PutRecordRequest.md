# AmazonSageMakerFeatureStoreRuntime.PutRecordRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | [**[FeatureValue]**](FeatureValue.md) | &lt;p&gt;List of FeatureValues to be inserted. This will be a full over-write. If you only want to update few of the feature values, do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;GetRecord&lt;/code&gt; to retrieve the latest record.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the record returned from &lt;code&gt;GetRecord&lt;/code&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use &lt;code&gt;PutRecord&lt;/code&gt; to update feature values.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**targetStores** | [**[TargetStore]**](TargetStore.md) | A list of stores to which you&#39;re adding the record. By default, Feature Store adds the record to all of the stores that you&#39;re using for the &lt;code&gt;FeatureGroup&lt;/code&gt;. | [optional] 
**ttlDuration** | [**PutRecordRequestTtlDuration**](PutRecordRequestTtlDuration.md) |  | [optional] 


