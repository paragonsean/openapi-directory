# AmazonOpenSearchService.StartServiceSoftwareUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainName** | **String** | The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an Amazon Web Services Region. | 
**scheduleAt** | **String** | &lt;p&gt;When to start the service software update.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NOW&lt;/code&gt; - Immediately schedules the update to happen in the current hour if there&#39;s capacity available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TIMESTAMP&lt;/code&gt; - Lets you specify a custom date and time to apply the update. If you specify this value, you must also provide a value for &lt;code&gt;DesiredStartTime&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;OFF_PEAK_WINDOW&lt;/code&gt; - Marks the update to be picked up during an upcoming off-peak window. There&#39;s no guarantee that the update will happen during the next immediate window. Depending on capacity, it might happen in subsequent days.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;NOW&lt;/code&gt; if you don&#39;t specify a value for &lt;code&gt;DesiredStartTime&lt;/code&gt;, and &lt;code&gt;TIMESTAMP&lt;/code&gt; if you do.&lt;/p&gt; | [optional] 
**desiredStartTime** | **Number** | The Epoch timestamp when you want the service software update to start. You only need to specify this parameter if you set &lt;code&gt;ScheduleAt&lt;/code&gt; to &lt;code&gt;TIMESTAMP&lt;/code&gt;. | [optional] 



## Enum: ScheduleAtEnum


* `NOW` (value: `"NOW"`)

* `TIMESTAMP` (value: `"TIMESTAMP"`)

* `OFF_PEAK_WINDOW` (value: `"OFF_PEAK_WINDOW"`)




