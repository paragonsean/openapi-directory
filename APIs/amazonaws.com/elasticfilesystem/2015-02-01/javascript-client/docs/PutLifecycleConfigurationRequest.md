# AmazonElasticFileSystem.PutLifecycleConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lifecyclePolicies** | [**[LifecyclePolicy]**](LifecyclePolicy.md) | &lt;p&gt;An array of &lt;code&gt;LifecyclePolicy&lt;/code&gt; objects that define the file system&#39;s &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object. A &lt;code&gt;LifecycleConfiguration&lt;/code&gt; object informs EFS lifecycle management and EFS Intelligent-Tiering of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;When to move files in the file system from primary storage to the IA storage class.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When to move files that are in IA storage to primary storage.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;When using the &lt;code&gt;put-lifecycle-configuration&lt;/code&gt; CLI command or the &lt;code&gt;PutLifecycleConfiguration&lt;/code&gt; API action, Amazon EFS requires that each &lt;code&gt;LifecyclePolicy&lt;/code&gt; object have only a single transition. This means that in a request body, &lt;code&gt;LifecyclePolicies&lt;/code&gt; must be structured as an array of &lt;code&gt;LifecyclePolicy&lt;/code&gt; objects, one object for each transition, &lt;code&gt;TransitionToIA&lt;/code&gt;, &lt;code&gt;TransitionToPrimaryStorageClass&lt;/code&gt;. See the example requests in the following section for more information.&lt;/p&gt; &lt;/note&gt; | 


