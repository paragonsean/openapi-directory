# AwsArcZonalShift.UpdateZonalShiftRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string. | [optional] 
**expiresIn** | **String** | &lt;p&gt;The length of time that you want a zonal shift to be active, which Route 53 ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).&lt;/p&gt; &lt;p&gt;If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you&#39;re ready to restore traffic to the Availability Zone.&lt;/p&gt; &lt;p&gt;To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;A lowercase letter m:&lt;/b&gt; To specify that the value is in minutes.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;A lowercase letter h:&lt;/b&gt; To specify that the value is in hours.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example: &lt;code&gt;20h&lt;/code&gt; means the zonal shift expires in 20 hours. &lt;code&gt;120m&lt;/code&gt; means the zonal shift expires in 120 minutes (2 hours).&lt;/p&gt; | [optional] 


