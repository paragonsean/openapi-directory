

# StartZonalShiftRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**awayFrom** | **String** | The Availability Zone that traffic is moved away from for a resource when you start a zonal shift. Until the zonal shift expires or you cancel it, traffic for the resource is instead moved to other Availability Zones in the AWS Region. |  |
|**comment** | **String** | A comment that you enter about the zonal shift. Only the latest comment is retained; no comment history is maintained. A new comment overwrites any existing comment string. |  |
|**expiresIn** | **String** | &lt;p&gt;The length of time that you want a zonal shift to be active, which Route 53 ARC converts to an expiry time (expiration time). Zonal shifts are temporary. You can set a zonal shift to be active initially for up to three days (72 hours).&lt;/p&gt; &lt;p&gt;If you want to still keep traffic away from an Availability Zone, you can update the zonal shift and set a new expiration. You can also cancel a zonal shift, before it expires, for example, if you&#39;re ready to restore traffic to the Availability Zone.&lt;/p&gt; &lt;p&gt;To set a length of time for a zonal shift to be active, specify a whole number, and then one of the following, with no space:&lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;b&amp;gt;A lowercase letter m:&amp;lt;/b&amp;gt; To specify that the value is in minutes.&amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;li&amp;gt; &amp;lt;p&amp;gt; &amp;lt;b&amp;gt;A lowercase letter h:&amp;lt;/b&amp;gt; To specify that the value is in hours.&amp;lt;/p&amp;gt; &amp;lt;/li&amp;gt; &amp;lt;/ul&amp;gt; &amp;lt;p&amp;gt;For example: &amp;lt;code&amp;gt;20h&amp;lt;/code&amp;gt; means the zonal shift expires in 20 hours. &amp;lt;code&amp;gt;120m&amp;lt;/code&amp;gt; means the zonal shift expires in 120 minutes (2 hours).&amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt; |  |
|**resourceIdentifier** | **String** | &lt;p&gt;The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt; |  |



