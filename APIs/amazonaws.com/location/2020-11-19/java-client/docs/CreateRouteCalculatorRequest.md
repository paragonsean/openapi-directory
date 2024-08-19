

# CreateRouteCalculatorRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculatorName** | **String** | &lt;p&gt;The name of the route calculator resource. &lt;/p&gt; &lt;p&gt;Requirements:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Can use alphanumeric characters (A–Z, a–z, 0–9) , hyphens (-), periods (.), and underscores (_).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Must be a unique Route calculator resource name.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;No spaces allowed. For example, &lt;code&gt;ExampleRouteCalculator&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**dataSource** | **String** | &lt;p&gt;Specifies the data provider of traffic and road network data.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This field is case-sensitive. Enter the valid values as shown. For example, entering &lt;code&gt;HERE&lt;/code&gt; returns an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Valid values include:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Esri&lt;/code&gt; – For additional information about &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/esri.html\&quot;&gt;Esri&lt;/a&gt;&#39;s coverage in your region of interest, see &lt;a href&#x3D;\&quot;https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm\&quot;&gt;Esri details on street networks and traffic coverage&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Route calculators that use Esri as a data source only calculate routes that are shorter than 400 km.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Grab&lt;/code&gt; – Grab provides routing functionality for Southeast Asia. For additional information about &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html\&quot;&gt;GrabMaps&lt;/a&gt;&#39; coverage, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/grab.html#grab-coverage-area\&quot;&gt;GrabMaps countries and areas covered&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Here&lt;/code&gt; – For additional information about &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/HERE.html\&quot;&gt;HERE Technologies&lt;/a&gt;&#39; coverage in your region of interest, see &lt;a href&#x3D;\&quot;https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html\&quot;&gt;HERE car routing coverage&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html\&quot;&gt;HERE truck routing coverage&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For additional information , see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/location/latest/developerguide/what-is-data-provider.html\&quot;&gt;Data providers&lt;/a&gt; on the &lt;i&gt;Amazon Location Service Developer Guide&lt;/i&gt;.&lt;/p&gt; |  |
|**description** | **String** | The optional description for the route calculator resource. |  [optional] |
|**pricingPlan** | [**PricingPlanEnum**](#PricingPlanEnum) | No longer used. If included, the only allowed value is &lt;code&gt;RequestBasedUsage&lt;/code&gt;. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | &lt;p&gt;Applies one or more tags to the route calculator resource. A tag is a key-value pair helps manage, identify, search, and filter your resources by labelling them.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For example: { &lt;code&gt;\&quot;tag1\&quot; : \&quot;value1\&quot;&lt;/code&gt;, &lt;code&gt;\&quot;tag2\&quot; : \&quot;value2\&quot;&lt;/code&gt;}&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Format: &lt;code&gt;\&quot;key\&quot; : \&quot;value\&quot;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;Restrictions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Maximum 50 tags per resource&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Each resource tag must be unique with a maximum of one value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum key length: 128 Unicode characters in UTF-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Maximum value length: 256 Unicode characters in UTF-8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - &#x3D; . _ : / @. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Cannot use \&quot;aws:\&quot; as a prefix for a key.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



## Enum: PricingPlanEnum

| Name | Value |
|---- | -----|
| REQUEST_BASED_USAGE | &quot;RequestBasedUsage&quot; |
| MOBILE_ASSET_TRACKING | &quot;MobileAssetTracking&quot; |
| MOBILE_ASSET_MANAGEMENT | &quot;MobileAssetManagement&quot; |



